total = 0
cnt = 0

minn = 100
maxx = 0

while True:
	num = raw_input('Enter a number: ')
	if num == 'done':
			break
	try:
		int_num = int(num)
	except:
		print('bad data invalid input')
		continue
	if 0 > int_num or int_num > 100:
		print 'please enter the number in 0~100'
		continue
	
	total += int_num	
	cnt += 1
	
	if maxx < int_num:
		maxx = int_num
	elif minn > int_num:
		minn = int_num
		



print('sum',total,'count',cnt,'min',minn,'max',maxx)


