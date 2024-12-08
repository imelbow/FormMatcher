from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.common.db import DBMiddleware, MongoDB
from src.common.docs import api_docs
from src.common.routes import load_routes


def build_app() -> FastAPI:
    routes = load_routes()

    app = FastAPI(
        title=api_docs['info']['title'],
        description=api_docs['info']['description'],
        version=api_docs['info']['version'],
        openapi_tags=api_docs['tags']
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    db = MongoDB()
    app.add_middleware(DBMiddleware, db_instance=db)

    for router in routes:
        app.include_router(router)

    return app


app = build_app()
