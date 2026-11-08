### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.1.html "What’s New In Python 3.1")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.3.html "What’s New In Python 3.3")
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
*   [What’s New In Python 3.2](https://docs.python.org/3/whatsnew/3.2.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s New In Python 3.2[¶](https://docs.python.org/3/whatsnew/3.2.html#what-s-new-in-python-3-2 "Link to this heading")

=========================================================================================================================

Author:

Raymond Hettinger

This article explains the new features in Python 3.2 as compared to 3.1. Python 3.2 was released on February 20, 2011. It focuses on a few highlights and gives a few examples. For full details, see the [Misc/NEWS](https://github.com/python/cpython/blob/076ca6c3c8df3030307e548d9be792ce3c1c6eea/Misc/NEWS)
 file.

See also

[**PEP 392**](https://peps.python.org/pep-0392/)
 - Python 3.2 Release Schedule

PEP 384: Defining a Stable ABI[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-384-defining-a-stable-abi "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

In the past, extension modules built for one Python version were often not usable with other Python versions. Particularly on Windows, every feature release of Python required rebuilding all extension modules that one wanted to use. This requirement was the result of the free access to Python interpreter internals that extension modules could use.

With Python 3.2, an alternative approach becomes available: extension modules which restrict themselves to a limited API (by defining Py\_LIMITED\_API) cannot use many of the internals, but are constrained to a set of API functions that are promised to be stable for several releases. As a consequence, extension modules built for 3.2 in that mode will also work with 3.3, 3.4, and so on. Extension modules that make use of details of memory structures can still be built, but will need to be recompiled for every feature release.

See also

[**PEP 384**](https://peps.python.org/pep-0384/)
 - Defining a Stable ABI

PEP written by Martin von Löwis.

PEP 389: Argparse Command Line Parsing Module[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-389-argparse-command-line-parsing-module "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

A new module for command line parsing, [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
, was introduced to overcome the limitations of [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
 which did not provide support for positional arguments (not just options), subcommands, required options and other common patterns of specifying and validating options.

This module has already had widespread success in the community as a third-party module. Being more fully featured than its predecessor, the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
 module is now the preferred module for command-line processing. The older module is still being kept available because of the substantial amount of legacy code that depends on it.

Here’s an annotated example parser showing features like limiting results to a set of choices, specifying a _metavar_ in the help screen, validating that one or more positional arguments is present, and making a required option:

Copy

import argparse
parser \= argparse.ArgumentParser(
            description \= 'Manage servers',         \# main description for help
            epilog \= 'Tested on Solaris and Linux') \# displayed after help
parser.add\_argument('action',                       \# argument name
            choices \= \['deploy', 'start', 'stop'\],  \# three allowed values
            help \= 'action on each target')         \# help msg
parser.add\_argument('targets',
            metavar \= 'HOSTNAME',                   \# var name used in help msg
            nargs \= '+',                            \# require one or more targets
            help \= 'url for target machines')       \# help msg explanation
parser.add\_argument('-u', '--user',                 \# -u or --user option
            required \= True,                        \# make it a required argument
            help \= 'login as user')

Example of calling the parser on a command string:

Copy

\>>> cmd \= 'deploy sneezy.example.com sleepy.example.com -u skycaptain'
\>>> result \= parser.parse\_args(cmd.split())
\>>> result.action
'deploy'
\>>> result.targets
\['sneezy.example.com', 'sleepy.example.com'\]
\>>> result.user
'skycaptain'

Example of the parser’s automatically generated help:

Copy

\>>> parser.parse\_args('-h'.split())

usage: manage\_cloud.py \[-h\] -u USER
                       {deploy,start,stop} HOSTNAME \[HOSTNAME ...\]

Manage servers

positional arguments:
  {deploy,start,stop}   action on each target
  HOSTNAME              url for target machines

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  login as user

Tested on Solaris and Linux

An especially nice [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
 feature is the ability to define subparsers, each with their own argument patterns and help displays:

Copy

import argparse
parser \= argparse.ArgumentParser(prog\='HELM')
subparsers \= parser.add\_subparsers()

parser\_l \= subparsers.add\_parser('launch', help\='Launch Control')   \# first subgroup
parser\_l.add\_argument('-m', '--missiles', action\='store\_true')
parser\_l.add\_argument('-t', '--torpedos', action\='store\_true')

parser\_m \= subparsers.add\_parser('move', help\='Move Vessel',        \# second subgroup
                                 aliases\=('steer', 'turn'))         \# equivalent names
parser\_m.add\_argument('-c', '--course', type\=int, required\=True)
parser\_m.add\_argument('-s', '--speed', type\=int, default\=0)

Copy

$ ./helm.py \--help                         \# top level help (launch and move)
$ ./helm.py launch \--help                  \# help for launch options
$ ./helm.py launch \--missiles              \# set missiles=True and torpedos=False
$ ./helm.py steer \--course 180 \--speed 5   \# set movement parameters

See also

[**PEP 389**](https://peps.python.org/pep-0389/)
 - New Command Line Parsing Module

PEP written by Steven Bethard.

[Migrating optparse code to argparse](https://docs.python.org/3/howto/argparse-optparse.html#upgrading-optparse-code)
 for details on the differences from [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
.

PEP 391: Dictionary Based Configuration for Logging[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-391-dictionary-based-configuration-for-logging "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
 module provided two kinds of configuration, one style with function calls for each option or another style driven by an external file saved in a [`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.")
 format. Those options did not provide the flexibility to create configurations from JSON or YAML files, nor did they support incremental configuration, which is needed for specifying logger options from a command line.

To support a more flexible style, the module now offers [`logging.config.dictConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "logging.config.dictConfig")
 for specifying logging configuration with plain Python dictionaries. The configuration options include formatters, handlers, filters, and loggers. Here’s a working example of a configuration dictionary:

Copy

{"version": 1,
 "formatters": {"brief": {"format": "%(levelname)-8s: %(name)-15s: %(message)s"},
                "full": {"format": "%(asctime)s %(name)-15s %(levelname)-8s %(message)s"}
                },
 "handlers": {"console": {
                   "class": "logging.StreamHandler",
                   "formatter": "brief",
                   "level": "INFO",
                   "stream": "ext://sys.stdout"},
              "console\_priority": {
                   "class": "logging.StreamHandler",
                   "formatter": "full",
                   "level": "ERROR",
                   "stream": "ext://sys.stderr"}
              },
 "root": {"level": "DEBUG", "handlers": \["console", "console\_priority"\]}}

If that dictionary is stored in a file called `conf.json`, it can be loaded and called with code like this:

Copy

\>>> import json, logging.config
\>>> with open('conf.json') as f:
...     conf \= json.load(f)
...
\>>> logging.config.dictConfig(conf)
\>>> logging.info("Transaction completed normally")
INFO    : root           : Transaction completed normally
\>>> logging.critical("Abnormal termination")
2011-02-17 11:14:36,694 root            CRITICAL Abnormal termination

See also

[**PEP 391**](https://peps.python.org/pep-0391/)
 - Dictionary Based Configuration for Logging

PEP written by Vinay Sajip.

PEP 3148: The `concurrent.futures` module[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-3148-the-concurrent-futures-module "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Code for creating and managing concurrency is being collected in a new top-level namespace, _concurrent_. Its first member is a _futures_ package which provides a uniform high-level interface for managing threads and processes.

The design for [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.")
 was inspired by the _java.util.concurrent_ package. In that model, a running call and its result are represented by a [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future")
 object that abstracts features common to threads, processes, and remote procedure calls. That object supports status checks (running or done), timeouts, cancellations, adding callbacks, and access to results or exceptions.

The primary offering of the new module is a pair of executor classes for launching and managing calls. The goal of the executors is to make it easier to use existing tools for making parallel calls. They save the effort needed to setup a pool of resources, launch the calls, create a results queue, add time-out handling, and limit the total number of threads, processes, or remote procedure calls.

Ideally, each application should share a single executor across multiple components so that process and thread limits can be centrally managed. This solves the design challenge that arises when each component has its own competing strategy for resource management.

Both classes share a common interface with three methods: [`submit()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "concurrent.futures.Executor.submit")
 for scheduling a callable and returning a [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future")
 object; [`map()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "concurrent.futures.Executor.map")
 for scheduling many asynchronous calls at a time, and [`shutdown()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown "concurrent.futures.Executor.shutdown")
 for freeing resources. The class is a [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 and can be used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement to assure that resources are automatically released when currently pending futures are done executing.

A simple of example of [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
 is a launch of four parallel threads for copying files:

Copy

import concurrent.futures, shutil
with concurrent.futures.ThreadPoolExecutor(max\_workers\=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest4.txt')

See also

[**PEP 3148**](https://peps.python.org/pep-3148/)
 - Futures – Execute Computations Asynchronously

PEP written by Brian Quinlan.

[Code for Threaded Parallel URL reads](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example)
, an example using threads to fetch multiple web pages in parallel.

[Code for computing prime numbers in parallel](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example)
, an example demonstrating [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor")
.

PEP 3147: PYC Repository Directories[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-3147-pyc-repository-directories "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Python’s scheme for caching bytecode in _.pyc_ files did not work well in environments with multiple Python interpreters. If one interpreter encountered a cached file created by another interpreter, it would recompile the source and overwrite the cached file, thus losing the benefits of caching.

The issue of “pyc fights” has become more pronounced as it has become commonplace for Linux distributions to ship with multiple versions of Python. These conflicts also arise with CPython alternatives such as Unladen Swallow.

To solve this problem, Python’s import machinery has been extended to use distinct filenames for each interpreter. Instead of Python 3.2 and Python 3.3 and Unladen Swallow each competing for a file called “mymodule.pyc”, they will now look for “mymodule.cpython-32.pyc”, “mymodule.cpython-33.pyc”, and “mymodule.unladen10.pyc”. And to prevent all of these new files from cluttering source directories, the _pyc_ files are now collected in a “\_\_pycache\_\_” directory stored under the package directory.

Aside from the filenames and target directories, the new scheme has a few aspects that are visible to the programmer:

*   Imported modules now have a `__cached__` attribute which stores the name of the actual file that was imported:
    
    Copy
    
    \>>> import collections
    \>>> collections.\_\_cached\_\_
    'c:/py32/lib/\_\_pycache\_\_/collections.cpython-32.pyc'
    
*   The tag that is unique to each interpreter is accessible from the `imp` module:
    
    Copy
    
    \>>> import imp
    \>>> imp.get\_tag()
    'cpython-32'
    
*   Scripts that try to deduce source filename from the imported file now need to be smarter. It is no longer sufficient to simply strip the “c” from a “.pyc” filename. Instead, use the new functions in the `imp` module:
    
    Copy
    
    \>>> imp.source\_from\_cache('c:/py32/lib/\_\_pycache\_\_/collections.cpython-32.pyc')
    'c:/py32/lib/collections.py'
    \>>> imp.cache\_from\_source('c:/py32/lib/collections.py')
    'c:/py32/lib/\_\_pycache\_\_/collections.cpython-32.pyc'
    
*   The [`py_compile`](https://docs.python.org/3/library/py_compile.html#module-py_compile "py_compile: Generate byte-code files from Python source files.")
     and [`compileall`](https://docs.python.org/3/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.")
     modules have been updated to reflect the new naming convention and target directory. The command-line invocation of _compileall_ has new options: `-i` for specifying a list of files and directories to compile and `-b` which causes bytecode files to be written to their legacy location rather than _\_\_pycache\_\__.
    
*   The [`importlib.abc`](https://docs.python.org/3/library/importlib.html#module-importlib.abc "importlib.abc: Abstract base classes related to import")
     module has been updated with new [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class)
     for loading bytecode files. The obsolete ABCs, `PyLoader` and `PyPycLoader`, have been deprecated (instructions on how to stay Python 3.1 compatible are included with the documentation).
    

See also

[**PEP 3147**](https://peps.python.org/pep-3147/)
 - PYC Repository Directories

PEP written by Barry Warsaw.

PEP 3149: ABI Version Tagged .so Files[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-3149-abi-version-tagged-so-files "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The PYC repository directory allows multiple bytecode cache files to be co-located. This PEP implements a similar mechanism for shared object files by giving them a common directory and distinct names for each version.

The common directory is “pyshared” and the file names are made distinct by identifying the Python implementation (such as CPython, PyPy, Jython, etc.), the major and minor version numbers, and optional build flags (such as “d” for debug, “m” for pymalloc, “u” for wide-unicode). For an arbitrary package “foo”, you may see these files when the distribution package is installed:

Copy

/usr/share/pyshared/foo.cpython\-32m.so
/usr/share/pyshared/foo.cpython\-33md.so

In Python itself, the tags are accessible from functions in the [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
 module:

Copy

\>>> import sysconfig
\>>> sysconfig.get\_config\_var('SOABI')       \# find the version tag
'cpython-32mu'
\>>> sysconfig.get\_config\_var('EXT\_SUFFIX')  \# find the full filename extension
'.cpython-32mu.so'

See also

[**PEP 3149**](https://peps.python.org/pep-3149/)
 - ABI Version Tagged .so Files

PEP written by Barry Warsaw.

PEP 3333: Python Web Server Gateway Interface v1.0.1[¶](https://docs.python.org/3/whatsnew/3.2.html#pep-3333-python-web-server-gateway-interface-v1-0-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This informational PEP clarifies how bytes/text issues are to be handled by the WSGI protocol. The challenge is that string handling in Python 3 is most conveniently handled with the [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 type even though the HTTP protocol is itself bytes oriented.

The PEP differentiates so-called _native strings_ that are used for request/response headers and metadata versus _byte strings_ which are used for the bodies of requests and responses.

The _native strings_ are always of type [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 but are restricted to code points between _U+0000_ through _U+00FF_ which are translatable to bytes using _Latin-1_ encoding. These strings are used for the keys and values in the environment dictionary and for response headers and statuses in the `start_response()` function. They must follow [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html)
 with respect to encoding. That is, they must either be _ISO-8859-1_ characters or use [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
 MIME encoding.

For developers porting WSGI applications from Python 2, here are the salient points:

*   If the app already used strings for headers in Python 2, no change is needed.
    
*   If instead, the app encoded output headers or decoded input headers, then the headers will need to be re-encoded to Latin-1. For example, an output header encoded in utf-8 was using `h.encode('utf-8')` now needs to convert from bytes to native strings using `h.encode('utf-8').decode('latin-1')`.
    
*   Values yielded by an application or sent using the `write()` method must be byte strings. The `start_response()` function and environ must use native strings. The two cannot be mixed.
    

For server implementers writing CGI-to-WSGI pathways or other CGI-style protocols, the users must to be able access the environment using native strings even though the underlying platform may have a different convention. To bridge this gap, the [`wsgiref`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref "wsgiref: WSGI Utilities and Reference Implementation.")
 module has a new function, [`wsgiref.handlers.read_environ()`](https://docs.python.org/3/library/wsgiref.html#wsgiref.handlers.read_environ "wsgiref.handlers.read_environ")
 for transcoding CGI variables from [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 into native strings and returning a new dictionary.

See also

[**PEP 3333**](https://peps.python.org/pep-3333/)
 - Python Web Server Gateway Interface v1.0.1

PEP written by Phillip Eby.

Other Language Changes[¶](https://docs.python.org/3/whatsnew/3.2.html#other-language-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Some smaller changes made to the core Python language are:

*   String formatting for [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
     and [`str.format()`](https://docs.python.org/3/builtins/stdtypes.html#str.format "str.format")
     gained new capabilities for the format character **#**. Previously, for integers in binary, octal, or hexadecimal, it caused the output to be prefixed with ‘0b’, ‘0o’, or ‘0x’ respectively. Now it can also handle floats, complex, and Decimal, causing the output to always have a decimal point even when no digits follow it.
    
    Copy
    
    \>>> format(20, '#o')
    '0o24'
    \>>> format(12.34, '#5.0f')
    '  12.'
    
    (Suggested by Mark Dickinson and implemented by Eric Smith in [bpo-7094](https://bugs.python.org/issue?@action=redirect&bpo=7094)
    .)
    
*   There is also a new [`str.format_map()`](https://docs.python.org/3/builtins/stdtypes.html#str.format_map "str.format_map")
     method that extends the capabilities of the existing [`str.format()`](https://docs.python.org/3/builtins/stdtypes.html#str.format "str.format")
     method by accepting arbitrary [mapping](https://docs.python.org/3/glossary.html#term-mapping)
     objects. This new method makes it possible to use string formatting with any of Python’s many dictionary-like objects such as [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
    , [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf")
    , [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
    , or [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.")
    . It is also useful with custom [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
     subclasses that normalize keys before look-up or that supply a [`__missing__()`](https://docs.python.org/3/reference/datamodel.html#object.__missing__ "object.__missing__")
     method for unknown keys:
    
    Copy
    
    \>>> import shelve
    \>>> d \= shelve.open('tmp.shl')
    \>>> 'The {project\_name} status is {status} as of {date}'.format\_map(d)
    'The testing project status is green as of February 15, 2011'
    
    \>>> class LowerCasedDict(dict):
    ...     def \_\_getitem\_\_(self, key):
    ...         return dict.\_\_getitem\_\_(self, key.lower())
    ...
    \>>> lcd \= LowerCasedDict(part\='widgets', quantity\=10)
    \>>> 'There are {QUANTITY} {Part} in stock'.format\_map(lcd)
    'There are 10 widgets in stock'
    
    \>>> class PlaceholderDict(dict):
    ...     def \_\_missing\_\_(self, key):
    ...         return '<{}\>'.format(key)
    ...
    \>>> 'Hello {name}, welcome to {location}'.format\_map(PlaceholderDict())
    'Hello <name>, welcome to <location>'
    

> (Suggested by Raymond Hettinger and implemented by Eric Smith in [bpo-6081](https://bugs.python.org/issue?@action=redirect&bpo=6081)
> .)

*   The interpreter can now be started with a quiet option, `-q`, to prevent the copyright and version information from being displayed in the interactive mode. The option can be introspected using the [`sys.flags`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags")
     attribute:
    
    Copy
    
    $ python \-q
    \>>> sys.flags
    sys.flags(debug=0, division\_warning=0, inspect=0, interactive=0,
    optimize=0, dont\_write\_bytecode=0, no\_user\_site=0, no\_site=0,
    ignore\_environment=0, verbose=0, bytes\_warning=0, quiet=1)
    
    (Contributed by Marcin Wojdyr in [bpo-1772833](https://bugs.python.org/issue?@action=redirect&bpo=1772833)
    ).
    
*   The [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
     function works by calling [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
     and detecting whether an exception is raised. This technique allows it to detect methods created dynamically by [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
     or [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__")
     which would otherwise be absent from the class dictionary. Formerly, _hasattr_ would catch any exception, possibly masking genuine errors. Now, _hasattr_ has been tightened to only catch [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
     and let other exceptions pass through:
    
    Copy
    
    \>>> class A:
    ...     @property
    ...     def f(self):
    ...         return 1 // 0
    ...
    \>>> a \= A()
    \>>> hasattr(a, 'f')
    Traceback (most recent call last):
      ...
    ZeroDivisionError: integer division or modulo by zero
    
    (Discovered by Yury Selivanov and fixed by Benjamin Peterson; [bpo-9666](https://bugs.python.org/issue?@action=redirect&bpo=9666)
    .)
    
*   The [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     of a float or complex number is now the same as its [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
    . Previously, the `str()` form was shorter but that just caused confusion and is no longer needed now that the shortest possible `repr()` is displayed by default:
    
    Copy
    
    \>>> import math
    \>>> repr(math.pi)
    '3.141592653589793'
    \>>> str(math.pi)
    '3.141592653589793'
    
    (Proposed and implemented by Mark Dickinson; [bpo-9337](https://bugs.python.org/issue?@action=redirect&bpo=9337)
    .)
    
*   [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
     objects now have a [`release()`](https://docs.python.org/3/builtins/stdtypes.html#memoryview.release "memoryview.release")
     method and they also now support the context management protocol. This allows timely release of any resources that were acquired when requesting a buffer from the original object.
    
    Copy
    
    \>>> with memoryview(b'abcdefgh') as v:
    ...     print(v.tolist())
    \[97, 98, 99, 100, 101, 102, 103, 104\]
    
    (Added by Antoine Pitrou; [bpo-9757](https://bugs.python.org/issue?@action=redirect&bpo=9757)
    .)
    
*   Previously it was illegal to delete a name from the local namespace if it occurs as a free variable in a nested block:
    
    Copy
    
    def outer(x):
        def inner():
            return x
        inner()
        del x
    
    This is now allowed. Remember that the target of an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     clause is cleared, so this code which used to work with Python 2.6, raised a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
     with Python 3.1 and now works again:
    
    Copy
    
    def f():
        def print\_error():
            print(e)
        try:
            something
        except Exception as e:
            print\_error()
            \# implicit "del e" here
    
    (See [bpo-4617](https://bugs.python.org/issue?@action=redirect&bpo=4617)
    .)
    
*   [Struct sequence types](https://docs.python.org/3/c-api/tuple.html#struct-sequence-objects)
     are now subclasses of tuple. This means that C structures like those returned by [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
    , [`time.gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
    , and [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")
     now work like a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
     and now work with functions and methods that expect a tuple as an argument. This is a big step forward in making the C structures as flexible as their pure Python counterparts:
    
    Copy
    
    \>>> import sys
    \>>> isinstance(sys.version\_info, tuple)
    True
    \>>> 'Version %d.%d.%d %s(%d)' % sys.version\_info
    'Version 3.2.0 final(0)'
    
    (Suggested by Arfrever Frehtes Taifersar Arahesis and implemented by Benjamin Peterson in [bpo-8413](https://bugs.python.org/issue?@action=redirect&bpo=8413)
    .)
    
*   Warnings are now easier to control using the [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS)
     environment variable as an alternative to using `-W` at the command line:
    
    Copy
    
    $ export PYTHONWARNINGS\='ignore::RuntimeWarning::,once::UnicodeWarning::'
    
    (Suggested by Barry Warsaw and implemented by Philip Jenvey in [bpo-7301](https://bugs.python.org/issue?@action=redirect&bpo=7301)
    .)
    
*   A new warning category, [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
    , has been added. It is emitted when potential issues with resource consumption or cleanup are detected. It is silenced by default in normal release builds but can be enabled through the means provided by the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
     module, or on the command line.
    
    A [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
     is issued at interpreter shutdown if the [`gc.garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage")
     list isn’t empty, and if [`gc.DEBUG_UNCOLLECTABLE`](https://docs.python.org/3/library/gc.html#gc.DEBUG_UNCOLLECTABLE "gc.DEBUG_UNCOLLECTABLE")
     is set, all uncollectable objects are printed. This is meant to make the programmer aware that their code contains object finalization issues.
    
    A [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
     is also issued when a [file object](https://docs.python.org/3/glossary.html#term-file-object)
     is destroyed without having been explicitly closed. While the deallocator for such object ensures it closes the underlying operating system resource (usually, a file descriptor), the delay in deallocating the object could produce various issues, especially under Windows. Here is an example of enabling the warning from the command line:
    
    Copy
    
    $ python \-q \-Wdefault
    \>>> f = open("foo", "wb")
    \>>> del f
    \_\_main\_\_:1: ResourceWarning: unclosed file <\_io.BufferedWriter name='foo'>
    
    (Added by Antoine Pitrou and Georg Brandl in [bpo-10093](https://bugs.python.org/issue?@action=redirect&bpo=10093)
     and [bpo-477863](https://bugs.python.org/issue?@action=redirect&bpo=477863)
    .)
    
*   [`range`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
     objects now support _index_ and _count_ methods. This is part of an effort to make more objects fully implement the [`collections.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")
     [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
    . As a result, the language will have a more uniform API. In addition, `range` objects now support slicing and negative indices, even with values larger than [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize")
    . This makes _range_ more interoperable with lists:
    
    Copy
    
    \>>> range(0, 100, 2).count(10)
    1
    \>>> range(0, 100, 2).index(10)
    5
    \>>> range(0, 100, 2)\[5\]
    10
    \>>> range(0, 100, 2)\[0:5\]
    range(0, 10, 2)
    
    (Contributed by Daniel Stutzbach in [bpo-9213](https://bugs.python.org/issue?@action=redirect&bpo=9213)
    , by Alexander Belopolsky in [bpo-2690](https://bugs.python.org/issue?@action=redirect&bpo=2690)
    , and by Nick Coghlan in [bpo-10889](https://bugs.python.org/issue?@action=redirect&bpo=10889)
    .)
    
*   The [`callable()`](https://docs.python.org/3/builtins/functions.html#callable "callable")
     builtin function from Py2.x was resurrected. It provides a concise, readable alternative to using an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
     in an expression like `isinstance(x, collections.Callable)`:
    
    Copy
    
    \>>> callable(max)
    True
    \>>> callable(20)
    False
    
    (See [bpo-10518](https://bugs.python.org/issue?@action=redirect&bpo=10518)
    .)
    
*   Python’s import mechanism can now load modules installed in directories with non-ASCII characters in the path name. This solved an aggravating problem with home directories for users with non-ASCII characters in their usernames.
    

> (Required extensive work by Victor Stinner in [bpo-9425](https://bugs.python.org/issue?@action=redirect&bpo=9425)
> .)

New, Improved, and Deprecated Modules[¶](https://docs.python.org/3/whatsnew/3.2.html#new-improved-and-deprecated-modules "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Python’s standard library has undergone significant maintenance efforts and quality improvements.

The biggest news for Python 3.2 is that the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package, [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
 module, and `nntplib` modules now work correctly with the bytes/text model in Python 3. For the first time, there is correct handling of messages with mixed encodings.

Throughout the standard library, there has been more careful attention to encodings and text versus bytes issues. In particular, interactions with the operating system are now better able to exchange non-ASCII data using the Windows MBCS encoding, locale-aware encodings, or UTF-8.

Another significant win is the addition of substantially better support for _SSL_ connections and security certificates.

In addition, more classes now implement a [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 to support convenient and reliable resource clean-up using a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

### email[¶](https://docs.python.org/3/whatsnew/3.2.html#email "Link to this heading")

The usability of the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package in Python 3 has been mostly fixed by the extensive efforts of R. David Murray. The problem was that emails are typically read and stored in the form of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 rather than [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 text, and they may contain multiple encodings within a single email. So, the email package had to be extended to parse and generate email messages in bytes format.

*   New functions [`message_from_bytes()`](https://docs.python.org/3/library/email.parser.html#email.message_from_bytes "email.message_from_bytes")
     and [`message_from_binary_file()`](https://docs.python.org/3/library/email.parser.html#email.message_from_binary_file "email.message_from_binary_file")
    , and new classes [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser")
     and [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser")
     allow binary message data to be parsed into model objects.
    
*   Given bytes input to the model, [`get_payload()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_payload "email.message.Message.get_payload")
     will by default decode a message body that has a _Content-Transfer-Encoding_ of _8bit_ using the charset specified in the MIME headers and return the resulting string.
    
*   Given bytes input to the model, [`Generator`](https://docs.python.org/3/library/email.generator.html#email.generator.Generator "email.generator.Generator")
     will convert message bodies that have a _Content-Transfer-Encoding_ of _8bit_ to instead have a _7bit_ _Content-Transfer-Encoding_.
    
    Headers with unencoded non-ASCII bytes are deemed to be [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)
    \-encoded using the _unknown-8bit_ character set.
    
*   A new class [`BytesGenerator`](https://docs.python.org/3/library/email.generator.html#email.generator.BytesGenerator "email.generator.BytesGenerator")
     produces bytes as output, preserving any unchanged non-ASCII data that was present in the input used to build the model, including message bodies with a _Content-Transfer-Encoding_ of _8bit_.
    
*   The [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).")
     [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP")
     class now accepts a byte string for the _msg_ argument to the [`sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail")
     method, and a new method, [`send_message()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message "smtplib.SMTP.send_message")
     accepts a [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
     object and can optionally obtain the _from\_addr_ and _to\_addrs_ addresses directly from the object.
    

(Proposed and implemented by R. David Murray, [bpo-4661](https://bugs.python.org/issue?@action=redirect&bpo=4661)
 and [bpo-10321](https://bugs.python.org/issue?@action=redirect&bpo=10321)
.)

### elementtree[¶](https://docs.python.org/3/whatsnew/3.2.html#elementtree "Link to this heading")

The [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
 package and its `xml.etree.cElementTree` counterpart have been updated to version 1.3.

Several new and useful functions and methods have been added:

*   [`xml.etree.ElementTree.fromstringlist()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.fromstringlist "xml.etree.ElementTree.fromstringlist")
     which builds an XML document from a sequence of fragments
    
*   [`xml.etree.ElementTree.register_namespace()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.register_namespace "xml.etree.ElementTree.register_namespace")
     for registering a global namespace prefix
    
*   [`xml.etree.ElementTree.tostringlist()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.tostringlist "xml.etree.ElementTree.tostringlist")
     for string representation including all sublists
    
*   [`xml.etree.ElementTree.Element.extend()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.extend "xml.etree.ElementTree.Element.extend")
     for appending a sequence of zero or more elements
    
*   [`xml.etree.ElementTree.Element.iterfind()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iterfind "xml.etree.ElementTree.Element.iterfind")
     searches an element and subelements
    
*   [`xml.etree.ElementTree.Element.itertext()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.itertext "xml.etree.ElementTree.Element.itertext")
     creates a text iterator over an element and its subelements
    
*   [`xml.etree.ElementTree.TreeBuilder.end()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.end "xml.etree.ElementTree.TreeBuilder.end")
     closes the current element
    
*   [`xml.etree.ElementTree.TreeBuilder.doctype()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder.doctype "xml.etree.ElementTree.TreeBuilder.doctype")
     handles a doctype declaration
    

Two methods have been deprecated:

*   `xml.etree.ElementTree.getchildren()` use `list(elem)` instead.
    
*   `xml.etree.ElementTree.getiterator()` use `Element.iter` instead.
    

For details of the update, see [Introducing ElementTree](https://web.archive.org/web/20200703234532/http://effbot.org/zone/elementtree-13-intro.htm)
 on Fredrik Lundh’s website.

(Contributed by Florent Xicluna and Fredrik Lundh, [bpo-6472](https://bugs.python.org/issue?@action=redirect&bpo=6472)
.)

### functools[¶](https://docs.python.org/3/whatsnew/3.2.html#functools "Link to this heading")

*   The [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
     module includes a new decorator for caching function calls. [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache")
     can save repeated queries to an external resource whenever the results are expected to be the same.
    
    For example, adding a caching decorator to a database query function can save database accesses for popular searches:
    
    Copy
    
    \>>> import functools
    \>>> @functools.lru\_cache(maxsize\=300)
    ... def get\_phone\_number(name):
    ...     c \= conn.cursor()
    ...     c.execute('SELECT phonenumber FROM phonelist WHERE name=?', (name,))
    ...     return c.fetchone()\[0\]
    
    Copy
    
    \>>> for name in user\_requests:
    ...     get\_phone\_number(name)        \# cached lookup
    
    To help with choosing an effective cache size, the wrapped function is instrumented for tracking cache statistics:
    
    Copy
    
    \>>> get\_phone\_number.cache\_info()
    CacheInfo(hits=4805, misses=980, maxsize=300, currsize=300)
    
    If the phonelist table gets updated, the outdated contents of the cache can be cleared with:
    
    Copy
    
    \>>> get\_phone\_number.cache\_clear()
    
    (Contributed by Raymond Hettinger and incorporating design ideas from Jim Baker, Miki Tebeka, and Nick Coghlan; see [recipe 498245](https://code.activestate.com/recipes/498245-lru-and-lfu-cache-decorators/)
    , [recipe 577479](https://code.activestate.com/recipes/577479-simple-caching-decorator/)
    , [bpo-10586](https://bugs.python.org/issue?@action=redirect&bpo=10586)
    , and [bpo-10593](https://bugs.python.org/issue?@action=redirect&bpo=10593)
    .)
    
*   The [`@functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps "functools.wraps")
     decorator now adds a `__wrapped__` attribute pointing to the original callable function. This allows wrapped functions to be introspected. It also copies [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#function.__annotations__ "function.__annotations__")
     if defined. And now it also gracefully skips over missing attributes such as [`__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__")
     which might not be defined for the wrapped callable.
    
    In the above example, the cache can be removed by recovering the original function:
    
    Copy
    
    \>>> get\_phone\_number \= get\_phone\_number.\_\_wrapped\_\_    \# uncached function
    
    (By Nick Coghlan and Terrence Cole; [bpo-9567](https://bugs.python.org/issue?@action=redirect&bpo=9567)
    , [bpo-3445](https://bugs.python.org/issue?@action=redirect&bpo=3445)
    , and [bpo-8814](https://bugs.python.org/issue?@action=redirect&bpo=8814)
    .)
    
*   To help write classes with rich comparison methods, a new decorator [`@functools.total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering "functools.total_ordering")
     will use existing equality and inequality methods to fill in the remaining methods.
    
    For example, supplying _\_\_eq\_\__ and _\_\_lt\_\__ will enable [`@total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering "functools.total_ordering")
     to fill-in _\_\_le\_\__, _\_\_gt\_\__ and _\_\_ge\_\__:
    
    Copy
    
    @total\_ordering
    class Student:
        def \_\_eq\_\_(self, other):
            return ((self.lastname.lower(), self.firstname.lower()) \==
                    (other.lastname.lower(), other.firstname.lower()))
    
        def \_\_lt\_\_(self, other):
            return ((self.lastname.lower(), self.firstname.lower()) <
                    (other.lastname.lower(), other.firstname.lower()))
    
    With the _total\_ordering_ decorator, the remaining comparison methods are filled in automatically.
    
    (Contributed by Raymond Hettinger.)
    
*   To aid in porting programs from Python 2, the [`functools.cmp_to_key()`](https://docs.python.org/3/library/functools.html#functools.cmp_to_key "functools.cmp_to_key")
     function converts an old-style comparison function to modern [key function](https://docs.python.org/3/glossary.html#term-key-function)
    :
    
    Copy
    
    \>>> \# locale-aware sort order
    \>>> sorted(iterable, key\=cmp\_to\_key(locale.strcoll))
    
    For sorting examples and a brief sorting tutorial, see the [Sorting HowTo](https://wiki.python.org/moin/HowTo/Sorting/)
     tutorial.
    
    (Contributed by Raymond Hettinger.)
    

### itertools[¶](https://docs.python.org/3/whatsnew/3.2.html#itertools "Link to this heading")

*   The [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.")
     module has a new [`accumulate()`](https://docs.python.org/3/library/itertools.html#itertools.accumulate "itertools.accumulate")
     function modeled on APL’s _scan_ operator and Numpy’s _accumulate_ function:
    
    Copy
    
    \>>> from itertools import accumulate
    \>>> list(accumulate(\[8, 2, 50\]))
    \[8, 10, 60\]
    
    Copy
    
    \>>> prob\_dist \= \[0.1, 0.4, 0.2, 0.3\]
    \>>> list(accumulate(prob\_dist))      \# cumulative probability distribution
    \[0.1, 0.5, 0.7, 1.0\]
    
    For an example using [`accumulate()`](https://docs.python.org/3/library/itertools.html#itertools.accumulate "itertools.accumulate")
    , see the [examples for the random module](https://docs.python.org/3/library/random.html#random-examples)
    .
    
    (Contributed by Raymond Hettinger and incorporating design suggestions from Mark Dickinson.)
    

### collections[¶](https://docs.python.org/3/whatsnew/3.2.html#collections "Link to this heading")

*   The [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")
     class now has two forms of in-place subtraction, the existing _\-=_ operator for [saturating subtraction](https://en.wikipedia.org/wiki/Saturation_arithmetic)
     and the new [`subtract()`](https://docs.python.org/3/library/collections.html#collections.Counter.subtract "collections.Counter.subtract")
     method for regular subtraction. The former is suitable for [multisets](https://en.wikipedia.org/wiki/Multiset)
     which only have positive counts, and the latter is more suitable for use cases that allow negative counts:
    
    Copy
    
    \>>> from collections import Counter
    \>>> tally \= Counter(dogs\=5, cats\=3)
    \>>> tally \-= Counter(dogs\=2, cats\=8)    \# saturating subtraction
    \>>> tally
    Counter({'dogs': 3})
    
    Copy
    
    \>>> tally \= Counter(dogs\=5, cats\=3)
    \>>> tally.subtract(dogs\=2, cats\=8)      \# regular subtraction
    \>>> tally
    Counter({'dogs': 3, 'cats': -5})
    
    (Contributed by Raymond Hettinger.)
    
*   The [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
     class has a new method [`move_to_end()`](https://docs.python.org/3/library/collections.html#collections.OrderedDict.move_to_end "collections.OrderedDict.move_to_end")
     which takes an existing key and moves it to either the first or last position in the ordered sequence.
    
    The default is to move an item to the last position. This is equivalent of renewing an entry with `od[k] = od.pop(k)`.
    
    A fast move-to-end operation is useful for resequencing entries. For example, an ordered dictionary can be used to track order of access by aging entries from the oldest to the most recently accessed.
    
    Copy
    
    \>>> from collections import OrderedDict
    \>>> d \= OrderedDict.fromkeys(\['a', 'b', 'X', 'd', 'e'\])
    \>>> list(d)
    \['a', 'b', 'X', 'd', 'e'\]
    \>>> d.move\_to\_end('X')
    \>>> list(d)
    \['a', 'b', 'd', 'e', 'X'\]
    
    (Contributed by Raymond Hettinger.)
    
*   The [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque")
     class grew two new methods [`count()`](https://docs.python.org/3/library/collections.html#collections.deque.count "collections.deque.count")
     and [`reverse()`](https://docs.python.org/3/library/collections.html#collections.deque.reverse "collections.deque.reverse")
     that make them more substitutable for [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
     objects:
    
    Copy
    
    \>>> from collections import deque
    \>>> d \= deque('simsalabim')
    \>>> d.count('s')
    2
    \>>> d.reverse()
    \>>> d
    deque(\['m', 'i', 'b', 'a', 'l', 'a', 's', 'm', 'i', 's'\])
    
    (Contributed by Raymond Hettinger.)
    

### threading[¶](https://docs.python.org/3/whatsnew/3.2.html#threading "Link to this heading")

The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 module has a new [`Barrier`](https://docs.python.org/3/library/threading.html#threading.Barrier "threading.Barrier")
 synchronization class for making multiple threads wait until all of them have reached a common barrier point. Barriers are useful for making sure that a task with multiple preconditions does not run until all of the predecessor tasks are complete.

Barriers can work with an arbitrary number of threads. This is a generalization of a [Rendezvous](https://en.wikipedia.org/wiki/Synchronous_rendezvous)
 which is defined for only two threads.

Implemented as a two-phase cyclic barrier, [`Barrier`](https://docs.python.org/3/library/threading.html#threading.Barrier "threading.Barrier")
 objects are suitable for use in loops. The separate _filling_ and _draining_ phases assure that all threads get released (drained) before any one of them can loop back and re-enter the barrier. The barrier fully resets after each cycle.

Example of using barriers:

Copy

from threading import Barrier, Thread

def get\_votes(site):
    ballots \= conduct\_election(site)
    all\_polls\_closed.wait()        \# do not count until all polls are closed
    totals \= summarize(ballots)
    publish(site, totals)

all\_polls\_closed \= Barrier(len(sites))
for site in sites:
    Thread(target\=get\_votes, args\=(site,)).start()

In this example, the barrier enforces a rule that votes cannot be counted at any polling site until all polls are closed. Notice how a solution with a barrier is similar to one with [`threading.Thread.join()`](https://docs.python.org/3/library/threading.html#threading.Thread.join "threading.Thread.join")
, but the threads stay alive and continue to do work (summarizing ballots) after the barrier point is crossed.

If any of the predecessor tasks can hang or be delayed, a barrier can be created with an optional _timeout_ parameter. Then if the timeout period elapses before all the predecessor tasks reach the barrier point, all waiting threads are released and a [`BrokenBarrierError`](https://docs.python.org/3/library/threading.html#threading.BrokenBarrierError "threading.BrokenBarrierError")
 exception is raised:

Copy

def get\_votes(site):
    ballots \= conduct\_election(site)
    try:
        all\_polls\_closed.wait(timeout\=midnight \- time.now())
    except BrokenBarrierError:
        lockbox \= seal\_ballots(ballots)
        queue.put(lockbox)
    else:
        totals \= summarize(ballots)
        publish(site, totals)

In this example, the barrier enforces a more robust rule. If some election sites do not finish before midnight, the barrier times-out and the ballots are sealed and deposited in a queue for later handling.

See [Barrier Synchronization Patterns](https://osl.cs.illinois.edu/media/papers/karmani-2009-barrier_synchronization_pattern.pdf)
 for more examples of how barriers can be used in parallel computing. Also, there is a simple but thorough explanation of barriers in [The Little Book of Semaphores](https://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf)
, _section 3.6_.

(Contributed by Kristján Valur Jónsson with an API review by Jeffrey Yasskin in [bpo-8777](https://bugs.python.org/issue?@action=redirect&bpo=8777)
.)

### datetime and time[¶](https://docs.python.org/3/whatsnew/3.2.html#datetime-and-time "Link to this heading")

*   The [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
     module has a new type [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
     that implements the [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo")
     interface by returning a fixed UTC offset and timezone name. This makes it easier to create timezone-aware datetime objects:
    
    Copy
    
    \>>> import datetime as dt
    
    \>>> dt.datetime.now(dt.timezone.utc)
    datetime.datetime(2010, 12, 8, 21, 4, 2, 923754, tzinfo=datetime.timezone.utc)
    
    \>>> dt.datetime.strptime("01/01/2000 12:00 +0000", "%m/%d/%Y %H:%M %z")
    datetime.datetime(2000, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
    
*   Also, [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
     objects can now be multiplied by [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
     and divided by `float` and [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     objects. And `timedelta` objects can now divide one another.
    
*   The [`datetime.date.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strftime "datetime.date.strftime")
     method is no longer restricted to years after 1900. The new supported year range is from 1000 to 9999 inclusive.
    
*   Whenever a two-digit year is used in a time tuple, the interpretation has been governed by `time.accept2dyear`. The default is `True` which means that for a two-digit year, the century is guessed according to the POSIX rules governing the `%y` strptime format.
    
    Starting with Py3.2, use of the century guessing heuristic will emit a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
    . Instead, it is recommended that `time.accept2dyear` be set to `False` so that large date ranges can be used without guesswork:
    
    Copy
    
    \>>> import time, warnings
    \>>> warnings.resetwarnings()      \# remove the default warning filters
    
    \>>> time.accept2dyear \= True      \# guess whether 11 means 11 or 2011
    \>>> time.asctime((11, 1, 1, 12, 34, 56, 4, 1, 0))
    Warning (from warnings module):
      ...
    DeprecationWarning: Century info guessed for a 2-digit year.
    'Fri Jan  1 12:34:56 2011'
    
    \>>> time.accept2dyear \= False     \# use the full range of allowable dates
    \>>> time.asctime((11, 1, 1, 12, 34, 56, 4, 1, 0))
    'Fri Jan  1 12:34:56 11'
    
    Several functions now have significantly expanded date ranges. When `time.accept2dyear` is false, the [`time.asctime()`](https://docs.python.org/3/library/time.html#time.asctime "time.asctime")
     function will accept any year that fits in a C int, while the [`time.mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime")
     and [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime")
     functions will accept the full range supported by the corresponding operating system functions.
    

(Contributed by Alexander Belopolsky and Victor Stinner in [bpo-1289118](https://bugs.python.org/issue?@action=redirect&bpo=1289118)
, [bpo-5094](https://bugs.python.org/issue?@action=redirect&bpo=5094)
, [bpo-6641](https://bugs.python.org/issue?@action=redirect&bpo=6641)
, [bpo-2706](https://bugs.python.org/issue?@action=redirect&bpo=2706)
, [bpo-1777412](https://bugs.python.org/issue?@action=redirect&bpo=1777412)
, [bpo-8013](https://bugs.python.org/issue?@action=redirect&bpo=8013)
, and [bpo-10827](https://bugs.python.org/issue?@action=redirect&bpo=10827)
.)

### math[¶](https://docs.python.org/3/whatsnew/3.2.html#math "Link to this heading")

The [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
 module has been updated with six new functions inspired by the C99 standard.

The [`isfinite()`](https://docs.python.org/3/library/math.html#math.isfinite "math.isfinite")
 function provides a reliable and fast way to detect special values. It returns `True` for regular numbers and `False` for _Nan_ or _Infinity_:

Copy

\>>> from math import isfinite
\>>> \[isfinite(x) for x in (123, 4.56, float('Nan'), float('Inf'))\]
\[True, True, False, False\]

The [`expm1()`](https://docs.python.org/3/library/math.html#math.expm1 "math.expm1")
 function computes `e**x-1` for small values of _x_ without incurring the loss of precision that usually accompanies the subtraction of nearly equal quantities:

Copy

\>>> from math import expm1
\>>> expm1(0.013671875)   \# more accurate way to compute e\*\*x-1 for a small x
0.013765762467652909

The [`erf()`](https://docs.python.org/3/library/math.html#math.erf "math.erf")
 function computes a probability integral or [Gaussian error function](https://en.wikipedia.org/wiki/Error_function)
. The complementary error function, [`erfc()`](https://docs.python.org/3/library/math.html#math.erfc "math.erfc")
, is `1 - erf(x)`:

Copy

\>>> from math import erf, erfc, sqrt
\>>> erf(1.0/sqrt(2.0))   \# portion of normal distribution within 1 standard deviation
0.682689492137086
\>>> erfc(1.0/sqrt(2.0))  \# portion of normal distribution outside 1 standard deviation
0.31731050786291404
\>>> erf(1.0/sqrt(2.0)) + erfc(1.0/sqrt(2.0))
1.0

The [`gamma()`](https://docs.python.org/3/library/math.html#math.gamma "math.gamma")
 function is a continuous extension of the factorial function. See [https://en.wikipedia.org/wiki/Gamma\_function](https://en.wikipedia.org/wiki/Gamma_function)
 for details. Because the function is related to factorials, it grows large even for small values of _x_, so there is also a [`lgamma()`](https://docs.python.org/3/library/math.html#math.lgamma "math.lgamma")
 function for computing the natural logarithm of the gamma function:

Copy

\>>> from math import gamma, lgamma
\>>> gamma(7.0)           \# six factorial
720.0
\>>> lgamma(801.0)        \# log(800 factorial)
4551.950730698041

(Contributed by Mark Dickinson.)

### abc[¶](https://docs.python.org/3/whatsnew/3.2.html#abc "Link to this heading")

The [`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")
 module now supports [`@abstractclassmethod`](https://docs.python.org/3/library/abc.html#abc.abstractclassmethod "abc.abstractclassmethod")
 and [`@abstractstaticmethod`](https://docs.python.org/3/library/abc.html#abc.abstractstaticmethod "abc.abstractstaticmethod")
.

These tools make it possible to define an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 that requires a particular [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 or [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 to be implemented:

Copy

class Temperature(metaclass\=abc.ABCMeta):
    @abc.abstractclassmethod
    def from\_fahrenheit(cls, t):
        ...
    @abc.abstractclassmethod
    def from\_celsius(cls, t):
        ...

(Patch submitted by Daniel Urban; [bpo-5867](https://bugs.python.org/issue?@action=redirect&bpo=5867)
.)

### io[¶](https://docs.python.org/3/whatsnew/3.2.html#io "Link to this heading")

The [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
 has a new method, [`getbuffer()`](https://docs.python.org/3/library/io.html#io.BytesIO.getbuffer "io.BytesIO.getbuffer")
, which provides functionality similar to [`memoryview()`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
. It creates an editable view of the data without making a copy. The buffer’s random access and support for slice notation are well-suited to in-place editing:

Copy

\>>> REC\_LEN, LOC\_START, LOC\_LEN \= 34, 7, 11

\>>> def change\_location(buffer, record\_number, location):
...     start \= record\_number \* REC\_LEN + LOC\_START
...     buffer\[start: start+LOC\_LEN\] \= location

\>>> import io

\>>> byte\_stream \= io.BytesIO(
...     b'G3805  storeroom  Main chassis    '
...     b'X7899  shipping   Reserve cog     '
...     b'L6988  receiving  Primary sprocket'
... )
\>>> buffer \= byte\_stream.getbuffer()
\>>> change\_location(buffer, 1, b'warehouse  ')
\>>> change\_location(buffer, 0, b'showroom   ')
\>>> print(byte\_stream.getvalue())
b'G3805  showroom   Main chassis    '
b'X7899  warehouse  Reserve cog     '
b'L6988  receiving  Primary sprocket'

(Contributed by Antoine Pitrou in [bpo-5506](https://bugs.python.org/issue?@action=redirect&bpo=5506)
.)

### reprlib[¶](https://docs.python.org/3/whatsnew/3.2.html#reprlib "Link to this heading")

When writing a [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 method for a custom container, it is easy to forget to handle the case where a member refers back to the container itself. Python’s builtin objects such as [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 and [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 handle self-reference by displaying “…” in the recursive part of the representation string.

To help write such [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 methods, the [`reprlib`](https://docs.python.org/3/library/reprlib.html#module-reprlib "reprlib: Alternate repr() implementation with size limits.")
 module has a new decorator, [`@recursive_repr`](https://docs.python.org/3/library/reprlib.html#reprlib.recursive_repr "reprlib.recursive_repr")
, for detecting recursive calls to `__repr__()` and substituting a placeholder string instead:

Copy

\>>> class MyList(list):
...     @recursive\_repr()
...     def \_\_repr\_\_(self):
...         return '<' + '|'.join(map(repr, self)) + '>'
...
\>>> m \= MyList('abc')
\>>> m.append(m)
\>>> m.append('x')
\>>> print(m)
<'a'|'b'|'c'|...|'x'>

(Contributed by Raymond Hettinger in [bpo-9826](https://bugs.python.org/issue?@action=redirect&bpo=9826)
 and [bpo-9840](https://bugs.python.org/issue?@action=redirect&bpo=9840)
.)

### logging[¶](https://docs.python.org/3/whatsnew/3.2.html#logging "Link to this heading")

In addition to dictionary-based configuration described above, the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
 package has many other improvements.

The logging documentation has been augmented by a [basic tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)
, an [advanced tutorial](https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial)
, and a [cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)
 of logging recipes. These documents are the fastest way to learn about logging.

The [`logging.basicConfig()`](https://docs.python.org/3/library/logging.html#logging.basicConfig "logging.basicConfig")
 set-up function gained a _style_ argument to support three different types of string formatting. It defaults to “%” for traditional %-formatting, can be set to “{” for the new [`str.format()`](https://docs.python.org/3/builtins/stdtypes.html#str.format "str.format")
 style, or can be set to “$” for the shell-style formatting provided by [`string.Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template")
. The following three configurations are equivalent:

Copy

\>>> from logging import basicConfig
\>>> basicConfig(style\='%', format\="%(name)s -> %(levelname)s: %(message)s")
\>>> basicConfig(style\='{', format\="{name} -> {levelname} {message}")
\>>> basicConfig(style\='$', format\="$name -> $levelname: $message")

If no configuration is set-up before a logging event occurs, there is now a default configuration using a [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler")
 directed to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 for events of `WARNING` level or higher. Formerly, an event occurring before a configuration was set-up would either raise an exception or silently drop the event depending on the value of [`logging.raiseExceptions`](https://docs.python.org/3/library/logging.html#logging.raiseExceptions "logging.raiseExceptions")
. The new default handler is stored in [`logging.lastResort`](https://docs.python.org/3/library/logging.html#logging.lastResort "logging.lastResort")
.

The use of filters has been simplified. Instead of creating a [`Filter`](https://docs.python.org/3/library/logging.html#logging.Filter "logging.Filter")
 object, the predicate can be any Python callable that returns `True` or `False`.

There were a number of other improvements that add flexibility and simplify configuration. See the module documentation for a full listing of changes in Python 3.2.

### csv[¶](https://docs.python.org/3/whatsnew/3.2.html#csv "Link to this heading")

The [`csv`](https://docs.python.org/3/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.")
 module now supports a new dialect, [`unix_dialect`](https://docs.python.org/3/library/csv.html#csv.unix_dialect "csv.unix_dialect")
, which applies quoting for all fields and a traditional Unix style with `'\n'` as the line terminator. The registered dialect name is `unix`.

The [`csv.DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter "csv.DictWriter")
 has a new method, [`writeheader()`](https://docs.python.org/3/library/csv.html#csv.DictWriter.writeheader "csv.DictWriter.writeheader")
 for writing-out an initial row to document the field names:

Copy

\>>> import csv, sys
\>>> w \= csv.DictWriter(sys.stdout, \['name', 'dept'\], dialect\='unix')
\>>> w.writeheader()
"name","dept"
\>>> w.writerows(\[\
...     {'name': 'tom', 'dept': 'accounting'},\
...     {'name': 'susan', 'dept': 'Salesl'}\])
"tom","accounting"
"susan","sales"

(New dialect suggested by Jay Talbot in [bpo-5975](https://bugs.python.org/issue?@action=redirect&bpo=5975)
, and the new method suggested by Ed Abraham in [bpo-1537721](https://bugs.python.org/issue?@action=redirect&bpo=1537721)
.)

### contextlib[¶](https://docs.python.org/3/whatsnew/3.2.html#contextlib "Link to this heading")

There is a new and slightly mind-blowing tool [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
 that is helpful for creating a [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 that does double duty as a function decorator.

As a convenience, this new functionality is used by [`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
 so that no extra effort is needed to support both roles.

The basic idea is that both context managers and function decorators can be used for pre-action and post-action wrappers. Context managers wrap a group of statements using a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, and function decorators wrap a group of statements enclosed in a function. So, occasionally there is a need to write a pre-action or post-action wrapper that can be used in either role.

For example, it is sometimes useful to wrap functions or groups of statements with a logger that can track the time of entry and time of exit. Rather than writing both a function decorator and a context manager for the task, the [`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
 provides both capabilities in a single definition:

Copy

from contextlib import contextmanager
import logging

logging.basicConfig(level\=logging.INFO)

@contextmanager
def track\_entry\_and\_exit(name):
    logging.info('Entering: %s', name)
    yield
    logging.info('Exiting: %s', name)

Formerly, this would have only been usable as a context manager:

Copy

with track\_entry\_and\_exit('widget loader'):
    print('Some time consuming activity goes here')
    load\_widget()

Now, it can be used as a decorator as well:

Copy

@track\_entry\_and\_exit('widget loader')
def activity():
    print('Some time consuming activity goes here')
    load\_widget()

Trying to fulfill two roles at once places some limitations on the technique. Context managers normally have the flexibility to return an argument usable by a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, but there is no parallel for function decorators.

In the above example, there is not a clean way for the _track\_entry\_and\_exit_ context manager to return a logging instance for use in the body of enclosed statements.

(Contributed by Michael Foord in [bpo-9110](https://bugs.python.org/issue?@action=redirect&bpo=9110)
.)

### decimal and fractions[¶](https://docs.python.org/3/whatsnew/3.2.html#decimal-and-fractions "Link to this heading")

Mark Dickinson crafted an elegant and efficient scheme for assuring that different numeric datatypes will have the same hash value whenever their actual values are equal ([bpo-8188](https://bugs.python.org/issue?@action=redirect&bpo=8188)
):

Copy

assert hash(Fraction(3, 2)) \== hash(1.5) \== \\
       hash(Decimal("1.5")) \== hash(complex(1.5, 0))

Some of the hashing details are exposed through a new attribute, [`sys.hash_info`](https://docs.python.org/3/library/sys.html#sys.hash_info "sys.hash_info")
, which describes the bit width of the hash value, the prime modulus, the hash values for _infinity_ and _nan_, and the multiplier used for the imaginary part of a number:

Copy

\>>> sys.hash\_info
sys.hash\_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003)

An early decision to limit the interoperability of various numeric types has been relaxed. It is still unsupported (and ill-advised) to have implicit mixing in arithmetic expressions such as `Decimal('1.1') + float('1.1')` because the latter loses information in the process of constructing the binary float. However, since existing floating-point value can be converted losslessly to either a decimal or rational representation, it makes sense to add them to the constructor and to support mixed-type comparisons.

*   The [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     constructor now accepts [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
     objects directly so there in no longer a need to use the [`from_float()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.from_float "decimal.Decimal.from_float")
     method ([bpo-8257](https://bugs.python.org/issue?@action=redirect&bpo=8257)
    ).
    
*   Mixed type comparisons are now fully supported so that [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     objects can be directly compared with [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
     and [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
     ([bpo-2531](https://bugs.python.org/issue?@action=redirect&bpo=2531)
     and [bpo-8188](https://bugs.python.org/issue?@action=redirect&bpo=8188)
    ).
    

Similar changes were made to [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
 so that the [`from_float()`](https://docs.python.org/3/library/fractions.html#fractions.Fraction.from_float "fractions.Fraction.from_float")
 and [`from_decimal()`](https://docs.python.org/3/library/fractions.html#fractions.Fraction.from_decimal "fractions.Fraction.from_decimal")
 methods are no longer needed ([bpo-8294](https://bugs.python.org/issue?@action=redirect&bpo=8294)
):

Copy

\>>> from decimal import Decimal
\>>> from fractions import Fraction
\>>> Decimal(1.1)
Decimal('1.100000000000000088817841970012523233890533447265625')
\>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)

Another useful change for the [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
 module is that the [`Context.clamp`](https://docs.python.org/3/library/decimal.html#decimal.Context.clamp "decimal.Context.clamp")
 attribute is now public. This is useful in creating contexts that correspond to the decimal interchange formats specified in IEEE 754 (see [bpo-8540](https://bugs.python.org/issue?@action=redirect&bpo=8540)
).

(Contributed by Mark Dickinson and Raymond Hettinger.)

### ftp[¶](https://docs.python.org/3/whatsnew/3.2.html#ftp "Link to this heading")

The [`ftplib.FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
 class now supports the context management protocol to unconditionally consume [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error")
 exceptions and to close the FTP connection when done:

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

Other file-like objects such as [`mmap.mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap")
 and [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input")
 also grew auto-closing context managers:

Copy

with fileinput.input(files\=('log1.txt', 'log2.txt')) as f:
    for line in f:
        process(line)

(Contributed by Tarek Ziadé and Giampaolo Rodolà in [bpo-4972](https://bugs.python.org/issue?@action=redirect&bpo=4972)
, and by Georg Brandl in [bpo-8046](https://bugs.python.org/issue?@action=redirect&bpo=8046)
 and [bpo-1286](https://bugs.python.org/issue?@action=redirect&bpo=1286)
.)

The [`FTP_TLS`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS "ftplib.FTP_TLS")
 class now accepts a _context_ parameter, which is a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 object allowing bundling SSL configuration options, certificates and private keys into a single (potentially long-lived) structure.

(Contributed by Giampaolo Rodolà; [bpo-8806](https://bugs.python.org/issue?@action=redirect&bpo=8806)
.)

### popen[¶](https://docs.python.org/3/whatsnew/3.2.html#popen "Link to this heading")

The [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 and [`subprocess.Popen()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
 functions now support [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements for auto-closing of the file descriptors.

(Contributed by Antoine Pitrou and Brian Curtin in [bpo-7461](https://bugs.python.org/issue?@action=redirect&bpo=7461)
 and [bpo-10554](https://bugs.python.org/issue?@action=redirect&bpo=10554)
.)

### select[¶](https://docs.python.org/3/whatsnew/3.2.html#select "Link to this heading")

The [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")
 module now exposes a new, constant attribute, [`PIPE_BUF`](https://docs.python.org/3/library/select.html#select.PIPE_BUF "select.PIPE_BUF")
, which gives the minimum number of bytes which are guaranteed not to block when [`select.select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
 says a pipe is ready for writing.

Copy

\>>> import select
\>>> select.PIPE\_BUF
512

(Available on Unix systems. Patch by Sébastien Sablé in [bpo-9862](https://bugs.python.org/issue?@action=redirect&bpo=9862)
)

### gzip and zipfile[¶](https://docs.python.org/3/whatsnew/3.2.html#gzip-and-zipfile "Link to this heading")

[`gzip.GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile")
 now implements the [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
 [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 (except for `truncate()`). It also has a [`peek()`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile.peek "gzip.GzipFile.peek")
 method and supports unseekable as well as zero-padded file objects.

The [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")
 module also gains the [`compress()`](https://docs.python.org/3/library/gzip.html#gzip.compress "gzip.compress")
 and [`decompress()`](https://docs.python.org/3/library/gzip.html#gzip.decompress "gzip.decompress")
 functions for easier in-memory compression and decompression. Keep in mind that text needs to be encoded as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 before compressing and decompressing:

Copy

\>>> import gzip
\>>> s \= 'Three shall be the number thou shalt count, '
\>>> s += 'and the number of the counting shall be three'
\>>> b \= s.encode()                        \# convert to utf-8
\>>> len(b)
89
\>>> c \= gzip.compress(b)
\>>> len(c)
77
\>>> gzip.decompress(c).decode()\[:42\]      \# decompress and convert to text
'Three shall be the number thou shalt count'

(Contributed by Anand B. Pillai in [bpo-3488](https://bugs.python.org/issue?@action=redirect&bpo=3488)
; and by Antoine Pitrou, Nir Aides and Brian Curtin in [bpo-9962](https://bugs.python.org/issue?@action=redirect&bpo=9962)
, [bpo-1675951](https://bugs.python.org/issue?@action=redirect&bpo=1675951)
, [bpo-7471](https://bugs.python.org/issue?@action=redirect&bpo=7471)
 and [bpo-2846](https://bugs.python.org/issue?@action=redirect&bpo=2846)
.)

Also, the [`zipfile.ZipExtFile`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open")
 class was reworked internally to represent files stored inside an archive. The new implementation is significantly faster and can be wrapped in an [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader")
 object for more speedups. It also solves an issue where interleaved calls to _read_ and _readline_ gave the wrong results.

(Patch submitted by Nir Aides in [bpo-7610](https://bugs.python.org/issue?@action=redirect&bpo=7610)
.)

### tarfile[¶](https://docs.python.org/3/whatsnew/3.2.html#tarfile "Link to this heading")

The [`TarFile`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile "tarfile.TarFile")
 class can now be used as a context manager. In addition, its [`add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add")
 method has a new option, _filter_, that controls which files are added to the archive and allows the file metadata to be edited.

The new _filter_ option replaces the older, less flexible _exclude_ parameter which is now deprecated. If specified, the optional _filter_ parameter needs to be a [keyword argument](https://docs.python.org/3/glossary.html#term-keyword-argument)
. The user-supplied filter function accepts a [`TarInfo`](https://docs.python.org/3/library/tarfile.html#tarfile.TarInfo "tarfile.TarInfo")
 object and returns an updated `TarInfo` object, or if it wants the file to be excluded, the function can return `None`:

Copy

\>>> import tarfile, glob

\>>> def myfilter(tarinfo):
...     if tarinfo.isfile():             \# only save real files
...         tarinfo.uname \= 'monty'      \# redact the user name
...         return tarinfo

\>>> with tarfile.open(name\='myarchive.tar.gz', mode\='w:gz') as tf:
...     for filename in glob.glob('\*.txt'):
...         tf.add(filename, filter\=myfilter)
...     tf.list()
\-rw-r--r-- monty/501        902 2011-01-26 17:59:11 annotations.txt
\-rw-r--r-- monty/501        123 2011-01-26 17:59:11 general\_questions.txt
\-rw-r--r-- monty/501       3514 2011-01-26 17:59:11 prion.txt
\-rw-r--r-- monty/501        124 2011-01-26 17:59:11 py\_todo.txt
\-rw-r--r-- monty/501       1399 2011-01-26 17:59:11 semaphore\_notes.txt

(Proposed by Tarek Ziadé and implemented by Lars Gustäbel in [bpo-6856](https://bugs.python.org/issue?@action=redirect&bpo=6856)
.)

### hashlib[¶](https://docs.python.org/3/whatsnew/3.2.html#hashlib "Link to this heading")

The [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
 module has two new constant attributes listing the hashing algorithms guaranteed to be present in all implementations and those available on the current implementation:

Copy

\>>> import hashlib

\>>> hashlib.algorithms\_guaranteed
{'sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'}

\>>> hashlib.algorithms\_available
{'md2', 'SHA256', 'SHA512', 'dsaWithSHA', 'mdc2', 'SHA224', 'MD4', 'sha256',
'sha512', 'ripemd160', 'SHA1', 'MDC2', 'SHA', 'SHA384', 'MD2',
'ecdsa-with-SHA1','md4', 'md5', 'sha1', 'DSA-SHA', 'sha224',
'dsaEncryption', 'DSA', 'RIPEMD160', 'sha', 'MD5', 'sha384'}

(Suggested by Carl Chenet in [bpo-7418](https://bugs.python.org/issue?@action=redirect&bpo=7418)
.)

### ast[¶](https://docs.python.org/3/whatsnew/3.2.html#ast "Link to this heading")

The [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
 module has a wonderful a general-purpose tool for safely evaluating expression strings using the Python literal syntax. The [`ast.literal_eval()`](https://docs.python.org/3/library/ast.html#ast.literal_eval "ast.literal_eval")
 function serves as a secure alternative to the builtin [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 function which is easily abused. Python 3.2 adds [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 literals to the list of supported types: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and `None`.

Copy

\>>> from ast import literal\_eval

\>>> request \= "{'req': 3, 'func': 'pow', 'args': (2, 0.5)}"
\>>> literal\_eval(request)
{'args': (2, 0.5), 'req': 3, 'func': 'pow'}

\>>> request \= "os.system('do something harmful')"
\>>> literal\_eval(request)
Traceback (most recent call last):
  ...
ValueError: malformed node or string: <\_ast.Call object at 0x101739a10>

(Implemented by Benjamin Peterson and Georg Brandl.)

### os[¶](https://docs.python.org/3/whatsnew/3.2.html#os "Link to this heading")

Different operating systems use various encodings for filenames and environment variables. The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
 module provides two new functions, [`fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode")
 and [`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
, for encoding and decoding filenames:

Copy

\>>> import os
\>>> filename \= 'Sehenswürdigkeiten'
\>>> os.fsencode(filename)
b'Sehensw\\xc3\\xbcrdigkeiten'

Some operating systems allow direct access to encoded bytes in the environment. If so, the [`os.supports_bytes_environ`](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "os.supports_bytes_environ")
 constant will be true.

For direct access to encoded environment variables (if available), use the new [`os.getenvb()`](https://docs.python.org/3/library/os.html#os.getenvb "os.getenvb")
 function or use [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb")
 which is a bytes version of [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
.

(Contributed by Victor Stinner.)

### shutil[¶](https://docs.python.org/3/whatsnew/3.2.html#shutil "Link to this heading")

The [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree")
 function has two new options:

*   _ignore\_dangling\_symlinks_: when `symlinks=False` so that the function copies a file pointed to by a symlink, not the symlink itself. This option will silence the error raised if the file doesn’t exist.
    
*   _copy\_function_: is a callable that will be used to copy files. [`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2")
     is used by default.
    

(Contributed by Tarek Ziadé.)

In addition, the [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
 module now supports [archiving operations](https://docs.python.org/3/library/shutil.html#archiving-operations)
 for zipfiles, uncompressed tarfiles, gzipped tarfiles, and bzipped tarfiles. And there are functions for registering additional archiving file formats (such as xz compressed tarfiles or custom formats).

The principal functions are [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive")
 and [`unpack_archive()`](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "shutil.unpack_archive")
. By default, both operate on the current directory (which can be set by [`os.chdir()`](https://docs.python.org/3/library/os.html#os.chdir "os.chdir")
) and on any sub-directories. The archive filename needs to be specified with a full pathname. The archiving step is non-destructive (the original files are left unchanged).

Copy

\>>> import shutil, pprint

\>>> os.chdir('mydata')  \# change to the source directory
\>>> f \= shutil.make\_archive('/var/backup/mydata',
...                         'zip')      \# archive the current directory
\>>> f                                   \# show the name of archive
'/var/backup/mydata.zip'
\>>> os.chdir('tmp')                     \# change to an unpacking
\>>> shutil.unpack\_archive('/var/backup/mydata.zip')  \# recover the data

\>>> pprint.pprint(shutil.get\_archive\_formats())  \# display known formats
\[('bztar', "bzip2'ed tar-file"),\
 ('gztar', "gzip'ed tar-file"),\
 ('tar', 'uncompressed tar file'),\
 ('zip', 'ZIP file')\]

\>>> shutil.register\_archive\_format(     \# register a new archive format
...     name\='xz',
...     function\=xz.compress,           \# callable archiving function
...     extra\_args\=\[('level', 8)\],      \# arguments to the function
...     description\='xz compression'
... )

(Contributed by Tarek Ziadé.)

### sqlite3[¶](https://docs.python.org/3/whatsnew/3.2.html#sqlite3 "Link to this heading")

The [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
 module was updated to pysqlite version 2.6.0. It has two new capabilities.

*   The [`sqlite3.Connection.in_transaction`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.in_transaction "sqlite3.Connection.in_transaction")
     attribute is true if there is an active transaction for uncommitted changes.
    
*   The [`sqlite3.Connection.enable_load_extension()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension "sqlite3.Connection.enable_load_extension")
     and [`sqlite3.Connection.load_extension()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.load_extension "sqlite3.Connection.load_extension")
     methods allows you to load SQLite extensions from “.so” files. One well-known extension is the fulltext-search extension distributed with SQLite.
    

(Contributed by R. David Murray and Shashwat Anand; [bpo-8845](https://bugs.python.org/issue?@action=redirect&bpo=8845)
.)

### html[¶](https://docs.python.org/3/whatsnew/3.2.html#html "Link to this heading")

A new [`html`](https://docs.python.org/3/library/html.html#module-html "html: Helpers for manipulating HTML.")
 module was introduced with only a single function, [`escape()`](https://docs.python.org/3/library/html.html#html.escape "html.escape")
, which is used for escaping reserved characters from HTML markup:

Copy

\>>> import html
\>>> html.escape('x > 2 && x < 7')
'x &gt; 2 &amp;&amp; x &lt; 7'

### socket[¶](https://docs.python.org/3/whatsnew/3.2.html#socket "Link to this heading")

The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
 module has two new improvements.

*   Socket objects now have a [`detach()`](https://docs.python.org/3/library/socket.html#socket.socket.detach "socket.socket.detach")
     method which puts the socket into closed state without actually closing the underlying file descriptor. The latter can then be reused for other purposes. (Added by Antoine Pitrou; [bpo-8524](https://bugs.python.org/issue?@action=redirect&bpo=8524)
    .)
    
*   [`socket.create_connection()`](https://docs.python.org/3/library/socket.html#socket.create_connection "socket.create_connection")
     now supports the context management protocol to unconditionally consume [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error")
     exceptions and to close the socket when done. (Contributed by Giampaolo Rodolà; [bpo-9794](https://bugs.python.org/issue?@action=redirect&bpo=9794)
    .)
    

### ssl[¶](https://docs.python.org/3/whatsnew/3.2.html#ssl "Link to this heading")

The [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
 module added a number of features to satisfy common requirements for secure (encrypted, authenticated) internet connections:

*   A new class, [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
    , serves as a container for persistent SSL data, such as protocol settings, certificates, private keys, and various other options. It includes a [`wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket")
     for creating an SSL socket from an SSL context.
    
*   A new function, `ssl.match_hostname()`, supports server identity verification for higher-level protocols by implementing the rules of HTTPS (from [**RFC 2818**](https://datatracker.ietf.org/doc/html/rfc2818.html)
    ) which are also suitable for other protocols.
    
*   The [`ssl.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket")
     constructor function now takes a _ciphers_ argument. The _ciphers_ string lists the allowed encryption algorithms using the format described in the [OpenSSL documentation](https://docs.openssl.org/1.0.2/man1/ciphers/#cipher-list-format)
    .
    
*   When linked against recent versions of OpenSSL, the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     module now supports the Server Name Indication extension to the TLS protocol, allowing multiple “virtual hosts” using different certificates on a single IP port. This extension is only supported in client mode, and is activated by passing the _server\_hostname_ argument to [`ssl.SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket")
    .
    
*   Various options have been added to the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     module, such as [`OP_NO_SSLv2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "ssl.OP_NO_SSLv2")
     which disables the insecure and obsolete SSLv2 protocol.
    
*   The extension now loads all the OpenSSL ciphers and digest algorithms. If some SSL certificates cannot be verified, they are reported as an “unknown algorithm” error.
    
*   The version of OpenSSL being used is now accessible using the module attributes [`ssl.OPENSSL_VERSION`](https://docs.python.org/3/library/ssl.html#ssl.OPENSSL_VERSION "ssl.OPENSSL_VERSION")
     (a string), [`ssl.OPENSSL_VERSION_INFO`](https://docs.python.org/3/library/ssl.html#ssl.OPENSSL_VERSION_INFO "ssl.OPENSSL_VERSION_INFO")
     (a 5-tuple), and [`ssl.OPENSSL_VERSION_NUMBER`](https://docs.python.org/3/library/ssl.html#ssl.OPENSSL_VERSION_NUMBER "ssl.OPENSSL_VERSION_NUMBER")
     (an integer).
    

(Contributed by Antoine Pitrou in [bpo-8850](https://bugs.python.org/issue?@action=redirect&bpo=8850)
, [bpo-1589](https://bugs.python.org/issue?@action=redirect&bpo=1589)
, [bpo-8322](https://bugs.python.org/issue?@action=redirect&bpo=8322)
, [bpo-5639](https://bugs.python.org/issue?@action=redirect&bpo=5639)
, [bpo-4870](https://bugs.python.org/issue?@action=redirect&bpo=4870)
, [bpo-8484](https://bugs.python.org/issue?@action=redirect&bpo=8484)
, and [bpo-8321](https://bugs.python.org/issue?@action=redirect&bpo=8321)
.)

### nntp[¶](https://docs.python.org/3/whatsnew/3.2.html#nntp "Link to this heading")

The `nntplib` module has a revamped implementation with better bytes and text semantics as well as more practical APIs. These improvements break compatibility with the nntplib version in Python 3.1, which was partly dysfunctional in itself.

Support for secure connections through both implicit (using `nntplib.NNTP_SSL`) and explicit (using `nntplib.NNTP.starttls()`) TLS has also been added.

(Contributed by Antoine Pitrou in [bpo-9360](https://bugs.python.org/issue?@action=redirect&bpo=9360)
 and Andrew Vant in [bpo-1926](https://bugs.python.org/issue?@action=redirect&bpo=1926)
.)

### certificates[¶](https://docs.python.org/3/whatsnew/3.2.html#certificates "Link to this heading")

[`http.client.HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
, [`urllib.request.HTTPSHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPSHandler "urllib.request.HTTPSHandler")
 and [`urllib.request.urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen")
 now take optional arguments to allow for server certificate checking against a set of Certificate Authorities, as recommended in public uses of HTTPS.

(Added by Antoine Pitrou, [bpo-9003](https://bugs.python.org/issue?@action=redirect&bpo=9003)
.)

### imaplib[¶](https://docs.python.org/3/whatsnew/3.2.html#imaplib "Link to this heading")

Support for explicit TLS on standard IMAP4 connections has been added through the new [`imaplib.IMAP4.starttls`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.starttls "imaplib.IMAP4.starttls")
 method.

(Contributed by Lorenzo M. Catucci and Antoine Pitrou, [bpo-4471](https://bugs.python.org/issue?@action=redirect&bpo=4471)
.)

### http.client[¶](https://docs.python.org/3/whatsnew/3.2.html#http-client "Link to this heading")

There were a number of small API improvements in the [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).")
 module. The old-style HTTP 0.9 simple responses are no longer supported and the _strict_ parameter is deprecated in all classes.

The [`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection")
 and [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
 classes now have a _source\_address_ parameter for a (host, port) tuple indicating where the HTTP connection is made from.

Support for certificate checking and HTTPS virtual hosts were added to [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
.

The [`request()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.request "http.client.HTTPConnection.request")
 method on connection objects allowed an optional _body_ argument so that a [file object](https://docs.python.org/3/glossary.html#term-file-object)
 could be used to supply the content of the request. Conveniently, the _body_ argument now also accepts an [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 object so long as it includes an explicit `Content-Length` header. This extended interface is much more flexible than before.

To establish an HTTPS connection through a proxy server, there is a new [`set_tunnel()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.set_tunnel "http.client.HTTPConnection.set_tunnel")
 method that sets the host and port for HTTP Connect tunneling.

To match the behavior of [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
, the HTTP client library now also encodes headers with ISO-8859-1 (Latin-1) encoding. It was already doing that for incoming headers, so now the behavior is consistent for both incoming and outgoing traffic. (See work by Armin Ronacher in [bpo-10980](https://bugs.python.org/issue?@action=redirect&bpo=10980)
.)

### unittest[¶](https://docs.python.org/3/whatsnew/3.2.html#unittest "Link to this heading")

The unittest module has a number of improvements supporting test discovery for packages, easier experimentation at the interactive prompt, new testcase methods, improved diagnostic messages for test failures, and better method names.

*   The command-line call `python -m unittest` can now accept file paths instead of module names for running specific tests ([bpo-10620](https://bugs.python.org/issue?@action=redirect&bpo=10620)
    ). The new test discovery can find tests within packages, locating any test importable from the top-level directory. The top-level directory can be specified with the `-t` option, a pattern for matching files with `-p`, and a directory to start discovery with `-s`:
    
    Copy
    
    $ python \-m unittest discover \-s my\_proj\_dir \-p \_test.py
    
    (Contributed by Michael Foord.)
    
*   Experimentation at the interactive prompt is now easier because the [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")
     class can now be instantiated without arguments:
    
    Copy
    
    \>>> from unittest import TestCase
    \>>> TestCase().assertEqual(pow(2, 3), 8)
    
    (Contributed by Michael Foord.)
    
*   The [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
     module has two new methods, [`assertWarns()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns")
     and [`assertWarnsRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex")
     to verify that a given warning type is triggered by the code under test:
    
    Copy
    
    with self.assertWarns(DeprecationWarning):
        legacy\_function('XYZ')
    
    (Contributed by Antoine Pitrou, [bpo-9754](https://bugs.python.org/issue?@action=redirect&bpo=9754)
    .)
    
    Another new method, [`assertCountEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual "unittest.TestCase.assertCountEqual")
     is used to compare two iterables to determine if their element counts are equal (whether the same elements are present with the same number of occurrences regardless of order):
    
    Copy
    
    def test\_anagram(self):
        self.assertCountEqual('algorithm', 'logarithm')
    
    (Contributed by Raymond Hettinger.)
    
*   A principal feature of the unittest module is an effort to produce meaningful diagnostics when a test fails. When possible, the failure is recorded along with a diff of the output. This is especially helpful for analyzing log files of failed test runs. However, since diffs can sometime be voluminous, there is a new [`maxDiff`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.maxDiff "unittest.TestCase.maxDiff")
     attribute that sets maximum length of diffs displayed.
    
*   In addition, the method names in the module have undergone a number of clean-ups.
    
    For example, [`assertRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex "unittest.TestCase.assertRegex")
     is the new name for `assertRegexpMatches()` which was misnamed because the test uses [`re.search()`](https://docs.python.org/3/library/re.html#re.search "re.search")
    , not [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match")
    . Other methods using regular expressions are now named using short form “Regex” in preference to “Regexp” – this matches the names used in other unittest implementations, matches Python’s old name for the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
     module, and it has unambiguous camel-casing.
    
    (Contributed by Raymond Hettinger and implemented by Ezio Melotti.)
    
*   To improve consistency, some long-standing method aliases are being deprecated in favor of the preferred names:
    
    > | Old Name | Preferred Name |
    > | --- | --- |
    > | `assert_()` | [`assertTrue()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "unittest.TestCase.assertTrue") |
    > | `assertEquals()` | [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") |
    > | `assertNotEquals()` | [`assertNotEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual "unittest.TestCase.assertNotEqual") |
    > | `assertAlmostEquals()` | [`assertAlmostEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "unittest.TestCase.assertAlmostEqual") |
    > | `assertNotAlmostEquals()` | [`assertNotAlmostEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual "unittest.TestCase.assertNotAlmostEqual") |
    
    Likewise, the `TestCase.fail*` methods deprecated in Python 3.1 are expected to be removed in Python 3.3.
    
    (Contributed by Ezio Melotti; [bpo-9424](https://bugs.python.org/issue?@action=redirect&bpo=9424)
    .)
    
*   The `assertDictContainsSubset()` method was deprecated because it was misimplemented with the arguments in the wrong order. This created hard-to-debug optical illusions where tests like `TestCase().assertDictContainsSubset({'a':1, 'b':2}, {'a':1})` would fail.
    
    (Contributed by Raymond Hettinger.)
    

### random[¶](https://docs.python.org/3/whatsnew/3.2.html#random "Link to this heading")

The integer methods in the [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
 module now do a better job of producing uniform distributions. Previously, they computed selections with `int(n*random())` which had a slight bias whenever _n_ was not a power of two. Now, multiple selections are made from a range up to the next power of two and a selection is kept only when it falls within the range `0 <= x < n`. The functions and methods affected are [`randrange()`](https://docs.python.org/3/library/random.html#random.randrange "random.randrange")
, [`randint()`](https://docs.python.org/3/library/random.html#random.randint "random.randint")
, [`choice()`](https://docs.python.org/3/library/random.html#random.choice "random.choice")
, [`shuffle()`](https://docs.python.org/3/library/random.html#random.shuffle "random.shuffle")
 and [`sample()`](https://docs.python.org/3/library/random.html#random.sample "random.sample")
.

(Contributed by Raymond Hettinger; [bpo-9025](https://bugs.python.org/issue?@action=redirect&bpo=9025)
.)

### poplib[¶](https://docs.python.org/3/whatsnew/3.2.html#poplib "Link to this heading")

[`POP3_SSL`](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL "poplib.POP3_SSL")
 class now accepts a _context_ parameter, which is a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
 object allowing bundling SSL configuration options, certificates and private keys into a single (potentially long-lived) structure.

(Contributed by Giampaolo Rodolà; [bpo-8807](https://bugs.python.org/issue?@action=redirect&bpo=8807)
.)

### asyncore[¶](https://docs.python.org/3/whatsnew/3.2.html#asyncore "Link to this heading")

`asyncore.dispatcher` now provides a `handle_accepted()` method returning a `(sock, addr)` pair which is called when a connection has actually been established with a new remote endpoint. This is supposed to be used as a replacement for old `handle_accept()` and avoids the user to call `accept()` directly.

(Contributed by Giampaolo Rodolà; [bpo-6706](https://bugs.python.org/issue?@action=redirect&bpo=6706)
.)

### tempfile[¶](https://docs.python.org/3/whatsnew/3.2.html#tempfile "Link to this heading")

The [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories.")
 module has a new context manager, [`TemporaryDirectory`](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory "tempfile.TemporaryDirectory")
 which provides easy deterministic cleanup of temporary directories:

Copy

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary dir:', tmpdirname)

(Contributed by Neil Schemenauer and Nick Coghlan; [bpo-5178](https://bugs.python.org/issue?@action=redirect&bpo=5178)
.)

### inspect[¶](https://docs.python.org/3/whatsnew/3.2.html#inspect "Link to this heading")

*   The [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
     module has a new function [`getgeneratorstate()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorstate "inspect.getgeneratorstate")
     to easily identify the current state of a generator-iterator:
    
    Copy
    
    \>>> from inspect import getgeneratorstate
    \>>> def gen():
    ...     yield 'demo'
    ...
    \>>> g \= gen()
    \>>> getgeneratorstate(g)
    'GEN\_CREATED'
    \>>> next(g)
    'demo'
    \>>> getgeneratorstate(g)
    'GEN\_SUSPENDED'
    \>>> next(g, None)
    \>>> getgeneratorstate(g)
    'GEN\_CLOSED'
    
    (Contributed by Rodolpho Eckhardt and Nick Coghlan, [bpo-10220](https://bugs.python.org/issue?@action=redirect&bpo=10220)
    .)
    
*   To support lookups without the possibility of activating a dynamic attribute, the [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.")
     module has a new function, [`getattr_static()`](https://docs.python.org/3/library/inspect.html#inspect.getattr_static "inspect.getattr_static")
    . Unlike [`hasattr()`](https://docs.python.org/3/builtins/functions.html#hasattr "hasattr")
    , this is a true read-only search, guaranteed not to change state while it is searching:
    
    Copy
    
    \>>> class A:
    ...     @property
    ...     def f(self):
    ...         print('Running')
    ...         return 10
    ...
    \>>> a \= A()
    \>>> getattr(a, 'f')
    Running
    10
    \>>> inspect.getattr\_static(a, 'f')
    <property object at 0x1022bd788>
    

> (Contributed by Michael Foord.)

### pydoc[¶](https://docs.python.org/3/whatsnew/3.2.html#pydoc "Link to this heading")

The [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 module now provides a much-improved web server interface, as well as a new command-line option `-b` to automatically open a browser window to display that server:

Copy

$ pydoc3.2 \-b

(Contributed by Ron Adam; [bpo-2001](https://bugs.python.org/issue?@action=redirect&bpo=2001)
.)

### dis[¶](https://docs.python.org/3/whatsnew/3.2.html#dis "Link to this heading")

The [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
 module gained two new functions for inspecting code, [`code_info()`](https://docs.python.org/3/library/dis.html#dis.code_info "dis.code_info")
 and [`show_code()`](https://docs.python.org/3/library/dis.html#dis.show_code "dis.show_code")
. Both provide detailed code object information for the supplied function, method, source code string or code object. The former returns a string and the latter prints it:

Copy

\>>> import dis, random
\>>> dis.show\_code(random.choice)
Name:              choice
Filename:          /Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/random.py
Argument count:    2
Kw-only arguments: 0
Number of locals:  3
Stack size:        11
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: 'Choose a random element from a non-empty sequence.'
   1: 'Cannot choose from an empty sequence'
Names:
   0: \_randbelow
   1: len
   2: ValueError
   3: IndexError
Variable names:
   0: self
   1: seq
   2: i

In addition, the [`dis()`](https://docs.python.org/3/library/dis.html#dis.dis "dis.dis")
 function now accepts string arguments so that the common idiom `dis(compile(s, '', 'eval'))` can be shortened to `dis(s)`:

Copy

\>>> dis('3\*x+1 if x%2==1 else x//2')
  1           0 LOAD\_NAME                0 (x)
              3 LOAD\_CONST               0 (2)
              6 BINARY\_MODULO
              7 LOAD\_CONST               1 (1)
             10 COMPARE\_OP               2 (==)
             13 POP\_JUMP\_IF\_FALSE       28
             16 LOAD\_CONST               2 (3)
             19 LOAD\_NAME                0 (x)
             22 BINARY\_MULTIPLY
             23 LOAD\_CONST               1 (1)
             26 BINARY\_ADD
             27 RETURN\_VALUE
        >>   28 LOAD\_NAME                0 (x)
             31 LOAD\_CONST               0 (2)
             34 BINARY\_FLOOR\_DIVIDE
             35 RETURN\_VALUE

Taken together, these improvements make it easier to explore how CPython is implemented and to see for yourself what the language syntax does under-the-hood.

(Contributed by Nick Coghlan in [bpo-9147](https://bugs.python.org/issue?@action=redirect&bpo=9147)
.)

### dbm[¶](https://docs.python.org/3/whatsnew/3.2.html#dbm "Link to this heading")

All database modules now support the `get()` and `setdefault()` methods.

(Suggested by Ray Allen in [bpo-9523](https://bugs.python.org/issue?@action=redirect&bpo=9523)
.)

### ctypes[¶](https://docs.python.org/3/whatsnew/3.2.html#ctypes "Link to this heading")

A new type, [`ctypes.c_ssize_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ssize_t "ctypes.c_ssize_t")
 represents the C `ssize_t` datatype.

### site[¶](https://docs.python.org/3/whatsnew/3.2.html#site "Link to this heading")

The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module has three new functions useful for reporting on the details of a given Python installation.

*   [`getsitepackages()`](https://docs.python.org/3/library/site.html#site.getsitepackages "site.getsitepackages")
     lists all global site-packages directories.
    
*   [`getuserbase()`](https://docs.python.org/3/library/site.html#site.getuserbase "site.getuserbase")
     reports on the user’s base directory where data can be stored.
    
*   [`getusersitepackages()`](https://docs.python.org/3/library/site.html#site.getusersitepackages "site.getusersitepackages")
     reveals the user-specific site-packages directory path.
    

Copy

\>>> import site
\>>> site.getsitepackages()
\['/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/site-packages',\
 '/Library/Frameworks/Python.framework/Versions/3.2/lib/site-python',\
 '/Library/Python/3.2/site-packages'\]
\>>> site.getuserbase()
'/Users/raymondhettinger/Library/Python/3.2'
\>>> site.getusersitepackages()
'/Users/raymondhettinger/Library/Python/3.2/lib/python/site-packages'

Conveniently, some of site’s functionality is accessible directly from the command-line:

Copy

$ python \-m site \--user-base
/Users/raymondhettinger/.local
$ python \-m site \--user-site
/Users/raymondhettinger/.local/lib/python3.2/site-packages

(Contributed by Tarek Ziadé in [bpo-6693](https://bugs.python.org/issue?@action=redirect&bpo=6693)
.)

### sysconfig[¶](https://docs.python.org/3/whatsnew/3.2.html#sysconfig "Link to this heading")

The new [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
 module makes it straightforward to discover installation paths and configuration variables that vary across platforms and installations.

The module offers access simple access functions for platform and version information:

*   [`get_platform()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_platform "sysconfig.get_platform")
     returning values like _linux-i586_ or _macosx-10.6-ppc_.
    
*   [`get_python_version()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_python_version "sysconfig.get_python_version")
     returns a Python version string such as “3.2”.
    

It also provides access to the paths and variables corresponding to one of seven named schemes used by `distutils`. Those include _posix\_prefix_, _posix\_home_, _posix\_user_, _nt_, _nt\_user_, _os2_, _os2\_home_:

*   [`get_paths()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_paths "sysconfig.get_paths")
     makes a dictionary containing installation paths for the current installation scheme.
    
*   [`get_config_vars()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "sysconfig.get_config_vars")
     returns a dictionary of platform specific variables.
    

There is also a convenient command-line interface:

Copy

C:\\Python32>python -m sysconfig
Platform: "win32"
Python version: "3.2"
Current installation scheme: "nt"

Paths:
        data = "C:\\Python32"
        include = "C:\\Python32\\Include"
        platinclude = "C:\\Python32\\Include"
        platlib = "C:\\Python32\\Lib\\site-packages"
        platstdlib = "C:\\Python32\\Lib"
        purelib = "C:\\Python32\\Lib\\site-packages"
        scripts = "C:\\Python32\\Scripts"
        stdlib = "C:\\Python32\\Lib"

Variables:
        BINDIR = "C:\\Python32"
        BINLIBDEST = "C:\\Python32\\Lib"
        EXE = ".exe"
        INCLUDEPY = "C:\\Python32\\Include"
        LIBDEST = "C:\\Python32\\Lib"
        SO = ".pyd"
        VERSION = "32"
        abiflags = ""
        base = "C:\\Python32"
        exec\_prefix = "C:\\Python32"
        platbase = "C:\\Python32"
        prefix = "C:\\Python32"
        projectbase = "C:\\Python32"
        py\_version = "3.2"
        py\_version\_nodot = "32"
        py\_version\_short = "3.2"
        srcdir = "C:\\Python32"
        userbase = "C:\\Documents and Settings\\Raymond\\Application Data\\Python"

(Moved out of Distutils by Tarek Ziadé.)

### pdb[¶](https://docs.python.org/3/whatsnew/3.2.html#pdb "Link to this heading")

The [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")
 debugger module gained a number of usability improvements:

*   `pdb.py` now has a `-c` option that executes commands as given in a `.pdbrc` script file.
    
*   A `.pdbrc` script file can contain `continue` and `next` commands that continue debugging.
    
*   The [`Pdb`](https://docs.python.org/3/library/pdb.html#pdb.Pdb "pdb.Pdb")
     class constructor now accepts a _nosigint_ argument.
    
*   New commands: `l(list)`, `ll(long list)` and `source` for listing source code.
    
*   New commands: `display` and `undisplay` for showing or hiding the value of an expression if it has changed.
    
*   New command: `interact` for starting an interactive interpreter containing the global and local names found in the current scope.
    
*   Breakpoints can be cleared by breakpoint number.
    

(Contributed by Georg Brandl, Antonio Cuni and Ilya Sandler.)

### configparser[¶](https://docs.python.org/3/whatsnew/3.2.html#configparser "Link to this heading")

The [`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.")
 module was modified to improve usability and predictability of the default parser and its supported INI syntax. The old `ConfigParser` class was removed in favor of `SafeConfigParser` which has in turn been renamed to [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
. Support for inline comments is now turned off by default and section or option duplicates are not allowed in a single configuration source.

Config parsers gained a new API based on the mapping protocol:

Copy

\>>> parser \= ConfigParser()
\>>> parser.read\_string("""
... \[DEFAULT\]
... location = upper left
... visible = yes
... editable = no
... color = blue
...
... \[main\]
... title = Main Menu
... color = green
...
... \[options\]
... title = Options
... """)
\>>> parser\['main'\]\['color'\]
'green'
\>>> parser\['main'\]\['editable'\]
'no'
\>>> section \= parser\['options'\]
\>>> section\['title'\]
'Options'
\>>> section\['title'\] \= 'Options (editable: %(editable)s)'
\>>> section\['title'\]
'Options (editable: no)'

The new API is implemented on top of the classical API, so custom parser subclasses should be able to use it without modifications.

The INI file structure accepted by config parsers can now be customized. Users can specify alternative option/value delimiters and comment prefixes, change the name of the _DEFAULT_ section or switch the interpolation syntax.

There is support for pluggable interpolation including an additional interpolation handler [`ExtendedInterpolation`](https://docs.python.org/3/library/configparser.html#configparser.ExtendedInterpolation "configparser.ExtendedInterpolation")
:

Copy

\>>> parser \= ConfigParser(interpolation\=ExtendedInterpolation())
\>>> parser.read\_dict({'buildout': {'directory': '/home/ambv/zope9'},
...                   'custom': {'prefix': '/usr/local'}})
\>>> parser.read\_string("""
... \[buildout\]
... parts =
...   zope9
...   instance
... find-links =
...   ${buildout:directory}/downloads/dist
...
... \[zope9\]
... recipe = plone.recipe.zope9install
... location = /opt/zope
...
... \[instance\]
... recipe = plone.recipe.zope9instance
... zope9-location = ${zope9:location}
... zope-conf = ${custom:prefix}/etc/zope.conf
... """)
\>>> parser\['buildout'\]\['find-links'\]
'\\n/home/ambv/zope9/downloads/dist'
\>>> parser\['instance'\]\['zope-conf'\]
'/usr/local/etc/zope.conf'
\>>> instance \= parser\['instance'\]
\>>> instance\['zope-conf'\]
'/usr/local/etc/zope.conf'
\>>> instance\['zope9-location'\]
'/opt/zope'

A number of smaller features were also introduced, like support for specifying encoding in read operations, specifying fallback values for get-functions, or reading directly from dictionaries and strings.

(All changes contributed by Łukasz Langa.)

### urllib.parse[¶](https://docs.python.org/3/whatsnew/3.2.html#urllib-parse "Link to this heading")

A number of usability improvements were made for the [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.")
 module.

The [`urlparse()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse "urllib.parse.urlparse")
 function now supports [IPv6](https://en.wikipedia.org/wiki/IPv6)
 addresses as described in [**RFC 2732**](https://datatracker.ietf.org/doc/html/rfc2732.html)
:

Copy

\>>> import urllib.parse
\>>> urllib.parse.urlparse('http://\[dead:beef:cafe:5417:affe:8FA3:deaf:feed\]/foo/')
ParseResult(scheme='http',
            netloc='\[dead:beef:cafe:5417:affe:8FA3:deaf:feed\]',
            path='/foo/',
            params='',
            query='',
            fragment='')

The [`urldefrag()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urldefrag "urllib.parse.urldefrag")
 function now returns a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
:

Copy

\>>> r \= urllib.parse.urldefrag('http://python.org/about/#target')
\>>> r
DefragResult(url='http://python.org/about/', fragment='target')
\>>> r\[0\]
'http://python.org/about/'
\>>> r.fragment
'target'

And, the [`urlencode()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode "urllib.parse.urlencode")
 function is now much more flexible, accepting either a string or bytes type for the _query_ argument. If it is a string, then the _safe_, _encoding_, and _error_ parameters are sent to [`quote_plus()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote_plus "urllib.parse.quote_plus")
 for encoding:

Copy

\>>> urllib.parse.urlencode(\[\
...      ('type', 'telenovela'),\
...      ('name', '¿Dónde Está Elisa?')\],
...      encoding\='latin-1')
'type=telenovela&name=%BFD%F3nde+Est%E1+Elisa%3F'

As detailed in [Parsing ASCII Encoded Bytes](https://docs.python.org/3/library/urllib.parse.html#parsing-ascii-encoded-bytes)
, all the [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.")
 functions now accept ASCII-encoded byte strings as input, so long as they are not mixed with regular strings. If ASCII-encoded byte strings are given as parameters, the return types will also be an ASCII-encoded byte strings:

Copy

\>>> urllib.parse.urlparse(b'http://www.python.org:80/about/')
ParseResultBytes(scheme=b'http', netloc=b'www.python.org:80',
                 path=b'/about/', params=b'', query=b'', fragment=b'')

(Work by Nick Coghlan, Dan Mahn, and Senthil Kumaran in [bpo-2987](https://bugs.python.org/issue?@action=redirect&bpo=2987)
, [bpo-5468](https://bugs.python.org/issue?@action=redirect&bpo=5468)
, and [bpo-9873](https://bugs.python.org/issue?@action=redirect&bpo=9873)
.)

### mailbox[¶](https://docs.python.org/3/whatsnew/3.2.html#mailbox "Link to this heading")

Thanks to a concerted effort by R. David Murray, the [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
 module has been fixed for Python 3.2. The challenge was that mailbox had been originally designed with a text interface, but email messages are best represented with [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 because various parts of a message may have different encodings.

The solution harnessed the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
 package’s binary support for parsing arbitrary email messages. In addition, the solution required a number of API changes.

As expected, the [`add()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.add "mailbox.Mailbox.add")
 method for [`mailbox.Mailbox`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox "mailbox.Mailbox")
 objects now accepts binary input.

[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
 and text file input are deprecated. Also, string input will fail early if non-ASCII characters are used. Previously it would fail when the email was processed in a later step.

There is also support for binary output. The [`get_file()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_file "mailbox.Mailbox.get_file")
 method now returns a file in the binary mode (where it used to incorrectly set the file to text-mode). There is also a new [`get_bytes()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_bytes "mailbox.Mailbox.get_bytes")
 method that returns a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 representation of a message corresponding to a given _key_.

It is still possible to get non-binary output using the old API’s [`get_string()`](https://docs.python.org/3/library/mailbox.html#mailbox.Mailbox.get_string "mailbox.Mailbox.get_string")
 method, but that approach is not very useful. Instead, it is best to extract messages from a [`Message`](https://docs.python.org/3/library/mailbox.html#mailbox.Message "mailbox.Message")
 object or to load them from binary input.

(Contributed by R. David Murray, with efforts from Steffen Daode Nurpmeso and an initial patch by Victor Stinner in [bpo-9124](https://bugs.python.org/issue?@action=redirect&bpo=9124)
.)

### turtledemo[¶](https://docs.python.org/3/whatsnew/3.2.html#turtledemo "Link to this heading")

The demonstration code for the [`turtle`](https://docs.python.org/3/library/turtle.html#module-turtle "turtle: An educational framework for simple graphics applications")
 module was moved from the _Demo_ directory to main library. It includes over a dozen sample scripts with lively displays. Being on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
, it can now be run directly from the command-line:

Copy

$ python \-m turtledemo

(Moved from the Demo directory by Alexander Belopolsky in [bpo-10199](https://bugs.python.org/issue?@action=redirect&bpo=10199)
.)

Multi-threading[¶](https://docs.python.org/3/whatsnew/3.2.html#multi-threading "Link to this heading")

-------------------------------------------------------------------------------------------------------

*   The mechanism for serializing execution of concurrently running Python threads (generally known as the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
     or Global Interpreter Lock) has been rewritten. Among the objectives were more predictable switching intervals and reduced overhead due to lock contention and the number of ensuing system calls. The notion of a “check interval” to allow thread switches has been abandoned and replaced by an absolute duration expressed in seconds. This parameter is tunable through [`sys.setswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "sys.setswitchinterval")
    . It currently defaults to 5 milliseconds.
    
    Additional details about the implementation can be read from a [python-dev mailing-list message](https://mail.python.org/pipermail/python-dev/2009-October/093321.html)
     (however, “priority requests” as exposed in this message have not been kept for inclusion).
    
    (Contributed by Antoine Pitrou.)
    
*   Regular and recursive locks now accept an optional _timeout_ argument to their [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire")
     method. (Contributed by Antoine Pitrou; [bpo-7316](https://bugs.python.org/issue?@action=redirect&bpo=7316)
    .)
    
*   Similarly, [`threading.Semaphore.acquire()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire")
     also gained a _timeout_ argument. (Contributed by Torsten Landschoff; [bpo-850728](https://bugs.python.org/issue?@action=redirect&bpo=850728)
    .)
    
*   Regular and recursive lock acquisitions can now be interrupted by signals on platforms using Pthreads. This means that Python programs that deadlock while acquiring locks can be successfully killed by repeatedly sending SIGINT to the process (by pressing Ctrl+C in most shells). (Contributed by Reid Kleckner; [bpo-8844](https://bugs.python.org/issue?@action=redirect&bpo=8844)
    .)
    

Optimizations[¶](https://docs.python.org/3/whatsnew/3.2.html#optimizations "Link to this heading")

---------------------------------------------------------------------------------------------------

A number of small performance enhancements have been added:

*   Python’s peephole optimizer now recognizes patterns such `x in {1, 2, 3}` as being a test for membership in a set of constants. The optimizer recasts the [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
     as a [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
     and stores the pre-built constant.
    
    Now that the speed penalty is gone, it is practical to start writing membership tests using set-notation. This style is both semantically clear and operationally fast:
    
    Copy
    
    extension \= name.rpartition('.')\[2\]
    if extension in {'xml', 'html', 'xhtml', 'css'}:
        handle(name)
    
    (Patch and additional tests contributed by Dave Malcolm; [bpo-6690](https://bugs.python.org/issue?@action=redirect&bpo=6690)
    ).
    
*   Serializing and unserializing data using the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
     module is now several times faster.
    
    (Contributed by Alexandre Vassalotti, Antoine Pitrou and the Unladen Swallow team in [bpo-9410](https://bugs.python.org/issue?@action=redirect&bpo=9410)
     and [bpo-3873](https://bugs.python.org/issue?@action=redirect&bpo=3873)
    .)
    
*   The [Timsort algorithm](https://en.wikipedia.org/wiki/Timsort)
     used in [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
     and [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
     now runs faster and uses less memory when called with a [key function](https://docs.python.org/3/glossary.html#term-key-function)
    . Previously, every element of a list was wrapped with a temporary object that remembered the key value associated with each element. Now, two arrays of keys and values are sorted in parallel. This saves the memory consumed by the sort wrappers, and it saves time lost to delegating comparisons.
    
    (Patch by Daniel Stutzbach in [bpo-9915](https://bugs.python.org/issue?@action=redirect&bpo=9915)
    .)
    
*   JSON decoding performance is improved and memory consumption is reduced whenever the same string is repeated for multiple keys. Also, JSON encoding now uses the C speedups when the `sort_keys` argument is true.
    
    (Contributed by Antoine Pitrou in [bpo-7451](https://bugs.python.org/issue?@action=redirect&bpo=7451)
     and by Raymond Hettinger and Antoine Pitrou in [bpo-10314](https://bugs.python.org/issue?@action=redirect&bpo=10314)
    .)
    
*   Recursive locks (created with the [`threading.RLock()`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock")
     API) now benefit from a C implementation which makes them as fast as regular locks, and between 10x and 15x faster than their previous pure Python implementation.
    
    (Contributed by Antoine Pitrou; [bpo-3001](https://bugs.python.org/issue?@action=redirect&bpo=3001)
    .)
    
*   The fast-search algorithm in stringlib is now used by the [`split()`](https://docs.python.org/3/builtins/stdtypes.html#str.split "str.split")
    , [`rsplit()`](https://docs.python.org/3/builtins/stdtypes.html#str.rsplit "str.rsplit")
    , [`splitlines()`](https://docs.python.org/3/builtins/stdtypes.html#str.splitlines "str.splitlines")
     and [`replace()`](https://docs.python.org/3/builtins/stdtypes.html#str.replace "str.replace")
     methods on [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     and [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     objects. Likewise, the algorithm is also used by [`rfind()`](https://docs.python.org/3/builtins/stdtypes.html#str.rfind "str.rfind")
    , [`rindex()`](https://docs.python.org/3/builtins/stdtypes.html#str.rindex "str.rindex")
    , `rsplit()` and [`rpartition()`](https://docs.python.org/3/builtins/stdtypes.html#str.rpartition "str.rpartition")
    .
    
    (Patch by Florent Xicluna in [bpo-7622](https://bugs.python.org/issue?@action=redirect&bpo=7622)
     and [bpo-7462](https://bugs.python.org/issue?@action=redirect&bpo=7462)
    .)
    
*   Integer to string conversions now work two “digits” at a time, reducing the number of division and modulo operations.
    
    ([bpo-6713](https://bugs.python.org/issue?@action=redirect&bpo=6713)
     by Gawain Bolton, Mark Dickinson, and Victor Stinner.)
    

There were several other minor optimizations. Set differencing now runs faster when one operand is much larger than the other (patch by Andress Bennetts in [bpo-8685](https://bugs.python.org/issue?@action=redirect&bpo=8685)
). The `array.repeat()` method has a faster implementation ([bpo-1569291](https://bugs.python.org/issue?@action=redirect&bpo=1569291)
 by Alexander Belopolsky). The [`BaseHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler "http.server.BaseHTTPRequestHandler")
 has more efficient buffering ([bpo-3709](https://bugs.python.org/issue?@action=redirect&bpo=3709)
 by Andrew Schaaf). The [`operator.attrgetter()`](https://docs.python.org/3/library/operator.html#operator.attrgetter "operator.attrgetter")
 function has been sped-up ([bpo-10160](https://bugs.python.org/issue?@action=redirect&bpo=10160)
 by Christos Georgiou). And [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
 loads multi-line arguments a bit faster ([bpo-7113](https://bugs.python.org/issue?@action=redirect&bpo=7113)
 by Łukasz Langa).

Unicode[¶](https://docs.python.org/3/whatsnew/3.2.html#unicode "Link to this heading")

---------------------------------------------------------------------------------------

Python has been updated to [Unicode 6.0.0](https://unicode.org/versions/Unicode6.0.0/)
. The update to the standard adds over 2,000 new characters including [emoji](https://en.wikipedia.org/wiki/Emoji)
 symbols which are important for mobile phones.

In addition, the updated standard has altered the character properties for two Kannada characters (U+0CF1, U+0CF2) and one New Tai Lue numeric character (U+19DA), making the former eligible for use in identifiers while disqualifying the latter. For more information, see [Unicode Character Database Changes](https://www.unicode.org/versions/Unicode6.0.0/#Database_Changes)
.

Codecs[¶](https://docs.python.org/3/whatsnew/3.2.html#codecs "Link to this heading")

-------------------------------------------------------------------------------------

Support was added for _cp720_ Arabic DOS encoding ([bpo-1616979](https://bugs.python.org/issue?@action=redirect&bpo=1616979)
).

MBCS encoding no longer ignores the error handler argument. In the default strict mode, it raises an [`UnicodeDecodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")
 when it encounters an undecodable byte sequence and an [`UnicodeEncodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeEncodeError "UnicodeEncodeError")
 for an unencodable character.

The MBCS codec supports `'strict'` and `'ignore'` error handlers for decoding, and `'strict'` and `'replace'` for encoding.

To emulate Python3.1 MBCS encoding, select the `'ignore'` handler for decoding and the `'replace'` handler for encoding.

On Mac OS X, Python decodes command line arguments with `'utf-8'` rather than the locale encoding.

By default, [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
 uses `'utf-8'` encoding on Windows (instead of `'mbcs'`) and the `'surrogateescape'` error handler on all operating systems.

Documentation[¶](https://docs.python.org/3/whatsnew/3.2.html#documentation "Link to this heading")

---------------------------------------------------------------------------------------------------

The documentation continues to be improved.

*   A table of quick links has been added to the top of lengthy sections such as [Built-in functions](https://docs.python.org/3/builtins/functions.html#built-in-funcs)
    . In the case of [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.")
    , the links are accompanied by tables of cheatsheet-style summaries to provide an overview and memory jog without having to read all of the docs.
    
*   In some cases, the pure Python source code can be a helpful adjunct to the documentation, so now many modules now feature quick links to the latest version of the source code. For example, the [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
     module documentation has a quick link at the top labeled:
    
    > **Source code** [Lib/functools.py](https://github.com/python/cpython/tree/3.15/Lib/functools.py)
    > .
    
    (Contributed by Raymond Hettinger; see [rationale](https://rhettinger.wordpress.com/2011/01/28/open-your-source-more/)
    .)
    
*   The docs now contain more examples and recipes. In particular, [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
     module has an extensive section, [Regular expression examples](https://docs.python.org/3/library/re.html#re-examples)
    . Likewise, the [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.")
     module continues to be updated with new [Itertools Recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes)
    .
    
*   The [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
     module now has an auxiliary implementation in pure Python. No functionality was changed. This just provides an easier-to-read alternate implementation.
    
    (Contributed by Alexander Belopolsky in [bpo-9528](https://bugs.python.org/issue?@action=redirect&bpo=9528)
    .)
    
*   The unmaintained `Demo` directory has been removed. Some demos were integrated into the documentation, some were moved to the `Tools/demo` directory, and others were removed altogether.
    
    (Contributed by Georg Brandl in [bpo-7962](https://bugs.python.org/issue?@action=redirect&bpo=7962)
    .)
    

IDLE[¶](https://docs.python.org/3/whatsnew/3.2.html#idle "Link to this heading")

---------------------------------------------------------------------------------

*   The format menu now has an option to clean source files by stripping trailing whitespace.
    
    (Contributed by Raymond Hettinger; [bpo-5150](https://bugs.python.org/issue?@action=redirect&bpo=5150)
    .)
    
*   IDLE on Mac OS X now works with both Carbon AquaTk and Cocoa AquaTk.
    
    (Contributed by Kevin Walzer, Ned Deily, and Ronald Oussoren; [bpo-6075](https://bugs.python.org/issue?@action=redirect&bpo=6075)
    .)
    

Code Repository[¶](https://docs.python.org/3/whatsnew/3.2.html#code-repository "Link to this heading")

-------------------------------------------------------------------------------------------------------

In addition to the existing Subversion code repository at [https://svn.python.org](https://svn.python.org/)
 there is now a [Mercurial](https://www.mercurial-scm.org/)
 repository at [https://hg.python.org/](https://hg.python.org/)
.

After the 3.2 release, there are plans to switch to Mercurial as the primary repository. This distributed version control system should make it easier for members of the community to create and share external changesets. See [**PEP 385**](https://peps.python.org/pep-0385/)
 for details.

To learn to use the new version control system, see the [Quick Start](https://www.mercurial-scm.org/wiki/QuickStart)
 or the [Guide to Mercurial Workflows](https://www.mercurial-scm.org/guide)
.

Build and C API Changes[¶](https://docs.python.org/3/whatsnew/3.2.html#build-and-c-api-changes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Changes to Python’s build process and to the C API include:

*   The _idle_, _pydoc_ and _2to3_ scripts are now installed with a version-specific suffix on `make altinstall` ([bpo-10679](https://bugs.python.org/issue?@action=redirect&bpo=10679)
    ).
    
*   The C functions that access the Unicode Database now accept and return characters from the full Unicode range, even on narrow unicode builds (Py\_UNICODE\_TOLOWER, Py\_UNICODE\_ISDECIMAL, and others). A visible difference in Python is that [`unicodedata.numeric()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.numeric "unicodedata.numeric")
     now returns the correct value for large code points, and [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
     may consider more characters as printable.
    
    (Reported by Bupjoe Lee and fixed by Amaury Forgeot D’Arc; [bpo-5127](https://bugs.python.org/issue?@action=redirect&bpo=5127)
    .)
    
*   Computed gotos are now enabled by default on supported compilers (which are detected by the configure script). They can still be disabled selectively by specifying `--without-computed-gotos`.
    
    (Contributed by Antoine Pitrou; [bpo-9203](https://bugs.python.org/issue?@action=redirect&bpo=9203)
    .)
    
*   The option `--with-wctype-functions` was removed. The built-in unicode database is now used for all functions.
    
    (Contributed by Amaury Forgeot D’Arc; [bpo-9210](https://bugs.python.org/issue?@action=redirect&bpo=9210)
    .)
    
*   Hash values are now values of a new type, [`Py_hash_t`](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")
    , which is defined to be the same size as a pointer. Previously they were of type long, which on some 64-bit operating systems is still only 32 bits long. As a result of this fix, [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
     and [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
     can now hold more than `2**32` entries on builds with 64-bit pointers (previously, they could grow to that size but their performance degraded catastrophically).
    
    (Suggested by Raymond Hettinger and implemented by Benjamin Peterson; [bpo-9778](https://bugs.python.org/issue?@action=redirect&bpo=9778)
    .)
    
*   A new macro `Py_VA_COPY` copies the state of the variable argument list. It is equivalent to C99 _va\_copy_ but available on all Python platforms ([bpo-2443](https://bugs.python.org/issue?@action=redirect&bpo=2443)
    ).
    
*   A new C API function `PySys_SetArgvEx()` allows an embedded interpreter to set [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
     without also modifying [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
     ([bpo-5753](https://bugs.python.org/issue?@action=redirect&bpo=5753)
    ).
    
*   `PyEval_CallObject()` is now only available in macro form. The function declaration, which was kept for backwards compatibility reasons, is now removed – the macro was introduced in 1997 ([bpo-8276](https://bugs.python.org/issue?@action=redirect&bpo=8276)
    ).
    
*   There is a new function [`PyLong_AsLongLongAndOverflow()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongLongAndOverflow "PyLong_AsLongLongAndOverflow")
     which is analogous to [`PyLong_AsLongAndOverflow()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongAndOverflow "PyLong_AsLongAndOverflow")
    . They both serve to convert Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     into a native fixed-width type while providing detection of cases where the conversion won’t fit ([bpo-7767](https://bugs.python.org/issue?@action=redirect&bpo=7767)
    ).
    
*   The [`PyUnicode_CompareWithASCIIString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CompareWithASCIIString "PyUnicode_CompareWithASCIIString")
     function now returns _not equal_ if the Python string is _NUL_ terminated.
    
*   There is a new function [`PyErr_NewExceptionWithDoc()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewExceptionWithDoc "PyErr_NewExceptionWithDoc")
     that is like [`PyErr_NewException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException "PyErr_NewException")
     but allows a docstring to be specified. This lets C exceptions have the same self-documenting capabilities as their pure Python counterparts ([bpo-7033](https://bugs.python.org/issue?@action=redirect&bpo=7033)
    ).
    
*   When compiled with the `--with-valgrind` option, the pymalloc allocator will be automatically disabled when running under Valgrind. This gives improved memory leak detection when running under Valgrind, while taking advantage of pymalloc at other times ([bpo-2422](https://bugs.python.org/issue?@action=redirect&bpo=2422)
    ).
    
*   Removed the `O?` format from the _PyArg\_Parse_ functions. The format is no longer used and it had never been documented ([bpo-8837](https://bugs.python.org/issue?@action=redirect&bpo=8837)
    ).
    

There were a number of other small changes to the C-API. See the [Misc/NEWS](https://github.com/python/cpython/blob/v3.2.6/Misc/NEWS)
 file for a complete list.

Also, there were a number of updates to the Mac OS X build, see [Mac/BuildScript/README.txt](https://github.com/python/cpython/blob/v3.2.6/Mac/BuildScript/README.txt)
 for details. For users running a 32/64-bit build, there is a known problem with the default Tcl/Tk on Mac OS X 10.6. Accordingly, we recommend installing an updated alternative such as [ActiveState Tcl/Tk 8.5.9](https://web.archive.org/web/20101208191259/https://www.activestate.com/activetcl/downloads)
. See [https://www.python.org/download/mac/tcltk/](https://www.python.org/download/mac/tcltk/)
 for additional details.

Porting to Python 3.2[¶](https://docs.python.org/3/whatsnew/3.2.html#porting-to-python-3-2 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

This section lists previously described changes and other bugfixes that may require changes to your code:

*   The [`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.")
     module has a number of clean-ups. The major change is to replace the old `ConfigParser` class with long-standing preferred alternative `SafeConfigParser`. In addition there are a number of smaller incompatibilities:
    
    *   The interpolation syntax is now validated on [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
         and [`set()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.set "configparser.ConfigParser.set")
         operations. In the default interpolation scheme, only two tokens with percent signs are valid: `%(name)s` and `%%`, the latter being an escaped percent sign.
        
    *   The [`set()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.set "configparser.ConfigParser.set")
         and [`add_section()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.add_section "configparser.ConfigParser.add_section")
         methods now verify that values are actual strings. Formerly, unsupported types could be introduced unintentionally.
        
    *   Duplicate sections or options from a single source now raise either [`DuplicateSectionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "configparser.DuplicateSectionError")
         or [`DuplicateOptionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateOptionError "configparser.DuplicateOptionError")
        . Formerly, duplicates would silently overwrite a previous entry.
        
    *   Inline comments are now disabled by default so now the **;** character can be safely used in values.
        
    *   Comments now can be indented. Consequently, for **;** or **#** to appear at the start of a line in multiline values, it has to be interpolated. This keeps comment prefix characters in values from being mistaken as comments.
        
    *   `""` is now a valid value and is no longer automatically converted to an empty string. For empty strings, use `"option ="` in a line.
        
*   The `nntplib` module was reworked extensively, meaning that its APIs are often incompatible with the 3.1 APIs.
    
*   [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     objects can no longer be used as filenames; instead, they should be converted to [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   The `array.tostring()` and `array.fromstring()` have been renamed to [`array.tobytes()`](https://docs.python.org/3/library/array.html#array.array.tobytes "array.array.tobytes")
     and [`array.frombytes()`](https://docs.python.org/3/library/array.html#array.array.frombytes "array.array.frombytes")
     for clarity. The old names have been deprecated. (See [bpo-8990](https://bugs.python.org/issue?@action=redirect&bpo=8990)
    .)
    
*   `PyArg_Parse*()` functions:
    
    *   “t#” format has been removed: use “s#” or “s\*” instead
        
    *   “w” and “w#” formats has been removed: use “w\*” instead
        
*   The `PyCObject` type, deprecated in 3.1, has been removed. To wrap opaque C pointers in Python objects, the [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "PyCapsule")
     API should be used instead; the new type has a well-defined interface for passing typing safety information and a less complicated signature for calling a destructor.
    
*   The `sys.setfilesystemencoding()` function was removed because it had a flawed design.
    
*   The [`random.seed()`](https://docs.python.org/3/library/random.html#random.seed "random.seed")
     function and method now salt string seeds with an sha512 hash function. To access the previous version of _seed_ in order to reproduce Python 3.1 sequences, set the _version_ argument to _1_, `random.seed(s, version=1)`.
    
*   The previously deprecated `string.maketrans()` function has been removed in favor of the static methods [`bytes.maketrans()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.maketrans "bytes.maketrans")
     and [`bytearray.maketrans()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.maketrans "bytearray.maketrans")
    . This change solves the confusion around which types were supported by the [`string`](https://docs.python.org/3/library/string.html#module-string "string: Common string operations.")
     module. Now, [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    , [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     each have their own **maketrans** and **translate** methods with intermediate translation tables of the appropriate type.
    
    (Contributed by Georg Brandl; [bpo-5675](https://bugs.python.org/issue?@action=redirect&bpo=5675)
    .)
    
*   The previously deprecated `contextlib.nested()` function has been removed in favor of a plain [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     statement which can accept multiple context managers. The latter technique is faster (because it is built-in), and it does a better job finalizing multiple context managers when one of them raises an exception:
    
    Copy
    
    with open('mylog.txt') as infile, open('a.out', 'w') as outfile:
        for line in infile:
            if '<critical>' in line:
                outfile.write(line)
    
    (Contributed by Georg Brandl and Mattias Brändström; [appspot issue 53094](https://codereview.appspot.com/53094)
    .)
    
*   [`struct.pack()`](https://docs.python.org/3/library/struct.html#struct.pack "struct.pack")
     now only allows bytes for the `s` string pack code. Formerly, it would accept text arguments and implicitly encode them to bytes using UTF-8. This was problematic because it made assumptions about the correct encoding and because a variable-length encoding can fail when writing to fixed length segment of a structure.
    
    Code such as `struct.pack('<6sHHBBB', 'GIF87a', x, y)` should be rewritten with to use bytes instead of text, `struct.pack('<6sHHBBB', b'GIF87a', x, y)`.
    
    (Discovered by David Beazley and fixed by Victor Stinner; [bpo-10783](https://bugs.python.org/issue?@action=redirect&bpo=10783)
    .)
    
*   The [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree")
     class now raises an [`xml.etree.ElementTree.ParseError`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ParseError "xml.etree.ElementTree.ParseError")
     when a parse fails. Previously it raised an [`xml.parsers.expat.ExpatError`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError")
    .
    
*   The new, longer [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     value on floats may break doctests which rely on the old output format.
    
*   In [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
    , the default value for _close\_fds_ is now `True` under Unix; under Windows, it is `True` if the three standard streams are set to `None`, `False` otherwise. Previously, _close\_fds_ was always `False` by default, which produced difficult to solve bugs or race conditions when open file descriptors would leak into the child process.
    
*   Support for legacy HTTP 0.9 has been removed from [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
     and [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).")
    . Such support is still present on the server side (in [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
    ).
    
    (Contributed by Antoine Pitrou, [bpo-10711](https://bugs.python.org/issue?@action=redirect&bpo=10711)
    .)
    
*   SSL sockets in timeout mode now raise [`socket.timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "socket.timeout")
     when a timeout occurs, rather than a generic [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError")
    .
    
    (Contributed by Antoine Pitrou, [bpo-10272](https://bugs.python.org/issue?@action=redirect&bpo=10272)
    .)
    
*   The misleading functions `PyEval_AcquireLock()` and `PyEval_ReleaseLock()` have been officially deprecated. The thread-state aware APIs (such as [`PyEval_SaveThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_SaveThread "PyEval_SaveThread")
     and [`PyEval_RestoreThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_RestoreThread "PyEval_RestoreThread")
    ) should be used instead.
    
*   Due to security risks, `asyncore.handle_accept()` has been deprecated, and a new function, `asyncore.handle_accepted()`, was added to replace it.
    
    (Contributed by Giampaolo Rodola in [bpo-6706](https://bugs.python.org/issue?@action=redirect&bpo=6706)
    .)
    
*   Due to the new [GIL](https://docs.python.org/3/glossary.html#term-GIL)
     implementation, `PyEval_InitThreads()` cannot be called before [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
     anymore.
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [What’s New In Python 3.2](https://docs.python.org/3/whatsnew/3.2.html#)
    *   [PEP 384: Defining a Stable ABI](https://docs.python.org/3/whatsnew/3.2.html#pep-384-defining-a-stable-abi)
        
    *   [PEP 389: Argparse Command Line Parsing Module](https://docs.python.org/3/whatsnew/3.2.html#pep-389-argparse-command-line-parsing-module)
        
    *   [PEP 391: Dictionary Based Configuration for Logging](https://docs.python.org/3/whatsnew/3.2.html#pep-391-dictionary-based-configuration-for-logging)
        
    *   [PEP 3148: The `concurrent.futures` module](https://docs.python.org/3/whatsnew/3.2.html#pep-3148-the-concurrent-futures-module)
        
    *   [PEP 3147: PYC Repository Directories](https://docs.python.org/3/whatsnew/3.2.html#pep-3147-pyc-repository-directories)
        
    *   [PEP 3149: ABI Version Tagged .so Files](https://docs.python.org/3/whatsnew/3.2.html#pep-3149-abi-version-tagged-so-files)
        
    *   [PEP 3333: Python Web Server Gateway Interface v1.0.1](https://docs.python.org/3/whatsnew/3.2.html#pep-3333-python-web-server-gateway-interface-v1-0-1)
        
    *   [Other Language Changes](https://docs.python.org/3/whatsnew/3.2.html#other-language-changes)
        
    *   [New, Improved, and Deprecated Modules](https://docs.python.org/3/whatsnew/3.2.html#new-improved-and-deprecated-modules)
        *   [email](https://docs.python.org/3/whatsnew/3.2.html#email)
            
        *   [elementtree](https://docs.python.org/3/whatsnew/3.2.html#elementtree)
            
        *   [functools](https://docs.python.org/3/whatsnew/3.2.html#functools)
            
        *   [itertools](https://docs.python.org/3/whatsnew/3.2.html#itertools)
            
        *   [collections](https://docs.python.org/3/whatsnew/3.2.html#collections)
            
        *   [threading](https://docs.python.org/3/whatsnew/3.2.html#threading)
            
        *   [datetime and time](https://docs.python.org/3/whatsnew/3.2.html#datetime-and-time)
            
        *   [math](https://docs.python.org/3/whatsnew/3.2.html#math)
            
        *   [abc](https://docs.python.org/3/whatsnew/3.2.html#abc)
            
        *   [io](https://docs.python.org/3/whatsnew/3.2.html#io)
            
        *   [reprlib](https://docs.python.org/3/whatsnew/3.2.html#reprlib)
            
        *   [logging](https://docs.python.org/3/whatsnew/3.2.html#logging)
            
        *   [csv](https://docs.python.org/3/whatsnew/3.2.html#csv)
            
        *   [contextlib](https://docs.python.org/3/whatsnew/3.2.html#contextlib)
            
        *   [decimal and fractions](https://docs.python.org/3/whatsnew/3.2.html#decimal-and-fractions)
            
        *   [ftp](https://docs.python.org/3/whatsnew/3.2.html#ftp)
            
        *   [popen](https://docs.python.org/3/whatsnew/3.2.html#popen)
            
        *   [select](https://docs.python.org/3/whatsnew/3.2.html#select)
            
        *   [gzip and zipfile](https://docs.python.org/3/whatsnew/3.2.html#gzip-and-zipfile)
            
        *   [tarfile](https://docs.python.org/3/whatsnew/3.2.html#tarfile)
            
        *   [hashlib](https://docs.python.org/3/whatsnew/3.2.html#hashlib)
            
        *   [ast](https://docs.python.org/3/whatsnew/3.2.html#ast)
            
        *   [os](https://docs.python.org/3/whatsnew/3.2.html#os)
            
        *   [shutil](https://docs.python.org/3/whatsnew/3.2.html#shutil)
            
        *   [sqlite3](https://docs.python.org/3/whatsnew/3.2.html#sqlite3)
            
        *   [html](https://docs.python.org/3/whatsnew/3.2.html#html)
            
        *   [socket](https://docs.python.org/3/whatsnew/3.2.html#socket)
            
        *   [ssl](https://docs.python.org/3/whatsnew/3.2.html#ssl)
            
        *   [nntp](https://docs.python.org/3/whatsnew/3.2.html#nntp)
            
        *   [certificates](https://docs.python.org/3/whatsnew/3.2.html#certificates)
            
        *   [imaplib](https://docs.python.org/3/whatsnew/3.2.html#imaplib)
            
        *   [http.client](https://docs.python.org/3/whatsnew/3.2.html#http-client)
            
        *   [unittest](https://docs.python.org/3/whatsnew/3.2.html#unittest)
            
        *   [random](https://docs.python.org/3/whatsnew/3.2.html#random)
            
        *   [poplib](https://docs.python.org/3/whatsnew/3.2.html#poplib)
            
        *   [asyncore](https://docs.python.org/3/whatsnew/3.2.html#asyncore)
            
        *   [tempfile](https://docs.python.org/3/whatsnew/3.2.html#tempfile)
            
        *   [inspect](https://docs.python.org/3/whatsnew/3.2.html#inspect)
            
        *   [pydoc](https://docs.python.org/3/whatsnew/3.2.html#pydoc)
            
        *   [dis](https://docs.python.org/3/whatsnew/3.2.html#dis)
            
        *   [dbm](https://docs.python.org/3/whatsnew/3.2.html#dbm)
            
        *   [ctypes](https://docs.python.org/3/whatsnew/3.2.html#ctypes)
            
        *   [site](https://docs.python.org/3/whatsnew/3.2.html#site)
            
        *   [sysconfig](https://docs.python.org/3/whatsnew/3.2.html#sysconfig)
            
        *   [pdb](https://docs.python.org/3/whatsnew/3.2.html#pdb)
            
        *   [configparser](https://docs.python.org/3/whatsnew/3.2.html#configparser)
            
        *   [urllib.parse](https://docs.python.org/3/whatsnew/3.2.html#urllib-parse)
            
        *   [mailbox](https://docs.python.org/3/whatsnew/3.2.html#mailbox)
            
        *   [turtledemo](https://docs.python.org/3/whatsnew/3.2.html#turtledemo)
            
    *   [Multi-threading](https://docs.python.org/3/whatsnew/3.2.html#multi-threading)
        
    *   [Optimizations](https://docs.python.org/3/whatsnew/3.2.html#optimizations)
        
    *   [Unicode](https://docs.python.org/3/whatsnew/3.2.html#unicode)
        
    *   [Codecs](https://docs.python.org/3/whatsnew/3.2.html#codecs)
        
    *   [Documentation](https://docs.python.org/3/whatsnew/3.2.html#documentation)
        
    *   [IDLE](https://docs.python.org/3/whatsnew/3.2.html#idle)
        
    *   [Code Repository](https://docs.python.org/3/whatsnew/3.2.html#code-repository)
        
    *   [Build and C API Changes](https://docs.python.org/3/whatsnew/3.2.html#build-and-c-api-changes)
        
    *   [Porting to Python 3.2](https://docs.python.org/3/whatsnew/3.2.html#porting-to-python-3-2)
        

#### Previous topic

[What’s New In Python 3.3](https://docs.python.org/3/whatsnew/3.3.html "previous chapter")

#### Next topic

[What’s New In Python 3.1](https://docs.python.org/3/whatsnew/3.1.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+New+In+Python+3.2&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F3.2.html&pagesource=whatsnew%2F3.2.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/3.2.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.1.html "What’s New In Python 3.1")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.3.html "What’s New In Python 3.3")
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
*   [What’s New In Python 3.2](https://docs.python.org/3/whatsnew/3.2.html)
    
*    
    
    |
*   Theme Auto Light Dark |