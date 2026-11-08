### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/argparse.html "Argparse Tutorial")
     |
*   [previous](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries")
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
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
     »
*   [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`argparse` — Parser for command-line options, arguments and subcommands[¶](https://docs.python.org/3/library/argparse.html#module-argparse "Link to this heading")

===================================================================================================================================================================

Added in version 3.2.

**Source code:** [Lib/argparse.py](https://github.com/python/cpython/tree/3.15/Lib/argparse.py)

Note

While `argparse` is the default recommended standard library module for implementing basic command line applications, authors with more exacting requirements for exactly how their command line applications behave may find it doesn’t provide the necessary level of control. Refer to [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parser)
 for alternatives to consider when `argparse` doesn’t support behaviors that the application requires (such as entirely disabling support for interspersed options and positional arguments, or accepting option parameter values that start with `-` even when they correspond to another defined option).

* * *

The `argparse` module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and `argparse` will figure out how to parse those out of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
. The `argparse` module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments.

The `argparse` module’s support for command-line interfaces is built around an instance of [`argparse.ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
. It is a container for argument specifications and has options that apply to the parser as whole:

Copy

parser \= argparse.ArgumentParser(
                    prog\='ProgramName',
                    description\='What the program does',
                    epilog\='Text at the bottom of help')

The [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 method attaches individual argument specifications to the parser. It supports positional arguments, options that accept values, and on/off flags:

Copy

parser.add\_argument('filename')           \# positional argument
parser.add\_argument('-c', '--count')      \# option that takes a value
parser.add\_argument('-v', '--verbose',
                    action\='store\_true')  \# on/off flag

The [`ArgumentParser.parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 method runs the parser and places the extracted data in a [`argparse.Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
 object:

Copy

args \= parser.parse\_args()
print(args.filename, args.count, args.verbose)

Note

If you’re looking for a guide about how to upgrade [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
 code to `argparse`, see [Upgrading Optparse Code](https://docs.python.org/3/howto/argparse-optparse.html#upgrading-optparse-code)
.

ArgumentParser objects[¶](https://docs.python.org/3/library/argparse.html#argumentparser-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

class argparse.ArgumentParser(_prog\=None_, _usage\=None_, _description\=None_, _epilog\=None_, _parents\=\[\]_, _formatter\_class\=argparse.HelpFormatter_, _prefix\_chars\='-'_, _fromfile\_prefix\_chars\=None_, _argument\_default\=None_, _conflict\_handler\='error'_, _add\_help\=True_, _allow\_abbrev\=True_, _exit\_on\_error\=True_, _\*_, _suggest\_on\_error\=True_, _color\=True_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "Link to this definition")

Create a new `ArgumentParser` object. All parameters should be passed as keyword arguments. Each parameter has its own more detailed description below, but in short they are:

*   [prog](https://docs.python.org/3/library/argparse.html#prog)
     - The name of the program (default: generated from the `__main__` module attributes and `sys.argv[0]`)
    
*   [usage](https://docs.python.org/3/library/argparse.html#usage)
     - The string describing the program usage (default: generated from arguments added to parser)
    
*   [description](https://docs.python.org/3/library/argparse.html#description)
     - Text to display before the argument help (by default, no text)
    
*   [epilog](https://docs.python.org/3/library/argparse.html#epilog)
     - Text to display after the argument help (by default, no text)
    
*   [parents](https://docs.python.org/3/library/argparse.html#parents)
     - A list of `ArgumentParser` objects whose arguments should also be included
    
*   [formatter\_class](https://docs.python.org/3/library/argparse.html#formatter-class)
     - A class for customizing the help output
    
*   [prefix\_chars](https://docs.python.org/3/library/argparse.html#prefix-chars)
     - The set of characters that prefix optional arguments (default: ‘-‘)
    
*   [fromfile\_prefix\_chars](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars)
     - The set of characters that prefix files from which additional arguments should be read (default: `None`)
    
*   [argument\_default](https://docs.python.org/3/library/argparse.html#argument-default)
     - The global default value for arguments (default: `None`)
    
*   [conflict\_handler](https://docs.python.org/3/library/argparse.html#conflict-handler)
     - The strategy for resolving conflicting optionals (usually unnecessary)
    
*   [add\_help](https://docs.python.org/3/library/argparse.html#add-help)
     - Add a `-h/--help` option to the parser (default: `True`)
    
*   [allow\_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev)
     - Allows long options to be abbreviated if the abbreviation is unambiguous (default: `True`)
    
*   [exit\_on\_error](https://docs.python.org/3/library/argparse.html#exit-on-error)
     - Determines whether or not `ArgumentParser` exits with error info when an error occurs. (default: `True`)
    
*   [suggest\_on\_error](https://docs.python.org/3/library/argparse.html#suggest-on-error)
     - Enables suggestions for mistyped argument choices and subparser names (default: `True`)
    
*   [color](https://docs.python.org/3/library/argparse.html#color)
     - Allow color output (default: `True`)
    

Changed in version 3.5: _allow\_abbrev_ parameter was added.

Changed in version 3.8: In previous versions, _allow\_abbrev_ also disabled grouping of short flags such as `-vv` to mean `-v -v`.

Changed in version 3.9: _exit\_on\_error_ parameter was added.

Changed in version 3.14: _suggest\_on\_error_ and _color_ parameters were added.

Changed in version 3.15: _suggest\_on\_error_ default changed to `True`.

The following sections describe how each of these are used.

### `prog`[¶](https://docs.python.org/3/library/argparse.html#prog "Link to this heading")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 calculates the name of the program to display in help messages depending on the way the Python interpreter was run:

*   The [`base name`](https://docs.python.org/3/library/os.path.html#os.path.basename "os.path.basename")
     of `sys.argv[0]` if a file was passed as argument.
    
*   The Python interpreter name followed by `sys.argv[0]` if a directory or a zipfile was passed as argument.
    
*   The Python interpreter name followed by `-m` followed by the module or package name if the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
     option was used.
    

This default is almost always desirable because it will make the help messages match the string that was used to invoke the program on the command line. However, to change this default behavior, another value can be supplied using the `prog=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='myprogram')
\>>> parser.print\_help()
usage: myprogram \[-h\]

options:
 -h, --help  show this help message and exit

Note that the program name, whether determined from `sys.argv[0]`, from the `__main__` module attributes or from the `prog=` argument, is available to help messages using the `%(prog)s` format specifier.

Copy

\>>> parser \= argparse.ArgumentParser(prog\='myprogram')
\>>> parser.add\_argument('--foo', help\='foo of the %(prog)s program')
\>>> parser.print\_help()
usage: myprogram \[-h\] \[--foo FOO\]

options:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program

Changed in version 3.14: The default `prog` value now reflects how `__main__` was actually executed, rather than always being `os.path.basename(sys.argv[0])`.

### `usage`[¶](https://docs.python.org/3/library/argparse.html#usage "Link to this heading")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 calculates the usage message from the arguments it contains. The default message can be overridden with the `usage=` keyword argument:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', usage\='%(prog)s \[options\]')
\>>> parser.add\_argument('--foo', nargs\='?', help\='foo help')
\>>> parser.add\_argument('bar', nargs\='+', help\='bar help')
\>>> parser.print\_help()
usage: PROG \[options\]

positional arguments:
 bar          bar help

options:
 -h, --help   show this help message and exit
 --foo \[FOO\]  foo help

The `%(prog)s` format specifier is available to fill in the program name in your usage messages.

When a custom usage message is specified for the main parser, you may also want to consider passing the `prog` argument to [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers")
 or the `prog` and the `usage` arguments to [`add_parser()`](https://docs.python.org/3/library/argparse.html#argparse._SubParsersAction.add_parser "argparse._SubParsersAction.add_parser")
, to ensure consistent command prefixes and usage information across subparsers.

### `description`[¶](https://docs.python.org/3/library/argparse.html#description "Link to this heading")

Most calls to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 constructor will use the `description=` keyword argument. This argument gives a brief description of what the program does and how it works. In help messages, the description is displayed between the command-line usage string and the help messages for the various arguments.

By default, the description will be line-wrapped so that it fits within the given space. To change this behavior, see the [formatter\_class](https://docs.python.org/3/library/argparse.html#formatter-class)
 argument.

### `epilog`[¶](https://docs.python.org/3/library/argparse.html#epilog "Link to this heading")

Some programs like to display additional description of the program after the description of the arguments. Such text can be specified using the `epilog=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
:

Copy

\>>> parser \= argparse.ArgumentParser(
...     description\='A foo that bars',
...     epilog\="And that's how you'd foo a bar")
\>>> parser.print\_help()
usage: argparse.py \[-h\]

A foo that bars

options:
 -h, --help  show this help message and exit

And that's how you'd foo a bar

As with the [description](https://docs.python.org/3/library/argparse.html#description)
 argument, the `epilog=` text is by default line-wrapped, but this behavior can be adjusted with the [formatter\_class](https://docs.python.org/3/library/argparse.html#formatter-class)
 argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
.

### `parents`[¶](https://docs.python.org/3/library/argparse.html#parents "Link to this heading")

Sometimes, several parsers share a common set of arguments. Rather than repeating the definitions of these arguments, a single parser with all the shared arguments and passed to `parents=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 can be used. The `parents=` argument takes a list of `ArgumentParser` objects, collects all the positional and optional actions from them, and adds these actions to the `ArgumentParser` object being constructed:

Copy

\>>> parent\_parser \= argparse.ArgumentParser(add\_help\=False)
\>>> parent\_parser.add\_argument('--parent', type\=int)

\>>> foo\_parser \= argparse.ArgumentParser(parents\=\[parent\_parser\])
\>>> foo\_parser.add\_argument('foo')
\>>> foo\_parser.parse\_args(\['--parent', '2', 'XXX'\])
Namespace(foo='XXX', parent=2)

\>>> bar\_parser \= argparse.ArgumentParser(parents\=\[parent\_parser\])
\>>> bar\_parser.add\_argument('--bar')
\>>> bar\_parser.parse\_args(\['--bar', 'YYY'\])
Namespace(bar='YYY', parent=None)

Note that most parent parsers will specify `add_help=False`. Otherwise, the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 will see two `-h/--help` options (one in the parent and one in the child) and raise an error.

Note

You must fully initialize the parsers before passing them via `parents=`. If you change the parent parsers after the child parser, those changes will not be reflected in the child.

### `formatter_class`[¶](https://docs.python.org/3/library/argparse.html#formatter-class "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects allow the help formatting to be customized by specifying an alternate formatting class. Currently, there are four such classes:

class argparse.RawDescriptionHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "Link to this definition")

class argparse.RawTextHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "Link to this definition")

class argparse.ArgumentDefaultsHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter "Link to this definition")

class argparse.MetavarTypeHelpFormatter[¶](https://docs.python.org/3/library/argparse.html#argparse.MetavarTypeHelpFormatter "Link to this definition")

[`RawDescriptionHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "argparse.RawDescriptionHelpFormatter")
 and [`RawTextHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "argparse.RawTextHelpFormatter")
 give more control over how textual descriptions are displayed. By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects line-wrap the [description](https://docs.python.org/3/library/argparse.html#description)
 and [epilog](https://docs.python.org/3/library/argparse.html#epilog)
 texts in command-line help messages:

Copy

\>>> parser \= argparse.ArgumentParser(
...     prog\='PROG',
...     description\='''this description
...         was indented weird
...             but that is okay''',
...     epilog\='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
\>>> parser.print\_help()
usage: PROG \[-h\]

this description was indented weird but that is okay

options:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines

Passing [`RawDescriptionHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter "argparse.RawDescriptionHelpFormatter")
 as `formatter_class=` indicates that [description](https://docs.python.org/3/library/argparse.html#description)
 and [epilog](https://docs.python.org/3/library/argparse.html#epilog)
 are already correctly formatted and should not be line-wrapped:

Copy

\>>> parser \= argparse.ArgumentParser(
...     prog\='PROG',
...     formatter\_class\=argparse.RawDescriptionHelpFormatter,
...     description\=textwrap.dedent('''\\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
\>>> parser.print\_help()
usage: PROG \[-h\]

Please do not mess up this text!
\--------------------------------
   I have indented it
   exactly the way
   I want it

options:
 -h, --help  show this help message and exit

[`RawTextHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.RawTextHelpFormatter "argparse.RawTextHelpFormatter")
 maintains whitespace for all sorts of help text, including argument descriptions. However, multiple newlines are replaced with one. If you wish to preserve multiple blank lines, add spaces between the newlines.

[`ArgumentDefaultsHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentDefaultsHelpFormatter "argparse.ArgumentDefaultsHelpFormatter")
 automatically adds information about default values to each of the argument help messages:

Copy

\>>> parser \= argparse.ArgumentParser(
...     prog\='PROG',
...     formatter\_class\=argparse.ArgumentDefaultsHelpFormatter)
\>>> parser.add\_argument('--foo', type\=int, default\=42, help\='FOO!')
\>>> parser.add\_argument('bar', nargs\='\*', default\=\[1, 2, 3\], help\='BAR!')
\>>> parser.print\_help()
usage: PROG \[-h\] \[--foo FOO\] \[bar ...\]

positional arguments:
 bar         BAR! (default: \[1, 2, 3\])

options:
 -h, --help  show this help message and exit
 --foo FOO   FOO! (default: 42)

[`MetavarTypeHelpFormatter`](https://docs.python.org/3/library/argparse.html#argparse.MetavarTypeHelpFormatter "argparse.MetavarTypeHelpFormatter")
 uses the name of the [type](https://docs.python.org/3/library/argparse.html#type)
 argument for each argument as the display name for its values (rather than using the [dest](https://docs.python.org/3/library/argparse.html#dest)
 as the regular formatter does):

Copy

\>>> parser \= argparse.ArgumentParser(
...     prog\='PROG',
...     formatter\_class\=argparse.MetavarTypeHelpFormatter)
\>>> parser.add\_argument('--foo', type\=int)
\>>> parser.add\_argument('bar', type\=float)
\>>> parser.print\_help()
usage: PROG \[-h\] \[--foo int\] float

positional arguments:
  float

options:
  -h, --help  show this help message and exit
  --foo int

### `prefix_chars`[¶](https://docs.python.org/3/library/argparse.html#prefix-chars "Link to this heading")

Most command-line options will use `-` as the prefix, e.g. `-f/--foo`. Parsers that need to support different or additional prefix characters, e.g. for options like `+f` or `/foo`, may specify them using the `prefix_chars=` argument to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 constructor:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', prefix\_chars\='-+')
\>>> parser.add\_argument('+f')
\>>> parser.add\_argument('++bar')
\>>> parser.parse\_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')

The `prefix_chars=` argument defaults to `'-'`. Supplying a set of characters that does not include `-` will cause `-f/--foo` options to be disallowed.

### `fromfile_prefix_chars`[¶](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars "Link to this heading")

Sometimes, when dealing with a particularly long argument list, it may make sense to keep the list of arguments in a file rather than typing it out at the command line. If the `fromfile_prefix_chars=` argument is given to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 constructor, then arguments that start with any of the specified characters will be treated as files, and will be replaced by the arguments they contain. For example:

Copy

\>>> with open('args.txt', 'w', encoding\=sys.getfilesystemencoding()) as fp:
...     fp.write('-f\\nbar')
...
\>>> parser \= argparse.ArgumentParser(fromfile\_prefix\_chars\='@')
\>>> parser.add\_argument('-f')
\>>> parser.parse\_args(\['-f', 'foo', '@args.txt'\])
Namespace(f='bar')

Arguments read from a file must be one per line by default (but see also [`convert_arg_line_to_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args "argparse.ArgumentParser.convert_arg_line_to_args")
) and are treated as if they were in the same place as the original file referencing argument on the command line. So in the example above, the expression `['-f', 'foo', '@args.txt']` is considered equivalent to the expression `['-f', 'foo', '-f', 'bar']`.

Note

Each line is treated as a single argument, so an empty line is read as an empty string (`''`).

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 uses [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 to read the file containing arguments.

The `fromfile_prefix_chars=` argument defaults to `None`, meaning that arguments will never be treated as file references.

Changed in version 3.12: [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 changed encoding and errors to read arguments files from default (e.g. [`locale.getpreferredencoding(False)`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding")
 and `"strict"`) to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. Arguments file should be encoded in UTF-8 instead of ANSI Codepage on Windows.

### `argument_default`[¶](https://docs.python.org/3/library/argparse.html#argument-default "Link to this heading")

Generally, argument defaults are specified either by passing a default to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 or by calling the [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults")
 methods with a specific set of name-value pairs. Sometimes however, it may be useful to specify a single parser-wide default for arguments. This can be accomplished by passing the `argument_default=` keyword argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
. For example, to globally suppress attribute creation on [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 calls, we supply `argument_default=SUPPRESS`:

Copy

\>>> parser \= argparse.ArgumentParser(argument\_default\=argparse.SUPPRESS)
\>>> parser.add\_argument('--foo')
\>>> parser.add\_argument('bar', nargs\='?')
\>>> parser.parse\_args(\['--foo', '1', 'BAR'\])
Namespace(bar='BAR', foo='1')
\>>> parser.parse\_args(\[\])
Namespace()

### `allow_abbrev`[¶](https://docs.python.org/3/library/argparse.html#allow-abbrev "Link to this heading")

Normally, when you pass an argument list to the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 method of an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
, it [recognizes abbreviations](https://docs.python.org/3/library/argparse.html#prefix-matching)
 of long options.

This feature can be disabled by setting `allow_abbrev` to `False`:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', allow\_abbrev\=False)
\>>> parser.add\_argument('--foobar', action\='store\_true')
\>>> parser.add\_argument('--foonley', action\='store\_false')
\>>> parser.parse\_args(\['--foon'\])
usage: PROG \[-h\] \[--foobar\] \[--foonley\]
PROG: error: unrecognized arguments: --foon

Added in version 3.5.

### `conflict_handler`[¶](https://docs.python.org/3/library/argparse.html#conflict-handler "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects do not allow two actions with the same option string. By default, `ArgumentParser` objects raise an exception if an attempt is made to create an argument with an option string that is already in use:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-f', '--foo', help\='old foo help')
\>>> parser.add\_argument('--foo', help\='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo

Sometimes (e.g. when using [parents](https://docs.python.org/3/library/argparse.html#parents)
) it may be useful to simply override any older arguments with the same option string. To get this behavior, the value `'resolve'` can be supplied to the `conflict_handler=` argument of [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', conflict\_handler\='resolve')
\>>> parser.add\_argument('-f', '--foo', help\='old foo help')
\>>> parser.add\_argument('--foo', help\='new foo help')
\>>> parser.print\_help()
usage: PROG \[-h\] \[-f FOO\] \[--foo FOO\]

options:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help

Note that [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects only remove an action if all of its option strings are overridden. So, in the example above, the old `-f/--foo` action is retained as the `-f` action, because only the `--foo` option string was overridden.

### `add_help`[¶](https://docs.python.org/3/library/argparse.html#add-help "Link to this heading")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects add an option which simply displays the parser’s help message. If `-h` or `--help` is supplied at the command line, the `ArgumentParser` help will be printed.

Occasionally, it may be useful to disable the addition of this help option. This can be achieved by passing `False` as the `add_help=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', add\_help\=False)
\>>> parser.add\_argument('--foo', help\='foo help')
\>>> parser.print\_help()
usage: PROG \[--foo FOO\]

options:
 --foo FOO  foo help

The help option is typically `-h/--help`. The exception to this is if the `prefix_chars=` is specified and does not include `-`, in which case `-h` and `--help` are not valid options. In this case, the first character in `prefix_chars` is used to prefix the help options:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', prefix\_chars\='+/')
\>>> parser.print\_help()
usage: PROG \[+h\]

options:
  +h, ++help  show this help message and exit

### `exit_on_error`[¶](https://docs.python.org/3/library/argparse.html#exit-on-error "Link to this heading")

Normally, when you pass an invalid argument list to the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 method of an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
, it will print a _message_ to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 and exit with a status code of 2.

If the user would like to catch errors manually, the feature can be enabled by setting `exit_on_error` to `False`:

Copy

\>>> parser \= argparse.ArgumentParser(exit\_on\_error\=False)
\>>> parser.add\_argument('--integers', type\=int)
\_StoreAction(option\_strings=\['--integers'\], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
\>>> try:
...     parser.parse\_args('--integers a'.split())
... except argparse.ArgumentError:
...     print('Catching an argumentError')
...
Catching an argumentError

Added in version 3.9.

### `suggest_on_error`[¶](https://docs.python.org/3/library/argparse.html#suggest-on-error "Link to this heading")

By default, when a user passes an invalid argument choice or subparser name, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 will exit with error info and provide suggestions for mistyped arguments. The error message will list the permissible argument choices (if specified) or subparser names, along with a “maybe you meant” suggestion if a close match is found. Note that this only applies for arguments when the choices specified are strings:

Copy

\>>> parser \= argparse.ArgumentParser(suggest\_on\_error\=True)
\>>> parser.add\_argument('--action', choices\=\['debug', 'dryrun'\])
\>>> parser.parse\_args(\['--action', 'debugg'\])
usage: tester.py \[-h\] \[--action {debug,dryrun}\]
tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)

You can disable suggestions by setting `suggest_on_error` to `False`.

Added in version 3.14.

Changed in version 3.15: Changed default value of `suggest_on_error` from `False` to `True`.

### `color`[¶](https://docs.python.org/3/library/argparse.html#color "Link to this heading")

By default, the help message is printed in color using [ANSI escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code)
. If you want plain text help messages, you can disable this [in your local environment](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
, or in the argument parser itself by setting `color` to `False`:

Copy

\>>> parser \= argparse.ArgumentParser(description\='Process some integers.',
...                                  color\=False)
\>>> parser.add\_argument('--action', choices\=\['sum', 'max'\])
\>>> parser.add\_argument('integers', metavar\='N', type\=int, nargs\='+',
...                     help\='an integer for the accumulator')
\>>> parser.parse\_args(\['--help'\])

Note that when `color=True`, colored output depends on both environment variables and terminal capabilities. However, if `color=False`, colored output is always disabled, even if environment variables like `FORCE_COLOR` are set.

Added in version 3.14.

To highlight inline code in your description, epilog, or argument `help` text, you can use single or double backticks:

Copy

\>>> parser \= argparse.ArgumentParser(
...     formatter\_class\=argparse.RawDescriptionHelpFormatter,
...     description\='Run \`\`python -m myapp\`\` to start.',
...     epilog\='''Examples:
...   \`python -m myapp --verbose\`
...   \`\`python -m myapp --config settings.json\`\`
... ''')
\>>> parser.add\_argument('--foo', help\='set the \`foo\` value')

When colors are enabled, the text inside backticks will be displayed in a distinct color to help examples stand out. When colors are disabled, backticks are preserved as-is, which is readable in plain text.

Added in version 3.15.

The add\_argument() method[¶](https://docs.python.org/3/library/argparse.html#the-add-argument-method "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

ArgumentParser.add\_argument(_name or flags..._, _\*_\[, _action_\]\[, _nargs_\]\[, _const_\]\[, _default_\]\[, _type_\]\[, _choices_\]\[, _required_\]\[, _help_\]\[, _metavar_\]\[, _dest_\]\[, _deprecated_\])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "Link to this definition")

Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

*   [name or flags](https://docs.python.org/3/library/argparse.html#name-or-flags)
     - Either a name or a list of option strings, e.g. `'foo'` or `'-f', '--foo'`.
    
*   [action](https://docs.python.org/3/library/argparse.html#action)
     - The basic type of action to be taken when this argument is encountered at the command line.
    
*   [nargs](https://docs.python.org/3/library/argparse.html#nargs)
     - The number of command-line arguments that should be consumed.
    
*   [const](https://docs.python.org/3/library/argparse.html#const)
     - A constant value required by some [action](https://docs.python.org/3/library/argparse.html#action)
     and [nargs](https://docs.python.org/3/library/argparse.html#nargs)
     selections.
    
*   [default](https://docs.python.org/3/library/argparse.html#default)
     - The value produced if the argument is absent from the command line and if it is absent from the namespace object.
    
*   [type](https://docs.python.org/3/library/argparse.html#type)
     - The type to which the command-line argument should be converted.
    
*   [choices](https://docs.python.org/3/library/argparse.html#choices)
     - A sequence of the allowable values for the argument.
    
*   [required](https://docs.python.org/3/library/argparse.html#required)
     - Whether or not the command-line option may be omitted (optionals only).
    
*   [help](https://docs.python.org/3/library/argparse.html#help)
     - A brief description of what the argument does.
    
*   [metavar](https://docs.python.org/3/library/argparse.html#metavar)
     - A name for the argument in usage messages.
    
*   [dest](https://docs.python.org/3/library/argparse.html#dest)
     - The name of the attribute to be added to the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
    .
    
*   [deprecated](https://docs.python.org/3/library/argparse.html#deprecated)
     - Whether or not use of the argument is deprecated.
    

The method returns an [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action")
 object representing the argument.

The following sections describe how each of these are used.

### `name` or `flags`[¶](https://docs.python.org/3/library/argparse.html#name-or-flags "Link to this heading")

The [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 method must know whether an optional argument, like `-f` or `--foo`, or a positional argument, like a list of filenames, is expected. The first arguments passed to `add_argument()` must therefore be either a series of flags, or a simple argument name.

For example, an optional argument could be created like:

Copy

\>>> parser.add\_argument('-f', '--foo')

while a positional argument could be created like:

Copy

\>>> parser.add\_argument('bar')

When [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 is called, optional arguments will be identified by the `-` prefix, and the remaining arguments will be assumed to be positional:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-f', '--foo')
\>>> parser.add\_argument('bar')
\>>> parser.parse\_args(\['BAR'\])
Namespace(bar='BAR', foo=None)
\>>> parser.parse\_args(\['BAR', '--foo', 'FOO'\])
Namespace(bar='BAR', foo='FOO')
\>>> parser.parse\_args(\['--foo', 'FOO'\])
usage: PROG \[-h\] \[-f FOO\] bar
PROG: error: the following arguments are required: bar

By default, `argparse` automatically handles the internal naming and display names of arguments, simplifying the process without requiring additional configuration. As such, you do not need to specify the [dest](https://docs.python.org/3/library/argparse.html#dest)
 and [metavar](https://docs.python.org/3/library/argparse.html#metavar)
 parameters. For optional arguments, the [dest](https://docs.python.org/3/library/argparse.html#dest)
 parameter defaults to the argument name, with underscores `_` replacing hyphens `-`. The [metavar](https://docs.python.org/3/library/argparse.html#metavar)
 parameter defaults to the upper-cased name. For example:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('--foo-bar')
\>>> parser.parse\_args(\['--foo-bar', 'FOO-BAR'\])
Namespace(foo\_bar='FOO-BAR')
\>>> parser.print\_help()
usage:  \[-h\] \[--foo-bar FOO\_BAR\]

optional arguments:
 -h, --help  show this help message and exit
 --foo-bar FOO\_BAR

### `action`[¶](https://docs.python.org/3/library/argparse.html#action "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects associate command-line arguments with actions. These actions can do just about anything with the command-line arguments associated with them, though most actions simply add an attribute to the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
. The `action` keyword argument specifies how the command-line arguments should be handled. The supplied actions are:

*   `'store'` - This just stores the argument’s value. This is the default action.
    
*   `'store_const'` - This stores the value specified by the [const](https://docs.python.org/3/library/argparse.html#const)
     keyword argument; note that the [const](https://docs.python.org/3/library/argparse.html#const)
     keyword argument defaults to `None`. The `'store_const'` action is most commonly used with optional arguments that specify some sort of flag. For example:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--foo', action\='store\_const', const\=42)
    \>>> parser.parse\_args(\['--foo'\])
    Namespace(foo=42)
    
*   `'store_true'` and `'store_false'` - These are special cases of `'store_const'` that respectively store the values `True` and `False` with default values of `False` and `True`:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--foo', action\='store\_true')
    \>>> parser.add\_argument('--bar', action\='store\_false')
    \>>> parser.add\_argument('--baz', action\='store\_false')
    \>>> parser.parse\_args('--foo --bar'.split())
    Namespace(foo=True, bar=False, baz=True)
    
    These defaults apply when the options are absent. They can be overridden by [default](https://docs.python.org/3/library/argparse.html#default)
     or [argument\_default](https://docs.python.org/3/library/argparse.html#argument-default)
    .
    
*   `'append'` - This appends each argument value to a list. It is useful for allowing an option to be specified multiple times. If the default value is a non-empty list, the parsed value will start with the default list’s elements and any values from the command line will be appended after those default values. Example usage:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--foo', action\='append', default\=\['0'\])
    \>>> parser.parse\_args('--foo 1 --foo 2'.split())
    Namespace(foo=\['0', '1', '2'\])
    
*   `'append_const'` - This appends the value specified by the [const](https://docs.python.org/3/library/argparse.html#const)
     keyword argument to a list; note that the [const](https://docs.python.org/3/library/argparse.html#const)
     keyword argument defaults to `None`. The `'append_const'` action is typically useful when multiple arguments need to store constants to the same list. For example:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--str', dest\='types', action\='append\_const', const\=str)
    \>>> parser.add\_argument('--int', dest\='types', action\='append\_const', const\=int)
    \>>> parser.parse\_args('--str --int'.split())
    Namespace(types=\[<class 'str'>, <class 'int'>\])
    
*   `'extend'` - This appends each item from a multi-value argument to a list. The `'extend'` action is typically used with the [nargs](https://docs.python.org/3/library/argparse.html#nargs)
     keyword argument value `'+'` or `'*'`. Note that when [nargs](https://docs.python.org/3/library/argparse.html#nargs)
     is `None` (the default) or `'?'`, each character of the argument string will be appended to the list. Example usage:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument("--foo", action\="extend", nargs\="+", type\=str)
    \>>> parser.parse\_args(\["--foo", "f1", "--foo", "f2", "f3", "f4"\])
    Namespace(foo=\['f1', 'f2', 'f3', 'f4'\])
    
    Added in version 3.8.
    
*   `'count'` - This counts the number of times an argument occurs. For example, this is useful for increasing verbosity levels:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--verbose', '-v', action\='count', default\=0)
    \>>> parser.parse\_args(\['-vvv'\])
    Namespace(verbose=3)
    
    Unless explicitly set, the _default_ will be `None`. If the default value is a non-zero number, the count starts from that number rather than from zero.
    
*   `'help'` - This prints a complete help message for all the options in the current parser and then exits. By default a help action is automatically added to the parser. See [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
     for details of how the output is created.
    
*   `'version'` - This expects a `version=` keyword argument in the [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
     call, and prints version information and exits when invoked:
    
    Copy
    
    \>>> import argparse
    \>>> parser \= argparse.ArgumentParser(prog\='PROG')
    \>>> parser.add\_argument('--version', action\='version', version\='%(prog)s 2.0')
    \>>> parser.parse\_args(\['--version'\])
    PROG 2.0
    

You may also specify an arbitrary action by passing an [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action")
 subclass (e.g. [`BooleanOptionalAction`](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "argparse.BooleanOptionalAction")
) or other object that implements the same interface. Only actions that consume command-line arguments (e.g. `'store'`, `'append'`, `'extend'`, or custom actions with non-zero `nargs`) can be used with positional arguments.

The recommended way to create a custom action is to extend [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action")
, overriding the `__call__()` method and optionally the `__init__()` and `format_usage()` methods. You can also register custom actions using the [`register()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "argparse.ArgumentParser.register")
 method and reference them by their registered name.

An example of a custom action:

Copy

\>>> class FooAction(argparse.Action):
...     def \_\_init\_\_(self, option\_strings, dest, nargs\=None, \*\*kwargs):
...         if nargs is not None:
...             raise ValueError("nargs not allowed")
...         super().\_\_init\_\_(option\_strings, dest, \*\*kwargs)
...     def \_\_call\_\_(self, parser, namespace, values, option\_string\=None):
...         print('%r %r %r' % (namespace, values, option\_string))
...         setattr(namespace, self.dest, values)
...
\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', action\=FooAction)
\>>> parser.add\_argument('bar', action\=FooAction)
\>>> args \= parser.parse\_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
\>>> args
Namespace(bar='1', foo='2')

For more details, see [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action")
.

### `nargs`[¶](https://docs.python.org/3/library/argparse.html#nargs "Link to this heading")

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 objects usually associate a single command-line argument with a single action to be taken. The `nargs` keyword argument associates a different number of command-line arguments with a single action. See also [Specifying ambiguous arguments](https://docs.python.org/3/howto/argparse.html#specifying-ambiguous-arguments)
. The supported values are:

*   `N` (an integer). `N` arguments from the command line will be gathered together into a list. For example:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--foo', nargs\=2)
    \>>> parser.add\_argument('bar', nargs\=1)
    \>>> parser.parse\_args('c --foo a b'.split())
    Namespace(bar=\['c'\], foo=\['a', 'b'\])
    
    Note that `nargs=1` produces a list of one item. This is different from the default, in which the item is produced by itself.
    

*   `'?'`. One argument will be consumed from the command line if possible, and produced as a single item. If no command-line argument is present, the value from [default](https://docs.python.org/3/library/argparse.html#default)
     will be produced. Note that for optional arguments, there is an additional case - the option string is present but not followed by a command-line argument. In this case the value from [const](https://docs.python.org/3/library/argparse.html#const)
     will be produced. Some examples to illustrate this:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--foo', nargs\='?', const\='c', default\='d')
    \>>> parser.add\_argument('bar', nargs\='?', default\='d')
    \>>> parser.parse\_args(\['XX', '--foo', 'YY'\])
    Namespace(bar='XX', foo='YY')
    \>>> parser.parse\_args(\['XX', '--foo'\])
    Namespace(bar='XX', foo='c')
    \>>> parser.parse\_args(\[\])
    Namespace(bar='d', foo='d')
    
    One of the more common uses of `nargs='?'` is to allow optional input and output files:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('infile', nargs\='?')
    \>>> parser.add\_argument('outfile', nargs\='?')
    \>>> parser.parse\_args(\['input.txt', 'output.txt'\])
    Namespace(infile='input.txt', outfile='output.txt')
    \>>> parser.parse\_args(\['input.txt'\])
    Namespace(infile='input.txt', outfile=None)
    \>>> parser.parse\_args(\[\])
    Namespace(infile=None, outfile=None)
    

*   `'*'`. All command-line arguments present are gathered into a list. Note that it generally doesn’t make much sense to have more than one positional argument with `nargs='*'`, but multiple optional arguments with `nargs='*'` is possible. For example:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser()
    \>>> parser.add\_argument('--foo', nargs\='\*')
    \>>> parser.add\_argument('--bar', nargs\='\*')
    \>>> parser.add\_argument('baz', nargs\='\*')
    \>>> parser.parse\_args('a b --foo x y --bar 1 2'.split())
    Namespace(bar=\['1', '2'\], baz=\['a', 'b'\], foo=\['x', 'y'\])
    

*   `'+'`. Just like `'*'`, all command-line arguments present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present. For example:
    
    Copy
    
    \>>> parser \= argparse.ArgumentParser(prog\='PROG')
    \>>> parser.add\_argument('foo', nargs\='+')
    \>>> parser.parse\_args(\['a', 'b'\])
    Namespace(foo=\['a', 'b'\])
    \>>> parser.parse\_args(\[\])
    usage: PROG \[-h\] foo \[foo ...\]
    PROG: error: the following arguments are required: foo
    

If the `nargs` keyword argument is not provided, the number of arguments consumed is determined by the [action](https://docs.python.org/3/library/argparse.html#action)
. Generally this means a single command-line argument will be consumed and a single item (not a list) will be produced. Actions that do not consume command-line arguments (e.g. `'store_const'`) set `nargs=0`.

### `const`[¶](https://docs.python.org/3/library/argparse.html#const "Link to this heading")

The `const` argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 is used to hold constant values that are not read from the command line but are required for the various [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 actions. The two most common uses of it are:

*   When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
     is called with `action='store_const'` or `action='append_const'`. These actions add the `const` value to one of the attributes of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
    . See the [action](https://docs.python.org/3/library/argparse.html#action)
     description for examples. If `const` is not provided to `add_argument()`, it will receive a default value of `None`.
    
*   When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
     is called with option strings (like `-f` or `--foo`) and `nargs='?'`. This creates an optional argument that can be followed by zero or one command-line arguments. When parsing the command line, if the option string is encountered with no command-line argument following it, the value from `const` will be used. See the [nargs](https://docs.python.org/3/library/argparse.html#nargs)
     description for examples.
    

Changed in version 3.11: `const=None` by default, including when `action='append_const'` or `action='store_const'`.

### `default`[¶](https://docs.python.org/3/library/argparse.html#default "Link to this heading")

All optional arguments and some positional arguments may be omitted at the command line. The `default` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 specifies what value should be used if the command-line argument is not present. For example:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', default\=42)
\>>> parser.parse\_args(\['--foo', '2'\])
Namespace(foo='2')
\>>> parser.parse\_args(\[\])
Namespace(foo=42)

If `default` is omitted, [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 uses a value previously set for the [dest](https://docs.python.org/3/library/argparse.html#dest)
 with [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults")
, or otherwise a non-`None` [argument\_default](https://docs.python.org/3/library/argparse.html#argument-default)
. If neither is set, the action’s own default is used.

If the target namespace already has an attribute set, the action _default_ will not overwrite it:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', default\=42)
\>>> parser.parse\_args(\[\], namespace\=argparse.Namespace(foo\=101))
Namespace(foo=101)

If the `default` value is a string, the parser parses the value as if it were a command-line argument. In particular, the parser applies any [type](https://docs.python.org/3/library/argparse.html#type)
 conversion argument, if provided, before setting the attribute on the [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
 return value. Otherwise, the parser uses the value as is:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--length', default\='10', type\=int)
\>>> parser.add\_argument('--width', default\=10.5, type\=int)
\>>> parser.parse\_args()
Namespace(length=10, width=10.5)

For positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs)
 equal to `?` or `*`, the `default` value is used when no command-line argument was present:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('foo', nargs\='?', default\=42)
\>>> parser.parse\_args(\['a'\])
Namespace(foo='a')
\>>> parser.parse\_args(\[\])
Namespace(foo=42)

Because `nargs='*'` gathers any supplied values into a list, an absent positional argument yields an empty list (`[]`). Only a non-`None` _default_ overrides this (so `default=None` still gives `[]`).

For [required](https://docs.python.org/3/library/argparse.html#required)
 arguments, the `default` value is ignored. For example, this applies to positional arguments with [nargs](https://docs.python.org/3/library/argparse.html#nargs)
 values other than `?` or `*`, or optional arguments marked as `required=True`.

Providing `default=argparse.SUPPRESS` causes no attribute to be added if the command-line argument was not present:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', default\=argparse.SUPPRESS)
\>>> parser.parse\_args(\[\])
Namespace()
\>>> parser.parse\_args(\['--foo', '1'\])
Namespace(foo='1')

### `type`[¶](https://docs.python.org/3/library/argparse.html#type "Link to this heading")

By default, the parser reads command-line arguments in as simple strings. However, quite often the command-line string should instead be interpreted as another type, such as a [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 or [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. The `type` keyword for [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 allows any necessary type-checking and type conversions to be performed.

If the [type](https://docs.python.org/3/library/argparse.html#type)
 keyword is used with the [default](https://docs.python.org/3/library/argparse.html#default)
 keyword, the type converter is only applied if the default is a string.

The argument to `type` can be a callable that accepts a single string or the name of a registered type (see [`register()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "argparse.ArgumentParser.register")
) If the function raises [`ArgumentTypeError`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentTypeError "argparse.ArgumentTypeError")
, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
, or [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
, the exception is caught and a nicely formatted error message is displayed. Other exception types are not handled.

Common built-in types and functions can be used as type converters:

Copy

import argparse
import pathlib

parser \= argparse.ArgumentParser()
parser.add\_argument('count', type\=int)
parser.add\_argument('distance', type\=float)
parser.add\_argument('street', type\=ascii)
parser.add\_argument('code\_point', type\=ord)
parser.add\_argument('datapath', type\=pathlib.Path)

User defined functions can be used as well:

Copy

\>>> def hyphenated(string):
...     return '-'.join(\[word\[:4\] for word in string.casefold().split()\])
...
\>>> parser \= argparse.ArgumentParser()
\>>> \_ \= parser.add\_argument('short\_title', type\=hyphenated)
\>>> parser.parse\_args(\['"The Tale of Two Cities"'\])
Namespace(short\_title='"the-tale-of-two-citi')

The [`bool()`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 function is not recommended as a type converter. All it does is convert empty strings to `False` and non-empty strings to `True`. This is usually not what is desired:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> \_ \= parser.add\_argument('--verbose', type\=bool)
\>>> parser.parse\_args(\['--verbose', 'False'\])
Namespace(verbose=True)

See [`BooleanOptionalAction`](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "argparse.BooleanOptionalAction")
 or `action='store_true'` for common alternatives.

In general, the `type` keyword is a convenience that should only be used for simple conversions that can only raise one of the three supported exceptions. Anything with more interesting error-handling or resource management should be done downstream after the arguments are parsed.

For example, JSON or YAML conversions have complex error cases that require better reporting than can be given by the `type` keyword. A [`JSONDecodeError`](https://docs.python.org/3/library/json.html#json.JSONDecodeError "json.JSONDecodeError")
 would not be well formatted and a [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 exception would not be handled at all.

Even [`FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType")
 has its limitations for use with the `type` keyword. If one argument uses `FileType` and then a subsequent argument fails, an error is reported but the file is not automatically closed. In this case, it would be better to wait until after the parser has run and then use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
\-statement to manage the files.

For type checkers that simply check against a fixed set of values, consider using the [choices](https://docs.python.org/3/library/argparse.html#choices)
 keyword instead.

### `choices`[¶](https://docs.python.org/3/library/argparse.html#choices "Link to this heading")

Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a sequence object as the _choices_ keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
. When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='game.py')
\>>> parser.add\_argument('move', choices\=\['rock', 'paper', 'scissors'\])
\>>> parser.parse\_args(\['rock'\])
Namespace(move='rock')
\>>> parser.parse\_args(\['fire'\])
usage: game.py \[-h\] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')

Any sequence can be passed as the _choices_ value, so [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 objects, [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 objects, and custom sequences are all supported.

Use of [`enum.Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")
 is not recommended because it is difficult to control its appearance in usage, help, and error messages.

Note that _choices_ are checked after any [type](https://docs.python.org/3/library/argparse.html#type)
 conversions have been performed, so objects in _choices_ should match the [type](https://docs.python.org/3/library/argparse.html#type)
 specified. This can make _choices_ appear unfamiliar in usage, help, or error messages.

To keep _choices_ user-friendly, consider a custom type wrapper that converts and formats values, or omit [type](https://docs.python.org/3/library/argparse.html#type)
 and handle conversion in your application code.

Formatted choices override the default _metavar_ which is normally derived from _dest_. This is usually what you want because the user never sees the _dest_ parameter. If this display isn’t desirable (perhaps because there are many choices), just specify an explicit [metavar](https://docs.python.org/3/library/argparse.html#metavar)
.

### `required`[¶](https://docs.python.org/3/library/argparse.html#required "Link to this heading")

In general, the `argparse` module assumes that flags like `-f` and `--bar` indicate _optional_ arguments, which can always be omitted at the command line. To make an option _required_, `True` can be specified for the `required=` keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', required\=True)
\>>> parser.parse\_args(\['--foo', 'BAR'\])
Namespace(foo='BAR')
\>>> parser.parse\_args(\[\])
usage: \[-h\] --foo FOO
: error: the following arguments are required: --foo

As the example shows, if an option is marked as `required`, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 will report an error if that option is not present at the command line.

Note

Required options are generally considered bad form because users expect _options_ to be _optional_, and thus they should be avoided when possible.

### `help`[¶](https://docs.python.org/3/library/argparse.html#help "Link to this heading")

The `help` value is a string containing a brief description of the argument. When a user requests help (usually by using `-h` or `--help` at the command line), these `help` descriptions will be displayed with each argument.

The `help` strings can include various format specifiers to avoid repetition of things like the program name or the argument [default](https://docs.python.org/3/library/argparse.html#default)
. The available specifiers include the program name, `%(prog)s` and most keyword arguments to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
, e.g. `%(default)s`, `%(type)s`, etc.:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='frobble')
\>>> parser.add\_argument('bar', nargs\='?', type\=int, default\=42,
...                     help\='the bar to %(prog)s (default: %(default)s)')
\>>> parser.print\_help()
usage: frobble \[-h\] \[bar\]

positional arguments:
 bar     the bar to frobble (default: 42)

options:
 -h, --help  show this help message and exit

As the help string supports %-formatting, if you want a literal `%` to appear in the help string, you must escape it as `%%`.

`argparse` supports silencing the help entry for certain options, by setting the `help` value to `argparse.SUPPRESS`:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='frobble')
\>>> parser.add\_argument('--foo', help\=argparse.SUPPRESS)
\>>> parser.print\_help()
usage: frobble \[-h\]

options:
  -h, --help  show this help message and exit

### `metavar`[¶](https://docs.python.org/3/library/argparse.html#metavar "Link to this heading")

When [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 generates help messages, it needs some way to refer to each expected argument. By default, `ArgumentParser` objects use the [dest](https://docs.python.org/3/library/argparse.html#dest)
 value as the “name” of each object. By default, for positional argument actions, the [dest](https://docs.python.org/3/library/argparse.html#dest)
 value is used directly, and for optional argument actions, the [dest](https://docs.python.org/3/library/argparse.html#dest)
 value is uppercased. So, a single positional argument with `dest='bar'` will be referred to as `bar`. A single optional argument `--foo` that should be followed by a single command-line argument will be referred to as `FOO`. An example:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo')
\>>> parser.add\_argument('bar')
\>>> parser.parse\_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
\>>> parser.print\_help()
usage:  \[-h\] \[--foo FOO\] bar

positional arguments:
 bar

options:
 -h, --help  show this help message and exit
 --foo FOO

An alternative name can be specified with `metavar`:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', metavar\='YYY')
\>>> parser.add\_argument('bar', metavar\='XXX')
\>>> parser.parse\_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
\>>> parser.print\_help()
usage:  \[-h\] \[--foo YYY\] XXX

positional arguments:
 XXX

options:
 -h, --help  show this help message and exit
 --foo YYY

Note that `metavar` only changes the _displayed_ name - the name of the attribute on the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 object is still determined by the [dest](https://docs.python.org/3/library/argparse.html#dest)
 value.

Different values of `nargs` may cause the metavar to be used multiple times. Providing a tuple to `metavar` specifies a different display for each of the arguments:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-x', nargs\=2)
\>>> parser.add\_argument('--foo', nargs\=2, metavar\=('bar', 'baz'))
\>>> parser.print\_help()
usage: PROG \[-h\] \[-x X X\] \[--foo bar baz\]

options:
 -h, --help     show this help message and exit
 -x X X
 --foo bar baz

### `dest`[¶](https://docs.python.org/3/library/argparse.html#dest "Link to this heading")

Most [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 actions add some value as an attribute of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
. The name of this attribute is determined by the `dest` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
. For positional argument actions, `dest` is normally supplied as the first argument to `add_argument()`:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('bar')
\>>> parser.parse\_args(\['XXX'\])
Namespace(bar='XXX')

For optional argument actions, the value of `dest` is normally inferred from the option strings. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 generates the value of `dest` by taking the first double-dash long option string and stripping away the initial `-` characters. If no double-dash long option strings were supplied, `dest` will be derived from the first single-dash long option string by stripping the initial `-` character. If no long option strings were supplied, `dest` will be derived from the first short option string by stripping the initial `-` character. Any internal `-` characters will be converted to `_` characters to make sure the string is a valid attribute name. The examples below illustrate this behavior:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('-f', '--foo-bar', '--foo')
\>>> parser.add\_argument('-q', '-quz')
\>>> parser.add\_argument('-x', '-y')
\>>> parser.parse\_args('-f 1 -q 2 -x 3'.split())
Namespace(foo\_bar='1', quz='2', x='3')
\>>> parser.parse\_args('--foo 1 -quz 2 -y 3'.split())
Namespace(foo\_bar='1', quz='2', x='3')

`dest` allows a custom attribute name to be provided:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', dest\='bar')
\>>> parser.parse\_args('--foo XXX'.split())
Namespace(bar='XXX')

Multiple arguments may share the same `dest`. By default, the value from the last such argument given on the command line wins. Use `action='append'` to collect values from all of them into a list instead. For conflicting _option strings_ rather than `dest` names, see [conflict\_handler](https://docs.python.org/3/library/argparse.html#conflict-handler)
.

Changed in version 3.15: Single-dash long option now takes precedence over short options.

### `deprecated`[¶](https://docs.python.org/3/library/argparse.html#deprecated "Link to this heading")

During a project’s lifetime, some arguments may need to be removed from the command line. Before removing them, you should inform your users that the arguments are deprecated and will be removed. The `deprecated` keyword argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
, which defaults to `False`, specifies if the argument is deprecated and will be removed in the future. For arguments, if `deprecated` is `True`, then a warning will be printed to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 when the argument is used:

Copy

\>>> import argparse
\>>> parser \= argparse.ArgumentParser(prog\='snake.py')
\>>> parser.add\_argument('--legs', default\=0, type\=int, deprecated\=True)
\>>> parser.parse\_args(\[\])
Namespace(legs=0)
\>>> parser.parse\_args(\['--legs', '4'\])
snake.py: warning: option '--legs' is deprecated
Namespace(legs=4)

Added in version 3.13.

### Action classes[¶](https://docs.python.org/3/library/argparse.html#action-classes "Link to this heading")

`Action` classes implement the Action API, a callable which returns a callable which processes arguments from the command-line. Any object which follows this API may be passed as the `action` parameter to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
.

class argparse.Action(_option\_strings_, _dest_, _nargs\=None_, _const\=None_, _default\=None_, _type\=None_, _choices\=None_, _required\=False_, _help\=None_, _metavar\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.Action "Link to this definition")

`Action` objects are used by an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 to represent the information needed to parse a single argument from one or more strings from the command line. The `Action` class must accept the two positional arguments plus any keyword arguments passed to [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 except for the `action` itself.

Instances of `Action` (or return value of any callable to the `action` parameter) should have attributes `dest`, `option_strings`, `default`, `type`, `required`, `help`, etc. defined. The easiest way to ensure these attributes are defined is to call `Action.__init__()`.

\_\_call\_\_(_parser_, _namespace_, _values_, _option\_string\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.Action.__call__ "Link to this definition")

`Action` instances should be callable, so subclasses must override the `__call__()` method, which should accept four parameters:

*   _parser_ - The [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
     object which contains this action.
    
*   _namespace_ - The [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
     object that will be returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
    . Most actions add an attribute to this object using [`setattr()`](https://docs.python.org/3/builtins/functions.html#setattr "setattr")
    .
    
*   _values_ - The associated command-line arguments, with any type conversions applied. Type conversions are specified with the [type](https://docs.python.org/3/library/argparse.html#type)
     keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
    .
    
*   _option\_string_ - The option string that was used to invoke this action. The `option_string` argument is optional, and will be absent if the action is associated with a positional argument.
    

The `__call__()` method may perform arbitrary actions, but will typically set attributes on the `namespace` based on `dest` and `values`.

format\_usage()[¶](https://docs.python.org/3/library/argparse.html#argparse.Action.format_usage "Link to this definition")

`Action` subclasses can define a `format_usage()` method that takes no argument and return a string which will be used when printing the usage of the program. If such method is not provided, a sensible default will be used.

class argparse.BooleanOptionalAction[¶](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "Link to this definition")

A subclass of [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action")
 for handling boolean flags with positive and negative options. Adding a single argument such as `--foo` automatically creates both `--foo` and `--no-foo` options, storing `True` and `False` respectively:

Copy

\>>> import argparse
\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', action\=argparse.BooleanOptionalAction)
\>>> parser.parse\_args(\['--no-foo'\])
Namespace(foo=False)

Single-dash long options are also supported. For example, negative option `-nofoo` is automatically added for positive option `-foo`. But no additional options are added for short options such as `-f`.

Added in version 3.9.

Changed in version 3.15: Added support for single-dash options.

Added support for alternate [prefix\_chars](https://docs.python.org/3/library/argparse.html#prefix-chars)
.

The parse\_args() method[¶](https://docs.python.org/3/library/argparse.html#the-parse-args-method "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

ArgumentParser.parse\_args(_args\=None_, _namespace\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "Link to this definition")

Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.

Previous calls to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 determine exactly what objects are created and how they are assigned. See the documentation for `add_argument()` for details.

*   [args](https://docs.python.org/3/library/argparse.html#args)
     - List of strings to parse. The default is taken from [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
    .
    
*   [namespace](https://docs.python.org/3/library/argparse.html#namespace)
     - An object to take the attributes. The default is a new empty [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace")
     object.
    

### Option value syntax[¶](https://docs.python.org/3/library/argparse.html#option-value-syntax "Link to this heading")

The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 method supports several ways of specifying the value of an option (if it takes one). In the simplest case, the option and its value are passed as two separate arguments:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-x')
\>>> parser.add\_argument('--foo')
\>>> parser.parse\_args(\['-x', 'X'\])
Namespace(foo=None, x='X')
\>>> parser.parse\_args(\['--foo', 'FOO'\])
Namespace(foo='FOO', x=None)

For long options (options with names longer than a single character), the option and value can also be passed as a single command-line argument, using `=` to separate them:

Copy

\>>> parser.parse\_args(\['--foo=FOO'\])
Namespace(foo='FOO', x=None)

For short options (options only one character long), the option and its value can be concatenated:

Copy

\>>> parser.parse\_args(\['-xX'\])
Namespace(foo=None, x='X')

Several short options can be joined together, using only a single `-` prefix, as long as only the last option (or none of them) requires a value:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-x', action\='store\_true')
\>>> parser.add\_argument('-y', action\='store\_true')
\>>> parser.add\_argument('-z')
\>>> parser.parse\_args(\['-xyzZ'\])
Namespace(x=True, y=True, z='Z')

### Invalid arguments[¶](https://docs.python.org/3/library/argparse.html#invalid-arguments "Link to this heading")

While parsing the command line, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 checks for a variety of errors, including ambiguous options, invalid types, invalid options, wrong number of positional arguments, etc. When it encounters such an error, it exits and prints the error along with a usage message:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('--foo', type\=int)
\>>> parser.add\_argument('bar', nargs\='?')

\>>> \# invalid type
\>>> parser.parse\_args(\['--foo', 'spam'\])
usage: PROG \[-h\] \[--foo FOO\] \[bar\]
PROG: error: argument --foo: invalid int value: 'spam'

\>>> \# invalid option
\>>> parser.parse\_args(\['--bar'\])
usage: PROG \[-h\] \[--foo FOO\] \[bar\]
PROG: error: unrecognized arguments: --bar

\>>> \# wrong number of arguments
\>>> parser.parse\_args(\['spam', 'badger'\])
usage: PROG \[-h\] \[--foo FOO\] \[bar\]
PROG: error: unrecognized arguments: badger

### Arguments containing `-`[¶](https://docs.python.org/3/library/argparse.html#arguments-containing "Link to this heading")

The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 method attempts to give errors whenever the user has clearly made a mistake, but some situations are inherently ambiguous. For example, the command-line argument `-1` could either be an attempt to specify an option or an attempt to provide a positional argument. The `parse_args()` method is cautious here: positional arguments may only begin with `-` if they look like negative numbers and there are no options in the parser that look like negative numbers:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-x')
\>>> parser.add\_argument('foo', nargs\='?')

\>>> \# no negative number options, so -1 is a positional argument
\>>> parser.parse\_args(\['-x', '-1'\])
Namespace(foo=None, x='-1')

\>>> \# no negative number options, so -1 and -5 are positional arguments
\>>> parser.parse\_args(\['-x', '-1', '-5'\])
Namespace(foo='-5', x='-1')

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-1', dest\='one')
\>>> parser.add\_argument('foo', nargs\='?')

\>>> \# negative number options present, so -1 is an option
\>>> parser.parse\_args(\['-1', 'X'\])
Namespace(foo=None, one='X')

\>>> \# negative number options present, so -2 is an option
\>>> parser.parse\_args(\['-2'\])
usage: PROG \[-h\] \[-1 ONE\] \[foo\]
PROG: error: unrecognized arguments: -2

\>>> \# negative number options present, so both -1s are options
\>>> parser.parse\_args(\['-1', '-1'\])
usage: PROG \[-h\] \[-1 ONE\] \[foo\]
PROG: error: argument -1: expected one argument

If you have positional arguments that must begin with `-` and don’t look like negative numbers, you can insert the pseudo-argument `'--'` which tells [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 that everything after that is a positional argument:

Copy

\>>> parser.parse\_args(\['--', '-f'\])
Namespace(foo='-f', one=None)

See also [the argparse howto on ambiguous arguments](https://docs.python.org/3/howto/argparse.html#specifying-ambiguous-arguments)
 for more details.

Changed in version 3.14: Negative-number matching was expanded to include numbers in scientific notation (`-2.5e-6`), numbers containing underscores (`-1_234.5`), and complex numbers (`-1.2e-3j`).

### Argument abbreviations (prefix matching)[¶](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching "Link to this heading")

The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 method [by default](https://docs.python.org/3/library/argparse.html#allow-abbrev)
 allows long options to be abbreviated to a prefix, if the abbreviation is unambiguous (the prefix matches a unique option):

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('-bacon')
\>>> parser.add\_argument('-badger')
\>>> parser.parse\_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
\>>> parser.parse\_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
\>>> parser.parse\_args('-ba BA'.split())
usage: PROG \[-h\] \[-bacon BACON\] \[-badger BADGER\]
PROG: error: ambiguous option: -ba could match -badger, -bacon

An error is produced for arguments that could produce more than one options. This feature can be disabled by setting [allow\_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev)
 to `False`.

### Beyond `sys.argv`[¶](https://docs.python.org/3/library/argparse.html#beyond-sys-argv "Link to this heading")

Sometimes it may be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 parse arguments other than those of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
. This can be accomplished by passing a list of strings to [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
. This is useful for testing at the interactive prompt:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument(
...     'integers', metavar\='int', type\=int, choices\=range(10),
...     nargs\='+', help\='an integer in the range 0..9')
\>>> parser.add\_argument(
...     '--sum', dest\='accumulate', action\='store\_const', const\=sum,
...     default\=max, help\='sum the integers (default: find the max)')
\>>> parser.parse\_args(\['1', '2', '3', '4'\])
Namespace(accumulate=<built-in function max>, integers=\[1, 2, 3, 4\])
\>>> parser.parse\_args(\['1', '2', '3', '4', '--sum'\])
Namespace(accumulate=<built-in function sum>, integers=\[1, 2, 3, 4\])

### The Namespace object[¶](https://docs.python.org/3/library/argparse.html#the-namespace-object "Link to this heading")

class argparse.Namespace[¶](https://docs.python.org/3/library/argparse.html#argparse.Namespace "Link to this definition")

Simple class used by default by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 to create an object holding attributes and return it.

This class is deliberately simple, just an [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 subclass with a readable string representation. If you prefer to have dict-like view of the attributes, you can use the standard Python idiom, [`vars()`](https://docs.python.org/3/builtins/functions.html#vars "vars")
:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo')
\>>> args \= parser.parse\_args(\['--foo', 'BAR'\])
\>>> vars(args)
{'foo': 'BAR'}

It may also be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 assign attributes to an already existing object, rather than a new `Namespace` object. This can be achieved by specifying the `namespace=` keyword argument:

Copy

\>>> class C:
...     pass
...
\>>> c \= C()
\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo')
\>>> parser.parse\_args(args\=\['--foo', 'BAR'\], namespace\=c)
\>>> c.foo
'BAR'

Other utilities[¶](https://docs.python.org/3/library/argparse.html#other-utilities "Link to this heading")

-----------------------------------------------------------------------------------------------------------

### Subcommands[¶](https://docs.python.org/3/library/argparse.html#subcommands "Link to this heading")

ArgumentParser.add\_subparsers(_\*_\[, _title_\]\[, _description_\]\[, _prog_\]\[, _parser\_class_\]\[, _action_\]\[, _dest_\]\[, _required_\]\[, _help_\]\[, _metavar_\])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "Link to this definition")

Many programs split up their functionality into a number of subcommands, for example, the `svn` program can invoke subcommands like `svn checkout`, `svn update`, and `svn commit`. Splitting up functionality this way can be a particularly good idea when a program performs several different functions which require different kinds of command-line arguments. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 supports the creation of such subcommands with the `add_subparsers()` method. The `add_subparsers()` method is normally called with no arguments and returns a special action object. This object has a single method, [`add_parser()`](https://docs.python.org/3/library/argparse.html#argparse._SubParsersAction.add_parser "argparse._SubParsersAction.add_parser")
, which takes a command name and any `ArgumentParser` constructor arguments, and returns an `ArgumentParser` object that can be modified as usual.

Description of parameters:

*   _title_ - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional arguments
    
*   _description_ - description for the sub-parser group in help output, by default `None`
    
*   _prog_ - usage information that will be displayed with subcommand help, by default the name of the program and any positional arguments before the subparser argument
    
*   _parser\_class_ - class which will be used to create sub-parser instances, by default the class of the current parser (e.g. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
    )
    
*   [action](https://docs.python.org/3/library/argparse.html#action)
     - the basic type of action to be taken when this argument is encountered at the command line
    
*   [dest](https://docs.python.org/3/library/argparse.html#dest)
     - name of the attribute under which subcommand name will be stored; by default `None` and no value is stored
    
*   [required](https://docs.python.org/3/library/argparse.html#required)
     - Whether or not a subcommand must be provided, by default `False` (added in 3.7)
    
*   [help](https://docs.python.org/3/library/argparse.html#help)
     - help for sub-parser group in help output, by default `None`
    
*   [metavar](https://docs.python.org/3/library/argparse.html#metavar)
     - string presenting available subcommands in help; by default it is `None` and presents subcommands in form {cmd1, cmd2, ..}
    

Some example usage:

Copy

\>>> \# create the top-level parser
\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> parser.add\_argument('--foo', action\='store\_true', help\='foo help')
\>>> subparsers \= parser.add\_subparsers(help\='subcommand help')
\>>>
\>>> \# create the parser for the "a" command
\>>> parser\_a \= subparsers.add\_parser('a', help\='a help')
\>>> parser\_a.add\_argument('bar', type\=int, help\='bar help')
\>>>
\>>> \# create the parser for the "b" command
\>>> parser\_b \= subparsers.add\_parser('b', help\='b help')
\>>> parser\_b.add\_argument('--baz', choices\=('X', 'Y', 'Z'), help\='baz help')
\>>>
\>>> \# parse some argument lists
\>>> parser.parse\_args(\['a', '12'\])
Namespace(bar=12, foo=False)
\>>> parser.parse\_args(\['--foo', 'b', '--baz', 'Z'\])
Namespace(baz='Z', foo=True)

Note that the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 will only contain attributes for the main parser and the subparser that was selected by the command line (and not any other subparsers). So in the example above, when the `a` command is specified, only the `foo` and `bar` attributes are present, and when the `b` command is specified, only the `foo` and `baz` attributes are present.

If a subparser defines an argument with the same `dest` as the parent parser, the two share a single namespace attribute, so the parent’s value won’t be retained. Users should give them distinct `dest` values to keep both.

Similarly, when a help message is requested from a subparser, only the help for that particular parser will be printed. The help message will not include parent parser or sibling parser messages. (A help message for each subparser command, however, can be given by supplying the `help=` argument to [`add_parser()`](https://docs.python.org/3/library/argparse.html#argparse._SubParsersAction.add_parser "argparse._SubParsersAction.add_parser")
 as above.)

Copy

\>>> parser.parse\_args(\['--help'\])
usage: PROG \[-h\] \[--foo\] {a,b} ...

positional arguments:
  {a,b}   subcommand help
    a     a help
    b     b help

options:
  -h, --help  show this help message and exit
  --foo   foo help

\>>> parser.parse\_args(\['a', '--help'\])
usage: PROG a \[-h\] bar

positional arguments:
  bar     bar help

options:
  -h, --help  show this help message and exit

\>>> parser.parse\_args(\['b', '--help'\])
usage: PROG b \[-h\] \[--baz {X,Y,Z}\]

options:
  -h, --help     show this help message and exit
  --baz {X,Y,Z}  baz help

The `add_subparsers()` method also supports `title` and `description` keyword arguments. When either is present, the subparser’s commands will appear in their own group in the help output. For example:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> subparsers \= parser.add\_subparsers(title\='subcommands',
...                                    description\='valid subcommands',
...                                    help\='additional help')
\>>> subparsers.add\_parser('foo')
\>>> subparsers.add\_parser('bar')
\>>> parser.parse\_args(\['-h'\])
usage:  \[-h\] {foo,bar} ...

options:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {foo,bar}   additional help

One particularly effective way of handling subcommands is to combine the use of the `add_subparsers()` method with calls to [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults")
 so that each subparser knows which Python function it should execute. For example:

Copy

\>>> \# subcommand functions
\>>> def foo(args):
...     print(args.x \* args.y)
...
\>>> def bar(args):
...     print('((%s))' % args.z)
...
\>>> \# create the top-level parser
\>>> parser \= argparse.ArgumentParser()
\>>> subparsers \= parser.add\_subparsers(required\=True)
\>>>
\>>> \# create the parser for the "foo" command
\>>> parser\_foo \= subparsers.add\_parser('foo')
\>>> parser\_foo.add\_argument('-x', type\=int, default\=1)
\>>> parser\_foo.add\_argument('y', type\=float)
\>>> parser\_foo.set\_defaults(func\=foo)
\>>>
\>>> \# create the parser for the "bar" command
\>>> parser\_bar \= subparsers.add\_parser('bar')
\>>> parser\_bar.add\_argument('z')
\>>> parser\_bar.set\_defaults(func\=bar)
\>>>
\>>> \# parse the args and call whatever function was selected
\>>> args \= parser.parse\_args('foo 1 -x 2'.split())
\>>> args.func(args)
2.0
\>>>
\>>> \# parse the args and call whatever function was selected
\>>> args \= parser.parse\_args('bar XYZYX'.split())
\>>> args.func(args)
((XYZYX))

This way, you can let [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 do the job of calling the appropriate function after argument parsing is complete. Associating functions with actions like this is typically the easiest way to handle the different actions for each of your subparsers. However, if it is necessary to check the name of the subparser that was invoked, the `dest` keyword argument to the `add_subparsers()` call will work:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> subparsers \= parser.add\_subparsers(dest\='subparser\_name')
\>>> subparser1 \= subparsers.add\_parser('1')
\>>> subparser1.add\_argument('-x')
\>>> subparser2 \= subparsers.add\_parser('2')
\>>> subparser2.add\_argument('y')
\>>> parser.parse\_args(\['2', 'frobble'\])
Namespace(subparser\_name='2', y='frobble')

Changed in version 3.7: New _required_ keyword-only parameter.

Changed in version 3.14: Subparser’s _prog_ is no longer affected by a custom usage message in the main parser.

\_SubParsersAction.add\_parser(_name_, _\*_, _help\=None_, _aliases\=None_, _deprecated\=False_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/argparse.html#argparse._SubParsersAction.add_parser "Link to this definition")

Create and return a new [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 object for the subcommand _name_.

The _name_ argument is the name of the sub-command.

The _help_ argument provides a short description for this sub-command.

The _aliases_ argument allows providing alternative names for this sub-command. For example:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> subparsers \= parser.add\_subparsers()
\>>> checkout \= subparsers.add\_parser('checkout', aliases\=\['co'\])
\>>> checkout.add\_argument('foo')
\>>> parser.parse\_args(\['co', 'bar'\])
Namespace(foo='bar')

The _deprecated_ argument, if `True`, marks the sub-command as deprecated and will issue a warning when used. For example:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='chicken.py')
\>>> subparsers \= parser.add\_subparsers()
\>>> fly \= subparsers.add\_parser('fly', deprecated\=True)
\>>> args \= parser.parse\_args(\['fly'\])
chicken.py: warning: command 'fly' is deprecated
Namespace()

All other keyword arguments are passed directly to the `ArgumentParser` constructor.

Added in version 3.13: Added the _deprecated_ parameter.

### FileType objects[¶](https://docs.python.org/3/library/argparse.html#filetype-objects "Link to this heading")

class argparse.FileType(_mode\='r'_, _bufsize\=\-1_, _encoding\=None_, _errors\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.FileType "Link to this definition")

The `FileType` factory creates objects that can be passed to the type argument of [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
. Arguments that have `FileType` objects as their type will open command-line arguments as files with the requested modes, buffer sizes, encodings and error handling (see the [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 function for more details):

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--raw', type\=argparse.FileType('wb', 0))
\>>> parser.add\_argument('out', type\=argparse.FileType('w', encoding\='UTF-8'))
\>>> parser.parse\_args(\['--raw', 'raw.dat', 'file.txt'\])
Namespace(out=<\_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<\_io.FileIO name='raw.dat' mode='wb'>)

FileType objects understand the pseudo-argument `'-'` and automatically convert this into [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
 for readable `FileType` objects and [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 for writable `FileType` objects:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('infile', type\=argparse.FileType('r'))
\>>> parser.parse\_args(\['-'\])
Namespace(infile=<\_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)

Note

If one argument uses _FileType_ and then a subsequent argument fails, an error is reported but the file is not automatically closed. This can also clobber the output files. In this case, it would be better to wait until after the parser has run and then use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
\-statement to manage the files.

Changed in version 3.4: Added the _encoding_ and _errors_ parameters.

Deprecated since version 3.14.

### Argument groups[¶](https://docs.python.org/3/library/argparse.html#argument-groups "Link to this heading")

ArgumentParser.add\_argument\_group(_title\=None_, _description\=None_, _\*_\[, _argument\_default_\]\[, _conflict\_handler_\])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "Link to this definition")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 groups command-line arguments into “positional arguments” and “options” when displaying help messages. When there is a better conceptual grouping of arguments than this default one, appropriate groups can be created using the `add_argument_group()` method:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', add\_help\=False)
\>>> group \= parser.add\_argument\_group('group')
\>>> group.add\_argument('--foo', help\='foo help')
\>>> group.add\_argument('bar', help\='bar help')
\>>> parser.print\_help()
usage: PROG \[--foo FOO\] bar

group:
  bar    bar help
  --foo FOO  foo help

The `add_argument_group()` method returns an argument group object which has an [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 method just like a regular [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
. When an argument is added to the group, the parser treats it just like a normal argument, but displays the argument in a separate group for help messages. The `add_argument_group()` method accepts _title_ and _description_ arguments which can be used to customize this display:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG', add\_help\=False)
\>>> group1 \= parser.add\_argument\_group('group1', 'group1 description')
\>>> group1.add\_argument('foo', help\='foo help')
\>>> group2 \= parser.add\_argument\_group('group2', 'group2 description')
\>>> group2.add\_argument('--bar', help\='bar help')
\>>> parser.print\_help()
usage: PROG \[--bar BAR\] foo

group1:
  group1 description

  foo    foo help

group2:
  group2 description

  --bar BAR  bar help

The optional, keyword-only parameters [argument\_default](https://docs.python.org/3/library/argparse.html#argument-default)
 and [conflict\_handler](https://docs.python.org/3/library/argparse.html#conflict-handler)
 allow for finer-grained control of the behavior of the argument group. These parameters have the same meaning as in the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 constructor, but apply specifically to the argument group rather than the entire parser.

Note that any arguments not in your user-defined groups will end up back in the usual “positional arguments” and “optional arguments” sections.

Within each argument group, arguments are displayed in help output in the order in which they are added.

Deprecated since version 3.11, removed in version 3.14: Calling `add_argument_group()` on an argument group now raises an exception. This nesting was never supported, often failed to work correctly, and was unintentionally exposed through inheritance.

Deprecated since version 3.14: Passing [prefix\_chars](https://docs.python.org/3/library/argparse.html#prefix-chars)
 to `add_argument_group()` is now deprecated.

### Mutual exclusion[¶](https://docs.python.org/3/library/argparse.html#mutual-exclusion "Link to this heading")

ArgumentParser.add\_mutually\_exclusive\_group(_required\=False_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group "Link to this definition")

Create a mutually exclusive group. `argparse` will make sure that only one of the arguments in the mutually exclusive group was present on the command line:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> group \= parser.add\_mutually\_exclusive\_group()
\>>> group.add\_argument('--foo', action\='store\_true')
\>>> group.add\_argument('--bar', action\='store\_false')
\>>> parser.parse\_args(\['--foo'\])
Namespace(bar=True, foo=True)
\>>> parser.parse\_args(\['--bar'\])
Namespace(bar=False, foo=False)
\>>> parser.parse\_args(\['--foo', '--bar'\])
usage: PROG \[-h\] \[--foo | --bar\]
PROG: error: argument --bar: not allowed with argument --foo

The `add_mutually_exclusive_group()` method also accepts a _required_ argument, to indicate that at least one of the mutually exclusive arguments is required:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> group \= parser.add\_mutually\_exclusive\_group(required\=True)
\>>> group.add\_argument('--foo', action\='store\_true')
\>>> group.add\_argument('--bar', action\='store\_false')
\>>> parser.parse\_args(\[\])
usage: PROG \[-h\] (--foo | --bar)
PROG: error: one of the arguments --foo --bar is required

Note that currently mutually exclusive argument groups do not support the _title_ and _description_ arguments of [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group")
. However, a mutually exclusive group can be added to an argument group that has a title and description. For example:

Copy

\>>> parser \= argparse.ArgumentParser(prog\='PROG')
\>>> group \= parser.add\_argument\_group('Group title', 'Group description')
\>>> exclusive\_group \= group.add\_mutually\_exclusive\_group(required\=True)
\>>> exclusive\_group.add\_argument('--foo', help\='foo help')
\>>> exclusive\_group.add\_argument('--bar', help\='bar help')
\>>> parser.print\_help()
usage: PROG \[-h\] (--foo FOO | --bar BAR)

options:
  -h, --help  show this help message and exit

Group title:
  Group description

  --foo FOO   foo help
  --bar BAR   bar help

Deprecated since version 3.11, removed in version 3.14: Calling [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group")
 or `add_mutually_exclusive_group()` on a mutually exclusive group now raises an exception. This nesting was never supported, often failed to work correctly, and was unintentionally exposed through inheritance.

### Parser defaults[¶](https://docs.python.org/3/library/argparse.html#parser-defaults "Link to this heading")

ArgumentParser.set\_defaults(_\*\*kwargs_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "Link to this definition")

Most of the time, the attributes of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 will be fully determined by inspecting the command-line arguments and the argument actions. `set_defaults()` allows some additional attributes that are determined without any inspection of the command line to be added:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('foo', type\=int)
\>>> parser.set\_defaults(bar\=42, baz\='badger')
\>>> parser.parse\_args(\['736'\])
Namespace(bar=42, baz='badger', foo=736)

Note that defaults can be set at both the parser level using `set_defaults()` and at the argument level using [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
. If both are called for the same argument, the last default set for an argument is used:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', default\='bar')
\>>> parser.set\_defaults(foo\='spam')
\>>> parser.parse\_args(\[\])
Namespace(foo='spam')

Parser-level defaults can be particularly useful when working with multiple parsers. See the [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers")
 method for an example of this type.

ArgumentParser.get\_default(_dest_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.get_default "Link to this definition")

Get the default value for a namespace attribute, as set by either [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
 or by [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults")
:

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', default\='badger')
\>>> parser.get\_default('foo')
'badger'

### Printing help[¶](https://docs.python.org/3/library/argparse.html#printing-help "Link to this heading")

In most typical applications, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
 will take care of formatting and printing any usage or error messages. However, several formatting methods are available:

ArgumentParser.print\_usage(_file\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.print_usage "Link to this definition")

Print a brief description of how the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 should be invoked on the command line. If _file_ is `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 is assumed.

ArgumentParser.print\_help(_file\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.print_help "Link to this definition")

Print a help message, including the program usage and information about the arguments registered with the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
. If _file_ is `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 is assumed.

There are also variants of these methods that simply return a string instead of printing it:

ArgumentParser.format\_usage()[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.format_usage "Link to this definition")

Return a string containing a brief description of how the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 should be invoked on the command line.

ArgumentParser.format\_help()[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.format_help "Link to this definition")

Return a string containing a help message, including the program usage and information about the arguments registered with the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
.

### Partial parsing[¶](https://docs.python.org/3/library/argparse.html#partial-parsing "Link to this heading")

ArgumentParser.parse\_known\_args(_args\=None_, _namespace\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "Link to this definition")

Sometimes a script only needs to handle a specific set of command-line arguments, leaving any unrecognized arguments for another script or program. In these cases, the `parse_known_args()` method can be useful.

This method works similarly to [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
, but it does not raise an error for extra, unrecognized arguments. Instead, it parses the known arguments and returns a two item tuple that contains the populated namespace and the list of any unrecognized arguments.

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo', action\='store\_true')
\>>> parser.add\_argument('bar')
\>>> parser.parse\_known\_args(\['--foo', '--badger', 'BAR', 'spam'\])
(Namespace(bar='BAR', foo=True), \['--badger', 'spam'\])

Warning

[Prefix matching](https://docs.python.org/3/library/argparse.html#prefix-matching)
 rules apply to [`parse_known_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "argparse.ArgumentParser.parse_known_args")
. The parser may consume an option even if it’s just a prefix of one of its known options, instead of leaving it in the remaining arguments list.

### Customizing file parsing[¶](https://docs.python.org/3/library/argparse.html#customizing-file-parsing "Link to this heading")

ArgumentParser.convert\_arg\_line\_to\_args(_arg\_line_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args "Link to this definition")

Arguments that are read from a file (see the _fromfile\_prefix\_chars_ keyword argument to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
 constructor) are read one argument per line. `convert_arg_line_to_args()` can be overridden for fancier reading.

This method takes a single argument _arg\_line_ which is a string read from the argument file. It returns a list of arguments parsed from this string. The method is called once per line read from the argument file, in order.

A useful override of this method is one that treats each space-separated word as an argument. The following example demonstrates how to do this:

Copy

class MyArgumentParser(argparse.ArgumentParser):
    def convert\_arg\_line\_to\_args(self, arg\_line):
        return arg\_line.split()

Note that with this override an argument can no longer contain spaces, since each space-separated word becomes a separate argument.

### Exiting methods[¶](https://docs.python.org/3/library/argparse.html#exiting-methods "Link to this heading")

ArgumentParser.exit(_status\=0_, _message\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.exit "Link to this definition")

This method terminates the program, exiting with the specified _status_ and, if given, it prints a _message_ to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 before that. The user can override this method to handle these steps differently:

Copy

class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def exit(self, status\=0, message\=None):
        if status:
            raise Exception(f'Exiting because of an error: {message}')
        exit(status)

ArgumentParser.error(_message_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.error "Link to this definition")

This method prints a usage message, including the _message_, to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 and terminates the program with a status code of 2.

### Intermixed parsing[¶](https://docs.python.org/3/library/argparse.html#intermixed-parsing "Link to this heading")

ArgumentParser.parse\_intermixed\_args(_args\=None_, _namespace\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "Link to this definition")

ArgumentParser.parse\_known\_intermixed\_args(_args\=None_, _namespace\=None_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_intermixed_args "Link to this definition")

A number of Unix commands allow the user to intermix optional arguments with positional arguments. The [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args")
 and `parse_known_intermixed_args()` methods support this parsing style.

These parsers do not support all the `argparse` features, and will raise exceptions if unsupported features are used. In particular, subparsers, and mutually exclusive groups that include both optionals and positionals are not supported.

The following example shows the difference between [`parse_known_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "argparse.ArgumentParser.parse_known_args")
 and [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args")
: the former returns `['2', '3']` as unparsed arguments, while the latter collects all the positionals into `rest`.

Copy

\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument('--foo')
\>>> parser.add\_argument('cmd')
\>>> parser.add\_argument('rest', nargs\='\*', type\=int)
\>>> parser.parse\_known\_args('doit 1 --foo bar 2 3'.split())
(Namespace(cmd='doit', foo='bar', rest=\[1\]), \['2', '3'\])
\>>> parser.parse\_intermixed\_args('doit 1 --foo bar 2 3'.split())
Namespace(cmd='doit', foo='bar', rest=\[1, 2, 3\])

`parse_known_intermixed_args()` returns a two item tuple containing the populated namespace and the list of remaining argument strings. [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args")
 raises an error if there are any remaining unparsed argument strings.

Added in version 3.7.

### Registering custom types or actions[¶](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions "Link to this heading")

ArgumentParser.register(_registry\_name_, _value_, _object_)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "Link to this definition")

Sometimes it’s desirable to use a custom string in error messages to provide more user-friendly output. In these cases, `register()` can be used to register custom actions or types with a parser and allow you to reference the type by their registered name instead of their callable name.

The `register()` method accepts three arguments - a _registry\_name_, specifying the internal registry where the object will be stored (e.g., `action`, `type`), _value_, which is the key under which the object will be registered, and object, the callable to be registered.

The following example shows how to register a custom type with a parser:

Copy

\>>> import argparse
\>>> parser \= argparse.ArgumentParser()
\>>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
\>>> parser.add\_argument('--foo', type\='hexadecimal integer')
\_StoreAction(option\_strings=\['--foo'\], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
\>>> parser.parse\_args(\['--foo', '0xFA'\])
Namespace(foo=250)
\>>> parser.parse\_args(\['--foo', '1.2'\])
usage: PROG \[-h\] \[--foo FOO\]
PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'

Exceptions[¶](https://docs.python.org/3/library/argparse.html#exceptions "Link to this heading")

-------------------------------------------------------------------------------------------------

exception argparse.ArgumentError[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentError "Link to this definition")

An error from creating or using an argument (optional or positional).

The string value of this exception is the message, augmented with information about the argument that caused it.

exception argparse.ArgumentTypeError[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentTypeError "Link to this definition")

Raised when something goes wrong converting a command line string to a type.

Guides and Tutorials

*   [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
    
*   [Migrating `optparse` code to `argparse`](https://docs.python.org/3/howto/argparse-optparse.html)
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html#)
    *   [ArgumentParser objects](https://docs.python.org/3/library/argparse.html#argumentparser-objects)
        *   [`prog`](https://docs.python.org/3/library/argparse.html#prog)
            
        *   [`usage`](https://docs.python.org/3/library/argparse.html#usage)
            
        *   [`description`](https://docs.python.org/3/library/argparse.html#description)
            
        *   [`epilog`](https://docs.python.org/3/library/argparse.html#epilog)
            
        *   [`parents`](https://docs.python.org/3/library/argparse.html#parents)
            
        *   [`formatter_class`](https://docs.python.org/3/library/argparse.html#formatter-class)
            
        *   [`prefix_chars`](https://docs.python.org/3/library/argparse.html#prefix-chars)
            
        *   [`fromfile_prefix_chars`](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars)
            
        *   [`argument_default`](https://docs.python.org/3/library/argparse.html#argument-default)
            
        *   [`allow_abbrev`](https://docs.python.org/3/library/argparse.html#allow-abbrev)
            
        *   [`conflict_handler`](https://docs.python.org/3/library/argparse.html#conflict-handler)
            
        *   [`add_help`](https://docs.python.org/3/library/argparse.html#add-help)
            
        *   [`exit_on_error`](https://docs.python.org/3/library/argparse.html#exit-on-error)
            
        *   [`suggest_on_error`](https://docs.python.org/3/library/argparse.html#suggest-on-error)
            
        *   [`color`](https://docs.python.org/3/library/argparse.html#color)
            
    *   [The add\_argument() method](https://docs.python.org/3/library/argparse.html#the-add-argument-method)
        *   [`name` or `flags`](https://docs.python.org/3/library/argparse.html#name-or-flags)
            
        *   [`action`](https://docs.python.org/3/library/argparse.html#action)
            
        *   [`nargs`](https://docs.python.org/3/library/argparse.html#nargs)
            
        *   [`const`](https://docs.python.org/3/library/argparse.html#const)
            
        *   [`default`](https://docs.python.org/3/library/argparse.html#default)
            
        *   [`type`](https://docs.python.org/3/library/argparse.html#type)
            
        *   [`choices`](https://docs.python.org/3/library/argparse.html#choices)
            
        *   [`required`](https://docs.python.org/3/library/argparse.html#required)
            
        *   [`help`](https://docs.python.org/3/library/argparse.html#help)
            
        *   [`metavar`](https://docs.python.org/3/library/argparse.html#metavar)
            
        *   [`dest`](https://docs.python.org/3/library/argparse.html#dest)
            
        *   [`deprecated`](https://docs.python.org/3/library/argparse.html#deprecated)
            
        *   [Action classes](https://docs.python.org/3/library/argparse.html#action-classes)
            
    *   [The parse\_args() method](https://docs.python.org/3/library/argparse.html#the-parse-args-method)
        *   [Option value syntax](https://docs.python.org/3/library/argparse.html#option-value-syntax)
            
        *   [Invalid arguments](https://docs.python.org/3/library/argparse.html#invalid-arguments)
            
        *   [Arguments containing `-`](https://docs.python.org/3/library/argparse.html#arguments-containing)
            
        *   [Argument abbreviations (prefix matching)](https://docs.python.org/3/library/argparse.html#argument-abbreviations-prefix-matching)
            
        *   [Beyond `sys.argv`](https://docs.python.org/3/library/argparse.html#beyond-sys-argv)
            
        *   [The Namespace object](https://docs.python.org/3/library/argparse.html#the-namespace-object)
            
    *   [Other utilities](https://docs.python.org/3/library/argparse.html#other-utilities)
        *   [Subcommands](https://docs.python.org/3/library/argparse.html#subcommands)
            
        *   [FileType objects](https://docs.python.org/3/library/argparse.html#filetype-objects)
            
        *   [Argument groups](https://docs.python.org/3/library/argparse.html#argument-groups)
            
        *   [Mutual exclusion](https://docs.python.org/3/library/argparse.html#mutual-exclusion)
            
        *   [Parser defaults](https://docs.python.org/3/library/argparse.html#parser-defaults)
            
        *   [Printing help](https://docs.python.org/3/library/argparse.html#printing-help)
            
        *   [Partial parsing](https://docs.python.org/3/library/argparse.html#partial-parsing)
            
        *   [Customizing file parsing](https://docs.python.org/3/library/argparse.html#customizing-file-parsing)
            
        *   [Exiting methods](https://docs.python.org/3/library/argparse.html#exiting-methods)
            
        *   [Intermixed parsing](https://docs.python.org/3/library/argparse.html#intermixed-parsing)
            
        *   [Registering custom types or actions](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions)
            
    *   [Exceptions](https://docs.python.org/3/library/argparse.html#exceptions)
        

#### Previous topic

[Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html "previous chapter")

#### Next topic

[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=argparse+%E2%80%94+Parser+for+command-line+options%2C+arguments+and+subcommands&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fargparse.html&pagesource=library%2Fargparse.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/argparse.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/argparse.html "Argparse Tutorial")
     |
*   [previous](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries")
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
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
     »
*   [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
    
*    
    
    |
*   Theme Auto Light Dark |