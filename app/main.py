import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.shanyrak.router import router as shanyraq_router
from app.comment.router import router as comment_router
from app.config import client, env, fastapi_config


app = FastAPI(**fastapi_config)


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

os.getenv()
app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)

app.include_router(shanyraq_router, prefix="", tags=["shanyraq"])   
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(comment_router, prefix="", tags=["Comment"])
