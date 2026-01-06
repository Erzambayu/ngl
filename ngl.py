#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NGSPAM - Advanced NGL Spammer v7.0
Tool untuk mengirim pesan anonim ke NGL.link

Author: Erzam Bayu
GitHub: @Erzambayu
"""

import requests
import time
import random
import uuid
import threading
import sys
import os
import argparse

try:
    import pyfiglet
    PYFIGLET_AVAILABLE = True
except ImportError:
    PYFIGLET_AVAILABLE = False

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    # Fallback jika colorama tidak tersedia
    class Fore:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""


class ProgressBar:
    """Progress bar dengan statistik realtime"""
    
    def __init__(self, target_success, prefix='Progress', length=40, fill='█'):
        self.target_success = target_success
        self.prefix = prefix
        self.length = length
        self.fill = fill
        self.success = 0
        self.failed = 0
        self.rate_limited = 0
        self.total_attempts = 0
        self.lock = threading.Lock()
        self.start_time = time.time()

    def _draw_bar(self):
        """Render progress bar ke terminal"""
        try:
            percent = min(100, (100 * (self.success / float(self.target_success))))
            percent_str = f"{percent:.1f}"
            filled_length = min(self.length, int(self.length * self.success // self.target_success))
            bar = self.fill * filled_length + '-' * (self.length - filled_length)
            elapsed_time = time.time() - self.start_time
            req_per_sec = self.total_attempts / elapsed_time if elapsed_time > 0 else 0

            stats = f"{Fore.GREEN}✓{self.success} {Fore.RED}✗{self.failed} {Fore.YELLOW}⏳{self.rate_limited}"

            sys.stdout.write(f'\r{Fore.CYAN}{self.prefix} |{Fore.GREEN}{bar}{Fore.CYAN}| {percent_str}% [{stats}{Fore.CYAN}] ({self.success}/{self.target_success}) {Fore.MAGENTA}[{req_per_sec:.1f} req/s]{Fore.RESET}')
            sys.stdout.flush()
        except Exception:
            pass

    def start(self):
        """Mulai progress bar"""
        self._draw_bar()

    def increment(self, result):
        """Update progress bar dengan hasil terbaru"""
        with self.lock:
            self.total_attempts += 1
            if result == 'success':
                self.success += 1
            elif result == 'failed':
                self.failed += 1
            elif result == 'rate_limited':
                self.rate_limited += 1
            self._draw_bar()


class NgspamRyuhan:
    """Kelas utama untuk NGL Spammer"""
    
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    ]

    def __init__(self, username, messages, target_success=100, delay=1, proxies=None, rate_limit_delay=25):
        self.username = username
        self.messages = messages
        self.target_success = target_success
        self.delay = delay
        self.proxies = proxies or []
        self.rate_limit_delay = rate_limit_delay
        self.session = requests.Session()

        self.base_headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Referer": f"https://ngl.link/{username}",
            "Origin": "https://ngl.link"
        }

    @staticmethod
    def format_proxy(proxy):
        """Format proxy dengan prefix http:// jika belum ada"""
        proxy = proxy.strip()
        if proxy and not proxy.startswith(('http://', 'https://', 'socks4://', 'socks5://')):
            proxy = f"http://{proxy}"
        return proxy

    def validate_username(self):
        """Validasi apakah username ada di NGL.link"""
        try:
            response = requests.get(
                f"https://ngl.link/{self.username}",
                headers={"User-Agent": random.choice(self.USER_AGENTS)},
                timeout=10
            )
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def send_single_message(self):
        """Kirim satu pesan ke target"""
        proxy_dict = None
        if self.proxies:
            proxy = random.choice(self.proxies)
            proxy = self.format_proxy(proxy)
            proxy_dict = {'http': proxy, 'https': proxy}

        try:
            request_headers = self.base_headers.copy()
            request_headers['User-Agent'] = random.choice(self.USER_AGENTS)
            message_to_send = random.choice(self.messages)
            device_id = str(uuid.uuid4())
            
            url = "https://ngl.link/api/submit"
            body = f"username={self.username}&question={message_to_send}&deviceId={device_id}&gameSlug=&referrer="
            
            response = self.session.post(
                url,
                headers=request_headers,
                data=body.encode('utf-8'),
                timeout=15,
                proxies=proxy_dict
            )
            
            if response.status_code == 429:
                return "rate_limited"
            elif response.status_code != 200:
                return "failed"
            else:
                return "success"
                
        except requests.exceptions.ProxyError:
            return "failed"
        except requests.exceptions.Timeout:
            return "failed"
        except requests.exceptions.ConnectionError:
            return "failed"
        except requests.exceptions.RequestException:
            return "failed"
        except Exception:
            return "failed"

    def run(self):
        """Jalankan spam loop"""
        print(f"\n{Fore.CYAN}{'═' * 60}")
        print(f"{Fore.GREEN}  NGSPAM - STABLE & STEALTH MODE")
        print(f"{Fore.CYAN}{'═' * 60}")
        print(f"{Fore.YELLOW}  Target       : {Fore.WHITE}{self.username}")
        
        if len(self.messages) == 1:
            msg_display = self.messages[0][:40] + "..." if len(self.messages[0]) > 40 else self.messages[0]
            print(f"{Fore.YELLOW}  Pesan        : {Fore.WHITE}{msg_display}")
        else:
            print(f"{Fore.YELLOW}  Pesan        : {Fore.WHITE}{len(self.messages)} pesan loaded")
        
        print(f"{Fore.YELLOW}  Target Sukses: {Fore.WHITE}{self.target_success}")
        print(f"{Fore.YELLOW}  Delay        : {Fore.WHITE}{self.delay} detik")
        
        if self.proxies:
            print(f"{Fore.YELLOW}  Proxies      : {Fore.WHITE}{len(self.proxies)} loaded")
        
        print(f"{Fore.YELLOW}  User Agents  : {Fore.WHITE}{len(self.USER_AGENTS)} loaded")
        print(f"{Fore.CYAN}{'═' * 60}\n")

        progress_bar = ProgressBar(self.target_success)
        progress_bar.start()

        try:
            while progress_bar.success < self.target_success:
                result = self.send_single_message()
                progress_bar.increment(result)

                if result == "rate_limited":
                    print(f"\n{Fore.YELLOW}⚠️  Rate limit terdeteksi! Menunggu {self.rate_limit_delay} detik...")
                    for countdown in range(self.rate_limit_delay, 0, -1):
                        sys.stdout.write(f'\r{Fore.YELLOW}⏳ Menunggu: {Fore.WHITE}{countdown:2d}{Fore.YELLOW} detik tersisa...{Fore.RESET}')
                        sys.stdout.flush()
                        time.sleep(1)
                    sys.stdout.write(f'\r{" " * 50}\r')
                    print(f"{Fore.GREEN}✅ Selesai menunggu! Melanjutkan...{Fore.RESET}")
                    continue

                time.sleep(self.delay)

        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}⛔ DIHENTIKAN OLEH USER{Style.RESET_ALL}")

        # Tampilkan hasil akhir
        print(f"\n\n{Fore.CYAN}{'═' * 60}")
        print(f"{Fore.GREEN}  📊 HASIL EKSEKUSI")
        print(f"{Fore.CYAN}{'═' * 60}")
        print(f"{Fore.GREEN}  ✓ Sukses       : {Fore.WHITE}{progress_bar.success}")
        print(f"{Fore.YELLOW}  ⏳ Rate Limited : {Fore.WHITE}{progress_bar.rate_limited}")
        print(f"{Fore.RED}  ✗ Gagal        : {Fore.WHITE}{progress_bar.failed}")
        print(f"{Fore.CYAN}  📈 Total        : {Fore.WHITE}{progress_bar.total_attempts}")
        
        if progress_bar.total_attempts > 0:
            success_rate = (progress_bar.success / progress_bar.total_attempts) * 100
            print(f"{Fore.MAGENTA}  📊 Success Rate : {Fore.WHITE}{success_rate:.2f}%")
        
        elapsed = time.time() - progress_bar.start_time
        print(f"{Fore.CYAN}  ⏱️  Waktu        : {Fore.WHITE}{elapsed:.1f} detik")
        print(f"{Fore.CYAN}{'═' * 60}\n")


def display_banner():
    """Tampilkan banner aplikasi"""
    os.system("cls" if os.name == "nt" else "clear")
    
    if PYFIGLET_AVAILABLE:
        try:
            banner = pyfiglet.figlet_format("NGSPAM", font="slant")
            print(Fore.CYAN + banner)
        except Exception:
            print(f"{Fore.CYAN}{'═' * 60}")
            print(f"{Fore.GREEN}  NGSPAM")
            print(f"{Fore.CYAN}{'═' * 60}")
    else:
        print(f"{Fore.CYAN}{'═' * 60}")
        print(f"{Fore.GREEN}  NGSPAM - NGL SPAMMER")
        print(f"{Fore.CYAN}{'═' * 60}")

    print(Fore.MAGENTA + Style.BRIGHT + "  ✉️  NGL SPAMER v7.0".center(50))
    print(Fore.CYAN + "═" * 60)
    print(f"{Fore.YELLOW}  👨‍💻 Developer : {Fore.WHITE}Erzam Bayu")
    print(f"{Fore.YELLOW}  🔗 GitHub    : {Fore.WHITE}@Erzambayu")
    print(f"{Fore.YELLOW}  ⚡ Status    : {Fore.WHITE}STABLE & STEALTH MODE")
    print(Fore.CYAN + "═" * 60)
    print()


def load_file_lines(filepath, file_type="file"):
    """Load lines dari file dengan error handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        if lines:
            print(f"{Fore.GREEN}✓ Berhasil memuat {len(lines)} {file_type} dari '{filepath}'")
            return lines
        else:
            print(f"{Fore.RED}✗ File '{filepath}' kosong.")
            return []
    except FileNotFoundError:
        print(f"{Fore.RED}✗ File '{filepath}' tidak ditemukan.")
        return []
    except UnicodeDecodeError:
        # Coba encoding alternatif
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                lines = [line.strip() for line in f if line.strip()]
            if lines:
                print(f"{Fore.GREEN}✓ Berhasil memuat {len(lines)} {file_type} dari '{filepath}'")
                return lines
        except Exception:
            pass
        print(f"{Fore.RED}✗ Error membaca file '{filepath}' - encoding tidak didukung.")
        return []
    except Exception as e:
        print(f"{Fore.RED}✗ Error membaca file '{filepath}': {e}")
        return []


def interactive_mode():
    """Mode interaktif dengan input dari user"""
    display_banner()

    # Input username
    print(f"\n{Fore.CYAN}📝 Masukkan Data Target:")
    print(f"{Fore.CYAN}{'─' * 40}")
    
    username = input(f"{Fore.YELLOW}  Username target: {Fore.WHITE}").strip()
    if not username:
        print(f"{Fore.RED}✗ Username tidak boleh kosong!")
        return

    # Validasi username
    print(f"\n{Fore.CYAN}🔍 Memvalidasi username '{username}'...")
    spammer = NgspamRyuhan(username=username, messages=["test"])
    if not spammer.validate_username():
        print(f"{Fore.RED}✗ Username '{username}' tidak ditemukan di NGL.link!")
        confirm = input(f"{Fore.YELLOW}  Lanjutkan tetap? (y/n): {Fore.WHITE}").strip().lower()
        if confirm not in ['y', 'ya', 'yes']:
            print(f"{Fore.YELLOW}Dibatalkan.")
            return
    else:
        print(f"{Fore.GREEN}✓ Username valid!")

    # Pilih mode pesan
    print(f"\n{Fore.CYAN}📨 Pilih Mode Pesan:")
    print(f"{Fore.CYAN}{'─' * 40}")
    print(f"{Fore.WHITE}  [1] Teks Tunggal")
    print(f"{Fore.WHITE}  [2] Wordlist (file)")
    message_mode = input(f"{Fore.YELLOW}  Pilihan (default: 2): {Fore.WHITE}").strip() or '2'

    messages = []
    if message_mode == '1':
        single_message = input(f"{Fore.YELLOW}  Masukkan pesan: {Fore.WHITE}").strip()
        if not single_message:
            print(f"{Fore.RED}✗ Pesan tidak boleh kosong!")
            return
        messages = [single_message]
    else:
        default_wordlist = 'wordlist.txt'
        wordlist_file = input(f"{Fore.YELLOW}  Path wordlist (default: {default_wordlist}): {Fore.WHITE}").strip() or default_wordlist
        messages = load_file_lines(wordlist_file, "pesan")
        if not messages:
            return

    # Input target dan delay
    print(f"\n{Fore.CYAN}⚙️  Konfigurasi:")
    print(f"{Fore.CYAN}{'─' * 40}")
    
    try:
        target_input = input(f"{Fore.YELLOW}  Target sukses (default: 100): {Fore.WHITE}").strip()
        target_success = int(target_input) if target_input else 100
        
        delay_input = input(f"{Fore.YELLOW}  Delay per pesan dalam detik (default: 1): {Fore.WHITE}").strip()
        delay = float(delay_input) if delay_input else 1.0
    except ValueError:
        print(f"{Fore.YELLOW}⚠️  Input tidak valid, menggunakan default values.")
        target_success = 100
        delay = 1.0

    # Proxy
    proxies = []
    print(f"\n{Fore.CYAN}🌐 Proxy (opsional):")
    print(f"{Fore.CYAN}{'─' * 40}")
    use_proxies = input(f"{Fore.YELLOW}  Gunakan proxy? (y/n, default: n): {Fore.WHITE}").strip().lower()
    
    if use_proxies == 'y':
        proxy_file = input(f"{Fore.YELLOW}  Path file proxy: {Fore.WHITE}").strip()
        if proxy_file:
            proxies = load_file_lines(proxy_file, "proxy")

    # Konfirmasi
    print(f"\n{Fore.CYAN}{'═' * 50}")
    print(f"{Fore.GREEN}  📋 KONFIRMASI TARGET")
    print(f"{Fore.CYAN}{'═' * 50}")
    print(f"{Fore.YELLOW}  Target       : {Fore.WHITE}{username}")
    
    if len(messages) == 1:
        print(f"{Fore.YELLOW}  Pesan        : {Fore.WHITE}{messages[0][:40]}...")
    else:
        print(f"{Fore.YELLOW}  Pesan        : {Fore.WHITE}{len(messages)} pesan")
    
    print(f"{Fore.YELLOW}  Target Sukses: {Fore.WHITE}{target_success}")
    print(f"{Fore.YELLOW}  Delay        : {Fore.WHITE}{delay} detik")
    
    if proxies:
        print(f"{Fore.YELLOW}  Proxies      : {Fore.WHITE}{len(proxies)} loaded")
    
    print(f"{Fore.CYAN}{'═' * 50}")

    confirm = input(f"\n{Fore.GREEN}  Lanjutkan? (y/n): {Fore.WHITE}").strip().lower()
    if confirm not in ['y', 'ya', 'yes']:
        print(f"{Fore.YELLOW}Dibatalkan.")
        return

    # Jalankan spam
    spammer = NgspamRyuhan(
        username=username,
        messages=messages,
        target_success=target_success,
        delay=delay,
        proxies=proxies
    )
    spammer.run()


def cli_mode(args):
    """Mode command line dengan argparse"""
    print(f"\n{Fore.CYAN}🚀 NGSPAM CLI Mode")
    print(f"{Fore.CYAN}{'═' * 50}")

    # Load messages
    if args.message:
        messages = [args.message]
        print(f"{Fore.GREEN}✓ Menggunakan pesan tunggal")
    else:
        messages = load_file_lines(args.wordlist, "pesan")
        if not messages:
            print(f"{Fore.RED}✗ Tidak ada pesan untuk dikirim!")
            sys.exit(1)

    # Load proxies
    proxies = []
    if args.proxy:
        proxies = load_file_lines(args.proxy, "proxy")

    # Validasi username jika tidak di-skip
    if not args.skip_validate:
        print(f"\n{Fore.CYAN}🔍 Memvalidasi username '{args.username}'...")
        spammer = NgspamRyuhan(username=args.username, messages=["test"])
        if not spammer.validate_username():
            print(f"{Fore.RED}✗ Username '{args.username}' tidak ditemukan!")
            if not args.force:
                sys.exit(1)
            print(f"{Fore.YELLOW}⚠️  Melanjutkan dengan --force")
        else:
            print(f"{Fore.GREEN}✓ Username valid!")

    # Jalankan spam
    spammer = NgspamRyuhan(
        username=args.username,
        messages=messages,
        target_success=args.target,
        delay=args.delay,
        proxies=proxies,
        rate_limit_delay=args.rate_limit_delay
    )
    spammer.run()


def main():
    """Entry point utama"""
    parser = argparse.ArgumentParser(
        description='NGSPAM - Advanced NGL Spammer v7.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python ngl.py                                    # Mode interaktif
  python ngl.py -u johndoe -t 50                   # CLI mode dengan target 50
  python ngl.py -u johndoe -m "Hello!"             # Kirim pesan tunggal
  python ngl.py -u johndoe -w custom.txt -d 0.5    # Custom wordlist & delay

Dibuat oleh Erzam Bayu (@Erzambayu)
        """
    )
    
    parser.add_argument('-u', '--username', type=str, help='Username target NGL')
    parser.add_argument('-m', '--message', type=str, help='Pesan tunggal untuk dikirim')
    parser.add_argument('-w', '--wordlist', type=str, default='wordlist.txt', help='Path file wordlist (default: wordlist.txt)')
    parser.add_argument('-t', '--target', type=int, default=100, help='Target pesan sukses (default: 100)')
    parser.add_argument('-d', '--delay', type=float, default=1.0, help='Delay antar pesan dalam detik (default: 1.0)')
    parser.add_argument('-p', '--proxy', type=str, help='Path file proxy list')
    parser.add_argument('--rate-limit-delay', type=int, default=25, help='Delay saat terkena rate limit (default: 25)')
    parser.add_argument('--skip-validate', action='store_true', help='Skip validasi username')
    parser.add_argument('--force', action='store_true', help='Lanjutkan meskipun username tidak valid')
    
    args = parser.parse_args()

    try:
        if args.username:
            # CLI mode
            cli_mode(args)
        else:
            # Interactive mode
            interactive_mode()
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}⛔ Program dihentikan oleh user.{Style.RESET_ALL}")
        sys.exit(0)
    except EOFError:
        print(f"\n\n{Fore.RED}✗ Input stream bermasalah. Jalankan di terminal yang mendukung input.{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
