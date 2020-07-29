lines = ""
with open("sequence.protein.fasta","r") as fr:
	for line in fr:
		line = line.strip()
		if line == "":
			continue
		lines += line

with open("sequence.protein.2.fasta",'w') as fw:
	fw.write(lines+"\n")
