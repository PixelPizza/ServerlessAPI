from enum import Enum


class Role(Enum):
    CUSTOMER = 1 << 0
    WORKER = 1 << 1
    STAFF = 1 << 2
    ADMIN = 1 << 3
