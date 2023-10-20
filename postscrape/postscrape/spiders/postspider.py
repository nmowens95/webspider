import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"
    allowed_domains = "https://books.toscrape.com"
    start_urls = [
       "https://books.toscrape.com/index.html"
    ]

    def parse(self, response):
         # gets each book on the page
         book = response.css("article.product_pod")

        # we are going to loop through each book on the page obtaining our information
         for b in book:
            yield {
                "name" : b.css("h3 a::text").get(),
                "price" : b.css(".product_price .price_color::text").get(),
                "url" : b.css(".image_container a").attrib["href"],
            }

            next_page = response.css("li.next a ::attr(href)").get()

            if next_page is not None:
                if "catalogue/" in next_page:
                    next_page_url = "https://books.toscrape.com/" + next_page
                else:
                    next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            yield response.follow(next_page_url, callback = self.parse)