cnt = 0
sequence = ""
origin_passed = False

with open("sequence.protein.gb",'r') as fr:
	for line in fr:
		cnt += 1
		if cnt == 1:
			title = line 
		elif line.startswith("ORIGIN"):
			sequence += line.strip()
			origin_passed = True 
		
		if origin_passed: 
			sequence+= line.strip()

print("title:",title+
		"seq:",sequence)
