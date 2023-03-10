from __future__ import annotations

from enum import Enum


class Environment(str, Enum):
    STAGE = 'stage'
    PRE = 'pre'
    PROD = 'prod'
    LOCAL = 'local'
    UNKNOWN = 'unknown'

    def is_local(self) -> bool:
        return self in (Environment.UNKNOWN, Environment.LOCAL)

    @classmethod
    def from_str(cls, param: str) -> Environment:
        try:
            return cls(param.lower())
        except ValueError:
            return cls.UNKNOWN
