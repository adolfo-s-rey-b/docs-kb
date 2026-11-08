### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/poplib.html "poplib — POP3 protocol client")
     |
*   [previous](https://docs.python.org/3/library/http.client.html "http.client — HTTP protocol client")
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
*   [`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`ftplib` — FTP protocol client[¶](https://docs.python.org/3/library/ftplib.html#module-ftplib "Link to this heading")

======================================================================================================================

**Source code:** [Lib/ftplib.py](https://github.com/python/cpython/tree/3.15/Lib/ftplib.py)

* * *

This module defines the class [`FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
 and a few related items. The `FTP` class implements the client side of the FTP protocol. You can use this to write Python programs that perform a variety of automated FTP jobs, such as mirroring other FTP servers. It is also used by the module [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
 to handle URLs that use FTP. For more information on FTP (File Transfer Protocol), see internet [**RFC 959**](https://datatracker.ietf.org/doc/html/rfc959.html)
.

The default encoding is UTF-8, following [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Here’s a sample session using the `ftplib` module:

Copy

\>>> from ftplib import FTP
\>>> ftp \= FTP('ftp.us.debian.org')  \# connect to host, default port
\>>> ftp.login()                     \# user anonymous, passwd anonymous@
'230 Login successful.'
\>>> ftp.cwd('debian')               \# change into "debian" directory
'250 Directory successfully changed.'
\>>> ftp.retrlines('LIST')           \# list directory contents
\-rw-rw-r--    1 1176     1176         1063 Jun 15 10:18 README
...
drwxr-sr-x    5 1176     1176         4096 Dec 19  2000 pool
drwxr-sr-x    4 1176     1176         4096 Nov 17  2008 project
drwxr-xr-x    3 1176     1176         4096 Oct 10  2012 tools
'226 Directory send OK.'
\>>> with open('README', 'wb') as fp:
...     ftp.retrbinary('RETR README', fp.write)
'226 Transfer complete.'
\>>> ftp.quit()
'221 Goodbye.'

Reference[¶](https://docs.python.org/3/library/ftplib.html#reference "Link to this heading")

---------------------------------------------------------------------------------------------

### FTP objects[¶](https://docs.python.org/3/library/ftplib.html#ftp-objects "Link to this heading")

class ftplib.FTP(_host\=''_, _user\=''_, _passwd\=''_, _acct\=''_, _timeout\=None_, _source\_address\=None_, _\*_, _encoding\='utf-8'_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "Link to this definition")

Return a new instance of the `FTP` class.

Parameters:

*   **host** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The hostname to connect to. If given, `connect(host)` is implicitly called by the constructor.
    
*   **user** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The username to log in with (default: `'anonymous'`). If given, `login(user, passwd, acct)` is implicitly called by the constructor.
    
*   **passwd** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The password to use when logging in. If not given, and if _passwd_ is the empty string or `"-"`, a password will be automatically generated.
    
*   **acct** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – Account information to be used for the `ACCT` FTP command. Few systems implement this. See [RFC-959](https://datatracker.ietf.org/doc/html/rfc959.html)
     for more details.
    
*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "float")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – A timeout in seconds for blocking operations like [`connect()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.connect "ftplib.FTP.connect")
     (default: the global default timeout setting).
    
*   **source\_address** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – A 2-tuple `(host, port)` for the socket to bind to as its source address before connecting.
    
*   **encoding** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The encoding for directories and filenames (default: `'utf-8'`).
    

The `FTP` class supports the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, e.g.:

Copy

\>>> from ftplib import FTP
\>>> with FTP("ftp1.at.proftpd.org") as ftp:
...     ftp.login()
...     ftp.dir()
...
'230 Anonymous login ok, restrictions apply.'
dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 .
dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 ..
dr-xr-xr-x   5 ftp      ftp          4096 May  6 10:43 CentOS
dr-xr-xr-x   3 ftp      ftp            18 Jul 10  2008 Fedora
\>>>

Changed in version 3.2: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement was added.

Changed in version 3.3: _source\_address_ parameter was added.

Changed in version 3.9: If the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 to prevent the creation of a non-blocking socket. The _encoding_ parameter was added, and the default was changed from Latin-1 to UTF-8 to follow [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html)
.

Several `FTP` methods are available in two flavors: one for handling text files and another for binary files. The methods are named for the command which is used followed by `lines` for the text version or `binary` for the binary version.

`FTP` instances have the following methods:

set\_debuglevel(_level_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.set_debuglevel "Link to this definition")

Set the instance’s debugging level as an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. This controls the amount of debugging output printed. The debug levels are:

*   `0` (default): No debug output.
    
*   `1`: Produce a moderate amount of debug output, generally a single line per request.
    
*   `2` or higher: Produce the maximum amount of debugging output, logging each line sent and received on the control connection.
    

connect(_host\=''_, _port\=0_, _timeout\=None_, _source\_address\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.connect "Link to this definition")

Connect to the given host and port. This function should be called only once for each instance; it should not be called if a _host_ argument was given when the `FTP` instance was created. All other `FTP` methods can only be called after a connection has successfully been made.

Parameters:

*   **host** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The host to connect to.
    
*   **port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "int")
    ) – The TCP port to connect to (default: `21`, as specified by the FTP protocol specification). It is rarely needed to specify a different port number.
    
*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "float")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – A timeout in seconds for the connection attempt (default: the global default timeout setting).
    
*   **source\_address** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – A 2-tuple `(host, port)` for the socket to bind to as its source address before connecting.
    

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ftplib.connect` with arguments `self`, `host`, `port`.

Changed in version 3.3: _source\_address_ parameter was added.

getwelcome()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.getwelcome "Link to this definition")

Return the welcome message sent by the server in reply to the initial connection. (This message sometimes contains disclaimers or help information that may be relevant to the user.)

login(_user\='anonymous'_, _passwd\=''_, _acct\=''_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.login "Link to this definition")

Log on to the connected FTP server. This function should be called only once for each instance, after a connection has been established; it should not be called if the _host_ and _user_ arguments were given when the `FTP` instance was created. Most FTP commands are only allowed after the client has logged in.

Parameters:

*   **user** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The username to log in with (default: `'anonymous'`).
    
*   **passwd** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The password to use when logging in. If not given, and if _passwd_ is the empty string or `"-"`, a password will be automatically generated.
    
*   **acct** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – Account information to be used for the `ACCT` FTP command. Few systems implement this. See [RFC-959](https://datatracker.ietf.org/doc/html/rfc959.html)
     for more details.
    

abort()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.abort "Link to this definition")

Abort a file transfer that is in progress. Using this does not always work, but it’s worth a try.

sendcmd(_cmd_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.sendcmd "Link to this definition")

Send a simple command string to the server and return the response string.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ftplib.sendcmd` with arguments `self`, `cmd`.

voidcmd(_cmd_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.voidcmd "Link to this definition")

Send a simple command string to the server and handle the response. Return the response string if the response code corresponds to success (codes in the range 200–299). Raise [`error_reply`](https://docs.python.org/3/library/ftplib.html#ftplib.error_reply "ftplib.error_reply")
 otherwise.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ftplib.sendcmd` with arguments `self`, `cmd`.

retrbinary(_cmd_, _callback_, _blocksize\=8192_, _rest\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.retrbinary "Link to this definition")

Retrieve a file in binary transfer mode.

Parameters:

*   **cmd** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – An appropriate `RETR` command: `"RETR _filename_"`.
    
*   **callback** ([callable](https://docs.python.org/3/glossary.html#term-callable)
    ) – A single parameter callable that is called for each block of data received, with its single argument being the data as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   **blocksize** ([_int_](https://docs.python.org/3/builtins/functions.html#int "int")
    ) – The maximum chunk size to read on the low-level [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     object created to do the actual transfer. This also corresponds to the largest size of data that will be passed to _callback_. Defaults to `8192`.
    
*   **rest** ([_int_](https://docs.python.org/3/builtins/functions.html#int "int")
    ) – A `REST` command to be sent to the server. See the documentation for the _rest_ parameter of the [`transfercmd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.transfercmd "ftplib.FTP.transfercmd")
     method.
    

retrlines(_cmd_, _callback\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.retrlines "Link to this definition")

Retrieve a file or directory listing in the encoding specified by the _encoding_ parameter at initialization. _cmd_ should be an appropriate `RETR` command (see [`retrbinary()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.retrbinary "ftplib.FTP.retrbinary")
) or a command such as `LIST` or `NLST` (usually just the string `'LIST'`). `LIST` retrieves a list of files and information about those files. `NLST` retrieves a list of file names. The _callback_ function is called for each line with a string argument containing the line with the trailing CRLF stripped. The default _callback_ prints the line to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
.

set\_pasv(_val_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.set_pasv "Link to this definition")

Enable “passive” mode if _val_ is true, otherwise disable passive mode. Passive mode is on by default.

storbinary(_cmd_, _fp_, _blocksize\=8192_, _callback\=None_, _rest\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.storbinary "Link to this definition")

Store a file in binary transfer mode.

Parameters:

*   **cmd** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – An appropriate `STOR` command: `"STOR _filename_"`.
    
*   **fp** ([file object](https://docs.python.org/3/glossary.html#term-file-object)
    ) – A file object (opened in binary mode) which is read until EOF, using its [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read")
     method in blocks of size _blocksize_ to provide the data to be stored.
    
*   **blocksize** ([_int_](https://docs.python.org/3/builtins/functions.html#int "int")
    ) – The read block size. Defaults to `8192`.
    
*   **callback** ([callable](https://docs.python.org/3/glossary.html#term-callable)
    ) – A single parameter callable that is called for each block of data sent, with its single argument being the data as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   **rest** ([_int_](https://docs.python.org/3/builtins/functions.html#int "int")
    ) – A `REST` command to be sent to the server. See the documentation for the _rest_ parameter of the [`transfercmd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.transfercmd "ftplib.FTP.transfercmd")
     method.
    

Changed in version 3.2: The _rest_ parameter was added.

storlines(_cmd_, _fp_, _callback\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.storlines "Link to this definition")

Store a file in line mode. _cmd_ should be an appropriate `STOR` command (see [`storbinary()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.storbinary "ftplib.FTP.storbinary")
). Lines are read until EOF from the [file object](https://docs.python.org/3/glossary.html#term-file-object)
 _fp_ (opened in binary mode) using its [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")
 method to provide the data to be stored. _callback_ is an optional single parameter callable that is called on each line after it is sent.

transfercmd(_cmd_, _rest\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.transfercmd "Link to this definition")

Initiate a transfer over the data connection. If the transfer is active, send an `EPRT` or `PORT` command and the transfer command specified by _cmd_, and accept the connection. If the server is passive, send an `EPSV` or `PASV` command, connect to it, and start the transfer command. Either way, return the socket for the connection.

If optional _rest_ is given, a `REST` command is sent to the server, passing _rest_ as an argument. _rest_ is usually a byte offset into the requested file, telling the server to restart sending the file’s bytes at the requested offset, skipping over the initial bytes. Note however that the `transfercmd()` method converts _rest_ to a string with the _encoding_ parameter specified at initialization, but no check is performed on the string’s contents. If the server does not recognize the `REST` command, an [`error_reply`](https://docs.python.org/3/library/ftplib.html#ftplib.error_reply "ftplib.error_reply")
 exception will be raised. If this happens, simply call `transfercmd()` without a _rest_ argument.

ntransfercmd(_cmd_, _rest\=None_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.ntransfercmd "Link to this definition")

Like [`transfercmd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.transfercmd "ftplib.FTP.transfercmd")
, but returns a tuple of the data connection and the expected size of the data. If the expected size could not be computed, `None` will be returned as the expected size. _cmd_ and _rest_ means the same thing as in `transfercmd()`.

mlsd(_path\=''_, _facts\=\[\]_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mlsd "Link to this definition")

List a directory in a standardized format by using `MLSD` command ([**RFC 3659**](https://datatracker.ietf.org/doc/html/rfc3659.html)
). If _path_ is omitted the current directory is assumed. _facts_ is a list of strings representing the type of information desired (e.g. `["type", "size", "perm"]`). Return a generator object yielding a tuple of two elements for every file found in path. First element is the file name, the second one is a dictionary containing facts about the file name. Content of this dictionary might be limited by the _facts_ argument but server is not guaranteed to return all requested facts.

Added in version 3.3.

nlst(_argument_\[, _..._\])[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.nlst "Link to this definition")

Return a list of file names as returned by the `NLST` command. The optional _argument_ is a directory to list (default is the current server directory). Multiple arguments can be used to pass non-standard options to the `NLST` command.

Note

If your server supports the command, [`mlsd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mlsd "ftplib.FTP.mlsd")
 offers a better API.

dir(_argument_\[, _..._\])[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.dir "Link to this definition")

Produce a directory listing as returned by the `LIST` command, printing it to standard output. The optional _argument_ is a directory to list (default is the current server directory). Multiple arguments can be used to pass non-standard options to the `LIST` command. If the last argument is a function, it is used as a _callback_ function as for [`retrlines()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.retrlines "ftplib.FTP.retrlines")
; the default prints to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
. This method returns `None`.

Note

If your server supports the command, [`mlsd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mlsd "ftplib.FTP.mlsd")
 offers a better API.

rename(_fromname_, _toname_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.rename "Link to this definition")

Rename file _fromname_ on the server to _toname_.

delete(_filename_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.delete "Link to this definition")

Remove the file named _filename_ from the server. If successful, returns the text of the response, otherwise raises [`error_perm`](https://docs.python.org/3/library/ftplib.html#ftplib.error_perm "ftplib.error_perm")
 on permission errors or [`error_reply`](https://docs.python.org/3/library/ftplib.html#ftplib.error_reply "ftplib.error_reply")
 on other errors.

cwd(_pathname_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.cwd "Link to this definition")

Set the current directory on the server.

mkd(_pathname_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mkd "Link to this definition")

Create a new directory on the server.

pwd()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.pwd "Link to this definition")

Return the pathname of the current directory on the server.

rmd(_dirname_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.rmd "Link to this definition")

Remove the directory named _dirname_ on the server.

size(_filename_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.size "Link to this definition")

Request the size of the file named _filename_ on the server. On success, the size of the file is returned as an integer, otherwise `None` is returned. Note that the `SIZE` command is not standardized, but is supported by many common server implementations.

quit()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.quit "Link to this definition")

Send a `QUIT` command to the server and close the connection. This is the “polite” way to close a connection, but it may raise an exception if the server responds with an error to the `QUIT` command. This implies a call to the [`close()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.close "ftplib.FTP.close")
 method which renders the `FTP` instance useless for subsequent calls (see below).

close()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.close "Link to this definition")

Close the connection unilaterally. This should not be applied to an already closed connection such as after a successful call to [`quit()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.quit "ftplib.FTP.quit")
. After this call the `FTP` instance should not be used any more (after a call to `close()` or `quit()` you cannot reopen the connection by issuing another [`login()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.login "ftplib.FTP.login")
 method).

### FTP\_TLS objects[¶](https://docs.python.org/3/library/ftplib.html#ftp-tls-objects "Link to this heading")

class ftplib.FTP\_TLS(_host\=''_, _user\=''_, _passwd\=''_, _acct\=''_, _\*_, _context\=None_, _timeout\=None_, _source\_address\=None_, _encoding\='utf-8'_)[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS "Link to this definition")

An [`FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
 subclass which adds TLS support to FTP as described in [**RFC 4217**](https://datatracker.ietf.org/doc/html/rfc4217.html)
. Connect to port 21 implicitly securing the FTP control connection before authenticating.

Note

The user must explicitly secure the data connection by calling the [`prot_p()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS.prot_p "ftplib.FTP_TLS.prot_p")
 method.

Parameters:

*   **host** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The hostname to connect to. If given, `connect(host)` is implicitly called by the constructor.
    
*   **user** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The username to log in with (default: `'anonymous'`). If given, `login(user, passwd, acct)` is implicitly called by the constructor.
    
*   **passwd** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The password to use when logging in. If not given, and if _passwd_ is the empty string or `"-"`, a password will be automatically generated.
    
*   **acct** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – Account information to be used for the `ACCT` FTP command. Few systems implement this. See [RFC-959](https://datatracker.ietf.org/doc/html/rfc959.html)
     for more details.
    
*   **context** ([`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
    ) – An SSL context object which allows bundling SSL configuration options, certificates and private keys into a single, potentially long-lived, structure. Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security)
     for best practices.
    
*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "float")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – A timeout in seconds for blocking operations like [`connect()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.connect "ftplib.FTP.connect")
     (default: the global default timeout setting).
    
*   **source\_address** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – A 2-tuple `(host, port)` for the socket to bind to as its source address before connecting.
    
*   **encoding** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ) – The encoding for directories and filenames (default: `'utf-8'`).
    

Added in version 3.2.

Changed in version 3.3: Added the _source\_address_ parameter.

Changed in version 3.4: The class now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname")
 and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")
).

Changed in version 3.9: If the _timeout_ parameter is set to be zero, it will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 to prevent the creation of a non-blocking socket. The _encoding_ parameter was added, and the default was changed from Latin-1 to UTF-8 to follow [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html)
.

Changed in version 3.12: The deprecated _keyfile_ and _certfile_ parameters have been removed.

Here’s a sample session using the `FTP_TLS` class:

Copy

\>>> ftps \= FTP\_TLS('ftp.pureftpd.org')
\>>> ftps.login()
'230 Anonymous user logged in'
\>>> ftps.prot\_p()
'200 Data protection level set to "private"'
\>>> ftps.nlst()
\['6jack', 'OpenBSD', 'antilink', 'blogbench', 'bsdcam', 'clockspeed', 'djbdns-jedi', 'docs', 'eaccelerator-jedi', 'favicon.ico', 'francotone', 'fugu', 'ignore', 'libpuzzle', 'metalog', 'minidentd', 'misc', 'mysql-udf-global-user-variables', 'php-jenkins-hash', 'php-skein-hash', 'php-webdav', 'phpaudit', 'phpbench', 'pincaster', 'ping', 'posto', 'pub', 'public', 'public\_keys', 'pure-ftpd', 'qscan', 'qtc', 'sharedance', 'skycache', 'sound', 'tmp', 'ucarp'\]

`FTP_TLS` class inherits from [`FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
, defining these additional methods and attributes:

auth()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS.auth "Link to this definition")

Set up a secure control connection by using TLS.

Changed in version 3.4: The method now supports hostname check with [`ssl.SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname")
 and _Server Name Indication_ (see [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI")
).

ccc()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS.ccc "Link to this definition")

Revert control channel back to plaintext. This can be useful to take advantage of firewalls that know how to handle NAT with non-secure FTP without opening fixed ports.

Added in version 3.3.

prot\_p()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS.prot_p "Link to this definition")

Set up secure data connection by using TLS.

prot\_c()[¶](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS.prot_c "Link to this definition")

Set up clear text data connection.

### Module variables[¶](https://docs.python.org/3/library/ftplib.html#module-variables "Link to this heading")

exception ftplib.error\_reply[¶](https://docs.python.org/3/library/ftplib.html#ftplib.error_reply "Link to this definition")

Exception raised when an unexpected reply is received from the server.

exception ftplib.error\_temp[¶](https://docs.python.org/3/library/ftplib.html#ftplib.error_temp "Link to this definition")

Exception raised when an error code signifying a temporary error (response codes in the range 400–499) is received.

exception ftplib.error\_perm[¶](https://docs.python.org/3/library/ftplib.html#ftplib.error_perm "Link to this definition")

Exception raised when an error code signifying a permanent error (response codes in the range 500–599) is received.

exception ftplib.error\_proto[¶](https://docs.python.org/3/library/ftplib.html#ftplib.error_proto "Link to this definition")

Exception raised when a reply is received from the server that does not fit the response specifications of the File Transfer Protocol, i.e. begin with a digit in the range 1–5.

ftplib.all\_errors[¶](https://docs.python.org/3/library/ftplib.html#ftplib.all_errors "Link to this definition")

The set of all exceptions (as a tuple) that methods of [`FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
 instances may raise as a result of problems with the FTP connection (as opposed to programming errors made by the caller). This set includes the four exceptions listed above as well as [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 and [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
.

See also

Module [`netrc`](https://docs.python.org/3/library/netrc.html#module-netrc "netrc: Loading of .netrc files.")

Parser for the `.netrc` file format. The file `.netrc` is typically used by FTP clients to load user authentication information before prompting the user.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html#)
    *   [Reference](https://docs.python.org/3/library/ftplib.html#reference)
        *   [FTP objects](https://docs.python.org/3/library/ftplib.html#ftp-objects)
            
        *   [FTP\_TLS objects](https://docs.python.org/3/library/ftplib.html#ftp-tls-objects)
            
        *   [Module variables](https://docs.python.org/3/library/ftplib.html#module-variables)
            

#### Previous topic

[`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html "previous chapter")

#### Next topic

[`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ftplib+%E2%80%94+FTP+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fftplib.html&pagesource=library%2Fftplib.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/ftplib.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/poplib.html "poplib — POP3 protocol client")
     |
*   [previous](https://docs.python.org/3/library/http.client.html "http.client — HTTP protocol client")
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
*   [`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html)
    
*    
    
    |
*   Theme Auto Light Dark |