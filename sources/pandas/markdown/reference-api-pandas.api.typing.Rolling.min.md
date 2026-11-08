[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.min.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.min[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.min.html#pandas-api-typing-rolling-min "Link to this heading")

=======================================================================================================================================================================

Rolling.min(_numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2566-L2632)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.min.html#pandas.api.typing.Rolling.min "Link to this definition")

Calculate the rolling minimum.

This is equivalent to applying `numpy.min` over each rolling window.

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

`Series.min`

Aggregating min for Series.

`DataFrame.min`

Aggregating min for DataFrame.

Notes

See [Numba engine](https://pandas.pydata.org/docs/user_guide/window.html#window-numba-engine)
 and [Numba (JIT compilation)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for extended documentation and performance considerations for the Numba engine.

Examples

Performing a rolling minimum with a window size of 3.

\>>> s \= pd.Series(\[4, 3, 5, 2, 6\])
\>>> s.rolling(3).min()
0    NaN
1    NaN
2    3.0
3    2.0
4    2.0
dtype: float64

Copy to clipboard

On this page