# Stubs for email._parseaddr (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any

def parsedate_tz(data): ...
def parsedate(data): ...
def mktime_tz(data): ...
def quote(str): ...

class AddrlistClass:
    specials = Undefined(Any)
    pos = Undefined(Any)
    LWS = Undefined(Any)
    CR = Undefined(Any)
    FWS = Undefined(Any)
    atomends = Undefined(Any)
    phraseends = Undefined(Any)
    field = Undefined(Any)
    commentlist = Undefined(Any)
    def __init__(self, field): ...
    def gotonext(self): ...
    def getaddrlist(self): ...
    def getaddress(self): ...
    def getrouteaddr(self): ...
    def getaddrspec(self): ...
    def getdomain(self): ...
    def getdelimited(self, beginchar, endchars, allowcomments=True): ...
    def getquote(self): ...
    def getcomment(self): ...
    def getdomainliteral(self): ...
    def getatom(self, atomends=None): ...
    def getphraselist(self): ...

class AddressList(AddrlistClass):
    addresslist = Undefined(Any)
    def __init__(self, field): ...
    def __len__(self): ...
    def __add__(self, other): ...
    def __iadd__(self, other): ...
    def __sub__(self, other): ...
    def __isub__(self, other): ...
    def __getitem__(self, index): ...
