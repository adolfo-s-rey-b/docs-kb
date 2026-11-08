### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/readline.html "readline — GNU readline interface")
     |
*   [previous](https://docs.python.org/3/library/unicodedata.html "unicodedata — Unicode Database")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`stringprep` — Internet String Preparation[¶](https://docs.python.org/3/library/stringprep.html#module-stringprep "Link to this heading")

==========================================================================================================================================

**Source code:** [Lib/stringprep.py](https://github.com/python/cpython/tree/3.15/Lib/stringprep.py)

* * *

When identifying things (such as host names) in the internet, it is often necessary to compare such identifications for “equality”. Exactly how this comparison is executed may depend on the application domain, e.g. whether it should be case-insensitive or not. It may be also necessary to restrict the possible identifications, to allow only identifications consisting of “printable” characters.

[**RFC 3454**](https://datatracker.ietf.org/doc/html/rfc3454.html)
 defines a procedure for “preparing” Unicode strings in internet protocols. Before passing strings onto the wire, they are processed with the preparation procedure, after which they have a certain normalized form. The RFC defines a set of tables, which can be combined into profiles. Each profile must define which tables it uses, and what other optional parts of the `stringprep` procedure are part of the profile. One example of a `stringprep` profile is `nameprep`, which is used for internationalized domain names.

The module `stringprep` only exposes the tables from [**RFC 3454**](https://datatracker.ietf.org/doc/html/rfc3454.html)
. As these tables would be very large to represent as dictionaries or lists, the module uses the Unicode character database internally. The module source code itself was generated using the `mkstringprep.py` utility.

As a result, these tables are exposed as functions, not as data structures. There are two kinds of tables in the RFC: sets and mappings. For a set, `stringprep` provides the “characteristic function”, i.e. a function that returns `True` if the parameter is part of the set. For mappings, it provides the mapping function: given the key, it returns the associated value. Below is a list of all functions available in the module.

stringprep.in\_table\_a1(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_a1 "Link to this definition")

Determine whether _code_ is in tableA.1 (Unassigned code points in Unicode 3.2).

stringprep.in\_table\_b1(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_b1 "Link to this definition")

Determine whether _code_ is in tableB.1 (Commonly mapped to nothing).

stringprep.map\_table\_b2(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.map_table_b2 "Link to this definition")

Return the mapped value for _code_ according to tableB.2 (Mapping for case-folding used with NFKC).

stringprep.map\_table\_b3(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.map_table_b3 "Link to this definition")

Return the mapped value for _code_ according to tableB.3 (Mapping for case-folding used with no normalization).

stringprep.in\_table\_c11(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c11 "Link to this definition")

Determine whether _code_ is in tableC.1.1 (ASCII space characters).

stringprep.in\_table\_c12(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c12 "Link to this definition")

Determine whether _code_ is in tableC.1.2 (Non-ASCII space characters).

stringprep.in\_table\_c11\_c12(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c11_c12 "Link to this definition")

Determine whether _code_ is in tableC.1 (Space characters, union of C.1.1 and C.1.2).

stringprep.in\_table\_c21(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c21 "Link to this definition")

Determine whether _code_ is in tableC.2.1 (ASCII control characters).

stringprep.in\_table\_c22(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c22 "Link to this definition")

Determine whether _code_ is in tableC.2.2 (Non-ASCII control characters).

stringprep.in\_table\_c21\_c22(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c21_c22 "Link to this definition")

Determine whether _code_ is in tableC.2 (Control characters, union of C.2.1 and C.2.2).

stringprep.in\_table\_c3(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c3 "Link to this definition")

Determine whether _code_ is in tableC.3 (Private use).

stringprep.in\_table\_c4(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c4 "Link to this definition")

Determine whether _code_ is in tableC.4 (Non-character code points).

stringprep.in\_table\_c5(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c5 "Link to this definition")

Determine whether _code_ is in tableC.5 (Surrogate codes).

stringprep.in\_table\_c6(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c6 "Link to this definition")

Determine whether _code_ is in tableC.6 (Inappropriate for plain text).

stringprep.in\_table\_c7(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c7 "Link to this definition")

Determine whether _code_ is in tableC.7 (Inappropriate for canonical representation).

stringprep.in\_table\_c8(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c8 "Link to this definition")

Determine whether _code_ is in tableC.8 (Change display properties or are deprecated).

stringprep.in\_table\_c9(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_c9 "Link to this definition")

Determine whether _code_ is in tableC.9 (Tagging characters).

stringprep.in\_table\_d1(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_d1 "Link to this definition")

Determine whether _code_ is in tableD.1 (Characters with bidirectional property “R” or “AL”).

stringprep.in\_table\_d2(_code_)[¶](https://docs.python.org/3/library/stringprep.html#stringprep.in_table_d2 "Link to this definition")

Determine whether _code_ is in tableD.2 (Characters with bidirectional property “L”).

#### Previous topic

[`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html "previous chapter")

#### Next topic

[`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=stringprep+%E2%80%94+Internet+String+Preparation&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstringprep.html&pagesource=library%2Fstringprep.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/stringprep.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/readline.html "readline — GNU readline interface")
     |
*   [previous](https://docs.python.org/3/library/unicodedata.html "unicodedata — Unicode Database")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
    
*    
    
    |
*   Theme Auto Light Dark |