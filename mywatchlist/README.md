# Tugas 3 Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Nama : Ied Mubaraque Sultan Salahuddine El Ayyubie
## NPM : 2106751120

**Link Heroku**
HTML    : [Link HerokuApp HTML](https://tugas2-ayyubie.herokuapp.com/mywatchlist/html)
XML     : [Link HerokuApp XML](https://tugas2-ayyubie.herokuapp.com/mywatchlist/xml)
JSON    : [Link HerokuApp JSON](https://tugas2-ayyubie.herokuapp.com/mywatchlist/json)

**1. Jelaskan perbedaan antara JSON, XML, dan HTML!**

**2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

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

<h3 align="center">**Postman HTML**</h3>

![MyWatchList_HTML]('../../MyWatchList_HTML.png?raw=true')

<h3 align="center">**Postman XML**</h3>

![MyWatchList_XML]('../../MyWatchList_XML.png?raw=true')

<h3 align="center">**Postman JSON**</h3>

![MyWatchList_JSON]('../../MyWatchList_JSON.png?raw=true')


