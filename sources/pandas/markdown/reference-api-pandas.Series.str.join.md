[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.join.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.join.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.join.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.join.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.join.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.join.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.join.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.join.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.join.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.join.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.join.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.join.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.join[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html#pandas-series-str-join "Link to this heading")

==================================================================================================================================================

Series.str.join(_sep_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1347-L1415)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html#pandas.Series.str.join "Link to this definition")

Join lists contained as elements in the Series/Index with passed delimiter.

If the elements of a Series are lists themselves, join the content of these lists using the delimiter passed to the function. This function is an equivalent to [`str.join()`](https://docs.python.org/3/builtins/stdtypes.html#str.join "(in Python v3.15)")
.

Parameters:

**sep**str

Delimiter to use between list entries.

Returns:

Series/Index: object

The list entries concatenated by intervening occurrences of the delimiter.

Raises:

AttributeError

If the supplied Series contains neither strings nor lists.

See also

[`str.join`](https://docs.python.org/3/builtins/stdtypes.html#str.join "(in Python v3.15)")

Standard library version of this method.

[`Series.str.split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split")

Split strings around given separator/delimiter.

Notes

If any of the list items is not a string object, the result of the join will be NaN.

Examples

Example with a list that contains non-string elements.

\>>> s \= pd.Series(
...     \[\
...         \["lion", "elephant", "zebra"\],\
...         \[1.1, 2.2, 3.3\],\
...         \["cat", np.nan, "dog"\],\
...         \["cow", 4.5, "goat"\],\
...         \["duck", \["swan", "fish"\], "guppy"\],\
...     \]
... )
\>>> s
0        \[lion, elephant, zebra\]
1                \[1.1, 2.2, 3.3\]
2                \[cat, nan, dog\]
3               \[cow, 4.5, goat\]
4    \[duck, \[swan, fish\], guppy\]
dtype: object

Copy to clipboard

Join all lists using a ‘-’. The lists containing object(s) of types other than str will produce a NaN.

\>>> s.str.join("-")
0    lion-elephant-zebra
1                    NaN
2                    NaN
3                    NaN
4                    NaN
dtype: object

Copy to clipboard

On this page