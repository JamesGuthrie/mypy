# Stubs for inspect

from typing import Undefined, Any, Tuple, List, Callable

_object = object

def getmembers(obj: object, predicate: Callable[[Any], bool]) -> List[Tuple[str, object]]: ...

def isclass(obj: object) -> bool: ...

# namedtuple('Attribute', 'name kind defining_class object')
class Attribute(tuple):
    name = Undefined(str)
    kind = Undefined(str)
    defining_class = Undefined(type)
    object = Undefined(_object)

def classify_class_attrs(cls: type) -> List[Attribute]: ...

def cleandoc(doc: str) -> str: ...

def getsourcelines(obj: object) -> Tuple[List[str], int]: ...

# namedtuple('ArgSpec', 'args varargs keywords defaults')
class ArgSpec(tuple):
    args = Undefined(List[str])
    varargs = Undefined(str)
    keywords = Undefined(str)
    defaults = Undefined(tuple)

def getargspec(func: object) -> ArgSpec: ...
