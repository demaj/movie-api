from config.settings.base import *
from config.settings.base import env

DEBUG = True

SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    default="d0075a28a745ba423da14edbf3863376a04c741ea23ca9fd1024202d53214bac",
)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
