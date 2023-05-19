class Polynucleotide:
    def __init__(self, sequence, ext5=None, ext3=None, isDoubleStranded=False, isCircular=False, mod_ext5=None, mod_ext3=None):
        self.sequence = sequence.upper()
        self.ext5 = ext5.upper() if ext5 else ext5
        self.ext3 = ext3.upper() if ext3 else ext3
        self.isDoubleStranded = isDoubleStranded
        self.isCircular = isCircular
        self.mod_ext5 = mod_ext5 or ''
        self.mod_ext3 = mod_ext3 or ''

    def __str__(self):
        return f'Polynucleotide(sequence={self.sequence}, ext5={self.ext5}, ext3={self.ext3}, isDoubleStranded={self.isDoubleStranded}, isCircular={self.isCircular}, mod_ext5={self.mod_ext5}, mod_ext3={self.mod_ext3})'

    def __repr__(self):
        return self.__str__()

def dsDNA(sequence):
    return Polynucleotide(sequence, '', '', True, False, 'hydroxyl', 'hydroxyl')


def oligo(sequence):
    return Polynucleotide(sequence, None, None, False, False, 'hydroxyl', None)


def plasmid(sequence):
    return Polynucleotide(sequence, '', '', True, True, None, None)