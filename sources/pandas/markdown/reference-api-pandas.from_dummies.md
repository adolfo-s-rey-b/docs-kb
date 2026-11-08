[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.from_dummies.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.from_dummies.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.from_dummies.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.from_dummies.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.from_dummies.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.from_dummies.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.from_dummies.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.from_dummies.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.from_dummies.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.from_dummies.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.from_dummies.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.from_dummies.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.from\_dummies[#](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html#pandas-from-dummies "Link to this heading")

==========================================================================================================================================

pandas.from\_dummies(_data_, _sep\=None_, _default\_category\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/encoding.py#L405-L623)
[#](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html#pandas.from_dummies "Link to this definition")

Create a categorical `DataFrame` from a `DataFrame` of dummy variables.

Inverts the operation performed by [`get_dummies()`](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#pandas.get_dummies "pandas.get_dummies")
.

Parameters:

**data**DataFrame

Data which contains dummy-coded variables in form of integer columns of 1’s and 0’s.

**sep**str, default None

Separator used in the column names of the dummy categories they are character indicating the separation of the categorical names from the prefixes. For example, if your column names are ‘prefix\_A’ and ‘prefix\_B’, you can strip the underscore by specifying sep=’\_’.

**default\_category**None, Hashable or dict of Hashables, default None

The default category is the implied category when a value has none of the listed categories specified with a one, i.e. if all dummies in a row are zero. Can be a single value for all variables or a dict directly mapping the default categories to a prefix of a variable. The default category will be coerced to the dtype of `data.columns` if such coercion is lossless, and will raise otherwise.

Returns:

DataFrame

Categorical data decoded from the dummy input-data.

Raises:

ValueError

*   When the input `DataFrame` `data` contains NA values.
    
*   When the input `DataFrame` `data` contains column names with separators that do not match the separator specified with `sep`.
    
*   When a `dict` passed to `default_category` does not include an implied category for each prefix.
    
*   When a value in `data` has more than one category assigned to it.
    
*   When `default_category=None` and a value in `data` has no category assigned to it.
    

TypeError

*   When the input `data` is not of type `DataFrame`.
    
*   When the input `DataFrame` `data` contains non-dummy data.
    
*   When the passed `sep` is of a wrong data type.
    
*   When the passed `default_category` is of a wrong data type.
    

See also

[`get_dummies()`](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#pandas.get_dummies "pandas.get_dummies")

Convert `Series` or `DataFrame` to dummy codes.

[`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")

Represent a categorical variable in classic.

Notes

The columns of the passed dummy data should only include 1’s and 0’s, or boolean values.

Examples

\>>> df \= pd.DataFrame({"a": \[1, 0, 0, 1\], "b": \[0, 1, 0, 0\], "c": \[0, 0, 1, 0\]})

Copy to clipboard

\>>> df
   a  b  c
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0

Copy to clipboard

\>>> pd.from\_dummies(df)
0     a
1     b
2     c
3     a

Copy to clipboard

\>>> df \= pd.DataFrame(
...     {
...         "col1\_a": \[1, 0, 1\],
...         "col1\_b": \[0, 1, 0\],
...         "col2\_a": \[0, 1, 0\],
...         "col2\_b": \[1, 0, 0\],
...         "col2\_c": \[0, 0, 1\],
...     }
... )

Copy to clipboard

\>>> df
      col1\_a  col1\_b  col2\_a  col2\_b  col2\_c
0       1       0       0       1       0
1       0       1       1       0       0
2       1       0       0       0       1

Copy to clipboard

\>>> pd.from\_dummies(df, sep\="\_")
    col1    col2
0    a       b
1    b       a
2    a       c

Copy to clipboard

\>>> df \= pd.DataFrame(
...     {
...         "col1\_a": \[1, 0, 0\],
...         "col1\_b": \[0, 1, 0\],
...         "col2\_a": \[0, 1, 0\],
...         "col2\_b": \[1, 0, 0\],
...         "col2\_c": \[0, 0, 0\],
...     }
... )

Copy to clipboard

\>>> df
      col1\_a  col1\_b  col2\_a  col2\_b  col2\_c
0       1       0       0       1       0
1       0       1       1       0       0
2       0       0       0       0       0

Copy to clipboard

\>>> pd.from\_dummies(df, sep\="\_", default\_category\={"col1": "d", "col2": "e"})
    col1    col2
0    a       b
1    b       a
2    d       e

Copy to clipboard

On this page