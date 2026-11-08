[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.register_matplotlib_converters.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.register_matplotlib_converters.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.register_matplotlib_converters.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.register_matplotlib_converters.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.register_matplotlib_converters.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.register_matplotlib_converters.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.register_matplotlib_converters.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.register_matplotlib_converters.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.register_matplotlib_converters.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.register_matplotlib_converters.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.register_matplotlib_converters.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.register_matplotlib_converters.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.register\_matplotlib\_converters[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html#pandas-plotting-register-matplotlib-converters "Link to this heading")

============================================================================================================================================================================================================================

pandas.plotting.register\_matplotlib\_converters()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L85-L129)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html#pandas.plotting.register_matplotlib_converters "Link to this definition")

Register pandas formatters and converters with matplotlib.

This function modifies the global `matplotlib.units.registry` dictionary. pandas adds custom converters for

*   pd.Timestamp
    
*   pd.Period
    
*   np.datetime64
    
*   datetime.datetime
    
*   datetime.date
    
*   datetime.time
    

See also

[`deregister_matplotlib_converters`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.deregister_matplotlib_converters.html#pandas.plotting.deregister_matplotlib_converters "pandas.plotting.deregister_matplotlib_converters")

Remove pandas formatters and converters.

Examples

The following line is done automatically by pandas so the plot can be rendered:

\>>> pd.plotting.register\_matplotlib\_converters()

Copy to clipboard

\>>> df \= pd.DataFrame(
...     {"ts": pd.period\_range("2020", periods\=2, freq\="M"), "y": \[1, 2\]}
... )
\>>> plot \= df.plot.line(x\="ts", y\="y")

Copy to clipboard

![../../_images/pandas-plotting-register_matplotlib_converters-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-register_matplotlib_converters-1.png)

Unsetting the register manually an error will be raised:

\>>> pd.set\_option(
...     "plotting.matplotlib.register\_converters", False
... )
\>>> df.plot.line(x\="ts", y\="y")
Traceback (most recent call last):
TypeError: float() argument must be a string or a real number, not 'Period'

Copy to clipboard

On this page