### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/lexical_analysis.html "2. Lexical analysis")
     |
*   [previous](https://docs.python.org/3/reference/index.html "The Python Language Reference")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python Language Reference](https://docs.python.org/3/reference/index.html)
     »
*   [1\. Introduction](https://docs.python.org/3/reference/introduction.html)
    
*    
    
    |
*   Theme Auto Light Dark |

1\. Introduction[¶](https://docs.python.org/3/reference/introduction.html#introduction "Link to this heading")

===============================================================================================================

This reference manual describes the Python programming language. It is not intended as a tutorial.

While I am trying to be as precise as possible, I chose to use English rather than formal specifications for everything except syntax and lexical analysis. This should make the document more understandable to the average reader, but will leave room for ambiguities. Consequently, if you were coming from Mars and tried to re-implement Python from this document alone, you might have to guess things and in fact you would probably end up implementing quite a different language. On the other hand, if you are using Python and wonder what the precise rules about a particular area of the language are, you should definitely be able to find them here. If you would like to see a more formal definition of the language, maybe you could volunteer your time — or invent a cloning machine :-).

It is dangerous to add too many implementation details to a language reference document — the implementation may change, and other implementations of the same language may work differently. On the other hand, CPython is the one Python implementation in widespread use (although alternate implementations continue to gain support), and its particular quirks are sometimes worth being mentioned, especially where the implementation imposes additional limitations. Therefore, you’ll find short “implementation notes” sprinkled throughout the text.

Every Python implementation comes with a number of built-in and standard modules. These are documented in [The Python standard library](https://docs.python.org/3/library/index.html#library-index)
. A few built-in modules are mentioned when they interact in a significant way with the language definition.

1.1. Alternate Implementations[¶](https://docs.python.org/3/reference/introduction.html#alternate-implementations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Though there is one Python implementation which is by far the most popular, there are some alternate implementations which are of particular interest to different audiences.

Known implementations include:

CPython

This is the original and most-maintained implementation of Python, written in C. New language features generally appear here first.

Jython

Python implemented in Java. This implementation can be used as a scripting language for Java applications, or can be used to create applications using the Java class libraries. It is also often used to create tests for Java libraries. More information can be found at [the Jython website](https://www.jython.org/)
.

Python for .NET

This implementation actually uses the CPython implementation, but is a managed .NET application and makes .NET libraries available. It was created by Brian Lloyd. For more information, see the [Python for .NET home page](https://pythonnet.github.io/)
.

IronPython

An alternate Python for .NET. Unlike Python.NET, this is a complete Python implementation that generates IL, and compiles Python code directly to .NET assemblies. It was created by Jim Hugunin, the original creator of Jython. For more information, see [the IronPython website](https://ironpython.net/)
.

PyPy

An implementation of Python written completely in Python. It supports several advanced features not found in other implementations like stackless support and a Just in Time compiler. One of the goals of the project is to encourage experimentation with the language itself by making it easier to modify the interpreter (since it is written in Python). Additional information is available on [the PyPy project’s home page](https://pypy.org/)
.

Each of these implementations varies in some way from the language as documented in this manual, or introduces specific information beyond what’s covered in the standard Python documentation. Please refer to the implementation-specific documentation to determine what else you need to know about the specific implementation you’re using.

1.2. Notation[¶](https://docs.python.org/3/reference/introduction.html#notation "Link to this heading")

--------------------------------------------------------------------------------------------------------

The descriptions of lexical analysis and syntax use a grammar notation that is a mixture of [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)
 and [PEG](https://en.wikipedia.org/wiki/Parsing_expression_grammar)
. For example:

**name**:   [`letter`](https://docs.python.org/3/reference/introduction.html#grammar-token-notation-letter)
 ([`letter`](https://docs.python.org/3/reference/introduction.html#grammar-token-notation-letter)
 | [`digit`](https://docs.python.org/3/reference/introduction.html#grammar-token-notation-digit)
 | "\_")\*
**letter**: "a"..."z" | "A"..."Z"
**digit**:  "0"..."9"

In this example, the first line says that a `name` is a `letter` followed by a sequence of zero or more `letter`s, `digit`s, and underscores. A `letter` in turn is any of the single characters `'a'` through `'z'` and `A` through `Z`; a `digit` is a single character from `0` to `9`.

Each rule begins with a name (which identifies the rule that’s being defined) followed by a colon, `:`. The definition to the right of the colon uses the following syntax elements:

*   `name`: A name refers to another rule. Where possible, it is a link to the rule’s definition.
    
    *   `TOKEN`: An uppercase name refers to a [token](https://docs.python.org/3/glossary.html#term-token)
        . For the purposes of grammar definitions, tokens are the same as rules.
        
*   `"text"`, `'text'`: Text in single or double quotes must match literally (without the quotes). The type of quote is chosen according to the meaning of `text`:
    
    *   `'if'`: A name in single quotes denotes a [keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
        .
        
    *   `"case"`: A name in double quotes denotes a [soft-keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords)
        .
        
    *   `'@'`: A non-letter symbol in single quotes denotes an [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP")
         token, that is, a [delimiter](https://docs.python.org/3/reference/lexical_analysis.html#delimiters)
         or [operator](https://docs.python.org/3/reference/lexical_analysis.html#operators)
        .
        
*   `e1 e2`: Items separated only by whitespace denote a sequence. Here, `e1` must be followed by `e2`.
    
*   `e1 | e2`: A vertical bar is used to separate alternatives. It denotes PEG’s “ordered choice”: if `e1` matches, `e2` is not considered. In traditional PEG grammars, this is written as a slash, `/`, rather than a vertical bar. See [**PEP 617**](https://peps.python.org/pep-0617/)
     for more background and details.
    
*   `e*`: A star means zero or more repetitions of the preceding item.
    
*   `e+`: Likewise, a plus means one or more repetitions.
    
*   `[e]`: A phrase enclosed in square brackets means zero or one occurrences. In other words, the enclosed phrase is optional.
    
*   `e?`: A question mark has exactly the same meaning as square brackets: the preceding item is optional.
    
*   `(e)`: Parentheses are used for grouping.
    

The following notation is only used in [lexical definitions](https://docs.python.org/3/reference/introduction.html#notation-lexical-vs-syntactic)
.

*   `"a"..."z"`: Two literal characters separated by three dots mean a choice of any single character in the given (inclusive) range of ASCII characters.
    
*   `<...>`: A phrase between angular brackets gives an informal description of the matched symbol (for example, `<any ASCII character except "\">`), or an abbreviation that is defined in nearby text (for example, `<Lu>`).
    

Some definitions also use _lookaheads_, which indicate that an element must (or must not) match at a given position, but without consuming any input:

*   `&e`: a positive lookahead (that is, `e` is required to match)
    
*   `!e`: a negative lookahead (that is, `e` is required _not_ to match)
    

The unary operators (`*`, `+`, `?`) bind as tightly as possible; the vertical bar (`|`) binds most loosely.

White space is only meaningful to separate tokens.

Rules are normally contained on a single line, but rules that are too long may be wrapped:

**literal**: stringliteral | bytesliteral
         | integer | floatnumber | imagnumber

Alternatively, rules may be formatted with the first line ending at the colon, and each alternative beginning with a vertical bar on a new line. For example:

**literal**:
   | stringliteral
   | bytesliteral
   | integer
   | floatnumber
   | imagnumber

This does _not_ mean that there is an empty first alternative.

### 1.2.1. Lexical and Syntactic definitions[¶](https://docs.python.org/3/reference/introduction.html#lexical-and-syntactic-definitions "Link to this heading")

There is some difference between _lexical_ and _syntactic_ analysis: the [lexical analyzer](https://docs.python.org/3/glossary.html#term-lexical-analyzer)
 operates on the individual characters of the input source, while the _parser_ (syntactic analyzer) operates on the stream of [tokens](https://docs.python.org/3/glossary.html#term-token)
 generated by the lexical analysis. However, in some cases the exact boundary between the two phases is a CPython implementation detail.

The practical difference between the two is that in _lexical_ definitions, all whitespace is significant. The lexical analyzer [discards](https://docs.python.org/3/reference/lexical_analysis.html#whitespace)
 all whitespace that is not converted to tokens like [`token.INDENT`](https://docs.python.org/3/library/token.html#token.INDENT "token.INDENT")
 or [`NEWLINE`](https://docs.python.org/3/library/token.html#token.NEWLINE "token.NEWLINE")
. _Syntactic_ definitions then use these tokens, rather than source characters.

This documentation uses the same BNF grammar for both styles of definitions. All uses of BNF in the next chapter ([Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html#lexical)
) are lexical definitions; uses in subsequent chapters are syntactic definitions.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [1\. Introduction](https://docs.python.org/3/reference/introduction.html#)
    *   [1.1. Alternate Implementations](https://docs.python.org/3/reference/introduction.html#alternate-implementations)
        
    *   [1.2. Notation](https://docs.python.org/3/reference/introduction.html#notation)
        *   [1.2.1. Lexical and Syntactic definitions](https://docs.python.org/3/reference/introduction.html#lexical-and-syntactic-definitions)
            

#### Previous topic

[The Python Language Reference](https://docs.python.org/3/reference/index.html "previous chapter")

#### Next topic

[2\. Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=1.+Introduction&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fintroduction.html&pagesource=reference%2Fintroduction.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/reference/introduction.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/reference/lexical_analysis.html "2. Lexical analysis")
     |
*   [previous](https://docs.python.org/3/reference/index.html "The Python Language Reference")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python Language Reference](https://docs.python.org/3/reference/index.html)
     »
*   [1\. Introduction](https://docs.python.org/3/reference/introduction.html)
    
*    
    
    |
*   Theme Auto Light Dark |