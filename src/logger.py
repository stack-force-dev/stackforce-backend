import logging.config

from src.settings import settings


def configure_logging():
    logging.config.dictConfig(LOGGING_CONFIG)


class PackagePathFilter(logging.Filter):
    def _patch_pathname(self, record, piece: str):
        pathname = record.pathname
        if piece in pathname:
            index = pathname.index(piece)
            record.pathname = 'app->' + pathname[index + len(piece):]
        return record

    def filter(self, record):
        record = self._patch_pathname(record, '/src/tic_tac_toe/')
        record = self._patch_pathname(record, '/src/bin/')
        record = self._patch_pathname(record, '/site-packages/')
        return record


LOGGING_CONFIG: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)-5s] | "
                      "%(pathname)s@%(lineno)d | %(message)s"
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '[%(asctime)s] [%(levelname)-5s] | '
                   '%(name)s | %(client_addr)s - '
                   '"%(request_line)s" %(status_code)s',
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "filters": ['special']
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "filters":  ['special']
        },
        "null": {
            "class": "logging.NullHandler"
        },
    },
    'filters': {
        'special': {
            '()': PackagePathFilter
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["null", ],
            "propagate": False,
        },
        "asyncio": {
            "handlers": ["null", ],
            "propagate": False,
        },
        'alembic': {
            'handlers': ['default', ],
            'propagate': False,
        },
        "sqlalchemy.engine": {
            "handlers": ["null", ],
            "propagate": False,
        },
        # "uvicorn.error": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.access": {
            "handlers": ["access", ],
            "propagate": False,
        },
        "root": {
            "handlers": ["default", ],
            "level": settings.LOGGING_LEVEL,
        },
    },
}

