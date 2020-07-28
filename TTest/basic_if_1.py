H = raw_input('enter hour: ')
M = raw_input('enter rate: ')

if H >= 100:
	print 'pay:',int(H)*int(M)*2
else:
	print 'pay:',int(H)*int(M)
