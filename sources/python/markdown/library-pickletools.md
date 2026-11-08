### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/windows.html "MS Windows Specific Services")
     |
*   [previous](https://docs.python.org/3/library/dis.html "dis — Disassembler for Python bytecode")
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
*   [Python Language Services](https://docs.python.org/3/library/language.html)
     »
*   [`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`pickletools` — Tools for pickle developers[¶](https://docs.python.org/3/library/pickletools.html#module-pickletools "Link to this heading")

=============================================================================================================================================

**Source code:** [Lib/pickletools.py](https://github.com/python/cpython/tree/3.15/Lib/pickletools.py)

* * *

This module contains various constants relating to the intimate details of the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 module, some lengthy comments about the implementation, and a few useful functions for analyzing pickled data. The contents of this module are useful for Python core developers who are working on the `pickle`; ordinary users of the `pickle` module probably won’t find the `pickletools` module relevant.

Command-line usage[¶](https://docs.python.org/3/library/pickletools.html#command-line-usage "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Added in version 3.2.

When invoked from the command line, `python -m pickletools` will disassemble the contents of one or more pickle files. Note that if you want to see the Python object stored in the pickle rather than the details of pickle format, you may want to use `-m pickle` instead. However, when the pickle file that you want to examine comes from an untrusted source, `-m pickletools` is a safer option because it does not execute pickle bytecode.

For example, with a tuple `(1, 2)` pickled in file `x.pickle`:

Copy

$ python \-m pickle x.pickle
(1, 2)

$ python \-m pickletools x.pickle
    0: \\x80 PROTO      3
    2: K    BININT1    1
    4: K    BININT1    2
    6: \\x86 TUPLE2
    7: q    BINPUT     0
    9: .    STOP
highest protocol among opcodes = 2

### Command-line options[¶](https://docs.python.org/3/library/pickletools.html#command-line-options "Link to this heading")

\-a, \--annotate[¶](https://docs.python.org/3/library/pickletools.html#cmdoption-pickletools-a "Link to this definition")

Annotate each line with a short opcode description.

\-o, \--output\=<file>[¶](https://docs.python.org/3/library/pickletools.html#cmdoption-pickletools-o "Link to this definition")

Name of a file where the output should be written.

\-l, \--indentlevel\=<num>[¶](https://docs.python.org/3/library/pickletools.html#cmdoption-pickletools-l "Link to this definition")

The number of blanks by which to indent a new MARK level.

\-m, \--memo[¶](https://docs.python.org/3/library/pickletools.html#cmdoption-pickletools-m "Link to this definition")

When multiple objects are disassembled, preserve memo between disassemblies.

\-p, \--preamble\=<preamble>[¶](https://docs.python.org/3/library/pickletools.html#cmdoption-pickletools-p "Link to this definition")

When more than one pickle file is specified, print given preamble before each disassembly.

pickle\_file[¶](https://docs.python.org/3/library/pickletools.html#cmdoption-pickletools-arg-pickle_file "Link to this definition")

A pickle file to read, or `-` to indicate reading from standard input.

Added in version 3.15: Output is in color by default and can be [controlled using environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
.

Programmatic interface[¶](https://docs.python.org/3/library/pickletools.html#programmatic-interface "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

pickletools.dis(_pickle_, _out\=None_, _memo\=None_, _indentlevel\=4_, _annotate\=0_)[¶](https://docs.python.org/3/library/pickletools.html#pickletools.dis "Link to this definition")

Outputs a symbolic disassembly of the pickle to the file-like object _out_, defaulting to `sys.stdout`. _pickle_ can be a string or a file-like object. _memo_ can be a Python dictionary that will be used as the pickle’s memo; it can be used to perform disassemblies across multiple pickles created by the same pickler. Successive levels, indicated by `MARK` opcodes in the stream, are indented by _indentlevel_ spaces. If a nonzero value is given to _annotate_, each opcode in the output is annotated with a short description. The value of _annotate_ is used as a hint for the column where annotation should start.

Changed in version 3.2: Added the _annotate_ parameter.

pickletools.genops(_pickle_)[¶](https://docs.python.org/3/library/pickletools.html#pickletools.genops "Link to this definition")

Provides an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 over all of the opcodes in a pickle, returning a sequence of `(opcode, arg, pos)` triples. _opcode_ is an instance of an `OpcodeInfo` class; _arg_ is the decoded value, as a Python object, of the opcode’s argument; _pos_ is the position at which this opcode is located. _pickle_ can be a string or a file-like object.

pickletools.optimize(_picklestring_)[¶](https://docs.python.org/3/library/pickletools.html#pickletools.optimize "Link to this definition")

Returns a new equivalent pickle string after eliminating unused `PUT` opcodes. The optimized pickle is shorter, takes less transmission time, requires less storage space, and unpickles more efficiently.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html#)
    *   [Command-line usage](https://docs.python.org/3/library/pickletools.html#command-line-usage)
        *   [Command-line options](https://docs.python.org/3/library/pickletools.html#command-line-options)
            
    *   [Programmatic interface](https://docs.python.org/3/library/pickletools.html#programmatic-interface)
        

#### Previous topic

[`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html "previous chapter")

#### Next topic

[MS Windows Specific Services](https://docs.python.org/3/library/windows.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pickletools+%E2%80%94+Tools+for+pickle+developers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpickletools.html&pagesource=library%2Fpickletools.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/pickletools.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/windows.html "MS Windows Specific Services")
     |
*   [previous](https://docs.python.org/3/library/dis.html "dis — Disassembler for Python bytecode")
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
*   [Python Language Services](https://docs.python.org/3/library/language.html)
     »
*   [`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html)
    
*    
    
    |
*   Theme Auto Light Dark |