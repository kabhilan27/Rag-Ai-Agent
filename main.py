from fastapi import FastAPI

app = FastAPI(title="rag")

@app.get("/health")
async def health_check():
    return {"message": "ok"}
