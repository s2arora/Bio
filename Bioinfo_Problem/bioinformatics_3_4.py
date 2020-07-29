lines = ""
with open("sequence.protein.fasta","r") as fr:
	lines=fr.read()

with open("sequence.protein.2.fasta",'w') as fw:
	fw.write(lines.strip()+"\n")
