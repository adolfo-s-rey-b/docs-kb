[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.plot_params.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.plot_params.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.plot_params.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.plot_params.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.plot_params.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.plot_params.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.plot_params.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.plot_params.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.plot_params.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.plot_params.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.plot_params.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.plot_params.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.plot_params.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.plot_params.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.plot\_params[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.plot_params.html#pandas-plotting-plot-params "Link to this heading")

==================================================================================================================================================================

pandas.plotting.plot\_params \= {'xaxis.compat': False}[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.plot_params.html#pandas.plotting.plot_params "Link to this definition")

Stores pandas plotting options.

Allows for parameter aliasing so you can just use parameter names that are the same as the plot function parameters, but is stored in a canonical format that makes it easy to breakdown into groups later.

See also

`plotting.register_matplotlib_converters`

Register pandas formatters and converters with matplotlib.

`plotting.bootstrap_plot`

Bootstrap plot on mean, median and mid-range statistics.

`plotting.autocorrelation_plot`

Autocorrelation plot for time series.

`plotting.lag_plot`

Lag plot for time series.

Examples

\>>> rng \= np.random.default\_rng(42)
\>>> df \= pd.DataFrame(
...     {"A": rng.standard\_normal(10), "B": rng.standard\_normal(10)},
...     index\=pd.date\_range("1/1/2000", freq\="4MS", periods\=10),
... )
\>>> with pd.plotting.plot\_params.use("x\_compat", True):
...     \_ \= df\["A"\].plot(color\="r")
...     \_ \= df\["B"\].plot(color\="g")

Copy to clipboard

![../../_images/pandas-plotting-plot_params-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-plot_params-1.png)

On this page