[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.transpose[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas-dataframe-transpose "Link to this heading")

==============================================================================================================================================================

DataFrame.transpose(_\*args_, _copy\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L4018-L4202)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose "Link to this definition")

Transpose index and columns.

Reflect the DataFrame over its main diagonal by writing rows as columns and vice-versa. The property [`T`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html#pandas.DataFrame.T "pandas.DataFrame.T")
 is an accessor to the method [`transpose()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose "pandas.DataFrame.transpose")
.

Parameters:

**\*args**tuple, optional

Accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Note that a copy is always required for mixed dtype DataFrames, or for DataFrames with any extension types.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

Returns:

DataFrame

The transposed DataFrame.

See also

[`numpy.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "(in NumPy v2.5)")

Permute the dimensions of a given array.

Notes

Transposing a DataFrame with mixed dtypes will result in a homogeneous DataFrame with the object dtype. In such a case, a copy of the data is always made.

Examples

**Square DataFrame with homogeneous dtype**

\>>> d1 \= {"col1": \[1, 2\], "col2": \[3, 4\]}
\>>> df1 \= pd.DataFrame(data\=d1)
\>>> df1
   col1  col2
0     1     3
1     2     4

Copy to clipboard

\>>> df1\_transposed \= df1.T  \# or df1.transpose()
\>>> df1\_transposed
      0  1
col1  1  2
col2  3  4

Copy to clipboard

When the dtype is homogeneous in the original DataFrame, we get a transposed DataFrame with the same dtype:

\>>> df1.dtypes
col1    int64
col2    int64
dtype: object
\>>> df1\_transposed.dtypes
0    int64
1    int64
dtype: object

Copy to clipboard

**Non-square DataFrame with mixed dtypes**

\>>> d2 \= {
...     "name": \["Alice", "Bob"\],
...     "score": \[9.5, 8\],
...     "employed": \[False, True\],
...     "kids": \[0, 0\],
... }
\>>> df2 \= pd.DataFrame(data\=d2)
\>>> df2
    name  score  employed  kids
0  Alice    9.5     False     0
1    Bob    8.0      True     0

Copy to clipboard

\>>> df2\_transposed \= df2.T  \# or df2.transpose()
\>>> df2\_transposed
              0     1
name      Alice   Bob
score       9.5   8.0
employed  False  True
kids          0     0

Copy to clipboard

When the DataFrame has mixed dtypes, we get a transposed DataFrame with the object dtype:

\>>> df2.dtypes
name            str
score       float64
employed       bool
kids          int64
dtype: object
\>>> df2\_transposed.dtypes
0    object
1    object
dtype: object

Copy to clipboard

On this page