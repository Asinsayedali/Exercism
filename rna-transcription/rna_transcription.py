def to_rna(dna_strand):
    Check=str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(Check)