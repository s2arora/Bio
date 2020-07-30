cnt = 0
ORIGIN_passed = False
Origin_trace = []

with open("sequence.protein.gb",'r') as fr:
	for line in fr:
		cnt += 1
		if cnt == 1:
			title = line 
		
		if line.startswith("ORIGIN"):
			ORIGIN_passed = True
		elif ORIGIN_passed:
			Origin_trace.append(line[10:-1])
			
protein = ""
for protein_line in Origin_trace:
	protein += protein_line.replace(" ",'') 

cnt2 = 0
count70 = ""

for one_protein in protein:
	cnt2 += 1
	if cnt2 % 70 == 0:
		count70 += cnt2
	
print(count70)

	

