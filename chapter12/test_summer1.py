# test mod2 (which uses mod1)
# pytest -q test_summer1.py
# => next question: how to test ONLY mod2 (the sum function) => mockup test
import mod2 

def test_summer():
  assert "The sum is 11" == mod2.summer(5, 6)
