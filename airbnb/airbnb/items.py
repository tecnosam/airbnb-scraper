# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Listing(scrapy.Item):

    listing_id = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    beds = scrapy.Field()
    accomodation_total = scrapy.Field()

    host_name = scrapy.Field()
    host_id = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    room_type = scrapy.Field()

    picture_url = scrapy.Field()

    amenities: list = scrapy.Field()

    # rating: RatingItem


class RatingItem(scrapy.Item):
    
    accuracy = scrapy.Field()
    checkin = scrapy.Field()
    cleanliness = scrapy.Field()
    communication = scrapy.Field()
    location = scrapy.Field()
    overall_rating = scrapy.Field()
    review_count = scrapy.Field()
