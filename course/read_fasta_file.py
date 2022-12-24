# -*- coding: utf-8 -*-

"""
How to read fasta files > 
main methods -> 
seq.id() & seq.seq()
"""

from Bio import SeqIO

# print sequence
# for fasta in SeqIO.parse('1bga_seq.fasta','fasta'):
#     print(fasta.seq)

# print sequence using list comprehension
print("".join([str(fasta.seq) for fasta in SeqIO.parse('1bga_seq.fasta', 'fasta')])) 
