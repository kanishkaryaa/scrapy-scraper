import scrapy


class Spider1Spider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["worldometers.info"]
    start_urls = ["https://worldometers.info/world-population/population-by-country/"]

    def parse(self, response):

        rows = response.xpath('//tr')


        for row in rows:
           #title = response.xpath("//h1/text()").get()
            countries = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()
            yield {
                #'titles':title,
                'countries':countries,
                'population':population,
            }
