import subprocess
import requests
import json

# local ip of device to scan for
IP_DEVICE = "192.168.178.XX"

# hue api with token
HUE_URL_BASE = "http://192.168.178.XX/api/<TOKEN>/"

HUE_LAMP_ID = "1"

proc = subprocess.Popen(["ping", '-t', IP_DEVICE], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    response = str(line)
    print(response)

    if "bytes" in response.lower() and IP_DEVICE in response:
        print("Connected!")
        getRes = requests.get(HUE_URL_BASE + "lights/" + HUE_LAMP_ID)
        parsed = json.loads(getRes.text)
        if not bool(parsed["state"]["on"]):
            postData = {"on": True}
            postRes = requests.put(HUE_URL_BASE + "lights/" + HUE_LAMP_ID + "/state", json=postData)
            print("Turning on Light 1: " + postRes.text)
