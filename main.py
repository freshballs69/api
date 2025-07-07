import os
from sanic import Sanic
from sanic.request import Request
from sanic.response import json, file_stream, text
import time
import aiofiles

app = Sanic("ImageStorageAPI")
app.config.CORS_ORIGINS = '*'

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.static('api/uploads/', 'uploads/', directory_view=True)

@app.post("/api/upload")
async def upload_image(request: Request):
    try:
        photo = request.files["file"][0].body
        save_path = os.path.join(UPLOAD_FOLDER, f'{time.time()}.png')
        async with aiofiles.open(save_path, "wb") as f:
            await f.write(photo)
        return text('ok')
    except:
        return text('fuck you')
