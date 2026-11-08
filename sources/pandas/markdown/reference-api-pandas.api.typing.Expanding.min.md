[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.min.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.min.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.min.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.min.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.min.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.min.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.min.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.min.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.min.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.min.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.min.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.min.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.min.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.min.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.min[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.min.html#pandas-api-typing-expanding-min "Link to this heading")

=============================================================================================================================================================================

Expanding.min(_numeric\_only\=False_, _engine\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L566-L627)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.min.html#pandas.api.typing.Expanding.min "Link to this definition")

Calculate the expanding minimum.

At each point in time, returns the minimum value observed up to that point, respecting the `min_periods` threshold.

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

`Series.min`

Aggregating min for Series.

`DataFrame.min`

Aggregating min for DataFrame.

Notes

See [Numba engine](https://pandas.pydata.org/docs/user_guide/window.html#window-numba-engine)
 and [Numba (JIT compilation)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for extended documentation and performance considerations for the Numba engine.

Examples

\>>> ser \= pd.Series(\[2, 3, 4, 1\], index\=\["a", "b", "c", "d"\])
\>>> ser.expanding().min()
a    2.0
b    2.0
c    2.0
d    1.0
dtype: float64

Copy to clipboard

On this page