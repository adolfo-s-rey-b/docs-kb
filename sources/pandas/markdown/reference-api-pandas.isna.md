[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.isna[#](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas-isna "Link to this heading")

=================================================================================================================

pandas.isna(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/missing.py#L98-L175)
[#](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "Link to this definition")

Detect missing values for an array-like object.

This function takes a scalar or array-like object and indicates whether values are missing (`NaN` in numeric arrays, `None` or `NaN` in object arrays, `NaT` in datetimelike).

Parameters:

**obj**scalar or array-like

Object to check for null or missing values.

Returns:

bool or array-like of bool

For scalar input, returns a scalar boolean. For array input, returns an array of boolean indicating whether each corresponding element is missing.

See also

[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "pandas.notna")

Boolean inverse of pandas.isna.

[`Series.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")

Detect missing values in a Series.

[`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")

Detect missing values in a DataFrame.

[`Index.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas.Index.isna "pandas.Index.isna")

Detect missing values in an Index.

Examples

Scalar arguments (including strings) result in a scalar boolean.

\>>> pd.isna("dog")
False

Copy to clipboard

\>>> pd.isna(pd.NA)
True

Copy to clipboard

\>>> pd.isna(np.nan)
True

Copy to clipboard

ndarrays result in an ndarray of booleans.

\>>> array \= np.array(\[\[1, np.nan, 3\], \[4, 5, np.nan\]\])
\>>> array
array(\[\[ 1., nan,  3.\],\
       \[ 4.,  5., nan\]\])
\>>> pd.isna(array)
array(\[\[False,  True, False\],\
       \[False, False,  True\]\])

Copy to clipboard

For indexes, an ndarray of booleans is returned.

\>>> index \= pd.DatetimeIndex(\["2017-07-05", "2017-07-06", None, "2017-07-08"\])
\>>> index
DatetimeIndex(\['2017-07-05', '2017-07-06', 'NaT', '2017-07-08'\],
              dtype='datetime64\[us\]', freq=None)
\>>> pd.isna(index)
array(\[False, False,  True, False\])

Copy to clipboard

For Series and DataFrame, the same type is returned, containing booleans.

\>>> df \= pd.DataFrame(\[\["ant", "bee", "cat"\], \["dog", None, "fly"\]\])
\>>> df
     0    1    2
0  ant  bee  cat
1  dog  NaN  fly
\>>> pd.isna(df)
       0      1      2
0  False  False  False
1  False   True  False

Copy to clipboard

\>>> pd.isna(df\[1\])
0    False
1     True
Name: 1, dtype: bool

Copy to clipboard

On this page