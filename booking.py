import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess


class BookingSpider(scrapy.Spider):
    name = "booking"
    
    start_urls = ['https://www.booking.com/searchresults.fr.html?ss=Paris&checkin=2024-04-02&checkout=2024-04-05&group_adults=2&no_rooms=1&group_children=0']

       
    # Parse function for login
    def parse(self, response):
        print('####: RESPONSE = ')
        print(response)
        quotes = response.xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div[2]')
        for quote in quotes:
            return {
                'hotel': quote.xpath('div[4]/div[3]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]/text()').get()
            }
        


# Name of the file where the results will be saved
filename = "booking3.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('src/'):
        os.remove('src/' + filename)


process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'src/' + filename: {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(BookingSpider)
process.start()