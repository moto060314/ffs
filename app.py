from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import socketio
import pymysql

# Socket.IOサーバー
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
asgi_app = socketio.ASGIApp(sio, app)

# 静的ファイル
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# DB接続情報
def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",    # Password を設定
        database="ffs",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

# メッセージ取得API
@app.get("/messages")
async def get_messages():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM messages ORDER BY created_at DESC LIMIT 20")
        messages = cur.fetchall()
    conn.close()
    return messages

# メッセージ投稿API
@app.post("/message")
async def post_message(message: str = Form(...)):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
        conn.commit()
    conn.close()
    await sio.emit("new_message", {"content": message})
    return RedirectResponse("/", status_code=303)

# トップページ
@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")

# Socket.IOイベント
@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

def main():
    import uvicorn
    uvicorn.run(asgi_app, host="localhost", port=3000)

if __name__ == "__main__":
    main()