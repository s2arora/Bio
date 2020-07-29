with open("sequence.protein.fasta","r") as fr:
	for line in fr:
		line = line.strip()
		if line == '':
			continue
		print(line)
