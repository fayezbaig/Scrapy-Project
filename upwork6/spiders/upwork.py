import scrapy
from upwork6.items import Upwork6Item


class UpworkSpider(scrapy.Spider):
    name = "upwork"
    allowed_domains = ["www.worldcitydb.com"]
    start_urls = ["https://www.worldcitydb.com/search-by-country?lang=en_US"]

    def parse(self, response):

        country_table = response.css('table tr table tr')

        for country in country_table:

            country_name = country.css('td a::text').get()

            url = country.css('td a::attr(href)').get()

            yield response.follow(url, callback= self.parse_regions, meta={'country_name': country_name})


    def parse_regions(self,response):

        regions_table = response.css('div.panel-body div.col-md-12 table tr table tr')

        country_name = response.meta.get('country_name') 

        for regions in regions_table:

            region_name = regions.css('td a::text').get()

            self.parse_cities(region_name)

            url2 = regions.css('td a::attr(href)').get()

            yield response.follow(url2,callback = self.parse_cities, meta={'region_name': region_name, 'country_name': country_name})

    def parse_cities(self,response):

        site_item = Upwork6Item()

        cities_table = response.css('table tr table tr')

        region_name = response.meta.get('region_name')

        country_name = response.meta.get('country_name')        

        for city in cities_table:

            
            site_item['country_name'] = country_name.strip()
            site_item['region_name'] = region_name.strip()
            site_item['cities_name'] = city.css('td a::text').get().strip()

            yield site_item
            

        next_pages_urls = response.css('ul.pagination li')

        for next_page in next_pages_urls:

            try:
                url3 = next_page.css('a::attr(href)').get()
                yield response.follow(url3, callback = self.parse_cities, meta={'region_name': region_name, 'country_name': country_name})
            except:
                pass

        


