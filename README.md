# 📚 API Automation Project: Restful Booker

[![Status Proyek](https://img.shields.io/badge/Status-Aktif-green.svg)](https://github.com/idham099/API_Automation_Restful_Booker)
[![API Target](https://img.shields.io/badge/API-Restful--Booker-blue)](https://restful-booker.herokuapp.com/apidoc/)
[![Framework](https://img.shields.io/badge/Framework-Pytest-orange)](SebutkanVersi)

## 🎯 Tentang Proyek

Proyek ini adalah **Otomatisasi Pengujian API** yang ditujukan untuk menguji API *dummy* **Restful Booker**. 
Tujuan utama dari proyek ini adalah untuk memastikan fungsionalitas dan keandalan API *booking* hotel secara otomatis.
Saya menguji *endpoint* utama yang didefinisikan dalam dokumentasi API [Restful Booker API Documentation](https://restful-booker.herokuapp.com/apidoc/).


<img width="1819" height="1460" alt="image" src="https://github.com/user-attachments/assets/603948d8-35d4-437b-b742-18d96c63f7eb" />



### Skenario Pengujian yang Dicakup

Pengujian otomatisasi ini mencakup skenario-skenario penting, seperti:

1. Skenario positif
* **Autentikasi (POST):** Membuat token otentikasi.
* **Create Booking (POST):** Memastikan reservasi dapat dibuat dengan data yang valid.
* **Get Booking (GET):** Mengambil detail reservasi berdasarkan List maupun ID.
* **Update Booking (PUT/PATCH):** Mengubah detail reservasi yang sudah ada.
* **Delete Booking (DELETE):** Menghapus reservasi.
* **Validasi Skema:** Memeriksa struktur JSON respons.
* **Validasi Status Kode:** Memastikan *status code* HTTP yang benar dikembalikan (e.g., 200 OK, 201 Created).


2. Skenario Negatif
* **Payload Tidak Lengkap (POST):** Memastikan API menolak permintaan untuk membuat booking baru (POST) tanpa field mandatory.
* **Tanpa Token Otentikasi (DELETE):** Memastikan bahwa API menolak permintaan untuk menghapus booking (DELETE) tanpa Token.
* **Tanpa Token Otentikasi (GET):** Menguji Integritas Data dan Penanganan Resource yang Hilang.
* **Validasi Skema:** Memeriksa struktur JSON respons.
* **Validasi Status Kode:** Memastikan *status code* HTTP yang benar dikembalikan (e.g., 500 Internal Server Error, 403 Forbidden, 404 Not Found).


## ⚙️ Teknologi yang Digunakan

| Kategori | Teknologi | Deskripsi |
| :--- | :--- | :--- |
| **Bahasa Pemrograman** | **Python 3.12+** | Bahasa utama untuk pengembangan skrip pengujian. |
| **Framework Pengujian** | **[Pytest](https://docs.pytest.org/)**| Digunakan untuk struktur, eksekusi, dan *assertion* pengujian. |
| **Library HTTP** | **[Requests](https://docs.python-requests.org/en/master/)** | Library khusus untuk mengirim permintaan HTTP. |
| **Manajemen Environment** | **`python-dotenv`**| Untuk mengelola kredensial. |
| **Pelaporan** | **[Allure Report](https://qameta.io/allure/)** | Alat untuk menghasilkan laporan pengujian visual yang detail. |



## 🚀 Cara Menjalankan Tes dan Laporan
Ikuti langkah-langkah berikut untuk menjalankan proyek secara lokal.

### 1. Eksekusi Tes
Jalankan script dari Terminal/Command Prompt di root folder proyek:
```
.\run_api_report.bat
```

### 2. Melihat Laporan
Setelah tes selesai (Langkah [2/3] dalam script), laporan HTML interaktif akan dibuat di folder allure-report/.

**Jika laporan tidak otomatis terbuka (Langkah [3/3] gagal):**

Jalankan perintah berikut di Terminal Anda untuk meluncurkan server laporan:
```
allure serve allure-results
```


## 🔗 Fixture Chaining
Proyek ini sangat bergantung pada Fixture Chaining (misalnya, created_booking_id menggunakan auth_token dan create_booking_payload). Ini memastikan setiap tes CRUD memiliki data yang unik, fresh, dan terotentikasi untuk dijalankan, meningkatkan stabilitas dan isolasi tes.

##
Dibuat dengan 😭 oleh Ainul idham.

