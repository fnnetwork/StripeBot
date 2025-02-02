import requests
import re
import random
import time
import string
import base64
import cloudscraper
from bs4 import BeautifulSoup

def Tele(ccx):
    ccx = ccx.strip()

    try:
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print(f"❌ Error: Invalid CC format -> {ccx}")
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

    params = {
        'data': f'{n}|{mm}|20{yy}|{cvc}',
        'key': 'YOUR_API_KEY',  # Add a valid API key if required
    }

    try:
        scraper = cloudscraper.create_scraper()
        response = scraper.get('https://chkr.cc/api.php', headers=headers, params=params)

        # ✅ Debugging: Print Response
        print(f"\n🔹 Request Sent To: {response.url}")
        print(f"🔹 Response Status: {response.status_code}")
        print(f"🔹 Response Headers: {response.headers}")
        print(f"🔹 Response Text: {response.text}\n")

        if response.status_code != 200:
            return f"❌ HTTP Error {response.status_code}"

        if not response.text.strip():
            return "❌ Empty Response from Server"

        if "<html" in response.text.lower():
            return "❌ Received HTML Page instead of JSON (Check API Endpoint)"

        try:
            response_json = response.json()
            return response_json.get('msg', 'Unknown Response')
        except ValueError:
            return "❌ Error: Response is not valid JSON."

    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return "Request Failed"

def Tele1(ccx):
    ccx = ccx.strip()

    try:
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print(f"❌ Error: Invalid CC format -> {ccx}")
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

    params = {
        'data': f'{n}|{mm}|20{yy}|{cvc}',
        'key': 'YOUR_API_KEY',  # Add a valid API key if required
    }

    try:
        scraper = cloudscraper.create_scraper()
        response = scraper.get('https://chkr.cc/api.php', headers=headers, params=params)

        # ✅ Debugging: Print Response
        print(f"\n🔹 Request Sent To: {response.url}")
        print(f"🔹 Response Status: {response.status_code}")
        print(f"🔹 Response Headers: {response.headers}")
        print(f"🔹 Response Text: {response.text}\n")

        if response.status_code != 200:
            return f"❌ HTTP Error {response.status_code}"

        if not response.text.strip():
            return "❌ Empty Response from Server"

        if "<html" in response.text.lower():
            return "❌ Received HTML Page instead of JSON (Check API Endpoint)"

        try:
            response_json = response.json()
            return response_json.get('msg', 'Unknown Response')
        except ValueError:
            return "❌ Error: Response is not valid JSON."

    except requests.exceptions.RequestException as e:
        print(f"❌ Request Error: {e}")
        return "Request Failed"
