from collections import Counter, defaultdict 
import data.game as data 

def get_word() -> str:
  return data.get_word()

HIT = "H"
MISS = "M"
CLOSE = "C" # letter is in the word, but at another position
ERROR = "" # Player doesn't fill all the input char slots

# score: "MMHCMMC"
def get_score(actual:str, guess:str) -> str:
  length:int = len(actual) # solution word length
  if len(guess) != length:
    return ERROR
  actual_counter = Counter(actual) # bigfoot->{'b':1, 'i':1, 'o':2,...}
  guess_counter = defaultdict(int) 
  result = [MISS] * length; # "MMMMMMM"
  # mark which char in <guess> is a HIT
  for pos, letter in enumerate(guess):
    if letter == actual[pos]:
      result[pos] = HIT
      guess_counter[letter] += 1
  # mark the char not yet HIT but correct char, just in wrong position
  for pos, letter in enumerate(guess):
    if result[pos] == HIT: continue
    # e.g. if guess 'xoxxxox' for 'bigfoot', actual_counter['o']=2 => for the first 'o' in 'xoxxxox' must be marked as 'CLOSE'
    guess_counter[letter] += 1
    if (letter in actual and guess_counter[letter] <= actual_counter[letter]):
      result[pos] = CLOSE 
  result = ''.join(result)
  return result

