import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"
    allowed_domains = "https://books.toscrape.com"
    start_urls = [
       "https://books.toscrape.com/index.html"
    ]

    def parse(self, response):
        pass