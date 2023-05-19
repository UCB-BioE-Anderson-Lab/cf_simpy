from .revcomp import revcomp

def pcr(forwardSeq, reverseSeq, templateSeq):
    # Find index of 18 bp match on 3' end of forward oligo and template
    foranneal = forwardSeq[-18:]

    forwardMatchIndex = templateSeq.find(foranneal)
    if forwardMatchIndex == -1:
        templateSeq = revcomp(templateSeq)
        forwardMatchIndex = templateSeq.find(foranneal)
        if forwardMatchIndex == -1:
            raise ValueError("Forward oligo does not exactly anneal to the template")

    # Rotate template sequence to begin with annealing region of forward oligo
    rotatedTemplate = templateSeq[forwardMatchIndex:] + templateSeq[:forwardMatchIndex]

    # Find reverse complement of reverse oligo
    reverseComp = revcomp(reverseSeq)

    # Find index of 18 bp match on 3' end of reverse complement and rotated template
    revanneal = reverseComp[:18]
    reverseMatchIndex = rotatedTemplate.find(revanneal)
    if reverseMatchIndex == -1:
        raise ValueError("Reverse oligo does not exactly anneal to the template")

    # Concatenate entire forward oligo, region between annealing regions on rotated template, and entire 
    # reverse complement of reverse oligo to obtain final PCR product
    finalProduct = forwardSeq + rotatedTemplate[18:reverseMatchIndex] + reverseComp

    return finalProduct