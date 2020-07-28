fname = raw_input('enter the file name: ')
fnumber = int(raw_input('enter the number: '))

fw = open(fname , 'w')
for i in range(1,10):
	string = '{0} * {1} = {2}\n'.format(fnumber, i, fnumber*i)
	fw.write(string)

fw.close()

fr = open(fname , 'r')
lines = fr.xreadlines()

summ = 0
cnt = 0
for line in lines:
	line = line.rstrip() 
	line_li = line.split(' ')
	for j in line_li:
		try: 
			all_int = int(j)	
		except:
			continue
		print(all_int)
		#for k in all_int:
		cnt += 1
		summ += all_int
fr.close()

print summ, cnt, float(summ)/cnt 




	

