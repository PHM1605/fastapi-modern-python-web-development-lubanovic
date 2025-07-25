# python -m pytest -q test/unit/service/test_game.py
import pytest 
from service import game 

# to test the score returning from backend (2nd element) for each guess (1st element) 
word = "bigfoot"
guesses = [
  ("bigfoot", "HHHHHHH"),
  ("abcdefg", "MCMMMCC"),
  ("toofgib", "CCCHCCC"),
  ("wronglength", ""),
  ("", "")
]

# i.e. picking each line of <guesses> to test
@pytest.mark.parametrize("guess,score", guesses)
def test_match(guess, score):
  assert game.get_score(word, guess) == score 
