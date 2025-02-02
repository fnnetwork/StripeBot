import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup

# ✅ Function to check CCs using chkr.cc API
def Tele(ccx):
    # Strip any extra spaces
    ccx = ccx.strip()

    try:
        # Split the card details into number, month, year, and CVC
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print(f"Error: The input string {ccx} is not in the correct format.")
        return "Invalid Input Format"

    # Shorten year if necessary (e.g., '2028' becomes '28')
    if yy.startswith("20"):
        yy = yy[2:]

    # Set headers
    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://chkr.cc',
        'referer': 'https://chkr.cc/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Set data payload
    data = {
        'data': f'{n}|{mm}|20{yy}|{cvc}',
        'key': '',  # Add API key if required
    }

    try:
        response = requests.post('https://chkr.cc/api.php', headers=headers, data=data)

        # Ensure the response is valid JSON
        response_json = response.json()
        return response_json.get('msg', 'Unknown Response')

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return "Request Failed"
    
    except ValueError:
        print("Error: Response is not in JSON format.")
        return "Invalid JSON Response"


# ✅ Duplicate Function (Tele1) for Checking Another CC
def Tele1(ccx):
    # Strip any extra spaces
    ccx = ccx.strip()

    try:
        # Split the card details into number, month, year, and CVC
        n, mm, yy, cvc = ccx.split("|")
    except ValueError:
        print(f"Error: The input string {ccx} is not in the correct format.")
        return "Invalid Input Format"

    # Shorten year if necessary (e.g., '2028' becomes '28')
    if yy.startswith("20"):
        yy = yy[2:]

    # Set headers
    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://chkr.cc',
        'referer': 'https://chkr.cc/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Set data payload
    data = {
        'data': f'{n}|{mm}|20{yy}|{cvc}',
        'key': '',  # Add API key if required
    }

    try:
        response = requests.post('https://chkr.cc/api.php', headers=headers, data=data)

        # Ensure the response is valid JSON
        response_json = response.json()
        return response_json.get('msg', 'Unknown Response')

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return "Request Failed"
    
    except ValueError:
        print("Error: Response is not in JSON format.")
        return "Invalid JSON Response"
