dd = dict()

while True:
	nm = raw_input('enter the name: ')
	if nm == 'done':
		break
	ph = raw_input('enter the phone number: ')
	dd[nm] = ph


search = raw_input('Enter the name you want to know: ')

print(dd[search])
