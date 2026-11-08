[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.sum.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.sum.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.sum.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.sum.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.sum.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.sum.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.sum.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.sum.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.sum.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.sum.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.sum.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.sum.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.sum.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.sum.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.sum[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.sum.html#pandas-api-typing-rolling-sum "Link to this heading")

=======================================================================================================================================================================

Rolling.sum(_numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2393-L2491)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.sum.html#pandas.api.typing.Rolling.sum "Link to this definition")

Calculate the rolling sum.

This is equivalent to applying `numpy.sum` over each rolling window. Missing values (NaN) are excluded from the calculation.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**engine**str, default None

*   `'cython'` : Runs the operation through C-extensions from cython.
    
*   `'numba'` : Runs the operation through JIT compiled code from numba.
    
*   `None` : Defaults to `'cython'` or globally setting `compute.use_numba`
    

**engine\_kwargs**dict, default None

*   For `'cython'` engine, there are no accepted `engine_kwargs`
    
*   For `'numba'` engine, the engine can accept `nogil` and `parallel` dictionary keys. The values must either be `True` or `False`. The default `engine_kwargs` for the `'numba'` engine is `{'nogil': False, 'parallel': False}`.
    

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.sum`

Aggregating sum for Series.

`DataFrame.sum`

Aggregating sum for DataFrame.

Notes

See [Numba engine](https://pandas.pydata.org/docs/user_guide/window.html#window-numba-engine)
 and [Numba (JIT compilation)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for extended documentation and performance considerations for the Numba engine.

Examples

\>>> s \= pd.Series(\[1, 2, 3, 4, 5\])
\>>> s
0    1
1    2
2    3
3    4
4    5
dtype: int64

Copy to clipboard

\>>> s.rolling(3).sum()
0     NaN
1     NaN
2     6.0
3     9.0
4    12.0
dtype: float64

Copy to clipboard

\>>> s.rolling(3, center\=True).sum()
0     NaN
1     6.0
2     9.0
3    12.0
4     NaN
dtype: float64

Copy to clipboard

For DataFrame, each sum is computed column-wise.

\>>> df \= pd.DataFrame({"A": s, "B": s\*\*2})
\>>> df
A   B
0  1   1
1  2   4
2  3   9
3  4  16
4  5  25

Copy to clipboard

\>>> df.rolling(3).sum()
     A     B
0   NaN   NaN
1   NaN   NaN
2   6.0  14.0
3   9.0  29.0
4  12.0  50.0

Copy to clipboard

On this page