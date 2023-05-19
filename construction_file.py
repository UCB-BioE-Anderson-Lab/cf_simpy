class ConstructionFile:
    def __init__(self, steps, sequences):
        self.steps = steps
        self.sequences = sequences


class PCR:
    def __init__(self, operation, output, forward_oligo, reverse_oligo, template, product_size):
        self.operation = operation
        self.output = output
        self.forward_oligo = forward_oligo
        self.reverse_oligo = reverse_oligo
        self.template = template
        self.product_size = product_size


class Assemble:
    def __init__(self, operation, output, dnas, enzyme):
        self.operation = operation
        self.output = output
        self.dnas = dnas
        self.enzyme = enzyme


class Transform:
    def __init__(self, operation, output, dna, strain, antibiotics, temperature=None):
        self.operation = operation
        self.output = output
        self.dna = dna
        self.strain = strain
        self.antibiotics = antibiotics
        self.temperature = temperature


class Digest:
    def __init__(self, operation, output, dna, fragSelect, enzymes):
        self.operation = operation
        self.output = output
        self.dna = dna
        self.fragSelect = fragSelect
        self.enzymes = enzymes


class Ligate:
    def __init__(self, operation, output, dnas):
        self.operation = operation
        self.output = output
        self.dnas = dnas