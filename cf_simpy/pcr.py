from .polynucleotide import Polynucleotide
from .revcomp import revcomp

def pcr(forwardOligo, reverseOligo, template):
    # Check that the forward and reverse oligos are single stranded and linear
    if not isinstance(forwardOligo, Polynucleotide):
        raise ValueError("Forward oligo must be a Polynucleotide")
    if forwardOligo.is_double_stranded:
        raise ValueError("Forward oligo must be single stranded")
    if forwardOligo.is_circular:
        raise ValueError("Forward oligo must be linear")
    if not isinstance(reverseOligo, Polynucleotide):
        raise ValueError("Reverse oligo must be a Polynucleotide")
    if reverseOligo.is_double_stranded:
        raise ValueError("Reverse oligo must be single stranded")
    if reverseOligo.is_circular:
        raise ValueError("Reverse oligo must be linear")

    # Find index of 18 bp match on 3' end of forward oligo and template
    foranneal = forwardOligo.sequence[-18:]
    if template.is_circular:
        template.sequence = template.sequence[-18:] + template.sequence
    forwardMatchIndex = template.sequence.find(foranneal)
    if forwardMatchIndex == -1:
        template.sequence = revcomp(template.sequence)
        if template.is_circular:
            template.sequence = template.sequence[-18:] + template.sequence
        forwardMatchIndex = template.sequence.find(foranneal)
    if forwardMatchIndex == -1:
        raise ValueError("Forward oligo does not exactly anneal to the template")
        if forwardMatchIndex == -1:
            raise ValueError("Forward oligo does not exactly anneal to the template")

    # Rotate template sequence to begin with annealing region of forward oligo
    if template.is_circular:
        rotatedTemplate = template.sequence[forwardMatchIndex:] + template.sequence[:forwardMatchIndex]
    else:
        rotatedTemplate = template.sequence[forwardMatchIndex:]

    # Find reverse complement of reverse oligo
    reverseComp = revcomp(reverseOligo.sequence)

    # Find index of 18 bp match on 3' end of reverse complement and rotated template
    revanneal = reverseComp[:18]
    reverseMatchIndex = rotatedTemplate.find(revanneal)
    if reverseMatchIndex == -1:
        raise ValueError("Reverse oligo does not exactly anneal to the template")

    # Concatenate entire forward oligo, region between annealing regions on rotated template, and entire 
    # reverse complement of reverse oligo to obtain final PCR product
    pcrProduct = forwardOligo.sequence + rotatedTemplate[18:reverseMatchIndex] + reverseComp

    # Return PCR product as a Polynucleotide
    return Polynucleotide(pcrProduct, '', '', True, False, forwardOligo.mod_ext5, reverseOligo.mod_ext5)