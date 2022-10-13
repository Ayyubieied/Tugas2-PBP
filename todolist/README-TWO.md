# Tugas 6 Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Nama : Ied Mubaraque Sultan Salahuddine El Ayyubie
## NPM : 2106751120

Contributor : Rakan Fasya Athhar Rayyan (2106750950)

**Link Heroku** : [Link HerokuApp](https://tugas2-ayyubie.herokuapp.com/todolist/)

### **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
- Asynchronous programming: Suatu model pemrograman dimana suatu program dapat menjalankan beberapa tugas secara bersamaan. Suatu tugas akan berjalan tanpa harus menunggu function tersebut selesai (concurrent). Suatu tugas dilaksanakan, maka instruksi untuk menjalankan tugas lain masih dapat dijalankan. 

- Synchronous programming: Suatu model pemrograman dimana suatu program berjalan secara berurutan. Program berjalan satu per satu. Suatu tugas akan berjalan ketika tugas lainnya sudah selesai (sequential). Suatu tugas dilaksanakan, maka instruksi untuk menjalankan tugas lain diblokir.

### **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-Driven programming merupakan adalah pola design perangkat lunak ketika suatu program dieksekusi berdasarkan event yang ada. Event-Driven Programming bergantung pada event, sehingga alur dari program dapat dijalankan secara tidak berurutan (sequential) dengan menerapkan proses asynchronous programming (concurrent). Pada tugas ini, salah satu penerapan dari Event-Driven Programming adalah ketika button `submit` di click, maka anak dijalankan suatu fungsi untuk membuat task baru. Fungsi ini akan selalu dijalankan jika terdapat event yaitu click (onclick)

### **Jelaskan penerapan asynchronous programming pada AJAX.**
Asynchronus programming yang terdapat pada AJAX adalah ketika terdapat sebuah event, event tersebut akan menjalankan fungsionalitas AJAX. Jika dimisalkan pada tugas 6 terdapat button submit pada form untuk membuat task baru dan di click oleh User, maka akan dilakukan AJAX POST untuk mengirim data ke server. Setelah server selesai mengolah data tersebut, maka akan dijalankan callback function yang telah dibuat sebelumnya. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload sehingga memberikan pengalaman browsing yang lebih baik

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- Fungsi `show_json` digunakan untuk return data input form dalam bentuk JSON
- Manambahkan routing `/todolist/json` pada `urls.py` untuk fungsi `show_json`
- Membuat fungsi JavaScript `cardReset()` dengan memanfaatkan AJAX GET untuk merender cards berdasarkan database JSON dari `/todolist/json`
- `cardReset()` akan dijalankan ketika halaman sudah selesai dimuat untuk render cards
- Membuat fungsi `add_ajax_task` untuk menambahkan data task baru 
- Menambahkan routing `/todolist/add` pada `urls.py` untuk fungsi `add_ajax_task`
- Membuat modal dengan menambahkan form untuk input nama dan deskripsi task yang kemudian akan ditampilkan dengan menambah cards baru
- Membuat fungsi pada HTML dengan menggunakan tag `script` berupa javaScript dengan method addNewTask() dan tipe method POST untuk menerima input dari modal dan disubmit. Kemudian, input tersebut akan diproses oleh `add_ajax_task`. Setelah diproses, maka website akan update cards secara *Asynchronous* 