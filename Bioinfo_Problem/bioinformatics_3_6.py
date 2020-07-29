cnt = 0
seq = ""

with open("sequence.protein.2.fasta",'r') as fr:
	for line in fr:
		if line.startswith(">"):
			title = line
		else:
			seq += line.strip()

print ( "title: "+title+
		"seq: "+seq)		
