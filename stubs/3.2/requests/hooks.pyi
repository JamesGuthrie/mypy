# Stubs for requests.hooks (Python 3)

from typing import Undefined, Any

HOOKS = Undefined(Any)

def default_hooks(): ...
def dispatch_hook(key, hooks, hook_data, **kwargs): ...
