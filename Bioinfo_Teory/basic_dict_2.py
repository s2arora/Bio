st = raw_input('enter the string: ')

dic = {}

li = []

for count in st:
	if dic.has_key(count):
		dic[count] += 1
	else:
		dic[count] = 1
	 
li_keys = dic.keys()
li_keys.sort()

for key in li_keys:
	print '{} : {}'.format(key,dic[key])


