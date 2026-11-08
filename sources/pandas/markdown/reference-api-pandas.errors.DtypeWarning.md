[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.DtypeWarning.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.DtypeWarning.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.DtypeWarning.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.DtypeWarning.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.DtypeWarning.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.DtypeWarning.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.DtypeWarning.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.DtypeWarning.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.DtypeWarning.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.DtypeWarning.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.DtypeWarning.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.DtypeWarning.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.DtypeWarning.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.DtypeWarning.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.DtypeWarning[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.DtypeWarning.html#pandas-errors-dtypewarning "Link to this heading")

==============================================================================================================================================================

exception pandas.errors.DtypeWarning[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L333-L388)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.DtypeWarning.html#pandas.errors.DtypeWarning "Link to this definition")

Warning raised when reading different dtypes in a column from a file.

Raised for a dtype incompatibility. This can happen whenever read\_csv or read\_table encounter non-uniform dtypes in a column(s) of a given CSV file.

See also

`read_csv`

Read CSV (comma-separated) file into a DataFrame.

`read_table`

Read general delimited file into a DataFrame.

Notes

This warning is issued when dealing with larger files because the dtype checking happens per chunk read.

Despite the warning, the CSV file is read with mixed types in a single column which will be an object type. See the examples below to better understand this issue.

Examples

This example creates and reads a large CSV file with a column that contains int and str.

\>>> df \= pd.DataFrame(
...     {
...         "a": (\["1"\] \* 100000 + \["X"\] \* 100000 + \["1"\] \* 100000),
...         "b": \["b"\] \* 300000,
...     }
... )
\>>> df.to\_csv("test.csv", index\=False)
\>>> df2 \= pd.read\_csv("test.csv")
... \# DtypeWarning: Columns (0: a) have mixed types

Copy to clipboard

Important to notice that `df2` will contain both str and int for the same input, ‘1’.

\>>> df2.iloc\[262140, 0\]
'1'
\>>> type(df2.iloc\[262140, 0\])
<class 'str'>
\>>> df2.iloc\[262150, 0\]
1
\>>> type(df2.iloc\[262150, 0\])
<class 'int'>

Copy to clipboard

One way to solve this issue is using the dtype parameter in the read\_csv and read\_table functions to explicit the conversion:

\>>> df2 \= pd.read\_csv("test.csv", sep\=",", dtype\={"a": str})

Copy to clipboard

No warning was issued.

On this page