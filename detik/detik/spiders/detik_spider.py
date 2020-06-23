import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://finance.detik.com/berita-ekonomi-bisnis/5064934/ada-42-juta-pns-di-ri-kebanyakan-cuma-jadi-admin"
    ]

    def parse(self, response):
        for content in response.css('div.detail_content'):
            yield {
                'judul': content.css('div.jdl h1::text').get(),
                'berita': content.css('small.author::text').get(),
            }