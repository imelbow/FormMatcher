from typing import Optional
from pymongo import MongoClient
from src.common.logger import logger
from src.common.config import config

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class MongoDB:
    _instance: Optional['MongoDB'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.db_config = config['mongodb']
            try:
                self.conn = MongoClient(
                    self.db_config['dsn'],
                    serverSelectionTimeoutMS=5000
                )
                self.conn.admin.command('ping')
                self.db = self.conn['forms_db']
                self.form_templates = self.db['form_templates']
                self._init_templates()
                self._initialized = True
            except Exception as e:
                logger.error(f"Failed to connect to MongoDB: {str(e)}")
                raise

    def _init_templates(self):
        self.form_templates.delete_many({})
        self.form_templates.insert_many(self.db_config['templates'])
        logger.info("The database has been successfully optimized with templates.")


class DBMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, db_instance: MongoDB):
        super().__init__(app)
        self.db = db_instance

    async def dispatch(self, request: Request, call_next):
        request.state.db = self.db
        response = await call_next(request)
        return response
