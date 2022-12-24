# -*- coding: utf-8 -*-

from Bio import SeqIO, Seq

sequence_1bga = Seq.Seq("".join([str(fasta.seq) for fasta in SeqIO.parse('1bga_seq.fasta', 'fasta')])) 

# reverse using python logic as str
print(sequence_1bga[::-1])

# get complement 
print(sequence_1bga.complement())

# get RNA complement 
print(sequence_1bga.complement_rna())

# transcribe into RNA
print(sequence_1bga.transcribe())

# translate RNA into a Protein seq -> (this seq has an error at UIF codon)
try:
    print(sequence_1bga.transcribe().translate()) 
except:
    print("uif invalid codon")

