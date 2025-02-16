import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_value(key) -> str:
    load_env()
    return os.getenv(key)