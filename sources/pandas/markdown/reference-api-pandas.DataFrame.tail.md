[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.tail.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.tail.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.tail.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.tail.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.tail.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.tail.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.tail.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.tail.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.tail.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.tail.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.tail.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.tail.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.tail[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas-dataframe-tail "Link to this heading")

===============================================================================================================================================

DataFrame.tail(_n\=5_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L5987-L6075)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "Link to this definition")

Return the last n rows.

This function returns last n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

For negative values of n, this function returns all rows except the first |n| rows, equivalent to `df[|n|:]`.

If `n` is larger than the number of rows, this function returns all rows.

Parameters:

**n**int, default 5

Number of rows to select.

Returns:

type of caller

The last n rows of the caller object.

See also

[`DataFrame.head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head")

The first n rows of the caller object.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "animal": \[\
...             "alligator",\
...             "bee",\
...             "falcon",\
...             "lion",\
...             "monkey",\
...             "parrot",\
...             "shark",\
...             "whale",\
...             "zebra",\
...         \]
...     }
... )
\>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

Copy to clipboard

Viewing the last 5 lines

\>>> df.tail()
   animal
4  monkey
5  parrot
6   shark
7   whale
8   zebra

Copy to clipboard

Viewing the last n lines (three in this case)

\>>> df.tail(3)
  animal
6  shark
7  whale
8  zebra

Copy to clipboard

For negative values of n

\>>> df.tail(\-3)
   animal
3    lion
4  monkey
5  parrot
6   shark
7   whale
8   zebra

Copy to clipboard

On this page