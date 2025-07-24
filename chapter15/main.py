# uvicorn main:app 
# To test: 'cd client_folder' first
# http -f -b POST http://localhost:8000/small small_file@test_uploaded_file.txt
# OR python send_small.py
from fastapi import File, FastAPI
app = FastAPI()
# Upload small file to server
@app.post("/small")
async def upload_small_file(small_file:bytes=File())->str:
  # small_file: b'This is only a test file\r\n' (content of the 'test_uploaded_file.txt')
  return f"file size: {len(small_file)}"

# http -f -b POST http://localhost:8000/big big_file@test_uploaded_file.txt
# OR python send_big.py
from fastapi import UploadFile 
@app.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
  return f"file size: {big_file.size}, name: {big_file.filename}"

# http -b http://localhost:8000/small/test_downloaded_file.txt | wc -c (word count)
from fastapi.responses import FileResponse 
@app.get("/small/{name}")
async def download_small_file(name):
  return FileResponse(name) # content of file e.g. "This is a test downloaded file."

# http -b http://localhost:8000/download_big/test_downloaded_file.txt | wc -c 
from pathlib import Path 
from typing import Generator 
from fastapi.responses import StreamingResponse 
def gen_file(path:str) -> Generator:
  with open(file=path, mode="rb") as file:
    yield file.read()
@app.get("/download_big/{name}")
async def download_big_file(name:str):
  path = Path(".") / name 
  gen_expr = gen_file(path=path)
  response = StreamingResponse(content=gen_expr, status_code=200)
  return response 

# free folder to download files
# http -b localhost:8000/static/abc.txt
# http -b localhost:8000/static/ (as we passed StaticFiles(..., html=True), we automatically serve index.html)
# http -b localhost:8000/static/xyz/ (for index.html inside sub-directory 'xyz')
from fastapi.staticfiles import StaticFiles 
top = Path(__file__).resolve().parent 
app.mount("/static", StaticFiles(directory=f"{top}/static", html=True), name="free")