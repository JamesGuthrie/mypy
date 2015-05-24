# Stubs for _dummy_thread

# NOTE: These are incomplete!

from typing import Undefined, Any

class LockType:
    def acquire(self) -> None: ...
    def release(self) -> None: ...

def allocate_lock() -> LockType: ...
