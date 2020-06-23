import scrapy

class DetikSpider(scrapy.Spider):
    name = "detik"
    # satu satu karena mager implementasi utk auto browse dan 
    # ambil yg baru, tapi bisa kok pake scrapy 🙏
    start_urls = [
        "https://finance.detik.com/berita-ekonomi-bisnis/5064934/ada-42-juta-pns-di-ri-kebanyakan-cuma-jadi-admin"
    ]

    def parse(self, response):
        for content in response.css('div.detail_content'):
            yield {
                'judul': content.css('div.jdl h1::text').get(),
                'berita': response.css("div.itp_bodycontent p::text").getall(),
            }