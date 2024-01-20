import os

from dotenv import load_dotenv

load_dotenv()


def get_environment(key: str):
    return os.getenv(key)
