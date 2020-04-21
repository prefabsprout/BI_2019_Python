class RNA:
    def __init__(self, seq: str):
        self.seq = seq.upper()
        if 'T' in self.seq:
            raise Exception('Thymine should not be contained in RNA sequences')

    def gc_content(self):
        return self.seq.count('GC') / len(self.seq) * 100

    def reverse_comp(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        revcomped = [complement[elem] for elem in list(self.seq)[::-1]]
        return ''.join(revcomped)


class DNA:
    def __init__(self, seq: str):
        self.seq = seq.upper()
        if 'U' in self.seq:
            raise Exception('Uracil should not be contained in DNA sequences')

    def gc_content(self):
        return self.seq.count('GC') / len(self.seq) * 100

    def reverse_comp(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        revcomped = [complement[elem] for elem in list(self.seq)[::-1]]
        return ''.join(revcomped)

    def transcription(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        rnaseq = RNA(''.join([complement[elem] for elem in list(self.seq)]))
        return str(rnaseq.seq)
