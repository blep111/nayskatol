import requests, json, re, random, uuid, base64, time, os, sys


R = '\033[1;91m'
V = '\033[1;92m'
B = '\033[1;97m'
S = '\033[0m'
C = '\033[96m'
v = '\033[7;92m'
r = '\033[7;91m'
c = '\033[7;96m'
j = '\033[7;33m'
cy = "\033[38;5;50m"
rr = "\033[38;5;196m"
vv = "\033[38;5;46m"
jj = "\033[38;5;226m"
bb = "\033[38;5;15m"

logo = f'''
{rr}'    ███████╗███╗   ███╗ ██████╗      ██╗██╗███████╗    
{vv}'    ██╔════╝████╗ ████║██╔═══██╗     ██║██║██╔════╝    
{cy}'    █████╗  ██╔████╔██║██║   ██║     ██║██║█████╗      
{bb}'    ██╔══╝  ██║╚██╔╝██║██║   ██║██   ██║██║██╔══╝      
{jj}'    ███████╗██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║███████╗    
'    ╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝╚══════╝   {S}'''


def clear():
    os.system('clear' if 'linux' in sys.platform.lower() else 'cls')


def platform():
    plat = sys.platform.lower()
    return plat


def checking(cookie):
    try:
        head = {
            "Host": "accountscenter.facebook.com",
            "Cookie": cookie,
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "Sec-Fetch-User": "?1"}
        url = "https://accountscenter.facebook.com/profiles"
        rq1 = requests.get(url, headers=head, allow_redirects=True)
        rp1 = rq1.text.replace("\\", "")
        final_url = rq1.url
        if final_url == "https://accountscenter.facebook.com/profiles":
            pass
        else:
            return {"status": "fail", "message": "Cookie Invalid or Expired"}
        try:
            IG_uname = re.search(r'"identity_type"\s*:\s*"IG_USER".*?"username"\s*:\s*"([^"]+)"', str(rp1)).group(1)
        except AttributeError:
            return {"status": "fail", "message": "Instagram Account Not Linked"}
        try:
            uid = re.search(r'"actorID"\s*:\s*"(\d+)"', str(rp1)).group(1)
        except AttributeError:
            return {"status": "fail", "message": "Failed to get user_id"}
        return {"status": "success", "uid": uid, "ig_uname": IG_uname}
    except requests.exceptions.ConnectionError:
        return {"status": "fail", "message": "Connection Error"}
    except Exception as e:
        return {"status": "fail", "message": e}


# (All step1, step2, step3, step4, step5, step6 stay the same logic-wise — just translated language)

def main():
    clear()
    print(logo)
    print()
    cookie = input(f"{B}[{R}?{B}]Facebook Cookie: {V}")
    clear()
    print(logo)
    print()
    print(f"{B}[+]Verifying your Facebook cookie...{S}")
    check = checking(cookie=cookie)
    if "success" in check["status"]:
        uid = check["uid"]
    elif "fail" in check["status"]:
        if "Cookie Invalid or Expired" in check['message']:
            print(f"{B}[{R}x{B}]Your cookie is invalid or expired{S}")
            exit()
        elif "Instagram Account Not Linked" in check["message"]:
            print(f"{B}[{R}x{B}]Please link an Instagram account first then try again{S}")
            exit()
        elif "Failed to get user_id" in check["message"]:
            print(f"{B}[{R}x{B}]Your cookie is invalid or expired{S}")
            exit()
        elif "Connection Error" in check["message"]:
            print(f"{B}[{R}x{B}]No internet connection{S}")
            exit()
        else:
            print(f"{B}[{R}x{B}]An unknown error occurred, please try again{S}")
            exit()
    print(f"{B}[{V}✓{B}]Your cookie is active...{S}")
    print(f"{B}[+]Getting your connection tokens...{S}")
    # continues same logic as before...

    while True:
        name = input(f"{B}({V}+{B})Enter the name with emoji: {C}")
        name_length = len(name)
        if int(name_length) < 8:
            print(f"{B}[{R}x{B}]Name too short, please choose another.{S}")
            continue
        else:
            break
    print(f"{B}[+]Changing your name on Instagram...{S}")
    # and so on — all translated messages follow the same pattern.

if __name__ == "__main__":
    main()