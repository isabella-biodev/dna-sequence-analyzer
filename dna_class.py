
class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence

from dna_utils import count_nucleotides
class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
    def analyze(self):
        return count_nucleotides(
            self.sequence
        )




















