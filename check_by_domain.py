import requests

email=input('enter email:')

dommain=email[email.find('@'):]
try:
	requests.get('https://'+dommain)
	print(email+" is real")
except:
	print(email+' is fake')