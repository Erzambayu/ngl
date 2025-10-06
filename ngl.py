import requests
import time
import random
import hashlib
import uuid
from datetime import datetime
import threading
import json
import pyfiglet
from colorama import Fore, Style, init
import os

init(autoreset=True)

class NgspamRyuhan:
    def __init__(self, username, message, max_attempts=1000, delay=1):
        self.username = username
        self.message = message
        self.max_attempts = max_attempts
        self.delay = delay
        self.counter = 0
        self.session = requests.Session()
        

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
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
    
    def generate_device_id(self):

        return hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:42]
    
    def get_formatted_time(self):

        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def send_single_message(self, attempt_number):

        try:
            formatted_time = self.get_formatted_time()
            device_id = self.generate_device_id()
            
            url = "https://ngl.link/api/submit"
            
            body = f"username={self.username}&question={self.message}&deviceId={device_id}&gameSlug=&referrer="
            
            print(f"{Fore.YELLOW}[{formatted_time}] {Fore.CYAN}[Attempt {attempt_number}] {Fore.WHITE}Sending request...")
            
            response = self.session.post(
                url,
                headers=self.headers,
                data=body,
                timeout=10
            )
            
            if response.status_code != 200:
                print(f"{Fore.YELLOW}[{formatted_time}] {Fore.RED}[Error] Rate limited - Status: {response.status_code}")
                return False, "rate_limited"
            else:
                self.counter += 1
                print(f"{Fore.YELLOW}[{formatted_time}] {Fore.GREEN}[Success] {Fore.WHITE}Message sent: {self.counter}")
                return True, "success"
                
        except requests.exceptions.RequestException as e:
            formatted_time = self.get_formatted_time()
            print(f"{Fore.YELLOW}[{formatted_time}] {Fore.RED}[Error] Request failed: {e}")
            return False, str(e)
    
    def run_educational_test(self):
        print(f"{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.GREEN}NGSPAM")
        print(f"{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.YELLOW}Target: {Fore.WHITE}{self.username}")
        print(f"{Fore.YELLOW}Message: {Fore.WHITE}{self.message}")
        print(f"{Fore.YELLOW}Max Attempts: {Fore.WHITE}{self.max_attempts}")
        print(f"{Fore.YELLOW}Delay: {Fore.WHITE}{self.delay} seconds")
        print(f"{Fore.CYAN}{'=' * 70}")
        
        successful_attempts = 0
        rate_limited_attempts = 0
        failed_attempts = 0
        
        for attempt in range(1, self.max_attempts + 1):
            success, reason = self.send_single_message(attempt)
            
            if success:
                successful_attempts += 1
            elif reason == "rate_limited":
                rate_limited_attempts += 1
                
                print(f"{Fore.MAGENTA}[Info] Waiting 25 seconds due to rate limit...")
                time.sleep(25)
                continue
            else:
                failed_attempts += 1
            
            if attempt < self.max_attempts:
                time.sleep(self.delay)
        
        print(f"\n{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.GREEN} RESULT SPAMING")
        print(f"{Fore.CYAN}{'=' * 70}")
        print(f"{Fore.GREEN}Successful attempts: {Fore.WHITE}{successful_attempts}")
        print(f"{Fore.YELLOW}Rate limited attempts: {Fore.WHITE}{rate_limited_attempts}")
        print(f"{Fore.RED}Failed attempts: {Fore.WHITE}{failed_attempts}")
        print(f"{Fore.CYAN}Total attempts: {Fore.WHITE}{self.max_attempts}")
        

        if self.max_attempts > 0:
            success_rate = (successful_attempts / self.max_attempts) * 100
            print(f"{Fore.MAGENTA}Success Rate: {Fore.WHITE}{success_rate:.2f}%")
        
        print(f"{Fore.CYAN}{'=' * 70}")

class AdvancedSecurityAnalyzer:
    
    @staticmethod
    def analyze_headers(target_url):
    
        try:
            response = requests.get(target_url, timeout=10)
            
            print(f"\n{Fore.CYAN}{'=' * 50}")
            print(f"{Fore.GREEN}SECURITY HEADERS ANALYSIS")
            print(f"{Fore.CYAN}{'=' * 50}")
            
            security_headers = {
                'Content-Security-Policy': 'Missing',
                'X-Frame-Options': 'Missing', 
                'X-Content-Type-Options': 'Missing',
                'Strict-Transport-Security': 'Missing',
                'X-XSS-Protection': 'Missing'
            }
            
            for header in security_headers:
                if header in response.headers:
                    security_headers[header] = response.headers[header]
                    print(f"{Fore.GREEN}✓ {header}: {Fore.WHITE}{response.headers[header]}")
                else:
                    print(f"{Fore.RED}✗ {header}: {Fore.YELLOW}Missing")
            
            return security_headers
            
        except Exception as e:
            print(f"{Fore.RED}Error during security analysis: {e}")
            return None

def display_banner():

    os.system("cls" if os.name == "nt" else "clear")
    
    try:
        banner = pyfiglet.figlet_format("NGSPAM", font="slant")
        print(Fore.CYAN + banner)
    except:
        print(f"{Fore.CYAN}{'=' * 80}")
        print(f"{Fore.GREEN}NGSPAMER")
        print(f"{Fore.CYAN}{'=' * 80}")
    
    print(Fore.MAGENTA + Style.BRIGHT + "✉️  NGL SPAMER".center(80))
    print(Fore.CYAN + "=" * 80)
    print(Fore.YELLOW + " Developer: " + Fore.WHITE + "Ryuhan Minamoto")
    print(Fore.YELLOW + "🔗 GitHub: " + Fore.WHITE + "@ryuhandev")
    print(Fore.YELLOW + "💧  Status: " + Fore.WHITE + "FREE PLAN")

    print(Fore.CYAN + "=" * 80)
    print()

def main():

    display_banner()
    
    print(f"\n{Fore.CYAN}Masukan data pengguna:")
    username = input(f"{Fore.YELLOW}Username target: {Fore.WHITE}").strip()
    
    if not username:
        print(f"{Fore.RED}Username tidak boleh kosong!")
        return
        
    message = input(f"{Fore.YELLOW}Pesan testing: {Fore.WHITE}").strip()
    
    if not message:
        print(f"{Fore.RED}Pesan tidak boleh kosong!")
        return
    
    try:
        max_attempts = int(input(f"{Fore.YELLOW}Max attempts (default 100): {Fore.WHITE}") or "100")
        delay = float(input(f"{Fore.YELLOW}Delay antara request detik (default 1): {Fore.WHITE}") or "1")
    except ValueError:
        print(f"{Fore.RED}Input tidak valid, menggunakan default values")
        max_attempts = 100
        delay = 1
    

    if max_attempts > 1000:
        print(f"{Fore.RED}Max attempts terlalu tinggi, dibatasi ke 1000 untuk safety")
        max_attempts = 1000
    
    if delay < 0.5:
        print(f"{Fore.YELLOW}Delay terlalu pendek, meningkatkan ke 0.5 detik untuk menghindari rate limit")
        delay = 0.5
    

    print(f"\n{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.GREEN}TARGET CONFIRMATION")
    print(f"{Fore.CYAN}{'=' * 50}")
    print(f"{Fore.YELLOW}Target: {Fore.WHITE}{username}")
    print(f"{Fore.YELLOW}Message: {Fore.WHITE}{message}")
    print(f"{Fore.YELLOW}Max Attempts: {Fore.WHITE}{max_attempts}")
    print(f"{Fore.YELLOW}Delay: {Fore.WHITE}{delay} detik")
    print(f"{Fore.CYAN}{'=' * 50}")
    
    confirm = input(f"\n{Fore.GREEN}ARE YOU SURE? (y/n): ").strip().lower()
    
    if confirm not in ['y', 'ya', 'yes']:
        print(f"{Fore.YELLOW}Testing dibatalkan.")
        return
    
    # Jalankan testing
    print(f"\n{Fore.GREEN}Start spamming...\n")
    Ryuhan = NgspamRyuhan(
        username=username,
        message=message,
        max_attempts=max_attempts,
        delay=delay
    )
    
    Ryuhan.run_educational_test()
   

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Script dihentikan oleh user.")
    except Exception as e:
        print(f"\n{Fore.RED}Terjadi error: {e}")
