
def count_nucleotides(sequence):
    counts = {
        "A": 0,
        "T": 0,
        "G": 0,
        "C": 0
    }
    for nucleotide in sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    return counts

def validate_sequence(sequence):
    valid_nucleotides = {"A", "T", "G", "C"}
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(
                f"Invalid nucleotide detected: {nucleotide}"
            )















