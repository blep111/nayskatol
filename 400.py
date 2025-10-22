#--> Author's Info
Author    = 'Gab'
Facebook  = 'https://www.facebook.com/profile.php?id=61581977649127'
Instagram = 'Gabx'
GitHub  = 'blep111'
Telegram   = 'showx'

#--> Colors
P = "\x1b[38;5;231m" # White
M = "\x1b[38;5;196m" # Red
H = "\x1b[38;5;46m"  # Green
A = '\x1b[38;5;248m' # Gray

#--> Import Modules & Run
try:
    import os, sys, time, re, datetime, random
    from datetime import datetime
except Exception as e:
    print(e)
    exit('\nAn error occurred!')
try:
    import requests
except Exception as e:
    os.system('pip install requests')
    import requests
try:
    import bs4
    from bs4 import BeautifulSoup as bs
except Exception as e:
    os.system('pip install bs4')
    import bs4
    from bs4 import BeautifulSoup as bs

#--> Global Variables
auth1 = 'Dapunta Khurayra X'
auth2 = 'Suci Maharani Putri'
reco = 'Do not recode, just use it as is.'
rede = 'I told you, do not recode it.'
key = len(auth1) * len(auth2) - len(auth1)
months = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
    '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
ok = 0
cp = 0
boys_name = [
    'Axel Lateef Noah', 'Anzel Qasim Wisthara', 'Basheer Malik Yazdan', 'Bernardus Clementine Christian',
    'Carel Vasco Zachariah', 'Cyrus Osmanth Elkanah', 'Damian Vasyl Isaac', 'Dominic Valdi Xander',
    'Ephraim Benedict Gevariel', 'El Fatih Ghazwan', 'Fawwaz Rafisqy Ezaz', 'Faheem Fakhri Isyraq',
    'Gianluca Nathanael Nadav', 'Haddad Ammar Ar-Rayyan', 'Istafa Tabriz Qiwam', 'Kenneth Krisantus Lazarus',
    'Nathanael Alfred William', 'Vaskylo Yeremia Clearesta', 'Xaferius Eliel Antonios', 'Yesaya Nathanael Liam'
]
girls_name = [
    'Atika Fithriya Tsabita', 'Alya Kinana Juwairiyah', 'Adzkiya Naila Taleetha', 'Adiva Arsyila Savina',
    'Aqeela Nabiha Sakhi', 'Bilqis Adzkiya Rana', 'Chayra Ainin Qulaibah', 'Caliana Fiona Syafazea',
    'Chaerunnisa Denia Athalla', 'Dhawiyah Nisrin Naziha', 'Dilara Adina Yuani', 'Farah Sachnaz Ashanty',
    'Ghariyah Zharufa Abidah', 'Hamna Nafisa Raihana', 'Hanin Raihana Syahira', 'Izza Hilyah Nafisah',
    'Kayla Zhara Qamela', 'Mahreen Shafana Almahyra', 'Rasahana Shafwa Ruqayah', 'Shakayla Aretha Shaima'
]

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():
        os.system('clear')
    elif "win" in sys.platform.lower():
        os.system('cls')

#--> Date and Time
def get_current_date():
    current_month = months[str(datetime.now().month)]
    current_date = f"{datetime.now().day} {current_month} {datetime.now().year}"
    return current_date.lower()

#--> Time Delay
def delay(seconds):
    for remaining in range(seconds, -1, -1):
        print(f'\r{P}Wait {remaining} seconds...', end='')
        sys.stdout.flush()
        time.sleep(1)

#--> Function to Generate Random User-Agent (example for Vivo devices)
def random_ua_vivo():
    chrome_version = f"{random.randint(112, 115)}.0.{random.randint(1000, 9999)}.{random.randint(10, 99)}"
    device_model = random.choice(['vivo 1951', 'vivo 1918', 'V2011A', 'V2047'])
    os_version = random.randint(10, 13)
    build_type = f"RP1A.{random.randint(100000, 250000)}.00{random.randint(1, 9)}"
    user_agent = (
        f"Mozilla/5.0 (Linux; Android {os_version}; {device_model} Build/{build_type}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36"
    )
    return user_agent

#--> Logo
def logo():
    print(f"{P}_________                      __        {M}________________ {P}")
    print(f"{P}\\_   ___ \\_______ ____ _____ _/  |_  ____{M}\\_   ____|___   \\{P}")
    print(f"{P}/    \\  \\/\\_  __ \\ __ \\\\__  \\\\   __\\/ __ \\{M}|    __)   |  _/{P}")
    print(f"{P}\\ {H}0.1 {P}\\____|  | \\/ ___/ / __ \\|  | \\  ___/{M}|   \\  |   |   \\{P}")
    print(f"{P} \\________/|__|  \\_____>______/__|  \\____>{M}|___/  |_______/{P}")
    print(f"{P}\n      ─────────────── {M}• {P}Dapunta Dev {M}• {P}───────────────\n")

#--> Main Menu
class Menu:
    def __init__(self):
        logo()
        self.display_main_menu()

    def display_main_menu(self):
        print(f"{M}[1] {P}Create Account")
        print(f"{M}[2] {P}Check Result")
        print(f"{M}[3] {P}Settings")
        print(f"{M}[4] {P}Bot")
        choice = input(f" {M}└─ {P}Choose {M}: {P}").lower()
        print('')
        if choice in ['1', '01', 'a']:
            MenuCreate()
        elif choice in ['2', '02', 'b']:
            MenuCheck()
        elif choice in ['3', '03', 'c']:
            not_available()
        elif choice in ['4', '04', 'd']:
            not_available()
        else:
            exit(f"{M}Enter a valid option!{P}")

#--> Placeholder for Not Available Features
def not_available():
    print(f"{P}Sorry, this feature {M}is not available yet{P}.")
    print(f"{P}Please wait for the next update...")
    print(f"{P}Thank you!")
    print(f"{P}- {M}Dapunta Dev{P}\n")

#--> Main Trigger
if __name__ == '__main__':
    clear()
    Menu()