# Stubs for enum (Python 3.4)
#
# TODO: This isn't working yet!

class Enum:
    name = ''
    value = ''

    def __init__(self, value): ...

class IntEnum(int, Enum): ...

def unique(enumeration): ...
