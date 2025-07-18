import datetime
import pytest
from fastapi.encoders import jsonable_encoder
import json 

@pytest.fixture
def data():
  return datetime.datetime.now()

def test_json_dump(data):
  with pytest.raises(Exception):
    _ = json.dumps(data)

def test_encoder(data):
  out = jsonable_encoder(data) # convert any data to JSONable data
  assert(out)
  json_out = json.dumps(out) # convert JSONable data to json before return
  assert(json_out)