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
        'authority': 'api.chkr.cc',
        'method': 'POST',
        'path': '/',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Length': '44',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://chkr.cc',
        'Referer': 'https://chkr.cc/',
        'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Example data payload (customize as needed)
    data = {
         'data':  f'{n}|{mm}|20{yy}|{cvc}',
         'key': '',
    }


    # Make an API request (using a legitimate API, not the one you're working with)
    # This is just a placeholder for a legitimate use case, e.g., Stripe API or any other
    response = requests.post('https://api.chkr.cc/', headers=headers, data=data).json()
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
        'authority': 'api.chkr.cc',
        'method': 'POST',
        'path': '/',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Content-Length': '44',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://chkr.cc',
        'Referer': 'https://chkr.cc/',
        'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Example data payload (customize as needed)
    data = {
         'data':  f'{n}|{mm}|20{yy}|{cvc}',
         'key': '',
    }


    # Make an API request (using a legitimate API, not the one you're working with)
    # This is just a placeholder for a legitimate use case, e.g., Stripe API or any other
    response = requests.post('https://api.chkr.cc/', headers=headers, data=data).json()
    try:
    	ii=response['msg']
    except:
    	return 'Live' or 'Thank You'
    return ii
