[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.var.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.var.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.var.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.var.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.var.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.var.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.var.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.var.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.var.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.var.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.var.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.var.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.var.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.var.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.var[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.var.html#pandas-api-typing-rolling-var "Link to this heading")

=======================================================================================================================================================================

Rolling.var(_ddof\=1_, _numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2855-L2930)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.var.html#pandas.api.typing.Rolling.var "Link to this definition")

Calculate the rolling variance.

This is equivalent to applying `numpy.var` (with the specified `ddof`) over each rolling window.

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
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`.
    

The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}`.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

[`numpy.var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "(in NumPy v2.5)")

Equivalent method for NumPy array.

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.var`

Aggregating var for Series.

`DataFrame.var`

Aggregating var for DataFrame.

Notes

The default `ddof` of 1 used in `Series.var()` is different than the default `ddof` of 0 in [`numpy.var()`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "(in NumPy v2.5)")
.

A minimum of one period is required for the rolling calculation.

Examples

\>>> s \= pd.Series(\[5, 5, 6, 7, 5, 5, 5\])
\>>> s.rolling(3).var()
0         NaN
1         NaN
2    0.333333
3    1.000000
4    1.000000
5    1.333333
6    0.000000
dtype: float64

Copy to clipboard

On this page