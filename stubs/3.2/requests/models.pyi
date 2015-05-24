# Stubs for requests.models (Python 3)

from typing import Undefined, Any, List, MutableMapping, Iterator, Dict
import datetime

from . import hooks
from . import structures
from . import auth
from . import cookies
from .cookies import RequestsCookieJar
from .packages.urllib3 import fields
from .packages.urllib3 import filepost
from .packages.urllib3 import util
from .packages.urllib3 import exceptions as urllib3_exceptions
from . import exceptions
from . import utils
from . import compat
from . import status_codes

default_hooks = hooks.default_hooks
CaseInsensitiveDict = structures.CaseInsensitiveDict
HTTPBasicAuth = auth.HTTPBasicAuth
cookiejar_from_dict = cookies.cookiejar_from_dict
get_cookie_header = cookies.get_cookie_header
RequestField = fields.RequestField
encode_multipart_formdata = filepost.encode_multipart_formdata
parse_url = util.parse_url
DecodeError = urllib3_exceptions.DecodeError
ReadTimeoutError = urllib3_exceptions.ReadTimeoutError
ProtocolError = urllib3_exceptions.ProtocolError
LocationParseError = urllib3_exceptions.LocationParseError
HTTPError = exceptions.HTTPError
MissingSchema = exceptions.MissingSchema
InvalidURL = exceptions.InvalidURL
ChunkedEncodingError = exceptions.ChunkedEncodingError
ContentDecodingError = exceptions.ContentDecodingError
ConnectionError = exceptions.ConnectionError
StreamConsumedError = exceptions.StreamConsumedError
guess_filename = utils.guess_filename
get_auth_from_url = utils.get_auth_from_url
requote_uri = utils.requote_uri
stream_decode_response_unicode = utils.stream_decode_response_unicode
to_key_val_list = utils.to_key_val_list
parse_header_links = utils.parse_header_links
iter_slices = utils.iter_slices
guess_json_utf = utils.guess_json_utf
super_len = utils.super_len
to_native_string = utils.to_native_string
codes = status_codes.codes

REDIRECT_STATI = Undefined(Any)
DEFAULT_REDIRECT_LIMIT = Undefined(Any)
CONTENT_CHUNK_SIZE = Undefined(Any)
ITER_CHUNK_SIZE = Undefined(Any)
json_dumps = Undefined(Any)

class RequestEncodingMixin:
    @property
    def path_url(self): ...

class RequestHooksMixin:
    def register_hook(self, event, hook): ...
    def deregister_hook(self, event, hook): ...

class Request(RequestHooksMixin):
    hooks = Undefined(Any)
    method = Undefined(Any)
    url = Undefined(Any)
    headers = Undefined(Any)
    files = Undefined(Any)
    data = Undefined(Any)
    json = Undefined(Any)
    params = Undefined(Any)
    auth = Undefined(Any)
    cookies = Undefined(Any)
    def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None,
                 auth=None, cookies=None, hooks=None, json=None): ...
    def prepare(self): ...

class PreparedRequest(RequestEncodingMixin, RequestHooksMixin):
    method = Undefined(Any)
    url = Undefined(Any)
    headers = Undefined(Any)
    body = Undefined(Any)
    hooks = Undefined(Any)
    def __init__(self): ...
    def prepare(self, method=None, url=None, headers=None, files=None, data=None, params=None,
                auth=None, cookies=None, hooks=None, json=None): ...
    def copy(self): ...
    def prepare_method(self, method): ...
    def prepare_url(self, url, params): ...
    def prepare_headers(self, headers): ...
    def prepare_body(self, data, files, json=None): ...
    def prepare_content_length(self, body): ...
    def prepare_auth(self, auth, url=''): ...
    def prepare_cookies(self, cookies): ...
    def prepare_hooks(self, hooks): ...

class Response:
    __attrs__ = Undefined(Any)
    status_code = Undefined(int)
    headers = Undefined(MutableMapping[str, str])
    raw = Undefined(Any)
    url = Undefined(str)
    encoding = Undefined(str)
    history = Undefined(List[Response])
    reason = Undefined(str)
    cookies = Undefined(RequestsCookieJar)
    elapsed = Undefined(datetime.timedelta)
    request = Undefined(PreparedRequest)
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __iter__(self) -> Iterator[bytes]: ...
    @property
    def ok(self) -> bool: ...
    @property
    def is_redirect(self) -> bool: ...
    @property
    def is_permanent_redirect(self) -> bool: ...
    @property
    def apparent_encoding(self) -> str: ...
    def iter_content(self, chunk_size: int = 1,
                     decode_unicode: bool = False) -> Iterator[Any]: ...
    def iter_lines(self, chunk_size=Undefined, decode_unicode=None, delimiter=None): ...
    @property
    def content(self) -> bytes: ...
    @property
    def text(self) -> str: ...
    def json(self, **kwargs) -> Any: ...
    @property
    def links(self) -> Dict[Any, Any]: ...
    def raise_for_status(self) -> None: ...
    def close(self) -> None: ...
