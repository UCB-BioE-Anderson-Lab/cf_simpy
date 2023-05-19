from Polynucleotide import Polynucleotide
from assemble import restriction_enzymes


def cut_once(poly, enz):
    seq = poly.sequence
    enz_data = restriction_enzymes[enz]
    recognition_seq = enz_data['recognition_sequence']
    recognition_seq_rc = enz_data['recognition_rc']
    cut5 = enz_data['cut5']
    cut3 = enz_data['cut3']

    index = seq.find(recognition_seq)
    index_rc = seq.find(recognition_seq_rc)

    if index == -1 and index_rc == -1:
        return None

    found_on_coding_strand = index != -1
    is_five_prime = enz_data['is_five_prime']
    ss_region_start = None
    ss_region_end = None

    if found_on_coding_strand:
        if is_five_prime:
            ss_region_start = index + len(recognition_seq) + cut5
            ss_region_end = index + len(recognition_seq) + cut3
        else:
            ss_region_start = index + len(recognition_seq) + cut3
            ss_region_end = index + len(recognition_seq) + cut5
    else:
        if is_five_prime:
            ss_region_start = index_rc - cut3
            ss_region_end = index_rc - cut5
        else:
            ss_region_start = index_rc - cut5
            ss_region_end = index_rc - cut3

    sticky_end = ''
    if not is_five_prime:
        sticky_end += '-'
    sticky_end += seq[ss_region_start:ss_region_end]

    if poly.is_circular:
        linear_seq = seq[ss_region_end:] + seq[:ss_region_start]
        linear_poly = Polynucleotide(
            linear_seq,
            sticky_end,
            sticky_end,
            poly.is_double_stranded,
            False,
            'phos5',
            'phos5'
        )
        output = [linear_poly]
    else:
        left_poly = Polynucleotide(
            seq[:ss_region_start],
            poly.ext5,
            sticky_end,
            poly.is_double_stranded,
            False,
            poly.mod_ext5,
            'phos5'
        )

        right_poly = Polynucleotide(
            seq[ss_region_end:],
            sticky_end,
            poly.ext3,
            poly.is_double_stranded,
            False,
            'phos5',
            poly.mod_ext3
        )

        output = [left_poly, right_poly]

    return output

def digest(seq, enzymes, fragselect):
    if isinstance(seq, str):
        seq = Polynucleotide(seq, '', '', True, False, 'hydroxyl', 'hydroxyl')

    enz_list = [enz.strip() for enz in enzymes.split(',') if enz.strip()]

    for enz in enz_list:
        if enz not in restriction_enzymes:
            raise ValueError(f'Enzyme "{enz}" not found.')

    frags_out = [seq]

    while True:
        worklist = frags_out[:]
        frags_out = []

        for poly in worklist:
            found_cut = False

            for enz in enz_list:
                frags = cut_once(poly, enz)
                if frags:
                    frags_out.extend(frags)
                    found_cut = True
                    break

            if not found_cut:
                frags_out.append(poly)

        if not found_cut:
            break

    if fragselect is not None and 0 <= fragselect < len(frags_out):
        if seq.is_circular:
            target_index = fragselect

            frags_out.sort(key=lambda x: seq.sequence.find(x.sequence))

            if seq.sequence.find(frags_out[0].sequence) != 0:
                first_frag = frags_out.pop(0)
                frags_out.append(first_frag)
                target_index = fragselect - 1 if fragselect != 0 else len(frags_out) - 1

            return frags_out[target_index]
        else:
            return frags_out[fragselect]
    else:
        raise ValueError('Invalid fragselect provided.')