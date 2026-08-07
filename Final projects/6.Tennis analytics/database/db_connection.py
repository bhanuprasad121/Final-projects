import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def get_engine():
    """Create and return a MySQL SQLAlchemy connection."""

    username = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    database = os.getenv("DB_NAME", "tennis_analytics")
   

    connection_url = (
        f"mysql+pymysql://{username}:{password}"
        f"@{host}/{database}"
    )

    return create_engine(connection_url)

