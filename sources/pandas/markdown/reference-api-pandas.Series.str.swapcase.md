[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.swapcase.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.swapcase.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.swapcase.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.swapcase.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.swapcase.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.swapcase.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.swapcase.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.swapcase.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.swapcase.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.swapcase.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.swapcase.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.swapcase.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.swapcase[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html#pandas-series-str-swapcase "Link to this heading")

==============================================================================================================================================================

Series.str.swapcase()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L4210-L4280)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html#pandas.Series.str.swapcase "Link to this definition")

Convert strings in the Series/Index to be swapcased.

Equivalent to [`str.swapcase()`](https://docs.python.org/3/builtins/stdtypes.html#str.swapcase "(in Python v3.15)")
.

Returns:

Series or Index of objects

A Series or Index where the strings are modified by [`str.swapcase()`](https://docs.python.org/3/builtins/stdtypes.html#str.swapcase "(in Python v3.15)")
.

See also

[`Series.str.lower`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")

Converts all characters to lowercase.

[`Series.str.upper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")

Converts all characters to uppercase.

[`Series.str.title`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")

Converts first character of each word to uppercase and remaining to lowercase.

[`Series.str.capitalize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.capitalize.html#pandas.Series.str.capitalize "pandas.Series.str.capitalize")

Converts first character to uppercase and remaining to lowercase.

[`Series.str.swapcase`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html#pandas.Series.str.swapcase "pandas.Series.str.swapcase")

Converts uppercase to lowercase and lowercase to uppercase.

[`Series.str.casefold`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.casefold.html#pandas.Series.str.casefold "pandas.Series.str.casefold")

Removes all case distinctions in the string.

Examples

\>>> s \= pd.Series(\["lower", "CAPITALS", "this is a sentence", "SwApCaSe"\])
\>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: str

Copy to clipboard

\>>> s.str.lower()
0                 lower
1              capitals
2    this is a sentence
3              swapcase
dtype: str

Copy to clipboard

\>>> s.str.upper()
0                 LOWER
1              CAPITALS
2    THIS IS A SENTENCE
3              SWAPCASE
dtype: str

Copy to clipboard

\>>> s.str.title()
0                 Lower
1              Capitals
2    This Is A Sentence
3              Swapcase
dtype: str

Copy to clipboard

\>>> s.str.capitalize()
0                 Lower
1              Capitals
2    This is a sentence
3              Swapcase
dtype: str

Copy to clipboard

\>>> s.str.swapcase()
0                 LOWER
1              capitals
2    THIS IS A SENTENCE
3              sWaPcAsE
dtype: str

Copy to clipboard

On this page