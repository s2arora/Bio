seq = ""
with open("sequence.nucleotide.fasta","r") as fr:
    for line in fr:
        if line.startswith(">"):
            title = line
        else:
            seq += line.strip()


sequence_reversed = ''.join(reversed(seq))

sequence_ATGC = {"A":"T",
                 "T":"A",
                 "G":"C",
                 "C":"G"}

sequence_reversed_complement = ""
for seq_rev in sequence_reversed:
    sequence_reversed_complement += sequence_ATGC[seq_rev] 

print(sequence_reversed_complement)