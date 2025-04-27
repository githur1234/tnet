from flask import Flask, request, jsonify
import json
import threading
import time
import os
import sys
import requests
import winsound
import base64

app = Flask(__name__)

# Kullanılacak değişkenler
blcip = []
avadhcp = []
dhcp = ["dev1", "dev2", "dev3", "dev4", "dev5", "dev6", "dev7", "dev8", "dev9", "dev10",
        "dev11", "dev12", "dev13", "dev14", "dev15", "dev16", "dev17", "dev18", "dev19", "dev20",
        "dev21", "dev22", "dev23", "dev24", "dev25"]

# JSON dosya yolu
db_path = "c:/users/yavuz/desktop/tnetdb.json"

# Mesaj gönderme fonksiyonu
def send(dhcp1, dhcp2, message):
    encbuffer = []
    encoded_message = base64.b64encode(message.encode()).decode()
    for chr_ in encoded_message:
        encbuffer.append(ord(chr_) * 54)
    
    with open(db_path, "r") as dbfile:
        ip = json.load(dbfile)[dhcp2]["ip"]
    
    requests.post(f"http://{ip}", json={"sender": dhcp1, "message":[encbuffer]})

# Ana cihaz kayıt fonksiyonu
@app.route("/", methods=["POST"])
def main():
    global dhcp, avadhcp

    rp = request.get_json()
    ip = rp["ip"]
    
    if ip in blcip:
        return "You do not have access to this page for DHCP spoofing."
    
    mac = rp["mac"]
    mode = rp["statu"]
    password = rp["passs"]
    
    if password == "tnet123321123321":
        subdomain = "s1"
    else:
        subdomain = "s2"

    for cdhcp in dhcp:
        if cdhcp not in avadhcp:
            avadhcp.append(cdhcp)
            break

    with open(db_path, "r") as rdb:
        db = json.load(rdb)
    
    db[cdhcp] = {"mode": mode, "ip": ip, "mac": mac, "subdomain": subdomain}

    with open(db_path, "w") as rdb:
        json.dump(db, rdb, indent=4)

    print(f"""
    NEW DEVICE DATA:
    DHCP: {cdhcp}
    IP: {ip}
    MAC: {mac}
    Status: {mode}
    Subdomain: {subdomain}
    Password: {password}
    [-] If you do not recognize this MAC and IP, please block this device.
    """)

    return jsonify({"your_dhcp": cdhcp})

# Mesaj gönderme endpoint'i
@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    dhcp_sender = data["dhcp"]
    dhcp_receiver = data["dhcp2"]
    message_content = data["message"]

    with open(db_path, "r") as dbfile:
        db = json.load(dbfile)
    
    if db.get(dhcp_sender, {}).get("ip") == request.remote_addr:
        send(dhcp_sender, dhcp_receiver, message_content)
        return "Message sent."
    else:
        blcip.append(request.remote_addr)
        return "Access Denied", 403

# Flask sunucusunu arka planda başlat
def run_server():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_server, daemon=True).start()

# Komut satırı kontrolü
restartjson = """

{
                             "subdomains": [
                                                          "s1",
                                                          "s2"
                             ],
                             "s2pass": "ff000000ab123456",
                             "s1pass": "tnet123321123321",
                             "dev1": {
                                                          "mode": [
                                                                                       "statu"
                                                          ],
                                                          "ip": "172.26.32.1",
                                                          "mac": "a4:4c:c8:73:59:e2",
                                                          "subdomain": "s1"
                             },
                             "dev2": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev3": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev4": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev5": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev6": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev7": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev8": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev9": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev10": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev11": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev12": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev13": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev14": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev15": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev16": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev17": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev18": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev19": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev20": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev21": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev22": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev23": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev24": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "dev25": {
                                                          "mode": "none",
                                                          "subdomain": "none",
                                                          "ip": "none",
                                                          "mac": "none"
                             },
                             "registerpath": "c:/users/yavuz/desktop/register"
}

"""

while True:
    run = input("tnetmainserver>>> ").split()

    if run[0] == "r":
        if "/j" in run:
            if "/t" in run:
                for i in range(len(run)):
                    if run[i] == "/t":
                        time.sleep(int(run[i+1]))
                        break
            else:
                time.sleep(1)
            
            os.system('msg * "TNet JSON has restarted"')
            with open(db_path, "w") as dbfile:
                dbfile.truncate(0)
                dbfile.write(restartjson)
        else:
            print("Server shutting down...")
            sys.exit(1)
            for _ in range(10):
                winsound.Beep(1000, 500)
                time.sleep(1)
            os.system('msg * "TNet server is restarting"')
