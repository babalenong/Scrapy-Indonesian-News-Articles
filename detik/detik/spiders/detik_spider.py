# run "scrapy crawl detik -o detik.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class DetikSpider(scrapy.Spider):
    name = "detik"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
        "https://finance.detik.com/berita-ekonomi-bisnis/5064934/ada-42-juta-pns-di-ri-kebanyakan-cuma-jadi-admin",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5065025/bkpm-minta-tambahan-anggaran-rp-509-m-di-2021-ini-alokasinya",
        "https://finance.detik.com/energi/d-5064740/anggaran-dipangkas-pembangunan-jargas-berkurang-jadi-127-ribu",
    ]

    def parse(self, response):
        for content in response.css("article.detail.itp_bodycontent"):
            yield {
                'judul': content.css("h1.detail__title::text").get(),
                'berita': content.css("div.detail__body p::text").getall()
            }
