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
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5073805/pendapatan-kai-anjlok-dari-rp-23-m-tinggal-rp-300-jutahari",
        "https://finance.detik.com/bursa-dan-valas/d-5073851/kuartal-i-2020-pendapatan-lippo-karawaci-tembus-rp-31-t",
        "https://finance.detik.com/moneter/d-5073479/dapat-rp-30-t-bank-bumn-harus-genjot-kredit-3-kali-lipat?single=1",
        "https://finance.detik.com/energi/d-5072401/total-utang-pemerintah-ke-pertamina-tembus-rp-96-triliun",
        "https://finance.detik.com/bursa-dan-valas/d-5072182/rupiah-menguat-tipis-dolar-as-turun-ke-14209",
        "https://finance.detik.com/bursa-dan-valas/d-5069331/waskita-terima-pembayaran-tol-japek-layang-dan-lrt-palembang-rp-6-t",
        "https://finance.detik.com/infrastruktur/d-5066707/basuki-minta-rp-280-m-buat-tangani-lumpur-lapindo",
        "https://finance.detik.com/infrastruktur/d-5066584/bangun-tol-trans-sumatera-771-km-hutama-karya-tarik-utang-rp-12-t?single=1",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5066522/perusahaan-korsel-dan-singapura-bikin-lab-corona-di-bandara-kalimantan?single=1",
        "https://finance.detik.com/moneter/d-5066510/titipkan-rp-30-t-ke-bank-bumn-sri-mulyani-beri-bunga-murah",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5066485/kai-catat-kenaikan-volume-penumpang-ka-reguler-hingga-49",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5078770/dilelang-untuk-bantuan-covid-19-jaket-ini-laku-rp-88-juta?tag_from=wp_nhl_2",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5064177/ancaman-pengangguran-tembus-12-juta-orang-di-depan-mata",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5066351/perpajakan-ditargetkan-tumbuh-105-di-2021-bagaimana-caranya",
        "https://finance.detik.com/bumn/d-5066282/di-tengah-gelombang-phk-bumn-ini-rekrut-1490-karyawan-baru",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5066241/dapat-suntikan-rp-11-t-laba-hutama-karya-diprediksi-turun-50",
        "https://finance.detik.com/infrastruktur/d-5066180/basuki-minta-rp-112-t-buat-kebut-proyek-stadion-piala-dunia-u-20",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5066179/pertama-kali-penerimaan-perpajakan-ri-minus-92",
        "https://finance.detik.com/berita-ekonomi-bisnis/d-5066155/tenaga-medis-gugur-tangani-corona-dapat-santunan-hingga-rp-341-juta",
        "https://finance.detik.com/infrastruktur/d-5066151/hk-masih-butuh-rp-51-t-rampungkan-771-km-tol-trans-sumatera",
        "https://finance.detik.com/industri/d-5079048/kalung-antivirus-corona-buatan-ri-diproduksi-massal-bulan-depan?tag_from=wp_nhl_3",
        "https://finance.detik.com/bursa-dan-valas/d-5066012/umumkan-ios-14-saham-apple-diprediksi-melejit-10"
    ]

    def parse(self, response):
        for content in response.css("article.detail.itp_bodycontent"):
            yield {
                'judul': content.css("h1.detail__title::text").get(),
                'berita': content.css("div.detail__body p::text").getall()
            }
