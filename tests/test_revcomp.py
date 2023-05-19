import pytest
import pandas as pd
from cf_simpy.revcomp import revcomp


test_data = pd.read_csv('tests/revcomp_test_data.txt', sep='\t')


@pytest.mark.parametrize('data', test_data.itertuples(index=False))
def test_revcomp(data):
    input_seq = data.input_seq
    expected_output = data.output_seq
    should_throw_error = data.should_throw_error

    if should_throw_error:
        with pytest.raises(Exception):
            result = revcomp(input_seq)
    else:
        result = revcomp(input_seq)
        assert result == expected_output