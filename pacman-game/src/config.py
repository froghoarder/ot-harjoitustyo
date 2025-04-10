import os
from dotenv import load_dotenv

directoryname = os.path.dirname(__file__)

try:
    env_path=os.path.join(directoryname, "..", ".env")
    load_dotenv(env_path)
except FileNotFoundError:
    pass
