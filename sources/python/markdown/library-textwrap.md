### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/unicodedata.html "unicodedata — Unicode Database")
     |
*   [previous](https://docs.python.org/3/library/difflib.html "difflib — Helpers for computing deltas")
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
*   [`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`textwrap` — Text wrapping and filling[¶](https://docs.python.org/3/library/textwrap.html#module-textwrap "Link to this heading")

==================================================================================================================================

**Source code:** [Lib/textwrap.py](https://github.com/python/cpython/tree/3.15/Lib/textwrap.py)

* * *

The `textwrap` module provides some convenience functions, as well as [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper")
, the class that does all the work. If you’re just wrapping or filling one or two text strings, the convenience functions should be good enough; otherwise, you should use an instance of `TextWrapper` for efficiency.

textwrap.wrap(_text_, _width\=70_, _\*_, _initial\_indent\=''_, _subsequent\_indent\=''_, _expand\_tabs\=True_, _replace\_whitespace\=True_, _fix\_sentence\_endings\=False_, _break\_long\_words\=True_, _drop\_whitespace\=True_, _break\_on\_hyphens\=True_, _tabsize\=8_, _max\_lines\=None_, _placeholder\=' \[...\]'_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "Link to this definition")

Wraps the single paragraph in _text_ (a string) so every line is at most _width_ characters long. Returns a list of output lines, without final newlines.

Optional keyword arguments correspond to the instance attributes of [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper")
, documented below.

See the [`TextWrapper.wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.wrap "textwrap.TextWrapper.wrap")
 method for additional details on how `wrap()` behaves.

textwrap.fill(_text_, _width\=70_, _\*_, _initial\_indent\=''_, _subsequent\_indent\=''_, _expand\_tabs\=True_, _replace\_whitespace\=True_, _fix\_sentence\_endings\=False_, _break\_long\_words\=True_, _drop\_whitespace\=True_, _break\_on\_hyphens\=True_, _tabsize\=8_, _max\_lines\=None_, _placeholder\=' \[...\]'_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.fill "Link to this definition")

Wraps the single paragraph in _text_, and returns a single string containing the wrapped paragraph. `fill()` is shorthand for

Copy

"\\n".join(wrap(text, ...))

In particular, `fill()` accepts exactly the same keyword arguments as [`wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "textwrap.wrap")
.

textwrap.shorten(_text_, _width_, _\*_, _fix\_sentence\_endings\=False_, _break\_long\_words\=True_, _break\_on\_hyphens\=True_, _placeholder\=' \[...\]'_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.shorten "Link to this definition")

Collapse and truncate the given _text_ to fit in the given _width_.

First the whitespace in _text_ is collapsed (all whitespace is replaced by single spaces). If the result fits in the _width_, it is returned. Otherwise, enough words are dropped from the end so that the remaining words plus the _placeholder_ fit within _width_:

Copy

\>>> textwrap.shorten("Hello  world!", width\=12)
'Hello world!'
\>>> textwrap.shorten("Hello  world!", width\=11)
'Hello \[...\]'
\>>> textwrap.shorten("Hello world", width\=10, placeholder\="...")
'Hello...'

Optional keyword arguments correspond to the instance attributes of [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper")
, documented below. Note that the whitespace is collapsed before the text is passed to the `TextWrapper` [`fill()`](https://docs.python.org/3/library/textwrap.html#textwrap.fill "textwrap.fill")
 function, so changing the value of [`tabsize`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.tabsize "textwrap.TextWrapper.tabsize")
, [`expand_tabs`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.expand_tabs "textwrap.TextWrapper.expand_tabs")
, [`drop_whitespace`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.drop_whitespace "textwrap.TextWrapper.drop_whitespace")
, and [`replace_whitespace`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.replace_whitespace "textwrap.TextWrapper.replace_whitespace")
 will have no effect.

Added in version 3.4.

textwrap.dedent(_text_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.dedent "Link to this definition")

Remove any common leading whitespace from every line in _text_.

This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.

Note that tabs and spaces are both treated as whitespace, but they are not equal: the lines `"  hello"` and `"\thello"` are considered to have no common leading whitespace.

Lines containing only whitespace are ignored in the input and normalized to a single newline character in the output.

For example:

Copy

def test():
    \# end first line with \\ to avoid the empty line!
    s \= '''\\
    hello
      world
    '''
    print(repr(s))          \# prints '    hello\\n      world\\n    '
    print(repr(dedent(s)))  \# prints 'hello\\n  world\\n'

Changed in version 3.14: The `dedent()` function now correctly normalizes blank lines containing only whitespace characters. Previously, the implementation only normalized blank lines containing tabs and spaces.

textwrap.indent(_text_, _prefix_, _predicate\=None_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.indent "Link to this definition")

Add _prefix_ to the beginning of selected lines in _text_.

Lines are separated by calling `text.splitlines(True)`.

By default, _prefix_ is added to all lines that do not consist solely of whitespace (including any line endings).

For example:

Copy

\>>> s \= 'hello\\n\\n \\nworld'
\>>> indent(s, '  ')
'  hello\\n\\n \\n  world'

The optional _predicate_ argument can be used to control which lines are indented. For example, it is easy to add _prefix_ to even empty and whitespace-only lines:

Copy

\>>> print(indent(s, '+ ', lambda line: True))
\+ hello
+
+
\+ world

Added in version 3.3.

[`wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "textwrap.wrap")
, [`fill()`](https://docs.python.org/3/library/textwrap.html#textwrap.fill "textwrap.fill")
 and [`shorten()`](https://docs.python.org/3/library/textwrap.html#textwrap.shorten "textwrap.shorten")
 work by creating a [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper")
 instance and calling a single method on it. That instance is not reused, so for applications that process many text strings using `wrap()` and/or `fill()`, it may be more efficient to create your own `TextWrapper` object.

Text is preferably wrapped on whitespaces and right after the hyphens in hyphenated words; only then will long words be broken if necessary, unless [`TextWrapper.break_long_words`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.break_long_words "textwrap.TextWrapper.break_long_words")
 is set to false.

class textwrap.TextWrapper(_\*\*kwargs_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "Link to this definition")

The `TextWrapper` constructor accepts a number of optional keyword arguments. Each keyword argument corresponds to an instance attribute, so for example

Copy

wrapper \= TextWrapper(initial\_indent\="\* ")

is the same as

Copy

wrapper \= TextWrapper()
wrapper.initial\_indent \= "\* "

You can reuse the same `TextWrapper` object many times, and you can change any of its options through direct assignment to instance attributes between uses.

The `TextWrapper` instance attributes (and keyword arguments to the constructor) are as follows:

width[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.width "Link to this definition")

(default: `70`) The maximum length of wrapped lines. As long as there are no individual words in the input text longer than [`width`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.width "textwrap.TextWrapper.width")
, `TextWrapper` guarantees that no output line will be longer than `width` characters.

expand\_tabs[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.expand_tabs "Link to this definition")

(default: `True`) If true, then all tab characters in _text_ will be expanded to spaces using the [`expandtabs()`](https://docs.python.org/3/builtins/stdtypes.html#str.expandtabs "str.expandtabs")
 method of _text_.

tabsize[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.tabsize "Link to this definition")

(default: `8`) If [`expand_tabs`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.expand_tabs "textwrap.TextWrapper.expand_tabs")
 is true, then all tab characters in _text_ will be expanded to zero or more spaces, depending on the current column and the given tab size.

Added in version 3.3.

replace\_whitespace[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.replace_whitespace "Link to this definition")

(default: `True`) If true, after tab expansion but before wrapping, the [`wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "textwrap.wrap")
 method will replace each whitespace character with a single space. The whitespace characters replaced are as follows: tab, newline, vertical tab, formfeed, and carriage return (`'\t\n\v\f\r'`).

Note

If [`expand_tabs`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.expand_tabs "textwrap.TextWrapper.expand_tabs")
 is false and [`replace_whitespace`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.replace_whitespace "textwrap.TextWrapper.replace_whitespace")
 is true, each tab character will be replaced by a single space, which is _not_ the same as tab expansion.

Note

If [`replace_whitespace`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.replace_whitespace "textwrap.TextWrapper.replace_whitespace")
 is false, newlines may appear in the middle of a line and cause strange output. For this reason, text should be split into paragraphs (using [`str.splitlines()`](https://docs.python.org/3/builtins/stdtypes.html#str.splitlines "str.splitlines")
 or similar) which are wrapped separately.

drop\_whitespace[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.drop_whitespace "Link to this definition")

(default: `True`) If true, whitespace at the beginning and ending of every line (after wrapping but before indenting) is dropped. Whitespace at the beginning of the paragraph, however, is not dropped if non-whitespace follows it. If whitespace being dropped takes up an entire line, the whole line is dropped.

initial\_indent[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.initial_indent "Link to this definition")

(default: `''`) String that will be prepended to the first line of wrapped output. Counts towards the length of the first line. The empty string is not indented.

subsequent\_indent[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.subsequent_indent "Link to this definition")

(default: `''`) String that will be prepended to all lines of wrapped output except the first. Counts towards the length of each line except the first.

fix\_sentence\_endings[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.fix_sentence_endings "Link to this definition")

(default: `False`) If true, `TextWrapper` attempts to detect sentence endings and ensure that sentences are always separated by exactly two spaces. This is generally desired for text in a monospaced font. However, the sentence detection algorithm is imperfect: it assumes that a sentence ending consists of a lowercase letter followed by one of `'.'`, `'!'`, or `'?'`, possibly followed by one of `'"'` or `"'"`, followed by a space. One problem with this algorithm is that it is unable to detect the difference between “Dr.” in

Copy

\[...\] Dr. Frankenstein's monster \[...\]

and “Spot.” in

Copy

\[...\] See Spot. See Spot run \[...\]

[`fix_sentence_endings`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.fix_sentence_endings "textwrap.TextWrapper.fix_sentence_endings")
 is false by default.

Since the sentence detection algorithm defines “lowercase letter” using the characters in `string.ascii_lowercase`, and relies on a convention of using two spaces after a period to separate sentences on the same line, it is specific to English-language texts.

break\_long\_words[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.break_long_words "Link to this definition")

(default: `True`) If true, then words longer than [`width`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.width "textwrap.TextWrapper.width")
 will be broken in order to ensure that no lines are longer than `width`. If it is false, long words will not be broken, and some lines may be longer than `width`. (Long words will be put on a line by themselves, in order to minimize the amount by which `width` is exceeded.)

break\_on\_hyphens[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.break_on_hyphens "Link to this definition")

(default: `True`) If true, wrapping will occur preferably on whitespaces and right after hyphens in compound words, as it is customary in English. If false, only whitespaces will be considered as potentially good places for line breaks, but you need to set [`break_long_words`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.break_long_words "textwrap.TextWrapper.break_long_words")
 to false if you want truly insecable words. Default behaviour in previous versions was to always allow breaking hyphenated words.

max\_lines[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.max_lines "Link to this definition")

(default: `None`) If not `None`, then the output will contain at most _max\_lines_ lines, with _placeholder_ appearing at the end of the output.

Added in version 3.4.

placeholder[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.placeholder "Link to this definition")

(default: `' [...]'`) String that will appear at the end of the output text if it has been truncated.

Added in version 3.4.

`TextWrapper` also provides some public methods, analogous to the module-level convenience functions:

wrap(_text_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.wrap "Link to this definition")

Wraps the single paragraph in _text_ (a string) so every line is at most [`width`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.width "textwrap.TextWrapper.width")
 characters long. All wrapping options are taken from instance attributes of the `TextWrapper` instance. Returns a list of output lines, without final newlines. If the wrapped output has no content, the returned list is empty.

fill(_text_)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.fill "Link to this definition")

Wraps the single paragraph in _text_, and returns a single string containing the wrapped paragraph.

#### Previous topic

[`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html "previous chapter")

#### Next topic

[`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=textwrap+%E2%80%94+Text+wrapping+and+filling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftextwrap.html&pagesource=library%2Ftextwrap.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/textwrap.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/unicodedata.html "unicodedata — Unicode Database")
     |
*   [previous](https://docs.python.org/3/library/difflib.html "difflib — Helpers for computing deltas")
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
*   [`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html)
    
*    
    
    |
*   Theme Auto Light Dark |