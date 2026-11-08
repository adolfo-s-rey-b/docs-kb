[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.get.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.get.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.get.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.get.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.get.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.get.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.get.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.get.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.get.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.get.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.get.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.get.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.get[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html#pandas-series-str-get "Link to this heading")

===============================================================================================================================================

Series.str.get(_i_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1269-L1345)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html#pandas.Series.str.get "Link to this definition")

Extract element from each component at specified position or with specified key.

Extract element from lists, tuples, dict, or strings in each element in the Series/Index.

Parameters:

**i**int or hashable dict label

Position or key of element to extract.

Returns:

Series or Index

Series or Index where each value is the extracted element from the corresponding input component.

See also

[`Series.str.extract`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "pandas.Series.str.extract")

Extract capture groups in the regex as columns in a DataFrame.

Examples

\>>> s \= pd.Series(
...     \[\
...         "String",\
...         (1, 2, 3),\
...         \["a", "b", "c"\],\
...         123,\
...         \-456,\
...         {1: "Hello", "2": "World"},\
...     \]
... )
\>>> s
0                        String
1                     (1, 2, 3)
2                     \[a, b, c\]
3                           123
4                          -456
5    {1: 'Hello', '2': 'World'}
dtype: object

Copy to clipboard

\>>> s.str.get(1)
0        t
1        2
2        b
3      NaN
4      NaN
5    Hello
dtype: object

Copy to clipboard

\>>> s.str.get(\-1)
0      g
1      3
2      c
3    NaN
4    NaN
5    None
dtype: object

Copy to clipboard

Return element with given key

\>>> s \= pd.Series(
...     \[\
...         {"name": "Hello", "value": "World"},\
...         {"name": "Goodbye", "value": "Planet"},\
...     \]
... )
\>>> s.str.get("name")
0      Hello
1    Goodbye
dtype: object

Copy to clipboard

On this page