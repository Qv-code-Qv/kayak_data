#from urllib.parse import unquote
#import unicodedata
import re
import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import utils

class BookingLogin(scrapy.Spider):
    name = "booking"
    start_urls = utils.start_urls
    def parse(self, response):
        url=response.request.url                                                           
        appts = response.xpath('//div[@class ="d4924c9e74"]//div[@aria-label = "Établissement"][position() < 21]')        
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
book = BookingLogin
process.crawl(book)
process.start()