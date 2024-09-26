from typing import Protocol

from pathlib import Path

# NOTE: These type aliases cannot start with "Test" because then pytest will
#       believe that they are test classes, see https://stackoverflow.com/q/76689604/2173773


class PrepareConfigDir(Protocol):  # pragma: no cover
    def __call__(self, add_config_ini: bool) -> Path:
        pass


class PrepareDataDir(Protocol):  # pragma: no cover
    def __call__(self, datafile_exists: bool) -> Path:
        pass
