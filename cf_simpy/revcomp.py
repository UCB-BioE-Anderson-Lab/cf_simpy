def revcomp(inseq):
    if not inseq:
        return 'error on ' + inseq

    output = ''
    for i in range(len(inseq) - 1, -1, -1):
        if inseq[i] in 'ATCGBDHKNSMVWYR':
            output += {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                        'B': 'V', 'D': 'H', 'H': 'D', 'K': 'M', 'N': 'N', 'R': 'Y', 'S': 'S', 'M': 'K', 'V': 'B', 'W': 'W', 'Y': 'R'}[inseq[i]]
        else:
            raise ValueError(f"Character '{inseq[i]}' is not a valid DNA character")
    return output