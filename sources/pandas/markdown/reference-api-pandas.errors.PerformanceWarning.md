[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.PerformanceWarning.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.PerformanceWarning.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.PerformanceWarning.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.PerformanceWarning.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.PerformanceWarning.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.PerformanceWarning.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.PerformanceWarning.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.PerformanceWarning.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.PerformanceWarning.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.PerformanceWarning.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.PerformanceWarning.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.PerformanceWarning.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.PerformanceWarning.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.PerformanceWarning.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.PerformanceWarning[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.PerformanceWarning.html#pandas-errors-performancewarning "Link to this heading")

================================================================================================================================================================================

exception pandas.errors.PerformanceWarning[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L64-L96)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.PerformanceWarning.html#pandas.errors.PerformanceWarning "Link to this definition")

Warning raised when there is a possible performance impact.

This warning is typically raised when an operation may be slower than expected due to the data structure or access pattern being used.

See also

`DataFrame.set_index`

Set the DataFrame index using existing columns.

`DataFrame.loc`

Access a group of rows and columns by label(s) or a boolean array.

Examples

\>>> df \= pd.DataFrame(
...     {"jim": \[0, 0, 1, 1\], "joe": \["x", "x", "z", "y"\], "jolie": \[1, 2, 3, 4\]}
... )
\>>> df \= df.set\_index(\["jim", "joe"\])
\>>> df
          jolie
jim  joe
0    x    1
     x    2
1    z    3
     y    4
\>>> df.loc\[(1, "z")\]
\# PerformanceWarning: indexing past lexsort depth may impact performance.
df.loc\[(1, 'z')\]
          jolie
jim  joe
1    z        3

Copy to clipboard

On this page