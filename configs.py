from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "6942558543:AAGRQGTKHw2wT3e-vBE_WN9dBEoAKaw0Ad4")

config = Config()
