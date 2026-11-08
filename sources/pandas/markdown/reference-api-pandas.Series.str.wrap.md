[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.wrap.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.wrap[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.wrap.html#pandas-series-str-wrap "Link to this heading")

==================================================================================================================================================

Series.str.wrap(_width_, _expand\_tabs\=True_, _tabsize\=8_, _replace\_whitespace\=True_, _drop\_whitespace\=True_, _initial\_indent\=''_, _subsequent\_indent\=''_, _fix\_sentence\_endings\=False_, _break\_long\_words\=True_, _break\_on\_hyphens\=True_, _max\_lines\=None_, _placeholder\=' \[...\]'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2883-L3006)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.wrap.html#pandas.Series.str.wrap "Link to this definition")

Wrap strings in Series/Index at specified line width.

This method has the same keyword parameters and defaults as

[`textwrap.TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "(in Python v3.15)")
.

Parameters:

**width**int, optional

Maximum line width.

**expand\_tabs**bool, optional

If True, tab characters will be expanded to spaces (default: True).

**tabsize**int, optional

If expand\_tabs is true, then all tab characters in text will be expanded to zero or more spaces, depending on the current column and the given tab size (default: 8).

**replace\_whitespace**bool, optional

If True, each whitespace character (as defined by string.whitespace) remaining after tab expansion will be replaced by a single space (default: True).

**drop\_whitespace**bool, optional

If True, whitespace that, after wrapping, happens to end up at the beginning or end of a line is dropped (default: True).

**initial\_indent**str, optional

String that will be prepended to the first line of wrapped output. Counts towards the length of the first line. The empty string is not indented (default: ‘’).

**subsequent\_indent**str, optional

String that will be prepended to all lines of wrapped output except the first. Counts towards the length of each line except the first (default: ‘’).

**fix\_sentence\_endings**bool, optional

If true, TextWrapper attempts to detect sentence endings and ensure that sentences are always separated by exactly two spaces. This is generally desired for text in a monospaced font. However, the sentence detection algorithm is imperfect: it assumes that a sentence ending consists of a lowercase letter followed by one of ‘.’, ‘!’, or ‘?’, possibly followed by one of ‘”’ or “’”, followed by a space. One problem with this algorithm is that it is unable to detect the difference between “Dr.” in \[…\] Dr. Frankenstein’s monster \[…\] and “Spot.” in \[…\] See Spot. See Spot run \[…\] Since the sentence detection algorithm relies on string.lowercase for the definition of “lowercase letter”, and a convention of using two spaces after a period to separate sentences on the same line, it is specific to English-language texts (default: False).

**break\_long\_words**bool, optional

If True, then words longer than width will be broken in order to ensure that no lines are longer than width. If it is false, long words will not be broken, and some lines may be longer than width (default: True).

**break\_on\_hyphens**bool, optional

If True, wrapping will occur preferably on whitespace and right after hyphens in compound words, as it is customary in English. If false, only whitespaces will be considered as potentially good places for line breaks, but you need to set break\_long\_words to false if you want truly insecable words (default: True).

**max\_lines**int, optional

If not None, then the output will contain at most max\_lines lines, with placeholder appearing at the end of the output (default: None).

**placeholder**str, optional

String that will appear at the end of the output text if it has been truncated (default: ‘ \[…\]’).

Returns:

Series or Index

A Series or Index where the strings are wrapped at the specified line width.

See also

[`Series.str.strip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip "pandas.Series.str.strip")

Remove leading and trailing characters in Series/Index.

[`Series.str.lstrip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lstrip.html#pandas.Series.str.lstrip "pandas.Series.str.lstrip")

Remove leading characters in Series/Index.

[`Series.str.rstrip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rstrip.html#pandas.Series.str.rstrip "pandas.Series.str.rstrip")

Remove trailing characters in Series/Index.

Notes

Internally, this method uses a [`textwrap.TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "(in Python v3.15)")
 instance with default settings. To achieve behavior matching R’s stringr library str\_wrap function, use the arguments:

*   expand\_tabs = False
    
*   replace\_whitespace = True
    
*   drop\_whitespace = True
    
*   break\_long\_words = False
    
*   break\_on\_hyphens = False
    

Examples

\>>> s \= pd.Series(\["line to be wrapped", "another line to be wrapped"\])
\>>> s.str.wrap(12)
0             line to be\\nwrapped
1    another line\\nto be\\nwrapped
dtype: str

Copy to clipboard

On this page