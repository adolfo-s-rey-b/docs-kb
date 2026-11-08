### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/2.7.html "What’s New in Python 2.7")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.1.html "What’s New In Python 3.1")
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
*   [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s New In Python 3.0[¶](https://docs.python.org/3/whatsnew/3.0.html#what-s-new-in-python-3-0 "Link to this heading")

=========================================================================================================================

Author:

Guido van Rossum

This article explains the new features in Python 3.0, compared to 2.6. Python 3.0, also known as “Python 3000” or “Py3K”, is the first ever _intentionally backwards incompatible_ Python release. Python 3.0 was released on December 3, 2008. There are more changes than in a typical release, and more that are important for all Python users. Nevertheless, after digesting the changes, you’ll find that Python really hasn’t changed all that much – by and large, we’re mostly fixing well-known annoyances and warts, and removing a lot of old cruft.

This article doesn’t attempt to provide a complete specification of all new features, but instead tries to give a convenient overview. For full details, you should refer to the documentation for Python 3.0, and/or the many PEPs referenced in the text. If you want to understand the complete implementation and design rationale for a particular feature, PEPs usually have more details than the regular documentation; but note that PEPs usually are not kept up-to-date once a feature has been fully implemented.

Due to time constraints this document is not as complete as it should have been. As always for a new release, the `Misc/NEWS` file in the source distribution contains a wealth of detailed information about every small thing that was changed.

Common Stumbling Blocks[¶](https://docs.python.org/3/whatsnew/3.0.html#common-stumbling-blocks "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

This section lists those few changes that are most likely to trip you up if you’re used to Python 2.5.

### Print Is A Function[¶](https://docs.python.org/3/whatsnew/3.0.html#print-is-a-function "Link to this heading")

The `print` statement has been replaced with a [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function, with keyword arguments to replace most of the special syntax of the old `print` statement ([**PEP 3105**](https://peps.python.org/pep-3105/)
). Examples:

Copy

Old: print "The answer is", 2\*2
New: print("The answer is", 2\*2)

Old: print x,           \# Trailing comma suppresses newline
New: print(x, end\=" ")  \# Appends a space instead of a newline

Old: print              \# Prints a newline
New: print()            \# You must call the function!

Old: print \>>sys.stderr, "fatal error"
New: print("fatal error", file\=sys.stderr)

Old: print (x, y)       \# prints repr((x, y))
New: print((x, y))      \# Not the same as print(x, y)!

You can also customize the separator between items, e.g.:

Copy

print("There are <", 2\*\*32, "> possibilities!", sep\="")

which produces:

There are <4294967296> possibilities!

Note:

*   The [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
     function doesn’t support the “softspace” feature of the old `print` statement. For example, in Python 2.x, `print "A\n", "B"` would write `"A\nB\n"`; but in Python 3.0, `print("A\n", "B")` writes `"A\n B\n"`.
    
*   Initially, you’ll be finding yourself typing the old `print x` a lot in interactive mode. Time to retrain your fingers to type `print(x)` instead!
    
*   When using the `2to3` source-to-source conversion tool, all `print` statements are automatically converted to [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
     function calls, so this is mostly a non-issue for larger projects.
    

### Views And Iterators Instead Of Lists[¶](https://docs.python.org/3/whatsnew/3.0.html#views-and-iterators-instead-of-lists "Link to this heading")

Some well-known APIs no longer return lists:

*   [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
     methods [`dict.keys()`](https://docs.python.org/3/builtins/stdtypes.html#dict.keys "dict.keys")
    , [`dict.items()`](https://docs.python.org/3/builtins/stdtypes.html#dict.items "dict.items")
     and [`dict.values()`](https://docs.python.org/3/builtins/stdtypes.html#dict.values "dict.values")
     return “views” instead of lists. For example, this no longer works: `k = d.keys(); k.sort()`. Use `k = sorted(d)` instead (this works in Python 2.5 too and is just as efficient).
    
*   Also, the `dict.iterkeys()`, `dict.iteritems()` and `dict.itervalues()` methods are no longer supported.
    
*   [`map()`](https://docs.python.org/3/builtins/functions.html#map "map")
     and [`filter()`](https://docs.python.org/3/builtins/functions.html#filter "filter")
     return iterators. If you really need a list and the input sequences are all of equal length, a quick fix is to wrap `map()` in [`list()`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
    , e.g. `list(map(...))`, but a better fix is often to use a list comprehension (especially when the original code uses [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda)
    ), or rewriting the code so it doesn’t need a list at all. Particularly tricky is `map()` invoked for the side effects of the function; the correct transformation is to use a regular [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
     loop (since creating a list would just be wasteful).
    
    If the input sequences are not of equal length, [`map()`](https://docs.python.org/3/builtins/functions.html#map "map")
     will stop at the termination of the shortest of the sequences. For full compatibility with `map()` from Python 2.x, also wrap the sequences in [`itertools.zip_longest()`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest "itertools.zip_longest")
    , e.g. `map(func, *sequences)` becomes `list(map(func, itertools.zip_longest(*sequences)))`.
    
*   [`range()`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
     now behaves like `xrange()` used to behave, except it works with values of arbitrary size. The latter no longer exists.
    
*   [`zip()`](https://docs.python.org/3/builtins/functions.html#zip "zip")
     now returns an iterator.
    

### Ordering Comparisons[¶](https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons "Link to this heading")

Python 3.0 has simplified the rules for ordering comparisons:

*   The ordering comparison operators (`<`, `<=`, `>=`, `>`) raise a TypeError exception when the operands don’t have a meaningful natural ordering. Thus, expressions like `1 < ''`, `0 > None` or `len <= len` are no longer valid, and e.g. `None < None` raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     instead of returning `False`. A corollary is that sorting a heterogeneous list no longer makes sense – all the elements must be comparable to each other. Note that this does not apply to the `==` and `!=` operators: objects of different incomparable types always compare unequal to each other.
    
*   [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
     and [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
     no longer accept the _cmp_ argument providing a comparison function. Use the _key_ argument instead. N.B. the _key_ and _reverse_ arguments are now “keyword-only”.
    
*   The `cmp()` function should be treated as gone, and the `__cmp__()` special method is no longer supported. Use [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
     for sorting, [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
     with [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
    , and other rich comparisons as needed. (If you really need the `cmp()` functionality, you could use the expression `(a > b) - (a < b)` as the equivalent for `cmp(a, b)`.)
    

### Integers[¶](https://docs.python.org/3/whatsnew/3.0.html#integers "Link to this heading")

*   [**PEP 237**](https://peps.python.org/pep-0237/)
    : Essentially, `long` renamed to [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
    . That is, there is only one built-in integral type, named `int`; but it behaves mostly like the old `long` type.
    
*   [**PEP 238**](https://peps.python.org/pep-0238/)
    : An expression like `1/2` returns a float. Use `1//2` to get the truncating behavior. (The latter syntax has existed for years, at least since Python 2.2.)
    
*   The `sys.maxint` constant was removed, since there is no longer a limit to the value of integers. However, [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize")
     can be used as an integer larger than any practical list or string index. It conforms to the implementation’s “natural” integer size and is typically the same as `sys.maxint` in previous releases on the same platform (assuming the same build options).
    
*   The [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
     of a long integer doesn’t include the trailing `L` anymore, so code that unconditionally strips that character will chop off the last digit instead. (Use [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     instead.)
    
*   Octal literals are no longer of the form `0720`; use `0o720` instead.
    

### Text Vs. Data Instead Of Unicode Vs. 8-bit[¶](https://docs.python.org/3/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit "Link to this heading")

Everything you thought you knew about binary data and Unicode has changed.

*   Python 3.0 uses the concepts of _text_ and (binary) _data_ instead of Unicode strings and 8-bit strings. All text is Unicode; however _encoded_ Unicode is represented as binary data. The type used to hold text is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    , the type used to hold data is [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    . The biggest difference with the 2.x situation is that any attempt to mix text and data in Python 3.0 raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
    , whereas if you were to mix Unicode and 8-bit strings in Python 2.x, it would work if the 8-bit string happened to contain only 7-bit (ASCII) bytes, but you would get [`UnicodeDecodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")
     if it contained non-ASCII values. This value-specific behavior has caused numerous sad faces over the years.
    
*   As a consequence of this change in philosophy, pretty much all code that uses Unicode, encodings or binary data most likely has to change. The change is for the better, as in the 2.x world there were numerous bugs having to do with mixing encoded and unencoded text. To be prepared in Python 2.x, start using `unicode` for all unencoded text, and [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     for binary or encoded data only. Then the `2to3` tool will do most of the work for you.
    
*   You can no longer use `u"..."` literals for Unicode text. However, you must use `b"..."` literals for binary data.
    
*   As the [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     and [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     types cannot be mixed, you must always explicitly convert between them. Use [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
     to go from `str` to `bytes`, and [`bytes.decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.decode "bytes.decode")
     to go from `bytes` to `str`. You can also use `bytes(s, encoding=...)` and `str(b, encoding=...)`, respectively.
    
*   Like [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    , the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     type is immutable. There is a separate _mutable_ type to hold buffered binary data, [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    . Nearly all APIs that accept `bytes` also accept `bytearray`. The mutable API is based on [`collections.MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")
    .
    
*   All backslashes in raw string literals are interpreted literally. This means that `'\U'` and `'\u'` escapes in raw strings are not treated specially. For example, `r'\u20ac'` is a string of 6 characters in Python 3.0, whereas in 2.6, `ur'\u20ac'` was the single “euro” character. (Of course, this change only affects raw string literals; the euro character is `'\u20ac'` in Python 3.0.)
    
*   The built-in `basestring` abstract type was removed. Use [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     instead. The `str` and [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     types don’t have functionality enough in common to warrant a shared base class. The `2to3` tool (see below) replaces every occurrence of `basestring` with `str`.
    
*   Files opened as text files (still the default mode for [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
    ) always use an encoding to map between strings (in memory) and bytes (on disk). Binary files (opened with a `b` in the mode argument) always use bytes in memory. This means that if a file is opened using an incorrect mode or encoding, I/O will likely fail loudly, instead of silently producing incorrect data. It also means that even Unix users will have to specify the correct mode (text or binary) when opening a file. There is a platform-dependent default encoding, which on Unixy platforms can be set with the `LANG` environment variable (and sometimes also with some other platform-specific locale-related environment variables). In many cases, but not all, the system default is UTF-8; you should never count on this default. Any application reading or writing more than pure ASCII text should probably have a way to override the encoding. There is no longer any need for using the encoding-aware streams in the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
     module.
    
*   The initial values of [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
    , [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
     and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
     are now unicode-only text files (i.e., they are instances of [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase")
    ). To read and write bytes data with these streams, you need to use their [`io.TextIOBase.buffer`](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "io.TextIOBase.buffer")
     attribute.
    
*   Filenames are passed to and returned from APIs as (Unicode) strings. This can present platform-specific problems because on some platforms filenames are arbitrary byte strings. (On the other hand, on Windows filenames are natively stored as Unicode.) As a work-around, most APIs (e.g. [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
     and many functions in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module) that take filenames accept [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     objects as well as strings, and a few APIs have a way to ask for a `bytes` return value. Thus, [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir")
     returns a list of `bytes` instances if the argument is a `bytes` instance, and [`os.getcwdb()`](https://docs.python.org/3/library/os.html#os.getcwdb "os.getcwdb")
     returns the current working directory as a `bytes` instance. Note that when `os.listdir()` returns a list of strings, filenames that cannot be decoded properly are omitted rather than raising [`UnicodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError "UnicodeError")
    .
    
*   Some system APIs like [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
     and [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
     can also present problems when the bytes made available by the system is not interpretable using the default encoding. Setting the `LANG` variable and rerunning the program is probably the best approach.
    
*   [**PEP 3138**](https://peps.python.org/pep-3138/)
    : The [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
     of a string no longer escapes non-ASCII characters. It still escapes control characters and code points with non-printable status in the Unicode standard, however.
    
*   [**PEP 3120**](https://peps.python.org/pep-3120/)
    : The default source encoding is now UTF-8.
    
*   [**PEP 3131**](https://peps.python.org/pep-3131/)
    : Non-ASCII letters are now allowed in identifiers. (However, the standard library remains ASCII-only with the exception of contributor names in comments.)
    
*   The `StringIO` and `cStringIO` modules are gone. Instead, import the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
     module and use [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
     or [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
     for text and data respectively.
    
*   See also the [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto)
    , which was updated for Python 3.0.
    

Overview Of Syntax Changes[¶](https://docs.python.org/3/whatsnew/3.0.html#overview-of-syntax-changes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

This section gives a brief overview of every _syntactic_ change in Python 3.0.

### New Syntax[¶](https://docs.python.org/3/whatsnew/3.0.html#new-syntax "Link to this heading")

*   [**PEP 3107**](https://peps.python.org/pep-3107/)
    : Function argument and return value annotations. This provides a standardized way of annotating a function’s parameters and return value. There are no semantics attached to such annotations except that they can be introspected at runtime using the [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__")
     attribute. The intent is to encourage experimentation through metaclasses, decorators or frameworks.
    
*   [**PEP 3102**](https://peps.python.org/pep-3102/)
    : Keyword-only arguments. Named parameters occurring after `*args` in the parameter list _must_ be specified using keyword syntax in the call. You can also use a bare `*` in the parameter list to indicate that you don’t accept a variable-length argument list, but you do have keyword-only arguments.
    
*   Keyword arguments are allowed after the list of base classes in a class definition. This is used by the new convention for specifying a metaclass (see next section), but can be used for other purposes as well, as long as the metaclass supports it.
    
*   [**PEP 3104**](https://peps.python.org/pep-3104/)
    : [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
     statement. Using `nonlocal x` you can now assign directly to a variable in an outer (but non-global) scope. `nonlocal` is a new reserved word.
    
*   [**PEP 3132**](https://peps.python.org/pep-3132/)
    : Extended Iterable Unpacking. You can now write things like `a, b, *rest = some_sequence`. And even `*rest, a = stuff`. The `rest` object is always a (possibly empty) list; the right-hand side may be any iterable. Example:
    
    Copy
    
    (a, \*rest, b) \= range(5)
    
    This sets _a_ to `0`, _b_ to `4`, and _rest_ to `[1, 2, 3]`.
    
*   Dictionary comprehensions: `{k: v for k, v in stuff}` means the same thing as `dict(stuff)` but is more flexible. (This is [**PEP 274**](https://peps.python.org/pep-0274/)
     vindicated. :-)
    
*   Set literals, e.g. `{1, 2}`. Note that `{}` is an empty dictionary; use `set()` for an empty set. Set comprehensions are also supported; e.g., `{x for x in stuff}` means the same thing as `set(stuff)` but is more flexible.
    
*   New octal literals, e.g. `0o720` (already in 2.6). The old octal literals (`0720`) are gone.
    
*   New binary literals, e.g. `0b1010` (already in 2.6), and there is a new corresponding built-in function, [`bin()`](https://docs.python.org/3/builtins/functions.html#bin "bin")
    .
    
*   Bytes literals are introduced with a leading `b` or `B`, and there is a new corresponding built-in function, [`bytes()`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    

### Changed Syntax[¶](https://docs.python.org/3/whatsnew/3.0.html#changed-syntax "Link to this heading")

*   [**PEP 3109**](https://peps.python.org/pep-3109/)
     and [**PEP 3134**](https://peps.python.org/pep-3134/)
    : new [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise)
     statement syntax: `raise [_expr_ [from _expr_]]`. See below.
    
*   `as` and [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     are now reserved words. (Since 2.6, actually.)
    
*   `True`, `False`, and `None` are reserved words. (2.6 partially enforced the restrictions on `None` already.)
    
*   Change from [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     _exc_, _var_ to `except` _exc_ `as` _var_. See [**PEP 3110**](https://peps.python.org/pep-3110/)
    .
    
*   [**PEP 3115**](https://peps.python.org/pep-3115/)
    : New Metaclass Syntax. Instead of:
    
    Copy
    
    class C:
        \_\_metaclass\_\_ \= M
        ...
    
    you must now use:
    
    Copy
    
    class C(metaclass\=M):
        ...
    
    The module-global `__metaclass__` variable is no longer supported. (It was a crutch to make it easier to default to new-style classes without deriving every class from [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
    .)
    
*   List comprehensions no longer support the syntactic form `[... for _var_ in _item1_, _item2_, ...]`. Use `[... for _var_ in (_item1_, _item2_, ...)]` instead. Also note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a [`list()`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
     constructor, and in particular the loop control variables are no longer leaked into the surrounding scope.
    
*   The _ellipsis_ (`...`) can be used as an atomic expression anywhere. (Previously it was only allowed in slices.) Also, it _must_ now be spelled as `...`. (Previously it could also be spelled as `. . .`, by a mere accident of the grammar.)
    

### Removed Syntax[¶](https://docs.python.org/3/whatsnew/3.0.html#removed-syntax "Link to this heading")

*   [**PEP 3113**](https://peps.python.org/pep-3113/)
    : Tuple parameter unpacking removed. You can no longer write `def foo(a, (b, c)): ...`. Use `def foo(a, b_c): b, c = b_c` instead.
    
*   Removed backticks (use [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
     instead).
    
*   Removed `<>` (use `!=` instead).
    
*   Removed keyword: [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
     is no longer a keyword; it remains as a function. (Fortunately the function syntax was also accepted in 2.x.) Also note that `exec()` no longer takes a stream argument; instead of `exec(f)` you can use `exec(f.read())`.
    
*   Integer literals no longer support a trailing `l` or `L`.
    
*   String literals no longer support a leading `u` or `U`.
    
*   The [`from`](https://docs.python.org/3/reference/simple_stmts.html#from)
     _module_ [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
     `*` syntax is only allowed at the module level, no longer inside functions.
    
*   The only acceptable syntax for relative imports is `from .[_module_] import _name_`. All [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
     forms not starting with `.` are interpreted as absolute imports. ([**PEP 328**](https://peps.python.org/pep-0328/)
    )
    
*   Classic classes are gone.
    

Changes Already Present In Python 2.6[¶](https://docs.python.org/3/whatsnew/3.0.html#changes-already-present-in-python-2-6 "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Since many users presumably make the jump straight from Python 2.5 to Python 3.0, this section reminds the reader of new features that were originally designed for Python 3.0 but that were back-ported to Python 2.6. The corresponding sections in [What’s New in Python 2.6](https://docs.python.org/3/whatsnew/2.6.html#whats-new-in-2-6)
 should be consulted for longer descriptions.

*   [PEP 343: The ‘with’ statement](https://docs.python.org/3/whatsnew/2.6.html#pep-0343)
    . The [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     statement is now a standard feature and no longer needs to be imported from the [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
    . Also check out [Writing Context Managers](https://docs.python.org/3/whatsnew/2.6.html#new-26-context-managers)
     and [The contextlib module](https://docs.python.org/3/whatsnew/2.6.html#new-module-contextlib)
    .
    
*   [PEP 366: Explicit Relative Imports From a Main Module](https://docs.python.org/3/whatsnew/2.6.html#pep-0366)
    . This enhances the usefulness of the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
     option when the referenced module lives in a package.
    
*   [PEP 370: Per-user site-packages Directory](https://docs.python.org/3/whatsnew/2.6.html#pep-0370)
    .
    
*   [PEP 371: The multiprocessing Package](https://docs.python.org/3/whatsnew/2.6.html#pep-0371)
    .
    
*   [PEP 3101: Advanced String Formatting](https://docs.python.org/3/whatsnew/2.6.html#pep-3101)
    . Note: the 2.6 description mentions the [`format()`](https://docs.python.org/3/builtins/functions.html#format "format")
     method for both 8-bit and Unicode strings. In 3.0, only the [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     type (text strings with Unicode support) supports this method; the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     type does not. The plan is to eventually make this the only API for string formatting, and to start deprecating the `%` operator in Python 3.1.
    
*   [PEP 3105: print As a Function](https://docs.python.org/3/whatsnew/2.6.html#pep-3105)
    . This is now a standard feature and no longer needs to be imported from [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
    . More details were given above.
    
*   [PEP 3110: Exception-Handling Changes](https://docs.python.org/3/whatsnew/2.6.html#pep-3110)
    . The [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     _exc_ `as` _var_ syntax is now standard and `except` _exc_, _var_ is no longer supported. (Of course, the `as` _var_ part is still optional.)
    
*   [PEP 3112: Byte Literals](https://docs.python.org/3/whatsnew/2.6.html#pep-3112)
    . The `b"..."` string literal notation (and its variants like `b'...'`, `b"""..."""`, and `br"..."`) now produces a literal of type [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   [PEP 3116: New I/O Library](https://docs.python.org/3/whatsnew/2.6.html#pep-3116)
    . The [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
     module is now the standard way of doing file I/O. The built-in [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
     function is now an alias for [`io.open()`](https://docs.python.org/3/library/io.html#io.open "io.open")
     and has additional keyword arguments _encoding_, _errors_, _newline_ and _closefd_. Also note that an invalid _mode_ argument now raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
    , not [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
    . The binary file object underlying a text file object can be accessed as `f.buffer` (but beware that the text object maintains a buffer of itself in order to speed up the encoding and decoding operations).
    
*   [PEP 3118: Revised Buffer Protocol](https://docs.python.org/3/whatsnew/2.6.html#pep-3118)
    . The old builtin `buffer()` is now really gone; the new builtin [`memoryview()`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
     provides (mostly) similar functionality.
    
*   [PEP 3119: Abstract Base Classes](https://docs.python.org/3/whatsnew/2.6.html#pep-3119)
    . The [`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")
     module and the ABCs defined in the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
     module plays a somewhat more prominent role in the language now, and built-in collection types like [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
     and [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
     conform to the [`collections.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping")
     and [`collections.MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")
     ABCs, respectively.
    
*   [PEP 3127: Integer Literal Support and Syntax](https://docs.python.org/3/whatsnew/2.6.html#pep-3127)
    . As mentioned above, the new octal literal notation is the only one supported, and binary literals have been added.
    
*   [PEP 3129: Class Decorators](https://docs.python.org/3/whatsnew/2.6.html#pep-3129)
    .
    
*   [PEP 3141: A Type Hierarchy for Numbers](https://docs.python.org/3/whatsnew/2.6.html#pep-3141)
    . The [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).")
     module is another new use of ABCs, defining Python’s “numeric tower”. Also note the new [`fractions`](https://docs.python.org/3/library/fractions.html#module-fractions "fractions: Rational numbers.")
     module which implements [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational")
    .
    

Library Changes[¶](https://docs.python.org/3/whatsnew/3.0.html#library-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------

Due to time constraints, this document does not exhaustively cover the very extensive changes to the standard library. [**PEP 3108**](https://peps.python.org/pep-3108/)
 is the reference for the major changes to the library. Here’s a capsule review:

*   Many old modules were removed. Some, like `gopherlib` (no longer used) and `md5` (replaced by [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
    ), were already deprecated by [**PEP 4**](https://peps.python.org/pep-0004/)
    . Others were removed as a result of the removal of support for various platforms such as Irix, BeOS and Mac OS 9 (see [**PEP 11**](https://peps.python.org/pep-0011/)
    ). Some modules were also selected for removal in Python 3.0 due to lack of use or because a better replacement exists. See [**PEP 3108**](https://peps.python.org/pep-3108/)
     for an exhaustive list.
    
*   The `bsddb3` package was removed because its presence in the core standard library has proved over time to be a particular burden for the core developers due to testing instability and Berkeley DB’s release schedule. However, the package is alive and well, externally maintained at [https://www.jcea.es/programacion/pybsddb.htm](https://www.jcea.es/programacion/pybsddb.htm)
    .
    
*   Some modules were renamed because their old name disobeyed [**PEP 8**](https://peps.python.org/pep-0008/)
    , or for various other reasons. Here’s the list:
    
    | Old Name | New Name |
    | --- | --- |
    | \_winreg | winreg |
    | ConfigParser | configparser |
    | copy\_reg | copyreg |
    | Queue | queue |
    | SocketServer | socketserver |
    | markupbase | \_markupbase |
    | repr | reprlib |
    | test.test\_support | test.support |
    
*   A common pattern in Python 2.x is to have one version of a module implemented in pure Python, with an optional accelerated version implemented as a C extension; for example, [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
     and `cPickle`. This places the burden of importing the accelerated version and falling back on the pure Python version on each user of these modules. In Python 3.0, the accelerated versions are considered implementation details of the pure Python versions. Users should always import the standard version, which attempts to import the accelerated version and falls back to the pure Python version. The `pickle` / `cPickle` pair received this treatment. The [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
     module is on the list for 3.1. The `StringIO` module has been turned into a class in the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
     module.
    
*   Some related modules have been grouped into packages, and usually the submodule names have been simplified. The resulting new packages are:
    
    *   [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.")
         (`anydbm`, `dbhash`, `dbm`, `dumbdbm`, `gdbm`, `whichdb`).
        
    *   [`html`](https://docs.python.org/3/library/html.html#module-html "html: Helpers for manipulating HTML.")
         (`HTMLParser`, `htmlentitydefs`).
        
    *   [`http`](https://docs.python.org/3/library/http.html#module-http "http: HTTP status codes and messages")
         (`httplib`, `BaseHTTPServer`, `CGIHTTPServer`, `SimpleHTTPServer`, `Cookie`, `cookielib`).
        
    *   [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
         (all `Tkinter`\-related modules except [`turtle`](https://docs.python.org/3/library/turtle.html#module-turtle "turtle: An educational framework for simple graphics applications")
        ). The target audience of `turtle` doesn’t really care about `tkinter`. Also note that as of Python 2.6, the functionality of `turtle` has been greatly enhanced.
        
    *   [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "urllib")
         (`urllib`, `urllib2`, `urlparse`, `robotparse`).
        
    *   [`xmlrpc`](https://docs.python.org/3/library/xmlrpc.html#module-xmlrpc "xmlrpc: Server and client modules implementing XML-RPC.")
         (`xmlrpclib`, `DocXMLRPCServer`, `SimpleXMLRPCServer`).
        

Some other changes to standard library modules, not covered by [**PEP 3108**](https://peps.python.org/pep-3108/)
:

*   Killed `sets`. Use the built-in [`set()`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
     class.
    
*   Cleanup of the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
     module: removed `sys.exitfunc()`, `sys.exc_clear()`, `sys.exc_type`, `sys.exc_value`, `sys.exc_traceback`. (Note that [`sys.last_type`](https://docs.python.org/3/library/sys.html#sys.last_type "sys.last_type")
     etc. remain.)
    
*   Cleanup of the [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array")
     type: the `read()` and `write()` methods are gone; use [`fromfile()`](https://docs.python.org/3/library/array.html#array.array.fromfile "array.array.fromfile")
     and [`tofile()`](https://docs.python.org/3/library/array.html#array.array.tofile "array.array.tofile")
     instead. Also, the `'c'` typecode for array is gone – use either `'b'` for bytes or `'u'` for Unicode characters.
    
*   Cleanup of the [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators.")
     module: removed `sequenceIncludes()` and `isCallable()`.
    
*   Cleanup of the `thread` module: `acquire_lock()` and `release_lock()` are gone; use [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire")
     and [`release()`](https://docs.python.org/3/library/threading.html#threading.Lock.release "threading.Lock.release")
     instead.
    
*   Cleanup of the [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
     module: removed the `jumpahead()` API.
    
*   The `new` module is gone.
    
*   The functions `os.tmpnam()`, `os.tempnam()` and `os.tmpfile()` have been removed in favor of the [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories.")
     module.
    
*   The [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.")
     module has been changed to work with bytes. The main entry point is now [`tokenize.tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")
    , instead of generate\_tokens.
    
*   `string.letters` and its friends (`string.lowercase` and `string.uppercase`) are gone. Use [`string.ascii_letters`](https://docs.python.org/3/library/string.html#string.ascii_letters "string.ascii_letters")
     etc. instead. (The reason for the removal is that `string.letters` and friends had locale-specific behavior, which is a bad idea for such attractively named global “constants”.)
    
*   Renamed module `__builtin__` to [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
     (removing the underscores, adding an ‘s’). The `__builtins__` variable found in most global namespaces is unchanged. To modify a builtin, you should use `builtins`, not `__builtins__`!
    

[**PEP 3101**](https://peps.python.org/pep-3101/)
: A New Approach To String Formatting[¶](https://docs.python.org/3/whatsnew/3.0.html#pep-3101-a-new-approach-to-string-formatting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   A new system for built-in string formatting operations replaces the `%` string formatting operator. (However, the `%` operator is still supported; it will be deprecated in Python 3.1 and removed from the language at some later time.) Read [**PEP 3101**](https://peps.python.org/pep-3101/)
     for the full scoop.
    

Changes To Exceptions[¶](https://docs.python.org/3/whatsnew/3.0.html#changes-to-exceptions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

The APIs for raising and catching exception have been cleaned up and new powerful features added:

*   [**PEP 352**](https://peps.python.org/pep-0352/)
    : All exceptions must be derived (directly or indirectly) from [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
    . This is the root of the exception hierarchy. This is not new as a recommendation, but the _requirement_ to inherit from `BaseException` is new. (Python 2.6 still allowed classic classes to be raised, and placed no restriction on what you can catch.) As a consequence, string exceptions are finally truly and utterly dead.
    
*   Almost all exceptions should actually derive from [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
    ; [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
     should only be used as a base class for exceptions that should only be handled at the top level, such as [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
     or [`KeyboardInterrupt`](https://docs.python.org/3/builtins/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")
    . The recommended idiom for handling all exceptions except for this latter category is to use [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     `Exception`.
    
*   `StandardError` was removed.
    
*   Exceptions no longer behave as sequences. Use the [`args`](https://docs.python.org/3/builtins/exceptions.html#BaseException.args "BaseException.args")
     attribute instead.
    
*   [**PEP 3109**](https://peps.python.org/pep-3109/)
    : Raising exceptions. You must now use `raise _Exception_(_args_)` instead of `raise _Exception_, _args_`. Additionally, you can no longer explicitly specify a traceback; instead, if you _have_ to do this, you can assign directly to the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
     attribute (see below).
    
*   [**PEP 3110**](https://peps.python.org/pep-3110/)
    : Catching exceptions. You must now use `except _SomeException_ as _variable_` instead of `except _SomeException_, _variable_`. Moreover, the _variable_ is explicitly deleted when the [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     block is left.
    
*   [**PEP 3134**](https://peps.python.org/pep-3134/)
    : Exception chaining. There are two cases: implicit chaining and explicit chaining. Implicit chaining happens when an exception is raised in an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     or [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
     handler block. This usually happens due to a bug in the handler block; we call this a _secondary_ exception. In this case, the original exception (that was being handled) is saved as the [`__context__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__context__ "BaseException.__context__")
     attribute of the secondary exception. Explicit chaining is invoked with this syntax:
    
    Copy
    
    raise SecondaryException() from primary\_exception
    
    (where _primary\_exception_ is any expression that produces an exception object, probably an exception that was previously caught). In this case, the primary exception is stored on the [`__cause__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__cause__ "BaseException.__cause__")
     attribute of the secondary exception. The traceback printed when an unhandled exception occurs walks the chain of `__cause__` and [`__context__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__context__ "BaseException.__context__")
     attributes and prints a separate traceback for each component of the chain, with the primary exception at the top. (Java users may recognize this behavior.)
    
*   [**PEP 3134**](https://peps.python.org/pep-3134/)
    : Exception objects now store their traceback as the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
     attribute. This means that an exception object now contains all the information pertaining to an exception, and there are fewer reasons to use [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
     (though the latter is not removed).
    
*   A few exception messages are improved when Windows fails to load an extension module. For example, `error code 193` is now `%1 is not a valid Win32 application`. Strings now deal with non-English locales.
    

Miscellaneous Other Changes[¶](https://docs.python.org/3/whatsnew/3.0.html#miscellaneous-other-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Operators And Special Methods[¶](https://docs.python.org/3/whatsnew/3.0.html#operators-and-special-methods "Link to this heading")

*   `!=` now returns the opposite of `==`, unless `==` returns [`NotImplemented`](https://docs.python.org/3/builtins/constants.html#NotImplemented "NotImplemented")
    .
    
*   The concept of “unbound methods” has been removed from the language. When referencing a method as a class attribute, you now get a plain function object.
    
*   `__getslice__()`, `__setslice__()` and `__delslice__()` were killed. The syntax `a[i:j]` now translates to `a.__getitem__(slice(i, j))` (or [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__")
     or [`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__")
    , when used as an assignment or deletion target, respectively).
    
*   [**PEP 3114**](https://peps.python.org/pep-3114/)
    : the standard [`next()`](https://docs.python.org/3/builtins/functions.html#next "next")
     method has been renamed to [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
    .
    
*   The `__oct__()` and `__hex__()` special methods are removed – [`oct()`](https://docs.python.org/3/builtins/functions.html#oct "oct")
     and [`hex()`](https://docs.python.org/3/builtins/functions.html#hex "hex")
     use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
     now to convert the argument to an integer.
    
*   Removed support for `__members__` and `__methods__`.
    
*   The function attributes named `func_X` have been renamed to use the `__X__` form, freeing up these names in the function attribute namespace for user-defined attributes. To wit, `func_closure`, `func_code`, `func_defaults`, `func_dict`, `func_doc`, `func_globals`, `func_name` were renamed to [`__closure__`](https://docs.python.org/3/reference/datamodel.html#function.__closure__ "function.__closure__")
    , [`__code__`](https://docs.python.org/3/reference/datamodel.html#function.__code__ "function.__code__")
    , [`__defaults__`](https://docs.python.org/3/reference/datamodel.html#function.__defaults__ "function.__defaults__")
    , [`__dict__`](https://docs.python.org/3/reference/datamodel.html#function.__dict__ "function.__dict__")
    , [`__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__")
    , [`__globals__`](https://docs.python.org/3/reference/datamodel.html#function.__globals__ "function.__globals__")
    , [`__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__")
    , respectively.
    
*   `__nonzero__()` is now [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__")
    .
    

### Builtins[¶](https://docs.python.org/3/whatsnew/3.0.html#builtins "Link to this heading")

*   [**PEP 3135**](https://peps.python.org/pep-3135/)
    : New [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
    . You can now invoke `super()` without arguments and (assuming this is in a regular instance method defined inside a [`class`](https://docs.python.org/3/reference/compound_stmts.html#class)
     statement) the right class and instance will automatically be chosen. With arguments, the behavior of `super()` is unchanged.
    
*   [**PEP 3111**](https://peps.python.org/pep-3111/)
    : `raw_input()` was renamed to [`input()`](https://docs.python.org/3/builtins/functions.html#input "input")
    . That is, the new `input()` function reads a line from [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
     and returns it with the trailing newline stripped. It raises [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
     if the input is terminated prematurely. To get the old behavior of `input()`, use `eval(input())`.
    
*   A new built-in function [`next()`](https://docs.python.org/3/builtins/functions.html#next "next")
     was added to call the [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
     method on an object.
    
*   The [`round()`](https://docs.python.org/3/builtins/functions.html#round "round")
     function rounding strategy and return type have changed. Exact halfway cases are now rounded to the nearest even result instead of away from zero. (For example, `round(2.5)` now returns `2` rather than `3`.) `round(x[, n])` now delegates to `x.__round__([n])` instead of always returning a float. It generally returns an integer when called with a single argument and a value of the same type as `x` when called with two arguments.
    
*   Moved `intern()` to [`sys.intern()`](https://docs.python.org/3/library/sys.html#sys.intern "sys.intern")
    .
    
*   Removed: `apply()`. Instead of `apply(f, args)` use `f(*args)`.
    
*   Removed [`callable()`](https://docs.python.org/3/builtins/functions.html#callable "callable")
    . Instead of `callable(f)` you can use `isinstance(f, collections.Callable)`. The `operator.isCallable()` function is also gone.
    
*   Removed `coerce()`. This function no longer serves a purpose now that classic classes are gone.
    
*   Removed `execfile()`. Instead of `execfile(fn)` use `exec(open(fn).read())`.
    
*   Removed the `file` type. Use [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
    . There are now several different kinds of streams that open can return in the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
     module.
    
*   Removed `reduce()`. Use [`functools.reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce "functools.reduce")
     if you really need it; however, 99 percent of the time an explicit [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
     loop is more readable.
    
*   Removed `reload()`. Use `imp.reload()`.
    
*   Removed. `dict.has_key()` – use the [`in`](https://docs.python.org/3/reference/expressions.html#in)
     operator instead.
    

Build and C API Changes[¶](https://docs.python.org/3/whatsnew/3.0.html#build-and-c-api-changes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Due to time constraints, here is a _very_ incomplete list of changes to the C API.

*   Support for several platforms was dropped, including but not limited to Mac OS 9, BeOS, RISCOS, Irix, and Tru64.
    
*   [**PEP 3118**](https://peps.python.org/pep-3118/)
    : New Buffer API.
    
*   [**PEP 3121**](https://peps.python.org/pep-3121/)
    : Extension Module Initialization & Finalization.
    
*   [**PEP 3123**](https://peps.python.org/pep-3123/)
    : Making [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "PyObject_HEAD")
     conform to standard C.
    
*   No more C API support for restricted execution.
    
*   `PyNumber_Coerce()`, `PyNumber_CoerceEx()`, `PyMember_Get()`, and `PyMember_Set()` C APIs are removed.
    
*   New C API `PyImport_ImportModuleNoBlock()`, works like [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
     but won’t block on the import lock (returning an error instead).
    
*   Renamed the boolean conversion C-level slot and method: `nb_nonzero` is now `nb_bool`.
    
*   Removed `METH_OLDARGS` and `WITH_CYCLE_GC` from the C API.
    

Performance[¶](https://docs.python.org/3/whatsnew/3.0.html#performance "Link to this heading")

-----------------------------------------------------------------------------------------------

The net result of the 3.0 generalizations is that Python 3.0 runs the pystone benchmark around 10% slower than Python 2.5. Most likely the biggest cause is the removal of special-casing for small integers. There’s room for improvement, but it will happen after 3.0 is released!

Porting To Python 3.0[¶](https://docs.python.org/3/whatsnew/3.0.html#porting-to-python-3-0 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

For porting existing Python 2.5 or 2.6 source code to Python 3.0, the best strategy is the following:

0.  (Prerequisite:) Start with excellent test coverage.
    
1.  Port to Python 2.6. This should be no more work than the average port from Python 2.x to Python 2.(x+1). Make sure all your tests pass.
    
2.  (Still using 2.6:) Turn on the `-3` command line switch. This enables warnings about features that will be removed (or change) in 3.0. Run your test suite again, and fix code that you get warnings about until there are no warnings left, and all your tests still pass.
    
3.  Run the `2to3` source-to-source translator over your source code tree. Run the result of the translation under Python 3.0. Manually fix up any remaining issues, fixing problems until all tests pass again.
    

It is not recommended to try to write source code that runs unchanged under both Python 2.6 and 3.0; you’d have to use a very contorted coding style, e.g. avoiding `print` statements, metaclasses, and much more. If you are maintaining a library that needs to support both Python 2.6 and Python 3.0, the best approach is to modify step 3 above by editing the 2.6 version of the source code and running the `2to3` translator again, rather than editing the 3.0 version of the source code.

For porting C extensions to Python 3.0, please see [Porting Extension Modules to Python 3](https://docs.python.org/3/howto/cporting.html#cporting-howto)
.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html#)
    *   [Common Stumbling Blocks](https://docs.python.org/3/whatsnew/3.0.html#common-stumbling-blocks)
        *   [Print Is A Function](https://docs.python.org/3/whatsnew/3.0.html#print-is-a-function)
            
        *   [Views And Iterators Instead Of Lists](https://docs.python.org/3/whatsnew/3.0.html#views-and-iterators-instead-of-lists)
            
        *   [Ordering Comparisons](https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons)
            
        *   [Integers](https://docs.python.org/3/whatsnew/3.0.html#integers)
            
        *   [Text Vs. Data Instead Of Unicode Vs. 8-bit](https://docs.python.org/3/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)
            
    *   [Overview Of Syntax Changes](https://docs.python.org/3/whatsnew/3.0.html#overview-of-syntax-changes)
        *   [New Syntax](https://docs.python.org/3/whatsnew/3.0.html#new-syntax)
            
        *   [Changed Syntax](https://docs.python.org/3/whatsnew/3.0.html#changed-syntax)
            
        *   [Removed Syntax](https://docs.python.org/3/whatsnew/3.0.html#removed-syntax)
            
    *   [Changes Already Present In Python 2.6](https://docs.python.org/3/whatsnew/3.0.html#changes-already-present-in-python-2-6)
        
    *   [Library Changes](https://docs.python.org/3/whatsnew/3.0.html#library-changes)
        
    *   [**PEP 3101**: A New Approach To String Formatting](https://docs.python.org/3/whatsnew/3.0.html#pep-3101-a-new-approach-to-string-formatting)
        
    *   [Changes To Exceptions](https://docs.python.org/3/whatsnew/3.0.html#changes-to-exceptions)
        
    *   [Miscellaneous Other Changes](https://docs.python.org/3/whatsnew/3.0.html#miscellaneous-other-changes)
        *   [Operators And Special Methods](https://docs.python.org/3/whatsnew/3.0.html#operators-and-special-methods)
            
        *   [Builtins](https://docs.python.org/3/whatsnew/3.0.html#builtins)
            
    *   [Build and C API Changes](https://docs.python.org/3/whatsnew/3.0.html#build-and-c-api-changes)
        
    *   [Performance](https://docs.python.org/3/whatsnew/3.0.html#performance)
        
    *   [Porting To Python 3.0](https://docs.python.org/3/whatsnew/3.0.html#porting-to-python-3-0)
        

#### Previous topic

[What’s New In Python 3.1](https://docs.python.org/3/whatsnew/3.1.html "previous chapter")

#### Next topic

[What’s New in Python 2.7](https://docs.python.org/3/whatsnew/2.7.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+New+In+Python+3.0&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F3.0.html&pagesource=whatsnew%2F3.0.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/3.0.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/2.7.html "What’s New in Python 2.7")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.1.html "What’s New In Python 3.1")
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
*   [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html)
    
*    
    
    |
*   Theme Auto Light Dark |