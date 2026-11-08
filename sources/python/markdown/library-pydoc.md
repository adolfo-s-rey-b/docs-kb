### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/devmode.html "Python Development Mode")
     |
*   [previous](https://docs.python.org/3/library/typing.html "typing — Support for type hints")
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
*   [Development Tools](https://docs.python.org/3/library/development.html)
     »
*   [`pydoc` — Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`pydoc` — Documentation generator and online help system[¶](https://docs.python.org/3/library/pydoc.html#module-pydoc "Link to this heading")

==============================================================================================================================================

**Source code:** [Lib/pydoc.py](https://github.com/python/cpython/tree/3.15/Lib/pydoc.py)

* * *

The `pydoc` module automatically generates documentation from Python modules. The documentation can be presented as pages of text on the console, served to a web browser, or saved to HTML files.

For modules, classes, functions and methods, the displayed documentation is derived from the docstring (i.e. the [`__doc__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__doc__ "definition.__doc__")
 attribute) of the object, and recursively of its documentable members. If there is no docstring, `pydoc` tries to obtain a description from the block of comment lines just above the definition of the class, function or method in the source file, or at the top of the module (see [`inspect.getcomments()`](https://docs.python.org/3/library/inspect.html#inspect.getcomments "inspect.getcomments")
).

The built-in function [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
 invokes the online help system in the interactive interpreter, which uses `pydoc` to generate its documentation as text on the console. The same text documentation can also be viewed from outside the Python interpreter by running **pydoc** as a script at the operating system’s command prompt. For example, running

Copy

python \-m pydoc sys

at a shell prompt will display documentation on the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module, in a style similar to the manual pages shown by the Unix **man** command. The argument to **pydoc** can be the name of a function, module, or package, or a dotted reference to a class, method, or function within a module or module in a package. If the argument to **pydoc** looks like a path (that is, it contains the path separator for your operating system, such as a slash in Unix), and refers to an existing Python source file, then documentation is produced for that file.

Note

In order to find objects and their documentation, `pydoc` imports the module(s) to be documented. Therefore, any code on module level will be executed on that occasion. Use an `if __name__ == '__main__':` guard to only execute code when a file is invoked as a script and not just imported.

When printing output to the console, **pydoc** attempts to paginate the output for easier reading. If either the `MANPAGER` or the `PAGER` environment variable is set, **pydoc** will use its value as a pagination program. When both are set, `MANPAGER` is used.

Specifying a `-w` flag before the argument will cause HTML documentation to be written out to a file in the current directory, instead of displaying text on the console.

Specifying a `-k` flag before the argument will search the synopsis lines of all available modules for the keyword given as the argument, again in a manner similar to the Unix **man** command. The synopsis line of a module is the first line of its documentation string.

You can also use **pydoc** to start an HTTP server on the local machine that will serve documentation to visiting web browsers. **python -m pydoc -p 1234** will start a HTTP server on port 1234, allowing you to browse the documentation at `http://localhost:1234/` in your preferred web browser. Specifying `0` as the port number will select an arbitrary unused port.

Warning

The `pydoc` HTTP server is intended for local use during development and is not suitable for production use.

**python -m pydoc -n <hostname>** will start the server listening at the given hostname. By default the hostname is ‘localhost’ but if you want the server to be reached from other machines, you may want to change the host name that the server responds to. During development this is especially useful if you want to run pydoc from within a container.

**python -m pydoc -b** will start the server and additionally open a web browser to a module index page. Each served page has a navigation bar at the top where you can _Get_ help on an individual item, _Search_ all modules with a keyword in their synopsis line, and go to the _Module index_, _Topics_ and _Keywords_ pages.

When **pydoc** generates documentation, it uses the current environment and path to locate modules. Thus, invoking **pydoc spam** documents precisely the version of the module you would get if you started the Python interpreter and typed `import spam`.

Module docs for core modules are assumed to reside in `https://docs.python.org/X.Y/library/` where `X` and `Y` are the major and minor version numbers of the Python interpreter. This can be overridden by setting the `PYTHONDOCS` environment variable to a different URL or to a local directory containing the Library Reference Manual pages.

Changed in version 3.2: Added the `-b` option.

Changed in version 3.3: The `-g` command line option was removed.

Changed in version 3.4: `pydoc` now uses [`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 rather than [`inspect.getfullargspec()`](https://docs.python.org/3/library/inspect.html#inspect.getfullargspec "inspect.getfullargspec")
 to extract signature information from callables.

Changed in version 3.7: Added the `-n` option.

#### Previous topic

[`typing` — Support for type hints](https://docs.python.org/3/library/typing.html "previous chapter")

#### Next topic

[Python Development Mode](https://docs.python.org/3/library/devmode.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pydoc+%E2%80%94+Documentation+generator+and+online+help+system&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpydoc.html&pagesource=library%2Fpydoc.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/pydoc.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/devmode.html "Python Development Mode")
     |
*   [previous](https://docs.python.org/3/library/typing.html "typing — Support for type hints")
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
*   [Development Tools](https://docs.python.org/3/library/development.html)
     »
*   [`pydoc` — Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html)
    
*    
    
    |
*   Theme Auto Light Dark |