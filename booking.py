import re
from urllib.parse import unquote
import unicodedata
import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import utils

class BookingLogin(scrapy.Spider):
    name = "booking"
                                                        
    """
    start_urls = ['https://www.booking.com/searchresults.fr.html?ss=Bretagne&order=review_score_and_price&dest_id=791&dest_type=region&lang=fr&ac_langcode=fr&checkin=2024-04-04&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0',
    'https://www.booking.com/searchresults.fr.html?ss=Annecy&dest_id=-1407760&dest_type=city&lang=fr&ac_langcode=fr&checkin=2024-04-04&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0',
    'https://www.booking.com/searchresults.fr.html?ss=Paris&dest_id=-1456928&dest_type=city&lang=fr&ac_langcode=fr&checkin=2024-04-04&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0']
    """
    top_dest = utils.urls_ville[:5]
    start_urls = top_dest[]
    def parse(self, response):
        url=response.request.url
                                                           
        appts = response.xpath('//div[@class ="d4924c9e74"]//div[@aria-label = "Établissement"][position() < 11]')        
        for appt in appts:
          yield {
            'dest' : (re.split('=',url)[1].split('&')[0]),
            'hostel': (appt.xpath('.//div[@data-testid = "title"]/text()').get()),
            #'price' : (appt.xpath('.//div[contains(@data-testid, "availability-rate-information")]//span/text()').get()),
            'website' :(appt.xpath('.//a/@href').get()),
            'score': (appt.xpath('.//div[contains(@data-testid,"rating-")]/ancestor::div[@tabindex = "0"]/@aria-label').get()),
            #'desc' : (appt.xpath('.//div[@data-testid = "recommended-units"]//div//h4/text()').get()) 
            'desc' :  appt.xpath('.//div[@class = "abf093bdfe"]/text()').get() 
          }        
                    
filename = "booking.json"
if filename in os.listdir('out/'):
        os.remove('out/' + filename)
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
         ('out/') + filename: {"format": "json",
                            "encoding" : "UTF-8"},
                          
    }
})
process.crawl(BookingLogin)
process.start()