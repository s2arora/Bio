s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

s1_len = len(s1)
s2_len = len(s2)

if s1_len % 2 != 0 and s1_len < s2_len:
	print (s1+s2)
else:
	print (s2+s1)
