import requests
import time
import random
import hashlib
import uuid
from datetime import datetime
import threading
import pyfiglet
from colorama import Fore, Style, init
import os
import sys

init(autoreset=True)

class ProgressBar:
    def __init__(self, total, prefix='Progress', length=40, fill='█'):
        self.total = total
        self.prefix = prefix
        self.length = length
        self.fill = fill
        self.success = 0
        self.failed = 0
        self.rate_limited = 0
        self.total_attempts = 0
        self.lock = threading.Lock() # Lock is still used for single-thread safety, good practice
        self.start_time = time.time()

    def _draw_bar(self):
        # Progress is now based on total attempts
        percent = ("{0:.1f}").format(100 * (self.total_attempts / float(self.total)))
        filled_length = int(self.length * self.total_attempts // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        elapsed_time = time.time() - self.start_time
        req_per_sec = self.total_attempts / elapsed_time if elapsed_time > 0 else 0

        stats = f"{Fore.GREEN}S:{self.success} {Fore.RED}F:{self.failed} {Fore.YELLOW}R:{self.rate_limited}{Fore.CYAN}"

        sys.stdout.write(f'\r{Fore.CYAN}{self.prefix} |{Fore.GREEN}{bar}{Fore.CYAN}| {percent}% [{stats}] ({self.total_attempts}/{self.total}) {Fore.MAGENTA}[{req_per_sec:.1f} req/s]')
        sys.stdout.flush()

    def start(self):
        self._draw_bar()

    def increment(self, result):
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
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    ]

    def __init__(self, username, messages, max_attempts=100, delay=1, proxies=None):
        self.username = username
        self.messages = messages
        self.max_attempts = max_attempts
        self.delay = delay
        self.proxies = proxies or []
        self.session = requests.Session()

        self.base_headers = {
            "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest", "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
            "Referer": f"https://ngl.link/{username}", "Origin": "https://ngl.link"
        }
    
    def send_single_message(self):
        proxy_dict = None
        if self.proxies:
            proxy = random.choice(self.proxies)
            proxy_dict = {'http': proxy, 'https': proxy}
        try:
            request_headers = self.base_headers.copy()
            request_headers['User-Agent'] = random.choice(self.USER_AGENTS)
            message_to_send = random.choice(self.messages)
            device_id = str(uuid.uuid4())
            url = "https://ngl.link/api/submit"
            body = f"username={self.username}&question={message_to_send}&deviceId={device_id}&gameSlug=&referrer="
            response = self.session.post(url, headers=request_headers, data=body, timeout=10, proxies=proxy_dict)
            if response.status_code != 200:
                # No need to sleep here, main loop handles delay
                return "rate_limited"
            else:
                return "success"
        except (requests.exceptions.ProxyError, requests.exceptions.RequestException):
            return "failed"

    def run_educational_test(self):
        print(f"{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.GREEN}NGSPAM - STABLE & STEALTH MODE")
        print(f"{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.YELLOW}Target: {Fore.WHITE}{self.username}")
        if len(self.messages) == 1:
            print(f"{Fore.YELLOW}Message: {Fore.WHITE}{self.messages[0]}")
        else:
            print(f"{Fore.YELLOW}Messages: {Fore.WHITE}{len(self.messages)} loaded")
        print(f"{Fore.YELLOW}Attempts: {Fore.WHITE}{self.max_attempts}")
        print(f"{Fore.YELLOW}Delay: {Fore.WHITE}{self.delay} seconds")
        if self.proxies: print(f"{Fore.YELLOW}Proxies: {Fore.WHITE}{len(self.proxies)} loaded")
        print(f"{Fore.YELLOW}User Agents: {Fore.WHITE}{len(self.USER_AGENTS)} loaded")
        print(f"{Fore.CYAN}{'=' * 70}")
        print()

        progress_bar = ProgressBar(self.max_attempts)
        progress_bar.start()

        try:
            for i in range(self.max_attempts):
                result = self.send_single_message()
                progress_bar.increment(result)
                
                # Don't sleep on the last attempt
                if i < self.max_attempts - 1:
                    time.sleep(self.delay)

        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}TERMINATING...{Style.RESET_ALL}")
        
        print() # Newline after progress bar

        print(f"\n{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.GREEN} EXECUTION COMPLETE")
        print(f"{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.GREEN}Successful: {Fore.WHITE}{progress_bar.success}")
        print(f"{Fore.YELLOW}Rate Limited: {Fore.WHITE}{progress_bar.rate_limited}")
        print(f"{Fore.RED}Failed: {Fore.WHITE}{progress_bar.failed}")
        print(f"{Fore.CYAN}Total Attempts: {Fore.WHITE}{progress_bar.total_attempts}")
        if progress_bar.total_attempts > 0:
            success_rate = (progress_bar.success / progress_bar.total_attempts) * 100
            print(f"{Fore.MAGENTA}Success Rate: {Fore.WHITE}{success_rate:.2f}%")
        print(f"{Fore.CYAN}{'=' * 70}")

def display_banner():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        banner = pyfiglet.figlet_format("NGSPAM", font="slant")
        print(Fore.CYAN + banner)
    except:
        print(f"{Fore.CYAN}{'=' * 80}")
        print(f"{Fore.GREEN}NGSPAMER")
        print(f"{Fore.CYAN}{'=' * 80}")
    
    print(Fore.MAGENTA + Style.BRIGHT + "✉️  NGL SPAMER v6.0".center(80))
    print(Fore.CYAN + "=" * 80)
    print(Fore.YELLOW + " Developer: " + Fore.WHITE + "Ryuhan Minamoto")
    print(Fore.YELLOW + "🔗 GitHub: " + Fore.WHITE + "@ryuhandev")
    print(Fore.YELLOW + "⚡️ Status: " + Fore.WHITE + "STABLE & STEALTH MODE")
    print(Fore.CYAN + "=" * 80)
    print()

def main():
    display_banner()
    
    print(f"\n{Fore.CYAN}Masukan data pengguna:")
    username = input(f"{Fore.YELLOW}Username target: {Fore.WHITE}").strip()
    if not username: return

    messages = []
    print(f"\n{Fore.CYAN}Pilih mode pesan:")
    message_mode = input(f"{Fore.YELLOW}[1] Teks Tunggal, [2] Wordlist (default: 2): {Fore.WHITE}").strip() or '2'

    if message_mode == '1':
        single_message = input(f"{Fore.YELLOW}Masukan pesan tunggal: {Fore.WHITE}").strip()
        if not single_message: print(f"{Fore.RED}Pesan tidak boleh kosong!"); return
        messages = [single_message]
    else:
        default_wordlist = 'wordlist.txt'
        wordlist_file = input(f"{Fore.YELLOW}Masukan path file wordlist (default: {default_wordlist}): {Fore.WHITE}").strip() or default_wordlist
        try:
            with open(wordlist_file, 'r', encoding='utf-8') as f:
                messages = [line.strip() for line in f if line.strip()]
            if messages: print(f"{Fore.GREEN}Berhasil memuat {len(messages)} pesan dari '{wordlist_file}'.")
            else: print(f"{Fore.RED}File wordlist '{wordlist_file}' kosong."); return
        except FileNotFoundError: print(f"{Fore.RED}Error: File wordlist '{wordlist_file}' tidak ditemukan."); return
        except Exception as e: print(f"{Fore.RED}Terjadi error saat membaca file wordlist: {e}"); return

    try:
        max_attempts = int(input(f"\n{Fore.YELLOW}Jumlah Percobaan (default 100): {Fore.WHITE}") or "100")
        delay = float(input(f"{Fore.YELLOW}Jeda waktu per pesan (detik, cth: 1): {Fore.WHITE}") or "1")
    except ValueError:
        print(f"{Fore.RED}Input tidak valid, menggunakan default values.")
        max_attempts = 100
        delay = 1

    proxies = []
    use_proxies = input(f"\n{Fore.CYAN}Gunakan proxy? (y/n, default n): {Fore.WHITE}").strip().lower()
    if use_proxies == 'y':
        proxy_file = input(f"{Fore.YELLOW}Masukan path file proxy (.txt): {Fore.WHITE}").strip()
        try:
            with open(proxy_file, 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            if proxies: print(f"{Fore.GREEN}Berhasil memuat {len(proxies)} proxy.")
            else: print(f"{Fore.RED}File proxy kosong atau tidak valid.")
        except FileNotFoundError: print(f"{Fore.RED}Error: File proxy '{proxy_file}' tidak ditemukan.")
        except Exception as e: print(f"{Fore.RED}Terjadi error saat membaca file proxy: {e}")

    print(f"\n{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.GREEN}TARGET CONFIRMATION")
    print(f"{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.YELLOW}Target: {Fore.WHITE}{username}")
    if len(messages) == 1: print(f"{Fore.YELLOW}Message: {Fore.WHITE}{messages[0]}")
    else: print(f"{Fore.YELLOW}Messages: {Fore.WHITE}{len(messages)} loaded")
    print(f"{Fore.YELLOW}Attempts: {Fore.WHITE}{max_attempts}")
    print(f"{Fore.YELLOW}Delay: {Fore.WHITE}{delay} seconds")
    if proxies: print(f"{Fore.YELLOW}Proxies: {Fore.WHITE}{len(proxies)} loaded")
    print(f"{Fore.CYAN}{'=' * 50}")
    
    confirm = input(f"\n{Fore.GREEN}ARE YOU SURE? (y/n): ").strip().lower()
    if confirm not in ['y', 'ya', 'yes']: print(f"{Fore.YELLOW}Testing dibatalkan."); return
    
    Ryuhan = NgspamRyuhan(
        username=username, messages=messages, max_attempts=max_attempts,
        delay=delay, proxies=proxies
    )
    
    Ryuhan.run_educational_test()

if __name__ == "__main__":
    main()
