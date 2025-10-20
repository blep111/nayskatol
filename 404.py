#!/usr/bin/env python3
"""
facebook_proxy_tool.py
----------------------
This script creates email (Mail.tm) and Facebook accounts using proxies.
Note: The Facebook registration code is for demonstration only.
"""

import threading
from queue import Queue, Empty
import requests
import random
import string
import json
import hashlib
from faker import Faker
import time

print('\033[1;35m' + f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
> › Github :- \033[1;36m@blep111\033[1;35m 
> › By      :- \033[1;36mgabhndsm\033[1;35m
> › This tool is supported with proxy’s
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""" + '\033[0m')

print('\x1b[38;5;208m⇼' * 60)
print('\x1b[38;5;22m•' * 60)
print('\x1b[38;5;22m•' * 60)
print('\x1b[38;5;208m⇼' * 60)

# Increase timeout values as needed.
REQUEST_TIMEOUT = 15

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def get_mail_domains(proxy=None):
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url, proxies=proxy, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            return response.json().get('hydra:member', [])
        else:
            print(f'\033[1;31m[×] Email Error : {response.text}\033[0m')
    except Exception as e:
        print(f'\033[1;31m[×] Error getting domains: {e}\033[0m')
    return None

def create_mail_tm_account(proxy=None):
    fake = Faker()
    mail_domains = get_mail_domains(proxy)
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password": password}
        try:
            response = requests.post(url, headers=headers, json=data, proxies=proxy, timeout=REQUEST_TIMEOUT)
            if response.status_code == 201:
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'\033[1;31m[×] Email Registration Error: {response.status_code} - {response.text}\033[0m')
        except Exception as e:
            print(f'\033[1;31m[×] Email API Error: {e}\033[0m')
    return None, None, None, None, None

def register_facebook_account(email, password, first_name, last_name, birthday, proxy=None):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    req['sig'] = hashlib.md5((sig + secret).encode()).hexdigest()
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req, proxy)
    # Log the full response for diagnostic purposes.
    print(f'\033[1;33m[!] Facebook API response: {reg}\033[0m')
    try:
        user_id = reg.get('new_user_id')
        token = reg.get('session_info', {}).get('access_token')
        if not user_id or not token:
            raise ValueError("Missing new_user_id or access_token in response")
        print(f'''\033[1;32m
-----------GENERATED-----------
EMAIL : {email}
ID : {user_id}
PASSWORD : {password}
NAME : {first_name} {last_name}
BIRTHDAY : {birthday} 
GENDER : {gender}
TOKEN : {token}
-----------GENERATED-----------
\033[0m''')
        with open('accounts_log.txt', 'a') as f:
            f.write(f'{email},{password},{first_name},{last_name},{birthday},{gender},{token}\n')
    except Exception as e:
        print(f'\033[1;31m[×] Facebook Registration Failed: {e}\033[0m')

def _call(url, params, proxy=None, post=True):
    global working_proxies
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    for attempt in range(3):  # Retry up to 3 times
        try:
            if post:
                response = requests.post(url, data=params, headers=headers, proxies=proxy, timeout=REQUEST_TIMEOUT)
            else:
                response = requests.get(url, params=params, headers=headers, proxies=proxy, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'\033[1;31m[×] API call returned: {response.status_code} - {response.text}\033[0m')
        except Exception as e:
            print(f'\033[1;31m[×] API call exception on attempt {attempt+1}: {e}\033[0m')
            if working_proxies:
                proxy = random.choice(working_proxies)
    return {}

def test_proxy(proxy, q, valid_proxies):
    if test_proxy_helper(proxy):
        valid_proxies.append(proxy)
    q.task_done()

def test_proxy_helper(proxy):
    try:
        response = requests.get('https://api.mail.tm', proxies=proxy, timeout=REQUEST_TIMEOUT)
        print(f'\033[1;32m[✓] Working proxy: {proxy["http"]}\033[0m')
        return response.status_code == 200
    except Exception as e:
        print(f'\033[1;31m[×] Bad proxy: {proxy["http"]} - {e}\033[0m')
        return False

def load_proxies():
    with open('proxies.txt', 'r') as file:
        proxy_list = [line.strip() for line in file if line.strip()]
    proxies = []
    for entry in proxy_list:
        if '@' in entry:
            user_pass, address = entry.split('@', 1)
            proxy_url = f'http://{user_pass}@{address}'
        else:
            proxy_url = f'http://{entry}'
        proxies.append({'http': proxy_url, 'https': proxy_url})
    return proxies

def get_working_proxies():
    proxies = load_proxies()
    valid_proxies = []
    q = Queue()
    for proxy in proxies:
        q.put(proxy)
    # Start 10 threads for testing proxies
    threads = []
    for _ in range(10):
        worker = threading.Thread(target=worker_test_proxy, args=(q, valid_proxies))
        worker.daemon = True
        worker.start()
        threads.append(worker)
    q.join()
    return valid_proxies

def worker_test_proxy(q, valid_proxies):
    while True:
        try:
            proxy = q.get_nowait()
        except Empty:
            break
        test_proxy(proxy, q, valid_proxies)

# === Main Execution ===
working_proxies = get_working_proxies()

if not working_proxies:
    print('\033[1;31m[×] No working proxies found. Please check proxies.txt\033[0m')
else:
    try:
        count = int(input('\033[1;34m[+] How many accounts do you want to generate? \033[0m'))
        for _ in range(count):
            proxy = random.choice(working_proxies)
            email, password, first_name, last_name, birthday = create_mail_tm_account(proxy)
            if all([email, password, first_name, last_name, birthday]):
                register_facebook_account(email, password, first_name, last_name, birthday, proxy)
                time.sleep(random.uniform(2, 5))  # sleep between accounts
    except Exception as e:
        print(f'\033[1;31m[×] Error: {e}\033[0m')

print('\x1b[38;5;208m⇼' * 60)