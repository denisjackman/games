'''
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems.
It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells.
RNA differs slightly from DNA its chemical structure and contains no Thymine.
In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a funciton which translates a given DNA string into RNA.
'''


def DNAtoRNA(dna):
    rna = ""
    for nucleic_acid_base in dna:
        if nucleic_acid_base == 'T':
            rna += 'U'
        else:
            rna += nucleic_acid_base
    return rna


'''
'GCATGCATGCATU' should equal 'GCAU'
'GACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCCGACCGCCGCC' should equal 'GACCGCCGCC'
'''


print "GCATGCATGCATU : ",DNAtoRNA("GCATGCATGCATU")