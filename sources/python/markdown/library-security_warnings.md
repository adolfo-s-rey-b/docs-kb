### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/index.html "Extending and Embedding the Python Interpreter")
     |
*   [previous](https://docs.python.org/3/library/xdrlib.html "xdrlib — Encode and decode XDR data")
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
*   [Security Considerations](https://docs.python.org/3/library/security_warnings.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Security Considerations[¶](https://docs.python.org/3/library/security_warnings.html#security-considerations "Link to this heading")

====================================================================================================================================

The following modules have specific security considerations:

*   [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
    : [base64 security considerations](https://docs.python.org/3/library/base64.html#base64-security)
     in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
    
*   [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
    : [all constructors take a “usedforsecurity” keyword-only argument disabling known insecure and blocked algorithms](https://docs.python.org/3/library/hashlib.html#hashlib-usedforsecurity)
    
*   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
     is not suitable for production use, only implementing basic security checks. See the [security considerations](https://docs.python.org/3/library/http.server.html#http-server-security)
    .
    
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
    : [Logging configuration uses eval()](https://docs.python.org/3/library/logging.config.html#logging-eval-security)
    
*   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
    : [Connection.recv() uses pickle](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-recv-pickle-security)
    
*   [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
    : [Restricting globals in pickle](https://docs.python.org/3/library/pickle.html#pickle-restrict)
    
*   [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
     shouldn’t be used for security purposes, use [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.")
     instead
    
*   [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")
    : [shelve is based on pickle and thus unsuitable for dealing with untrusted sources](https://docs.python.org/3/library/shelve.html#shelve-security)
    
*   [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
    : [SSL/TLS security considerations](https://docs.python.org/3/library/ssl.html#ssl-security)
    
*   [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
    : [Subprocess security considerations](https://docs.python.org/3/library/subprocess.html#subprocess-security)
    
*   [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories.")
    : [mktemp is deprecated due to vulnerability to race conditions](https://docs.python.org/3/library/tempfile.html#tempfile-mktemp-deprecated)
    
*   [`xml`](https://docs.python.org/3/library/xml.html#module-xml "xml: Package containing XML processing modules")
    : [XML security](https://docs.python.org/3/library/xml.html#xml-security)
    
*   [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
    : [maliciously prepared .zip files can cause disk volume exhaustion](https://docs.python.org/3/library/zipfile.html#zipfile-resources-limitations)
    

The [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 command line option can be used to run Python in isolated mode. When it cannot be used, the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)
 option or the [`PYTHONSAFEPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH)
 environment variable can be used to not prepend a potentially unsafe path to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 such as the current directory, the script’s directory or an empty string.

#### Previous topic

[`xdrlib` — Encode and decode XDR data](https://docs.python.org/3/library/xdrlib.html "previous chapter")

#### Next topic

[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Security+Considerations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsecurity_warnings.html&pagesource=library%2Fsecurity_warnings.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/security_warnings.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/index.html "Extending and Embedding the Python Interpreter")
     |
*   [previous](https://docs.python.org/3/library/xdrlib.html "xdrlib — Encode and decode XDR data")
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
*   [Security Considerations](https://docs.python.org/3/library/security_warnings.html)
    
*    
    
    |
*   Theme Auto Light Dark |