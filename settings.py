from envparse import Env


env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://andrii:5048@127.0.0.1:5432/postgres_5"
)
