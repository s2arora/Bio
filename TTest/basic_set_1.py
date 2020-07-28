s1 = raw_input('enter the number: ')
print("3,5,1,3,2")
s1 = "3,5,1,3,2"

s1_li= s1.split(",")

s1_li_int = []

for i in s1_li:
	s1_li_int.append(int(i))

set1 = set(s1_li_int)

s2 = raw_input('enter the number: ')
print("4,6,6,4,1")
s2 = "4,6,6,4,1"

s2_li= s2.split(",")

s2_li_int = []

for j in s2_li:
	s2_li_int.append(int(j))

set2 = set(s2_li_int)

print(set1.intersection(set2))



	

