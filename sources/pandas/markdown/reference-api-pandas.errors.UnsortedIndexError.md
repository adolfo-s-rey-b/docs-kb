[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsortedIndexError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.UnsortedIndexError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsortedIndexError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.UnsortedIndexError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.UnsortedIndexError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.UnsortedIndexError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.UnsortedIndexError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.UnsortedIndexError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.UnsortedIndexError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.UnsortedIndexError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.UnsortedIndexError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.UnsortedIndexError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.UnsortedIndexError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.UnsortedIndexError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.UnsortedIndexError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsortedIndexError.html#pandas-errors-unsortedindexerror "Link to this heading")

================================================================================================================================================================================

exception pandas.errors.UnsortedIndexError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L273-L305)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.UnsortedIndexError.html#pandas.errors.UnsortedIndexError "Link to this definition")

Error raised when slicing a MultiIndex which has not been lexsorted.

Subclass of KeyError.

See also

`DataFrame.sort_index`

Sort a DataFrame by its index.

`DataFrame.set_index`

Set the DataFrame index using existing columns.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "cat": \[0, 0, 1, 1\],
...         "color": \["white", "white", "brown", "black"\],
...         "lives": \[4, 4, 3, 7\],
...     },
... )
\>>> df \= df.set\_index(\["cat", "color"\])
\>>> df
            lives
cat  color
0    white    4
     white    4
1    brown    3
     black    7
\>>> df.loc\[(0, "black") : (1, "white")\]
Traceback (most recent call last):
UnsortedIndexError: 'Key length (2) was greater
than MultiIndex lexsort depth (1)'

Copy to clipboard

On this page