import requests
import json
import socket
import uuid
import threading
import time
from flask import Flask, request
import base64
# Sunucu ayarları
SERVER_IP = "127.0.0.1"  # Sunucunun IP adresi
SERVER_PORT = 8080
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"

# Client ayarları
LOCAL_PORT = 5000  # Client'ın kendi mesaj sunucusunun portu (farklı bir port)

PASSWORD = "tnet123321123321"  # Kayıt şifresi (subdomain belirliyor)

# Flask app (gelen mesajları almak için)
app = Flask(__name__)

# Global değişkenler
my_dhcp = None

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(mac_num[i:i+2] for i in range(0, len(mac_num), 2))
    return mac

def register_device():
    data = {
        "ip": get_ip(),  # Bilgisayarın IP adresi
        "mac": get_mac(),  # MAC adresi
        "statu": "client",  # Cihaz modu
        "passs": PASSWORD
    }
    try:
        r = requests.post(SERVER_URL + "/", json=data)
        if r.status_code == 200:
            response = r.json()
            print("[+] Başarılı kayıt. DHCP ID:", response["your dhcp"])
            return response["your dhcp"]
        else:
            print("[-] Kayıt başarısız:", r.text)
            return None
    except Exception as e:
        print("[-] Sunucuya bağlanılamadı:", e)
        return None

def send_message(my_dhcp, target_dhcp, message):
    data = {
        "dhcp": my_dhcp,
        "dhcp2": target_dhcp,
        "message": message
    }
    try:
        r = requests.post(SERVER_URL + "/message", json=data)
        if r.status_code == 200:
            print("[+] Mesaj gönderildi.")
        else:
            print("[-] Mesaj gönderilemedi:", r.text)
    except Exception as e:
        print("[-] Hata oluştu:", e)

@app.route("/", methods=["POST"])
def receive_message():
    data = request.get_json()
    sender = data.get("sender")
    message = data.get("message")
    buffer=[]
    decoded_bytes = base64.b64decode(message)
    dmessage = decoded_bytes.decode('utf-8')
    for char in dmessage:
        buffer.append(chr(int(char)/54))
    print(f"\n[📩 Gelen mesaj] Gönderen DHCP: {sender} | Mesaj: {str()}")
    return "OK"

def start_flask_server():
    app.run(host="0.0.0.0", port=LOCAL_PORT)

if __name__ == "__main__":
    # Flask serverı arka planda başlat
    threading.Thread(target=start_flask_server, daemon=True).start()

    # Cihazı kaydet
    my_dhcp = register_device()

    if my_dhcp:
        while True:
            target = input("Göndermek istediğin DHCP ID (örnek dev2): ")
            msg = input("Gönderilecek mesaj: ")
            send_message(my_dhcp, target, msg)
            time.sleep(1)
    else:
        print("[-] Kayıt başarısız oldu, çıkılıyor.")
