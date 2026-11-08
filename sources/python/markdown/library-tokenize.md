### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tabnanny.html "tabnanny — Detection of ambiguous indentation")
     |
*   [previous](https://docs.python.org/3/library/keyword.html "keyword — Testing for Python keywords")
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
*   [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tokenize` — Tokenizer for Python source[¶](https://docs.python.org/3/library/tokenize.html#module-tokenize "Link to this heading")

====================================================================================================================================

**Source code:** [Lib/tokenize.py](https://github.com/python/cpython/tree/3.15/Lib/tokenize.py)

* * *

The `tokenize` module provides a lexical scanner for Python source code, implemented in Python. The scanner in this module returns comments as tokens as well, making it useful for implementing “pretty-printers”, including colorizers for on-screen displays.

To simplify token stream handling, all [operator](https://docs.python.org/3/reference/lexical_analysis.html#operators)
 and [delimiter](https://docs.python.org/3/reference/lexical_analysis.html#delimiters)
 tokens and [`Ellipsis`](https://docs.python.org/3/builtins/constants.html#Ellipsis "Ellipsis")
 are returned using the generic [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP")
 token type. The [`TokenInfo.exact_type`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.exact_type "tokenize.TokenInfo.exact_type")
 property gives the exact token type.

Warning

Note that the functions in this module are only designed to parse syntactically valid Python code (code that does not raise when parsed using [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse")
). The behavior of the functions in this module is **undefined** when providing invalid Python code and it can change at any point.

Tokenizing input[¶](https://docs.python.org/3/library/tokenize.html#tokenizing-input "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The primary entry point is a [generator](https://docs.python.org/3/glossary.html#term-generator)
:

tokenize.tokenize(_readline_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "Link to this definition")

The `tokenize()` generator requires one argument, _readline_, which must be a callable object which provides the same interface as the [`io.IOBase.readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")
 method of file objects. Each call to the function should return one line of input as bytes.

The generator produces [`TokenInfo`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo "tokenize.TokenInfo")
 objects.

Changed in version 3.1: Changed to yield [`TokenInfo`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo "tokenize.TokenInfo")
 objects instead of plain tuples.

`tokenize()` determines the source encoding of the file by looking for a UTF-8 BOM or encoding cookie, according to [**PEP 263**](https://peps.python.org/pep-0263/)
.

tokenize.generate\_tokens(_readline_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.generate_tokens "Link to this definition")

Tokenize a source reading unicode strings instead of bytes.

Like [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")
, the _readline_ argument is a callable returning a single line of input. However, `generate_tokens()` expects _readline_ to return a str object rather than bytes.

The result is an iterator yielding [`TokenInfo`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo "tokenize.TokenInfo")
 objects, exactly like [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")
. It does not yield an [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING")
 token.

class tokenize.TokenInfo(_type_, _string_, _start_, _end_, _line_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 describing a token. It has five fields and an additional [`exact_type`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.exact_type "tokenize.TokenInfo.exact_type")
 property.

Added in version 3.1.

type[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.type "Link to this definition")

An integer identifying the token type, as defined by the constants in [`token`](https://docs.python.org/3/library/token.html#module-token "token: Constants representing terminal nodes of the parse tree.")
, such as [`NAME`](https://docs.python.org/3/library/token.html#token.NAME "token.NAME")
 and [`STRING`](https://docs.python.org/3/library/token.html#token.STRING "token.STRING")
. Operators and delimiters have type [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP")
; use [`exact_type`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.exact_type "tokenize.TokenInfo.exact_type")
 for their specific token type.

string[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.string "Link to this definition")

The token text as a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
. For [`STRING`](https://docs.python.org/3/library/token.html#token.STRING "token.STRING")
 tokens, this includes the quotes, any prefix, and escape sequences, without evaluating them.

For an [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING")
 token, this is the encoding name. Tokens inserted without corresponding source text can have an empty string. In [`FSTRING_MIDDLE`](https://docs.python.org/3/library/token.html#token.FSTRING_MIDDLE "token.FSTRING_MIDDLE")
 and [`TSTRING_MIDDLE`](https://docs.python.org/3/library/token.html#token.TSTRING_MIDDLE "token.TSTRING_MIDDLE")
 tokens, doubled braces are replaced by single braces.

start[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.start "Link to this definition")

A 2-tuple `(srow, scol)` of ints specifying the inclusive start position of the token in the source. Rows are numbered from 1 and columns from 0. Columns count Unicode code points; a tab counts as one column, without expanding it to a tab stop.

For an [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING")
 token, this is `(0, 0)`.

end[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.end "Link to this definition")

A 2-tuple `(erow, ecol)` of ints specifying the exclusive end position of the token. Rows are numbered from 1 and columns from 0. For a token spanning multiple lines, _erow_ is the final row and _ecol_ is the column on that row.

For example, the name `spam` at the beginning of the first line has [`start`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.start "tokenize.TokenInfo.start")
 equal to `(1, 0)` and [`end`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.end "tokenize.TokenInfo.end")
 equal to `(1, 4)`.

For an [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING")
 token, this is `(0, 0)`. A [`NEWLINE`](https://docs.python.org/3/library/token.html#token.NEWLINE "token.NEWLINE")
 or [`NL`](https://docs.python.org/3/library/token.html#token.NL "token.NL")
 token inserted at the end of input without a final newline can have an end column one beyond the source text.

line[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.line "Link to this definition")

A [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 containing the full source line on which the token was found, including surrounding text and the line terminator if present. For a token spanning multiple lines, this can contain several source lines. It is empty for [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING")
 and [`ENDMARKER`](https://docs.python.org/3/library/token.html#token.ENDMARKER "token.ENDMARKER")
 tokens.

exact\_type[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.exact_type "Link to this definition")

An integer identifying the specific operator type for [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP")
 tokens, as defined by the constants in [`token`](https://docs.python.org/3/library/token.html#module-token "token: Constants representing terminal nodes of the parse tree.")
. For all other token types, this equals [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
. For example, a `+` token has `type` equal to `OP` and [`exact_type`](https://docs.python.org/3/library/tokenize.html#tokenize.TokenInfo.exact_type "tokenize.TokenInfo.exact_type")
 equal to [`PLUS`](https://docs.python.org/3/library/token.html#token.PLUS "token.PLUS")
.

Added in version 3.3.

All constants from the [`token`](https://docs.python.org/3/library/token.html#module-token "token: Constants representing terminal nodes of the parse tree.")
 module are also exported from `tokenize`.

Another function is provided to reverse the tokenization process. This is useful for creating tools that tokenize a script, modify the token stream, and write back the modified script.

tokenize.untokenize(_iterable_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.untokenize "Link to this definition")

Converts tokens back into Python source code. The _iterable_ must return sequences with at least two elements, the token type and the token string. Any additional sequence elements are ignored.

The result is guaranteed to tokenize back to match the input so that the conversion is lossless and round-trips are assured. The guarantee applies only to the token type and token string as the spacing between tokens (column positions) may change.

It returns bytes, encoded using the [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING")
 token, which is the first token sequence output by [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")
. If there is no encoding token in the input, it returns a str instead.

[`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")
 needs to detect the encoding of source files it tokenizes. The function it uses to do this is available:

tokenize.detect\_encoding(_readline_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.detect_encoding "Link to this definition")

The `detect_encoding()` function is used to detect the encoding that should be used to decode a Python source file. It requires one argument, readline, in the same way as the [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")
 generator.

It will call readline a maximum of twice, and return the encoding used (as a string) and a list of any lines (not decoded from bytes) it has read in.

It detects the encoding from the presence of a UTF-8 BOM or an encoding cookie as specified in [**PEP 263**](https://peps.python.org/pep-0263/)
. If both a BOM and a cookie are present, but disagree, a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 will be raised. Note that if the BOM is found, `'utf-8-sig'` will be returned as an encoding.

If no encoding is specified, then the default of `'utf-8'` will be returned.

Use [`open()`](https://docs.python.org/3/library/tokenize.html#tokenize.open "tokenize.open")
 to open Python source files: it uses `detect_encoding()` to detect the file encoding.

tokenize.open(_filename_)[¶](https://docs.python.org/3/library/tokenize.html#tokenize.open "Link to this definition")

Open a file in read only mode using the encoding detected by [`detect_encoding()`](https://docs.python.org/3/library/tokenize.html#tokenize.detect_encoding "tokenize.detect_encoding")
.

Added in version 3.2.

exception tokenize.TokenError[¶](https://docs.python.org/3/library/tokenize.html#tokenize.TokenError "Link to this definition")

Raised when either a docstring or expression that may be split over several lines is not completed anywhere in the file, for example:

Copy

"""Beginning of
docstring

or:

Copy

\[1,\
 2,\
 3\
\
Command-line usage[¶](https://docs.python.org/3/library/tokenize.html#command-line-usage "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------\
\
Added in version 3.3.\
\
The `tokenize` module can be executed as a script from the command line. It is as simple as:\
\
Copy\
\
python \-m tokenize \[\-e\] \[filename.py\]\
\
The following options are accepted:\
\
\-h, \--help[¶](https://docs.python.org/3/library/tokenize.html#cmdoption-tokenize-h "Link to this definition")\
\
show this help message and exit\
\
\-e, \--exact[¶](https://docs.python.org/3/library/tokenize.html#cmdoption-tokenize-e "Link to this definition")\
\
display token names using the exact type\
\
If `filename.py` is specified its contents are tokenized to stdout. Otherwise, tokenization is performed on stdin.\
\
Added in version 3.15: Output is in color by default and can be [controlled using environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)\
.\
\
Examples[¶](https://docs.python.org/3/library/tokenize.html#examples "Link to this heading")\
\
---------------------------------------------------------------------------------------------\
\
Example of a script rewriter that transforms float literals into Decimal objects:\
\
Copy\
\
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP\
from io import BytesIO\
\
def decistmt(s):\
    """Substitute Decimals for floats in a string of statements.\
\
    >>> from decimal import Decimal\
    >>> s = 'print(+21.3e-5\*-.1234/81.7)'\
    >>> decistmt(s)\
    "print (+Decimal ('21.3e-5')\*-Decimal ('.1234')/Decimal ('81.7'))"\
\
    The format of the exponent is inherited from the platform C library.\
    Known cases are "e-007" (Windows) and "e-07" (not Windows).  Since\
    we're only showing 12 digits, and the 13th isn't close to 5, the\
    rest of the output should be platform-independent.\
\
    >>> exec(s)  #doctest: +ELLIPSIS\
    -3.21716034272e-0...7\
\
    Output from calculations with Decimal should be identical across all\
    platforms.\
\
    >>> exec(decistmt(s))\
    -3.217160342717258261933904529E-7\
    """\
    result \= \[\]\
    g \= tokenize(BytesIO(s.encode('utf-8')).readline)  \# tokenize the string\
    for toknum, tokval, \_, \_, \_ in g:\
        if toknum \== NUMBER and '.' in tokval:  \# replace NUMBER tokens\
            result.extend(\[\
                (NAME, 'Decimal'),\
                (OP, '('),\
                (STRING, repr(tokval)),\
                (OP, ')')\
            \])\
        else:\
            result.append((toknum, tokval))\
    return untokenize(result).decode('utf-8')\
\
Example of tokenizing from the command line. The script:\
\
Copy\
\
def say\_hello():\
    print("Hello, World!")\
\
say\_hello()\
\
will be tokenized to the following output where the first column is the range of the line/column coordinates where the token is found, the second column is the name of the token, and the final column is the value of the token (if any):\
\
Copy\
\
$ python \-m tokenize hello.py\
0,0-0,0:            ENCODING       'utf-8'\
1,0-1,3:            NAME           'def'\
1,4-1,13:           NAME           'say\_hello'\
1,13-1,14:          OP             '('\
1,14-1,15:          OP             ')'\
1,15-1,16:          OP             ':'\
1,16-1,17:          NEWLINE        '\\n'\
2,0-2,4:            INDENT         '    '\
2,4-2,9:            NAME           'print'\
2,9-2,10:           OP             '('\
2,10-2,25:          STRING         '"Hello, World!"'\
2,25-2,26:          OP             ')'\
2,26-2,27:          NEWLINE        '\\n'\
3,0-3,1:            NL             '\\n'\
4,0-4,0:            DEDENT         ''\
4,0-4,9:            NAME           'say\_hello'\
4,9-4,10:           OP             '('\
4,10-4,11:          OP             ')'\
4,11-4,12:          NEWLINE        '\\n'\
5,0-5,0:            ENDMARKER      ''\
\
The exact token type names can be displayed using the [`-e`](https://docs.python.org/3/library/tokenize.html#cmdoption-tokenize-e)\
 option:\
\
Copy\
\
$ python \-m tokenize \-e hello.py\
0,0-0,0:            ENCODING       'utf-8'\
1,0-1,3:            NAME           'def'\
1,4-1,13:           NAME           'say\_hello'\
1,13-1,14:          LPAR           '('\
1,14-1,15:          RPAR           ')'\
1,15-1,16:          COLON          ':'\
1,16-1,17:          NEWLINE        '\\n'\
2,0-2,4:            INDENT         '    '\
2,4-2,9:            NAME           'print'\
2,9-2,10:           LPAR           '('\
2,10-2,25:          STRING         '"Hello, World!"'\
2,25-2,26:          RPAR           ')'\
2,26-2,27:          NEWLINE        '\\n'\
3,0-3,1:            NL             '\\n'\
4,0-4,0:            DEDENT         ''\
4,0-4,9:            NAME           'say\_hello'\
4,9-4,10:           LPAR           '('\
4,10-4,11:          RPAR           ')'\
4,11-4,12:          NEWLINE        '\\n'\
5,0-5,0:            ENDMARKER      ''\
\
Example of tokenizing a file programmatically, reading unicode strings instead of bytes with [`generate_tokens()`](https://docs.python.org/3/library/tokenize.html#tokenize.generate_tokens "tokenize.generate_tokens")\
:\
\
Copy\
\
import tokenize\
\
with tokenize.open('hello.py') as f:\
    tokens \= tokenize.generate\_tokens(f.readline)\
    for token in tokens:\
        print(token)\
\
Or reading bytes directly with [`tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize")\
:\
\
Copy\
\
import tokenize\
\
with open('hello.py', 'rb') as f:\
    tokens \= tokenize.tokenize(f.readline)\
    for token in tokens:\
        print(token)\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html#)\
    *   [Tokenizing input](https://docs.python.org/3/library/tokenize.html#tokenizing-input)\
        \
    *   [Command-line usage](https://docs.python.org/3/library/tokenize.html#command-line-usage)\
        \
    *   [Examples](https://docs.python.org/3/library/tokenize.html#examples)\
        \
\
#### Previous topic\
\
[`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html "previous chapter")\
\
#### Next topic\
\
[`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/3/library/tabnanny.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tokenize+%E2%80%94+Tokenizer+for+Python+source&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftokenize.html&pagesource=library%2Ftokenize.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tokenize.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/library/tabnanny.html "tabnanny — Detection of ambiguous indentation")\
     |\
*   [previous](https://docs.python.org/3/library/keyword.html "keyword — Testing for Python keywords")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python standard library](https://docs.python.org/3/library/index.html)\
     »\
*   [Python Language Services](https://docs.python.org/3/library/language.html)\
     »\
*   [`tokenize` — Tokenizer for Python source](https://docs.python.org/3/library/tokenize.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |