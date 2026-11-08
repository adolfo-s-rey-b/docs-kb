[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.notna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.notna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.notna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.notna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.notna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.notna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.notna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.notna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.notna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.notna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.notna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.notna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.notna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.notna[#](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas-notna "Link to this heading")

====================================================================================================================

pandas.notna(_obj_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/missing.py#L312-L392)
[#](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "Link to this definition")

Detect non-missing values for an array-like object.

This function takes a scalar or array-like object and indicates whether values are valid (not missing, which is `NaN` in numeric arrays, `None` or `NaN` in object arrays, `NaT` in datetimelike).

Parameters:

**obj**array-like or object value

Object to check for _not_ null or _non_\-missing values.

Returns:

bool or array-like of bool

For scalar input, returns a scalar boolean. For array input, returns an array of boolean indicating whether each corresponding element is valid.

See also

[`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")

Boolean inverse of pandas.notna.

[`Series.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")

Detect valid values in a Series.

[`DataFrame.notna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "pandas.DataFrame.notna")

Detect valid values in a DataFrame.

[`Index.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#pandas.Index.notna "pandas.Index.notna")

Detect valid values in an Index.

Examples

Scalar arguments (including strings) result in a scalar boolean.

\>>> pd.notna("dog")
True

Copy to clipboard

\>>> pd.notna(pd.NA)
False

Copy to clipboard

\>>> pd.notna(np.nan)
False

Copy to clipboard

ndarrays result in an ndarray of booleans.

\>>> array \= np.array(\[\[1, np.nan, 3\], \[4, 5, np.nan\]\])
\>>> array
array(\[\[ 1., nan,  3.\],\
       \[ 4.,  5., nan\]\])
\>>> pd.notna(array)
array(\[\[ True, False,  True\],\
       \[ True,  True, False\]\])

Copy to clipboard

For indexes, an ndarray of booleans is returned.

\>>> index \= pd.DatetimeIndex(\["2017-07-05", "2017-07-06", None, "2017-07-08"\])
\>>> index
DatetimeIndex(\['2017-07-05', '2017-07-06', 'NaT', '2017-07-08'\],
              dtype='datetime64\[us\]', freq=None)
\>>> pd.notna(index)
array(\[ True,  True, False,  True\])

Copy to clipboard

For Series and DataFrame, the same type is returned, containing booleans.

\>>> df \= pd.DataFrame(\[\["ant", "bee", "cat"\], \["dog", None, "fly"\]\])
\>>> df
     0    1    2
0  ant  bee  cat
1  dog  NaN  fly
\>>> pd.notna(df)
      0      1     2
0  True   True  True
1  True  False  True

Copy to clipboard

\>>> pd.notna(df\[1\])
0     True
1    False
Name: 1, dtype: bool

Copy to clipboard

On this page