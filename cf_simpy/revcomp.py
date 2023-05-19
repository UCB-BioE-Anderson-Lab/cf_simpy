def revcomp(inseq):
    if not inseq:
        return 'error on ' + inseq

    output = ''
    for i in range(len(inseq) - 1, -1, -1):
        if inseq[i] in 'ATCGatcgBDHKNSMVWYbdhknsmyvwr':
            output += {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                        'a': 't', 't': 'a', 'c': 'g', 'g': 'c',
                        'B': 'V', 'D': 'H', 'H': 'D', 'K': 'M', 'N': 'N', 'R': 'Y', 'S': 'S', 'M': 'K', 'V': 'B', 'W': 'W', 'Y': 'R',
                        'b': 'v', 'd': 'h', 'h': 'd', 'k': 'm', 'n': 'n', 'r': 'y', 's': 's', 'm': 'k', 'v': 'b', 'w': 'w', 'y': 'r'}[inseq[i]]
        else:
            raise ValueError(f"Character '{inseq[i]}' is not a valid DNA character")
    return output