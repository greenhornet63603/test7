import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8212010986:AAH7ZZIF3SvuBY_aYvLfl6fdJ1bO7sOEfqE")
    API_ID = int(os.environ.get("API_ID", "27400172"))
    API_HASH = os.environ.get("API_HASH", "56d0a75c5f9a9de6beb5452aa63c2d36")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7540570087")

