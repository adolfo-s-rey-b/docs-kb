[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.interpolate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.interpolate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.interpolate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.interpolate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.interpolate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.interpolate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.interpolate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.interpolate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.interpolate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.interpolate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.interpolate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.interpolate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.interpolate[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html#pandas-dataframe-interpolate "Link to this heading")

====================================================================================================================================================================

DataFrame.interpolate(_method\='linear'_, _\*_, _axis\=0_, _limit\=None_, _inplace\=False_, _limit\_direction\=None_, _limit\_area\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L8193-L8415)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate "Link to this definition")

Fill NaN values using an interpolation method.

Please note that only `method='linear'` is supported for DataFrame/Series with a MultiIndex.

Parameters:

**method**str, default ‘linear’

Interpolation technique to use. One of:

*   ‘linear’: Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes.
    
*   ‘time’: Works on daily and higher resolution data to interpolate given length of interval. This interpolates values based on time interval between observations.
    
*   ‘index’: The interpolation uses the numerical values of the DataFrame’s index to linearly calculate missing values.
    
*   ‘values’: Interpolation based on the numerical values in the DataFrame, treating them as equally spaced along the index.
    
*   ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘polynomial’: Passed to scipy.interpolate.interp1d, whereas ‘spline’ is passed to scipy.interpolate.UnivariateSpline. These methods use the numerical values of the index. Both ‘polynomial’ and ‘spline’ require that you also specify an order (int), e.g. `df.interpolate(method='polynomial', order=5)`. Note that, slinear method in Pandas refers to the Scipy first order spline instead of Pandas first order spline.
    
*   ‘krogh’, ‘piecewise\_polynomial’, ‘spline’, ‘pchip’, ‘akima’, ‘cubicspline’: Wrappers around the SciPy interpolation methods of similar names. See Notes.
    
*   ‘from\_derivatives’: Refers to scipy.interpolate.BPoly.from\_derivatives.
    

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Axis to interpolate along. For Series this parameter is unused and defaults to 0.

**limit**int, optional

Maximum number of consecutive NaNs to fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled, from the direction given by `limit_direction`. Must be greater than 0.

**inplace**bool, default False

Update the data in place if possible.

**limit\_direction**{‘forward’, ‘backward’, ‘both’}, optional, default ‘forward’

Consecutive NaNs will be filled in this direction.

**limit\_area**{None, ‘inside’, ‘outside’}, default None

Restrict which NaNs are filled based on their position relative to the valid values.

*   `None`: No fill restriction.
    
*   ‘inside’: Only fill NaNs surrounded by valid values (interpolate).
    
*   ‘outside’: Only fill NaNs outside valid values (extrapolate).
    

**\*\*kwargs**optional

Keyword arguments to pass on to the interpolating function. Not all methods use them: the `'linear'`, `'time'`, `'index'`, and `'values'` methods use NumPy and ignore any extra keyword arguments (for example, `left` and `right`).

Returns:

Series or DataFrame

Returns the same object type as the caller, interpolated at some or all `NaN` values.

See also

[`fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")

Fill missing values using different methods.

`scipy.interpolate.Akima1DInterpolator`

Piecewise cubic polynomials (Akima interpolator).

`scipy.interpolate.BPoly.from_derivatives`

Piecewise polynomial in the Bernstein basis.

`scipy.interpolate.interp1d`

Interpolate a 1-D function.

`scipy.interpolate.KroghInterpolator`

Interpolate polynomial (Krogh interpolator).

`scipy.interpolate.PchipInterpolator`

PCHIP 1-d monotonic cubic interpolation.

`scipy.interpolate.CubicSpline`

Cubic spline data interpolator.

Notes

The ‘krogh’, ‘piecewise\_polynomial’, ‘spline’, ‘pchip’ and ‘akima’ methods are wrappers around the respective SciPy implementations of similar names. These use the actual numerical values of the index. For more information on their behavior, see the [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/interpolate.html#univariate-interpolation)
.

Examples

Filling in `NaN` in a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 via linear interpolation.

\>>> s \= pd.Series(\[0, 1, np.nan, 3\])
\>>> s
0    0.0
1    1.0
2    NaN
3    3.0
dtype: float64
\>>> s.interpolate()
0    0.0
1    1.0
2    2.0
3    3.0
dtype: float64

Copy to clipboard

Filling in `NaN` in a Series via polynomial interpolation or splines: Both ‘polynomial’ and ‘spline’ methods require that you also specify an `order` (int).

\>>> s \= pd.Series(\[0, 2, np.nan, 8\])
\>>> s.interpolate(method\="polynomial", order\=2)
0    0.000000
1    2.000000
2    4.666667
3    8.000000
dtype: float64

Copy to clipboard

Fill the DataFrame forward (that is, going down) along each column using linear interpolation.

Note how the last entry in column ‘a’ is interpolated differently, because there is no entry after it to use for interpolation. Note how the first entry in column ‘b’ remains `NaN`, because there is no entry before it to use for interpolation.

\>>> df \= pd.DataFrame(
...     \[\
...         (0.0, np.nan, \-1.0, 1.0),\
...         (np.nan, 2.0, np.nan, np.nan),\
...         (2.0, 3.0, np.nan, 9.0),\
...         (np.nan, 4.0, \-4.0, 16.0),\
...     \],
...     columns\=list("abcd"),
... )
\>>> df
     a    b    c     d
0  0.0  NaN -1.0   1.0
1  NaN  2.0  NaN   NaN
2  2.0  3.0  NaN   9.0
3  NaN  4.0 -4.0  16.0
\>>> df.interpolate(method\="linear", limit\_direction\="forward", axis\=0)
     a    b    c     d
0  0.0  NaN -1.0   1.0
1  1.0  2.0 -2.0   5.0
2  2.0  3.0 -3.0   9.0
3  2.0  4.0 -4.0  16.0

Copy to clipboard

Using polynomial interpolation.

\>>> df\["d"\].interpolate(method\="polynomial", order\=2)
0     1.0
1     4.0
2     9.0
3    16.0
Name: d, dtype: float64

Copy to clipboard

On this page