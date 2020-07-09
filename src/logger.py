"""Logger."""
from logging import INFO, Formatter, getLevelName, getLogger

import env


class Logger:
    """Logger."""

    def __init__(self, name: str = __name__):
        """logger初期化."""
        self.logger = getLogger(name)
        if env.LOG_LEVEL:
            level = getLevelName(env.LOG_LEVEL)
            self.logger.setLevel(level)
        else:
            self.logger.setLevel(INFO)
        formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")
        for handler in self.logger.handlers:
            handler.setFormatter(formatter)

    def debug(self, msg: str, stack_info: bool = False, exc_info: bool = False) -> None:
        """debugログ出力."""
        self.logger.debug(msg, stack_info=stack_info, exc_info=exc_info)

    def info(self, msg: str, stack_info: bool = False, exc_info: bool = False) -> None:
        """infoログ出力."""
        self.logger.info(msg, stack_info=stack_info, exc_info=exc_info)

    def warn(self, msg: str, stack_info: bool = False, exc_info: bool = False) -> None:
        """warnログ出力."""
        self.logger.warning(msg, stack_info=stack_info, exc_info=exc_info)

    def error(self, msg: str, stack_info: bool = True, exc_info: bool = True) -> None:
        """errorログ出力."""
        self.logger.error(msg, stack_info=stack_info, exc_info=exc_info)

    def critical(self, msg: str, stack_info: bool = False, exc_info: bool = False) -> None:
        """criticalログ出力."""
        self.logger.critical(msg, stack_info=stack_info, exc_info=exc_info)
