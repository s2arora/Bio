h = raw_input('enter hours: ')
m = raw_input('enter rate: ')
try:
	print 'pay:', int(h)*int(m)
except:
	print ''
	print 'please enter the number '
