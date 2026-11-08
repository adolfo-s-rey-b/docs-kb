[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.get_dummies.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.get_dummies.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.get_dummies.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.get_dummies.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.get_dummies.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.get_dummies.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.get_dummies.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.get_dummies.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.get_dummies.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.get_dummies.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.get_dummies.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.get_dummies.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.get\_dummies[#](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#pandas-get-dummies "Link to this heading")

=======================================================================================================================================

pandas.get\_dummies(_data_, _prefix\=None_, _prefix\_sep\='\_'_, _dummy\_na\=False_, _columns\=None_, _sparse\=False_, _drop\_first\=False_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/encoding.py#L43-L275)
[#](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#pandas.get_dummies "Link to this definition")

Convert categorical variable into dummy/indicator variables.

Each variable is converted in as many 0/1 variables as there are different values. Columns in the output are each named after a value; if the input is a DataFrame, the name of the original variable is prepended to the value.

Parameters:

**data**array-like, Series, or DataFrame

Data of which to get dummy indicators.

**prefix**str, list of str, or dict of str, default None

A string to be prepended to DataFrame column names. Pass a list with length equal to the number of columns when calling get\_dummies on a DataFrame. Alternatively, prefix can be a dictionary mapping column names to prefixes.

**prefix\_sep**str, list of str, or dict of str, default ‘\_’

Should you choose to prepend DataFrame column names with a prefix, this is the separator/delimiter to use between the two. Alternatively, prefix\_sep can be a list with length equal to the number of columns, or a dictionary mapping column names to separators.

**dummy\_na**bool, default False

If True, a NaN indicator column will be added even if no NaN values are present. If False, NA values are encoded as all zero.

**columns**list-like, default None

Column names in the DataFrame to be encoded. If columns is None then all the columns with object, string, or category dtype will be converted.

**sparse**bool, default False

Whether the dummy-encoded columns should be backed by a `SparseArray` (True) or a regular NumPy array (False).

**drop\_first**bool, default False

Whether to get k-1 dummies out of k categorical levels by removing the first level.

**dtype**dtype, default bool

Data type for new columns. Only a single dtype is allowed.

Returns:

DataFrame

Dummy-coded data. If data contains other columns than the dummy-coded one(s), these will be prepended, unaltered, to the result.

See also

[`Series.str.get_dummies`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html#pandas.Series.str.get_dummies "pandas.Series.str.get_dummies")

Convert Series of strings to dummy codes.

[`from_dummies()`](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html#pandas.from_dummies "pandas.from_dummies")

Convert dummy codes to categorical `DataFrame`.

Notes

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-dummies)
 for more examples.

Examples

\>>> s \= pd.Series(list("abca"))

Copy to clipboard

\>>> pd.get\_dummies(s)
       a      b      c
0   True  False  False
1  False   True  False
2  False  False   True
3   True  False  False

Copy to clipboard

\>>> s1 \= \["a", "b", np.nan\]

Copy to clipboard

\>>> pd.get\_dummies(s1)
       a      b
0   True  False
1  False   True
2  False  False

Copy to clipboard

\>>> pd.get\_dummies(s1, dummy\_na\=True)
       a      b    NaN
0   True  False  False
1  False   True  False
2  False  False   True

Copy to clipboard

\>>> df \= pd.DataFrame({"A": \["a", "b", "a"\], "B": \["b", "a", "c"\], "C": \[1, 2, 3\]})

Copy to clipboard

\>>> pd.get\_dummies(df, prefix\=\["col1", "col2"\])
   C  col1\_a  col1\_b  col2\_a  col2\_b  col2\_c
0  1    True   False   False    True   False
1  2   False    True    True   False   False
2  3    True   False   False   False    True

Copy to clipboard

\>>> pd.get\_dummies(pd.Series(list("abcaa")))
       a      b      c
0   True  False  False
1  False   True  False
2  False  False   True
3   True  False  False
4   True  False  False

Copy to clipboard

\>>> pd.get\_dummies(pd.Series(list("abcaa")), drop\_first\=True)
       b      c
0  False  False
1   True  False
2  False   True
3  False  False
4  False  False

Copy to clipboard

\>>> pd.get\_dummies(pd.Series(list("abc")), dtype\=float)
     a    b    c
0  1.0  0.0  0.0
1  0.0  1.0  0.0
2  0.0  0.0  1.0

Copy to clipboard

On this page