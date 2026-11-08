[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.mean.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.mean[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.mean.html#pandas-api-typing-expanding-mean "Link to this heading")

================================================================================================================================================================================

Expanding.mean(_numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L629-L690)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.mean.html#pandas.api.typing.Expanding.mean "Link to this definition")

Calculate the expanding mean.

At each point in time, returns the arithmetic mean of all values observed up to that point, respecting the `min_periods` threshold.

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

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.mean`

Aggregating mean for Series.

`DataFrame.mean`

Aggregating mean for DataFrame.

Notes

See [Numba engine](https://pandas.pydata.org/docs/user_guide/window.html#window-numba-engine)
 and [Numba (JIT compilation)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for extended documentation and performance considerations for the Numba engine.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4\], index\=\["a", "b", "c", "d"\])
\>>> ser.expanding().mean()
a    1.0
b    1.5
c    2.0
d    2.5
dtype: float64

Copy to clipboard

On this page