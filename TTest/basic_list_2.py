b = raw_input('enter the string: ')

li = b.split(',')
print type(li)

li2 = li[:]
li2.sort()

li3 = li[:]
li3.sort(reverse=True)

if li == li2:
	print 'ascending'
elif li == li3:
	print 'descending'
else:
	print 'not sorted'

