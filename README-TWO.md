### **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
- Asynchronous programming: Suatu model pemrograman dimana suatu program dapat menjalankan beberapa tugas secara bersamaan. Suatu tugas akan berjalan tanpa harus menunggu function tersebut selesai (concurrent). Suatu tugas dilaksanakan, maka instruksi untuk menjalankan tugas lain masih dapat dijalankan. 

- Synchronous programming: Suatu model pemrograman dimana suatu program berjalan secara berurutan. Program berjalan satu per satu. Suatu tugas akan berjalan ketika tugas lainnya sudah selesai (sequential). Suatu tugas dilaksanakan, maka instruksi untuk menjalankan tugas lain diblokir.

### **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-Driven programming merupakan adalah pola design perangkat lunak ketika suatu program dieksekusi berdasarkan event yang ada. Event-Driven Programming bergantung pada event, sehingga alur dari program dapat dijalankan secara tidak berurutan (sequential) dengan menerapkan proses asynchronous programming (concurrent). Pada tugas ini, salah satu penerapan dari Event-Driven Programming adalah ketika button `submit` di click, maka anak dijalankan suatu fungsi untuk membuat task baru. Fungsi ini akan selalu dijalankan jika terdapat event yaitu click (onclick)

### **Jelaskan penerapan asynchronous programming pada AJAX.**
Asynchronus programming pada AJAX adalah ketika sebuah event terjadi, event tersebut akan menjalankan fungsionalitas AJAX. Misalnya pada tugas 6 ini ketika mengklik button create pada form untuk membuat task baru, akan dilakukan AJAX POST untuk mengirim data ke server. Setelah server selesai mengolah data tersebut, akan dijalankan callback function yang telah dibuat sebelumnya. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload sehingga memberikan pengalaman browsing lebih baik.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
AJAX GET 
- Pada views.py, ditambahkan function untuk mengambil task yang sesuai dengan user login saat itu dalam bentuk JSON. Views akan terhubung setelah kita menambahkan routing path pada urls.py. Ketika website selesai load, AJAX GET terpanggil untuk mendapatkan task dalam bentuk JSON yang dimasukkan ke dalam masing-masing cards.
##
AJAX POST
- Button create yang sebelumnya redirect ke todolist/create_task, kita ubah agar dapat memunculkan modal. Implementasinya, pada views.py ditambahkan function create_task_modal dan views akan terhubung setelah kita menambahkan routing path pada urls.py. Pada function diterapkan asynchronous programming sehingga task akan terupdate tanpa reload website. 