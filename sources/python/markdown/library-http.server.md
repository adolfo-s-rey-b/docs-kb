### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/http.cookies.html "http.cookies — HTTP state management")
     |
*   [previous](https://docs.python.org/3/library/socketserver.html "socketserver — A framework for network servers")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
     »
*   [`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`http.server` — HTTP servers[¶](https://docs.python.org/3/library/http.server.html#module-http.server "Link to this heading")

==============================================================================================================================

**Source code:** [Lib/http/server.py](https://github.com/python/cpython/tree/3.15/Lib/http/server.py)

* * *

This module defines classes for implementing HTTP servers.

Warning

`http.server` is not recommended for production. It only implements [basic security checks](https://docs.python.org/3/library/http.server.html#http-server-security)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

One class, [`HTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer "http.server.HTTPServer")
, is a [`socketserver.TCPServer`](https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer "socketserver.TCPServer")
 subclass. It creates and listens at the HTTP socket, dispatching the requests to a handler. Code to create and run the server looks like this:

Copy

def run(server\_class\=HTTPServer, handler\_class\=BaseHTTPRequestHandler):
    server\_address \= ('', 8000)
    httpd \= server\_class(server\_address, handler\_class)
    httpd.serve\_forever()

class http.server.HTTPServer(_server\_address_, _RequestHandlerClass_)[¶](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer "Link to this definition")

This class builds on the [`TCPServer`](https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer "socketserver.TCPServer")
 class by storing the server address as instance variables named [`server_name`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer.server_name "http.server.HTTPServer.server_name")
 and [`server_port`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer.server_port "http.server.HTTPServer.server_port")
. The server is accessible by the handler, typically through the handler’s [`server`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseRequestHandler.server "socketserver.BaseRequestHandler.server")
 instance variable.

server\_name[¶](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer.server_name "Link to this definition")

The HTTP server’s fully qualified domain name.

server\_port[¶](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer.server_port "Link to this definition")

The HTTP server’s port number obtained from _server\_address_.

class http.server.ThreadingHTTPServer(_server\_address_, _RequestHandlerClass_)[¶](https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPServer "Link to this definition")

This class is identical to HTTPServer but uses threads to handle requests by using the [`ThreadingMixIn`](https://docs.python.org/3/library/socketserver.html#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn")
. This is useful to handle web browsers pre-opening sockets, on which [`HTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer "http.server.HTTPServer")
 would wait indefinitely.

Added in version 3.7.

class http.server.HTTPSServer(_server\_address_, _RequestHandlerClass_, _bind\_and\_activate\=True_, _\*_, _certfile_, _keyfile\=None_, _password\=None_, _alpn\_protocols\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.HTTPSServer "Link to this definition")

Subclass of [`HTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer "http.server.HTTPServer")
 with a wrapped socket using the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
 module. If the `ssl` module is not available, instantiating a `HTTPSServer` object fails with a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
.

The _certfile_ argument is the path to the SSL certificate chain file, and the _keyfile_ is the path to the file containing the private key.

A _password_ can be specified for files protected and wrapped with PKCS#8, but beware that this could possibly expose hardcoded passwords in clear.

See also

See [`ssl.SSLContext.load_cert_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain "ssl.SSLContext.load_cert_chain")
 for additional information on the accepted values for _certfile_, _keyfile_ and _password_.

When specified, the _alpn\_protocols_ argument must be a sequence of strings specifying the “Application-Layer Protocol Negotiation” (ALPN) protocols supported by the server. ALPN allows the server and the client to negotiate the application protocol during the TLS handshake.

By default, it is set to `["http/1.1"]`, meaning the server supports HTTP/1.1.

Added in version 3.14.

class http.server.ThreadingHTTPSServer(_server\_address_, _RequestHandlerClass_, _bind\_and\_activate\=True_, _\*_, _certfile_, _keyfile\=None_, _password\=None_, _alpn\_protocols\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPSServer "Link to this definition")

This class is identical to [`HTTPSServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPSServer "http.server.HTTPSServer")
 but uses threads to handle requests by inheriting from [`ThreadingMixIn`](https://docs.python.org/3/library/socketserver.html#socketserver.ThreadingMixIn "socketserver.ThreadingMixIn")
. This is analogous to [`ThreadingHTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPServer "http.server.ThreadingHTTPServer")
 only using `HTTPSServer`.

Added in version 3.14.

The [`HTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer "http.server.HTTPServer")
, [`ThreadingHTTPServer`](https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPServer "http.server.ThreadingHTTPServer")
, [`HTTPSServer`](https://docs.python.org/3/library/http.server.html#http.server.HTTPSServer "http.server.HTTPSServer")
 and [`ThreadingHTTPSServer`](https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPSServer "http.server.ThreadingHTTPSServer")
 must be given a _RequestHandlerClass_ on instantiation, of which this module provides three different variants:

class http.server.BaseHTTPRequestHandler(_request_, _client\_address_, _server_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler "Link to this definition")

This class is used to handle the HTTP requests that arrive at the server. By itself, it cannot respond to any actual HTTP requests; it must be subclassed to handle each request method (for example, `'GET'` or `'POST'`). `BaseHTTPRequestHandler` provides a number of class and instance variables, and methods for use by subclasses.

The handler will parse the request and the headers, then call a method specific to the request type. The method name is constructed from the request. For example, for the request method `SPAM`, the `do_SPAM()` method will be called with no arguments. All of the relevant information is stored in instance variables of the handler. Subclasses should not need to override or extend the `__init__()` method.

`BaseHTTPRequestHandler` has the following instance variables:

client\_address[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.client_address "Link to this definition")

Contains a tuple of the form `(host, port)` referring to the client’s address.

server[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.server "Link to this definition")

Contains the server instance.

close\_connection[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.close_connection "Link to this definition")

Boolean that should be set before [`handle_one_request()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.handle_one_request "http.server.BaseHTTPRequestHandler.handle_one_request")
 returns, indicating if another request may be expected, or if the connection should be shut down.

requestline[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.requestline "Link to this definition")

Contains the string representation of the HTTP request line. The terminating CRLF is stripped. This attribute should be set by [`handle_one_request()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.handle_one_request "http.server.BaseHTTPRequestHandler.handle_one_request")
. If no valid request line was processed, it should be set to the empty string.

command[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.command "Link to this definition")

Contains the command (request type). For example, `'GET'`.

path[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.path "Link to this definition")

Contains the request path. If the query component of the URL is present, then `path` includes the query. Using the terminology of [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html)
, `path` here includes `hier-part` and the `query`.

request\_version[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.request_version "Link to this definition")

Contains the version string from the request. For example, `'HTTP/1.0'`.

headers[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.headers "Link to this definition")

Holds an instance of the class specified by the [`MessageClass`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.MessageClass "http.server.BaseHTTPRequestHandler.MessageClass")
 class variable. This instance parses and manages the headers in the HTTP request. The [`parse_headers()`](https://docs.python.org/3/library/http.client.html#http.client.parse_headers "http.client.parse_headers")
 function from [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).")
 is used to parse the headers and it requires that the HTTP request provide a valid [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 style header.

rfile[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.rfile "Link to this definition")

An [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
 input stream, ready to read from the start of the optional input data.

wfile[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.wfile "Link to this definition")

Contains the output stream for writing a response back to the client. Proper adherence to the HTTP protocol must be used when writing to this stream in order to achieve successful interoperation with HTTP clients.

Changed in version 3.6: This is an [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
 stream.

`BaseHTTPRequestHandler` has the following attributes:

server\_version[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.server_version "Link to this definition")

Specifies the server software version. You may want to override this. The format is multiple whitespace-separated strings, where each string is of the form name\[/version\]. For example, `'BaseHTTP/0.2'`.

sys\_version[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.sys_version "Link to this definition")

Contains the Python system version, in a form usable by the [`version_string`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.version_string "http.server.BaseHTTPRequestHandler.version_string")
 method and the [`server_version`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.server_version "http.server.BaseHTTPRequestHandler.server_version")
 class variable. For example, `'Python/1.4'`.

error\_message\_format[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.error_message_format "Link to this definition")

Specifies a format string that should be used by [`send_error()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_error "http.server.BaseHTTPRequestHandler.send_error")
 method for building an error response to the client. The string is filled by default with variables from [`responses`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses "http.server.BaseHTTPRequestHandler.responses")
 based on the status code passed to `send_error()`.

error\_content\_type[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.error_content_type "Link to this definition")

Specifies the Content-Type HTTP header of error responses sent to the client. The default value is `'text/html'`.

protocol\_version[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.protocol_version "Link to this definition")

Specifies the HTTP version to which the server is conformant. It is sent in responses to let the client know the server’s communication capabilities for future requests. If set to `'HTTP/1.1'`, the server will permit HTTP persistent connections; however, your server _must_ then include an accurate `Content-Length` header (using [`send_header()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_header "http.server.BaseHTTPRequestHandler.send_header")
) in all of its responses to clients. For backwards compatibility, the setting defaults to `'HTTP/1.0'`.

MessageClass[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.MessageClass "Link to this definition")

Specifies an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
\-like class to parse HTTP headers. Typically, this is not overridden, and it defaults to [`http.client.HTTPMessage`](https://docs.python.org/3/library/http.client.html#http.client.HTTPMessage "http.client.HTTPMessage")
.

responses[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses "Link to this definition")

This attribute contains a mapping of error code integers to two-element tuples containing a short and long message. For example, `{code: (shortmessage, longmessage)}`. The _shortmessage_ is usually used as the _message_ key in an error response, and _longmessage_ as the _explain_ key. It is used by [`send_response_only()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_response_only "http.server.BaseHTTPRequestHandler.send_response_only")
 and [`send_error()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_error "http.server.BaseHTTPRequestHandler.send_error")
 methods.

A `BaseHTTPRequestHandler` instance has the following methods:

handle()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.handle "Link to this definition")

Calls [`handle_one_request()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.handle_one_request "http.server.BaseHTTPRequestHandler.handle_one_request")
 once (or, if persistent connections are enabled, multiple times) to handle incoming HTTP requests. You should never need to override it; instead, implement appropriate `do_*()` methods.

handle\_one\_request()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.handle_one_request "Link to this definition")

This method will parse and dispatch the request to the appropriate `do_*()` method. You should never need to override it.

handle\_expect\_100()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.handle_expect_100 "Link to this definition")

When an HTTP/1.1 conformant server receives an `Expect: 100-continue` request header it responds with a `100 Continue` followed by `200 OK` headers. This method can be overridden to raise an error if the server does not want the client to continue. For example, the server can choose to send `417 Expectation Failed` as a response header and `return False`.

Added in version 3.2.

send\_error(_code_, _message\=None_, _explain\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_error "Link to this definition")

Sends and logs a complete error reply to the client. The numeric _code_ specifies the HTTP error code, with _message_ as an optional, short, human readable description of the error. The _explain_ argument can be used to provide more detailed information about the error; it will be formatted using the [`error_message_format`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.error_message_format "http.server.BaseHTTPRequestHandler.error_message_format")
 attribute and emitted, after a complete set of headers, as the response body. The [`responses`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses "http.server.BaseHTTPRequestHandler.responses")
 attribute holds the default values for _message_ and _explain_ that will be used if no value is provided; for unknown codes the default value for both is the string `???`. The body will be empty if the method is HEAD or the response code is one of the following: `1_xx_`, `204 No Content`, `205 Reset Content`, `304 Not Modified`.

Changed in version 3.4: The error response includes a Content-Length header. Added the _explain_ argument.

send\_response(_code_, _message\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_response "Link to this definition")

Adds a response header to the headers buffer and logs the accepted request. The HTTP response line is written to the internal buffer, followed by _Server_ and _Date_ headers. The values for these two headers are picked up from the [`version_string()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.version_string "http.server.BaseHTTPRequestHandler.version_string")
 and [`date_time_string()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.date_time_string "http.server.BaseHTTPRequestHandler.date_time_string")
 methods, respectively. If the server does not intend to send any other headers using the [`send_header()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_header "http.server.BaseHTTPRequestHandler.send_header")
 method, then `send_response()` should be followed by an [`end_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers "http.server.BaseHTTPRequestHandler.end_headers")
 call.

Changed in version 3.3: Headers are stored to an internal buffer and [`end_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers "http.server.BaseHTTPRequestHandler.end_headers")
 needs to be called explicitly.

send\_header(_keyword_, _value_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_header "Link to this definition")

Adds the HTTP header to an internal buffer which will be written to the output stream when either [`end_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers "http.server.BaseHTTPRequestHandler.end_headers")
 or [`flush_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.flush_headers "http.server.BaseHTTPRequestHandler.flush_headers")
 is invoked. _keyword_ should specify the header keyword, with _value_ specifying its value. Note that, after the send\_header calls are done, `end_headers()` MUST BE called in order to complete the operation.

This method does not reject input containing CRLF sequences.

Changed in version 3.2: Headers are stored in an internal buffer.

send\_response\_only(_code_, _message\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_response_only "Link to this definition")

Sends the response header only, used for the purposes when `100 Continue` response is sent by the server to the client. The headers are not buffered and sent directly the output stream. If the _message_ is not specified, the HTTP message corresponding the response _code_ is sent.

This method does not reject _message_ containing CRLF sequences.

Added in version 3.2.

end\_headers()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers "Link to this definition")

Adds a blank line (indicating the end of the HTTP headers in the response) to the headers buffer and calls [`flush_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.flush_headers "http.server.BaseHTTPRequestHandler.flush_headers")
.

Changed in version 3.2: The buffered headers are written to the output stream.

flush\_headers()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.flush_headers "Link to this definition")

Finally send the headers to the output stream and flush the internal headers buffer.

Added in version 3.3.

log\_request(_code\='-'_, _size\='-'_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.log_request "Link to this definition")

Logs an accepted (successful) request. _code_ should specify the numeric HTTP code associated with the response. If a size of the response is available, then it should be passed as the _size_ parameter.

log\_error(_..._)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.log_error "Link to this definition")

Logs an error when a request cannot be fulfilled. By default, it passes the message to [`log_message()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.log_message "http.server.BaseHTTPRequestHandler.log_message")
, so it takes the same arguments (_format_ and additional values).

log\_message(_format_, _..._)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.log_message "Link to this definition")

Logs an arbitrary message to `sys.stderr`. This is typically overridden to create custom error logging mechanisms. The _format_ argument is a standard printf-style format string, where the additional arguments to `log_message()` are applied as inputs to the formatting. The client IP address and current date and time are prefixed to every message logged.

version\_string()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.version_string "Link to this definition")

Returns the server software’s version string. This is a combination of the [`server_version`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.server_version "http.server.BaseHTTPRequestHandler.server_version")
 and [`sys_version`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.sys_version "http.server.BaseHTTPRequestHandler.sys_version")
 attributes.

date\_time\_string(_timestamp\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.date_time_string "Link to this definition")

Returns the date and time given by _timestamp_ (which must be `None` or in the format returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
), formatted for a message header. If _timestamp_ is omitted, it uses the current date and time.

The result looks like `'Sun, 06 Nov 1994 08:49:37 GMT'`.

log\_date\_time\_string()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.log_date_time_string "Link to this definition")

Returns the current date and time, formatted for logging.

address\_string()[¶](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.address_string "Link to this definition")

Returns the client address.

Changed in version 3.3: Previously, a name lookup was performed. To avoid name resolution delays, it now always returns the IP address.

class http.server.SimpleHTTPRequestHandler(_request_, _client\_address_, _server_, _\*_, _directory\=None_, _extra\_response\_headers\=None_)[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler "Link to this definition")

This class serves files from the directory _directory_ and below, or the current directory if _directory_ is not provided, directly mapping the directory structure to HTTP requests.

Changed in version 3.7: Added the _directory_ parameter.

Changed in version 3.9: The _directory_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.15: Added _extra\_response\_headers_ parameter.

A lot of the work, such as parsing the request, is done by the base class [`BaseHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler "http.server.BaseHTTPRequestHandler")
. This class implements the [`do_GET()`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET "http.server.SimpleHTTPRequestHandler.do_GET")
 and [`do_HEAD()`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_HEAD "http.server.SimpleHTTPRequestHandler.do_HEAD")
 functions.

The following are defined as class-level attributes of `SimpleHTTPRequestHandler`:

server\_version[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.server_version "Link to this definition")

This will be `"SimpleHTTP/" + __version__`, where `__version__` is defined at the module level.

default\_content\_type[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.default_content_type "Link to this definition")

Specifies the Content-Type header value sent when the MIME type cannot be guessed from the file extension of the requested URL. By default, it is set to `'application/octet-stream'`.

Added in version 3.15.

index\_pages[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.index_pages "Link to this definition")

Specifies the filenames that are treated as directory index pages.

Defaults to `("index.html", "index.htm")`.

Added in version 3.12.

extensions\_map[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.extensions_map "Link to this definition")

A dictionary mapping suffixes into MIME types, contains custom overrides for the default system mappings. The mapping is used case-insensitively, and so should contain only lower-cased keys.

Changed in version 3.9: This dictionary is no longer filled with the default system mappings, but only contains overrides.

extra\_response\_headers[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.extra_response_headers "Link to this definition")

A sequence of `(name, value)` pairs containing user-defined extra HTTP response headers to add to each successful HTTP status 200 response. These headers are not included in other status code responses.

Headers that the server sends automatically such as `Content-Type` will not be overwritten by `extra_response_headers`.

The `SimpleHTTPRequestHandler` class defines the following methods:

do\_HEAD()[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_HEAD "Link to this definition")

This method serves the `'HEAD'` request type: it sends the headers it would send for the equivalent `GET` request. See the [`do_GET()`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET "http.server.SimpleHTTPRequestHandler.do_GET")
 method for a more complete explanation of the possible headers.

do\_GET()[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET "Link to this definition")

The request is mapped to a local file by interpreting the request as a path relative to the current working directory.

If the request was mapped to a directory, the directory is checked for an index page as specified by [`index_pages`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.index_pages "http.server.SimpleHTTPRequestHandler.index_pages")
. If found, the file’s contents are returned; otherwise a directory listing is generated by calling the [`list_directory()`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.list_directory "http.server.SimpleHTTPRequestHandler.list_directory")
 method. This method uses [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir")
 to scan the directory, and returns a `404` error response if the `listdir()` fails.

If the request was mapped to a file, it is opened. Any [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception in opening the requested file is mapped to a `404`, `'File not found'` error. If there was an `'If-Modified-Since'` header in the request, and the file was not modified after this time, a `304`, `'Not Modified'` response is sent. Otherwise, the content type is guessed by calling the [`guess_type()`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.guess_type "http.server.SimpleHTTPRequestHandler.guess_type")
 method, which in turn uses the _extensions\_map_ variable, and the file contents are returned.

A `'Content-type:'` header with the guessed content type is output, followed by a `'Content-Length:'` header with the file’s size and a `'Last-Modified:'` header with the file’s modification time.

The instance attribute [`extra_response_headers`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.extra_response_headers "http.server.SimpleHTTPRequestHandler.extra_response_headers")
 is a sequence of `(name, value)` pairs containing user-defined extra response headers.

Then follows a blank line signifying the end of the headers, and then the contents of the file are output.

For example usage, see the implementation of the `test` function in [Lib/http/server.py](https://github.com/python/cpython/tree/3.15/Lib/http/server.py)
.

Changed in version 3.7: Support of the `'If-Modified-Since'` header.

list\_directory(_path_)[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.list_directory "Link to this definition")

Helper to list the contents of _path_ when no index page is present.

This returns either a [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object)
 (which must be closed by the caller) or `None` to indicate an error, in which case the caller has nothing further to do. In either case, the headers are sent.

guess\_type(_path_)[¶](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.guess_type "Link to this definition")

Guess the type of the file at the given _path_.

This returns a string of the form `type/subtype`, usable for a MIME Content-type header.

The default implementation looks the file’s extension up in [`extensions_map`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.extensions_map "http.server.SimpleHTTPRequestHandler.extensions_map")
, falling back to [`mimetypes.guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type")
 and then to [`default_content_type`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.default_content_type "http.server.SimpleHTTPRequestHandler.default_content_type")
.

Changed in version 3.13: Add [`mimetypes.guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type")
 as a fallback.

The [`SimpleHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler "http.server.SimpleHTTPRequestHandler")
 class can be used to create a very basic webserver serving files relative to the current directory as follows:

Copy

import http.server
import socketserver

PORT \= 8000

Handler \= http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve\_forever()

[`SimpleHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler "http.server.SimpleHTTPRequestHandler")
 can also be subclassed to enhance behavior, such as using different index file names by overriding the class attribute [`index_pages`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.index_pages "http.server.SimpleHTTPRequestHandler.index_pages")
.

Command-line interface[¶](https://docs.python.org/3/library/http.server.html#command-line-interface "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

`http.server` can also be invoked directly using the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
 switch of the interpreter. The following example illustrates how to serve files relative to the current directory:

Copy

python \-m http.server \[OPTIONS\] \[port\]

The following options are accepted:

port[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-arg-port "Link to this definition")

The server listens to port 8000 by default. The default can be overridden by passing the desired port number as an argument:

Copy

python \-m http.server 9000

\-b, \--bind <address>[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-b "Link to this definition")

Specifies a specific address to which it should bind. Both IPv4 and IPv6 addresses are supported. By default, the server binds itself to all interfaces. For example, the following command causes the server to bind to localhost only:

Copy

python \-m http.server \--bind 127.0.0.1

Added in version 3.4.

Changed in version 3.8: Support IPv6 in the `--bind` option.

\-d, \--directory <dir>[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-d "Link to this definition")

Specifies a directory to which it should serve the files. By default, the server uses the current directory. For example, the following command uses a specific directory:

Copy

python \-m http.server \--directory /tmp/

Added in version 3.7.

\-p, \--protocol <version>[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-p "Link to this definition")

Specifies the HTTP version to which the server is conformant. By default, the server is conformant to HTTP/1.0. For example, the following command runs an HTTP/1.1 conformant server:

Copy

python \-m http.server \--protocol HTTP/1.1

Added in version 3.11.

\--content-type <content\_type>[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-content-type "Link to this definition")

Specifies the default Content-Type HTTP header used when the MIME type cannot be guessed from the URL’s file extension. By default, the server uses `'application/octet-stream'`:

Copy

python \-m http.server \--content-type text/html

Added in version 3.15.

\--tls-cert[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-tls-cert "Link to this definition")

Specifies a TLS certificate chain for HTTPS connections:

Copy

python \-m http.server \--tls-cert fullchain.pem

Added in version 3.14.

\--tls-key[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-tls-key "Link to this definition")

Specifies a private key file for HTTPS connections.

This option requires `--tls-cert` to be specified.

Added in version 3.14.

\--tls-password-file[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-tls-password-file "Link to this definition")

Specifies the password file for password-protected private keys:

Copy

python \-m http.server \\
       \--tls-cert cert.pem \\
       \--tls-key key.pem \\
       \--tls-password-file password.txt

This option requires `--tls-cert` to be specified.

Added in version 3.14.

\-H, \--header <header> <value>[¶](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-H "Link to this definition")

Specify an additional HTTP Response Header to send on successful HTTP 200 responses. Can be used multiple times to send additional custom response headers. Headers that are sent automatically by the server (for instance Content-Type) will not be overwritten by the server.

Added in version 3.15.

Security considerations[¶](https://docs.python.org/3/library/http.server.html#security-considerations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

[`SimpleHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler "http.server.SimpleHTTPRequestHandler")
 will follow symbolic links when handling requests which makes it possible for files outside of the specified directory to be served.

Methods [`BaseHTTPRequestHandler.send_header()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_header "http.server.BaseHTTPRequestHandler.send_header")
 and [`BaseHTTPRequestHandler.send_response_only()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_response_only "http.server.BaseHTTPRequestHandler.send_response_only")
 assume sanitized input and do not perform input validation such as checking for the presence of CRLF sequences. Untrusted input may result in HTTP header injection attacks.

Earlier versions of Python did not scrub control characters from the log messages emitted to stderr from `python -m http.server` or the default [`BaseHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler "http.server.BaseHTTPRequestHandler")
 `.log_message` implementation. This could allow remote clients connecting to your server to send nefarious control codes to your terminal.

Changed in version 3.12: Control characters are scrubbed in stderr logs.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html#)
    *   [Command-line interface](https://docs.python.org/3/library/http.server.html#command-line-interface)
        
    *   [Security considerations](https://docs.python.org/3/library/http.server.html#security-considerations)
        

#### Previous topic

[`socketserver` — A framework for network servers](https://docs.python.org/3/library/socketserver.html "previous chapter")

#### Next topic

[`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.server+%E2%80%94+HTTP+servers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.server.html&pagesource=library%2Fhttp.server.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/http.server.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/http.cookies.html "http.cookies — HTTP state management")
     |
*   [previous](https://docs.python.org/3/library/socketserver.html "socketserver — A framework for network servers")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
     »
*   [`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html)
    
*    
    
    |
*   Theme Auto Light Dark |