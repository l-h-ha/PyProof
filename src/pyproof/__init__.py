from . import _config


def set_logging_state(state: bool) -> None:
    _config.logging = state
