[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.mean.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.ExponentialMovingWindow.mean[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.mean.html#pandas-api-typing-exponentialmovingwindow-mean "Link to this heading")

==========================================================================================================================================================================================================================

ExponentialMovingWindow.mean(_numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/ewm.py#L536-L623)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.mean.html#pandas.api.typing.ExponentialMovingWindow.mean "Link to this definition")

Calculate the ewm (exponential weighted moment) mean.

The weighting is controlled by the `com`, `span`, `halflife`, or `alpha` parameter specified when calling `DataFrame.ewm()` or `Series.ewm()`.

Parameters:

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

`Series.ewm`

Calling ewm with Series data.

`DataFrame.ewm`

Calling ewm with DataFrames.

`Series.mean`

Aggregating mean for Series.

`DataFrame.mean`

Aggregating mean for DataFrame.

Notes

See [Numba engine](https://pandas.pydata.org/docs/user_guide/window.html#window-numba-engine)
 and [Numba (JIT compilation)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for extended documentation and performance considerations for the Numba engine.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4\])
\>>> ser.ewm(alpha\=0.2).mean()
0    1.000000
1    1.555556
2    2.147541
3    2.775068
dtype: float64

Copy to clipboard

On this page