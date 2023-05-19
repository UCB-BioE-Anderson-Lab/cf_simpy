from .revcomp import revcomp

HOMOLOGY_LENGTH = 20

restrictionEnzymes = {
    'AarI': {'recognitionSequence': 'CACCTGC', 'cut5': 4, 'cut3': 8},
    'BbsI': {'recognitionSequence': 'GAAGAC', 'cut5': 2, 'cut3': 6},
    'BsaI': {'recognitionSequence': 'GGTCTC', 'cut5': 1, 'cut3': 5},
    'BsmBI': {'recognitionSequence': 'CGTCTC', 'cut5': 1, 'cut3': 5},
    'SapI': {'recognitionSequence': 'GCTCTTC', 'cut5': 1, 'cut3': 4},
    'BseRI': {'recognitionSequence': 'GAGGAG', 'cut5': 10, 'cut3': 8},
    'BamHI': {'recognitionSequence': 'GGATCC', 'cut5': -5, 'cut3': -1},
    'BglII': {'recognitionSequence': 'AGATCT', 'cut5': -5, 'cut3': -1},
    'EcoRI': {'recognitionSequence': 'GAATTC', 'cut5': -5, 'cut3': -1},
    'XhoI': {'recognitionSequence': 'CTCGAG', 'cut5': -5, 'cut3': -1},
    'SpeI': {'recognitionSequence': 'ACTAGT', 'cut5': -5, 'cut3': -1},
    'XbaI': {'recognitionSequence': 'TCTAGA', 'cut5': -5, 'cut3': -1},
    'PstI': {'recognitionSequence': 'CTGCAG', 'cut5': -1, 'cut3': -5},
}

for enzName in restrictionEnzymes:
    enzyme = restrictionEnzymes[enzName]
    enzyme['recognitionRC'] = revcomp(enzyme['recognitionSequence'])
    enzyme['isFivePrime'] = enzyme['cut5'] < enzyme['cut3']

def assemble(*dnaBlobs):
    dnaBlobs = ['CCATAGGTCTCAGCTTCTACTAGAGCATAAGCGTGGCTTAACAATTCCCTACTAGAGACCTTGTC','CCATAGGTCTCATACTATTAAGGTGGAGAAAGGTCAGGCCGGCTTAGAGACCTTGTC','BsaI']
    enzyme = dnaBlobs.pop()

    if not restrictionEnzymes.get(enzyme):
        return gibson(dnaBlobs)

    digestionFragments = []
    enzymeDetails = restrictionEnzymes[enzyme]
    restrictionSequence = enzymeDetails['recognitionSequence']
    revRestrictionSequence = enzymeDetails['recognitionRC']
    cut5 = enzymeDetails['cut5']
    cut3 = enzymeDetails['cut3']

    for sequence in dnaBlobs:
        sequence = sequence.upper()
        enzymeSites = sequence.count(restrictionSequence)
        revEnzymeSites = sequence.count(revRestrictionSequence)

        if enzymeSites == 0 or revEnzymeSites == 0:
            raise ValueError('Enzyme site not found in sequence')

        if enzymeSites > 1 or revEnzymeSites > 1:
            raise ValueError('More than one enzyme site found in sequence')

        enzymeSite = sequence.find(restrictionSequence)
        revEnzymeSite = sequence.find(revRestrictionSequence)

        if revEnzymeSite < enzymeSite:
            raise ValueError('Reverse enzyme site found before forward enzyme site')

        cutFragment = sequence[enzymeSite + len(restrictionSequence) + cut3 : revEnzymeSite - cut3]
        stickyEnd5 = sequence[enzymeSite + len(restrictionSequence) + cut5 : enzymeSite + len(restrictionSequence) + cut3]
        stickyEnd3 = sequence[revEnzymeSite - cut3 : revEnzymeSite - cut5]

        digestionFragments.append({
            'fragment': cutFragment,
            'stickyEnd5': stickyEnd5,
            'stickyEnd3': stickyEnd3
        })

    digestionFragments.sort(key=lambda x: x['stickyEnd5'])

    for i in range(len(digestionFragments) - 1):
        if digestionFragments[i]['stickyEnd3'] != digestionFragments[i + 1]['stickyEnd5']:
            raise ValueError('Sticky ends do not match between fragments')

    if digestionFragments[0]['stickyEnd5'] != digestionFragments[-1]['stickyEnd3']:
        raise ValueError('Sticky ends do not match between first and last fragments')

    finalSeq = ''
    for fragment in digestionFragments:
        finalSeq += fragment['stickyEnd5'] + fragment['fragment']

    return finalSeq

def gibson(seqs, check_circular=True):
    if not isinstance(seqs, list) or len(seqs) == 0:
        raise ValueError('Invalid input: expected non-empty list of DNA sequences')

    checkcirc = True
    if check_circular is False:
        checkcirc = False

    startList = seqs.copy()
    endList = []
    isCircular = False

    while len(startList) > 1:
        for seq1 in startList:
            threePrime = seq1[-HOMOLOGY_LENGTH:]
            for seq2 in startList:
                if seq2 == seq1:
                    continue
                startIndex = seq2.find(threePrime)
                if startIndex == -1:
                    continue
                newseq = seq1 + seq2[startIndex + len(threePrime):]
                endList.append(newseq)

        if len(endList) == len(startList):
            startList = endList[:-1]
            endList = []
            isCircular = True
        elif len(endList) < len(startList):
            startList = endList
            endList = []
        else:
            raise ValueError('Products do not assemble correctly, multiple assembly junctions present')

    if len(startList) != 1:
        raise ValueError('Gibson assembly did not resolve to a single product')

    outseq = startList[0]

    if isCircular:
        threePrime = outseq[-HOMOLOGY_LENGTH:]
        startIndex = outseq.find(threePrime)
        outseq = outseq[startIndex + len(threePrime):]
    elif checkcirc:
        raise ValueError('Products do not assemble into a circular product. If you are expecting a linear product, pass in check_circular = False')

    return outseq