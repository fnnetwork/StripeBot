import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup

# ✅ Function to check CCs using chkr.cc API
def Tele(ccx):
    ccx = ccx.strip()

    try:
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print(f"Error: Invalid CC format -> {ccx}")
        return "Invalid Input Format"

    if yy.startswith("20"):
        yy = yy[2:]

    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://chkr.cc',
        'referer': 'https://chkr.cc/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'data': f'{n}|{mm}|20{yy}|{cvc}',
        'key': '',
    }

    try:
        response = requests.post('https://chkr.cc/api.php', headers=headers, data=data)

        # ✅ Debugging: Print response
        print(f"\n🔹 Response Status: {response.status_code}")
        print(f"🔹 Response Headers: {response.headers}")
        print(f"🔹 Response Text: {response.text}\n")

        # ✅ Check if response is empty
        if not response.text.strip():
            return "❌ Empty Response from Server"

        # ✅ Check if response contains HTML (Error Page)
        if "<html" in response.text.lower():
            return "❌ Received HTML Page instead of JSON"

        # ✅ Try parsing JSON response
        response_json = response.json()
        return response_json.get('msg', 'Unknown Response')

    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return "Request Failed"

    except ValueError:
        print("❌ Error: Response is not valid JSON.")
        return "Invalid JSON Response"

# ✅ Function to check CCs using chkr.cc API (Alternative)
def Tele1(ccx):
    ccx = ccx.strip()

    try:
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print(f"Error: Invalid CC format -> {ccx}")
        return "Invalid Input Format"

    if yy.startswith("20"):
        yy = yy[2:]

    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://chkr.cc',
        'referer': 'https://chkr.cc/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'data': f'{n}|{mm}|20{yy}|{cvc}',
        'key': '',
    }

    try:
        response = requests.post('https://chkr.cc/api.php', headers=headers, data=data)

        # ✅ Debugging: Print response
        print(f"\n🔹 Response Status: {response.status_code}")
        print(f"🔹 Response Headers: {response.headers}")
        print(f"🔹 Response Text: {response.text}\n")

        # ✅ Check if response is empty
        if not response.text.strip():
            return "❌ Empty Response from Server"

        # ✅ Check if response contains HTML (Error Page)
        if "<html" in response.text.lower():
            return "❌ Received HTML Page instead of JSON"

        # ✅ Try parsing JSON response
        response_json = response.json()
        return response_json.get('msg', 'Unknown Response')

    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return "Request Failed"

    except ValueError:
        print("❌ Error: Response is not valid JSON.")
        return "Invalid JSON Response"
