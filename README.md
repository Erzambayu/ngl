# NGSPAM - NGL Spammer

NGSPAM adalah skrip Python untuk mengirim pesan anonim ke akun NGL.link secara massal. Skrip ini dapat digunakan untuk tujuan edukasi dan pengujian.

**Ini adalah fork dari repositori asli [ryuhandev/ngl](https://github.com/ryuhandev/ngl) oleh [Erzambayu](https://github.com/Erzambayu).**

## Fitur

*   **Mengirim Pesan Massal**: Kirim pesan dalam jumlah besar ke target pengguna NGL.
*   **Mode Pesan**: Gunakan satu pesan tunggal atau muat pesan dari file wordlist.
*   **Delay yang Dapat Disesuaikan**: Atur jeda waktu antar pengiriman pesan dalam detik.
*   **Dukungan Proxy**: Gunakan proxy untuk menyembunyikan alamat IP Anda.
*   **User-Agent Acak**: Menggunakan User-Agent yang berbeda untuk setiap permintaan.
*   **Tampilan Progres**: Lacak progres pengiriman pesan dengan progress bar yang informatif.

## Instalasi

1.  **Clone repository ini:**
    ```bash
    git clone https://github.com/Erzambayu/ngl
    ```
2.  **Masuk ke direktori proyek:**
    ```bash
    cd ngl
    ```
3.  **Install dependensi yang diperlukan:**
    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan

Jalankan skrip dengan perintah berikut:

```bash
python ngl.py
```

Skrip akan meminta Anda untuk memasukkan informasi berikut:

*   **Username target**: Nama pengguna NGL yang akan dikirimi pesan.
*   **Mode pesan**: Pilih antara menggunakan pesan tunggal atau wordlist.
*   **Pesan atau path wordlist**: Masukkan pesan tunggal atau path ke file wordlist.
*   **Jumlah percobaan**: Jumlah pesan yang akan dikirim.
*   **Jeda waktu**: Jeda waktu antar pengiriman pesan dalam detik.
*   **Gunakan proxy?**: Pilih apakah akan menggunakan proxy atau tidak.
*   **Path file proxy**: Jika menggunakan proxy, masukkan path ke file proxy.

Setelah semua informasi dimasukkan, skrip akan menampilkan konfirmasi sebelum memulai proses pengiriman.

## Disclaimer

Skrip ini dibuat untuk tujuan edukasi dan pengujian. Pengguna bertanggung jawab penuh atas segala tindakan yang dilakukan menggunakan skrip ini. Pengembang tidak bertanggung jawab atas penyalahgunaan apa pun.
