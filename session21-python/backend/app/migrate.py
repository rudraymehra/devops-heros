"""Serialize migrations so a multi-replica rollout cannot race table creation."""
from alembic import command
from alembic.config import Config
from sqlalchemy import text

from .db import engine


def main():
    with engine.connect() as connection:
        postgres = connection.dialect.name == "postgresql"
        if postgres:
            connection.execute(text("SELECT pg_advisory_lock(2410425)"))
        try:
            command.upgrade(Config("alembic.ini"), "head")
        finally:
            if postgres:
                connection.execute(text("SELECT pg_advisory_unlock(2410425)"))


if __name__ == "__main__":
    main()
