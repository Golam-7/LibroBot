from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pytesseract
import cv2
import numpy as np

app = FastAPI()

@app.post("/detect_book/")
async def detect_book(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(img)
    return JSONResponse(content={"text": text})
