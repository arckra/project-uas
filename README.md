# project-uas

# 1. Struktur Modular dan OOP
- **Kelas Data (Vehicle):**

Kelas ini bertanggung jawab untuk menyimpan informasi tentang kendaraan. Dengan mendefinisikan atribut jenis, nama, dan kapasitas, kita dapat membuat objek kendaraan yang memiliki karakteristik yang jelas.

- **Kelas View (View):**

Kelas ini memiliki metode statis display_vehicles yang bertugas untuk menampilkan daftar kendaraan dalam format tabel. Dengan memisahkan logika tampilan dari logika bisnis, kita menjaga kode tetap terorganisir dan mudah dipelihara.

- **Kelas Process (Process):**

Kelas ini mengelola logika program, termasuk menambah kendaraan dan menampilkan daftar kendaraan. Dengan menyimpan daftar kendaraan dalam atribut self.vehicles, kita dapat mengelola data kendaraan dengan lebih efisien.

![image](https://github.com/user-attachments/assets/90d7b319-ee20-4614-90fb-4b783dab157f)

# 2. Input Pengguna dan Validasi
- **Input dari Pengguna:**

Program meminta pengguna untuk memasukkan jenis kendaraan, nama kendaraan, dan kapasitas bensin. Ini dilakukan dalam metode add_vehicle di kelas Process.

![image](https://github.com/user-attachments/assets/644b309e-8b54-4a40-91e6-e0615410c17f)

- **Validasi Input:**

Program menggunakan blok try-except untuk menangani kesalahan input. Jika pengguna memasukkan jenis kendaraan yang tidak valid atau kapasitas yang tidak sesuai (misalnya, kurang dari atau sama dengan 0), program akan memberikan pesan kesalahan yang jelas. Ini meningkatkan pengalaman pengguna dengan memberikan umpan balik yang tepat.

# 3. Menampilkan Data
- **Format Tabel:**
  
Metode `display_vehicles` di kelas View menampilkan data kendaraan dalam format tabel yang rapi. Ini membuat informasi lebih mudah dibaca dan dipahami oleh pengguna. Penggunaan format string dengan pengaturan lebar kolom (`:<10`, `:<20`, `:<15`) memastikan bahwa data ditampilkan dengan rapi.

![image](https://github.com/user-attachments/assets/e38ca4a6-7303-4077-8516-e8d8eee70186)

# 4. Menu Interaktif
- **Fungsi Utama (main):**
  
Fungsi ini menyediakan menu interaktif yang memungkinkan pengguna untuk memilih opsi yang diinginkan (menambah kendaraan, menampilkan daftar kendaraan, atau keluar dari program). Dengan menggunakan loop while, program akan terus berjalan hingga pengguna memilih untuk keluar.

![image](https://github.com/user-attachments/assets/446cc0fc-4d03-4946-b1cc-b4853c39dd16)

- **Pengendalian Alur Program:**

Dengan menggunakan pernyataan if-elif-else, program dapat mengarahkan pengguna ke fungsi yang sesuai berdasarkan pilihan mereka. Ini memastikan bahwa pengguna dapat berinteraksi dengan program dengan cara yang intuitif.

![image](https://github.com/user-attachments/assets/a31f541b-cd9f-46a8-8e95-00235f6da6ea)

![image](https://github.com/user-attachments/assets/75e25d29-d20c-46d3-b456-e9527a6911f2)

# 5. Penggunaan Exception Handling
- **Menangani Kesalahan:**
  
Dengan menggunakan ValueError untuk menangani kesalahan input, program dapat memberikan umpan balik yang jelas kepada pengguna tanpa menghentikan eksekusi program. Ini membuat program lebih robust dan user-friendly.



Dengan semua elemen ini, program dapat berfungsi dengan baik dan memenuhi tujuan yang diinginkan, yaitu mengelola dan menampilkan daftar kendaraan dengan kapasitas bensin.
