import os
from sqlmodel import create_engine, SQLModel

from dotenv import load_dotenv

import db.models

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
