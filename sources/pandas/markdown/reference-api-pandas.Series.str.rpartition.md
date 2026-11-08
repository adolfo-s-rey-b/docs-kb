[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rpartition.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.rpartition.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rpartition.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.rpartition.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.rpartition.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.rpartition.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.rpartition.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.rpartition.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.rpartition.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.rpartition.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.rpartition.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.rpartition.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.rpartition.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.rpartition.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.rpartition[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rpartition.html#pandas-series-str-rpartition "Link to this heading")

====================================================================================================================================================================

Series.str.rpartition(_sep\=' '_, _expand\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L1177-L1267)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rpartition.html#pandas.Series.str.rpartition "Link to this definition")

Split the string at the last occurrence of sep.

This method splits the string at the last occurrence of sep, and returns 3 elements containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return 3 elements containing two empty strings, followed by the string itself.

Parameters:

**sep**str, default “ “

String to split on.

**expand**bool, default True

If True, return DataFrame/MultiIndex expanding dimensionality. If False, return Series/Index.

Returns:

DataFrame/MultiIndex or Series/Index of objects

Returns appropriate type based on expand parameter with strings split based on the sep parameter.

See also

[`partition`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.partition.html#pandas.Series.str.partition "pandas.Series.str.partition")

Split the string at the first occurrence of sep.

[`Series.str.split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split")

Split strings around given separators.

[`str.partition`](https://docs.python.org/3/builtins/stdtypes.html#str.partition "(in Python v3.15)")

Standard library version.

Examples

\>>> s \= pd.Series(\["Linda van der Berg", "George Pitt-Rivers"\])
\>>> s
0    Linda van der Berg
1    George Pitt-Rivers
dtype: str

Copy to clipboard

\>>> s.str.partition()
        0  1             2
0   Linda     van der Berg
1  George      Pitt-Rivers

Copy to clipboard

To partition by the last space instead of the first one:

\>>> s.str.rpartition()
               0  1            2
0  Linda van der            Berg
1         George     Pitt-Rivers

Copy to clipboard

To partition by something different than a space:

\>>> s.str.partition("-")
                    0  1       2
0  Linda van der Berg
1         George Pitt  -  Rivers

Copy to clipboard

To return a Series containing tuples instead of a DataFrame:

\>>> s.str.partition("-", expand\=False)
0    (Linda van der Berg, , )
1    (George Pitt, -, Rivers)
dtype: object

Copy to clipboard

Also available on indices:

\>>> idx \= pd.Index(\["X 123", "Y 999"\])
\>>> idx
Index(\['X 123', 'Y 999'\], dtype='str')

Copy to clipboard

Which will create a MultiIndex:

\>>> idx.str.partition()
MultiIndex(\[('X', ' ', '123'),\
            ('Y', ' ', '999')\],
           )

Copy to clipboard

Or an index with tuples with `expand=False`:

\>>> idx.str.partition(expand\=False)
Index(\[('X', ' ', '123'), ('Y', ' ', '999')\], dtype='object')

Copy to clipboard

On this page