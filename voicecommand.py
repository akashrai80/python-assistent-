import pyttsx3
import os
import pywhatkit as pwk
import datetime
i = 1
while i>0:
	gm = datetime.datetime.today()
	hours = gm.hour
	if hours < 12:
		pyttsx3.speak('good morning sir ')
		print('good morning sir!')
	elif hours >=12 and hours<16:
		pyttsx3.speak('good afternoon sir ')
		print('good afternoon sir!')
	else:
		pyttsx3.speak('good evening sir ')
		print('good evening sir!')
	pyttsx3.speak('plz tell me how can i help u')
	print('plz tell me how can i help u : ',end='')
	a = input()
	if ('do not' in a or 'dont' in a):
		pyttsx3.speak('as your wish sir!')
	else:
		if ('run' in a or 'open' in a) and ('chrome' in a or 'browser' in a):
			pyttsx3.speak('   opening chrome browser for u')
			os.system('chrome')
		elif ('date'in a):
			cd = datetime.date.today()
			pyttsx3.speak(cd)
			print(cd)
		elif ('time'in a):
			ct = datetime.datetime.today()
			h = str(ct.hour)
			m = str(ct.minute)
			s = str(ct.second)
			print(h+':hours:'+m+':minuts:'+s+':seconds')
			pyttsx3.speak((h+'hours'+m+'minuts'+s+'seconds'))
		elif ('youtube' in a) and ('run' in a or 'open' in a):
			pyttsx3.speak('opening youtube for u!')
			os.system('chrome youtube.com')
		elif ('run' in a or 'open' in a) and ('E mail' in a or 'G mail' in a or 'email' in a or 'gmail' in a):
			pyttsx3.speak('opening email for u!')
			os.system('chrome https://mail.google.com/')
		elif ('who are you' in a or 'what is your name' in a or 'tell me about your self' in a or 'tell me about you' in a or 'introduce yourself' in a ):
			pyttsx3.speak('my name is akash and i am here to help you in doing any task you can ask anything from me .')
		elif ('run' in a or 'open' in a) and ('notepad' in a or 'text editor' in a):
			pyttsx3.speak('   opening notepad for u')
			os.system('notepad')
		elif ('run' in a or 'open' in a) and ('microsoft edge' in a or 'microsoft browser' in a ):
			pyttsx3.speak('   opening microsoft edge  for u')
			os.system('msedge')
		elif ('run' in a or 'open' in a) and ('whatsapp' in a or 'whats app' in a):
			pyttsx3.speak('   opening whatsapp  for u')
			os.system('whatsapp')
		elif ('run' in a or 'open' in a) and ('telegram' in a):
			pyttsx3.speak('  opening telegram  for u')
			os.system('telegram')
		elif ('run' in a or 'open' in a) and ('zoom' in a):
			pyttsx3.speak('   opening zoom  for u')
			os.system('zoom')
		elif ('exit' in a or 'close' in a):
			pyttsx3.speak('  closing program')
			break
		elif ('run' in a or 'open' in a) and ('windows media player' in a):
			pyttsx3.speak('  opening windows media player  for u')
			os.system('wmplayer')
		elif ('run' in a or 'open' in a) and ('vlc media player' in a or 'media player' in a or 'vlc' in a):
			pyttsx3.speak('  opening vlc media player  for u')
			os.system('vlc')
		elif ('run' in a or 'open' in a) and ('control panel' in a):
			pyttsx3.speak('  opening control panel  for u')
			os.system('control panel')
		elif ('run' in a or 'open' in a) and ('facebook' in a or 'fb' in a):
			pyttsx3.speak('  opening facebook  for u')
			os.system('chrome facebook.com')
		elif ('run' in a or 'open' in a) and ('instagram' in a or 'insta' in a):
			pyttsx3.speak('  opening instagram  for u')
			os.system('chrome instagram.com')
		elif ('play a video' in a or 'open a video' in a or 'play video' in a or 'open video' in a):
			pyttsx3.speak('  which video do u want to play')
			video = input('which video do u want to play : ')
			pyttsx3.speak('  playing video for u')
			pwk.playonyt(video)
		elif ('send' in a) and ('whatsapp message ' in a or 'message by whatsapp' in a or 'message from whatsapp' in a ):
			current_time = datetime.datetime.today()	
			pyttsx3.speak('  plzz enter contect number ')
			contect = input('plz inter contect number : ')
			pyttsx3.speak('  plzz enter message to be sent ')
			msg = input('plz inter message to be sent : ')
			current_time = datetime.datetime.today()
			pwk.sendwhatmsg('+91'+contect, msg,current_time.hour,current_time.minute+2)
		elif ('search' in a or 'browse' in a ):
			pyttsx3.speak('  plzz tell me what do you want to search ')
			browse = input('what do u want to search : ')
			pyttsx3.speak('searching'+browse+'on google')
			pwk.search(browse)
		elif ('tell' in a or 'speak' in a ):
			pyttsx3.speak('  plzz tell me the topic ')
			topic = input('enter a topic : ')
			speach = pwk.info(topic,5)
			pyttsx3.speak(speach)
		elif ('shutdown' in a):
			pyttsx3.speak('closing window')
			print('closing window!')
			pwk.shutdown(20)
		else:
			pyttsx3.speak('sorry sir i am not able to understand what do u want !')
		
		