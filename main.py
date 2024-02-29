import os
import urllib.request
import json
import requests

# For your own IP Coding
url = "http://ip-api.com/json/"
load1 = urllib.request.urlopen(url)
read1 = load1.read()
result1 = json.loads(read1)
os.system('clear')

fb = "https://facebook.com/CoderSigma"
tik = "https://www.tiktok.com/@CoderSigma"

TOKEN = "123123123123"  # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_CHAT_ID = "1231231239"  # Replace 'YOUR_TELEGRAM_CHAT_ID' with your chat ID

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=data)

send_message("IP Tracker v1 - CoderSigma")

while True:
    ip = input("\033[1;36mEnter Your Target IP: \033[1;36m")

    if ip == 'exit':
        break
    else:
        # ips Coding
        api = "http://api.ipstack.com/"
        load = urllib.request.urlopen(api + ip + '?access_key=fd0c1eae3c2d27ee676af0db2b864b0e')
        read = load.read()
        result = json.loads(read)

        # ip-api
        url = "http://ip-api.com/json/"
        load1 = urllib.request.urlopen(url + ip)
        read1 = load1.read()
        result1 = json.loads(read1)

        if result1['status'] == 'success':
            # latitude
            lati = result['latitude']
            lat = "{:.4f}".format(lati)
            # longitude
            lon = result['longitude']
            long = "{:.4f}".format(lon)

            # more info
            more = json.dumps(result['location'])

            # Constructing message
            message = f"""
            Facebook: {fb}
            Tiktok: {tik}
            All The Information Of IP Is Here [{ip}] :
            IP: {result['ip']}
            IP Type: {result['type']}
            Continent Name: {result['continent_name']}
            Continent Code: {result['continent_code']}
            Country: {result['country_name']}
            Country Code: {result1['countryCode']}
            Region Name: {result['region_name']}
            Region Code: {result['region_code']}
            City: {result['city']}
            Zip: {result['zip']}
            TimeZone: {result1['timezone']}
            isp: {result1['isp']}
            Latitude: {lat}
            Longitude: {long}
            More Information Of IP : {more}
            """
            send_message(message)
        else:
            send_message(f"Sorry, Please Type The IP[{ip}] Please try again")

send_message("IP Tracker v3.0 - Ended")
