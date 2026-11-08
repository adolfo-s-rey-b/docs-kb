[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.std[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.std.html#pandas-api-typing-expanding-std "Link to this heading")

=============================================================================================================================================================================

Expanding.std(_ddof\=1_, _numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L755-L830)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.std.html#pandas.api.typing.Expanding.std "Link to this definition")

Calculate the expanding standard deviation.

At each point in time, returns the sample standard deviation of all values observed up to that point, using `ddof` degrees of freedom correction.

Parameters:

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**engine**str, default None

*   `'cython'` : Runs the operation through C-extensions from cython.
    
*   `'numba'` : Runs the operation through JIT compiled code from numba.
    
*   `None` : Defaults to `'cython'` or globally setting `compute.use_numba`
    

**engine\_kwargs**dict, default None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}`
    

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

[`numpy.std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "(in NumPy v2.5)")

Equivalent method for NumPy array.

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.std`

Aggregating std for Series.

`DataFrame.std`

Aggregating std for DataFrame.

Notes

The default `ddof` of 1 used in `Series.std()` is different than the default `ddof` of 0 in [`numpy.std()`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "(in NumPy v2.5)")
.

A minimum of one period is required for the rolling calculation.

Examples

\>>> s \= pd.Series(\[5, 5, 6, 7, 5, 5, 5\])

Copy to clipboard

\>>> s.expanding(3).std()
0         NaN
1         NaN
2    0.577350
3    0.957427
4    0.894427
5    0.836660
6    0.786796
dtype: float64

Copy to clipboard

On this page