# 🚀 NGSPAM - Advanced NGL Spammer v7.0

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable%20%26%20Stealth-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Termux-lightgrey.svg)

**✉️ Tool canggih untuk mengirim pesan anonim ke NGL.link dengan fitur stealth dan rate limiting**

[📥 Instalasi](#-instalasi) • [🚀 Penggunaan](#-penggunaan) • [⚙️ Fitur](#-fitur-utama) • [📖 Dokumentasi](#-dokumentasi)

</div>

---

## 📋 Daftar Isi

- [Fitur Utama](#-fitur-utama)
- [Instalasi](#-instalasi)
  - [Windows](#-windows)
  - [Linux / macOS](#-linux--macos)
  - [Android (Termux)](#-android-termux)
- [Penggunaan](#-penggunaan)
  - [Mode Interaktif](#mode-interaktif)
  - [Mode CLI](#mode-cli-command-line)
- [Konfigurasi](#️-konfigurasi)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)

---

## 🌟 Fitur Utama

### 🎯 **Smart Target System**
- ✅ **Target Success Mode** - Mencapai jumlah pesan sukses yang ditentukan
- 🔄 **Unlimited Attempts** - Tidak ada batas percobaan sampai target tercapai
- 📊 **Real-time Progress** - Progress bar berdasarkan sukses vs target

### 🛡️ **Advanced Rate Limiting**
- ⏰ **Auto Rate Limit Detection** - Deteksi otomatis HTTP 429
- ⏳ **Smart Countdown Timer** - Countdown dengan tampilan realtime
- 🔄 **Auto Retry** - Melanjutkan otomatis setelah cooldown

### 🎭 **Stealth & Security**
- 🌐 **Multiple User Agents** - 7+ user agent berbeda
- 🔀 **Random Message Selection** - Pilih pesan acak dari wordlist
- 🆔 **Unique Device ID** - Generate device ID unik setiap request
- 🌍 **Proxy Support** - Dukungan proxy HTTP/HTTPS/SOCKS

### 📱 **User Experience**
- 🎨 **Beautiful UI** - Interface colorful dengan emoji
- 📈 **Detailed Statistics** - Statistik lengkap
- ⚡ **Performance Metrics** - Request per second
- 🖥️ **Dual Mode** - Interaktif dan CLI

---

## 📥 Instalasi

### 🪟 Windows

#### Metode 1: PowerShell (Recommended)

```powershell
# 1. Install Python dari python.org jika belum ada
# Pastikan centang "Add Python to PATH" saat install

# 2. Clone repository
git clone https://github.com/Erzambayu/ngl.git
cd ngl

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan
python ngl.py
```

#### Metode 2: CMD

```cmd
:: 1. Buka Command Prompt sebagai Administrator

:: 2. Clone repository
git clone https://github.com/Erzambayu/ngl.git
cd ngl

:: 3. Install dependencies
pip install -r requirements.txt

:: 4. Jalankan
python ngl.py
```

> **💡 Tips Windows:**
> - Jika `git` tidak ditemukan, install dari [git-scm.com](https://git-scm.com)
> - Jika `python` tidak ditemukan, pastikan Python sudah di-add ke PATH

---

### 🐧 Linux / macOS

#### Ubuntu / Debian

```bash
# 1. Update package manager
sudo apt update && sudo apt upgrade -y

# 2. Install Python dan pip
sudo apt install python3 python3-pip git -y

# 3. Clone repository
git clone https://github.com/Erzambayu/ngl.git
cd ngl

# 4. Install dependencies
pip3 install -r requirements.txt

# 5. Jalankan
python3 ngl.py
```

#### Arch Linux / Manjaro

```bash
# 1. Install Python dan git
sudo pacman -Syu python python-pip git

# 2. Clone dan jalankan
git clone https://github.com/Erzambayu/ngl.git
cd ngl
pip install -r requirements.txt
python ngl.py
```

#### macOS

```bash
# 1. Install Homebrew jika belum ada
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install Python dan git
brew install python git

# 3. Clone dan jalankan
git clone https://github.com/Erzambayu/ngl.git
cd ngl
pip3 install -r requirements.txt
python3 ngl.py
```

---

### 📱 Android (Termux)

Termux adalah terminal emulator untuk Android yang memungkinkan menjalankan tool ini di HP.

#### Langkah Instalasi

```bash
# 1. Install Termux dari F-Droid (BUKAN Play Store!)
# Download: https://f-droid.org/packages/com.termux/

# 2. Buka Termux dan update packages
pkg update && pkg upgrade -y

# 3. Install Python dan git
pkg install python git -y

# 4. Berikan akses storage (opsional)
termux-setup-storage

# 5. Clone repository
git clone https://github.com/Erzambayu/ngl.git
cd ngl

# 6. Install dependencies
pip install -r requirements.txt

# 7. Jalankan
python ngl.py
```

#### Quick Install (Copy-Paste)

Copy dan paste command ini di Termux:

```bash
pkg update -y && pkg upgrade -y && pkg install python git -y && git clone https://github.com/Erzambayu/ngl.git && cd ngl && pip install -r requirements.txt && python ngl.py
```

> **⚠️ Penting untuk Termux:**
> - Install Termux dari **F-Droid**, bukan Play Store (versi Play Store sudah outdated)
> - Jika ada error "repository is under maintenance", jalankan `termux-change-repo` dan pilih mirror lain
> - Untuk menyalin teks, tap dan tahan, lalu pilih "Copy"
> - Untuk paste, tap dan tahan, lalu pilih "Paste"

---

## 🚀 Penggunaan

### Mode Interaktif

Jalankan tanpa argumen untuk mode interaktif dengan prompt:

```bash
python ngl.py
```

Program akan memandu Anda dengan pertanyaan:
1. Username target
2. Mode pesan (tunggal/wordlist)
3. Target pesan sukses
4. Delay antar pesan
5. Penggunaan proxy

### Mode CLI (Command Line)

Untuk automasi atau scripting, gunakan argumen command line:

```bash
# Basic usage
python ngl.py -u username -t 50

# Dengan pesan tunggal
python ngl.py -u username -m "Halo!"

# Dengan custom wordlist dan delay
python ngl.py -u username -w pesan.txt -d 0.5 -t 100

# Dengan proxy
python ngl.py -u username -p proxy.txt

# Skip validasi username
python ngl.py -u username --skip-validate --force
```

#### Argumen CLI

| Argumen | Deskripsi | Default |
|---------|-----------|---------|
| `-u, --username` | Username target NGL | - |
| `-m, --message` | Pesan tunggal | - |
| `-w, --wordlist` | Path file wordlist | `wordlist.txt` |
| `-t, --target` | Target pesan sukses | `100` |
| `-d, --delay` | Delay antar pesan (detik) | `1.0` |
| `-p, --proxy` | Path file proxy | - |
| `--rate-limit-delay` | Delay saat rate limit | `25` |
| `--skip-validate` | Skip validasi username | - |
| `--force` | Lanjut meski username invalid | - |

Lihat semua opsi:
```bash
python ngl.py --help
```

---

## ⚙️ Konfigurasi

### 📝 Wordlist Format

Buat file `wordlist.txt` dengan satu pesan per baris:

```
Hai, apa kabar?
Semangat ya hari ini!
Kamu keren banget deh
Jangan lupa senyum :)
```

### 🌐 Proxy Format

Buat file `proxy.txt` dengan format:

```
ip:port
ip:port:username:password
http://ip:port
https://ip:port
socks5://ip:port
```

Contoh:
```
103.152.112.162:80
154.194.12.137:8080
http://185.162.229.220:80
socks5://192.168.1.1:1080
```

---

## 📁 Struktur File

```
ngl/
├── ngl.py              # Script utama
├── wordlist.txt        # Default message wordlist
├── proxy.txt           # Proxy list (opsional)
├── requirements.txt    # Python dependencies
├── README.md           # Dokumentasi
└── LICENSE             # MIT License
```

---

## 🔧 Troubleshooting

### ❌ Error: `ModuleNotFoundError: No module named 'requests'`

**Solusi:** Install dependencies yang diperlukan

```bash
pip install -r requirements.txt
# atau
pip install requests pyfiglet colorama
```

### ❌ Error: `python: command not found`

**Solusi:** 
- Windows: Reinstall Python dan centang "Add to PATH"
- Linux: Gunakan `python3` bukan `python`
- Termux: `pkg install python`

### ❌ Error: `git: command not found`

**Solusi:**
- Windows: Install dari [git-scm.com](https://git-scm.com)
- Linux: `sudo apt install git` atau `sudo pacman -S git`
- Termux: `pkg install git`

### ❌ Error: Rate limit terus menerus

**Solusi:**
1. Tingkatkan delay: `-d 2` atau lebih
2. Gunakan proxy
3. Tunggu beberapa jam sebelum mencoba lagi

### ❌ Error: Username tidak valid

**Solusi:**
1. Pastikan username benar dan ada di NGL.link
2. Coba buka `https://ngl.link/USERNAME` di browser
3. Gunakan `--skip-validate --force` untuk bypass

### ❌ Termux: `repository is under maintenance`

**Solusi:**
```bash
termux-change-repo
# Pilih mirror lain (misal: Albatross)
```

---

## ❓ FAQ

**Q: Apakah tool ini gratis?**
> Ya, 100% gratis dan open source.

**Q: Apakah aman digunakan?**
> Tool ini untuk edukasi. Gunakan dengan tanggung jawab.

**Q: Kenapa pesan tidak terkirim?**
> Kemungkinan rate limit. Coba tingkatkan delay atau gunakan proxy.

**Q: Bisa dijalankan 24/7?**
> Ya, tapi disarankan jangan terlalu agresif untuk menghindari ban.

**Q: Proxy gratis dimana?**
> Cari di Google "free proxy list" atau [free-proxy-list.net](https://free-proxy-list.net)

---

## 📊 Contoh Output

```
═══════════════════════════════════════════════════════════════
  NGSPAM - STABLE & STEALTH MODE
═══════════════════════════════════════════════════════════════
  Target       : johndoe
  Pesan        : 50 pesan loaded
  Target Sukses: 100
  Delay        : 1 detik
  Proxies      : 10 loaded
  User Agents  : 7 loaded
═══════════════════════════════════════════════════════════════

Progress |████████████████████████████████████████| 100.0% [✓100 ✗5 ⏳3] (100/100) [2.5 req/s]

═══════════════════════════════════════════════════════════════
  📊 HASIL EKSEKUSI
═══════════════════════════════════════════════════════════════
  ✓ Sukses       : 100
  ⏳ Rate Limited : 3
  ✗ Gagal        : 5
  📈 Total        : 108
  📊 Success Rate : 92.59%
  ⏱️ Waktu        : 156.3 detik
═══════════════════════════════════════════════════════════════
```

---

## ⚠️ Disclaimer

> **PENTING**: Tool ini dibuat untuk tujuan **edukasi dan pengujian** saja.

- ✅ Gunakan hanya pada akun yang Anda miliki atau dengan izin
- ❌ Jangan gunakan untuk spam atau harassment
- ⚖️ Pengguna bertanggung jawab penuh atas penggunaan tool ini
- 🛡️ Developer tidak bertanggung jawab atas penyalahgunaan

---

## 🤝 Contributing

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📄 License

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

## 👨‍💻 Developer

<div align="center">

**Erzam Bayu**

[![GitHub](https://img.shields.io/badge/GitHub-@Erzambayu-black?style=flat&logo=github)](https://github.com/Erzambayu)

*"Code with passion, share with purpose"*

</div>

---

## ⭐ Support

Jika tool ini membantu, berikan ⭐ pada repository ini!

<div align="center">

**Made with ❤️ by Erzam Bayu**

</div>