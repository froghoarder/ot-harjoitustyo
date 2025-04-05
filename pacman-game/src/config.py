import os
from dotenv import load_dotenv

directoryname = os.path.dirname(__file__)

try:
    load_dotenv(env_path=os.path.join(directoryname, "..", ".env"))
except FileNotFoundError:
    pass
