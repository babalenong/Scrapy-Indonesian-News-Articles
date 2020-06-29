# run "scrapy crawl kompas -o kompas.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class KompasSpider(scrapy.Spider):
    name = "kompas"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
        "https://money.kompas.com/read/2020/06/29/142550626/tergerus-ponsel-bagaimana-produsen-kamera-digital-bertahan?page=all#page2",
        "https://money.kompas.com/read/2020/06/29/151814026/selama-psbb-penjualan-pertamina-anjlok-hingga-50-persen"
    ]

    def parse(self, response):
        for content in response.css("div.container.clearfix"):
            yield {
                'judul': content.css("h1.read__title::text").get(),
                'berita': content.css("div.read__content p::text").getall()
            }
