import requests
import random
import time
import re
import base64
import uuid
import json
from typing import Any, Dict, List

# ================== DEFAULT CONFIG (preserve names) ===================
auto_follow = True
config = {
    "cookie": "",
    "reactType": [],
}

# default target UID (preserved original subscribee id)
default_target_uid = "61557030103517"

# ================== REACTION TABLE (unchanged) ===================
reactTable = {}
reactTable[1] = ["LIKE", "1635855486666999", "👍"]
reactTable[2] = ["LOVE", "1678524932434102", "❤"]
reactTable[3] = ["WOW", "478547315650144", "😮"]
reactTable[4] = ["HAHA", "115940658764963", "😆"]
reactTable[7] = ["SAD", "908563459236466", "😢"]
reactTable[8] = ["ANGRY", "444813342392137", "😡"]
reactTable[16] = ["CARE", "613557422527858", "🤗"]


# ================== Lib class (preserve) ===================
class Lib:
    def __init__(self):
        pass

    def home(self) -> str:
        fetch = req.get("https://www.facebook.com/home.php?sk=h_chr")
        return fetch.text

    def random(self, a: List[Any]) -> int:
        return random.randint(0, len(a) - 1) if a else None

    def findFeed(self, a: str) -> List[str]:
        m = re.findall(r'"feedback_id":"(.*?)"', a)
        if not m:
            return []
        out = []
        for item in m:
            if item not in out:
                out.append(item)
        return out

    def findOne(self, a: str, b: re.Pattern) -> str:
        match = re.search(b, a)
        if not match:
            raise ValueError("Pattern not found")
        return match.group(1)

    def randomBase64(self, length: int) -> str:
        arr = bytearray(length)
        for i in range(length):
            arr[i] = random.getrandbits(8)
        return base64.b64encode(bytes(arr)).decode("ascii")

    def randomDigitString(self, length: int) -> str:
        return "".join(str(random.randint(0, 9)) for _ in range(length))

    def randomString(self, length: int) -> str:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        return "".join(random.choice(chars) for _ in range(length))

    def uuidv4(self) -> str:
        return str(uuid.uuid4())


lib = Lib()  # instantiate before Req class uses it


# ================== Req class (preserve) ===================
class Req:
    def __init__(self, cookies: str = ""):
        self.prp = {
            "muteHttpExceptions": True,
            "method": "GET",
            "followRedirects": False,
            "headers": {
                "Dpr": "1",
                "Viewport-Width": "958",
                "Sec-Ch-Ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "Windows",
                "Sec-Ch-Prefers-Color-Scheme": "dark",
                "Accept-Language": "en-US,en;q=0.9",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/139.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                          "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Accept-Encoding": "gzip, deflate",
            },
        }
        self.session = requests.Session()
        if cookies:
            self.check(cookies)

    def get(self, url: str) -> requests.Response:
        headers = self.prp["headers"].copy()
        return self.session.get(url, headers=headers, allow_redirects=False, timeout=30)

    def postql(self, data: Dict[str, Any], fn: str) -> requests.Response:
        head = {
            "Sec-Ch-Ua-Full-Version-List": "",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
            "X-Fb-Friendly-Name": fn,
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Model": '""',
            "X-Asbd-Id": lib.randomDigitString(6),
            "X-Fb-Lsd": data.get("lsd", ""),
            "Sec-Ch-Prefers-Color-Scheme": "dark",
            "User-Agent": self.prp["headers"]["User-Agent"],
            "Content-Type": "application/x-www-form-urlencoded",
            "Sec-Ch-Ua-Platform-Version": "",
            "Accept": "*/*",
            "Origin": "https://www.facebook.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.facebook.com/",
            "Accept-Encoding": "gzip, deflate",
        }
        cookie_val = self.prp["headers"].get("cookie") or ""
        if cookie_val:
            head["Cookie"] = cookie_val

        body = {}
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                body[k] = json.dumps(v)
            else:
                body[k] = str(v)

        response = self.session.post(
            "https://www.facebook.com/api/graphql/",
            data=body,
            headers=head,
            allow_redirects=True,
            timeout=30,
        )
        return response

    def check(self, c: str) -> None:
        try:
            if c.startswith("http://") or c.startswith("https://"):
                r = self.get(c)
                cookie_text = r.text
                self.prp["headers"]["cookie"] = cookie_text
                self.session.headers.update({"Cookie": cookie_text})
            else:
                self.prp["headers"]["cookie"] = c
                self.session.headers.update({"Cookie": c})
        except Exception:
            self.prp["headers"]["cookie"] = c
            self.session.headers.update({"Cookie": c})


req = Req(config["cookie"])  # instantiate after defining Req


# ================== Main start() (logic preserved) ===================
def start(target_uid: str):
    st = int(time.time() * 1000)
    try:
        print(
            "\033[4;34m⣏⡱ ⢀⡀ ⣰⡀ ⣏⡱ ⢀⡀ ⢀⣀ ⢀⣀ ⣰⡀\n ⠧⠜ ⠣⠜ ⠘⠤ ⠇⠱ ⠣⠭ ⠣⠼ ⠣⠤ ⠘⠤\n     [ S T A R T I N G ]"
        )

        a = lib.home()
        feedback_ids = lib.findFeed(a)
        cursor = lib.findOne(a, re.compile(r'"cursor":"(.*?)"'))
        hsi = lib.findOne(a, re.compile(r'"hsi":"(.*?)"'))
        hasess = lib.findOne(a, re.compile(r'"haste_session":"(.*?)"'))
        dtsg = lib.findOne(a, re.compile(r'{"dtsg":{"token":"(.*?)"'))
        acc_id = lib.findOne(a, re.compile(r'"ACCOUNT_ID":"(.*?)"'))
        jaz = lib.randomDigitString(5)
        lsd = lib.randomString(22)
        timestamp = int(time.time() * 1000)
        rev = str(timestamp - 729984972)

        payload = {
            "av": acc_id,
            "__aaid": "0",
            "__user": acc_id,
            "__a": "1",
            "__req": lib.randomString(2),
            "__hs": hasess,
            "dpr": "1",
            "__ccg": "EXCELLENT",
            "__rev": rev,
            "__s": ":".join(
                [lib.randomString(6), lib.randomString(6), lib.randomString(6)]
            ).lower(),
            "__hsi": hsi,
            "__dyn": lib.randomBase64(119),
            "__csr": lib.randomBase64(457),
            "__hsdp": lib.randomBase64(337),
            "__hblp": lib.randomBase64(343),
            "__sjsp": lib.randomBase64(169),
            "__comet_req": "15",
            "fb_dtsg": dtsg,
            "jazoest": jaz,
            "lsd": lsd,
            "__spin_r": rev,
            "__spin_b": "trunk",
            "__spin_t": timestamp,
            "__crn": "comet.fbweb.CometHomeRoute",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "CometNewsFeedPaginationQuery",
            "variables": {
                "RELAY_INCREMENTAL_DELIVERY": True,
                "clientQueryId": lib.uuidv4(),
                "clientSession": None,
                "connectionClass": "EXCELLENT",
                "count": 15,
                "cursor": cursor,
                "experimentalValues": None,
                "feedLocation": "NEWSFEED",
                "feedStyle": "DEFAULT",
                "feedbackSource": 1,
                "focusCommentID": None,
                "orderby": ["TOP_STORIES"],
                "privacySelectorRenderLocation": "COMET_STREAM",
                "recentVPVs": [],
                "refreshMode": "WARM",
                "renderLocation": "homepage_stream",
                "scale": 1,
                "shouldChangeBRSLabelFieldName": True,
                "shouldChangeSponsoredAuctionDistanceFieldName": True,
                "shouldChangeSponsoredDataFieldName": True,
                "shouldObfuscateCategoryField": False,
                "useDefaultActor": False,
            },
            "server_timestamps": True,
            "doc_id": "24313348174994672",
        }

        hasil_resp = req.postql(payload, "CometNewsFeedPaginationQuery")
        hasil_text = getattr(hasil_resp, "text", str(hasil_resp))

        found = lib.findFeed(hasil_text)
        extra_ids = []
        for x in found:
            try:
                idv = lib.findOne(x, re.compile(r'"feedback_id":"(.*?)"'))
                if len(idv) <= 36:
                    extra_ids.append(idv)
            except Exception:
                pass
        feedback_ids = feedback_ids + extra_ids

        if auto_follow:
            try:
                follow_payload = {
                    "av": acc_id,
                    "__aaid": "0",
                    "__user": acc_id,
                    "__a": "1",
                    "__req": lib.randomString(2),
                    "__hs": hasess,
                    "dpr": "1",
                    "__ccg": "EXCELLENT",
                    "__rev": rev,
                    "__s": ":".join(
                        [lib.randomString(6), lib.randomString(6), lib.randomString(6)]
                    ).lower(),
                    "__hsi": hsi,
                    "__dyn": lib.randomBase64(119),
                    "__csr": lib.randomBase64(457),
                    "__hsdp": lib.randomBase64(337),
                    "__hblp": lib.randomBase64(337),
                    "__sjsp": lib.randomBase64(169),
                    "__comet_req": "15",
                    "fb_dtsg": dtsg,
                    "jazoest": jaz,
                    "lsd": lsd,
                    "__spin_r": rev,
                    "__spin_b": "trunk",
                    "__spin_t": str(timestamp),
                    "__crn": "comet.fbweb.CometHomeRoute",
                    "fb_api_caller_class": "RelayModern",
                    "fb_api_req_friendly_name": "CometUserFollowMutation",
                    "variables": json.dumps(
                        {
                            "input": {
                                "attribution_id_v2": f"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_search_bar,{timestamp},{lib.randomDigitString(6)},,,",
                                "is_tracking_encrypted": False,
                                "subscribe_location": "PROFILE",
                                "subscribee_id": target_uid,
                                "tracking": None,
                                "actor_id": acc_id,
                                "client_mutation_id": "3",
                            }
                        }
                    ),
                    "server_timestamps": True,
                    "doc_id": "31095708380043916",
                }
                req.postql(follow_payload, "CometUserFollowMutation")
            except Exception:
                pass

    except Exception as e:
        print("EN: Cookies invalid.", str(e))

    # Reaction loop (preserved)
    try:
        for idx, fid in enumerate(feedback_ids):
            choice_index = lib.random(config["reactType"])
            reacts = config["reactType"][choice_index]
            react_id = reactTable[reacts][1]

            rpl = {
                "av": acc_id,
                "__aaid": "0",
                "__user": acc_id,
                "__a": "1",
                "__req": lib.randomString(2),
                "__hs": hasess,
                "dpr": "1",
                "__ccg": "EXCELLENT",
                "__rev": rev,
                "__s": ":".join(
                    [lib.randomString(6), lib.randomString(6), lib.randomString(6)]
                ).lower(),
                "__hsi": hsi,
                "__dyn": lib.randomBase64(119),
                "__csr": lib.randomBase64(457),
                "__hsdp": lib.randomBase64(337),
                "__hblp": lib.randomBase64(337),
                "__sjsp": lib.randomBase64(169),
                "__comet_req": "15",
                "fb_dtsg": dtsg,
                "jazoest": jaz,
                "lsd": lsd,
                "__spin_r": rev,
                "__spin_b": "trunk",
                "__spin_t": str(timestamp),
                "__crn": "comet.fbweb.CometHomeRoute",
                "fb_api_caller_class": "RelayModern",
                "fb_api_req_friendly_name": "CometUFIFeedbackReactMutation",
                "variables": json.dumps(
                    {
                        "input": {
                            "attribution_id_v2": f"CometHomeRoot.react,comet.home,via_cold_start,{timestamp},{lib.randomDigitString(6)},,,",
                            "feedback_id": fid,
                            "feedback_reaction_id": react_id,
                            "feedback_source": "MEDIA_VIEWER",
                            "is_tracking_encrypted": False,
                            "tracking": [],
                            "session_id": lib.uuidv4(),
                            "actor_id": acc_id,
                            "client_mutation_id": "4",
                        },
                        "useDefaultActor": False,
                    }
                ),
                "server_timestamps": True,
                "doc_id": "24034997962776771",
            }

            res = req.postql(rpl, "CometUFIFeedbackReactMutation")
            status_code = getattr(res, "status_code", None)
            status = "Success" if status_code == 200 else "Failed"
            print(
                f"--- React {status} ---\nPost {idx+1}/{len(feedback_ids)}\nPost Feedback ID : {fid}\nReact            : {reactTable[reacts][2]} ({reactTable[reacts][0]})\n---------------------"
            )
    except Exception as e:
        print("Error during reacting loop:", str(e))

    print(
        f"[ Reacts completed | Time elapsed: {(int(time.time()*1000) - st)/1000.0} second(s) ]"
    )


# ================== Interactive prompts (preserved) ===================
def interactive_setup():
    global config, auto_follow, req, lib

    print("\033[34m<+++COOKIE SESSION+++>")
    cookie_input = input("\033[32mEnter your cookie: ").strip()
    if cookie_input:
        config["cookie"] = cookie_input

    print("REACTION TYPE!:", config["reactType"])
    rt_input = input("\033[32mENTER REACTION TYPE! (1-8) ex 1: ").strip()
    if rt_input:
        try:
            parts = [int(x.strip()) for x in rt_input.split(",") if x.strip()]
            if parts:
                config["reactType"] = parts
        except Exception as e:
            print("Invalid reactType input, keeping default.", str(e))

    af_input = input("\033[32mAUTO FOLLOW (Y/N): ").strip().lower()
    if af_input in ["y", "yes"]:
        auto_follow = True
    elif af_input in ["n", "no"]:
        auto_follow = False

    target_input = input(f"\033[32mENTER TARGET UID: ").strip()
    target_uid = target_input if target_input else default_target_uid

    req = Req(config["cookie"])
    lib = Lib()
    print("Setup complete. Starting script...\n")
    return target_uid


# ================== Entrypoint ===================
if __name__ == "__main__":
    try:
        import requests
    except Exception:
        print("Please install 'requests' (pip install requests) and rerun.")
        exit(1)

    target_uid = interactive_setup()
    start(target_uid)