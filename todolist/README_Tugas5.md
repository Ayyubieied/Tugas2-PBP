# Tugas 4 Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Nama : Ied Mubaraque Sultan Salahuddine El Ayyubie
## NPM : 2106751120

**Link Heroku** : [Link HerokuApp](https://tugas2-ayyubie.herokuapp.com/todolist/)

**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

1. Inline CSS --> Inline CSS merupakan Kode CSS yang ditulis langsung pada atribut elemen HTML. Kelebihan inline CSS yaitu, proses request HTTP lebih kecil sehingga proses load website akan lebih cepat, dapat memperbaiki kode dengan cepat, dan membantu ketika developer ingin menguji perubahan pada satu elemen. Kekurangan inline CSS yaitu, tidak efisien karena inline CSS hanya dapat diterapkan pada satu elemen HTML.

2. Internal CSS --> Internal CSS merupakan Kode CSS yang di dalam tag style dan kode HTML ditulis pada header file HTML. Internal CSS cocok digunakan untuk membuat tampilan yang unik pada setiap page pada website karena mempunyai potensi untuk menampilkan tampilan yang berbeda-beda. Kelebihan internal CSS yaitu, tidak diperlukan untuk upload beberapa file dikarenakan kode HTML dan CSS berada di dalam satu file dan perubahan pada internal CSS hanya berlaku pada satu halaman saja. Kekurangan internal CSS yaitu. membuat performa website lebih lambat dikarenakan CSS yang berbeda-beda pada setiap halaman dapat membuat loading ulang setiap kali user mengganti halaman website.

3. External CSS --> External CSS merupakan Kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ditulis di file khusus (.css) dan diletakkan setelah bagian head pada halaman. Kelebihan external CSS yaitu, ukuran file HTML menjadi lebih kecil, struktur kode HTML lebih rapih, loading website lebih cepat, dan file CSS dapat digunakan di beberapa halaman sekaligus. Kekurangan eksternal CSS yaitu, halaman bisa saja berantakan akibat file CSS gagal dipanggil oleh file HTML yang biasa disebabkan oleh koneksi internet yang kurang bagus.

**Jelaskan tag HTML5 yang kamu ketahui.**

- `<!DOCTYPE>`	Tag untuk menentukan tipe dokumen
- `<html>`	    Tag untuk membuat sebuah dokumen HTML
- `<title>`	    Tag untuk membuat judul dari sebuah halaman
- `<body>`	    Tag untuk membuat tubuh dari sebuah halaman
- `<h1> - <h6>`	Tag untuk membuat heading
- `<p>`	        Tag untuk membuat paragraf
- `<!--...-->`	Tag untuk membuat komentar
- `<form>`	    Tag untuk membuat sebuah form HTML untuk input user
- `<input>`	    Tag untuk membuat sebuah kontrol input
- `<button>`	Tag untuk membuat sebuah tombol yang dapat diklik
- `<a>`	        Tag untuk membuat hyperlink
- `<nav>`	    Tag untuk membuat navigasi link

**Jelaskan tipe-tipe CSS selektor yang kamu ketahui.**

- selektor tag          --> selektor tag berfungsi untuk memilih elemen berdasarkan nama tag untuk menambahkan style pada tag tertentu, seperti `div {` atau `p {`.

- selektor class        --> Selektor class berfungsi untuk memilih elemen berdasarkan nama class untuk menambahkan style pada class tertentu. Selektor class dibuat dengan tanda titik di depannya, seperti `.card {`.

- selektor ID           --> Selektor ID berfungsi untuk memilih elemen berdasarkan ID nya, sama seperti class tetapi ID bersifat unik. Selektor ID dibuat dengan tanda pagar di depannya, seperti `#header {`.

- Selektor Atribut      --> Selektor Atribut berfungsi untuk memilih elemen berdasarkan attributnya, sama seperti tag tetapi dengan menambahkan attribut khusus pada tag, seperti `input type="text" {`.

- Selektor Universal    --> Selektor Universal berfungsi untuk memilih semua elemen pada scope tertentu. Selektor ini biasa digunakan untuk me-reset CSS, seperti `* {`.

- Selektor Pseudo       --> Selektor Pseudo berfungsi untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya. Terdapat dua macam selector pseudo, yaitu pseudo-class dan pseudo-element, seperti `.card:hover {`.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

- [x] Melakukan import framework bootstrap untuk aktivasi penggunaan bootstrap pada berkas html `base.html` yang nantinya akan di extend pada `login.html, register.html, add.html, todolist.html` sehingga nantinya dapat mengkostumisasi halaman HTML tersebut menggunakan bootstrap. Kode tersebut didapat dari https://getbootstrap.com/docs/5.2/getting-started/introduction/.

- [x] Selanjutnya, menkostumisasi halaman `login.html` dan `register.html` dengan mengubah warna background, padding, margin, font, text-allignment, serta menambahkan emoji agar lebih menarik. Selain itu, saya juga mengutilisasi cards dari bootstrap agar lebih tersusun rapih. Referensi halaman saya dapatkan dari https://mdbootstrap.com/docs/standard/extended/login/#!.

- [x] Berikutnya, menkustomisasi halaman `todolist.html` dan `add.html` dengan utilisasi yang sama pada `login.html` dan `register.html`, tetapi dengan perbedaan pada pemanfaatan cards dari bootstrapnya. Utilisasi card pada `todolist.html` adalah dengan memasukkan setiap task yang dibuat menjadi satu cards dan membungkus cards-cards tersebut dalam sebuah class yang mengatur baris dan kolom cards tersebut agar terdapat 4 cards dalam setiap barisnya dengan memanfaatkan 12-collums default yang digunakan oleh bootstrap dan membaginya menjadi 3 collums `<div class="row row-cols-md-3 mx-auto" style="width: 90%;">`. Saya juga mengutilisasi navbar sebagai perangkat utama dalam navigasi pada website todolist yang saya buat, serta dapat menampilkan username dari akun yang sedang login pada saat itu.

- [x] Kemudian, saya menambahkan class yang akan mengatur penggunaan space pada website apabila dibuka pada device yang berbeda-beda (Responsive) dengan memanfaatkan pembagian row-cols pada bootstrap `<div class="col-12 col-md-8 col-lg-6 col-xl-5">`

- [x] Terakhir, saya menambahkan folder css yang berisi file style.css pada folder static. style.css tersebut digunakan untuk menambahkan effect hover pada class card sebagai fitur tambahan pada website saya.


Note: `todolist1.html` dan `todolist4.html` merupakan template percobaan dan bukan template utama

Referensi:
- https://getbootstrap.com/docs/5.2/getting-started/introduction/

- https://mdbootstrap.com/docs/standard/extended/login/#!

- https://youtu.be/2qQxwT-Qm5E

- https://youtu.be/9cKsq14Kfsw

- https://youtu.be/At4B7A4GOPg