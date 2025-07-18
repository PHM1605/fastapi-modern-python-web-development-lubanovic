# run this with "python -m web.tag"
import datetime
from model.tag import TagIn, Tag, TagOut 
import service.tag as service

@app.post('/')
def create(tag_in: TagIn) -> TagIn:
  tag: Tag = Tag(tag=tag_in.tag, created=datetime.utcnow(), secret="shhhh")
  service.create(tag)
  return tag_in 

# 'response_model' will strip-off the field "secret" in "Tag", converting it to "TagOut"
@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
  tag: Tag = service.get(tag_str)
  return tag 
  