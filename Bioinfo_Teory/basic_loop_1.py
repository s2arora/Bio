total = 0
cnt = 0

while True:
	num = raw_input('Enter a number: ')
	if num == 'done':
			break
	try:
		int_num = int(num)
	except:
		print('bad data invalid input')
		continue
	total += int_num	
	cnt += 1

print('sum',total,'count',cnt,'mean',float(total)/float(cnt))


