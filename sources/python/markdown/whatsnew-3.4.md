### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.3.html "What’s New In Python 3.3")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.5.html "What’s New In Python 3.5")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New In Python 3.4](https://docs.python.org/3/whatsnew/3.4.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s New In Python 3.4[¶](https://docs.python.org/3/whatsnew/3.4.html#what-s-new-in-python-3-4 "Link to this heading")

=========================================================================================================================

Author:

R. David Murray <[rdmurray@bitdance.com](mailto:rdmurray%40bitdance.com)
\> (Editor)

This article explains the new features in Python 3.4, compared to 3.3. Python 3.4 was released on March 16, 2014. For full details, see the [changelog](https://docs.python.org/3.4/whatsnew/changelog.html)
.

See also

[**PEP 429**](https://peps.python.org/pep-0429/)
 – Python 3.4 Release Schedule

Summary – Release Highlights[¶](https://docs.python.org/3/whatsnew/3.4.html#summary-release-highlights "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

New syntax features:

*   No new syntax features were added in Python 3.4.
    

Other new features:

*   [pip should always be available](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-453)
     ([**PEP 453**](https://peps.python.org/pep-0453/)
    ).
    
*   [Newly created file descriptors are non-inheritable](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-446)
     ([**PEP 446**](https://peps.python.org/pep-0446/)
    ).
    
*   command line option for [isolated mode](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-isolated-mode)
     ([bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)
    ).
    
*   [improvements in the handling of codecs](https://docs.python.org/3/whatsnew/3.4.html#codec-handling-improvements)
     that are not text encodings (multiple issues).
    
*   [A ModuleSpec Type](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-451)
     for the Import System ([**PEP 451**](https://peps.python.org/pep-0451/)
    ). (Affects importer authors.)
    
*   The [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
     format has been made [more compact and efficient](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-marshal-3)
     ([bpo-16475](https://bugs.python.org/issue?@action=redirect&bpo=16475)
    ).
    

New library modules:

*   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
    : [New provisional API for asynchronous IO](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-asyncio)
     ([**PEP 3156**](https://peps.python.org/pep-3156/)
    ).
    
*   [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
    : [Bootstrapping the pip installer](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-ensurepip)
     ([**PEP 453**](https://peps.python.org/pep-0453/)
    ).
    
*   [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
    : [Support for enumeration types](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-enum)
     ([**PEP 435**](https://peps.python.org/pep-0435/)
    ).
    
*   [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
    : [Object-oriented filesystem paths](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pathlib)
     ([**PEP 428**](https://peps.python.org/pep-0428/)
    ).
    
*   [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.")
    : [High-level and efficient I/O multiplexing](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-selectors)
    , built upon the [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")
     module primitives (part of [**PEP 3156**](https://peps.python.org/pep-3156/)
    ).
    
*   [`statistics`](https://docs.python.org/3/library/statistics.html#module-statistics "statistics: Mathematical statistics functions")
    : A basic [numerically stable statistics library](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-statistics)
     ([**PEP 450**](https://peps.python.org/pep-0450/)
    ).
    
*   [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
    : [Trace Python memory allocations](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-tracemalloc)
     ([**PEP 454**](https://peps.python.org/pep-0454/)
    ).
    

Significantly improved library modules:

*   [Single-dispatch generic functions](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-singledispatch)
     in [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
     ([**PEP 443**](https://peps.python.org/pep-0443/)
    ).
    
*   New [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
     [protocol 4](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-protocol-4)
     ([**PEP 3154**](https://peps.python.org/pep-3154/)
    ).
    
*   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
     now has [an option to avoid using os.fork on Unix](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-multiprocessing-no-fork)
     ([bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713)
    ).
    
*   [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
     has a new submodule, [`contentmanager`](https://docs.python.org/3/library/email.contentmanager.html#module-email.contentmanager "email.contentmanager: Storing and Retrieving Content from MIME Parts")
    , and a new [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
     subclass ([`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
    ) that [simplify MIME handling](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-email-contentmanager)
     ([bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891)
    ).
    
*   The [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
     and [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
     modules are now capable of correct introspection of a much wider variety of callable objects, which improves the output of the Python [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
     system.
    
*   The [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")
     module API has been declared stable
    

Security improvements:

*   [Secure and interchangeable hash algorithm](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-456)
     ([**PEP 456**](https://peps.python.org/pep-0456/)
    ).
    
*   [Make newly created file descriptors non-inheritable](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-446)
     ([**PEP 446**](https://peps.python.org/pep-0446/)
    ) to avoid leaking file descriptors to child processes.
    
*   New command line option for [isolated mode](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-isolated-mode)
    , ([bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)
    ).
    
*   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
     now has [an option to avoid using os.fork on Unix](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-multiprocessing-no-fork)
    . _spawn_ and _forkserver_ are more secure because they avoid sharing data with child processes.
    
*   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
     child processes on Windows no longer inherit all of the parent’s inheritable handles, only the necessary ones.
    
*   A new [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac "hashlib.pbkdf2_hmac")
     function provides the [PKCS#5 password-based key derivation function 2](https://en.wikipedia.org/wiki/PBKDF2)
    .
    
*   [TLSv1.1 and TLSv1.2 support](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-tls-11-12)
     for [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
    .
    
*   [Retrieving certificates from the Windows system cert store support](https://docs.python.org/3/whatsnew/3.4.html#whatsnew34-win-cert-store)
     for [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
    .
    
*   [Server-side SNI (Server Name Indication) support](https://docs.python.org/3/whatsnew/3.4.html#whatsnew34-sni)
     for [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
    .
    
*   The [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
     class has a [lot of improvements](https://docs.python.org/3/whatsnew/3.4.html#whatsnew34-sslcontext)
    .
    
*   All modules in the standard library that support SSL now support server certificate verification, including hostname matching (`ssl.match_hostname()`) and CRLs (Certificate Revocation lists, see [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations")
    ).
    

CPython implementation improvements:

*   [Safe object finalization](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-442)
     ([**PEP 442**](https://peps.python.org/pep-0442/)
    ).
    
*   Leveraging [**PEP 442**](https://peps.python.org/pep-0442/)
    , in most cases [module globals are no longer set to None during finalization](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-442)
     ([bpo-18214](https://bugs.python.org/issue?@action=redirect&bpo=18214)
    ).
    
*   [Configurable memory allocators](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-445)
     ([**PEP 445**](https://peps.python.org/pep-0445/)
    ).
    
*   [Argument Clinic](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-436)
     ([**PEP 436**](https://peps.python.org/pep-0436/)
    ).
    

Please read on for a comprehensive list of user-facing changes, including many other smaller improvements, CPython optimizations, deprecations, and potential porting issues.

New Features[¶](https://docs.python.org/3/whatsnew/3.4.html#new-features "Link to this heading")

-------------------------------------------------------------------------------------------------

### PEP 453: Explicit Bootstrapping of PIP in Python Installations[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-453-explicit-bootstrapping-of-pip-in-python-installations "Link to this heading")

#### Bootstrapping pip By Default[¶](https://docs.python.org/3/whatsnew/3.4.html#bootstrapping-pip-by-default "Link to this heading")

The new [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
 module (defined in [**PEP 453**](https://peps.python.org/pep-0453/)
) provides a standard cross-platform mechanism to bootstrap the pip installer into Python installations and virtual environments. The version of `pip` included with Python 3.4.0 is `pip` 1.5.4, and future 3.4.x maintenance releases will update the bundled version to the latest version of `pip` that is available at the time of creating the release candidate.

By default, the commands `pipX` and `pipX.Y` will be installed on all platforms (where X.Y stands for the version of the Python installation), along with the `pip` Python package and its dependencies. On Windows and in virtual environments on all platforms, the unversioned `pip` command will also be installed. On other platforms, the system wide unversioned `pip` command typically refers to the separately installed Python 2 version.

The `pyvenv` command line utility and the [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.")
 module make use of the [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
 module to make `pip` readily available in virtual environments. When using the command line utility, `pip` is installed by default, while when using the `venv` module [API](https://docs.python.org/3/library/venv.html#venv-api)
 installation of `pip` must be requested explicitly.

For CPython [source builds on POSIX systems](https://docs.python.org/3/using/unix.html#building-python-on-unix)
, the `make install` and `make altinstall` commands bootstrap `pip` by default. This behaviour can be controlled through configure options, and overridden through Makefile options.

On Windows and Mac OS X, the CPython installers now default to installing `pip` along with CPython itself (users may opt out of installing it during the installation process). Window users will need to opt in to the automatic `PATH` modifications to have `pip` available from the command line by default, otherwise it can still be accessed through the Python launcher for Windows as `py -m pip`.

As [**discussed in the PEP**](https://peps.python.org/pep-0453/#recommendations-for-downstream-distributors)
 platform packagers may choose not to install these commands by default, as long as, when invoked, they provide clear and simple directions on how to install them on that platform (usually using the system package manager).

Note

To avoid conflicts between parallel Python 2 and Python 3 installations, only the versioned `pip3` and `pip3.4` commands are bootstrapped by default when `ensurepip` is invoked directly - the `--default-pip` option is needed to also request the unversioned `pip` command. `pyvenv` and the Windows installer ensure that the unqualified `pip` command is made available in those environments, and `pip` can always be invoked via the `-m` switch rather than directly to avoid ambiguity on systems with multiple Python installations.

#### Documentation Changes[¶](https://docs.python.org/3/whatsnew/3.4.html#documentation-changes "Link to this heading")

As part of this change, the [Installing Python modules](https://docs.python.org/3/installing/index.html#installing-index)
 and [Distributing Python Modules](https://docs.python.org/3/distributing/index.html#distributing-index)
 sections of the documentation have been completely redesigned as short getting started and FAQ documents. Most packaging documentation has now been moved out to the Python Packaging Authority maintained [Python Packaging User Guide](https://packaging.python.org/)
 and the documentation of the individual projects.

However, as this migration is currently still incomplete, the legacy versions of those guides remaining available as [Building C and C++ Extensions with setuptools](https://docs.python.org/3/extending/building.html#install-index)
 and [Building C and C++ Extensions with setuptools](https://docs.python.org/3/extending/building.html#setuptools-index)
.

See also

[**PEP 453**](https://peps.python.org/pep-0453/)
 – Explicit bootstrapping of pip in Python installations

PEP written by Donald Stufft and Nick Coghlan, implemented by Donald Stufft, Nick Coghlan, Martin von Löwis and Ned Deily.

### PEP 446: Newly Created File Descriptors Are Non-Inheritable[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-446-newly-created-file-descriptors-are-non-inheritable "Link to this heading")

[**PEP 446**](https://peps.python.org/pep-0446/)
 makes newly created file descriptors [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
. In general, this is the behavior an application will want: when launching a new process, having currently open files also open in the new process can lead to all sorts of hard to find bugs, and potentially to security issues.

However, there are occasions when inheritance is desired. To support these cases, the following new functions and methods are available:

*   [`os.get_inheritable()`](https://docs.python.org/3/library/os.html#os.get_inheritable "os.get_inheritable")
    , [`os.set_inheritable()`](https://docs.python.org/3/library/os.html#os.set_inheritable "os.set_inheritable")
    
*   [`os.get_handle_inheritable()`](https://docs.python.org/3/library/os.html#os.get_handle_inheritable "os.get_handle_inheritable")
    , [`os.set_handle_inheritable()`](https://docs.python.org/3/library/os.html#os.set_handle_inheritable "os.set_handle_inheritable")
    
*   [`socket.socket.get_inheritable()`](https://docs.python.org/3/library/socket.html#socket.socket.get_inheritable "socket.socket.get_inheritable")
    , [`socket.socket.set_inheritable()`](https://docs.python.org/3/library/socket.html#socket.socket.set_inheritable "socket.socket.set_inheritable")
    

See also

[**PEP 446**](https://peps.python.org/pep-0446/)
 – Make newly created file descriptors non-inheritable

PEP written and implemented by Victor Stinner.

### Improvements to Codec Handling[¶](https://docs.python.org/3/whatsnew/3.4.html#improvements-to-codec-handling "Link to this heading")

Since it was first introduced, the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
 module has always been intended to operate as a type-neutral dynamic encoding and decoding system. However, its close coupling with the Python text model, especially the type restricted convenience methods on the builtin [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 types, has historically obscured that fact.

As a key step in clarifying the situation, the [`codecs.encode()`](https://docs.python.org/3/library/codecs.html#codecs.encode "codecs.encode")
 and [`codecs.decode()`](https://docs.python.org/3/library/codecs.html#codecs.decode "codecs.decode")
 convenience functions are now properly documented in Python 2.7, 3.3 and 3.4. These functions have existed in the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
 module (and have been covered by the regression test suite) since Python 2.4, but were previously only discoverable through runtime introspection.

Unlike the convenience methods on [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
, the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
 convenience functions support arbitrary codecs in both Python 2 and Python 3, rather than being limited to Unicode text encodings (in Python 3) or `basestring` <-> `basestring` conversions (in Python 2).

In Python 3.4, the interpreter is able to identify the known non-text encodings provided in the standard library and direct users towards these general purpose convenience functions when appropriate:

Copy

\>>> b"abcdef".decode("hex")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'hex' is not a text encoding; use codecs.decode() to handle arbitrary codecs

\>>> "hello".encode("rot13")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'rot13' is not a text encoding; use codecs.encode() to handle arbitrary codecs

\>>> open("foo.txt", encoding\="hex")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'hex' is not a text encoding; use codecs.open() to handle arbitrary codecs

In a related change, whenever it is feasible without breaking backwards compatibility, exceptions raised during encoding and decoding operations are wrapped in a chained exception of the same type that mentions the name of the codec responsible for producing the error:

Copy

\>>> import codecs

\>>> codecs.decode(b"abcdefgh", "hex")
Traceback (most recent call last):
  File "/usr/lib/python3.4/encodings/hex\_codec.py", line 20, in hex\_decode
    return (binascii.a2b\_hex(input), len(input))
binascii.Error: Non-hexadecimal digit found

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
binascii.Error: decoding with 'hex' codec failed (Error: Non-hexadecimal digit found)

\>>> codecs.encode("hello", "bz2")
Traceback (most recent call last):
  File "/usr/lib/python3.4/encodings/bz2\_codec.py", line 17, in bz2\_encode
    return (bz2.compress(input), len(input))
  File "/usr/lib/python3.4/bz2.py", line 498, in compress
    return comp.compress(data) + comp.flush()
TypeError: 'str' does not support the buffer interface

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: encoding with 'bz2' codec failed (TypeError: 'str' does not support the buffer interface)

Finally, as the examples above show, these improvements have permitted the restoration of the convenience aliases for the non-Unicode codecs that were themselves restored in Python 3.2. This means that encoding binary data to and from its hexadecimal representation (for example) can now be written as:

Copy

\>>> from codecs import encode, decode
\>>> encode(b"hello", "hex")
b'68656c6c6f'
\>>> decode(b"68656c6c6f", "hex")
b'hello'

The binary and text transforms provided in the standard library are detailed in [Binary Transforms](https://docs.python.org/3/library/codecs.html#binary-transforms)
 and [Text Transforms](https://docs.python.org/3/library/codecs.html#text-transforms)
.

(Contributed by Nick Coghlan in [bpo-7475](https://bugs.python.org/issue?@action=redirect&bpo=7475)
, [bpo-17827](https://bugs.python.org/issue?@action=redirect&bpo=17827)
, [bpo-17828](https://bugs.python.org/issue?@action=redirect&bpo=17828)
 and [bpo-19619](https://bugs.python.org/issue?@action=redirect&bpo=19619)
.)

### PEP 451: A ModuleSpec Type for the Import System[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-451-a-modulespec-type-for-the-import-system "Link to this heading")

[**PEP 451**](https://peps.python.org/pep-0451/)
 provides an encapsulation of the information about a module that the import machinery will use to load it (that is, a module specification). This helps simplify both the import implementation and several import-related APIs. The change is also a stepping stone for [several future import-related improvements](https://mail.python.org/pipermail/python-dev/2013-November/130111.html)
.

The public-facing changes from the PEP are entirely backward-compatible. Furthermore, they should be transparent to everyone but importer authors. Key finder and loader methods have been deprecated, but they will continue working. New importers should use the new methods described in the PEP. Existing importers should be updated to implement the new methods. See the [Deprecated](https://docs.python.org/3/whatsnew/3.4.html#deprecated-3-4)
 section for a list of methods that should be replaced and their replacements.

### Other Language Changes[¶](https://docs.python.org/3/whatsnew/3.4.html#other-language-changes "Link to this heading")

Some smaller changes made to the core Python language are:

*   Unicode database updated to UCD version 6.3.
    
*   [`min()`](https://docs.python.org/3/builtins/functions.html#min "min")
     and [`max()`](https://docs.python.org/3/builtins/functions.html#max "max")
     now accept a _default_ keyword-only argument that can be used to specify the value they return if the iterable they are evaluating has no elements. (Contributed by Julian Berman in [bpo-18111](https://bugs.python.org/issue?@action=redirect&bpo=18111)
    .)
    
*   Module objects are now [weakly referenceable](https://docs.python.org/3/library/weakref.html#mod-weakref)
    .
    
*   Module `__file__` attributes (and related values) should now always contain absolute paths by default, with the sole exception of `__main__.__file__` when a script has been executed directly using a relative path. (Contributed by Brett Cannon in [bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416)
    .)
    
*   All the UTF-\* codecs (except UTF-7) now reject surrogates during both encoding and decoding unless the `surrogatepass` error handler is used, with the exception of the UTF-16 decoder (which accepts valid surrogate pairs) and the UTF-16 encoder (which produces them while encoding non-BMP characters). (Contributed by Victor Stinner, Kang-Hao (Kenny) Lu and Serhiy Storchaka in [bpo-12892](https://bugs.python.org/issue?@action=redirect&bpo=12892)
    .)
    
*   New German EBCDIC [codec](https://docs.python.org/3/library/codecs.html#standard-encodings)
     `cp273`. (Contributed by Michael Bierenfeld and Andrew Kuchling in [bpo-1097797](https://bugs.python.org/issue?@action=redirect&bpo=1097797)
    .)
    
*   New Ukrainian [codec](https://docs.python.org/3/library/codecs.html#standard-encodings)
     `cp1125`. (Contributed by Serhiy Storchaka in [bpo-19668](https://bugs.python.org/issue?@action=redirect&bpo=19668)
    .)
    
*   [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .join() and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    .join() now accept arbitrary buffer objects as arguments. (Contributed by Antoine Pitrou in [bpo-15958](https://bugs.python.org/issue?@action=redirect&bpo=15958)
    .)
    
*   The [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     constructor now accepts any object that has an `__index__` method for its _base_ argument. (Contributed by Mark Dickinson in [bpo-16772](https://bugs.python.org/issue?@action=redirect&bpo=16772)
    .)
    
*   Frame objects now have a [`clear()`](https://docs.python.org/3/reference/datamodel.html#frame.clear "frame.clear")
     method that clears all references to local variables from the frame. (Contributed by Antoine Pitrou in [bpo-17934](https://bugs.python.org/issue?@action=redirect&bpo=17934)
    .)
    
*   [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
     is now registered as a [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")
    , and supports the [`reversed()`](https://docs.python.org/3/builtins/functions.html#reversed "reversed")
     builtin. (Contributed by Nick Coghlan and Claudiu Popa in [bpo-18690](https://bugs.python.org/issue?@action=redirect&bpo=18690)
     and [bpo-19078](https://bugs.python.org/issue?@action=redirect&bpo=19078)
    .)
    
*   Signatures reported by [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
     have been modified and improved in several cases as a result of the introduction of Argument Clinic and other changes to the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
     and [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
     modules.
    
*   [`__length_hint__()`](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__ "object.__length_hint__")
     is now part of the formal language specification (see [**PEP 424**](https://peps.python.org/pep-0424/)
    ). (Contributed by Armin Ronacher in [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148)
    .)
    

New Modules[¶](https://docs.python.org/3/whatsnew/3.4.html#new-modules "Link to this heading")

-----------------------------------------------------------------------------------------------

### asyncio[¶](https://docs.python.org/3/whatsnew/3.4.html#asyncio "Link to this heading")

The new [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
 module (defined in [**PEP 3156**](https://peps.python.org/pep-3156/)
) provides a standard pluggable event loop model for Python, providing solid asynchronous IO support in the standard library, and making it easier for other event loop implementations to interoperate with the standard library and each other.

For Python 3.4, this module is considered a [provisional API](https://docs.python.org/3/glossary.html#term-provisional-API)
.

See also

[**PEP 3156**](https://peps.python.org/pep-3156/)
 – Asynchronous IO Support Rebooted: the “asyncio” Module

PEP written and implementation led by Guido van Rossum.

### ensurepip[¶](https://docs.python.org/3/whatsnew/3.4.html#ensurepip "Link to this heading")

The new [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
 module is the primary infrastructure for the [**PEP 453**](https://peps.python.org/pep-0453/)
 implementation. In the normal course of events end users will not need to interact with this module, but it can be used to manually bootstrap `pip` if the automated bootstrapping into an installation or virtual environment was declined.

[`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
 includes a bundled copy of `pip`, up-to-date as of the first release candidate of the release of CPython with which it ships (this applies to both maintenance releases and feature releases). `ensurepip` does not access the internet. If the installation has internet access, after `ensurepip` is run the bundled `pip` can be used to upgrade `pip` to a more recent release than the bundled one. (Note that such an upgraded version of `pip` is considered to be a separately installed package and will not be removed if Python is uninstalled.)

The module is named _ensure_pip because if called when `pip` is already installed, it does nothing. It also has an `--upgrade` option that will cause it to install the bundled copy of `pip` if the existing installed version of `pip` is older than the bundled copy.

### enum[¶](https://docs.python.org/3/whatsnew/3.4.html#enum "Link to this heading")

The new [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
 module (defined in [**PEP 435**](https://peps.python.org/pep-0435/)
) provides a standard implementation of enumeration types, allowing other modules (such as [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
) to provide more informative error messages and better debugging support by replacing opaque integer constants with backwards compatible enumeration values.

See also

[**PEP 435**](https://peps.python.org/pep-0435/)
 – Adding an Enum type to the Python standard library

PEP written by Barry Warsaw, Eli Bendersky and Ethan Furman, implemented by Ethan Furman.

### pathlib[¶](https://docs.python.org/3/whatsnew/3.4.html#pathlib "Link to this heading")

The new [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
 module offers classes representing filesystem paths with semantics appropriate for different operating systems. Path classes are divided between _pure paths_, which provide purely computational operations without I/O, and _concrete paths_, which inherit from pure paths but also provide I/O operations.

For Python 3.4, this module is considered a [provisional API](https://docs.python.org/3/glossary.html#term-provisional-API)
.

See also

[**PEP 428**](https://peps.python.org/pep-0428/)
 – The pathlib module – object-oriented filesystem paths

PEP written and implemented by Antoine Pitrou.

### selectors[¶](https://docs.python.org/3/whatsnew/3.4.html#selectors "Link to this heading")

The new [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.")
 module (created as part of implementing [**PEP 3156**](https://peps.python.org/pep-3156/)
) allows high-level and efficient I/O multiplexing, built upon the [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")
 module primitives.

### statistics[¶](https://docs.python.org/3/whatsnew/3.4.html#statistics "Link to this heading")

The new [`statistics`](https://docs.python.org/3/library/statistics.html#module-statistics "statistics: Mathematical statistics functions")
 module (defined in [**PEP 450**](https://peps.python.org/pep-0450/)
) offers some core statistics functionality directly in the standard library. This module supports calculation of the mean, median, mode, variance and standard deviation of a data series.

See also

[**PEP 450**](https://peps.python.org/pep-0450/)
 – Adding A Statistics Module To The Standard Library

PEP written and implemented by Steven D’Aprano

### tracemalloc[¶](https://docs.python.org/3/whatsnew/3.4.html#tracemalloc "Link to this heading")

The new [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
 module (defined in [**PEP 454**](https://peps.python.org/pep-0454/)
) is a debug tool to trace memory blocks allocated by Python. It provides the following information:

*   Trace where an object was allocated
    
*   Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks
    
*   Compute the differences between two snapshots to detect memory leaks
    

See also

[**PEP 454**](https://peps.python.org/pep-0454/)
 – Add a new tracemalloc module to trace Python memory allocations

PEP written and implemented by Victor Stinner

Improved Modules[¶](https://docs.python.org/3/whatsnew/3.4.html#improved-modules "Link to this heading")

---------------------------------------------------------------------------------------------------------

### abc[¶](https://docs.python.org/3/whatsnew/3.4.html#abc "Link to this heading")

New function [`abc.get_cache_token()`](https://docs.python.org/3/library/abc.html#abc.get_cache_token "abc.get_cache_token")
 can be used to know when to invalidate caches that are affected by changes in the object graph. (Contributed by Łukasz Langa in [bpo-16832](https://bugs.python.org/issue?@action=redirect&bpo=16832)
.)

New class [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")
 has [`ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta "abc.ABCMeta")
 as its meta class. Using `ABC` as a base class has essentially the same effect as specifying `metaclass=abc.ABCMeta`, but is simpler to type and easier to read. (Contributed by Bruno Dupuis in [bpo-16049](https://bugs.python.org/issue?@action=redirect&bpo=16049)
.)

### aifc[¶](https://docs.python.org/3/whatsnew/3.4.html#aifc "Link to this heading")

The `getparams()` method now returns a namedtuple rather than a plain tuple. (Contributed by Claudiu Popa in [bpo-17818](https://bugs.python.org/issue?@action=redirect&bpo=17818)
.)

`aifc.open()` now supports the context management protocol: when used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block, the `close()` method of the returned object will be called automatically at the end of the block. (Contributed by Serhiy Storchacha in [bpo-16486](https://bugs.python.org/issue?@action=redirect&bpo=16486)
.)

The `writeframesraw()` and `writeframes()` methods now accept any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311)
.)

### argparse[¶](https://docs.python.org/3/whatsnew/3.4.html#argparse "Link to this heading")

The [`FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType")
 class now accepts _encoding_ and _errors_ arguments, which are passed through to [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
. (Contributed by Lucas Maystre in [bpo-11175](https://bugs.python.org/issue?@action=redirect&bpo=11175)
.)

### audioop[¶](https://docs.python.org/3/whatsnew/3.4.html#audioop "Link to this heading")

`audioop` now supports 24-bit samples. (Contributed by Serhiy Storchaka in [bpo-12866](https://bugs.python.org/issue?@action=redirect&bpo=12866)
.)

New `byteswap()` function converts big-endian samples to little-endian and vice versa. (Contributed by Serhiy Storchaka in [bpo-19641](https://bugs.python.org/issue?@action=redirect&bpo=19641)
.)

All `audioop` functions now accept any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. Strings are not accepted: they didn’t work before, now they raise an error right away. (Contributed by Serhiy Storchaka in [bpo-16685](https://bugs.python.org/issue?@action=redirect&bpo=16685)
.)

### base64[¶](https://docs.python.org/3/whatsnew/3.4.html#base64 "Link to this heading")

The encoding and decoding functions in [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
 now accept any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 in cases where it previously required a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 instance. (Contributed by Nick Coghlan in [bpo-17839](https://bugs.python.org/issue?@action=redirect&bpo=17839)
.)

New functions [`a85encode()`](https://docs.python.org/3/library/base64.html#base64.a85encode "base64.a85encode")
, [`a85decode()`](https://docs.python.org/3/library/base64.html#base64.a85decode "base64.a85decode")
, [`b85encode()`](https://docs.python.org/3/library/base64.html#base64.b85encode "base64.b85encode")
, and [`b85decode()`](https://docs.python.org/3/library/base64.html#base64.b85decode "base64.b85decode")
 provide the ability to encode and decode binary data from and to `Ascii85` and the git/mercurial `Base85` formats, respectively. The `a85` functions have options that can be used to make them compatible with the variants of the `Ascii85` encoding, including the Adobe variant. (Contributed by Martin Morrison, the Mercurial project, Serhiy Storchaka, and Antoine Pitrou in [bpo-17618](https://bugs.python.org/issue?@action=redirect&bpo=17618)
.)

### collections[¶](https://docs.python.org/3/whatsnew/3.4.html#collections "Link to this heading")

The [`ChainMap.new_child()`](https://docs.python.org/3/library/collections.html#collections.ChainMap.new_child "collections.ChainMap.new_child")
 method now accepts an _m_ argument specifying the child map to add to the chain. This allows an existing mapping and/or a custom mapping type to be used for the child. (Contributed by Vinay Sajip in [bpo-16613](https://bugs.python.org/issue?@action=redirect&bpo=16613)
.)

### colorsys[¶](https://docs.python.org/3/whatsnew/3.4.html#colorsys "Link to this heading")

The number of digits in the coefficients for the RGB — YIQ conversions have been expanded so that they match the FCC NTSC versions. The change in results should be less than 1% and may better match results found elsewhere. (Contributed by Brian Landers and Serhiy Storchaka in [bpo-14323](https://bugs.python.org/issue?@action=redirect&bpo=14323)
.)

### contextlib[¶](https://docs.python.org/3/whatsnew/3.4.html#contextlib "Link to this heading")

The new [`contextlib.suppress`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress "contextlib.suppress")
 context manager helps to clarify the intent of code that deliberately suppresses exceptions from a single statement. (Contributed by Raymond Hettinger in [bpo-15806](https://bugs.python.org/issue?@action=redirect&bpo=15806)
 and Zero Piraeus in [bpo-19266](https://bugs.python.org/issue?@action=redirect&bpo=19266)
.)

The new [`contextlib.redirect_stdout()`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout "contextlib.redirect_stdout")
 context manager makes it easier for utility scripts to handle inflexible APIs that write their output to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 and don’t provide any options to redirect it. Using the context manager, the `sys.stdout` output can be redirected to any other stream or, in conjunction with [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
, to a string. The latter can be especially useful, for example, to capture output from a function that was written to implement a command line interface. It is recommended only for utility scripts because it affects the global state of `sys.stdout`. (Contributed by Raymond Hettinger in [bpo-15805](https://bugs.python.org/issue?@action=redirect&bpo=15805)
.)

The [`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.")
 documentation has also been updated to include a [discussion](https://docs.python.org/3/library/contextlib.html#single-use-reusable-and-reentrant-cms)
 of the differences between single use, reusable and reentrant context managers.

### dbm[¶](https://docs.python.org/3/whatsnew/3.4.html#dbm "Link to this heading")

[`dbm.open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open")
 objects now support the context management protocol. When used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, the `close` method of the database object will be called automatically at the end of the block. (Contributed by Claudiu Popa and Nick Coghlan in [bpo-19282](https://bugs.python.org/issue?@action=redirect&bpo=19282)
.)

### dis[¶](https://docs.python.org/3/whatsnew/3.4.html#dis "Link to this heading")

Functions [`show_code()`](https://docs.python.org/3/library/dis.html#dis.show_code "dis.show_code")
, [`dis()`](https://docs.python.org/3/library/dis.html#dis.dis "dis.dis")
, [`distb()`](https://docs.python.org/3/library/dis.html#dis.distb "dis.distb")
, and [`disassemble()`](https://docs.python.org/3/library/dis.html#dis.disassemble "dis.disassemble")
 now accept a keyword-only _file_ argument that controls where they write their output.

The [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
 module is now built around an [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
 class that provides object oriented access to the details of each individual bytecode operation.

A new method, [`get_instructions()`](https://docs.python.org/3/library/dis.html#dis.get_instructions "dis.get_instructions")
, provides an iterator that emits the Instruction stream for a given piece of Python code. Thus it is now possible to write a program that inspects and manipulates a bytecode object in ways different from those provided by the [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
 module itself. For example:

Copy

\>>> import dis
\>>> for instr in dis.get\_instructions(lambda x: x + 1):
...     print(instr.opname)
LOAD\_FAST
LOAD\_CONST
BINARY\_ADD
RETURN\_VALUE

The various display tools in the [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
 module have been rewritten to use these new components.

In addition, a new application-friendly class [`Bytecode`](https://docs.python.org/3/library/dis.html#dis.Bytecode "dis.Bytecode")
 provides an object-oriented API for inspecting bytecode in both in human-readable form and for iterating over instructions. The `Bytecode` constructor takes the same arguments that [`get_instructions()`](https://docs.python.org/3/library/dis.html#dis.get_instructions "dis.get_instructions")
 does (plus an optional _current\_offset_), and the resulting object can be iterated to produce [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
 objects. But it also has a [`dis`](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "dis.Bytecode.dis")
 method, equivalent to calling [`dis`](https://docs.python.org/3/library/dis.html#dis.dis "dis.dis")
 on the constructor argument, but returned as a multi-line string:

Copy

\>>> bytecode \= dis.Bytecode(lambda x: x + 1, current\_offset\=3)
\>>> for instr in bytecode:
...     print('{} ({})'.format(instr.opname, instr.opcode))
LOAD\_FAST (124)
LOAD\_CONST (100)
BINARY\_ADD (23)
RETURN\_VALUE (83)
\>>> bytecode.dis().splitlines()
\['  1           0 LOAD\_FAST                0 (x)',\
 '      -->     3 LOAD\_CONST               1 (1)',\
 '              6 BINARY\_ADD',\
 '              7 RETURN\_VALUE'\]

[`Bytecode`](https://docs.python.org/3/library/dis.html#dis.Bytecode "dis.Bytecode")
 also has a class method, [`from_traceback()`](https://docs.python.org/3/library/dis.html#dis.Bytecode.from_traceback "dis.Bytecode.from_traceback")
, that provides the ability to manipulate a traceback (that is, `print(Bytecode.from_traceback(tb).dis())` is equivalent to `distb(tb)`).

(Contributed by Nick Coghlan, Ryan Kelly and Thomas Kluyver in [bpo-11816](https://bugs.python.org/issue?@action=redirect&bpo=11816)
 and Claudiu Popa in [bpo-17916](https://bugs.python.org/issue?@action=redirect&bpo=17916)
.)

New function [`stack_effect()`](https://docs.python.org/3/library/dis.html#dis.stack_effect "dis.stack_effect")
 computes the effect on the Python stack of a given opcode and argument, information that is not otherwise available. (Contributed by Larry Hastings in [bpo-19722](https://bugs.python.org/issue?@action=redirect&bpo=19722)
.)

### doctest[¶](https://docs.python.org/3/whatsnew/3.4.html#doctest "Link to this heading")

A new [option flag](https://docs.python.org/3/library/doctest.html#doctest-options)
, [`FAIL_FAST`](https://docs.python.org/3/library/doctest.html#doctest.FAIL_FAST "doctest.FAIL_FAST")
, halts test running as soon as the first failure is detected. (Contributed by R. David Murray and Daniel Urban in [bpo-16522](https://bugs.python.org/issue?@action=redirect&bpo=16522)
.)

The [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")
 command line interface now uses [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
, and has two new options, `-o` and `-f`. `-o` allows [doctest options](https://docs.python.org/3/library/doctest.html#doctest-options)
 to be specified on the command line, and `-f` is a shorthand for `-o FAIL_FAST` (to parallel the similar option supported by the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
 CLI). (Contributed by R. David Murray in [bpo-11390](https://bugs.python.org/issue?@action=redirect&bpo=11390)
.)

[`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")
 will now find doctests in extension module `__doc__` strings. (Contributed by Zachary Ware in [bpo-3158](https://bugs.python.org/issue?@action=redirect&bpo=3158)
.)

### email[¶](https://docs.python.org/3/whatsnew/3.4.html#email "Link to this heading")

[`as_string()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_string "email.message.Message.as_string")
 now accepts a _policy_ argument to override the default policy of the message when generating a string representation of it. This means that `as_string` can now be used in more circumstances, instead of having to create and use a [`generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.")
 in order to pass formatting parameters to its `flatten` method. (Contributed by R. David Murray in [bpo-18600](https://bugs.python.org/issue?@action=redirect&bpo=18600)
.)

New method [`as_bytes()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.as_bytes "email.message.Message.as_bytes")
 added to produce a bytes representation of the message in a fashion similar to how `as_string` produces a string representation. It does not accept the _maxheaderlen_ argument, but does accept the _unixfrom_ and _policy_ arguments. The [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 [`__bytes__()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.__bytes__ "email.message.Message.__bytes__")
 method calls it, meaning that `bytes(mymsg)` will now produce the intuitive result: a bytes object containing the fully formatted message. (Contributed by R. David Murray in [bpo-18600](https://bugs.python.org/issue?@action=redirect&bpo=18600)
.)

The [`Message.set_param()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.set_param "email.message.Message.set_param")
 message now accepts a _replace_ keyword argument. When specified, the associated header will be updated without changing its location in the list of headers. For backward compatibility, the default is `False`. (Contributed by R. David Murray in [bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891)
.)

A pair of new subclasses of [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 have been added ([`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
 and [`MIMEPart`](https://docs.python.org/3/library/email.message.html#email.message.MIMEPart "email.message.MIMEPart")
), along with a new sub-module, [`contentmanager`](https://docs.python.org/3/library/email.contentmanager.html#module-email.contentmanager "email.contentmanager: Storing and Retrieving Content from MIME Parts")
 and a new [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 attribute [`content_manager`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.content_manager "email.policy.EmailPolicy.content_manager")
. All documentation is currently in the new module, which is being added as part of email’s new [provisional API](https://docs.python.org/3/glossary.html#term-provisional-API)
. These classes provide a number of new methods that make extracting content from and inserting content into email messages much easier. For details, see the `contentmanager` documentation and the [email: Examples](https://docs.python.org/3/library/email.examples.html#email-examples)
. These API additions complete the bulk of the work that was planned as part of the email6 project. The currently provisional API is scheduled to become final in Python 3.5 (possibly with a few minor additions in the area of error handling). (Contributed by R. David Murray in [bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891)
.)

### filecmp[¶](https://docs.python.org/3/whatsnew/3.4.html#filecmp "Link to this heading")

A new [`clear_cache()`](https://docs.python.org/3/library/filecmp.html#filecmp.clear_cache "filecmp.clear_cache")
 function provides the ability to clear the [`filecmp`](https://docs.python.org/3/library/filecmp.html#module-filecmp "filecmp: Compare files efficiently.")
 comparison cache, which uses [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 information to determine if the file has changed since the last compare. This can be used, for example, if the file might have been changed and re-checked in less time than the resolution of a particular filesystem’s file modification time field. (Contributed by Mark Levitt in [bpo-18149](https://bugs.python.org/issue?@action=redirect&bpo=18149)
.)

New module attribute [`DEFAULT_IGNORES`](https://docs.python.org/3/library/filecmp.html#filecmp.DEFAULT_IGNORES "filecmp.DEFAULT_IGNORES")
 provides the list of directories that are used as the default value for the _ignore_ parameter of the [`dircmp()`](https://docs.python.org/3/library/filecmp.html#filecmp.dircmp "filecmp.dircmp")
 function. (Contributed by Eli Bendersky in [bpo-15442](https://bugs.python.org/issue?@action=redirect&bpo=15442)
.)

### functools[¶](https://docs.python.org/3/whatsnew/3.4.html#functools "Link to this heading")

The new [`partialmethod()`](https://docs.python.org/3/library/functools.html#functools.partialmethod "functools.partialmethod")
 descriptor brings partial argument application to descriptors, just as [`partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 provides for normal callables. The new descriptor also makes it easier to get arbitrary callables (including `partial()` instances) to behave like normal instance methods when included in a class definition. (Contributed by Alon Horev and Nick Coghlan in [bpo-4331](https://bugs.python.org/issue?@action=redirect&bpo=4331)
.)

The new [`@singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch "functools.singledispatch")
 decorator brings support for single-dispatch generic functions to the Python standard library. Where object oriented programming focuses on grouping multiple operations on a common set of data into a class, a generic function focuses on grouping multiple implementations of an operation that allows it to work with _different_ kinds of data.

See also

[**PEP 443**](https://peps.python.org/pep-0443/)
 – Single-dispatch generic functions

PEP written and implemented by Łukasz Langa.

[`@total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering "functools.total_ordering")
 now supports a return value of [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
 from the underlying comparison function. (Contributed by Katie Miller in [bpo-10042](https://bugs.python.org/issue?@action=redirect&bpo=10042)
.)

A pure-python version of the [`partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 function is now in the stdlib; in CPython it is overridden by the C accelerated version, but it is available for other implementations to use. (Contributed by Brian Thorne in [bpo-12428](https://bugs.python.org/issue?@action=redirect&bpo=12428)
.)

### gc[¶](https://docs.python.org/3/whatsnew/3.4.html#gc "Link to this heading")

New function [`get_stats()`](https://docs.python.org/3/library/gc.html#gc.get_stats "gc.get_stats")
 returns a list of three per-generation dictionaries containing the collections statistics since interpreter startup. (Contributed by Antoine Pitrou in [bpo-16351](https://bugs.python.org/issue?@action=redirect&bpo=16351)
.)

### glob[¶](https://docs.python.org/3/whatsnew/3.4.html#glob "Link to this heading")

A new function [`escape()`](https://docs.python.org/3/library/glob.html#glob.escape "glob.escape")
 provides a way to escape special characters in a filename so that they do not become part of the globbing expansion but are instead matched literally. (Contributed by Serhiy Storchaka in [bpo-8402](https://bugs.python.org/issue?@action=redirect&bpo=8402)
.)

### hashlib[¶](https://docs.python.org/3/whatsnew/3.4.html#hashlib "Link to this heading")

A new [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac "hashlib.pbkdf2_hmac")
 function provides the [PKCS#5 password-based key derivation function 2](https://en.wikipedia.org/wiki/PBKDF2)
. (Contributed by Christian Heimes in [bpo-18582](https://bugs.python.org/issue?@action=redirect&bpo=18582)
.)

The [`name`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.name "hashlib.hash.name")
 attribute of [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
 hash objects is now a formally supported interface. It has always existed in CPython’s `hashlib` (although it did not return lower case names for all supported hashes), but it was not a public interface and so some other Python implementations have not previously supported it. (Contributed by Jason R. Coombs in [bpo-18532](https://bugs.python.org/issue?@action=redirect&bpo=18532)
.)

### hmac[¶](https://docs.python.org/3/whatsnew/3.4.html#hmac "Link to this heading")

[`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication (HMAC) implementation")
 now accepts `bytearray` as well as `bytes` for the _key_ argument to the [`new()`](https://docs.python.org/3/library/hmac.html#hmac.new "hmac.new")
 function, and the _msg_ parameter to both the `new()` function and the [`update()`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.update "hmac.HMAC.update")
 method now accepts any type supported by the [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
 module. (Contributed by Jonas Borgström in [bpo-18240](https://bugs.python.org/issue?@action=redirect&bpo=18240)
.)

The _digestmod_ argument to the [`hmac.new()`](https://docs.python.org/3/library/hmac.html#hmac.new "hmac.new")
 function may now be any hash digest name recognized by [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
. In addition, the current behavior in which the value of _digestmod_ defaults to `MD5` is deprecated: in a future version of Python there will be no default value. (Contributed by Christian Heimes in [bpo-17276](https://bugs.python.org/issue?@action=redirect&bpo=17276)
.)

With the addition of [`block_size`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.block_size "hmac.HMAC.block_size")
 and [`name`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.name "hmac.HMAC.name")
 attributes (and the formal documentation of the [`digest_size`](https://docs.python.org/3/library/hmac.html#hmac.HMAC.digest_size "hmac.HMAC.digest_size")
 attribute), the [`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication (HMAC) implementation")
 module now conforms fully to the [**PEP 247**](https://peps.python.org/pep-0247/)
 API. (Contributed by Christian Heimes in [bpo-18775](https://bugs.python.org/issue?@action=redirect&bpo=18775)
.)

### html[¶](https://docs.python.org/3/whatsnew/3.4.html#html "Link to this heading")

New function [`unescape()`](https://docs.python.org/3/library/html.html#html.unescape "html.unescape")
 function converts HTML5 character references to the corresponding Unicode characters. (Contributed by Ezio Melotti in [bpo-2927](https://bugs.python.org/issue?@action=redirect&bpo=2927)
.)

[`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
 accepts a new keyword argument _convert\_charrefs_ that, when `True`, automatically converts all character references. For backward-compatibility, its value defaults to `False`, but it will change to `True` in a future version of Python, so you are invited to set it explicitly and update your code to use this new feature. (Contributed by Ezio Melotti in [bpo-13633](https://bugs.python.org/issue?@action=redirect&bpo=13633)
.)

The _strict_ argument of [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
 is now deprecated. (Contributed by Ezio Melotti in [bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114)
.)

### http[¶](https://docs.python.org/3/whatsnew/3.4.html#http "Link to this heading")

[`send_error()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_error "http.server.BaseHTTPRequestHandler.send_error")
 now accepts an optional additional _explain_ parameter which can be used to provide an extended error description, overriding the hardcoded default if there is one. This extended error description will be formatted using the [`error_message_format`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.error_message_format "http.server.BaseHTTPRequestHandler.error_message_format")
 attribute and sent as the body of the error response. (Contributed by Karl Cow in [bpo-12921](https://bugs.python.org/issue?@action=redirect&bpo=12921)
.)

The [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
 [command line interface](https://docs.python.org/3/library/http.server.html#http-server-cli)
 now has a `-b/--bind` option that causes the server to listen on a specific address. (Contributed by Malte Swart in [bpo-17764](https://bugs.python.org/issue?@action=redirect&bpo=17764)
.)

### idlelib and IDLE[¶](https://docs.python.org/3/whatsnew/3.4.html#idlelib-and-idle "Link to this heading")

Since idlelib implements the IDLE shell and editor and is not intended for import by other programs, it gets improvements with every release. See `Lib/idlelib/NEWS.txt` for a cumulative list of changes since 3.3.0, as well as changes made in future 3.4.x releases. This file is also available from the IDLE Help ‣ About IDLE dialog.

### importlib[¶](https://docs.python.org/3/whatsnew/3.4.html#importlib "Link to this heading")

The [`InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader")
 ABC defines a new method, [`source_to_code()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.source_to_code "importlib.abc.InspectLoader.source_to_code")
 that accepts source data and a path and returns a code object. The default implementation is equivalent to `compile(data, path, 'exec', dont_inherit=True)`. (Contributed by Eric Snow and Brett Cannon in [bpo-15627](https://bugs.python.org/issue?@action=redirect&bpo=15627)
.)

[`InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader")
 also now has a default implementation for the [`get_code()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_code "importlib.abc.InspectLoader.get_code")
 method. However, it will normally be desirable to override the default implementation for performance reasons. (Contributed by Brett Cannon in [bpo-18072](https://bugs.python.org/issue?@action=redirect&bpo=18072)
.)

The [`reload()`](https://docs.python.org/3/library/importlib.html#importlib.reload "importlib.reload")
 function has been moved from `imp` to [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 as part of the `imp` module deprecation. (Contributed by Berker Peksag in [bpo-18193](https://bugs.python.org/issue?@action=redirect&bpo=18193)
.)

[`importlib.util`](https://docs.python.org/3/library/importlib.html#module-importlib.util "importlib.util: Utility code for importers")
 now has a [`MAGIC_NUMBER`](https://docs.python.org/3/library/importlib.html#importlib.util.MAGIC_NUMBER "importlib.util.MAGIC_NUMBER")
 attribute providing access to the bytecode version number. This replaces the `get_magic()` function in the deprecated `imp` module. (Contributed by Brett Cannon in [bpo-18192](https://bugs.python.org/issue?@action=redirect&bpo=18192)
.)

New [`importlib.util`](https://docs.python.org/3/library/importlib.html#module-importlib.util "importlib.util: Utility code for importers")
 functions [`cache_from_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source")
 and [`source_from_cache()`](https://docs.python.org/3/library/importlib.html#importlib.util.source_from_cache "importlib.util.source_from_cache")
 replace the same-named functions in the deprecated `imp` module. (Contributed by Brett Cannon in [bpo-18194](https://bugs.python.org/issue?@action=redirect&bpo=18194)
.)

The [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 bootstrap [`NamespaceLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.NamespaceLoader "importlib.machinery.NamespaceLoader")
 now conforms to the [`InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader")
 ABC, which means that `runpy` and `python -m` can now be used with namespace packages. (Contributed by Brett Cannon in [bpo-18058](https://bugs.python.org/issue?@action=redirect&bpo=18058)
.)

[`importlib.util`](https://docs.python.org/3/library/importlib.html#module-importlib.util "importlib.util: Utility code for importers")
 has a new function [`decode_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.decode_source "importlib.util.decode_source")
 that decodes source from bytes using universal newline processing. This is useful for implementing [`InspectLoader.get_source()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "importlib.abc.InspectLoader.get_source")
 methods.

[`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader")
 now has a [`get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_filename "importlib.machinery.ExtensionFileLoader.get_filename")
 method. This was inadvertently omitted in the original implementation. (Contributed by Eric Snow in [bpo-19152](https://bugs.python.org/issue?@action=redirect&bpo=19152)
.)

### inspect[¶](https://docs.python.org/3/whatsnew/3.4.html#inspect "Link to this heading")

The [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
 module now offers a basic [command line interface](https://docs.python.org/3/library/inspect.html#inspect-module-cli)
 to quickly display source code and other information for modules, classes and functions. (Contributed by Claudiu Popa and Nick Coghlan in [bpo-18626](https://bugs.python.org/issue?@action=redirect&bpo=18626)
.)

[`unwrap()`](https://docs.python.org/3/library/inspect.html#inspect.unwrap "inspect.unwrap")
 makes it easy to unravel wrapper function chains created by [`@functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps "functools.wraps")
 (and any other API that sets the `__wrapped__` attribute on a wrapper function). (Contributed by Daniel Urban, Aaron Iles and Nick Coghlan in [bpo-13266](https://bugs.python.org/issue?@action=redirect&bpo=13266)
.)

As part of the implementation of the new [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
 module, the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
 module now has substantially better support for custom `__dir__` methods and dynamic class attributes provided through metaclasses. (Contributed by Ethan Furman in [bpo-18929](https://bugs.python.org/issue?@action=redirect&bpo=18929)
 and [bpo-19030](https://bugs.python.org/issue?@action=redirect&bpo=19030)
.)

[`getfullargspec()`](https://docs.python.org/3/library/inspect.html#inspect.getfullargspec "inspect.getfullargspec")
 and `getargspec()` now use the [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 API. This allows them to support a much broader range of callables, including those with `__signature__` attributes, those with metadata provided by argument clinic, [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 objects and more. Note that, unlike `signature()`, these functions still ignore `__wrapped__` attributes, and report the already bound first argument for bound methods, so it is still necessary to update your code to use `signature()` directly if those features are desired. (Contributed by Yury Selivanov in [bpo-17481](https://bugs.python.org/issue?@action=redirect&bpo=17481)
.)

[`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 now supports duck types of CPython functions, which adds support for functions compiled with Cython. (Contributed by Stefan Behnel and Yury Selivanov in [bpo-17159](https://bugs.python.org/issue?@action=redirect&bpo=17159)
.)

### ipaddress[¶](https://docs.python.org/3/whatsnew/3.4.html#ipaddress "Link to this heading")

[`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")
 was added to the standard library in Python 3.3 as a [provisional API](https://docs.python.org/3/glossary.html#term-provisional-API)
. With the release of Python 3.4, this qualification has been removed: `ipaddress` is now considered a stable API, covered by the normal standard library requirements to maintain backwards compatibility.

A new [`is_global`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global "ipaddress.IPv4Address.is_global")
 property is `True` if an address is globally routeable. (Contributed by Peter Moody in [bpo-17400](https://bugs.python.org/issue?@action=redirect&bpo=17400)
.)

### logging[¶](https://docs.python.org/3/whatsnew/3.4.html#logging "Link to this heading")

The [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "logging.handlers.TimedRotatingFileHandler")
 has a new _atTime_ parameter that can be used to specify the time of day when rollover should happen. (Contributed by Ronald Oussoren in [bpo-9556](https://bugs.python.org/issue?@action=redirect&bpo=9556)
.)

[`SocketHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler "logging.handlers.SocketHandler")
 and [`DatagramHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler "logging.handlers.DatagramHandler")
 now support Unix domain sockets (by setting _port_ to `None`). (Contributed by Vinay Sajip in commit ce46195b56a9.)

[`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig")
 now accepts a [`configparser.RawConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser "configparser.RawConfigParser")
 subclass instance for the _fname_ parameter. This facilitates using a configuration file when logging configuration is just a part of the overall application configuration, or where the application modifies the configuration before passing it to `fileConfig()`. (Contributed by Vinay Sajip in [bpo-16110](https://bugs.python.org/issue?@action=redirect&bpo=16110)
.)

Logging configuration data received from a socket via the [`logging.config.listen()`](https://docs.python.org/3/library/logging.config.html#logging.config.listen "logging.config.listen")
 function can now be validated before being processed by supplying a verification function as the argument to the new _verify_ keyword argument. (Contributed by Vinay Sajip in [bpo-15452](https://bugs.python.org/issue?@action=redirect&bpo=15452)
.)

### marshal[¶](https://docs.python.org/3/whatsnew/3.4.html#marshal "Link to this heading")

The default [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
 version has been bumped to 3. The code implementing the new version restores the Python2 behavior of recording only one copy of interned strings and preserving the interning on deserialization, and extends this “one copy” ability to any object type (including handling recursive references). This reduces both the size of `.pyc` files and the amount of memory a module occupies in memory when it is loaded from a `.pyc` (or `.pyo`) file. (Contributed by Kristján Valur Jónsson in [bpo-16475](https://bugs.python.org/issue?@action=redirect&bpo=16475)
, with additional speedups by Antoine Pitrou in [bpo-19219](https://bugs.python.org/issue?@action=redirect&bpo=19219)
.)

### mmap[¶](https://docs.python.org/3/whatsnew/3.4.html#mmap "Link to this heading")

mmap objects are now [weakly referenceable](https://docs.python.org/3/library/weakref.html#mod-weakref)
. (Contributed by Valerie Lambert in [bpo-4885](https://bugs.python.org/issue?@action=redirect&bpo=4885)
.)

### multiprocessing[¶](https://docs.python.org/3/whatsnew/3.4.html#multiprocessing "Link to this heading")

On Unix two new [start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods)
, `spawn` and `forkserver`, have been added for starting processes using [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
. These make the mixing of processes with threads more robust, and the `spawn` method matches the semantics that multiprocessing has always used on Windows. New function [`get_all_start_methods()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_all_start_methods "multiprocessing.get_all_start_methods")
 reports all start methods available on the platform, [`get_start_method()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_start_method "multiprocessing.get_start_method")
 reports the current start method, and [`set_start_method()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method")
 sets the start method. (Contributed by Richard Oudkerk in [bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713)
.)

[`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
 also now has the concept of a `context`, which determines how child processes are created. New function [`get_context()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_context "multiprocessing.get_context")
 returns a context that uses a specified start method. It has the same API as the `multiprocessing` module itself, so you can use it to create [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool")
s and other objects that will operate within that context. This allows a framework and an application or different parts of the same application to use multiprocessing without interfering with each other. (Contributed by Richard Oudkerk in [bpo-18999](https://bugs.python.org/issue?@action=redirect&bpo=18999)
.)

Except when using the old _fork_ start method, child processes no longer inherit unneeded handles/file descriptors from their parents (part of [bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713)
).

[`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
 now relies on [`runpy`](https://docs.python.org/3/library/runpy.html#module-runpy "runpy: Locate and run Python modules without importing them first.")
 (which implements the `-m` switch) to initialise `__main__` appropriately in child processes when using the `spawn` or `forkserver` start methods. This resolves some edge cases where combining multiprocessing, the `-m` command line switch, and explicit relative imports could cause obscure failures in child processes. (Contributed by Nick Coghlan in [bpo-19946](https://bugs.python.org/issue?@action=redirect&bpo=19946)
.)

### operator[¶](https://docs.python.org/3/whatsnew/3.4.html#operator "Link to this heading")

New function [`length_hint()`](https://docs.python.org/3/library/operator.html#operator.length_hint "operator.length_hint")
 provides an implementation of the specification for how the [`__length_hint__()`](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__ "object.__length_hint__")
 special method should be used, as part of the [**PEP 424**](https://peps.python.org/pep-0424/)
 formal specification of this language feature. (Contributed by Armin Ronacher in [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148)
.)

There is now a pure-python version of the [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators.")
 module available for reference and for use by alternate implementations of Python. (Contributed by Zachary Ware in [bpo-16694](https://bugs.python.org/issue?@action=redirect&bpo=16694)
.)

### os[¶](https://docs.python.org/3/whatsnew/3.4.html#os "Link to this heading")

There are new functions to get and set the [inheritable flag](https://docs.python.org/3/library/os.html#fd-inheritance)
 of a file descriptor ([`os.get_inheritable()`](https://docs.python.org/3/library/os.html#os.get_inheritable "os.get_inheritable")
, [`os.set_inheritable()`](https://docs.python.org/3/library/os.html#os.set_inheritable "os.set_inheritable")
) or a Windows handle ([`os.get_handle_inheritable()`](https://docs.python.org/3/library/os.html#os.get_handle_inheritable "os.get_handle_inheritable")
, [`os.set_handle_inheritable()`](https://docs.python.org/3/library/os.html#os.set_handle_inheritable "os.set_handle_inheritable")
).

New function [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
 reports the number of CPUs available on the platform on which Python is running (or `None` if the count can’t be determined). The [`multiprocessing.cpu_count()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.cpu_count "multiprocessing.cpu_count")
 function is now implemented in terms of this function). (Contributed by Trent Nelson, Yogesh Chaudhari, Victor Stinner, and Charles-François Natali in [bpo-17914](https://bugs.python.org/issue?@action=redirect&bpo=17914)
.)

[`os.path.samestat()`](https://docs.python.org/3/library/os.path.html#os.path.samestat "os.path.samestat")
 is now available on the Windows platform (and the [`os.path.samefile()`](https://docs.python.org/3/library/os.path.html#os.path.samefile "os.path.samefile")
 implementation is now shared between Unix and Windows). (Contributed by Brian Curtin in [bpo-11939](https://bugs.python.org/issue?@action=redirect&bpo=11939)
.)

[`os.path.ismount()`](https://docs.python.org/3/library/os.path.html#os.path.ismount "os.path.ismount")
 now recognizes volumes mounted below a drive root on Windows. (Contributed by Tim Golden in [bpo-9035](https://bugs.python.org/issue?@action=redirect&bpo=9035)
.)

[`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 supports two new flags on platforms that provide them, [`O_PATH`](https://docs.python.org/3/library/os.html#os.O_PATH "os.O_PATH")
 (un-opened file descriptor), and [`O_TMPFILE`](https://docs.python.org/3/library/os.html#os.O_TMPFILE "os.O_TMPFILE")
 (unnamed temporary file; as of 3.4.0 release available only on Linux systems with a kernel version of 3.11 or newer that have uapi headers). (Contributed by Christian Heimes in [bpo-18673](https://bugs.python.org/issue?@action=redirect&bpo=18673)
 and Benjamin Peterson, respectively.)

### pdb[¶](https://docs.python.org/3/whatsnew/3.4.html#pdb "Link to this heading")

[`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")
 has been enhanced to handle generators, [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
, and `yield from` in a more useful fashion. This is especially helpful when debugging [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
 based programs. (Contributed by Andrew Svetlov and Xavier de Gaye in [bpo-16596](https://bugs.python.org/issue?@action=redirect&bpo=16596)
.)

The `print` command has been removed from [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")
, restoring access to the Python [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function from the pdb command line. Python2’s `pdb` did not have a `print` command; instead, entering `print` executed the `print` statement. In Python3 `print` was mistakenly made an alias for the pdb [`p`](https://docs.python.org/3/library/pdb.html#pdbcommand-p)
 command. `p`, however, prints the `repr` of its argument, not the `str` like the Python2 `print` command did. Worse, the Python3 `pdb print` command shadowed the Python3 `print` function, making it inaccessible at the `pdb` prompt. (Contributed by Connor Osborn in [bpo-18764](https://bugs.python.org/issue?@action=redirect&bpo=18764)
.)

### pickle[¶](https://docs.python.org/3/whatsnew/3.4.html#pickle "Link to this heading")

[`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 now supports (but does not use by default) a new pickle protocol, protocol 4. This new protocol addresses a number of issues that were present in previous protocols, such as the serialization of nested classes, very large strings and containers, and classes whose [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
 method takes keyword-only arguments. It also provides some efficiency improvements.

See also

[**PEP 3154**](https://peps.python.org/pep-3154/)
 – Pickle protocol 4

PEP written by Antoine Pitrou and implemented by Alexandre Vassalotti.

### plistlib[¶](https://docs.python.org/3/whatsnew/3.4.html#plistlib "Link to this heading")

[`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.")
 now has an API that is similar to the standard pattern for stdlib serialization protocols, with new [`load()`](https://docs.python.org/3/library/plistlib.html#plistlib.load "plistlib.load")
, [`dump()`](https://docs.python.org/3/library/plistlib.html#plistlib.dump "plistlib.dump")
, [`loads()`](https://docs.python.org/3/library/plistlib.html#plistlib.loads "plistlib.loads")
, and [`dumps()`](https://docs.python.org/3/library/plistlib.html#plistlib.dumps "plistlib.dumps")
 functions. (The older API is now deprecated.) In addition to the already supported XML plist format ([`FMT_XML`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_XML "plistlib.FMT_XML")
), it also now supports the binary plist format ([`FMT_BINARY`](https://docs.python.org/3/library/plistlib.html#plistlib.FMT_BINARY "plistlib.FMT_BINARY")
). (Contributed by Ronald Oussoren and others in [bpo-14455](https://bugs.python.org/issue?@action=redirect&bpo=14455)
.)

### poplib[¶](https://docs.python.org/3/whatsnew/3.4.html#poplib "Link to this heading")

Two new methods have been added to [`poplib`](https://docs.python.org/3/library/poplib.html#module-poplib "poplib: POP3 protocol client (requires sockets).")
: [`capa()`](https://docs.python.org/3/library/poplib.html#poplib.POP3.capa "poplib.POP3.capa")
, which returns the list of capabilities advertised by the POP server, and [`stls()`](https://docs.python.org/3/library/poplib.html#poplib.POP3.stls "poplib.POP3.stls")
, which switches a clear-text POP3 session into an encrypted POP3 session if the POP server supports it. (Contributed by Lorenzo Catucci in [bpo-4473](https://bugs.python.org/issue?@action=redirect&bpo=4473)
.)

### pprint[¶](https://docs.python.org/3/whatsnew/3.4.html#pprint "Link to this heading")

The [`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint "pprint: Data pretty printer.")
 module’s [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter")
 class and its [`pformat()`](https://docs.python.org/3/library/pprint.html#pprint.pformat "pprint.pformat")
, and [`pprint()`](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
 functions have a new option, _compact_, that controls how the output is formatted. Currently setting _compact_ to `True` means that sequences will be printed with as many sequence elements as will fit within _width_ on each (indented) line. (Contributed by Serhiy Storchaka in [bpo-19132](https://bugs.python.org/issue?@action=redirect&bpo=19132)
.)

Long strings are now wrapped using Python’s normal line continuation syntax. (Contributed by Antoine Pitrou in [bpo-17150](https://bugs.python.org/issue?@action=redirect&bpo=17150)
.)

### pty[¶](https://docs.python.org/3/whatsnew/3.4.html#pty "Link to this heading")

[`pty.spawn()`](https://docs.python.org/3/library/pty.html#pty.spawn "pty.spawn")
 now returns the status value from [`os.waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 on the child process, instead of `None`. (Contributed by Gregory P. Smith.)

### pydoc[¶](https://docs.python.org/3/whatsnew/3.4.html#pydoc "Link to this heading")

The [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 module is now based directly on the [`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 introspection API, allowing it to provide signature information for a wider variety of callable objects. This change also means that `__wrapped__` attributes are now taken into account when displaying help information. (Contributed by Larry Hastings in [bpo-19674](https://bugs.python.org/issue?@action=redirect&bpo=19674)
.)

The [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 module no longer displays the `self` parameter for already bound methods. Instead, it aims to always display the exact current signature of the supplied callable. (Contributed by Larry Hastings in [bpo-20710](https://bugs.python.org/issue?@action=redirect&bpo=20710)
.)

In addition to the changes that have been made to [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 directly, its handling of custom `__dir__` methods and various descriptor behaviours has also been improved substantially by the underlying changes in the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
 module.

As the [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
 builtin is based on [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
, the above changes also affect the behaviour of `help()`.

### re[¶](https://docs.python.org/3/whatsnew/3.4.html#re "Link to this heading")

New [`fullmatch()`](https://docs.python.org/3/library/re.html#re.fullmatch "re.fullmatch")
 function and [`Pattern.fullmatch()`](https://docs.python.org/3/library/re.html#re.Pattern.fullmatch "re.Pattern.fullmatch")
 method anchor the pattern at both ends of the string to match. This provides a way to be explicit about the goal of the match, which avoids a class of subtle bugs where `$` characters get lost during code changes or the addition of alternatives to an existing regular expression. (Contributed by Matthew Barnett in [bpo-16203](https://bugs.python.org/issue?@action=redirect&bpo=16203)
.)

The repr of [regex objects](https://docs.python.org/3/library/re.html#re-objects)
 now includes the pattern and the flags; the repr of [match objects](https://docs.python.org/3/library/re.html#match-objects)
 now includes the start, end, and the part of the string that matched. (Contributed by Hugo Lopes Tavares and Serhiy Storchaka in [bpo-13592](https://bugs.python.org/issue?@action=redirect&bpo=13592)
 and [bpo-17087](https://bugs.python.org/issue?@action=redirect&bpo=17087)
.)

### resource[¶](https://docs.python.org/3/whatsnew/3.4.html#resource "Link to this heading")

New [`prlimit()`](https://docs.python.org/3/library/resource.html#resource.prlimit "resource.prlimit")
 function, available on Linux platforms with a kernel version of 2.6.36 or later and glibc of 2.13 or later, provides the ability to query or set the resource limits for processes other than the one making the call. (Contributed by Christian Heimes in [bpo-16595](https://bugs.python.org/issue?@action=redirect&bpo=16595)
.)

On Linux kernel version 2.6.36 or later, there are also some new Linux specific constants: [`RLIMIT_MSGQUEUE`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_MSGQUEUE "resource.RLIMIT_MSGQUEUE")
, [`RLIMIT_NICE`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NICE "resource.RLIMIT_NICE")
, [`RLIMIT_RTPRIO`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_RTPRIO "resource.RLIMIT_RTPRIO")
, [`RLIMIT_RTTIME`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_RTTIME "resource.RLIMIT_RTTIME")
, and [`RLIMIT_SIGPENDING`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_SIGPENDING "resource.RLIMIT_SIGPENDING")
. (Contributed by Christian Heimes in [bpo-19324](https://bugs.python.org/issue?@action=redirect&bpo=19324)
.)

On FreeBSD version 9 and later, there some new FreeBSD specific constants: [`RLIMIT_SBSIZE`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_SBSIZE "resource.RLIMIT_SBSIZE")
, [`RLIMIT_SWAP`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_SWAP "resource.RLIMIT_SWAP")
, and [`RLIMIT_NPTS`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NPTS "resource.RLIMIT_NPTS")
. (Contributed by Claudiu Popa in [bpo-19343](https://bugs.python.org/issue?@action=redirect&bpo=19343)
.)

### select[¶](https://docs.python.org/3/whatsnew/3.4.html#select "Link to this heading")

[`epoll`](https://docs.python.org/3/library/select.html#select.epoll "select.epoll")
 objects now support the context management protocol. When used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, the [`close()`](https://docs.python.org/3/library/select.html#select.epoll.close "select.epoll.close")
 method will be called automatically at the end of the block. (Contributed by Serhiy Storchaka in [bpo-16488](https://bugs.python.org/issue?@action=redirect&bpo=16488)
.)

[`devpoll`](https://docs.python.org/3/library/select.html#select.devpoll "select.devpoll")
 objects now have [`fileno()`](https://docs.python.org/3/library/select.html#select.devpoll.fileno "select.devpoll.fileno")
 and [`close()`](https://docs.python.org/3/library/select.html#select.devpoll.close "select.devpoll.close")
 methods, as well as a new attribute [`closed`](https://docs.python.org/3/library/select.html#select.devpoll.closed "select.devpoll.closed")
. (Contributed by Victor Stinner in [bpo-18794](https://bugs.python.org/issue?@action=redirect&bpo=18794)
.)

### shelve[¶](https://docs.python.org/3/whatsnew/3.4.html#shelve "Link to this heading")

[`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf")
 instances may now be used in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements, and will be automatically closed at the end of the `with` block. (Contributed by Filip Gruszczyński in [bpo-13896](https://bugs.python.org/issue?@action=redirect&bpo=13896)
.)

### shutil[¶](https://docs.python.org/3/whatsnew/3.4.html#shutil "Link to this heading")

[`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile")
 now raises a specific [`Error`](https://docs.python.org/3/library/shutil.html#shutil.Error "shutil.Error")
 subclass, [`SameFileError`](https://docs.python.org/3/library/shutil.html#shutil.SameFileError "shutil.SameFileError")
, when the source and destination are the same file, which allows an application to take appropriate action on this specific error. (Contributed by Atsuo Ishimoto and Hynek Schlawack in [bpo-1492704](https://bugs.python.org/issue?@action=redirect&bpo=1492704)
.)

### smtpd[¶](https://docs.python.org/3/whatsnew/3.4.html#smtpd "Link to this heading")

The `SMTPServer` and `SMTPChannel` classes now accept a _map_ keyword argument which, if specified, is passed in to `asynchat.async_chat` as its _map_ argument. This allows an application to avoid affecting the global socket map. (Contributed by Vinay Sajip in [bpo-11959](https://bugs.python.org/issue?@action=redirect&bpo=11959)
.)

### smtplib[¶](https://docs.python.org/3/whatsnew/3.4.html#smtplib "Link to this heading")

[`SMTPException`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTPException "smtplib.SMTPException")
 is now a subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, which allows both socket level errors and SMTP protocol level errors to be caught in one try/except statement by code that only cares whether or not an error occurred. (Contributed by Ned Jackson Lovely in [bpo-2118](https://bugs.python.org/issue?@action=redirect&bpo=2118)
.)

### socket[¶](https://docs.python.org/3/whatsnew/3.4.html#socket "Link to this heading")

The socket module now supports the [`CAN_BCM`](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "socket.CAN_BCM")
 protocol on platforms that support it. (Contributed by Brian Thorne in [bpo-15359](https://bugs.python.org/issue?@action=redirect&bpo=15359)
.)

Socket objects have new methods to get or set their [inheritable flag](https://docs.python.org/3/library/os.html#fd-inheritance)
, [`get_inheritable()`](https://docs.python.org/3/library/socket.html#socket.socket.get_inheritable "socket.socket.get_inheritable")
 and [`set_inheritable()`](https://docs.python.org/3/library/socket.html#socket.socket.set_inheritable "socket.socket.set_inheritable")
.

The `socket.AF_*` and `socket.SOCK_*` constants are now enumeration values using the new [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
 module. This allows meaningful names to be printed during debugging, instead of integer “magic numbers”.

The [`AF_LINK`](https://docs.python.org/3/library/socket.html#socket.AF_LINK "socket.AF_LINK")
 constant is now available on BSD and OSX.

[`inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton")
 and [`inet_ntop()`](https://docs.python.org/3/library/socket.html#socket.inet_ntop "socket.inet_ntop")
 are now supported on Windows. (Contributed by Atsuo Ishimoto in [bpo-7171](https://bugs.python.org/issue?@action=redirect&bpo=7171)
.)

### sqlite3[¶](https://docs.python.org/3/whatsnew/3.4.html#sqlite3 "Link to this heading")

A new boolean parameter to the [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect")
 function, _uri_, can be used to indicate that the _database_ parameter is a `uri` (see the [SQLite URI documentation](https://www.sqlite.org/uri.html)
). (Contributed by poq in [bpo-13773](https://bugs.python.org/issue?@action=redirect&bpo=13773)
.)

### ssl[¶](https://docs.python.org/3/whatsnew/3.4.html#ssl "Link to this heading")

[`PROTOCOL_TLSv1_1`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLSv1_1 "ssl.PROTOCOL_TLSv1_1")
 and [`PROTOCOL_TLSv1_2`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLSv1_2 "ssl.PROTOCOL_TLSv1_2")
 (TLSv1.1 and TLSv1.2 support) have been added; support for these protocols is only available if Python is linked with OpenSSL 1.0.1 or later. (Contributed by Michele Orrù and Antoine Pitrou in [bpo-16692](https://bugs.python.org/issue?@action=redirect&bpo=16692)
.)

New function [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context")
 provides a standard way to obtain an [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 whose settings are intended to be a reasonable balance between compatibility and security. These settings are more stringent than the defaults provided by the `SSLContext` constructor, and may be adjusted in the future, without prior deprecation, if best-practice security requirements change. The new recommended best practice for using stdlib libraries that support SSL is to use `create_default_context()` to obtain an `SSLContext` object, modify it if needed, and then pass it as the _context_ argument of the appropriate stdlib API. (Contributed by Christian Heimes in [bpo-19689](https://bugs.python.org/issue?@action=redirect&bpo=19689)
.)

[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 method [`load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations")
 accepts a new optional argument _cadata_, which can be used to provide PEM or DER encoded certificates directly via strings or bytes, respectively. (Contributed by Christian Heimes in [bpo-18138](https://bugs.python.org/issue?@action=redirect&bpo=18138)
.)

New function [`get_default_verify_paths()`](https://docs.python.org/3/library/ssl.html#ssl.get_default_verify_paths "ssl.get_default_verify_paths")
 returns a named tuple of the paths and environment variables that the [`set_default_verify_paths()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_default_verify_paths "ssl.SSLContext.set_default_verify_paths")
 method uses to set OpenSSL’s default `cafile` and `capath`. This can be an aid in debugging default verification issues. (Contributed by Christian Heimes in [bpo-18143](https://bugs.python.org/issue?@action=redirect&bpo=18143)
.)

[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 has a new method, [`cert_store_stats()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.cert_store_stats "ssl.SSLContext.cert_store_stats")
, that reports the number of loaded `X.509` certs, `X.509 CA` certs, and certificate revocation lists (`crl`s), as well as a [`get_ca_certs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.get_ca_certs "ssl.SSLContext.get_ca_certs")
 method that returns a list of the loaded `CA` certificates. (Contributed by Christian Heimes in [bpo-18147](https://bugs.python.org/issue?@action=redirect&bpo=18147)
.)

If OpenSSL 0.9.8 or later is available, [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 has a new attribute [`verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags")
 that can be used to control the certificate verification process by setting it to some combination of the new constants [`VERIFY_DEFAULT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_DEFAULT "ssl.VERIFY_DEFAULT")
, [`VERIFY_CRL_CHECK_LEAF`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_CRL_CHECK_LEAF "ssl.VERIFY_CRL_CHECK_LEAF")
, [`VERIFY_CRL_CHECK_CHAIN`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_CRL_CHECK_CHAIN "ssl.VERIFY_CRL_CHECK_CHAIN")
, or [`VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT")
. OpenSSL does not do any CRL verification by default. (Contributed by Christien Heimes in [bpo-8813](https://bugs.python.org/issue?@action=redirect&bpo=8813)
.)

New [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 method [`load_default_certs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs "ssl.SSLContext.load_default_certs")
 loads a set of default “certificate authority” (CA) certificates from default locations, which vary according to the platform. It can be used to load both TLS web server authentication certificates (`purpose=`[`SERVER_AUTH`](https://docs.python.org/3/library/ssl.html#ssl.Purpose.SERVER_AUTH "ssl.Purpose.SERVER_AUTH")
) for a client to use to verify a server, and certificates for a server to use in verifying client certificates (`purpose=`[`CLIENT_AUTH`](https://docs.python.org/3/library/ssl.html#ssl.Purpose.CLIENT_AUTH "ssl.Purpose.CLIENT_AUTH")
). (Contributed by Christian Heimes in [bpo-19292](https://bugs.python.org/issue?@action=redirect&bpo=19292)
.)

Two new windows-only functions, [`enum_certificates()`](https://docs.python.org/3/library/ssl.html#ssl.enum_certificates "ssl.enum_certificates")
 and [`enum_crls()`](https://docs.python.org/3/library/ssl.html#ssl.enum_crls "ssl.enum_crls")
 provide the ability to retrieve certificates, certificate information, and CRLs from the Windows cert store. (Contributed by Christian Heimes in [bpo-17134](https://bugs.python.org/issue?@action=redirect&bpo=17134)
.)

Support for server-side SNI (Server Name Indication) using the new [`ssl.SSLContext.set_servername_callback()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_servername_callback "ssl.SSLContext.set_servername_callback")
 method. (Contributed by Daniel Black in [bpo-8109](https://bugs.python.org/issue?@action=redirect&bpo=8109)
.)

The dictionary returned by [`SSLSocket.getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert")
 contains additional `X509v3` extension items: `crlDistributionPoints`, `calIssuers`, and `OCSP` URIs. (Contributed by Christian Heimes in [bpo-18379](https://bugs.python.org/issue?@action=redirect&bpo=18379)
.)

### stat[¶](https://docs.python.org/3/whatsnew/3.4.html#stat "Link to this heading")

The [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
 module is now backed by a C implementation in `_stat`. A C implementation is required as most of the values aren’t standardized and are platform-dependent. (Contributed by Christian Heimes in [bpo-11016](https://bugs.python.org/issue?@action=redirect&bpo=11016)
.)

The module supports new [`ST_MODE`](https://docs.python.org/3/library/stat.html#stat.ST_MODE "stat.ST_MODE")
 flags, [`S_IFDOOR`](https://docs.python.org/3/library/stat.html#stat.S_IFDOOR "stat.S_IFDOOR")
, [`S_IFPORT`](https://docs.python.org/3/library/stat.html#stat.S_IFPORT "stat.S_IFPORT")
, and [`S_IFWHT`](https://docs.python.org/3/library/stat.html#stat.S_IFWHT "stat.S_IFWHT")
. (Contributed by Christian Hiemes in [bpo-11016](https://bugs.python.org/issue?@action=redirect&bpo=11016)
.)

### struct[¶](https://docs.python.org/3/whatsnew/3.4.html#struct "Link to this heading")

New function [`iter_unpack`](https://docs.python.org/3/library/struct.html#struct.iter_unpack "struct.iter_unpack")
 and a new [`struct.Struct.iter_unpack()`](https://docs.python.org/3/library/struct.html#struct.Struct.iter_unpack "struct.Struct.iter_unpack")
 method on compiled formats provide streamed unpacking of a buffer containing repeated instances of a given format of data. (Contributed by Antoine Pitrou in [bpo-17804](https://bugs.python.org/issue?@action=redirect&bpo=17804)
.)

### subprocess[¶](https://docs.python.org/3/whatsnew/3.4.html#subprocess "Link to this heading")

[`check_output()`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output "subprocess.check_output")
 now accepts an _input_ argument that can be used to provide the contents of `stdin` for the command that is run. (Contributed by Zack Weinberg in [bpo-16624](https://bugs.python.org/issue?@action=redirect&bpo=16624)
.)

[`getoutput()`](https://docs.python.org/3/library/subprocess.html#subprocess.getoutput "subprocess.getoutput")
 and [`getstatusoutput()`](https://docs.python.org/3/library/subprocess.html#subprocess.getstatusoutput "subprocess.getstatusoutput")
 now work on Windows. This change was actually inadvertently made in 3.3.4. (Contributed by Tim Golden in [bpo-10197](https://bugs.python.org/issue?@action=redirect&bpo=10197)
.)

### sunau[¶](https://docs.python.org/3/whatsnew/3.4.html#sunau "Link to this heading")

The `getparams()` method now returns a namedtuple rather than a plain tuple. (Contributed by Claudiu Popa in [bpo-18901](https://bugs.python.org/issue?@action=redirect&bpo=18901)
.)

`sunau.open()` now supports the context management protocol: when used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block, the `close` method of the returned object will be called automatically at the end of the block. (Contributed by Serhiy Storchaka in [bpo-18878](https://bugs.python.org/issue?@action=redirect&bpo=18878)
.)

`AU_write.setsampwidth()` now supports 24 bit samples, thus adding support for writing 24 sample using the module. (Contributed by Serhiy Storchaka in [bpo-19261](https://bugs.python.org/issue?@action=redirect&bpo=19261)
.)

The `writeframesraw()` and `writeframes()` methods now accept any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311)
.)

### sys[¶](https://docs.python.org/3/whatsnew/3.4.html#sys "Link to this heading")

New function [`sys.getallocatedblocks()`](https://docs.python.org/3/library/sys.html#sys.getallocatedblocks "sys.getallocatedblocks")
 returns the current number of blocks allocated by the interpreter. (In CPython with the default `--with-pymalloc` setting, this is allocations made through the [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
 API.) This can be useful for tracking memory leaks, especially if automated via a test suite. (Contributed by Antoine Pitrou in [bpo-13390](https://bugs.python.org/issue?@action=redirect&bpo=13390)
.)

When the Python interpreter starts in [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive)
, it checks for an [`__interactivehook__`](https://docs.python.org/3/library/sys.html#sys.__interactivehook__ "sys.__interactivehook__")
 attribute on the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module. If the attribute exists, its value is called with no arguments just before interactive mode is started. The check is made after the [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP)
 file is read, so it can be set there. The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module [sets it](https://docs.python.org/3/library/site.html#rlcompleter-config)
 to a function that enables tab completion and history saving (in `~/.python-history`) if the platform supports [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
. If you do not want this (new) behavior, you can override it in `PYTHONSTARTUP`, [`sitecustomize`](https://docs.python.org/3/library/site.html#module-sitecustomize "sitecustomize")
, or [`usercustomize`](https://docs.python.org/3/library/site.html#module-usercustomize "usercustomize")
 by deleting this attribute from `sys` (or setting it to some other callable). (Contributed by Éric Araujo and Antoine Pitrou in [bpo-5845](https://bugs.python.org/issue?@action=redirect&bpo=5845)
.)

### tarfile[¶](https://docs.python.org/3/whatsnew/3.4.html#tarfile "Link to this heading")

The [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
 module now supports a simple [Command-Line Interface](https://docs.python.org/3/library/tarfile.html#tarfile-commandline)
 when called as a script directly or via `-m`. This can be used to create and extract tarfile archives. (Contributed by Berker Peksag in [bpo-13477](https://bugs.python.org/issue?@action=redirect&bpo=13477)
.)

### textwrap[¶](https://docs.python.org/3/whatsnew/3.4.html#textwrap "Link to this heading")

The [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper")
 class has two new attributes/constructor arguments: [`max_lines`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.max_lines "textwrap.TextWrapper.max_lines")
, which limits the number of lines in the output, and [`placeholder`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.placeholder "textwrap.TextWrapper.placeholder")
, which is a string that will appear at the end of the output if it has been truncated because of _max\_lines_. Building on these capabilities, a new convenience function [`shorten()`](https://docs.python.org/3/library/textwrap.html#textwrap.shorten "textwrap.shorten")
 collapses all of the whitespace in the input to single spaces and produces a single line of a given _width_ that ends with the _placeholder_ (by default, `[...]`). (Contributed by Antoine Pitrou and Serhiy Storchaka in [bpo-18585](https://bugs.python.org/issue?@action=redirect&bpo=18585)
 and [bpo-18725](https://bugs.python.org/issue?@action=redirect&bpo=18725)
.)

### threading[¶](https://docs.python.org/3/whatsnew/3.4.html#threading "Link to this heading")

The [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
 object representing the main thread can be obtained from the new [`main_thread()`](https://docs.python.org/3/library/threading.html#threading.main_thread "threading.main_thread")
 function. In normal conditions this will be the thread from which the Python interpreter was started. (Contributed by Andrew Svetlov in [bpo-18882](https://bugs.python.org/issue?@action=redirect&bpo=18882)
.)

### traceback[¶](https://docs.python.org/3/whatsnew/3.4.html#traceback "Link to this heading")

A new [`traceback.clear_frames()`](https://docs.python.org/3/library/traceback.html#traceback.clear_frames "traceback.clear_frames")
 function takes a traceback object and clears the local variables in all of the frames it references, reducing the amount of memory consumed. (Contributed by Andrew Kuchling in [bpo-1565525](https://bugs.python.org/issue?@action=redirect&bpo=1565525)
.)

### types[¶](https://docs.python.org/3/whatsnew/3.4.html#types "Link to this heading")

A new [`DynamicClassAttribute()`](https://docs.python.org/3/library/types.html#types.DynamicClassAttribute "types.DynamicClassAttribute")
 descriptor provides a way to define an attribute that acts normally when looked up through an instance object, but which is routed to the _class_ `__getattr__` when looked up through the class. This allows one to have properties active on a class, and have virtual attributes on the class with the same name (see [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
 for an example). (Contributed by Ethan Furman in [bpo-19030](https://bugs.python.org/issue?@action=redirect&bpo=19030)
.)

### urllib[¶](https://docs.python.org/3/whatsnew/3.4.html#urllib "Link to this heading")

[`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
 now supports `data:` URLs via the [`DataHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.DataHandler "urllib.request.DataHandler")
 class. (Contributed by Mathias Panzenböck in [bpo-16423](https://bugs.python.org/issue?@action=redirect&bpo=16423)
.)

The http method that will be used by a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request")
 class can now be specified by setting a [`method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "urllib.request.Request.method")
 class attribute on the subclass. (Contributed by Jason R Coombs in [bpo-18978](https://bugs.python.org/issue?@action=redirect&bpo=18978)
.)

[`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request")
 objects are now reusable: if the [`full_url`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.full_url "urllib.request.Request.full_url")
 or [`data`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.data "urllib.request.Request.data")
 attributes are modified, all relevant internal properties are updated. This means, for example, that it is now possible to use the same `Request` object in more than one [`OpenerDirector.open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.open "urllib.request.OpenerDirector.open")
 call with different _data_ arguments, or to modify a `Request`‘s `url` rather than recomputing it from scratch. There is also a new [`remove_header()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.remove_header "urllib.request.Request.remove_header")
 method that can be used to remove headers from a `Request`. (Contributed by Alexey Kachayev in [bpo-16464](https://bugs.python.org/issue?@action=redirect&bpo=16464)
, Daniel Wozniak in [bpo-17485](https://bugs.python.org/issue?@action=redirect&bpo=17485)
, and Damien Brecht and Senthil Kumaran in [bpo-17272](https://bugs.python.org/issue?@action=redirect&bpo=17272)
.)

[`HTTPError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "urllib.error.HTTPError")
 objects now have a [`headers`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError.headers "urllib.error.HTTPError.headers")
 attribute that provides access to the HTTP response headers associated with the error. (Contributed by Berker Peksag in [bpo-15701](https://bugs.python.org/issue?@action=redirect&bpo=15701)
.)

### unittest[¶](https://docs.python.org/3/whatsnew/3.4.html#unittest "Link to this heading")

The [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")
 class has a new method, [`subTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest "unittest.TestCase.subTest")
, that produces a context manager whose [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block becomes a “sub-test”. This context manager allows a test method to dynamically generate subtests by, say, calling the `subTest` context manager inside a loop. A single test method can thereby produce an indefinite number of separately identified and separately counted tests, all of which will run even if one or more of them fail. For example:

Copy

class NumbersTest(unittest.TestCase):
    def test\_even(self):
        for i in range(6):
            with self.subTest(i\=i):
                self.assertEqual(i % 2, 0)

will result in six subtests, each identified in the unittest verbose output with a label consisting of the variable name `i` and a particular value for that variable (`i=0`, `i=1`, etc). See [Distinguishing test iterations using subtests](https://docs.python.org/3/library/unittest.html#subtests)
 for the full version of this example. (Contributed by Antoine Pitrou in [bpo-16997](https://bugs.python.org/issue?@action=redirect&bpo=16997)
.)

[`unittest.main()`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main")
 now accepts an iterable of test names for _defaultTest_, where previously it only accepted a single test name as a string. (Contributed by Jyrki Pulliainen in [bpo-15132](https://bugs.python.org/issue?@action=redirect&bpo=15132)
.)

If [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest")
 is raised during test discovery (that is, at the module level in the test file), it is now reported as a skip instead of an error. (Contributed by Zach Ware in [bpo-16935](https://bugs.python.org/issue?@action=redirect&bpo=16935)
.)

[`discover()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "unittest.TestLoader.discover")
 now sorts the discovered files to provide consistent test ordering. (Contributed by Martin Melin and Jeff Ramnani in [bpo-16709](https://bugs.python.org/issue?@action=redirect&bpo=16709)
.)

[`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite")
 now drops references to tests as soon as the test has been run, if the test is successful. On Python interpreters that do garbage collection, this allows the tests to be garbage collected if nothing else is holding a reference to the test. It is possible to override this behavior by creating a `TestSuite` subclass that defines a custom `_removeTestAtIndex` method. (Contributed by Tom Wardill, Matt McClure, and Andrew Svetlov in [bpo-11798](https://bugs.python.org/issue?@action=redirect&bpo=11798)
.)

A new test assertion context-manager, [`assertLogs()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs")
, will ensure that a given block of code emits a log message using the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
 module. By default the message can come from any logger and have a priority of `INFO` or higher, but both the logger name and an alternative minimum logging level may be specified. The object returned by the context manager can be queried for the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord")
s and/or formatted messages that were logged. (Contributed by Antoine Pitrou in [bpo-18937](https://bugs.python.org/issue?@action=redirect&bpo=18937)
.)

Test discovery now works with namespace packages (Contributed by Claudiu Popa in [bpo-17457](https://bugs.python.org/issue?@action=redirect&bpo=17457)
.)

[`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock "unittest.mock: Mock object library.")
 objects now inspect their specification signatures when matching calls, which means an argument can now be matched by either position or name, instead of only by position. (Contributed by Antoine Pitrou in [bpo-17015](https://bugs.python.org/issue?@action=redirect&bpo=17015)
.)

[`mock_open()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.mock_open "unittest.mock.mock_open")
 objects now have `readline` and `readlines` methods. (Contributed by Toshio Kuratomi in [bpo-17467](https://bugs.python.org/issue?@action=redirect&bpo=17467)
.)

### venv[¶](https://docs.python.org/3/whatsnew/3.4.html#venv "Link to this heading")

[`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.")
 now includes activation scripts for the `csh` and `fish` shells. (Contributed by Andrew Svetlov in [bpo-15417](https://bugs.python.org/issue?@action=redirect&bpo=15417)
.)

[`EnvBuilder`](https://docs.python.org/3/library/venv.html#venv.EnvBuilder "venv.EnvBuilder")
 and the [`create()`](https://docs.python.org/3/library/venv.html#venv.create "venv.create")
 convenience function take a new keyword argument _with\_pip_, which defaults to `False`, that controls whether or not `EnvBuilder` ensures that `pip` is installed in the virtual environment. (Contributed by Nick Coghlan in [bpo-19552](https://bugs.python.org/issue?@action=redirect&bpo=19552)
 as part of the [**PEP 453**](https://peps.python.org/pep-0453/)
 implementation.)

### wave[¶](https://docs.python.org/3/whatsnew/3.4.html#wave "Link to this heading")

The [`getparams()`](https://docs.python.org/3/library/wave.html#wave.Wave_read.getparams "wave.Wave_read.getparams")
 method now returns a namedtuple rather than a plain tuple. (Contributed by Claudiu Popa in [bpo-17487](https://bugs.python.org/issue?@action=redirect&bpo=17487)
.)

[`wave.open()`](https://docs.python.org/3/library/wave.html#wave.open "wave.open")
 now supports the context management protocol. (Contributed by Claudiu Popa in [bpo-17616](https://bugs.python.org/issue?@action=redirect&bpo=17616)
.)

[`wave`](https://docs.python.org/3/library/wave.html#module-wave "wave: Provide an interface to the WAV sound format.")
 can now [write output to unseekable files](https://docs.python.org/3/library/wave.html#wave-write-objects)
. (Contributed by David Jones, Guilherme Polo, and Serhiy Storchaka in [bpo-5202](https://bugs.python.org/issue?@action=redirect&bpo=5202)
.)

The [`writeframesraw()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframesraw "wave.Wave_write.writeframesraw")
 and [`writeframes()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.writeframes "wave.Wave_write.writeframes")
 methods now accept any [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311)
.)

### weakref[¶](https://docs.python.org/3/whatsnew/3.4.html#weakref "Link to this heading")

New [`WeakMethod`](https://docs.python.org/3/library/weakref.html#weakref.WeakMethod "weakref.WeakMethod")
 class simulates weak references to bound methods. (Contributed by Antoine Pitrou in [bpo-14631](https://bugs.python.org/issue?@action=redirect&bpo=14631)
.)

New [`finalize`](https://docs.python.org/3/library/weakref.html#weakref.finalize "weakref.finalize")
 class makes it possible to register a callback to be invoked when an object is garbage collected, without needing to carefully manage the lifecycle of the weak reference itself. (Contributed by Richard Oudkerk in [bpo-15528](https://bugs.python.org/issue?@action=redirect&bpo=15528)
.)

The callback, if any, associated with a [`ref`](https://docs.python.org/3/library/weakref.html#weakref.ref "weakref.ref")
 is now exposed via the [`__callback__`](https://docs.python.org/3/library/weakref.html#weakref.ref.__callback__ "weakref.ref.__callback__")
 attribute. (Contributed by Mark Dickinson in [bpo-17643](https://bugs.python.org/issue?@action=redirect&bpo=17643)
.)

### xml.etree[¶](https://docs.python.org/3/whatsnew/3.4.html#xml-etree "Link to this heading")

A new parser, [`XMLPullParser`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser "xml.etree.ElementTree.XMLPullParser")
, allows a non-blocking applications to parse XML documents. An example can be seen at [Pull API for non-blocking parsing](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-pull-parsing)
. (Contributed by Antoine Pitrou in [bpo-17741](https://bugs.python.org/issue?@action=redirect&bpo=17741)
.)

The [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
 [`tostring()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring "xml.etree.ElementTree.tostring")
 and [`tostringlist()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostringlist "xml.etree.ElementTree.tostringlist")
 functions, and the [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree")
 [`write()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write "xml.etree.ElementTree.ElementTree.write")
 method, now have a _short\_empty\_elements_ [keyword-only parameter](https://docs.python.org/3/glossary.html#keyword-only-parameter)
 providing control over whether elements with no content are written in abbreviated (`<tag />`) or expanded (`<tag></tag>`) form. (Contributed by Ariel Poliak and Serhiy Storchaka in [bpo-14377](https://bugs.python.org/issue?@action=redirect&bpo=14377)
.)

### zipfile[¶](https://docs.python.org/3/whatsnew/3.4.html#zipfile "Link to this heading")

The [`writepy()`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile.writepy "zipfile.PyZipFile.writepy")
 method of the [`PyZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "zipfile.PyZipFile")
 class has a new _filterfunc_ option that can be used to control which directories and files are added to the archive. For example, this could be used to exclude test files from the archive. (Contributed by Christian Tismer in [bpo-19274](https://bugs.python.org/issue?@action=redirect&bpo=19274)
.)

The _allowZip64_ parameter to [`ZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile "zipfile.ZipFile")
 and [`PyZipFile`](https://docs.python.org/3/library/zipfile.html#zipfile.PyZipFile "zipfile.PyZipFile")
 is now `True` by default. (Contributed by William Mallard in [bpo-17201](https://bugs.python.org/issue?@action=redirect&bpo=17201)
.)

CPython Implementation Changes[¶](https://docs.python.org/3/whatsnew/3.4.html#cpython-implementation-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

### PEP 445: Customization of CPython Memory Allocators[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-445-customization-of-cpython-memory-allocators "Link to this heading")

[**PEP 445**](https://peps.python.org/pep-0445/)
 adds new C level interfaces to customize memory allocation in the CPython interpreter.

See also

[**PEP 445**](https://peps.python.org/pep-0445/)
 – Add new APIs to customize Python memory allocators

PEP written and implemented by Victor Stinner.

### PEP 442: Safe Object Finalization[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-442-safe-object-finalization "Link to this heading")

[**PEP 442**](https://peps.python.org/pep-0442/)
 removes the current limitations and quirks of object finalization in CPython. With it, objects with [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__")
 methods, as well as generators with [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clauses, can be finalized when they are part of a reference cycle.

As part of this change, module globals are no longer forcibly set to [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 during interpreter shutdown in most cases, instead relying on the normal operation of the cyclic garbage collector. This avoids a whole class of interpreter-shutdown-time errors, usually involving `__del__` methods, that have plagued Python since the cyclic GC was first introduced.

See also

[**PEP 442**](https://peps.python.org/pep-0442/)
 – Safe object finalization

PEP written and implemented by Antoine Pitrou.

### PEP 456: Secure and Interchangeable Hash Algorithm[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-456-secure-and-interchangeable-hash-algorithm "Link to this heading")

[**PEP 456**](https://peps.python.org/pep-0456/)
 follows up on earlier security fix work done on Python’s hash algorithm to address certain DOS attacks to which public facing APIs backed by dictionary lookups may be subject. (See [bpo-14621](https://bugs.python.org/issue?@action=redirect&bpo=14621)
 for the start of the current round of improvements.) The PEP unifies CPython’s hash code to make it easier for a packager to substitute a different hash algorithm, and switches Python’s default implementation to a SipHash implementation on platforms that have a 64 bit data type. Any performance differences in comparison with the older FNV algorithm are trivial.

The PEP adds additional fields to the [`sys.hash_info`](https://docs.python.org/3/library/sys.html#sys.hash_info "sys.hash_info")
 named tuple to describe the hash algorithm in use by the currently executing binary. Otherwise, the PEP does not alter any existing CPython APIs.

### PEP 436: Argument Clinic[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-436-argument-clinic "Link to this heading")

“Argument Clinic” ([**PEP 436**](https://peps.python.org/pep-0436/)
) is now part of the CPython build process and can be used to simplify the process of defining and maintaining accurate signatures for builtins and standard library extension modules implemented in C.

Some standard library extension modules have been converted to use Argument Clinic in Python 3.4, and [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 and [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
 have been updated accordingly.

It is expected that signature metadata for programmatic introspection will be added to additional callables implemented in C as part of Python 3.4 maintenance releases.

Note

The Argument Clinic PEP is not fully up to date with the state of the implementation. This has been deemed acceptable by the release manager and core development team in this case, as Argument Clinic will not be made available as a public API for third party use in Python 3.4.

See also

[**PEP 436**](https://peps.python.org/pep-0436/)
 – The Argument Clinic DSL

PEP written and implemented by Larry Hastings.

### Other Build and C API Changes[¶](https://docs.python.org/3/whatsnew/3.4.html#other-build-and-c-api-changes "Link to this heading")

*   The new [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
     function has been added to the stable ABI, allowing retrieval of function pointers from named type slots when using the limited API. (Contributed by Martin von Löwis in [bpo-17162](https://bugs.python.org/issue?@action=redirect&bpo=17162)
    .)
    
*   The new `Py_SetStandardStreamEncoding()` pre-initialization API allows applications embedding the CPython interpreter to reliably force a particular encoding and error handler for the standard streams. (Contributed by Bastien Montagne and Nick Coghlan in [bpo-16129](https://bugs.python.org/issue?@action=redirect&bpo=16129)
    .)
    
*   Most Python C APIs that don’t mutate string arguments are now correctly marked as accepting `const char *` rather than `char *`. (Contributed by Serhiy Storchaka in [bpo-1772673](https://bugs.python.org/issue?@action=redirect&bpo=1772673)
    .)
    
*   A new shell version of `python-config` can be used even when a python interpreter is not available (for example, in cross compilation scenarios).
    
*   [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
     now supports width and precision specifications for `%s`, `%A`, `%U`, `%V`, `%S`, and `%R`. (Contributed by Ysj Ray and Victor Stinner in [bpo-7330](https://bugs.python.org/issue?@action=redirect&bpo=7330)
    .)
    
*   New function [`PyStructSequence_InitType2()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_InitType2 "PyStructSequence_InitType2")
     supplements the existing [`PyStructSequence_InitType()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_InitType "PyStructSequence_InitType")
     function. The difference is that it returns `0` on success and `-1` on failure.
    
*   The CPython source can now be compiled using the address sanity checking features of recent versions of GCC and clang: the false alarms in the small object allocator have been silenced. (Contributed by Dhiru Kholia in [bpo-18596](https://bugs.python.org/issue?@action=redirect&bpo=18596)
    .)
    
*   The Windows build now uses [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization)
     and [Data Execution Prevention](https://en.wikipedia.org/wiki/Data_Execution_Prevention)
    . (Contributed by Christian Heimes in [bpo-16632](https://bugs.python.org/issue?@action=redirect&bpo=16632)
    .)
    
*   New function [`PyObject_LengthHint()`](https://docs.python.org/3/c-api/object.html#c.PyObject_LengthHint "PyObject_LengthHint")
     is the C API equivalent of [`operator.length_hint()`](https://docs.python.org/3/library/operator.html#operator.length_hint "operator.length_hint")
    . (Contributed by Armin Ronacher in [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148)
    .)
    

### Other Improvements[¶](https://docs.python.org/3/whatsnew/3.4.html#other-improvements "Link to this heading")

*   The [python](https://docs.python.org/3/using/cmdline.html#using-on-cmdline)
     command has a new [option](https://docs.python.org/3/using/cmdline.html#using-on-misc-options)
    , `-I`, which causes it to run in “isolated mode”, which means that [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
     contains neither the script’s directory nor the user’s `site-packages` directory, and all `PYTHON*` environment variables are ignored (it implies both `-s` and `-E`). Other restrictions may also be applied in the future, with the goal being to isolate the execution of a script from the user’s environment. This is appropriate, for example, when Python is used to run a system script. On most POSIX systems it can and should be used in the `#!` line of system scripts. (Contributed by Christian Heimes in [bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)
    .)
    
*   Tab-completion is now enabled by default in the interactive interpreter on systems that support [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
    . History is also enabled by default, and is written to (and read from) the file `~/.python-history`. (Contributed by Antoine Pitrou and Éric Araujo in [bpo-5845](https://bugs.python.org/issue?@action=redirect&bpo=5845)
    .)
    
*   Invoking the Python interpreter with `--version` now outputs the version to standard output instead of standard error ([bpo-18338](https://bugs.python.org/issue?@action=redirect&bpo=18338)
    ). Similar changes were made to [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
     ([bpo-18920](https://bugs.python.org/issue?@action=redirect&bpo=18920)
    ) and other modules that have script-like invocation capabilities ([bpo-18922](https://bugs.python.org/issue?@action=redirect&bpo=18922)
    ).
    
*   The CPython Windows installer now adds `.py` to the `PATHEXT` variable when extensions are registered, allowing users to run a python script at the windows command prompt by just typing its name without the `.py` extension. (Contributed by Paul Moore in [bpo-18569](https://bugs.python.org/issue?@action=redirect&bpo=18569)
    .)
    
*   A new `make` target [coverage-report](https://devguide.python.org/coverage/#measuring-coverage-of-c-code-with-gcov-and-lcov)
     will build python, run the test suite, and generate an HTML coverage report for the C codebase using `gcov` and [lcov](https://github.com/linux-test-project/lcov)
    .
    
*   The `-R` option to the [python regression test suite](https://docs.python.org/3/library/test.html#regrtest)
     now also checks for memory allocation leaks, using [`sys.getallocatedblocks()`](https://docs.python.org/3/library/sys.html#sys.getallocatedblocks "sys.getallocatedblocks")
    . (Contributed by Antoine Pitrou in [bpo-13390](https://bugs.python.org/issue?@action=redirect&bpo=13390)
    .)
    
*   `python -m` now works with namespace packages.
    
*   The [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
     module is now implemented in C, which means it gets the values for its constants from the C header files, instead of having the values hard-coded in the python module as was previously the case.
    
*   Loading multiple python modules from a single OS module (`.so`, `.dll`) now works correctly (previously it silently returned the first python module in the file). (Contributed by Václav Šmilauer in [bpo-16421](https://bugs.python.org/issue?@action=redirect&bpo=16421)
    .)
    
*   A new opcode, `LOAD_CLASSDEREF`, has been added to fix a bug in the loading of free variables in class bodies that could be triggered by certain uses of [\_\_prepare\_\_](https://docs.python.org/3/reference/datamodel.html#prepare)
    . (Contributed by Benjamin Peterson in [bpo-17853](https://bugs.python.org/issue?@action=redirect&bpo=17853)
    .)
    
*   A number of MemoryError-related crashes were identified and fixed by Victor Stinner using his [**PEP 445**](https://peps.python.org/pep-0445/)
    \-based `pyfailmalloc` tool ([bpo-18408](https://bugs.python.org/issue?@action=redirect&bpo=18408)
    , [bpo-18520](https://bugs.python.org/issue?@action=redirect&bpo=18520)
    ).
    
*   The `pyvenv` command now accepts a `--copies` option to use copies rather than symlinks even on systems where symlinks are the default. (Contributed by Vinay Sajip in [bpo-18807](https://bugs.python.org/issue?@action=redirect&bpo=18807)
    .)
    
*   The `pyvenv` command also accepts a `--without-pip` option to suppress the otherwise-automatic bootstrapping of pip into the virtual environment. (Contributed by Nick Coghlan in [bpo-19552](https://bugs.python.org/issue?@action=redirect&bpo=19552)
     as part of the [**PEP 453**](https://peps.python.org/pep-0453/)
     implementation.)
    
*   The encoding name is now optional in the value set for the [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING)
     environment variable. This makes it possible to set just the error handler, without changing the default encoding. (Contributed by Serhiy Storchaka in [bpo-18818](https://bugs.python.org/issue?@action=redirect&bpo=18818)
    .)
    
*   The [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
    , [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
    , and [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")
     module `open` functions now support `x` (exclusive creation) mode. (Contributed by Tim Heaney and Vajrasky Kok in [bpo-19201](https://bugs.python.org/issue?@action=redirect&bpo=19201)
    , [bpo-19222](https://bugs.python.org/issue?@action=redirect&bpo=19222)
    , and [bpo-19223](https://bugs.python.org/issue?@action=redirect&bpo=19223)
    .)
    

### Significant Optimizations[¶](https://docs.python.org/3/whatsnew/3.4.html#significant-optimizations "Link to this heading")

*   The UTF-32 decoder is now 3x to 4x faster. (Contributed by Serhiy Storchaka in [bpo-14625](https://bugs.python.org/issue?@action=redirect&bpo=14625)
    .)
    
*   The cost of hash collisions for sets is now reduced. Each hash table probe now checks a series of consecutive, adjacent key/hash pairs before continuing to make random probes through the hash table. This exploits cache locality to make collision resolution less expensive. The collision resolution scheme can be described as a hybrid of linear probing and open addressing. The number of additional linear probes defaults to nine. This can be changed at compile-time by defining LINEAR\_PROBES to be any value. Set LINEAR\_PROBES=0 to turn-off linear probing entirely. (Contributed by Raymond Hettinger in [bpo-18771](https://bugs.python.org/issue?@action=redirect&bpo=18771)
    .)
    
*   The interpreter starts about 30% faster. A couple of measures lead to the speedup. The interpreter loads fewer modules on startup, e.g. the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
    , [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
     and [`locale`](https://docs.python.org/3/library/locale.html#module-locale "locale: Internationalization services.")
     modules and their dependencies are no longer imported by default. The marshal module has been improved to load compiled Python code faster. (Contributed by Antoine Pitrou, Christian Heimes and Victor Stinner in [bpo-19219](https://bugs.python.org/issue?@action=redirect&bpo=19219)
    , [bpo-19218](https://bugs.python.org/issue?@action=redirect&bpo=19218)
    , [bpo-19209](https://bugs.python.org/issue?@action=redirect&bpo=19209)
    , [bpo-19205](https://bugs.python.org/issue?@action=redirect&bpo=19205)
     and [bpo-9548](https://bugs.python.org/issue?@action=redirect&bpo=9548)
    .)
    
*   [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
     is now as fast or faster than the Python2 version for most cases. [`lzma.LZMAFile`](https://docs.python.org/3/library/lzma.html#lzma.LZMAFile "lzma.LZMAFile")
     has also been optimized. (Contributed by Serhiy Storchaka and Nadeem Vawda in [bpo-16034](https://bugs.python.org/issue?@action=redirect&bpo=16034)
    .)
    
*   [`random.getrandbits()`](https://docs.python.org/3/library/random.html#random.getrandbits "random.getrandbits")
     is 20%-40% faster for small integers (the most common use case). (Contributed by Serhiy Storchaka in [bpo-16674](https://bugs.python.org/issue?@action=redirect&bpo=16674)
    .)
    
*   By taking advantage of the new storage format for strings, pickling of strings is now significantly faster. (Contributed by Victor Stinner and Antoine Pitrou in [bpo-15596](https://bugs.python.org/issue?@action=redirect&bpo=15596)
    .)
    
*   A performance issue in `io.FileIO.readall()` has been solved. This particularly affects Windows, and significantly speeds up the case of piping significant amounts of data through [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
    . (Contributed by Richard Oudkerk in [bpo-15758](https://bugs.python.org/issue?@action=redirect&bpo=15758)
    .)
    
*   [`html.escape()`](https://docs.python.org/3/library/html.html#html.escape "html.escape")
     is now 10x faster. (Contributed by Matt Bryant in [bpo-18020](https://bugs.python.org/issue?@action=redirect&bpo=18020)
    .)
    
*   On Windows, the native `VirtualAlloc` is now used instead of the CRT `malloc` in `obmalloc`. Artificial benchmarks show about a 3% memory savings.
    
*   [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom")
     now uses a lazily opened persistent file descriptor so as to avoid using many file descriptors when run in parallel from multiple threads. (Contributed by Antoine Pitrou in [bpo-18756](https://bugs.python.org/issue?@action=redirect&bpo=18756)
    .)
    

Deprecated[¶](https://docs.python.org/3/whatsnew/3.4.html#deprecated "Link to this heading")

---------------------------------------------------------------------------------------------

This section covers various APIs and other features that have been deprecated in Python 3.4, and will be removed in Python 3.5 or later. In most (but not all) cases, using the deprecated APIs will produce a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
 when the interpreter is run with deprecation warnings enabled (for example, by using `-Wd`).

### Deprecations in the Python API[¶](https://docs.python.org/3/whatsnew/3.4.html#deprecations-in-the-python-api "Link to this heading")

*   As mentioned in [PEP 451: A ModuleSpec Type for the Import System](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-451)
    , a number of [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
     methods and functions are deprecated: `importlib.find_loader()` is replaced by [`importlib.util.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "importlib.util.find_spec")
    ; `importlib.machinery.PathFinder.find_module()` is replaced by [`importlib.machinery.PathFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.find_spec "importlib.machinery.PathFinder.find_spec")
    ; `importlib.abc.MetaPathFinder.find_module()` is replaced by [`importlib.abc.MetaPathFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec")
    ; `importlib.abc.PathEntryFinder.find_loader()` and `find_module()` are replaced by [`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec "importlib.abc.PathEntryFinder.find_spec")
    ; all of the `_xxx_Loader` ABC `load_module` methods (`importlib.abc.Loader.load_module`, `importlib.abc.InspectLoader.load_module`, `importlib.abc.FileLoader.load_module`, `importlib.abc.SourceLoader.load_module`) should no longer be implemented, instead loaders should implement an `exec_module` method ([`importlib.abc.Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module")
    , [`importlib.abc.InspectLoader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.exec_module "importlib.abc.InspectLoader.exec_module")
     [`importlib.abc.SourceLoader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.exec_module "importlib.abc.SourceLoader.exec_module")
    ) and let the import system take care of the rest; and `importlib.abc.Loader.module_repr()`, `importlib.util.module_for_loader()`, `importlib.util.set_loader()`, and `importlib.util.set_package()` are no longer needed because their functions are now handled automatically by the import system.
    
*   The `imp` module is pending deprecation. To keep compatibility with Python 2/3 code bases, the module’s removal is currently not scheduled.
    
*   The `formatter` module is pending deprecation and is slated for removal in Python 3.6.
    
*   `MD5` as the default _digestmod_ for the [`hmac.new()`](https://docs.python.org/3/library/hmac.html#hmac.new "hmac.new")
     function is deprecated. Python 3.6 will require an explicit digest name or constructor as _digestmod_ argument.
    
*   The internal `Netrc` class in the [`ftplib`](https://docs.python.org/3/library/ftplib.html#module-ftplib "ftplib: FTP protocol client (requires sockets).")
     module has been documented as deprecated in its docstring for quite some time. It now emits a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
     and will be removed completely in Python 3.5.
    
*   The undocumented _endtime_ argument to [`subprocess.Popen.wait()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "subprocess.Popen.wait")
     should not have been exposed and is hopefully not in use; it is deprecated and will mostly likely be removed in Python 3.5.
    
*   The _strict_ argument of [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
     is deprecated.
    
*   The [`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.")
     `readPlist()`, `writePlist()`, `readPlistFromBytes()`, and `writePlistToBytes()` functions are deprecated in favor of the corresponding new functions [`load()`](https://docs.python.org/3/library/plistlib.html#plistlib.load "plistlib.load")
    , [`dump()`](https://docs.python.org/3/library/plistlib.html#plistlib.dump "plistlib.dump")
    , [`loads()`](https://docs.python.org/3/library/plistlib.html#plistlib.loads "plistlib.loads")
    , and [`dumps()`](https://docs.python.org/3/library/plistlib.html#plistlib.dumps "plistlib.dumps")
    . `Data()` is deprecated in favor of just using the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     constructor.
    
*   The [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
     key `SO` is deprecated, it has been replaced by `EXT_SUFFIX`.
    
*   The `U` mode accepted by various `open` functions is deprecated. In Python3 it does not do anything useful, and should be replaced by appropriate uses of [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
     (if needed) and its _newline_ argument.
    
*   The _parser_ argument of [`xml.etree.ElementTree.iterparse()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse "xml.etree.ElementTree.iterparse")
     has been deprecated, as has the _html_ argument of [`XMLParser()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser "xml.etree.ElementTree.XMLParser")
    . To prepare for the removal of the latter, all arguments to `XMLParser` should be passed by keyword.
    

### Deprecated Features[¶](https://docs.python.org/3/whatsnew/3.4.html#deprecated-features "Link to this heading")

*   Running [IDLE — Python editor and shell](https://docs.python.org/3/library/idle.html#idle)
     with the `-n` flag (no subprocess) is deprecated. However, the feature will not be removed until [bpo-18823](https://bugs.python.org/issue?@action=redirect&bpo=18823)
     is resolved.
    
*   The site module adding a “site-python” directory to sys.path, if it exists, is deprecated ([bpo-19375](https://bugs.python.org/issue?@action=redirect&bpo=19375)
    ).
    

Removed[¶](https://docs.python.org/3/whatsnew/3.4.html#removed "Link to this heading")

---------------------------------------------------------------------------------------

### Operating Systems No Longer Supported[¶](https://docs.python.org/3/whatsnew/3.4.html#operating-systems-no-longer-supported "Link to this heading")

Support for the following operating systems has been removed from the source and build tools:

*   OS/2 ([bpo-16135](https://bugs.python.org/issue?@action=redirect&bpo=16135)
    ).
    
*   Windows 2000 (changeset e52df05b496a).
    
*   Windows systems where `COMSPEC` points to `command.com` ([bpo-14470](https://bugs.python.org/issue?@action=redirect&bpo=14470)
    ).
    
*   VMS ([bpo-16136](https://bugs.python.org/issue?@action=redirect&bpo=16136)
    ).
    

### API and Feature Removals[¶](https://docs.python.org/3/whatsnew/3.4.html#api-and-feature-removals "Link to this heading")

The following obsolete and previously deprecated APIs and features have been removed:

*   The unmaintained `Misc/TextMate` and `Misc/vim` directories have been removed (see the [devguide](https://devguide.python.org/)
     for suggestions on what to use instead).
    
*   The `SO` makefile macro is removed (it was replaced by the `SHLIB_SUFFIX` and `EXT_SUFFIX` macros) ([bpo-16754](https://bugs.python.org/issue?@action=redirect&bpo=16754)
    ).
    
*   The `PyThreadState.tick_counter` field has been removed; its value has been meaningless since Python 3.2, when the “new GIL” was introduced ([bpo-19199](https://bugs.python.org/issue?@action=redirect&bpo=19199)
    ).
    
*   `PyLoader` and `PyPycLoader` have been removed from [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
    . (Contributed by Taras Lyapun in [bpo-15641](https://bugs.python.org/issue?@action=redirect&bpo=15641)
    .)
    
*   The _strict_ argument to [`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection")
     and [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
     has been removed. HTTP 0.9-style “Simple Responses” are no longer supported.
    
*   The deprecated [`urllib.request.Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request")
     getter and setter methods `add_data`, `has_data`, `get_data`, `get_type`, `get_host`, `get_selector`, `set_proxy`, `get_origin_req_host`, and `is_unverifiable` have been removed (use direct attribute access instead).
    
*   Support for loading the deprecated `TYPE_INT64` has been removed from [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
    . (Contributed by Dan Riti in [bpo-15480](https://bugs.python.org/issue?@action=redirect&bpo=15480)
    .)
    
*   [`inspect.Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature")
    : positional-only parameters are now required to have a valid name.
    
*   [`object.__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__")
     no longer accepts non-empty format strings, it now raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     instead. Using a non-empty string has been deprecated since Python 3.2. This change has been made to prevent a situation where previously working (but incorrect) code would start failing if an object gained a \_\_format\_\_ method, which means that your code may now raise a `TypeError` if you are using an `'s'` format code with objects that do not have a \_\_format\_\_ method that handles it. See [bpo-7994](https://bugs.python.org/issue?@action=redirect&bpo=7994)
     for background.
    
*   `difflib.SequenceMatcher.isbjunk()` and `difflib.SequenceMatcher.isbpopular()` were deprecated in 3.2, and have now been removed: use `x in sm.bjunk` and `x in sm.bpopular`, where _sm_ is a [`SequenceMatcher`](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher "difflib.SequenceMatcher")
     object ([bpo-13248](https://bugs.python.org/issue?@action=redirect&bpo=13248)
    ).
    

### Code Cleanups[¶](https://docs.python.org/3/whatsnew/3.4.html#code-cleanups "Link to this heading")

*   The unused and undocumented internal `Scanner` class has been removed from the [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
     module.
    
*   The private and effectively unused `_gestalt` module has been removed, along with the private [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
     functions `_mac_ver_lookup`, `_mac_ver_gstalt`, and `_bcd2str`, which would only have ever been called on badly broken OSX systems (see [bpo-18393](https://bugs.python.org/issue?@action=redirect&bpo=18393)
    ).
    
*   The hardcoded copies of certain [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
     constants that were included in the [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
     module namespace have been removed.
    

Porting to Python 3.4[¶](https://docs.python.org/3/whatsnew/3.4.html#porting-to-python-3-4 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in ‘python’ Command Behavior[¶](https://docs.python.org/3/whatsnew/3.4.html#changes-in-python-command-behavior "Link to this heading")

*   In a posix shell, setting the `PATH` environment variable to an empty value is equivalent to not setting it at all. However, setting [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
     to an empty value was _not_ equivalent to not setting it at all: setting `PYTHONPATH` to an empty value was equivalent to setting it to `.`, which leads to confusion when reasoning by analogy to how `PATH` works. The behavior now conforms to the posix convention for `PATH`.
    
*   The \[X refs, Y blocks\] output of a debug (`--with-pydebug`) build of the CPython interpreter is now off by default. It can be re-enabled using the `-X showrefcount` option. (Contributed by Ezio Melotti in [bpo-17323](https://bugs.python.org/issue?@action=redirect&bpo=17323)
    .)
    
*   The python command and most stdlib scripts (as well as [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
    ) now output `--version` information to `stdout` instead of `stderr` (for issue list see [Other Improvements](https://docs.python.org/3/whatsnew/3.4.html#other-improvements-3-4)
     above).
    

### Changes in the Python API[¶](https://docs.python.org/3/whatsnew/3.4.html#changes-in-the-python-api "Link to this heading")

*   The ABCs defined in [`importlib.abc`](https://docs.python.org/3/library/importlib.html#module-importlib.abc "importlib.abc: Abstract base classes related to import")
     now either raise the appropriate exception or return a default value instead of raising [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
     blindly. This will only affect code calling [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
     and falling through all the way to the ABCs. For compatibility, catch both `NotImplementedError` or the appropriate exception as needed.
    
*   The module type now initializes the [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
     and [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
     attributes to `None` by default. To determine if these attributes were set in a backwards-compatible fashion, use e.g. `getattr(module, '__loader__', None) is not None`. ([bpo-17115](https://bugs.python.org/issue?@action=redirect&bpo=17115)
    .)
    
*   `importlib.util.module_for_loader()` now sets `__loader__` and `__package__` unconditionally to properly support reloading. If this is not desired then you will need to set these attributes manually. You can use `importlib.util._module_to_load()` for module management.
    
*   Import now resets relevant attributes (e.g. `__name__`, `__loader__`, `__package__`, `__file__`, `__cached__`) unconditionally when reloading. Note that this restores a pre-3.3 behavior in that it means a module is re-found when re-loaded ([bpo-19413](https://bugs.python.org/issue?@action=redirect&bpo=19413)
    ).
    
*   Frozen packages no longer set `__path__` to a list containing the package name, they now set it to an empty list. The previous behavior could cause the import system to do the wrong thing on submodule imports if there was also a directory with the same name as the frozen package. The correct way to determine if a module is a package or not is to use `hasattr(module, '__path__')` ([bpo-18065](https://bugs.python.org/issue?@action=redirect&bpo=18065)
    ).
    
*   Frozen modules no longer define a `__file__` attribute. It’s semantically incorrect for frozen modules to set the attribute as they are not loaded from any explicit location. If you must know that a module comes from frozen code then you can see if the module’s `__spec__.origin` is set to `'frozen'`, check if the loader is a subclass of [`importlib.machinery.FrozenImporter`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FrozenImporter "importlib.machinery.FrozenImporter")
    , or if Python 2 compatibility is necessary you can use `imp.is_frozen()`.
    
*   [`py_compile.compile()`](https://docs.python.org/3/library/py_compile.html#py_compile.compile "py_compile.compile")
     now raises [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
     if the file path it would write to is a symlink or a non-regular file. This is to act as a warning that import will overwrite those files with a regular file regardless of what type of file path they were originally.
    
*   [`importlib.abc.SourceLoader.get_source()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.get_source "importlib.abc.SourceLoader.get_source")
     no longer raises [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
     when the source code being loaded triggers a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
     or [`UnicodeDecodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")
    . As `ImportError` is meant to be raised only when source code cannot be found but it should, it was felt to be over-reaching/overloading of that meaning when the source code is found but improperly structured. If you were catching ImportError before and wish to continue to ignore syntax or decoding issues, catch all three exceptions now.
    
*   [`functools.update_wrapper()`](https://docs.python.org/3/library/functools.html#functools.update_wrapper "functools.update_wrapper")
     and [`@functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps "functools.wraps")
     now correctly set the `__wrapped__` attribute to the function being wrapped, even if that function also had its `__wrapped__` attribute set. This means `__wrapped__` attributes now correctly link a stack of decorated functions rather than every `__wrapped__` attribute in the chain referring to the innermost function. Introspection libraries that assumed the previous behaviour was intentional can use [`inspect.unwrap()`](https://docs.python.org/3/library/inspect.html#inspect.unwrap "inspect.unwrap")
     to access the first function in the chain that has no `__wrapped__` attribute.
    
*   [`inspect.getfullargspec()`](https://docs.python.org/3/library/inspect.html#inspect.getfullargspec "inspect.getfullargspec")
     has been reimplemented on top of [`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
     and hence handles a much wider variety of callable objects than it did in the past. It is expected that additional builtin and extension module callables will gain signature metadata over the course of the Python 3.4 series. Code that assumes that `inspect.getfullargspec()` will fail on non-Python callables may need to be adjusted accordingly.
    
*   [`importlib.machinery.PathFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder "importlib.machinery.PathFinder")
     now passes on the current working directory to objects in [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
     for the empty string. This results in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache")
     never containing `''`, thus iterating through `sys.path_importer_cache` based on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
     will not find all keys. A module’s `__file__` when imported in the current working directory will also now have an absolute path, including when using `-m` with the interpreter (except for `__main__.__file__` when a script has been executed directly using a relative path) (Contributed by Brett Cannon in [bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416)
    ). is specified on the command-line) ([bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416)
    ).
    
*   The removal of the _strict_ argument to [`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection")
     and [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
     changes the meaning of the remaining arguments if you are specifying them positionally rather than by keyword. If you’ve been paying attention to deprecation warnings your code should already be specifying any additional arguments via keywords.
    
*   Strings between `from __future__ import ...` statements now _always_ raise a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
    . Previously if there was no leading docstring, an interstitial string would sometimes be ignored. This brings CPython into compliance with the language spec; Jython and PyPy already were. ([bpo-17434](https://bugs.python.org/issue?@action=redirect&bpo=17434)
    ).
    
*   [`ssl.SSLSocket.getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert")
     and [`ssl.SSLSocket.do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake")
     now raise an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
     with `ENOTCONN` when the `SSLSocket` is not connected, instead of the previous behavior of raising an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
    . In addition, `getpeercert()` will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if the handshake has not yet been done.
    
*   [`base64.b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "base64.b32decode")
     now raises a [`binascii.Error`](https://docs.python.org/3/library/binascii.html#binascii.Error "binascii.Error")
     when the input string contains non-b32-alphabet characters, instead of a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    . This particular `TypeError` was missed when the other `TypeError`s were converted. (Contributed by Serhiy Storchaka in [bpo-18011](https://bugs.python.org/issue?@action=redirect&bpo=18011)
    .) Note: this change was also inadvertently applied in Python 3.3.3.
    
*   The `file` attribute is now automatically closed when the creating `cgi.FieldStorage` instance is garbage collected. If you were pulling the file object out separately from the `cgi.FieldStorage` instance and not keeping the instance alive, then you should either store the entire `cgi.FieldStorage` instance or read the contents of the file before the `cgi.FieldStorage` instance is garbage collected.
    
*   Calling `read` or `write` on a closed SSL socket now raises an informative [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     rather than the previous more mysterious [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
     ([bpo-9177](https://bugs.python.org/issue?@action=redirect&bpo=9177)
    ).
    
*   [`slice.indices()`](https://docs.python.org/3/reference/datamodel.html#slice.indices "slice.indices")
     no longer produces an [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
     for huge values. As a consequence of this fix, `slice.indices()` now raises a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if given a negative length; previously it returned nonsense values ([bpo-14794](https://bugs.python.org/issue?@action=redirect&bpo=14794)
    ).
    
*   The [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
     constructor, unlike the [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
     functions, was incorrectly accepting [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
     values if an object’s `__complex__` special method returned one. This now raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    . ([bpo-16290](https://bugs.python.org/issue?@action=redirect&bpo=16290)
    .)
    
*   The [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     constructor in 3.2 and 3.3 erroneously accepts [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
     values for the _base_ parameter. It is unlikely anyone was doing this, but if so, it will now raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     ([bpo-16772](https://bugs.python.org/issue?@action=redirect&bpo=16772)
    ).
    
*   Defaults for keyword-only arguments are now evaluated _after_ defaults for regular keyword arguments, instead of before. Hopefully no one wrote any code that depends on the previous buggy behavior ([bpo-16967](https://bugs.python.org/issue?@action=redirect&bpo=16967)
    ).
    
*   Stale thread states are now cleared after [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
    . This may cause some system resources to be released that previously were incorrectly kept perpetually alive (for example, database connections kept in thread-local storage). ([bpo-17094](https://bugs.python.org/issue?@action=redirect&bpo=17094)
    .)
    
*   Parameter names in `__annotations__` dicts are now mangled properly, similarly to [`__kwdefaults__`](https://docs.python.org/3/reference/datamodel.html#function.__kwdefaults__ "function.__kwdefaults__")
    . (Contributed by Yury Selivanov in [bpo-20625](https://bugs.python.org/issue?@action=redirect&bpo=20625)
    .)
    
*   [`hashlib.hash.name`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.name "hashlib.hash.name")
     now always returns the identifier in lower case. Previously some builtin hashes had uppercase names, but now that it is a formal public interface the naming has been made consistent ([bpo-18532](https://bugs.python.org/issue?@action=redirect&bpo=18532)
    ).
    
*   Because [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite")
     now drops references to tests after they are run, test harnesses that reuse a [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite")
     to re-run a set of tests may fail. Test suites should not be re-used in this fashion since it means state is retained between test runs, breaking the test isolation that [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
     is designed to provide. However, if the lack of isolation is considered acceptable, the old behavior can be restored by creating a `TestSuite` subclass that defines a `_removeTestAtIndex` method that does nothing (see [`TestSuite.__iter__()`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.__iter__ "unittest.TestSuite.__iter__")
    ) ([bpo-11798](https://bugs.python.org/issue?@action=redirect&bpo=11798)
    ).
    
*   [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
     now uses [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
     for command line parsing. There are certain invalid command forms that used to work that are no longer allowed; in theory this should not cause backward compatibility issues since the disallowed command forms didn’t make any sense and are unlikely to be in use.
    
*   The [`re.split()`](https://docs.python.org/3/library/re.html#re.split "re.split")
    , [`re.findall()`](https://docs.python.org/3/library/re.html#re.findall "re.findall")
    , and [`re.sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub")
     functions, and the [`group()`](https://docs.python.org/3/library/re.html#re.Match.group "re.Match.group")
     and [`groups()`](https://docs.python.org/3/library/re.html#re.Match.groups "re.Match.groups")
     methods of `match` objects now always return a _bytes_ object when the string to be matched is a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
    . Previously the return type matched the input type, so if your code was depending on the return value being, say, a `bytearray`, you will need to change your code.
    
*   `audioop` functions now raise an error immediately if passed string input, instead of failing randomly later on ([bpo-16685](https://bugs.python.org/issue?@action=redirect&bpo=16685)
    ).
    
*   The new _convert\_charrefs_ argument to [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
     currently defaults to `False` for backward compatibility, but will eventually be changed to default to `True`. It is recommended that you add this keyword, with the appropriate value, to any `HTMLParser` calls in your code ([bpo-13633](https://bugs.python.org/issue?@action=redirect&bpo=13633)
    ).
    
*   Since the _digestmod_ argument to the [`hmac.new()`](https://docs.python.org/3/library/hmac.html#hmac.new "hmac.new")
     function will in the future have no default, all calls to `hmac.new()` should be changed to explicitly specify a _digestmod_ ([bpo-17276](https://bugs.python.org/issue?@action=redirect&bpo=17276)
    ).
    
*   Calling [`sysconfig.get_config_var()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var")
     with the `SO` key, or looking `SO` up in the results of a call to [`sysconfig.get_config_vars()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "sysconfig.get_config_vars")
     is deprecated. This key should be replaced by `EXT_SUFFIX` or `SHLIB_SUFFIX`, depending on the context ([bpo-19555](https://bugs.python.org/issue?@action=redirect&bpo=19555)
    ).
    
*   Any calls to `open` functions that specify `U` should be modified. `U` is ineffective in Python3 and will eventually raise an error if used. Depending on the function, the equivalent of its old Python2 behavior can be achieved using either a _newline_ argument, or if necessary by wrapping the stream in [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
     to use its _newline_ argument ([bpo-15204](https://bugs.python.org/issue?@action=redirect&bpo=15204)
    ).
    
*   If you use `pyvenv` in a script and desire that pip _not_ be installed, you must add `--without-pip` to your command invocation.
    
*   The default behavior of [`json.dump()`](https://docs.python.org/3/library/json.html#json.dump "json.dump")
     and [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps "json.dumps")
     when an indent is specified has changed: it no longer produces trailing spaces after the item separating commas at the ends of lines. This will matter only if you have tests that are doing white-space-sensitive comparisons of such output ([bpo-16333](https://bugs.python.org/issue?@action=redirect&bpo=16333)
    ).
    
*   [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")
     now looks for doctests in extension module `__doc__` strings, so if your doctest test discovery includes extension modules that have things that look like doctests in them you may see test failures you’ve never seen before when running your tests ([bpo-3158](https://bugs.python.org/issue?@action=redirect&bpo=3158)
    ).
    
*   The [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")
     module has been slightly refactored as part of the Python startup improvements. As a consequence of this, it is no longer the case that importing [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
     automatically imports `collections.abc`. If your program depended on the (undocumented) implicit import, you will need to add an explicit `import collections.abc` ([bpo-20784](https://bugs.python.org/issue?@action=redirect&bpo=20784)
    ).
    

### Changes in the C API[¶](https://docs.python.org/3/whatsnew/3.4.html#changes-in-the-c-api "Link to this heading")

*   [`PyEval_EvalFrameEx()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalFrameEx "PyEval_EvalFrameEx")
    , [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")
    , and [`PyObject_Str()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "PyObject_Str")
    , along with some other internal C APIs, now include a debugging assertion that ensures they are not used in situations where they may silently discard a currently active exception. In cases where discarding the active exception is expected and desired (for example, because it has already been saved locally with [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
     or is being deliberately replaced with a different exception), an explicit [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear "PyErr_Clear")
     call will be needed to avoid triggering the assertion when invoking these operations (directly or indirectly) and running against a version of Python that is compiled with assertions enabled.
    
*   [`PyErr_SetImportError()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetImportError "PyErr_SetImportError")
     now sets [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     when its **msg** argument is not set. Previously only `NULL` was returned with no exception set.
    
*   The result of the [`PyOS_ReadlineFunctionPointer`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer "PyOS_ReadlineFunctionPointer")
     callback must now be a string allocated by [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
     or [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
    , or `NULL` if an error occurred, instead of a string allocated by [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
     or [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
     ([bpo-16742](https://bugs.python.org/issue?@action=redirect&bpo=16742)
    )
    
*   [`PyThread_set_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_set_key_value "PyThread_set_key_value")
     now always set the value. In Python 3.3, the function did nothing if the key already exists (if the current value is a non-`NULL` pointer).
    
*   The `f_tstate` (thread state) field of the [`PyFrameObject`](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
     structure has been removed to fix a bug: see [bpo-14432](https://bugs.python.org/issue?@action=redirect&bpo=14432)
     for the rationale.
    

Changed in 3.4.3[¶](https://docs.python.org/3/whatsnew/3.4.html#changed-in-3-4-3 "Link to this heading")

---------------------------------------------------------------------------------------------------------

### PEP 476: Enabling certificate verification by default for stdlib http clients[¶](https://docs.python.org/3/whatsnew/3.4.html#pep-476-enabling-certificate-verification-by-default-for-stdlib-http-clients "Link to this heading")

[`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).")
 and modules which use it, such as [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
 and [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.")
, will now verify that the server presents a certificate which is signed by a CA in the platform trust store and whose hostname matches the hostname being requested by default, significantly improving security for many applications.

For applications which require the old previous behavior, they can pass an alternate context:

Copy

import urllib.request
import ssl

\# This disables all verification
context \= ssl.\_create\_unverified\_context()

\# This allows using a specific certificate for the host, which doesn't need
\# to be in the trust store
context \= ssl.create\_default\_context(cafile\="/path/to/file.crt")

urllib.request.urlopen("https://invalid-cert", context\=context)

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [What’s New In Python 3.4](https://docs.python.org/3/whatsnew/3.4.html#)
    *   [Summary – Release Highlights](https://docs.python.org/3/whatsnew/3.4.html#summary-release-highlights)
        
    *   [New Features](https://docs.python.org/3/whatsnew/3.4.html#new-features)
        *   [PEP 453: Explicit Bootstrapping of PIP in Python Installations](https://docs.python.org/3/whatsnew/3.4.html#pep-453-explicit-bootstrapping-of-pip-in-python-installations)
            *   [Bootstrapping pip By Default](https://docs.python.org/3/whatsnew/3.4.html#bootstrapping-pip-by-default)
                
            *   [Documentation Changes](https://docs.python.org/3/whatsnew/3.4.html#documentation-changes)
                
        *   [PEP 446: Newly Created File Descriptors Are Non-Inheritable](https://docs.python.org/3/whatsnew/3.4.html#pep-446-newly-created-file-descriptors-are-non-inheritable)
            
        *   [Improvements to Codec Handling](https://docs.python.org/3/whatsnew/3.4.html#improvements-to-codec-handling)
            
        *   [PEP 451: A ModuleSpec Type for the Import System](https://docs.python.org/3/whatsnew/3.4.html#pep-451-a-modulespec-type-for-the-import-system)
            
        *   [Other Language Changes](https://docs.python.org/3/whatsnew/3.4.html#other-language-changes)
            
    *   [New Modules](https://docs.python.org/3/whatsnew/3.4.html#new-modules)
        *   [asyncio](https://docs.python.org/3/whatsnew/3.4.html#asyncio)
            
        *   [ensurepip](https://docs.python.org/3/whatsnew/3.4.html#ensurepip)
            
        *   [enum](https://docs.python.org/3/whatsnew/3.4.html#enum)
            
        *   [pathlib](https://docs.python.org/3/whatsnew/3.4.html#pathlib)
            
        *   [selectors](https://docs.python.org/3/whatsnew/3.4.html#selectors)
            
        *   [statistics](https://docs.python.org/3/whatsnew/3.4.html#statistics)
            
        *   [tracemalloc](https://docs.python.org/3/whatsnew/3.4.html#tracemalloc)
            
    *   [Improved Modules](https://docs.python.org/3/whatsnew/3.4.html#improved-modules)
        *   [abc](https://docs.python.org/3/whatsnew/3.4.html#abc)
            
        *   [aifc](https://docs.python.org/3/whatsnew/3.4.html#aifc)
            
        *   [argparse](https://docs.python.org/3/whatsnew/3.4.html#argparse)
            
        *   [audioop](https://docs.python.org/3/whatsnew/3.4.html#audioop)
            
        *   [base64](https://docs.python.org/3/whatsnew/3.4.html#base64)
            
        *   [collections](https://docs.python.org/3/whatsnew/3.4.html#collections)
            
        *   [colorsys](https://docs.python.org/3/whatsnew/3.4.html#colorsys)
            
        *   [contextlib](https://docs.python.org/3/whatsnew/3.4.html#contextlib)
            
        *   [dbm](https://docs.python.org/3/whatsnew/3.4.html#dbm)
            
        *   [dis](https://docs.python.org/3/whatsnew/3.4.html#dis)
            
        *   [doctest](https://docs.python.org/3/whatsnew/3.4.html#doctest)
            
        *   [email](https://docs.python.org/3/whatsnew/3.4.html#email)
            
        *   [filecmp](https://docs.python.org/3/whatsnew/3.4.html#filecmp)
            
        *   [functools](https://docs.python.org/3/whatsnew/3.4.html#functools)
            
        *   [gc](https://docs.python.org/3/whatsnew/3.4.html#gc)
            
        *   [glob](https://docs.python.org/3/whatsnew/3.4.html#glob)
            
        *   [hashlib](https://docs.python.org/3/whatsnew/3.4.html#hashlib)
            
        *   [hmac](https://docs.python.org/3/whatsnew/3.4.html#hmac)
            
        *   [html](https://docs.python.org/3/whatsnew/3.4.html#html)
            
        *   [http](https://docs.python.org/3/whatsnew/3.4.html#http)
            
        *   [idlelib and IDLE](https://docs.python.org/3/whatsnew/3.4.html#idlelib-and-idle)
            
        *   [importlib](https://docs.python.org/3/whatsnew/3.4.html#importlib)
            
        *   [inspect](https://docs.python.org/3/whatsnew/3.4.html#inspect)
            
        *   [ipaddress](https://docs.python.org/3/whatsnew/3.4.html#ipaddress)
            
        *   [logging](https://docs.python.org/3/whatsnew/3.4.html#logging)
            
        *   [marshal](https://docs.python.org/3/whatsnew/3.4.html#marshal)
            
        *   [mmap](https://docs.python.org/3/whatsnew/3.4.html#mmap)
            
        *   [multiprocessing](https://docs.python.org/3/whatsnew/3.4.html#multiprocessing)
            
        *   [operator](https://docs.python.org/3/whatsnew/3.4.html#operator)
            
        *   [os](https://docs.python.org/3/whatsnew/3.4.html#os)
            
        *   [pdb](https://docs.python.org/3/whatsnew/3.4.html#pdb)
            
        *   [pickle](https://docs.python.org/3/whatsnew/3.4.html#pickle)
            
        *   [plistlib](https://docs.python.org/3/whatsnew/3.4.html#plistlib)
            
        *   [poplib](https://docs.python.org/3/whatsnew/3.4.html#poplib)
            
        *   [pprint](https://docs.python.org/3/whatsnew/3.4.html#pprint)
            
        *   [pty](https://docs.python.org/3/whatsnew/3.4.html#pty)
            
        *   [pydoc](https://docs.python.org/3/whatsnew/3.4.html#pydoc)
            
        *   [re](https://docs.python.org/3/whatsnew/3.4.html#re)
            
        *   [resource](https://docs.python.org/3/whatsnew/3.4.html#resource)
            
        *   [select](https://docs.python.org/3/whatsnew/3.4.html#select)
            
        *   [shelve](https://docs.python.org/3/whatsnew/3.4.html#shelve)
            
        *   [shutil](https://docs.python.org/3/whatsnew/3.4.html#shutil)
            
        *   [smtpd](https://docs.python.org/3/whatsnew/3.4.html#smtpd)
            
        *   [smtplib](https://docs.python.org/3/whatsnew/3.4.html#smtplib)
            
        *   [socket](https://docs.python.org/3/whatsnew/3.4.html#socket)
            
        *   [sqlite3](https://docs.python.org/3/whatsnew/3.4.html#sqlite3)
            
        *   [ssl](https://docs.python.org/3/whatsnew/3.4.html#ssl)
            
        *   [stat](https://docs.python.org/3/whatsnew/3.4.html#stat)
            
        *   [struct](https://docs.python.org/3/whatsnew/3.4.html#struct)
            
        *   [subprocess](https://docs.python.org/3/whatsnew/3.4.html#subprocess)
            
        *   [sunau](https://docs.python.org/3/whatsnew/3.4.html#sunau)
            
        *   [sys](https://docs.python.org/3/whatsnew/3.4.html#sys)
            
        *   [tarfile](https://docs.python.org/3/whatsnew/3.4.html#tarfile)
            
        *   [textwrap](https://docs.python.org/3/whatsnew/3.4.html#textwrap)
            
        *   [threading](https://docs.python.org/3/whatsnew/3.4.html#threading)
            
        *   [traceback](https://docs.python.org/3/whatsnew/3.4.html#traceback)
            
        *   [types](https://docs.python.org/3/whatsnew/3.4.html#types)
            
        *   [urllib](https://docs.python.org/3/whatsnew/3.4.html#urllib)
            
        *   [unittest](https://docs.python.org/3/whatsnew/3.4.html#unittest)
            
        *   [venv](https://docs.python.org/3/whatsnew/3.4.html#venv)
            
        *   [wave](https://docs.python.org/3/whatsnew/3.4.html#wave)
            
        *   [weakref](https://docs.python.org/3/whatsnew/3.4.html#weakref)
            
        *   [xml.etree](https://docs.python.org/3/whatsnew/3.4.html#xml-etree)
            
        *   [zipfile](https://docs.python.org/3/whatsnew/3.4.html#zipfile)
            
    *   [CPython Implementation Changes](https://docs.python.org/3/whatsnew/3.4.html#cpython-implementation-changes)
        *   [PEP 445: Customization of CPython Memory Allocators](https://docs.python.org/3/whatsnew/3.4.html#pep-445-customization-of-cpython-memory-allocators)
            
        *   [PEP 442: Safe Object Finalization](https://docs.python.org/3/whatsnew/3.4.html#pep-442-safe-object-finalization)
            
        *   [PEP 456: Secure and Interchangeable Hash Algorithm](https://docs.python.org/3/whatsnew/3.4.html#pep-456-secure-and-interchangeable-hash-algorithm)
            
        *   [PEP 436: Argument Clinic](https://docs.python.org/3/whatsnew/3.4.html#pep-436-argument-clinic)
            
        *   [Other Build and C API Changes](https://docs.python.org/3/whatsnew/3.4.html#other-build-and-c-api-changes)
            
        *   [Other Improvements](https://docs.python.org/3/whatsnew/3.4.html#other-improvements)
            
        *   [Significant Optimizations](https://docs.python.org/3/whatsnew/3.4.html#significant-optimizations)
            
    *   [Deprecated](https://docs.python.org/3/whatsnew/3.4.html#deprecated)
        *   [Deprecations in the Python API](https://docs.python.org/3/whatsnew/3.4.html#deprecations-in-the-python-api)
            
        *   [Deprecated Features](https://docs.python.org/3/whatsnew/3.4.html#deprecated-features)
            
    *   [Removed](https://docs.python.org/3/whatsnew/3.4.html#removed)
        *   [Operating Systems No Longer Supported](https://docs.python.org/3/whatsnew/3.4.html#operating-systems-no-longer-supported)
            
        *   [API and Feature Removals](https://docs.python.org/3/whatsnew/3.4.html#api-and-feature-removals)
            
        *   [Code Cleanups](https://docs.python.org/3/whatsnew/3.4.html#code-cleanups)
            
    *   [Porting to Python 3.4](https://docs.python.org/3/whatsnew/3.4.html#porting-to-python-3-4)
        *   [Changes in ‘python’ Command Behavior](https://docs.python.org/3/whatsnew/3.4.html#changes-in-python-command-behavior)
            
        *   [Changes in the Python API](https://docs.python.org/3/whatsnew/3.4.html#changes-in-the-python-api)
            
        *   [Changes in the C API](https://docs.python.org/3/whatsnew/3.4.html#changes-in-the-c-api)
            
    *   [Changed in 3.4.3](https://docs.python.org/3/whatsnew/3.4.html#changed-in-3-4-3)
        *   [PEP 476: Enabling certificate verification by default for stdlib http clients](https://docs.python.org/3/whatsnew/3.4.html#pep-476-enabling-certificate-verification-by-default-for-stdlib-http-clients)
            

#### Previous topic

[What’s New In Python 3.5](https://docs.python.org/3/whatsnew/3.5.html "previous chapter")

#### Next topic

[What’s New In Python 3.3](https://docs.python.org/3/whatsnew/3.3.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+New+In+Python+3.4&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F3.4.html&pagesource=whatsnew%2F3.4.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/3.4.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.3.html "What’s New In Python 3.3")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.5.html "What’s New In Python 3.5")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New In Python 3.4](https://docs.python.org/3/whatsnew/3.4.html)
    
*    
    
    |
*   Theme Auto Light Dark |