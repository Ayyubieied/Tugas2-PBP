# Tugas 3 Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Nama : Ied Mubaraque Sultan Salahuddine El Ayyubie
## NPM : 2106751120

**Link Heroku**

HTML    : [Link HerokuApp HTML](https://tugas2-ayyubie.herokuapp.com/mywatchlist/html)

XML     : [Link HerokuApp XML](https://tugas2-ayyubie.herokuapp.com/mywatchlist/xml)

JSON    : [Link HerokuApp JSON](https://tugas2-ayyubie.herokuapp.com/mywatchlist/json)

--------------------------------------------------------------------------------------------------------------------

**1. Jelaskan perbedaan antara JSON, XML, dan HTML!**

Sebelum menjelaskan mengenai perbedaannya, kita perlu mengetahui definisi dari masing-masing tipe:

*Dikutip dari Wikipedia https://www.wikipedia.org/*
> **HTML (HyperText Markup Language)** adalah suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar

> **XML (Extensible Markup Language)** adalah bahasa markup untuk keperluan umum yang disarankan oleh W3C untuk membuat dokumen markup keperluan pertukaran data antar sistem yang beraneka ragam. XML merupakan kelanjutan dari HTML (HyperText Markup Language) yang merupakan bahasa standar untuk melacak Internet.

> **JSON (JavaScript Object Notation)** adalah sebuah format untuk menyimpan dan menukar informasi yang dapat dibaca oleh manusia.

Sehingga berdasarkan penjelasan tersebut, kita dapat mengetahui bahwa HTML (Hypertext Markup Language) dan XML (JavaScript Object Notation) merupakan sebuah *markup language* atau bahasa komputer yang biasanya menggunakan tags atau tanda. Meskipun keduanya merupakan sebuah *markup language*, tetapi HTML dan XML memiliki karakteristiknya tersendiri. HTML merupakan sebuah *markup language* yang menggunakan element tree untuk mewakilkan datanya dan dapat dimodifikasi tampilannya agar menghasilkan suatu tampilan secara benar (tampilan yang diinginkan oleh User). Sementara itu, XML merupakan *markup language* yang lebih difokuskan dan disarankan oleh W3C untuk keperluan data storage and delivery. Hal tersebut dikarenakan XML merupakan content driven dan HTML lebih ke format driven. Sehingga dapat kita simpulkan bahwa HTML lebih berfokus pada *data presentation* dan XML lebih fokus pada *data transfer*.

Sementara itu, JSON merupakan sebuah struktur data yang sederhana dan mudah dipahami. Struktur data JSON mewakili sebauah dictionary dengan 2 struktur utama, yaitu *keys* dan *values*, sehingga JSON dapat mempermudah penyimpanan data oleh komputer serta penukaran informasi dikarenakan struktur data yang mudah dipahami oleh manusia. JSON biasa digunakan untuk API dan pembuatan halaman website di mana informasinya dapat diperbarui tanpa harus memuat ulang halaman tersebut. Tidak adanya *tags* atau tanda pada struktur data JSON mempermudah proses *read* dan *write* pada komputer tetapi juga mempersulit user dikarenakan penulisan dalam format dictionary yang memberikan sedikit opsi saja dalam menampilkan data json, sehingga JSON lebih sering digunakan untuk *data transfer* sama seperti XML 


**2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery merupakan suatu kumpulan data yang tersedia dan dapat digunakan atau diperoleh User untuk menghasilkan suatu tampilan Struktur data yang diinginkan. Fleksibelitas tersebutlah yang membuat data delivery menjadi sebuah bagian penting pada pengimplementasian suatu platform. Dikarenakan dengan adanya data delivery, Data yang diambil dari database berdasarkan request user/browser dapat dirender menjadi sebuah output yang diinginkan pada website. Data delivery memungkinan output dari satu sumber data dapat berupa file HTML, XML, atau JSON sehingga developer memiliki fleksibelitas terhadap input data yang akan digunakan pada database dan output data yang dihasilkan berdasarkan tipe data yang diinginkan. Dengan adanya Data delivery seperti pada tugas 3 ini, mempermudah developer untuk melakukan modifikasi pada data dan mempermudah user dalam memahami data yang dirender.

**3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!**
- [x] Membuat suatu aplikasi baru bernama `mywatchlist` dengan menjalankan perintah `py manage.py startapp mywatchlist` pada file project Django Tugas 2
- [x] Menambahkan aplikasi `mywatchlist` kedalam variabel `INSTALLED_APPS` pada file `settings.py` di folder `project_django` 
- [x] Membuat skema Model pada file `models.py` di folder `mywatchlist` dengan atribut `watched, title, rating, release_date, review`
- [x] Menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal serta `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
- [x] Membuat folder baru bernama `fixtures` yang berisi sebuah berkas `mywatchlist_data.json` untuk menyimpan data yang ingin ditampilkan pada aplikasi
- [x] Menjalankan perintah `python manage.py loaddata mywatchlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.
- [x] Membuat sebuah fungsi yang menerima parameter `request` pada file `views.py` di folder `mywatchlist` dan mengembalikan `return render(request, "mywatchlist.html", context)` dengan context berupa pemberitahuan mengenai banyak film yang sudah atau belum ditonton serta Melakukan import Models yang telah dibuat ke dalam berkas `views.py` dengan melakukan import `from django.shortcuts import render` dan `from mywatchlist.models import MyWatchList`
- [x] Membuat folder baru bernama `template` yang berisi sebuah berkas `mywatchlist.html` untuk menjadi *template* dari aplikasi yang ingin dibuat
- [x] Membuat berkas `urls.py` pada folder `mywatchlist` untuk melakukan routing terhadap fungsi views yang telah dibuat, sehingga nantinya halaman HTML dapat ditampilkan lewat browser
- [x] Mendaftarkan path aplikasi `mywatchlist` kedalam berkas `urls.py` pada folder `project_django` dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada variabel `urlpatterns`
- [x] Melakukan *mapping* dari data yang diambil melalui `views.py` kedalam *template* dari aplikasi `mywatchlist.html`
- [X] Menambahkan import `HttpResponse` dan `Serializer` pada berkas `views.py` pada folder `mywatchlist` serta membuat dua buah fungsi baru yang menerima parameter `request` dan mengembalikan `return HttpResponse(serializers.serialize("xml", data_film), content_type="application/xml")` untuk tipe XML dan `return HttpResponse(serializers.serialize("json", data_film), content_type="application/json")` untuk tipe json
- [x] Melakukan import `from mywatchlist.views import mywatchlist_xml, mywatchlist_json` dan Menambahkan dua buah *path url* baru kedalam berkas `urls.py` pada folder `mywatchlist` untuk mengakses fungsi baru yang telah diimport `path('xml/', mywatchlist_xml, name='mywatchlist_xml'),` untuk tipe XML dan `path('json/', mywatchlist_json, name='mywatchlist_json'),` untuk tipe JSON
- [x] Menambahkan tiga function di berkas `test.py` pada folder `mywatchlist` untuk melakukan *testing* dari setiap urls (HTML, XML, JSON) dan mengembalikan respon `HTTP 200 OK`
- [x] Mengakses ketiga tipe aplikasi dengan urls nya masing-masing (HTML, XML, JSON) melalui kolom *request* Postman, kemudian Postman akan mengembalikan hasil berupa file HTML, XML, atau JSON dari website beserta status codenya

<h3 align="center">Postman HTML</h3>

![MyWatchList_HTML]('../../MyWatchList_HTML.png?raw=true')

<h3 align="center">Postman XML</h3>

![MyWatchList_XML]('../../MyWatchList_XML.png?raw=true')

<h3 align="center">Postman JSON</h3>

![MyWatchList_JSON]('../../MyWatchList_JSON.png?raw=true')

**REFERENSI**

1. https://docs.oracle.com/en/cloud/saas/data-cloud/data-cloud-help-center/IntegratingBlueKaiPlatform/data_delivery.html

2. https://id.wikipedia.org/wiki/HTML

3. https://id.wikipedia.org/wiki/XML

4. https://id.wikipedia.org/wiki/JSON

5. https://www.petanikode.com/markdown-pemula/


