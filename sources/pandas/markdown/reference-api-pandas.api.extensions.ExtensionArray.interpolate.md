[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.interpolate[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html#pandas-api-extensions-extensionarray-interpolate "Link to this heading")

================================================================================================================================================================================================================================

ExtensionArray.interpolate(_\*_, _method_, _axis_, _index_, _limit_, _limit\_direction_, _limit\_area_, _copy_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1190-L1301)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html#pandas.api.extensions.ExtensionArray.interpolate "Link to this definition")

Fill NaN values using an interpolation method.

This method fills missing values in the array by interpolating between existing values using the specified interpolation technique.

Parameters:

**method**str, default ‘linear’

Interpolation technique to use. One of: \* ‘linear’: Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes. \* ‘time’: Works on daily and higher resolution data to interpolate given length of interval. \* ‘index’, ‘values’: use the actual numerical values of the index. \* ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘polynomial’: Passed to scipy.interpolate.interp1d, whereas ‘spline’ is passed to scipy.interpolate.UnivariateSpline. These methods use the numerical values of the index. Both ‘polynomial’ and ‘spline’ require that you also specify an order (int), e.g. arr.interpolate(method=’polynomial’, order=5). \* ‘krogh’, ‘piecewise\_polynomial’, ‘spline’, ‘pchip’, ‘akima’, ‘cubicspline’: Wrappers around the SciPy interpolation methods of similar names. See Notes. \* ‘from\_derivatives’: Refers to scipy.interpolate.BPoly.from\_derivatives.

**axis**int

Axis to interpolate along. For 1-dimensional data, use 0.

**index**Index

Index to use for interpolation.

**limit**int or None

Maximum number of consecutive NaNs to fill. Must be greater than 0.

**limit\_direction**{‘forward’, ‘backward’, ‘both’}

Consecutive NaNs will be filled in this direction.

**limit\_area**{‘inside’, ‘outside’} or None

If limit is specified, consecutive NaNs will be filled with this restriction. \* None: No fill restriction. \* ‘inside’: Only fill NaNs surrounded by valid values (interpolate). \* ‘outside’: Only fill NaNs outside valid values (extrapolate).

**copy**bool

If True, a copy of the object is returned with interpolated values.

**\*\*kwargs**optional

Keyword arguments to pass on to the interpolating function.

Returns:

ExtensionArray

An ExtensionArray with interpolated values.

See also

`Series.interpolate`

Interpolate values in a Series.

`DataFrame.interpolate`

Interpolate values in a DataFrame.

Notes

*   All parameters must be specified as keyword arguments.
    
*   The ‘krogh’, ‘piecewise\_polynomial’, ‘spline’, ‘pchip’ and ‘akima’ methods are wrappers around the respective SciPy implementations of similar names. These use the actual numerical values of the index.
    

Examples

Interpolating values in a NumPy array:

\>>> arr \= pd.arrays.NumpyExtensionArray(np.array(\[0, 1, np.nan, 3\]))
\>>> arr.interpolate(
...     method\="linear",
...     limit\=3,
...     limit\_direction\="forward",
...     index\=pd.Index(range(len(arr))),
...     fill\_value\=1,
...     copy\=False,
...     axis\=0,
...     limit\_area\="inside",
... )
<NumpyExtensionArray>
\[0.0, 1.0, 2.0, 3.0\]
Length: 4, dtype: float64

Copy to clipboard

Interpolating values in a FloatingArray:

\>>> arr \= pd.array(\[1.0, pd.NA, 3.0, 4.0, pd.NA, 6.0\], dtype\="Float64")
\>>> arr.interpolate(
...     method\="linear",
...     axis\=0,
...     index\=pd.Index(range(len(arr))),
...     limit\=None,
...     limit\_direction\="both",
...     limit\_area\=None,
...     copy\=True,
... )
<FloatingArray>
\[1.0, 2.0, 3.0, 4.0, 5.0, 6.0\]
Length: 6, dtype: Float64

Copy to clipboard

On this page