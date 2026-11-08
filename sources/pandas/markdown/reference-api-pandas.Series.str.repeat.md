[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.repeat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.repeat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.repeat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.repeat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.repeat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.repeat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.repeat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.repeat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.repeat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.repeat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.repeat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.repeat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.repeat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.repeat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.repeat[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.repeat.html#pandas-series-str-repeat "Link to this heading")

========================================================================================================================================================

Series.str.repeat(_repeats_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1893-L1953)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.repeat.html#pandas.Series.str.repeat "Link to this definition")

Duplicate each string in the Series or Index.

Duplicates each string in the Series or Index, either by applying the same repeat count to all elements or by using different repeat values for each element.

Parameters:

**repeats**int or sequence of int

Same value for all (int) or different value per (sequence).

Returns:

Series or pandas.Index

Series or Index of repeated string objects specified by input parameter repeats.

See also

[`Series.str.lower`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")

Convert all characters in each string to lowercase.

[`Series.str.upper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")

Convert all characters in each string to uppercase.

[`Series.str.title`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")

Convert each string to title case (capitalizing the first letter of each word).

[`Series.str.strip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip "pandas.Series.str.strip")

Remove leading and trailing whitespace from each string.

[`Series.str.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html#pandas.Series.str.replace "pandas.Series.str.replace")

Replace occurrences of a substring with another substring in each string.

[`Series.str.ljust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.ljust.html#pandas.Series.str.ljust "pandas.Series.str.ljust")

Left-justify each string in the Series/Index by padding with a specified character.

[`Series.str.rjust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rjust.html#pandas.Series.str.rjust "pandas.Series.str.rjust")

Right-justify each string in the Series/Index by padding with a specified character.

Examples

\>>> s \= pd.Series(\["a", "b", "c"\])
\>>> s
0    a
1    b
2    c
dtype: str

Copy to clipboard

Single int repeats string in Series

\>>> s.str.repeat(repeats\=2)
0    aa
1    bb
2    cc
dtype: str

Copy to clipboard

Sequence of int repeats corresponding string in Series

\>>> s.str.repeat(repeats\=\[1, 2, 3\])
0      a
1     bb
2    ccc
dtype: str

Copy to clipboard

On this page