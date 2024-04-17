import re
import os 
import logging
import scrapy
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import utils
import my_key as key
import pandas as pd
import os

AWS_ACCESS_KEY_ID = "key.aws_access_key_id"
AWS_SECRET_ACCESS_KEY ="key.aws_secret_access_key"
REGION_NAME = "eu-west-3"

class BookingSpider(scrapy.Spider):
    name = "Hostels"
    start_urls = utils.url_villes
    def parse(self, response):
        url=response.request.url
        #liste des hôtels par ville = 20
        hostels = response.xpath('//div[@class ="d4924c9e74"]//div[@aria-label = "Établissement"][position() < 21]')    
        for hostel in hostels:
            ville = (re.split('=',url)[1].split('&')[0])
            hostel_name = hostel.xpath('.//div[@data-testid = "title"]/text()').get()
            website = hostel.xpath('.//a/@href').get()
            score = hostel.xpath('.//div[contains(@data-testid,"rating-")]/ancestor::div[@tabindex = "0"]/@aria-label').get()
            
            #desc a changé sur le site, ci-dessous old :
            #'desc' : (hostel.xpath('.//div[@data-testid = "recommended-units"]//div//h4/text()').get()) 
            desc = hostel.xpath('.//div[@class = "abf093bdfe"]/text()').get()
            
            #TODO : prix par défaut en $, il faut changer la devise et récupérer en EUR
            #'price' : (hostel.xpath('.//div[contains(@data-testid, "availability-rate-information")]//span/text()').get()),
           
            #on garde les informations pour le 2e spider
            part_detail = {
              "ville" : ville,
              "name" : hostel_name,
              "website" : website,
              "score" : score,
              "desc" : desc
              }
            #lien vers la page de localisation de l'h$otel            
            hostel_detail_url = hostel.xpath('.//div[@class = "abf093bdfe ecc6a9ed89"]//a').attrib["href"]
            try:
              yield scrapy.Request(url = hostel_detail_url, callback=self.parse_HostelMap, meta={'part_detail' : part_detail})
            except KeyError:
              logging.info("Hostel's location page not accessible.")
              #TO DO : renvoyer les gps de la ville à la place
              lat = ''
              lon =''
            else:
              {}

    def parse_HostelMap(self, response):
        #données GPS sont dans la balise <a>
        a_tag = response.xpath(".//a/@data-atlas-latlng").get()     
        lat = re.split(',',a_tag)[0]
        lon = re.split(',',a_tag)[1]
        meta = response.request.meta
        #on enlève le 1er niveau du dict provenant de meta (part_detail) pour ne pas polluer la sortie
        hostel_detail = meta['part_detail']
        hostel_detail['lat'] = lat
        hostel_detail['lon'] = lon
        yield hostel_detail 
          
filename = "booking.json"
if filename in os.listdir('fichier_final/'):
  os.remove('fichier_final/' + filename)
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
         ('fichier_final/') + filename: {"format": "json",
                            "encoding" : "UTF-8"},                          
    }
})
process.crawl(BookingSpider)
process.start()