import time
import os
import random
import sys

def clear_screen():
    os.system('clear')  # For Linux/MacOS
    # os.system('cls')  # Uncomment for Windows

# Colors for text styling
MERAH = '\033[31m'
HIJAU = '\033[32m'
KUNING = '\033[33m'
BIRU = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
PUTIH = '\033[37m'
RESET = '\033[0m'

def print_logo():
    logo = f"""
    {MAGENTA}
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠤⣤⣤⣤⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⠤⠤⠴⠶⠶⠶⠶
    ⢠⣤⣤⡄⣤⣤⣤⠄⣀⠉⣉⣙⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠘⣉⢡⣤⡤⠐⣶⡆⢶⠀⣶⣶⡦
    ⣄⢻⣿⣧⠻⠇⠋⠀⠋⠀⢘⣿⢳⣦⣌⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⣡⣴⣧⠻⣄⢸⣿⣿⡟⢁⡻⣸⣿⡿⠁
    ⠈⠃⠙⢿⣧⣙⠶⣿⣿⡷⢘⣡⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣷⣝⡳⠶⠶⠾⣛⣵⡿⠋⠀⠀
    ⠀⠀⠀⠉⠻⣿⣶⠂⠘⠛⠛⠛⢛⡛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠀⠉⠒⠛⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢻⡁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
    ┃       *** WELCOME TO TOOLS RPL  ***          ┃
    ┃                                           ┃
    ┃   Author: ANDHIKA ANGGA KURNIAWAN         ┃
    ┃   Class: X RPL 2                          ┃
    ┃   Tools: RPL                              ┃
    ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
    {RESET}
    """
    print(logo)

# Function to display the menu
def display_menu():
    print(HIJAU + """
    ┌────────────────────────────────────────────────────────┐
    │                   MAIN MENU                         │
    ├────────────────────────────────────────────────────────┤
    │ 1: LOGIN RPL                                          │
    │ 2: HACK SATELIT                                       │
    │ 3: HACK HP ORANG PAKE NOMER WA                       │
    │ 4: Gabut Mode (Dapet Inspirasi)                       │
    │ 5: SHOW SYSTEM STATUS                                 │
    │ 6: RUN SYSTEM DIAGNOSTIC                              │
    │ 7: FAKE CPU OVERLOAD                                  │
    │ 8: SIMULATE WIFI HACKING                              │
    │ 9: SHUTDOWN SYSTEM (Simulated)                        │
    │ 10: Display System Info                               │
    │ 11: SIMULATE DISK CLEANUP                            │
    │ 12: DISPLAY NETWORK INFO                              │
    │ 13: SIMULATE MEMORY USAGE                             │
    │ 14: DISPLAY FILE SYSTEM                               │
    │ 15: Exit                                              │
    └────────────────────────────────────────────────────────┘
    """ + RESET)

# Simulate "real" typing effect
def typing_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Simulate "real" hacking with more dynamic actions
def simulate_hack_action(action_name):
    print(f"{CYAN}Mencoba {action_name}...{RESET}")
    for i in range(5):
        time.sleep(0.5)
        typing_effect(f"Proses {'.' * (i + 1)}", delay=0.2)
    print(f"{HIJAU}Sukses! {action_name} berhasil dilakukan.{RESET}")
    time.sleep(1)

# Main function to run the program
def main():
    clear_screen()
    print_logo()
    while True:
        display_menu()
        choice = input(f"{HIJAU}[Pilih menu (1-15)] {RESET}")
        if choice == "1":
            print(f"{CYAN}[LOGIN] {RESET}")
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            if username == "admin" and password == "admin123":
                print(f"{HIJAU}Login berhasil!{RESET}")
            else:
                print(f"{MERAH}Login gagal. Coba lagi.{RESET}")
        elif choice == "2":
            simulate_hack_action("Hack Satelit")
        elif choice == "3":
            simulate_hack_action("Hack HP Orang Pake Nomor WA")
        elif choice == "4":
            print(f"{CYAN}[Gabut Mode] {RESET}")
            typing_effect("Dapatkan inspirasi!")
            typing_effect(f"{CYAN}Motivasi: {RESET} Setiap kegagalan adalah pelajaran.")
        elif choice == "5":
            typing_effect(f"{CYAN}[System Status] {RESET} Semua sistem berjalan dengan baik.")
        elif choice == "6":
            typing_effect(f"{CYAN}[System Diagnostic] {RESET} Semua sistem telah diperiksa dan berfungsi normal.")
        elif choice == "7":
            typing_effect(f"{CYAN}[CPU Overload] {RESET} CPU mengalami overload sementara. Mengatur ulang.")
            time.sleep(1)
        elif choice == "8":
            simulate_hack_action("Hack WiFi")
        elif choice == "9":
            print(f"{CYAN}[Shutdown System] {RESET} Sistem sedang dimatikan...")
            time.sleep(1)
            print(f"{CYAN}Sistem dimatikan dengan sukses.{RESET}")
        elif choice == "10":
            typing_effect(f"{CYAN}[System Info] {RESET} Sistem operasi: Linux, RAM: 16 GB, CPU: Intel i7.")
        elif choice == "11":
            typing_effect(f"{CYAN}[Disk Cleanup] {RESET} Membersihkan file sampah...")
            time.sleep(1)
            print("Pembersihan selesai.")
        elif choice == "12":
            typing_effect(f"{CYAN}[Network Info] {RESET} IP: 192.168.0.1, MAC: 00:1A:2B:3C:4D:5E")
        elif choice == "13":
            typing_effect(f"{CYAN}[Memory Usage] {RESET} Menggunakan 8 GB dari 16 GB.")
        elif choice == "14":
            typing_effect(f"{CYAN}[File System] {RESET} Disk: 500 GB, Digunakan: 300 GB, Sisa: 200 GB.")
        elif choice == "15":
            print(f"{MAGENTA}Terima kasih telah menggunakan program ini!{RESET}")
            break
        else:
            print(f"{MERAH}Pilihan tidak valid, coba lagi.{RESET}")
        time.sleep(1)  # Pause before showing the menu again

if __name__ == "__main__":
    main()
   