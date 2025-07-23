# <mod2> doesn't use <mod1>, but a fake dummy one
import os 
os.environ["UNIT_TEST"] = "true"

import mod2 
def test_summer_fake():
  assert "11" == mod2.summer(5,6)
