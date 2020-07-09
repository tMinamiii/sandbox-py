from contextlib import contextmanager
from time import sleep
from typing import Generator

from logger import Logger

log = Logger(__name__)


@contextmanager
def exception_handler(msg: str = "") -> Generator[None, None, None]:
    try:
        yield
    except Exception as e:
        log.error(str({e}))
        sleep(1)
