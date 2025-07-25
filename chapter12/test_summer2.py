# mock-test means removing the effect of <mod1.preamble> 
# i.e. assuming having called it first already and receive the result ""
# pytest -q test_summer2.py
from unittest import mock
import mod1 
import mod2 

def test_summer_a():
  with mock.patch("mod1.preamble", return_value=""):
    assert "11" == mod2.summer(5,6)

def test_summer_b():
  with mock.patch("mod1.preamble") as mock_preamble:
    mock_preamble.return_value = ""
    assert "11" == mod2.summer(5,6)

@mock.patch("mod1.preamble", return_value="")
def test_summer_c(mock_preamble):
  assert "11" == mod2.summer(5,6)

@mock.patch("mod1.preamble")
def test_summer_d(mock_preamble):
  mock_preamble.return_value = ""
  assert "11" == mod2.summer(5,6)

