# Tugas 4 Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Nama : Ied Mubaraque Sultan Salahuddine El Ayyubie
## NPM : 2106751120

**Link Heroku** : [Link HerokuApp](https://tugas2-ayyubie.herokuapp.com/todolist/)

**1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?**

Dikutip dari synopsys.com *A CSRF token is a secure random token (e.g., synchronizer token or challenge token) that is used to prevent CSRF attacks. The token needs to be unique per user session and should be of large random value to make it difficult to guess. A CSRF secure application assigns a unique CSRF token for every user session.* 

Sehingga dapat kita ketahui bahwa ``{% csrf_token %}`` merupakan sebuah token unik/random yang dibuat untuk setiap user session, berisi value yang bersifat rahasia serta sangat besar sehingga tidak dapat diprediksi. Token ini berguna untuk mencegah dari terjadinya CSRF (Cross-site Request Forgery) attack. pada elemen <form> sendiri, terdapat dua token ``{% csrf_token %}`` yang dibuat, yaitu ketika pengguna memasuki laman <form> dan setelah dikembalikan request dari pengguna ketika mengumpulkan (submit) data pada <form>. Cara kerja dari token tersebut adalah dengan membandingkan isi dari kedua token tersebut, apabila salah satu token memiliki value yang berbeda, maka request yang dibuat oleh user akan ditolak dan user session akan dihapus serta dicatat pada log sebagai potensi CSRF Attack.

Apabila <form> tidak memiliki ``{% csrf_token %}``, maka akan muncul error berupa *Forbidden (403) CSRF verification failed. Request aborted.*. Oleh karena itu diperlukan ``{% csrf_token %}`` pada setiap <form> yang dibuat pada suatu website untuk mencegah terjadinya CSRF Attack.

**2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.**

Ya, Elemen <form> dapat dibuat secara manual tanpa menggunakan generator seperti {{ form.as table }}. Elemen <form> tersebut dapat dibuat dengan memanfaatkan method POST. Pada saat pembuatan, perlu juga untuk ditambahkan ``{% csrf_token %}`` untuk mencegah terjadinya CSRF Attack dan error saat menjalankan program. Langkah-langkah yang diperlukan untuk membuat form secara manual, yaitu dengan membuat tag input dan tag form yang dibutuhkan pada HTML. Tag form berfungsi untuk membuat HTML form yang kemudian dapat digunakan untuk mendapatkan input dari user. Sementara tag input sendiri digunakan untuk menampung input yang diberikan oleh user. Input sendiri memiliki banyak tipe, seperti image, text, dan lainnya, tetapi dalam pembuatan form, salah satu contohnya pada tugas 4 ini, hanya diperlukan dua tipe input yaitu tipe text (untuk menampung input dari User) serta tipe submit (untuk submit data dari input User). Pengguna dapat memasukkan data yang diinginkan pada text box yang disediakan dan kemudian menekan input submit yang berupa tombol yang akan mengirim input yang sudah diisi oleh user ke server.

**3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

User akan memasukkan data melalui form HTML yang telah dirender, kemudian data tersebut dapat dikumpulkan (submit) menggunakan tombol submit yang berada pada interface. Setelah itu, pada berkas (file) views.py function yang berperan dalam mengakses form (add_task(request)) akan mengolah data-data baru tersebut. Kemudian, data tersebut akan di cek didalam database ketersediannya. Apabila data tersebut merupakan data baru yang belum ada pada database, maka data tersebut akan dibuat menjadi objek baru yang akan disimpan pada database. Akan tetapi, apabila data tersebut sudah ada pada data base dan hanya mengubah bagian-bagian yang terdapat pada data yang sudah ada, maka data lama tersebut akan "ditimpa" oleh data baru. Data-data yang sudah tersimpan pada database kemudian akan diakses kembali untuk dapat ditampilkan pada HTML setelah proses rendering.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

[x] Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya dengan menjalankan program ``python manage.py startapp todolist`` pada direktori cmd.

[x] Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.

[x] Membuat sebuah model Task yang memiliki atribut user, date, title, description dengan fields sesuai dengan ketentuan.

[x] Mengimplementasikan form registrasi, login, dan logout dengan mengimplementasikan 3 fungsi yaitu register, login_user, dan logout_user pada ``views.py`` untuk menghandle logic register, login, dan logout. Serta membuat 2 template HTML bernama ``login.html`` dan ``register.html`` agar pengguna dapat menggunakan to do list dengan baik.

[x] Membuat halaman utama todolist dengan mengimplementasikan ``todolist.html`` yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel yang menampilkan isi dari ``show_todolist`` yang berisi tanggal pembuatan task, judul task, dan deskripsi task.

[x] Membuat sebuah template HTML bernama ``add.html`` untuk ditampilkan ke user ketika akan membuat task baru. Selanjutnya, menambahkan sebuah fungsi add_task pada ``views.py`` untuk menghandle logic pembuatan model task yang baru.

[x] Membuat routing untuk mengakses fungsi-fungsi yang bersangkutan di ``views.py`` dengan menambahkan path url yang sesuai pada ``urls.py``.

[x] Melakukan deployment ke Heroku 

[x] Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku

~ Akun Dummy Pertama ~
- Username : ied.mubaraque

- Password : sultanied25

![Dummy1]('../../dummy1.png?raw=true')

~ Akun Dummy Pertama ~
- Username : ayyubie

- Password : sultanied25

![Dummy2]('../../dummy2.png?raw=true')


