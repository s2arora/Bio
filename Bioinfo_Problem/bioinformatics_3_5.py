cnt = 0

with open("sequence.protein.2.fasta",'r') as fr:
	for line in fr:
		line = line.strip()
		if cnt == 1:
			break
		cnt += 1
		
print("The second line is: {}".format(line))