import pytest
import json
from cf_simpy.pcr import pcr


def load_test_data():
    with open('tests/pcr_test_data.json') as f:
        data = json.load(f)
    print(f'Loaded test data: {data}')
    return data


test_data = load_test_data()
print(test_data)

@pytest.mark.parametrize('data', test_data)
def test_pcr(data):
    for_oligo, rev_oligo, template, expected = data
    result = pcr(for_oligo, rev_oligo, template)
    assert result == expected