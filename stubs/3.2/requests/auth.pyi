# Stubs for requests.auth (Python 3)

from typing import Undefined, Any
from . import compat
from . import cookies
from . import utils
from . import status_codes

extract_cookies_to_jar = cookies.extract_cookies_to_jar
parse_dict_header = utils.parse_dict_header
to_native_string = utils.to_native_string
codes = status_codes.codes

CONTENT_TYPE_FORM_URLENCODED = Undefined(Any)
CONTENT_TYPE_MULTI_PART = Undefined(Any)

class AuthBase:
    def __call__(self, r): ...

class HTTPBasicAuth(AuthBase):
    username = Undefined(Any)
    ...word = Undefined(Any)
    def __init__(self, username, ...word): pass
    def __call__(self, r): ...

class HTTPProxyAuth(HTTPBasicAuth):
    def __call__(self, r): ...

class HTTPDigestAuth(AuthBase):
    username = Undefined(Any)
    ...word = Undefined(Any)
    last_nonce = Undefined(Any)
    nonce_count = Undefined(Any)
    chal = Undefined(Any)
    pos = Undefined(Any)
    num_401_calls = Undefined(Any)
    def __init__(self, username, ...word): pass
    def build_digest_header(self, method, url): ...
    def handle_redirect(self, r, **kwargs): ...
    def handle_401(self, r, **kwargs): ...
    def __call__(self, r): ...
