### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/profile.html "profile — Pure Python profiler")
     |
*   [previous](https://docs.python.org/3/library/superseded.html "Superseded modules")
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
*   [Superseded modules](https://docs.python.org/3/library/superseded.html)
     »
*   [`getopt` — C-style parser for command line options](https://docs.python.org/3/library/getopt.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`getopt` — C-style parser for command line options[¶](https://docs.python.org/3/library/getopt.html#module-getopt "Link to this heading")

==========================================================================================================================================

**Source code:** [Lib/getopt.py](https://github.com/python/cpython/tree/3.15/Lib/getopt.py)

Note

This module is considered feature complete. A more declarative and extensible alternative to this API is provided in the [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
 module. Further functional enhancements for command line parameter processing are provided either as third party modules on PyPI, or else as features in the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
 module.

* * *

This module helps scripts to parse the command line arguments in `sys.argv`. It supports the same conventions as the Unix `getopt()` function (including the special meanings of arguments of the form ‘`-`’ and ‘`--`‘). Long options similar to those supported by GNU software may be used as well via an optional third argument.

Users who are unfamiliar with the Unix `getopt()` function should consider using the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
 module instead. Users who are familiar with the Unix `getopt()` function, but would like to get equivalent behavior while writing less code and getting better help and error messages should consider using the [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
 module. See [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parser)
 for additional details.

This module provides two functions and an exception:

getopt.getopt(_args_, _shortopts_, _longopts\=\[\]_)[¶](https://docs.python.org/3/library/getopt.html#getopt.getopt "Link to this definition")

Parses command line options and parameter list. _args_ is the argument list to be parsed, without the leading reference to the running program. Typically, this means `sys.argv[1:]`. _shortopts_ is the string of option letters that the script wants to recognize, with options that require an argument followed by a colon (`':'`) and options that accept an optional argument followed by two colons (`'::'`); i.e., the same format that Unix `getopt()` uses.

Note

Unlike GNU `getopt()`, after a non-option argument, all further arguments are considered also non-options. This is similar to the way non-GNU Unix systems work.

_longopts_, if specified, must be a list of strings with the names of the long options which should be supported. The leading `'--'` characters should not be included in the option name. Long options which require an argument should be followed by an equal sign (`'='`). Long options which accept an optional argument should be followed by an equal sign and question mark (`'=?'`). To accept only long options, _shortopts_ should be an empty string. Long options on the command line can be recognized so long as they provide a prefix of the option name that matches exactly one of the accepted options. For example, if _longopts_ is `['foo', 'frob']`, the option `--fo` will match as `--foo`, but `--f` will not match uniquely, so [`GetoptError`](https://docs.python.org/3/library/getopt.html#getopt.GetoptError "getopt.GetoptError")
 will be raised.

If _longopts_ is a string it gets treated as a list of a single element.

The return value consists of two elements: the first is a list of `(option, value)` pairs; the second is the list of program arguments left after the option list was stripped (this is a trailing slice of _args_). Each option-and-value pair returned has the option as its first element, prefixed with a hyphen for short options (e.g., `'-x'`) or two hyphens for long options (e.g., `'--long-option'`), and the option argument as its second element, or an empty string if the option has no argument. The options occur in the list in the same order in which they were found, thus allowing multiple occurrences. Long and short options may be mixed.

Changed in version 3.14: Optional arguments are supported.

getopt.gnu\_getopt(_args_, _shortopts_, _longopts\=\[\]_)[¶](https://docs.python.org/3/library/getopt.html#getopt.gnu_getopt "Link to this definition")

This function works like [`getopt()`](https://docs.python.org/3/library/getopt.html#getopt.getopt "getopt.getopt")
, except that GNU style scanning mode is used by default. This means that option and non-option arguments may be intermixed. The `getopt()` function stops processing options as soon as a non-option argument is encountered.

If the first character of the option string is `'+'`, or if the environment variable `POSIXLY_CORRECT` is set, then option processing stops as soon as a non-option argument is encountered.

If the first character of the option string is `'-'`, non-option arguments that are followed by options are added to the list of option-and-value pairs as a pair that has `None` as its first element and the list of non-option arguments as its second element. The second element of the `gnu_getopt()` result is a list of program arguments after the last option.

Changed in version 3.14: Support for returning intermixed options and non-option arguments in order.

exception getopt.GetoptError[¶](https://docs.python.org/3/library/getopt.html#getopt.GetoptError "Link to this definition")

This is raised when an unrecognized option is found in the argument list or when an option requiring an argument is given none. The argument to the exception is a string indicating the cause of the error. For long options, an argument given to an option which does not require one will also cause this exception to be raised. The attributes `msg` and `opt` give the error message and related option; if there is no specific option to which the exception relates, `opt` is an empty string.

exception getopt.error[¶](https://docs.python.org/3/library/getopt.html#getopt.error "Link to this definition")

Alias for [`GetoptError`](https://docs.python.org/3/library/getopt.html#getopt.GetoptError "getopt.GetoptError")
; for backward compatibility.

An example using only Unix style options:

Copy

\>>> import getopt
\>>> args \= '-a -b -cfoo -d bar a1 a2'.split()
\>>> args
\['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2'\]
\>>> optlist, args \= getopt.getopt(args, 'abc:d:')
\>>> optlist
\[('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')\]
\>>> args
\['a1', 'a2'\]

Using long option names is equally easy:

Copy

\>>> s \= '--condition=foo --testing --output-file abc.def -x a1 a2'
\>>> args \= s.split()
\>>> args
\['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2'\]
\>>> optlist, args \= getopt.getopt(args, 'x', \[\
...     'condition=', 'output-file=', 'testing'\])
\>>> optlist
\[('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')\]
\>>> args
\['a1', 'a2'\]

Optional arguments should be specified explicitly:

Copy

\>>> s \= '-Con -C --color=off --color a1 a2'
\>>> args \= s.split()
\>>> args
\['-Con', '-C', '--color=off', '--color', 'a1', 'a2'\]
\>>> optlist, args \= getopt.getopt(args, 'C::', \['color=?'\])
\>>> optlist
\[('-C', 'on'), ('-C', ''), ('--color', 'off'), ('--color', '')\]
\>>> args
\['a1', 'a2'\]

The order of options and non-option arguments can be preserved:

Copy

\>>> s \= 'a1 -x a2 a3 a4 --long a5 a6'
\>>> args \= s.split()
\>>> args
\['a1', '-x', 'a2', 'a3', 'a4', '--long', 'a5', 'a6'\]
\>>> optlist, args \= getopt.gnu\_getopt(args, '-x:', \['long='\])
\>>> optlist
\[(None, \['a1'\]), ('-x', 'a2'), (None, \['a3', 'a4'\]), ('--long', 'a5')\]
\>>> args
\['a6'\]

In a script, typical usage is something like this:

Copy

import getopt, sys

def main():
    try:
        opts, args \= getopt.getopt(sys.argv\[1:\], "ho:v", \["help", "output="\])
    except getopt.GetoptError as err:
        \# print help information and exit:
        print(err)  \# will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output \= None
    verbose \= False
    for o, a in opts:
        if o \== "-v":
            verbose \= True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output \= a
        else:
            assert False, "unhandled option"
    process(args, output\=output, verbose\=verbose)

if \_\_name\_\_ \== "\_\_main\_\_":
    main()

Note that an equivalent command line interface could be produced with less code and more informative help and error messages by using the [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
 module:

Copy

import optparse

if \_\_name\_\_ \== '\_\_main\_\_':
    parser \= optparse.OptionParser()
    parser.add\_option('-o', '--output')
    parser.add\_option('-v', dest\='verbose', action\='store\_true')
    opts, args \= parser.parse\_args()
    process(args, output\=opts.output, verbose\=opts.verbose)

A roughly equivalent command line interface for this case can also be produced by using the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
 module:

Copy

import argparse

if \_\_name\_\_ \== '\_\_main\_\_':
    parser \= argparse.ArgumentParser()
    parser.add\_argument('-o', '--output')
    parser.add\_argument('-v', dest\='verbose', action\='store\_true')
    parser.add\_argument('rest', nargs\='\*')
    args \= parser.parse\_args()
    process(args.rest, output\=args.output, verbose\=args.verbose)

See [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parser)
 for details on how the `argparse` version of this code differs in behaviour from the `optparse` (and `getopt`) version.

See also

Module [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")

Declarative command line option parsing.

Module [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")

More opinionated command line option and argument parsing library.

#### Previous topic

[Superseded modules](https://docs.python.org/3/library/superseded.html "previous chapter")

#### Next topic

[`profile` — Pure Python profiler](https://docs.python.org/3/library/profile.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=getopt+%E2%80%94+C-style+parser+for+command+line+options&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgetopt.html&pagesource=library%2Fgetopt.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/getopt.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/profile.html "profile — Pure Python profiler")
     |
*   [previous](https://docs.python.org/3/library/superseded.html "Superseded modules")
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
*   [Superseded modules](https://docs.python.org/3/library/superseded.html)
     »
*   [`getopt` — C-style parser for command line options](https://docs.python.org/3/library/getopt.html)
    
*    
    
    |
*   Theme Auto Light Dark |