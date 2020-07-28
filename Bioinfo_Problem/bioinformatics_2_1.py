#gugudan

num = int(input("Which times tables: "))

for i in range(1,10):	
	if num < 1 or num > 9:
		print ("What?")
		break
	print ("{} * {} = {}".format(num,i,num*i))


