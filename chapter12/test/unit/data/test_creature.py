# python -m pytest -v test/unit/data/test_creature.py
import os, pytest 
from model.creature import Creature 
from error import Missing, Duplicate 

# set the environment variable before import 'init' or 'creature'
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import creature

# 'fixture' of typed 'Creature' named 'sample' is passed to EVERY functions below it
# Purpose: to make db state UNCHANGED after each test
@pytest.fixture 
def sample() -> Creature:
  return Creature(name="yeti", country="CN", area="Himalayas", description="Harmless Himalayan", aka="Abominable Snowman")

def test_create(sample):
  resp = creature.create(sample)
  assert resp==sample 

def test_create_duplicate(sample):
  with pytest.raises(Duplicate):
    _ = creature.create(sample)

def test_get_one(sample):
  resp = creature.get_one(sample.name)
  assert resp == sample

def test_get_one_missing():
  with pytest.raises(Missing):
    _ = creature.get_one("boxturtle")

def test_modify(sample):
  sample.country = "JP" # japan
  resp = creature.modify(sample)
  assert resp==sample 

def test_modify_missing():
  thing: Creature = Creature(name="snurfle", country="RU", area="", description="some thing", aka="")
  with pytest.raises(Missing):
    _ = creature.modify(thing)

def test_delete(sample):
  resp = creature.delete(sample)
  assert resp is None 

def test_delete_missing(sample):
  with pytest.raises(Missing):
    _ = creature.delete(sample)
