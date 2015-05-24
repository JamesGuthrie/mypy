# Stubs for _thread

# NOTE: These are incomplete!

from typing import Undefined, Any

def _count() -> int: ...
_dangling = Undefined(Any)

class LockType:
    def acquire(self) -> None: ...
    def release(self) -> None: ...

def allocate_lock() -> LockType: ...
