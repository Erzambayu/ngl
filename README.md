# 🚀 NGSPAM - Advanced NGL Spammer v6.0

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable%20%26%20Stealth-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**✉️ Tool canggih untuk mengirim pesan anonim ke NGL.link dengan fitur rate limiting dan target sukses**

[📥 Download](#instalasi) • [🚀 Quick Start](#penggunaan) • [⚙️ Fitur](#fitur-utama) • [📖 Dokumentasi](#dokumentasi)

</div>

---

## 🌟 Fitur Utama

### 🎯 **Smart Target System**
- ✅ **Target Success Mode**: Mencapai jumlah pesan sukses yang ditentukan
- 🔄 **Unlimited Attempts**: Tidak ada batas percobaan sampai target tercapai
- 📊 **Real-time Progress**: Progress bar berdasarkan sukses vs target

### 🛡️ **Advanced Rate Limiting**
- ⏰ **Auto Rate Limit Detection**: Deteksi otomatis status code 429
- ⏳ **Smart Countdown Timer**: Countdown 25 detik dengan tampilan realtime
- 🔄 **Auto Retry**: Melanjutkan otomatis setelah rate limit selesai

### 🎭 **Stealth & Security**
- 🌐 **Multiple User Agents**: 5+ user agent berbeda untuk setiap request
- 🔀 **Random Message Selection**: Pilih pesan acak dari wordlist
- 🆔 **Unique Device ID**: Generate device ID unik untuk setiap request
- 🌍 **Proxy Support**: Dukungan proxy untuk menyembunyikan IP

### 📱 **User Experience**
- 🎨 **Beautiful UI**: Interface colorful dengan ASCII banner
- 📈 **Detailed Statistics**: Statistik lengkap (sukses, gagal, rate limited)
- ⚡ **Performance Metrics**: Request per second dan success rate
- 🛑 **Graceful Interruption**: Handle Ctrl+C dengan bersih

---

## 📥 Instalasi

### 📋 Prerequisites
- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### 🔧 Setup

1. **Clone repository:**
   ```bash
   git clone https://github.com/Erzambayu/ngl.git
   cd ngl
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Siap digunakan!**
   ```bash
   python ngl.py
   ```

---

## 🚀 Penggunaan

### 💡 Quick Start

```bash
python ngl.py
```

### 📝 Input Parameters

| Parameter | Deskripsi | Default | Contoh |
|-----------|-----------|---------|---------|
| **Username Target** | Username NGL target | - | `johndoe` |
| **Mode Pesan** | Pilih teks tunggal atau wordlist | `2` (wordlist) | `1` atau `2` |
| **Target Sukses** | Jumlah pesan yang harus berhasil | `100` | `50`, `200` |
| **Delay** | Jeda antar request (detik) | `1` | `0.5`, `2` |
| **Proxy** | Gunakan proxy atau tidak | `n` | `y` atau `n` |

### 📁 File Structure

```
ngl/
├── ngl.py              # Main script
├── wordlist.txt        # Default message wordlist
├── proxy.txt           # Proxy list (optional)
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── LICENSE            # MIT License
```

---

## ⚙️ Konfigurasi

### 📝 Wordlist Format
Buat file `wordlist.txt` dengan format:
```
Pesan pertama
Pesan kedua
Pesan ketiga
...
```

### 🌐 Proxy Format
Buat file `proxy.txt` dengan format:
```
http://proxy1:port
http://proxy2:port
https://proxy3:port
...
```

---

## 📊 Contoh Output

```
================================================================================
                               ✉️  NGL SPAMER v6.0                               
================================================================================
 Developer: Erzam Bayu
🔗 GitHub: @Erzambayu
⚡️ Status: STABLE & STEALTH MODE
================================================================================

======================================================================
NGSPAM - STABLE & STEALTH MODE
======================================================================
Target: johndoe
Messages: 50 loaded
Target Success: 100
Delay: 1 seconds
Proxies: 10 loaded
User Agents: 5 loaded
======================================================================

Progress |████████████████████████████████████████| 100.0% [S:100 F:5 R:3] (100/100) [2.5 req/s]

Rate limit terdeteksi! Menunggu 25 detik...
⏳ Menunggu: 15 detik tersisa...
✅ Menunggu selesai! Melanjutkan proses...

======================================================================
 EXECUTION COMPLETE
======================================================================
Successful: 100
Rate Limited: 3
Failed: 5
Total Attempts: 108
Success Rate: 92.59%
======================================================================
```

---

## 🔧 Advanced Features

### 🎯 Target Success Mode
- Program berjalan sampai mencapai jumlah **sukses** yang diinginkan
- Tidak peduli berapa banyak total attempts
- Progress bar menunjukkan sukses vs target

### ⏰ Smart Rate Limiting
- Deteksi otomatis rate limit (HTTP 429)
- Countdown timer 25 detik dengan update realtime
- Auto-resume setelah cooldown selesai

### 📈 Performance Monitoring
- Real-time statistics (sukses, gagal, rate limited)
- Request per second calculation
- Success rate percentage

---

## 🛡️ Error Handling

Program dilengkapi dengan error handling yang robust:

- **KeyboardInterrupt**: Handle Ctrl+C dengan graceful
- **EOFError**: Handle masalah input stream
- **Network Errors**: Handle timeout dan connection errors
- **File Errors**: Handle file tidak ditemukan atau corrupt

---

## 📖 Dokumentasi

### 🔍 Status Codes

| Status | Deskripsi | Action |
|--------|-----------|--------|
| `success` | Pesan berhasil dikirim | Continue |
| `failed` | Request gagal (network/server error) | Continue |
| `rate_limited` | Terkena rate limit (HTTP 429) | Wait 25s |

### 🎨 Color Codes

- 🟢 **Hijau**: Success, completion messages
- 🟡 **Kuning**: Warnings, rate limit notifications
- 🔴 **Merah**: Errors, failures
- 🔵 **Biru**: Information, headers
- 🟣 **Magenta**: Statistics, performance metrics

---

## 🤝 Contributing

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## ⚠️ Disclaimer

> **PENTING**: Tool ini dibuat untuk tujuan **edukasi dan pengujian** saja. 

- ✅ Gunakan hanya pada akun yang Anda miliki atau dengan izin
- ❌ Jangan gunakan untuk spam atau harassment
- ⚖️ Pengguna bertanggung jawab penuh atas penggunaan tool ini
- 🛡️ Developer tidak bertanggung jawab atas penyalahgunaan

---

## 📄 License

Proyek ini dilisensikan di bawah [MIT License](LICENSE) - lihat file LICENSE untuk detail.

---

## 👨‍💻 Developer

<div align="center">

**Erzam Bayu**

[![GitHub](https://img.shields.io/badge/GitHub-@Erzambayu-black?style=flat&logo=github)](https://github.com/Erzambayu)

*"Code with passion, share with purpose"*

</div>

---

## 🌟 Support

Jika tool ini membantu Anda, berikan ⭐ pada repository ini!

<div align="center">

**Made with ❤️ by Erzam Bayu**

</div>