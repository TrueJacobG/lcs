import pytest
from .lcs import LCSAlgorithm

class TestLCSAlgorithm:    
    @pytest.fixture
    def algo(self):
        return LCSAlgorithm("LCS Test")
    
    def test_basic_1(self, algo: LCSAlgorithm):
        X = "ABCDGH"
        Y = "AEDFHR"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 3
        assert subsequence == "ADH"
    
    def test_basic_2(self, algo: LCSAlgorithm):
        X = "AGGTAB"
        Y = "GXTXAYB"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 4
        assert subsequence == "GTAB"
    
    def test_identical_strings(self, algo: LCSAlgorithm):
        X = "ABCDEF"
        Y = "ABCDEF"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 6
        assert subsequence == "ABCDEF"
    
    def test_empty_strings(self, algo: LCSAlgorithm):
        length, subsequence = algo.lcs("", "")
        assert length == 0
        assert subsequence == ""
        
        length, subsequence = algo.lcs("ABC", "")
        assert length == 0
        assert subsequence == ""
        
        length, subsequence = algo.lcs("", "XYZ")
        assert length == 0
        assert subsequence == ""
    
    def test_no_common_subsequence(self, algo: LCSAlgorithm):
        X = "ABC"
        Y = "DEF"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 0
        assert subsequence == ""
    
    def test_single_character_common(self, algo: LCSAlgorithm):
        X = "ABCDEF"
        Y = "XYZC"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 1
        assert subsequence == "C"
    
    def test_one_is_subsequence_of_other(self, algo: LCSAlgorithm):
        X = "ABCDEFGH"
        Y = "ACE"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 3
        assert subsequence == "ACE"
    
    def test_repeated_characters(self, algo: LCSAlgorithm):
        X = "AAAA"
        Y = "AA"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 2
        assert subsequence == "AA"
    
    def test_reverse_strings(self, algo: LCSAlgorithm):
        X = "ABCD"
        Y = "DCBA"
        length, subsequence = algo.lcs(X, Y)
        
        # only one character can match
        assert length == 1
        assert len(subsequence) == 1
        assert subsequence in ["A", "B", "C", "D"]
    
    def test_single_character_strings(self, algo: LCSAlgorithm):
        length, subsequence = algo.lcs("A", "A")
        assert length == 1
        assert subsequence == "A"
        
        length, subsequence = algo.lcs("A", "B")
        assert length == 0
        assert subsequence == ""
    
    def test_numeric_strings(self, algo: LCSAlgorithm):
        X = "123456"
        Y = "246813"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 3
        assert subsequence == "246"
    
    def test_special_characters(self, algo: LCSAlgorithm):
        X = "A!B@C#"
        Y = "!@#ABC"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 3
        assert subsequence == "!@#"
    
    def test_case_sensitivity(self, algo: LCSAlgorithm):
        X = "ABC"
        Y = "abc"
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 0
        assert subsequence == ""
    
    def test_complexity_large_input(self, algo: LCSAlgorithm):
        X = "A" * 100 + "B" * 100
        Y = "B" * 100 + "A" * 100
        length, subsequence = algo.lcs(X, Y)
        
        assert length == 100
        assert len(subsequence) == 100
