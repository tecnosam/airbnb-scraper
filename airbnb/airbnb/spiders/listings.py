import scrapy
import json

from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.parse import parse_qs

from airbnb.items import Listing


class ListingsSpider(scrapy.Spider):
    name = 'listings'

    start_urls = ['http://airbnb.com/']


    base_url = "https://www.airbnb.com/api/v2/explore_tabs?"
    
    params = {
        "key": "d306zoyjsyarp7ifhu67rjxn52tv0t20",
        "selected_tab_id": "home_tab",
        "items_per_grid": 50,
        "max_total_count": 500,
        "place_id": "ChIJYSc_dD-e0ocR0NLf_z5pBaQ"
    }

    cities = {
        "Fayetteville": 0,
        "Rogers": 0,
        "Springdale": 0,
    }

    
    def gen_url(self, additional_params: dict = {}):
        
        return self.base_url + urlencode(self.params) + '&' + urlencode(additional_params)

    def parse(self, response):
        
        
        urls = []

        for city in self.cities.keys():

            new_url = self.gen_url({'query': city})

            print(f"\n\n\n{city}\n\n\n\n")

            yield scrapy.Request(url=new_url, callback=self.parse_page)


    def parse_page(self, response):

        data = json.loads(response.body)
        
        parsed_url = urlparse(response.url)

        city = parse_qs(parsed_url.query)['query'][0]

        # print(f"\n\nCITY{response.url} {city}\n\n")

        listings = data.get('explore_tabs')[0].get('sections')[-1].get('listings')

        for listing in listings:

            if self.cities[city] == 300:
                print(f"\n\nCITY{self.cities}\n\n")
                break

            yield self.extract_listing_info(listing, city)

            self.cities[city] += 1


        pagination_metadata = data.get('explore_tabs')[0].get('pagination_metadata')


        if pagination_metadata.get('has_next_page') and self.cities[city] < 300:

            params = {}
            params['items_offset'] = pagination_metadata.get('items_offset')
            params['section_offset'] = pagination_metadata.get('section_offset')

            params['query'] = city

            new_url = self.gen_url(params)

            yield scrapy.Request(url=new_url, callback=self.parse_page)
    
    
    def extract_listing_info(self, listing_row, city):
        
        
        pricing_quote = listing_row['pricing_quote']

        listing = listing_row['listing']

        data = {
            'listing_id': listing['id'],
            'name': listing['name'],
            'city': city,
            'state': "Arkansas",
            'country': "United States",
            'bedrooms': listing['bedrooms'],
            'beds': listing['beds'],
            'bathrooms': listing['bathrooms'],
            'accomodation_total': pricing_quote['structured_stay_display_price']['primary_line']['price'],
            'host_name': listing['user']['first_name'],
            'host_id': listing['user']['id'],
            'latitude': listing['lat'],
            'longitude': listing['lng'],
            'room_type': listing['room_type'],
            'picture_url': listing['picture_url'],
            'reviews_count': listing['reviews_count'],

            'amenities': listing['amenity_ids']
        }

        return Listing(data)
