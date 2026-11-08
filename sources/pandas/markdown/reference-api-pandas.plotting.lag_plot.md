[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.lag_plot.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.lag\_plot[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.lag_plot.html#pandas-plotting-lag-plot "Link to this heading")

=========================================================================================================================================================

pandas.plotting.lag\_plot(_series_, _lag\=1_, _ax\=None_, _\*\*kwds_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L625-L678)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.lag_plot.html#pandas.plotting.lag_plot "Link to this definition")

Lag plot for time series.

A lag plot is a scatter plot of a time series against a lag of itself. It helps in visualizing the temporal dependence between observations by plotting the values at time t on the x-axis and the values at time t + lag on the y-axis.

Parameters:

**series**Series

The time series to visualize.

**lag**int, default 1

Lag length of the scatter plot.

**ax**Matplotlib axis object, optional

The matplotlib axis object to use.

**\*\*kwds**

Matplotlib scatter method keyword arguments.

Returns:

matplotlib.axes.Axes

The matplotlib Axes object containing the lag plot.

See also

`plotting.autocorrelation_plot`

Autocorrelation plot for time series.

[`matplotlib.pyplot.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "(in Matplotlib v3.11.2)")

A scatter plot of y vs. x with varying marker size and/or color in Matplotlib.

Examples

Lag plots are most commonly used to look for patterns in time series data.

Given the following time series

\>>> rng \= np.random.default\_rng(42)
\>>> x \= np.cumsum(rng.normal(loc\=1, scale\=5, size\=50))
\>>> s \= pd.Series(x)
\>>> s.plot()

Copy to clipboard

![../../_images/pandas-plotting-lag_plot-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-lag_plot-1.png)

A lag plot with `lag=1` returns

\>>> \_ \= pd.plotting.lag\_plot(s, lag\=1)

Copy to clipboard

![../../_images/pandas-plotting-lag_plot-2.png](https://pandas.pydata.org/docs/_images/pandas-plotting-lag_plot-2.png)

On this page