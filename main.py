

from dna_utils import(count_nucleotides, validate_sequence)
from dna_class import DNASequence
samples = [
    "ATTCGGTA",
    "GGCCTTAA",
    "ATTXGGTA"
]

user_dna = input(
    "Enter an additional DNA sequence: "
).upper()
samples.append(user_dna)

for dna in samples:
    try:
        validate_sequence(dna)
        sample = DNASequence(dna)
        print(sample.analyze())
    except ValueError as error:
        print(error)














