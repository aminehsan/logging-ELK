import logging
import logstash


class LogstashLogger:
    """A Python class for interacting with Logstash, a logger."""

    def __init__(self, host: str, port: int, level: int, project: str, name: str) -> None:
        self.__setup(name=name, level=level, host=host, port=port)
        self.__extra = {'project_name': project}

    def __setup(self, name: str, level: int | str, host: str, port: int):
        """Set up the logger."""
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(level)
        self.__logger.addHandler(logstash.TCPLogstashHandler(host=host, port=port, version=1))

    def debug(self, msg: str = '', extra: dict = None) -> None:
        extra = extra or dict()
        extra.update(self.__extra)
        self.__logger.debug(msg=msg, exc_info=True, stack_info=True, extra=extra)

    def info(self, msg: str = '', extra: dict = None) -> None:
        extra = extra or dict()
        extra.update(self.__extra)
        self.__logger.info(msg=msg, exc_info=True, stack_info=True, extra=extra)

    def warning(self, msg: str = '', extra: dict = None) -> None:
        extra = extra or dict()
        extra.update(self.__extra)
        self.__logger.warning(msg=msg, exc_info=True, stack_info=True, extra=extra)

    def error(self, msg: str = '', extra: dict = None) -> None:
        extra = extra or dict()
        extra.update(self.__extra)
        self.__logger.error(msg=msg, exc_info=True, stack_info=True, extra=extra)

    def critical(self, msg: str = '', extra: dict = None) -> None:
        extra = extra or dict()
        extra.update(self.__extra)
        self.__logger.critical(msg=msg, exc_info=True, stack_info=True, extra=extra)
