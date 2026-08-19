"""Connessioni centralizzate a Postgres e MongoDB, lette da variabili d'ambiente.

Uso:
    from src.db.connections import get_postgres_connection, get_mongo_client
"""

import os

from dotenv import load_dotenv

load_dotenv()


def get_postgres_dsn() -> str:
    return (
        f"host={os.getenv('POSTGRES_HOST', 'localhost')} "
        f"port={os.getenv('POSTGRES_PORT', '5432')} "
        f"dbname={os.getenv('POSTGRES_DB', 'news_market')} "
        f"user={os.getenv('POSTGRES_USER', 'postgres')} "
        f"password={os.getenv('POSTGRES_PASSWORD', '')}"
    )


def get_postgres_connection():
    import psycopg

    return psycopg.connect(get_postgres_dsn())


def get_mongo_client():
    from pymongo import MongoClient

    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    return MongoClient(uri)
