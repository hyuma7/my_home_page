from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from ownlib.extract_text_from_video import extract_text_from_video
import asyncio

app = FastAPI()

# 非同期ジェネレータ関数
async def extract_text_gen(video_path, roi, frame_interval):
    for frame_count, num in extract_text_from_video(video_path, roi, frame_interval):
        yield frame_count, num
        await asyncio.sleep(0)  # 他の非同期タスクが実行される余地を与えます

# POSTメソッド用エンドポイント
@app.post("/extract_text/")
async def extract_text_post(video_path: str, x: int, y: int, w: int, h: int):
    roi = (x, y, w, h)
    frame_interval = 120  # フレーム間隔を固定値として設定します
    
    async def stream_result():
        async for frame_count, num in extract_text_gen(video_path, roi, frame_interval):
            yield f"Frame: {frame_count}, Num: {num}\n"
    
    return StreamingResponse(stream_result(), media_type="text/plain")

# GETメソッド用エンドポイント
@app.get("/extract_text/")
async def extract_text_get(video_path: str, x: int, y: int, w: int, h: int):
    roi = (x, y, w, h)
    frame_interval = 120  # フレーム間隔を固定値として設定します
    
    async def stream_result():
        async for frame_count, num in extract_text_gen(video_path, roi, frame_interval):
            yield f"Frame: {frame_count}, Num: {num}\n"
    
    return StreamingResponse(stream_result(), media_type="text/plain")