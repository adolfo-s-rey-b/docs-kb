[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.deregister_matplotlib_converters.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.deregister\_matplotlib\_converters[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.deregister_matplotlib_converters.html#pandas-plotting-deregister-matplotlib-converters "Link to this heading")

==================================================================================================================================================================================================================================

pandas.plotting.deregister\_matplotlib\_converters()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L132-L174)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.deregister_matplotlib_converters.html#pandas.plotting.deregister_matplotlib_converters "Link to this definition")

Remove pandas formatters and converters.

Removes the custom converters added by `register()`. This attempts to set the state of the registry back to the state before pandas registered its own units. Converters for pandas’ own types like Timestamp and Period are removed completely. Converters for types pandas overwrites, like `datetime.datetime`, are restored to their original value.

See also

[`register_matplotlib_converters`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html#pandas.plotting.register_matplotlib_converters "pandas.plotting.register_matplotlib_converters")

Register pandas formatters and converters with matplotlib.

Examples

The following line is done automatically by pandas so the plot can be rendered:

\>>> pd.plotting.register\_matplotlib\_converters()

Copy to clipboard

\>>> df \= pd.DataFrame(
...     {"ts": pd.period\_range("2020", periods\=2, freq\="M"), "y": \[1, 2\]}
... )
\>>> plot \= df.plot.line(x\="ts", y\="y")

Copy to clipboard

![../../_images/pandas-plotting-deregister_matplotlib_converters-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-deregister_matplotlib_converters-1.png)

Unsetting the register manually an error will be raised:

\>>> pd.set\_option(
...     "plotting.matplotlib.register\_converters", False
... )
\>>> df.plot.line(x\="ts", y\="y")
Traceback (most recent call last):
TypeError: float() argument must be a string or a real number, not 'Period'

Copy to clipboard

On this page