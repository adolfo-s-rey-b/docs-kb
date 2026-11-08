[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.autocorrelation_plot.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.autocorrelation_plot.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.autocorrelation_plot.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.autocorrelation_plot.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.autocorrelation_plot.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.autocorrelation_plot.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.autocorrelation_plot.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.autocorrelation_plot.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.autocorrelation_plot.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.autocorrelation_plot.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.autocorrelation_plot.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.autocorrelation_plot.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.autocorrelation_plot.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.autocorrelation_plot.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.autocorrelation\_plot[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.autocorrelation_plot.html#pandas-plotting-autocorrelation-plot "Link to this heading")

=============================================================================================================================================================================================

pandas.plotting.autocorrelation\_plot(_series_, _ax\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L681-L729)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.autocorrelation_plot.html#pandas.plotting.autocorrelation_plot "Link to this definition")

Autocorrelation plot for time series.

This method generates an autocorrelation plot for a given time series, which helps to identify any periodic structure or correlation within the data across various lags. It shows the correlation of a time series with a delayed copy of itself as a function of delay. Autocorrelation plots are useful for checking randomness in a data set. If the data are random, the autocorrelations should be near zero for any and all time-lag separations. If the data are not random, then one or more of the autocorrelations will be significantly non-zero.

Parameters:

**series**Series

The time series to visualize.

**ax**Matplotlib axis object, optional

The matplotlib axis object to use.

**\*\*kwargs**

Options to pass to matplotlib plotting method.

Returns:

matplotlib.axes.Axes

The matplotlib axes containing the autocorrelation plot.

See also

`Series.autocorr`

Compute the lag-N autocorrelation for a Series.

`plotting.lag_plot`

Lag plot for time series.

Examples

The horizontal lines in the plot correspond to 95% and 99% confidence bands.

The dashed line is 99% confidence band.

\>>> spacing \= np.linspace(\-9 \* np.pi, 9 \* np.pi, num\=1000)
\>>> rng \= np.random.default\_rng(42)
\>>> s \= pd.Series(0.7 \* rng.random(1000) + 0.3 \* np.sin(spacing))
\>>> pd.plotting.autocorrelation\_plot(s)

Copy to clipboard

![../../_images/pandas-plotting-autocorrelation_plot-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-autocorrelation_plot-1.png)

On this page