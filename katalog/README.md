# Tugas 2 Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Nama : Ied Mubaraque Sultan Salahuddine El Ayyubie
## NPM : 2106751120

**Link Heroku**
https://tugas2-ayyubie.herokuapp.com/katalog/

**Bagan request client ke web aplikasi berbasis Django**
![Gambar]('../../Bagan.png?raw=true')


Bagan / Pola request client ke web aplikasi berbasis Django diawali melalui permintaan masuk (request) dari Client (User) ke dalam server Django melalui Urls (urls.py). Kemudian request tersebut akan diarahkan ke halaman views.py yang telah di definisikan oleh developers untuk urls tersebut. Setelah request diterima oleh views.py, fungsi yang berada pada views.py akan dijalankan dengan memanfaatkan models.py sebagai penghubung apabila diperlukan keterlibatan database dengan memanfaatkan respon data (query) yang akan mengembalikan hasil dari query tersebut ke views.py. Apabila request dari Client (User) telah selesai diproses, maka hasil proses tersebut akan ditampilkan (render) ke dalam template (HTML) dan dikembalikan (return) ke Client (User) sebagai respon untuk ditampilkan.

## Virtual Environment
**Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Venv atau Virtual Environment merupakan environment manager yang disediakan oleh phyton sebagai alat untuk membuat scope virtual secara terisolasi. Virtual environment nantinya akan mengisolasi package dan dependecies dari aplikasi yang ada pada project, sehingga tidak terjadi crash dengan versi lain yang ada pada device. 

Venv akan memastikan seluruh data yang ada di library project tidak akan berubah pada storage local device dan hanya akan berubah di virtual environtment env. Hal tersebut dilakukan untuk mencegah perbedaan versi data pada project dikarenakan oleh perbedaan atau lebih dari satu versi Django yang berada pada device.

## Implementasi
**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

Views.py --> Implementasi Views.py adalah untuk mengambil semua data yang ada di database dengan menambahkan beberapa variable tambahan seperti nama dan npm yang akan disimpan melalui varibel context serta akan ikut di render saat pemanggilan fungsi show_catalog sehingga data tersebut juga akan terdapat pada template (HTML) 

Urls.py --> Implementasi Urls.py adalah dengan ditambahkan path('katalog/', include('katalog.urls')). Path tersebut berfungsi untuk Rounting '/katalog' dengan katalog/urls.py supaya menjalankan fungsi show_catalog yang terdapat pada katalog.views.py

katalog.html --> Program akan mengimplementasikan katalog.html untuk rendering, sehingga data pada katalog.html-lah yang akan digunakan untuk ditampilkan. Oleh karena itu, untuk menambahkan data tambahan berupa nama dan npm diperlukanlah curly bracket yang berisi variabel tersebut {{nama}} dan {{npm}}, serta program juga akan melakukan looping untuk mengambil data pada database yang akan disimpan ke dalam variabel list_catalog.

Deploy --> Implementasi deploy adalah untuk menghubungkan project secara realtime ke heroku dengan cara deploy melalui github. Deploy dapat dilakukan dengan menghubungkan (connect) repository github project dan akun heroku dengan menambahkan variabel HEROKU_APP_NAME dan HEROKU_API_KEY pada repositry secret.