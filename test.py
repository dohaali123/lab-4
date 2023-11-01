import pytest
import pickle
import os
from answers import *

DIRNAME = os.path.dirname(__file__)

@pytest.mark.m_1  # 2
def test_fastareader():
    assert (
        fastareader(f'{DIRNAME}/tests/test.fasta') == {"seq1": "ATCG", "seq2": "GCTA", "seq3": "CGAT"}
    ), "There is a problem with my fastareader function"

DNA = "ATGATGGCGAGCTAGCATACGCTTCAGACTG"

@pytest.mark.m_2  # 2
def test_getGCpercentage():
    assert (
        getGCpercentage(DNA) == 0.52
    ), "There is a problem with my getGCpercentage function"

@pytest.mark.m_3  # 2
def test_getobsCpGexpCpG():
    assert (
        getobsCpGexpCpG(DNA) == 0.98
    ), "There is a problem with my getobsCpGexpCpG function"

@pytest.mark.m_4  # 4
def test_getCpGislands():
    with open(f'{DIRNAME}/tests/dict.file', 'rb') as handle:
        sequences = pickle.load(handle)
    assert getCpGislands(sequences) == [
        "seq3",
        "seq4",
        "seq5",
        "seq7",
    ], "There is a problem with my getCpGislands function"