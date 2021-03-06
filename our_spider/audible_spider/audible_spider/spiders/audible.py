import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'audible'
    allowed_domains = ['www.audible.com']
    #start_urls = ['https://www.audible.com/search/']
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.audible.com/search/', callback=self.parse,
                       headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})

    def parse(self, response):
        # Getting the box that contains all the info we want (title, author, length)
        product_container = response.xpath('//div[@class="adbl-impression-container "]/li')

        # Looping through each product listed in the product_container box
        for product in product_container:
            book_title = product.xpath('.//h3[contains(@class , "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class , "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class , "runtimeLabel")]/span/text()').get()
            
            book_author_string = ' '.join(book_author)

            # Return data extracted
            yield {
                'title':book_title,
                'author':book_author_string,
                'length':book_length,
            }

        # Getting the pagination bar (pagination) and then the link within the next page button (next_page_url)
        pagination = response.xpath('//ul[contains(@class , "pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class , "nextButton")]/a/@href').get()

        # Going to the "next_page_url" link
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse, 
                    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})
