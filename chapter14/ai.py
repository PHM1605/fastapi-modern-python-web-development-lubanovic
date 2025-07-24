# uvicorn ai:app
# http -b localhost:8000/ai line=="What are you?"
from fastapi import FastAPI 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig

app = FastAPI()
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = GenerationConfig(max_length=20)

@app.get("/ai")
def prompt(line: str) -> str:
  tokens = tokenizer(line, return_tensors='pt') # {'input_ids': tensor[[],[],], 'attention_mask': tensor[xxxxx]}
  generation_args = config.to_dict()
  generation_args["decoder_start_token_id"] = model.config.decoder_start_token_id
  outputs = model.generate(**tokens, **generation_args) # tensor([[...]])
  result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
  return result[0]