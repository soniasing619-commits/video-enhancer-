from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil, os
from enhancer import enhance_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"
    
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output = enhance_video(path)

    return {"output": output}
