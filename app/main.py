from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"  # 모든 origin 허용
    # "http://localhost",
    # "http://localhost:8080",
]

# CORS 미들웨어 설정 - 올바른 구문
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # origins 리스트 사용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
