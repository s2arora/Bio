cnt = 0

with open("sequence.protein.2.fasta",'r') as fr:
	for line in fr:
		cnt += 1
		if cnt == 2:
			line = line 	

print("The second line is: {}".format(line.strip()))
