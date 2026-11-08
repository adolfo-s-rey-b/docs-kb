[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.median.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.median[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.median.html#pandas-api-typing-rolling-median "Link to this heading")

================================================================================================================================================================================

Rolling.median(_numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2709-L2776)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.median.html#pandas.api.typing.Rolling.median "Link to this definition")

Calculate the rolling median.

This is equivalent to applying `numpy.median` over each rolling window.

Parameters:

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

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.median`

Aggregating median for Series.

`DataFrame.median`

Aggregating median for DataFrame.

Notes

See [Numba engine](https://pandas.pydata.org/docs/user_guide/window.html#window-numba-engine)
 and [Numba (JIT compilation)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for extended documentation and performance considerations for the Numba engine.

Examples

Compute the rolling median of a series with a window size of 3.

\>>> s \= pd.Series(\[0, 1, 2, 3, 4\])
\>>> s.rolling(3).median()
0    NaN
1    NaN
2    1.0
3    2.0
4    3.0
dtype: float64

Copy to clipboard

On this page