# jurnal-umum-webapp
Aplikasi Pencatatan Jurnal Umum menggunakan Framework Flask.
![login](/src/static/image/jurnal.png)

## Tujuan:
1. Gambaran minimum aplikasi yang dapat di buat oleh peserta kursus python web apps.
2. Sebagai dokumentasi dan acuan bagi trainer python web apps yang baru.


## Fitur Aplikasi:
1. Login
2. List Jurnal
3. Tambah Jurnal
4. Edit Jurnal
5. Delete Jurnal  
6. List Transaksi
7. Tambah Transaksi
8. Edit Transaksi
9. Delete Transaksi

## Tutorial
### 1. Installasi
   - Clone project
    
      Sebelum melakukan proses cloning pastikan anda menginstall git di local machine anda. Kemudian untuk mendapatkan Jurnal Umum Web Apps kita dapat melakukan proses cloning project dengan menggunakan command sebagai berikut 
      ```
      git clone https://github.com/itecsmart/jurnal-umum-webapp.git
      ```
   - Menyiapkan environtment

      Setelah aplikasi jurnal umum berhasil di clone dari github kita perlu membuat sebuah environmet untuk menginstall seluruh dependency yang di butuhkan untuk menjalankan apliasi tersebut.
      
      Pada tutorial kali ini kita akan membuat sebuah python environment di dalam directory jurnal-umum-web-app.

      Anda dapat masuk ke dalam jurnal-umum-web-app directory dengan menggunakan command line sebagai berikut

        ```
        cd jurnal-umum-web-app/
        ```
      Selanjutnya unutk membuat environment gunakan command 

      ```
      python3 -m venv myenv 
      ```

  - Aktifasi environment
   
    Setelah kita membuat environment kita perlu untuk mengaktifasi environment tesebut dengan menggunakan command:
      
      Windows
      ```
      .\myenv\Scripts\activate
      ```
      
      Linux

      ```
      source myenv/bin/activate
      ```
   - Install requirement.txt
    
      Menginstall dependensi untuk menjalankan aplikasi yang terdapat dalam requirement.txt file dengan menggunakan command
      ```
      pip install -r requirement.txt
      ``` 
### 2. Menjalankan Aplikasi
   
   Setelah berhasil melakukan cloning dan membuat environtment, maka langkah selanjutnya adalah menjalankan project dengan cara
   ```
   python app.py
   ```
   
   Buka aplikasi pada web browser anda dengan menuliskan port yang tertera di terminal anda
   ![run](/src/static/image/run.png)

   Agar anda mengakses halaman login, tambahkan /login di belakang posrt :5000

   ![login_url](/src/static/image/login_url.png)

   Masukan username dan password untuk mengakses jurnal

   ```
   username : apip
   password : pipopedeng
   ```
   ![login](/src/static/image/login.png)
### 3. Video Tutorial
   
   [video_tutorial](https://www.youtube.com/watch?v=WBhNVDtNuHA&t=185s)