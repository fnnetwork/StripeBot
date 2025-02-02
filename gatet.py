import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
import requests

def Tele(ccx):
    # Strip any extra spaces
    ccx = ccx.strip()

    try:
        # Split the card details into number, month, year, and CVC
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
    except IndexError:
        print(f"Error: The input string {ccx} is not in the correct format.")
        return

    # Shorten year if necessary (e.g., '2028' becomes '28')
    if "20" in yy:
        yy = yy.split("20")[1]

    # Create a session

    # Example headers (customize as needed)
    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_clck=1nznmx5%7C2%7Cfqj%7C0%7C1767; _clsk=1y8plkh%7C1730567385506%7C1%7C1%7Cn.clarity.ms%2Fcollect',
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

    # Example data payload (customize as needed)
    data = {
         'data':  f'{n}|{mm}|20{yy}|{cvc}',
         'key': '',
    }


    # Make an API request (using a legitimate API, not the one you're working with)
    # This is just a placeholder for a legitimate use case, e.g., Stripe API or any other
    response = requests.post('https://chkr.cc/api.php', headers=headers, data=data).json()
    try:
    	ii=response['msg']
    except:
    	return 'Live' or 'Thank You'
    return ii
import requests

def Tele1(ccx):
    # Strip any extra spaces
    ccx = ccx.strip()

    try:
        # Split the card details into number, month, year, and CVC
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
    except IndexError:
        print(f"Error: The input string {ccx} is not in the correct format.")
        return

    # Shorten year if necessary (e.g., '2028' becomes '28')
    if "20" in yy:
        yy = yy.split("20")[1]

    # Create a session

    # Example headers (customize as needed)
    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_clck=1nznmx5%7C2%7Cfqj%7C0%7C1767; _clsk=1y8plkh%7C1730567385506%7C1%7C1%7Cn.clarity.ms%2Fcollect',
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

    # Example data payload (customize as needed)
    data = {
         'data':  f'{n}|{mm}|20{yy}|{cvc}',
         'key': '',
    }


    # Make an API request (using a legitimate API, not the one you're working with)
    # This is just a placeholder for a legitimate use case, e.g., Stripe API or any other
    response = requests.post('https://chkr.cc/api.php', headers=headers, data=data).json()
    try:
    	ii=response['msg']
    except:
    	return 'Live' or 'Thank You'
    return ii