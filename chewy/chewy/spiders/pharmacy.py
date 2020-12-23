import scrapy


class PharmacySpider(scrapy.Spider):
    name = 'pharmacy'
    allowed_domains = ['www.chewy.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.chewy.com/b/pharmacy-2515', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        })

    def parse(self, response):
        products = response.xpath('//section[@class="results-products js-tracked-product-list"]/article[@class="product-holder js-tracked-product  cw-card cw-card-hover"]')

        for product in products:
            yield {
                'brand': product.xpath('.//div[@class="content"]/h2/strong/text()').get(),
                'title': product.xpath('.//div[@class="content"]/h2/text()').extract(),
                'url': response.urljoin(product.xpath(".//a[@class='product']/@href").get()),
                'autoship_price': product.xpath('.//p[@class="autoship"]/strong/text()').get(),
                'price': product.xpath('.//p[@class="price"]/strong/text()').get(),
                'old_price': product.xpath('.//p[@class="price"]/span[@class="price-old"]/text()').get(),
                'rating': product.xpath('.//p[@class="rating item-rating"]/span/text()').get()
            }

        next_page = response.xpath('.//a[@class="pagination_selection cw-pagination__next "]/@href').get()
        domain_url = 'https://www.chewy.com'

        if next_page:
            next_page = domain_url + next_page
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            })
