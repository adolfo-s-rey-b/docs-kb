[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.slice.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.slice.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.slice.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.slice.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.slice.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.slice.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.slice.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.slice.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.slice.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.slice.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.slice.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.slice.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.slice[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html#pandas-series-str-slice "Link to this heading")

=====================================================================================================================================================

Series.str.slice(_start\=None_, _stop\=None_, _step\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L2290-L2368)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html#pandas.Series.str.slice "Link to this definition")

Slice substrings from each element in the Series or Index.

Slicing substrings from strings in a Series or Index helps extract specific portions of data, making it easier to analyze or manipulate text. This is useful for tasks like parsing structured text fields or isolating parts of strings with a consistent format.

Parameters:

**start**int, optional

Start position for slice operation.

**stop**int, optional

Stop position for slice operation.

**step**int, optional

Step size for slice operation.

Returns:

Series or Index of object

Series or Index from sliced substring from original string object.

See also

[`Series.str.slice_replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html#pandas.Series.str.slice_replace "pandas.Series.str.slice_replace")

Replace a slice with a string.

[`Series.str.get`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html#pandas.Series.str.get "pandas.Series.str.get")

Return element at position. Equivalent to Series.str.slice(start=i, stop=i+1) with i being the position.

Examples

\>>> s \= pd.Series(\["koala", "dog", "chameleon"\])
\>>> s
0        koala
1          dog
2    chameleon
dtype: str

Copy to clipboard

\>>> s.str.slice(start\=1)
0        oala
1          og
2    hameleon
dtype: str

Copy to clipboard

\>>> s.str.slice(start\=-1)
0           a
1           g
2           n
dtype: str

Copy to clipboard

\>>> s.str.slice(stop\=2)
0    ko
1    do
2    ch
dtype: str

Copy to clipboard

\>>> s.str.slice(step\=2)
0      kaa
1       dg
2    caeen
dtype: str

Copy to clipboard

\>>> s.str.slice(start\=0, stop\=5, step\=3)
0    kl
1     d
2    cm
dtype: str

Copy to clipboard

Equivalent behaviour to:

\>>> s.str\[0:5:3\]
0    kl
1     d
2    cm
dtype: str

Copy to clipboard

On this page