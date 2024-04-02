import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess


class BookingSpider(scrapy.Spider):
    name = "booking"
    start_urls = ["https://www.booking.com/"]

    def parse(self, response):
        # Définir les XPaths pour chaque élément
        city_name_xpath = "//div[@class='bui-destination-header__main-content']/h1/text()"
        city_location_xpath = "//div[@class='bui-destination-header__sub-content']/span/text()"

        # Extraire les noms et les localisations des villes
        for city in ["Mont Saint Michel", "St Malo", "Bayeux", "Le Havre", "Rouen", "Paris"]:
            # Remplacer les espaces par des tirets dans le nom de la ville pour l'utiliser dans l'XPath
            city_name_xpath_formatted = city_name_xpath.replace(" ", "-")

            # Extraire le nom de la ville
            city_name = response.xpath(city_name_xpath_formatted).get()

            # Extraire la localisation de la ville
            city_location = response.xpath(city_location_xpath).get()

            # Afficher les résultats
            yield {
                "city_name": city_name,
                "city_location": city_location,
            }


# Name of the file where the results will be saved
filename = "booking.json"

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