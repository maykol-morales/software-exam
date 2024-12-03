from logging import getLogger

instance = getLogger("uvicorn")


def info(msg: str):
    instance.info(msg)


def warn(msg: str):
    instance.info(msg)


def error(msg: str):
    instance.info(msg)
