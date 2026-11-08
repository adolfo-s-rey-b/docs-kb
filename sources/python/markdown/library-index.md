### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/intro.html "Introduction")
     |
*   [previous](https://docs.python.org/3/builtins/time-complexity.html "Time complexity of operations on built-in types")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |

The Python standard library[¶](https://docs.python.org/3/library/index.html#the-python-standard-library "Link to this heading")

================================================================================================================================

This library reference manual describes the standard library distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.

Elsewhere, [The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)
 describes the exact syntax and semantics of the Python language, and [Python built-ins reference](https://docs.python.org/3/builtins/index.html#builtins-index)
 describes the built-in functions.

Python’s standard library is extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.

In addition to the standard library, there is an active collection of hundreds of thousands of components (from individual programs and modules to packages and entire application development frameworks), available from the [Python Package Index](https://pypi.org/)
.

*   [Introduction](https://docs.python.org/3/library/intro.html)
    *   [Notes on availability](https://docs.python.org/3/library/intro.html#notes-on-availability)
        
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
    *   [`string` — Common string operations](https://docs.python.org/3/library/string.html)
        
    *   [`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html)
        
    *   [`re` — Regular expression operations](https://docs.python.org/3/library/re.html)
        
    *   [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
        
    *   [`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html)
        
    *   [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
        
    *   [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
        
    *   [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
        
    *   [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)
        
*   [Binary Data Services](https://docs.python.org/3/library/binary.html)
    *   [`struct` — Interpret bytes as packed binary data](https://docs.python.org/3/library/struct.html)
        
    *   [`codecs` — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)
        
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
    *   [`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html)
        
    *   [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
        
    *   [`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html)
        
    *   [`collections` — Container datatypes](https://docs.python.org/3/library/collections.html)
        
    *   [`collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)
        
    *   [`heapq` — Heap queue algorithm](https://docs.python.org/3/library/heapq.html)
        
    *   [`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html)
        
    *   [`array` — Efficient arrays of numeric values](https://docs.python.org/3/library/array.html)
        
    *   [`weakref` — Weak references](https://docs.python.org/3/library/weakref.html)
        
    *   [`types` — Dynamic type creation and names for built-in types](https://docs.python.org/3/library/types.html)
        
    *   [`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)
        
    *   [`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html)
        
    *   [`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html)
        
    *   [`enum` — Support for enumerations](https://docs.python.org/3/library/enum.html)
        
    *   [`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html)
        
*   [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)
    *   [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
        
    *   [`math` — Mathematical functions](https://docs.python.org/3/library/math.html)
        
    *   [`math.integer` — integer-specific mathematics functions](https://docs.python.org/3/library/math.integer.html)
        
    *   [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
        
    *   [`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html)
        
    *   [`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html)
        
    *   [`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
        
    *   [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
        
*   [Functional Programming Modules](https://docs.python.org/3/library/functional.html)
    *   [`itertools` — Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)
        
    *   [`functools` — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html)
        
    *   [`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html)
        
*   [File and Directory Access](https://docs.python.org/3/library/filesys.html)
    *   [`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
        
    *   [`os.path` — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)
        
    *   [`stat` — Interpreting `stat()` results](https://docs.python.org/3/library/stat.html)
        
    *   [`filecmp` — File and Directory Comparisons](https://docs.python.org/3/library/filecmp.html)
        
    *   [`tempfile` — Generate temporary files and directories](https://docs.python.org/3/library/tempfile.html)
        
    *   [`glob` — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
        
    *   [`fnmatch` — Unix filename pattern matching](https://docs.python.org/3/library/fnmatch.html)
        
    *   [`linecache` — Random access to text lines](https://docs.python.org/3/library/linecache.html)
        
    *   [`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html)
        
*   [Data Persistence](https://docs.python.org/3/library/persistence.html)
    *   [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
        
    *   [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
        
    *   [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
        
    *   [`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html)
        
    *   [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
        
    *   [`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)
        
*   [Data Compression and Archiving](https://docs.python.org/3/library/archiving.html)
    *   [The `compression` package](https://docs.python.org/3/library/compression.html)
        
    *   [`compression.zstd` — Compression compatible with the Zstandard format](https://docs.python.org/3/library/compression.zstd.html)
        
    *   [`zlib` — Compression compatible with **gzip**](https://docs.python.org/3/library/zlib.html)
        
    *   [`gzip` — Support for **gzip** files](https://docs.python.org/3/library/gzip.html)
        
    *   [`bz2` — Support for **bzip2** compression](https://docs.python.org/3/library/bz2.html)
        
    *   [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/3/library/lzma.html)
        
    *   [`zipfile` — Work with ZIP archives](https://docs.python.org/3/library/zipfile.html)
        
    *   [`tarfile` — Read and write tar archive files](https://docs.python.org/3/library/tarfile.html)
        
*   [File Formats](https://docs.python.org/3/library/fileformats.html)
    *   [`csv` — CSV file reading and writing](https://docs.python.org/3/library/csv.html)
        
    *   [`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html)
        
    *   [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
        
    *   [`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html)
        
    *   [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html)
        
*   [Cryptographic Services](https://docs.python.org/3/library/crypto.html)
    *   [`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
        
    *   [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html)
        
    *   [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)
        
*   [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
    *   [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
        
    *   [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html)
        
    *   [`time` — Time access and conversions](https://docs.python.org/3/library/time.html)
        
    *   [`logging` — Logging facility for Python](https://docs.python.org/3/library/logging.html)
        
    *   [`logging.config` — Logging configuration](https://docs.python.org/3/library/logging.config.html)
        
    *   [`logging.handlers` — Logging handlers](https://docs.python.org/3/library/logging.handlers.html)
        
    *   [`platform` — Access to underlying platform’s identifying data](https://docs.python.org/3/library/platform.html)
        
    *   [`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html)
        
    *   [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
        
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
    *   [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
        
    *   [`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html)
        
    *   [`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html)
        
    *   [`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html)
        
    *   [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html)
        
    *   [`curses.textpad` — Text input widget for curses programs](https://docs.python.org/3/library/curses.html#module-curses.textpad)
        
    *   [`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html)
        
    *   [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
        
    *   [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)
        
*   [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
    *   [`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html)
        
    *   [`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)
        
    *   [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
        
    *   [The `concurrent` package](https://docs.python.org/3/library/concurrent.html)
        
    *   [`concurrent.futures` — Launching parallel tasks](https://docs.python.org/3/library/concurrent.futures.html)
        
    *   [`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html)
        
    *   [`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)
        
    *   [`sched` — Event scheduler](https://docs.python.org/3/library/sched.html)
        
    *   [`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html)
        
    *   [`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html)
        
    *   [`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html)
        
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
    *   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
        
    *   [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html)
        
    *   [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
        
    *   [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
        
    *   [`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html)
        
    *   [`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html)
        
    *   [`mmap` — Memory-mapped file support](https://docs.python.org/3/library/mmap.html)
        
*   [Internet Data Handling](https://docs.python.org/3/library/netdata.html)
    *   [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html)
        
    *   [`json` — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
        
    *   [`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/3/library/mailbox.html)
        
    *   [`mimetypes` — Map filenames to MIME types](https://docs.python.org/3/library/mimetypes.html)
        
    *   [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)
        
    *   [`binascii` — Convert between binary and ASCII](https://docs.python.org/3/library/binascii.html)
        
    *   [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/3/library/quopri.html)
        
*   [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html)
    *   [`html` — HyperText Markup Language support](https://docs.python.org/3/library/html.html)
        
    *   [`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/3/library/html.parser.html)
        
    *   [`html.entities` — Definitions of HTML general entities](https://docs.python.org/3/library/html.entities.html)
        
    *   [XML Processing Modules](https://docs.python.org/3/library/xml.html)
        
    *   [`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)
        
    *   [`xml.dom` — The Document Object Model API](https://docs.python.org/3/library/xml.dom.html)
        
    *   [`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/3/library/xml.dom.minidom.html)
        
    *   [`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/3/library/xml.dom.pulldom.html)
        
    *   [`xml.sax` — Support for SAX2 parsers](https://docs.python.org/3/library/xml.sax.html)
        
    *   [`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html)
        
    *   [`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/3/library/xml.sax.utils.html)
        
    *   [`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/3/library/xml.sax.reader.html)
        
    *   [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/3/library/pyexpat.html)
        
*   [Internet Protocols and Support](https://docs.python.org/3/library/internet.html)
    *   [`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html)
        
    *   [`wsgiref` — WSGI Utilities and Reference Implementation](https://docs.python.org/3/library/wsgiref.html)
        
    *   [`urllib` — URL handling modules](https://docs.python.org/3/library/urllib.html)
        
    *   [`urllib.request` — Extensible library for opening URLs](https://docs.python.org/3/library/urllib.request.html)
        
    *   [`urllib.response` — Response classes used by urllib](https://docs.python.org/3/library/urllib.request.html#module-urllib.response)
        
    *   [`urllib.parse` — Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html)
        
    *   [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/3/library/urllib.error.html)
        
    *   [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/3/library/urllib.robotparser.html)
        
    *   [`http` — HTTP modules](https://docs.python.org/3/library/http.html)
        
    *   [`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html)
        
    *   [`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html)
        
    *   [`poplib` — POP3 protocol client](https://docs.python.org/3/library/poplib.html)
        
    *   [`imaplib` — IMAP4 protocol client](https://docs.python.org/3/library/imaplib.html)
        
    *   [`smtplib` — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
        
    *   [`uuid` — UUID objects according to **RFC 9562**](https://docs.python.org/3/library/uuid.html)
        
    *   [`socketserver` — A framework for network servers](https://docs.python.org/3/library/socketserver.html)
        
    *   [`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html)
        
    *   [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
        
    *   [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html)
        
    *   [`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html)
        
    *   [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/3/library/xmlrpc.client.html)
        
    *   [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html)
        
    *   [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html)
        
*   [Multimedia Services](https://docs.python.org/3/library/mm.html)
    *   [`wave` — Read and write WAV files](https://docs.python.org/3/library/wave.html)
        
    *   [`colorsys` — Conversions between color systems](https://docs.python.org/3/library/colorsys.html)
        
*   [Internationalization](https://docs.python.org/3/library/i18n.html)
    *   [`gettext` — Multilingual internationalization services](https://docs.python.org/3/library/gettext.html)
        
    *   [`locale` — Internationalization services](https://docs.python.org/3/library/locale.html)
        
*   [Graphical user interfaces with Tk](https://docs.python.org/3/library/tk.html)
    *   [`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
        
    *   [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/3/library/tkinter.colorchooser.html)
        
    *   [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/3/library/tkinter.font.html)
        
    *   [Tkinter dialogs](https://docs.python.org/3/library/dialog.html)
        
    *   [`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/3/library/tkinter.messagebox.html)
        
    *   [`tkinter.scrolledtext` — Scrolled text widget](https://docs.python.org/3/library/tkinter.scrolledtext.html)
        
    *   [`tkinter.dnd` — Drag and drop support](https://docs.python.org/3/library/tkinter.dnd.html)
        
    *   [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/3/library/tkinter.ttk.html)
        
    *   [IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html)
        
    *   [`turtle` — Turtle graphics](https://docs.python.org/3/library/turtle.html)
        
*   [Development Tools](https://docs.python.org/3/library/development.html)
    *   [`typing` — Support for type hints](https://docs.python.org/3/library/typing.html)
        
    *   [`pydoc` — Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html)
        
    *   [Python Development Mode](https://docs.python.org/3/library/devmode.html)
        
    *   [`doctest` — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
        
    *   [`unittest` — Unit testing framework](https://docs.python.org/3/library/unittest.html)
        
    *   [`unittest.mock` — mock object library](https://docs.python.org/3/library/unittest.mock.html)
        
    *   [`unittest.mock` — getting started](https://docs.python.org/3/library/unittest.mock-examples.html)
        
    *   [`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html)
        
    *   [`test.support` — Utilities for the Python test suite](https://docs.python.org/3/library/test.html#module-test.support)
        
    *   [`test.support.socket_helper` — Utilities for socket tests](https://docs.python.org/3/library/test.html#module-test.support.socket_helper)
        
    *   [`test.support.script_helper` — Utilities for the Python execution tests](https://docs.python.org/3/library/test.html#module-test.support.script_helper)
        
    *   [`test.support.bytecode_helper` — Support tools for testing correct bytecode generation](https://docs.python.org/3/library/test.html#module-test.support.bytecode_helper)
        
    *   [`test.support.threading_helper` — Utilities for threading tests](https://docs.python.org/3/library/test.html#module-test.support.threading_helper)
        
    *   [`test.support.os_helper` — Utilities for os tests](https://docs.python.org/3/library/test.html#module-test.support.os_helper)
        
    *   [`test.support.import_helper` — Utilities for import tests](https://docs.python.org/3/library/test.html#module-test.support.import_helper)
        
    *   [`test.support.warnings_helper` — Utilities for warnings tests](https://docs.python.org/3/library/test.html#module-test.support.warnings_helper)
        
*   [Debugging and profiling](https://docs.python.org/3/library/debug.html)
    *   [Audit events table](https://docs.python.org/3/library/audit_events.html)
        
    *   [`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html)
        
    *   [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
        
    *   [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
        
    *   [`profiling` — Python profilers](https://docs.python.org/3/library/profiling.html)
        
    *   [`pstats` — Statistics for profilers](https://docs.python.org/3/library/pstats.html)
        
    *   [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
        
    *   [`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html)
        
    *   [`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html)
        
*   [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html)
    *   [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/3/library/ensurepip.html)
        
    *   [`venv` — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
        
    *   [`zipapp` — Manage executable Python zip archives](https://docs.python.org/3/library/zipapp.html)
        
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
    *   [`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
        
    *   [`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html)
        
    *   [`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html)
        
    *   [`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html)
        
    *   [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)
        
    *   [`warnings` — Warning control](https://docs.python.org/3/library/warnings.html)
        
    *   [`dataclasses` — Data Classes](https://docs.python.org/3/library/dataclasses.html)
        
    *   [`contextlib` — Utilities for `with`\-statement contexts](https://docs.python.org/3/library/contextlib.html)
        
    *   [`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
        
    *   [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
        
    *   [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html)
        
    *   [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
        
    *   [`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html)
        
    *   [`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html)
        
    *   [`annotationlib` — Functionality for introspecting annotations](https://docs.python.org/3/library/annotationlib.html)
        
    *   [`site` — Site-specific configuration hook](https://docs.python.org/3/library/site.html)
        
*   [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html)
    *   [`code` — Interpreter base classes](https://docs.python.org/3/library/code.html)
        
    *   [`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html)
        
*   [Importing Modules](https://docs.python.org/3/library/modules.html)
    *   [`zipimport` — Import modules from Zip archives](https://docs.python.org/3/library/zipimport.html)
        
    *   [`pkgutil` — Package extension utility](https://docs.python.org/3/library/pkgutil.html)
        
    *   [`modulefinder` — Find modules used by a script](https://docs.python.org/3/library/modulefinder.html)
        
    *   [`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html)
        
    *   [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
        
    *   [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html)
        
    *   [`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/3/library/importlib.resources.abc.html)
        
    *   [`importlib.metadata` – Accessing package metadata](https://docs.python.org/3/library/importlib.metadata.html)
        
    *   [The initialization of the `sys.path` module search path](https://docs.python.org/3/library/sys_path_init.html)
        
*   [Python Language Services](https://docs.python.org/3/library/language.html)
    *   [`ast` — Abstract syntax trees](https://docs.python.org/3/library/ast.html)
        
    *   [`symtable` — Access to the compiler’s symbol tables](https://docs.python.org/3/library/symtable.html)
        
    *   [`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html)
        
    *   [`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html)
        
    *   [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
        
    *   [`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html)
        
    *   [`pyclbr` — Python module browser support](https://docs.python.org/3/library/pyclbr.html)
        
    *   [`py_compile` — Compile Python source files](https://docs.python.org/3/library/py_compile.html)
        
    *   [`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html)
        
    *   [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
        
    *   [`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html)
        
*   [MS Windows Specific Services](https://docs.python.org/3/library/windows.html)
    *   [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html)
        
    *   [`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html)
        
    *   [`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html)
        
*   [Unix-specific services](https://docs.python.org/3/library/unix.html)
    *   [`shlex` — Simple lexical analysis](https://docs.python.org/3/library/shlex.html)
        
    *   [`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html)
        
    *   [`pwd` — The password database](https://docs.python.org/3/library/pwd.html)
        
    *   [`grp` — The group database](https://docs.python.org/3/library/grp.html)
        
    *   [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
        
    *   [`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html)
        
    *   [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
        
    *   [`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html)
        
    *   [`resource` — Resource usage information](https://docs.python.org/3/library/resource.html)
        
    *   [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
        
*   [Modules command-line interface (CLI)](https://docs.python.org/3/library/cmdline.html)
    
*   [Superseded modules](https://docs.python.org/3/library/superseded.html)
    *   [`getopt` — C-style parser for command line options](https://docs.python.org/3/library/getopt.html)
        
    *   [`profile` — Pure Python profiler](https://docs.python.org/3/library/profile.html)
        
*   [Removed Modules](https://docs.python.org/3/library/removed.html)
    
*   [Security Considerations](https://docs.python.org/3/library/security_warnings.html)
    

#### Previous topic

[Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html "previous chapter")

#### Next topic

[Introduction](https://docs.python.org/3/library/intro.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=The+Python+standard+library&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Findex.html&pagesource=library%2Findex.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/index.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/intro.html "Introduction")
     |
*   [previous](https://docs.python.org/3/builtins/time-complexity.html "Time complexity of operations on built-in types")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |