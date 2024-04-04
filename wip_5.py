import re
from urllib.parse import unquote
import unicodedata

# Import os => Library used to easily manipulate operating systems
## More info => https://docs.python.org/3/library/os.html
import os 

# Import logging => Library used for logs manipulation 
## More info => https://docs.python.org/3/library/logging.html
import logging

# Import scrapy and scrapy.crawler 
import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesLogin(scrapy.Spider):
    # Name of your spider
    name = "login"

    # Starting URL
    start_urls = ['https://www.booking.com/searchresults.fr.html?dest_id=791&dest_type=region&lang=fr&ac_langcode=fr&checkin=2024-04-04&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0',]
    #'https://www.booking.com/searchresults.fr.html?dest_id=204055&dest_type=landmark&lang=fr&ac_langcode=fr&checkin=2024-04-04&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0',
    #'https://www.booking.com/searchresults.fr.html?dest_id=-1456928&dest_type=city&lang=fr&ac_langcode=fr&checkin=2024-04-04&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0']

    # Parse function for login
    def parse(self, response):
        url=response.request.url
        quotes = response.xpath('//div[@class ="d4924c9e74"]//div[@aria-label = "Établissement"][position() < 11]')        
        for quote in quotes:
          yield {
            'dest' : re.split('&',url[51:61])[0],
            'hotel': (quote.xpath('.//div[@data-testid = "title"]/text()').get())
          }
        
# Name of the file where the results will be saved
filename = "4_quotesauthentication.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('src/'):
        os.remove('src/' + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'src/' + filename: {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(QuotesLogin)
process.start()