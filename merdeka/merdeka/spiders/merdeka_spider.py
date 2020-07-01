# run "scrapy crawl merdeka -o merdeka.csv" on terminal
# csv karena lebi nyaman dgn excel things

import scrapy

class MerdekaSpider(scrapy.Spider):
    name = "merdeka"

    # satu satu karena mager implementasi utk di auto in 🙏
    # dan karena fungsi utamanya mendapatkan dataset, 
    # jadi dipilih yang cocok
    start_urls = [
        "https://www.merdeka.com/uang/umkm-sumbang-61-persen-ke-pdb-tapi-nilai-ekspor-umkm-masih-rendah.html",
        "https://www.merdeka.com/uang/bantu-penanganan-corona-aice-group-sebar-apd-untuk-13-rumah-sakit-rujukan.html",
        "https://www.merdeka.com/uang/mei-2020-kunjungan-turis-ke-indonesia-hanya-163000-orang.html",
        "https://www.merdeka.com/uang/pemerintah-tetap-cairkan-rp-429-m-renovasi-rumah-di-5-kspn-prioritas-untuk-homestay.html",
        "https://www.merdeka.com/uang/pertumbuhan-ekonomi-dunia-diprediksi-negatif-di-kuartal-ii-2020-termasuk-ri.html",
        "https://www.merdeka.com/uang/dpr-setuju-pemerintah-cicil-utang-ke-pupuk-indonesia-rp57-triliun-tahun-ini.html",
        "https://www.merdeka.com/uang/bos-ojk-harap-penempatan-dana-rp30-triliun-ke-bank-himbara-bantu-pulihkan-ekonomi.html",
        "https://www.merdeka.com/uang/tak-dilunasi-sejak-2017-utang-pemerintah-ke-pupuk-indonesia-bengkak-jadi-rp171-t.html",
        "https://www.merdeka.com/uang/dampak-corona-produksi-rokok-diprediksi-turun-hingga-23-persen.html",
        "https://www.merdeka.com/uang/bank-indonesia-catat-kepemilikan-sbn-per-23-juni-rp-4475-triliun.html",
        "https://www.merdeka.com/uang/indeks-kesiapan-digital-umkm-di-jabodetabek-masih-tahap-menengah-ini-penyebabnya.html",
        "https://www.merdeka.com/uang/pemerintah-siapkan-umkm-masuk-pengadaan-barang-bumn-dengan-proyek-di-bawah-rp14-m.html",
        "https://www.merdeka.com/uang/rupiah-melemah-ke-rp14220usd-dipicu-kekhawatiran-meningkatnya-penyebaran-covid-19.html",
        "https://www.merdeka.com/uang/lman-danai-pembebasan-lahan-proyek-psn-senilai-rp533-triliun.html",
        "https://www.merdeka.com/uang/bank-indonesia-ramal-inflasi-juni-2020-sebesar-minus-001-persen.html",
        "https://www.merdeka.com/uang/data-kadin-catat-64-juta-orang-di-phk-dan-dirumahkan-hingga-mei-2020.html",
        "https://www.merdeka.com/uang/pengunjung-mal-hanya-40-persen-pengelola-minta-pemerintah-bantu-soal-kelistrikan.html",
        "https://www.merdeka.com/uang/data-kadin-catat-64-juta-orang-di-phk-dan-dirumahkan-hingga-mei-2020.html",
        "https://www.merdeka.com/uang/nilai-tukar-rupiah-melemah-dipicu-kekhawatiran-potensi-gelombang-kedua-covid-19.html",
        "https://www.merdeka.com/uang/jalankan-program-rehabilitasi-hutan-klhk-minta-tambahan-anggaran-rp53-triliun.html",
        "https://www.merdeka.com/uang/per-24-juni-blt-dana-desa-sudah-tersalur-ke-69424-desa-dengan-nilai-rp43-triliun.html",
        "https://www.merdeka.com/uang/360818-wajib-pajak-telah-disetujui-permohonan-insentif-pajaknya.html",
        "https://www.merdeka.com/uang/jasindo-salurkan-dana-kemitraan-rp2446-miliar-untuk-umkm-di-2020.html",
        "https://www.merdeka.com/uang/imf-kembali-pangkas-proyeksi-pertumbuhan-ekonomi-global-jadi-minus-49-persen.html",
        "https://www.merdeka.com/uang/tingkatkan-daya-saing-global-ikm-gula-palma-terapkan-teknologi-industri-40.html"
    ]

    def parse(self, response):
        for content in response.css("div.mdk-body-detail"):
            yield {
                'judul': content.css("div.mdk-dt-headline h1::text").get(),
                'berita': content.css("div.mdk-body-detail p::text").getall()
            }
