from fastapi import FastAPI
from app.index import index
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_SHA = os.getenv("GITHUB_SHA", "unknown_version")
GITHUB_REF = os.getenv("GITHUB_REF", "unknown_branch")
PORT = os.environ.get("PORT", 8080)

app = FastAPI(
    title="OpenAI SDK Adapter",
    description="Adapter from OpenAI SDK to Yandex Cloud FoMo API, [full docs here!](https://ai-cookbook.ru/docs/adapter/)",
    version=f"{GITHUB_SHA=} - {GITHUB_REF=}"
)

app.include_router(index)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=int(PORT), host="0.0.0.0", reload=True)
