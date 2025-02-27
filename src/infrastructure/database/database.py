from pymongo import MongoClient
from pymongo.database import Database
from application.config.settings import settings
from core.errors.exeptions import DatabaseException


class MongoDBConnection:
    _client: MongoClient = None
    _db: Database = None

    @classmethod
    def get_db(cls) -> Database:
        if not cls._db:
            try:
                print(settings.MONGODB_USERNAME)
                print(settings.MONGODB_PASSWORD)
                cls._client = MongoClient(
                    f"mongodb+srv://{settings.MONGODB_USERNAME}:"
                    f"{settings.MONGODB_PASSWORD}"
                    "@venus.tlv0e.mongodb.net/?retryWrites=true&w=majority"
                    "&appName=venus"
                )
                cls._db = cls._client[settings.MONGODB_NAME]
                cls._db.command('ping')
            except Exception as e:
                raise DatabaseException(
                    f"Database connection failed: {str(e)}"
                )
        return cls._db

    @classmethod
    def close_connection(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None
