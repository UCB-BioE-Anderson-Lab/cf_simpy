import pytest
import pandas as pd
from cf_simpy.polynucleotide import oligo, dsDNA, plasmid, Polynucleotide
from cf_simpy.pcr import pcr


test_data = pd.read_csv('tests/pcr_test_data.tsv', sep='\t')


@pytest.mark.parametrize('data', test_data.itertuples(index=False))
def test_pcr(data):
    for_oligo_seq = data.for_oligo
    rev_oligo_seq = data.rev_oligo
    template_seq = data.template_seq if pd.notnull(data.template_seq) else ''
    template_ext5 = data.template_ext5 if pd.notnull(data.template_ext5) else ''
    template_ext3 = data.template_ext3 if pd.notnull(data.template_ext3) else ''
    template_is_double_stranded = data.template_is_double_stranded if pd.notnull(data.template_is_double_stranded) else False
    template_is_circular = data.template_is_circular if pd.notnull(data.template_is_circular) else False
    template_mod_ext5 = data.template_mod_ext5 if pd.notnull(data.template_mod_ext5) else ''
    template_mod_ext3 = data.template_mod_ext3 if pd.notnull(data.template_mod_ext3) else ''
    expected_seq = data.expected_seq if pd.notnull(data.expected_seq) else ''
    expected_ext5 = data.expected_ext5 if pd.notnull(data.expected_ext5) else ''
    expected_ext3 = data.expected_ext3 if pd.notnull(data.expected_ext3) else ''
    expected_is_double_stranded = data.expected_is_double_stranded if pd.notnull(data.expected_is_double_stranded) else False
    expected_is_circular = data.expected_is_circular if pd.notnull(data.expected_is_circular) else False
    expected_mod_ext5 = data.expected_mod_ext5 if pd.notnull(data.expected_mod_ext5) else ''
    expected_mod_ext3 = data.expected_mod_ext3 if pd.notnull(data.expected_mod_ext3) else ''
    should_throw_error = data.should_throw_error

    for_oligo = oligo(for_oligo_seq)
    rev_oligo = oligo(rev_oligo_seq)
    template = Polynucleotide(template_seq, template_ext5, template_ext3, template_is_double_stranded, template_is_circular, template_mod_ext5, template_mod_ext3)
    expected = Polynucleotide(expected_seq, expected_ext5, expected_ext3, expected_is_double_stranded, expected_is_circular, expected_mod_ext5, expected_mod_ext3)

    if should_throw_error:
        with pytest.raises(Exception):
            result = pcr(for_oligo, rev_oligo, template)
    else:
        result = pcr(for_oligo, rev_oligo, template)
        assert result == expected
