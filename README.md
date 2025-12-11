# 📚 API Automation Project: Restful Booker

[![Status Proyek](https://img.shields.io/badge/Status-Aktif-green.svg)](https://github.com/idham099/API_Automation_Restful_Booker)
[![API Target](https://img.shields.io/badge/API-Restful--Booker-blue)](https://restful-booker.herokuapp.com/apidoc/)
[![Framework](https://img.shields.io/badge/Framework-SebutkanFramework-orange)](SebutkanVersi)

## 🎯 Tentang Proyek

Proyek ini adalah solusi **Otomatisasi Pengujian API** yang ditujukan untuk menguji API *dummy* **Restful Booker**. Tujuan utama dari proyek ini adalah untuk memastikan fungsionalitas dan keandalan API *booking* hotel ini secara otomatis.

Kami menguji *endpoint* utama yang didefinisikan dalam dokumentasi API [Restful Booker API Documentation](https://restful-booker.herokuapp.com/apidoc/).

### Skenario Pengujian yang Dicakup

Pengujian otomatisasi ini mencakup skenario-skenario penting, seperti:

* **Autentikasi:** Membuat token otentikasi.
* **Create Booking (POST):** Memastikan reservasi dapat dibuat dengan data yang valid.
* **Get Booking (GET):** Mengambil detail reservasi berdasarkan ID.
* **Update Booking (PUT/PATCH):** Mengubah detail reservasi yang sudah ada.
* **Delete Booking (DELETE):** Menghapus reservasi.
* **Validasi Skema:** Memeriksa struktur JSON respons.
* **Validasi Status Kode:** Memastikan *status code* HTTP yang benar dikembalikan (e.g., 200 OK, 201 Created).

## 🛠️ Teknologi dan Dependensi

| Kategori | Teknologi | Deskripsi |
| :--- | :--- | :--- |
| **Bahasa Pemrograman** | **[Sebutkan Bahasa]** (e.g., Python, Java) | Bahasa utama untuk pengembangan skrip pengujian. |
| **Framework Pengujian** | **[Sebutkan Framework]** (e.g., Pytest, Rest Assured, TestNG) | Digunakan untuk struktur, eksekusi, dan *assertion* pengujian. |
| **Library HTTP** | **[Sebutkan Library]** (e.g., Requests, Rest Assured) | Library khusus untuk mengirim permintaan HTTP. |
| **Data/Config** | **[Sebutkan Format Data]** (e.g., JSON, YAML, Excel) | Format yang digunakan untuk mengelola data pengujian (Test Data Management). |
| **Pelaporan** | **[Sebutkan Alat Pelaporan]** (e.g., Allure, Extent Report) | Alat untuk menghasilkan laporan pengujian visual yang detail. |

## ⚙️ Persyaratan Sistem

Pastikan Anda memiliki hal-hal berikut terinstal di mesin Anda:

* **[Nama Bahasa] Runtime:** Versi **[Sebutkan Versi]** atau lebih tinggi.
* **[Nama Alat Manajemen Paket]** (e.g., `pip` atau `Maven`/`Gradle`).
* Git.

## 🚀 Instalasi dan Setup Lokal

Ikuti langkah-langkah di bawah ini untuk memulai.

### 1. Kloning Repositori

```bash
git clone [https://github.com/idham099/API_Automation_Restful_Booker.git](https://github.com/idham099/API_Automation_Restful_Booker.git)
cd API_Automation_Restful_Booker
