[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.bootstrap\_plot[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html#pandas-plotting-bootstrap-plot "Link to this heading")

===========================================================================================================================================================================

pandas.plotting.bootstrap\_plot(_series_, _fig\=None_, _size\=50_, _samples\=500_, _\*\*kwds_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L455-L514)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html#pandas.plotting.bootstrap_plot "Link to this definition")

Bootstrap plot on mean, median and mid-range statistics.

The bootstrap plot is used to estimate the uncertainty of a statistic by relying on random sampling with replacement [\[1\]](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html#r11075647b7c8-1)
. This function will generate bootstrapping plots for mean, median and mid-range statistics for the given number of samples of the given size.

\[[1](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html#id1)\
\]

“Bootstrapping (statistics)” in [https://en.wikipedia.org/wiki/Bootstrapping\_%28statistics%29](https://en.wikipedia.org/wiki/Bootstrapping_%28statistics%29)

Parameters:

**series**pandas.Series

Series from where to get the samplings for the bootstrapping.

**fig**matplotlib.figure.Figure, default None

If given, it will use the fig reference for plotting instead of creating a new one with default parameters.

**size**int, default 50

Number of data points to consider during each sampling. It must be less than or equal to the length of the series.

**samples**int, default 500

Number of times the bootstrap procedure is performed.

**\*\*kwds**

Options to pass to matplotlib plotting method.

Returns:

matplotlib.figure.Figure

Matplotlib figure.

See also

`DataFrame.plot`

Basic plotting for DataFrame objects.

`Series.plot`

Basic plotting for Series objects.

Examples

This example draws a basic bootstrap plot for a Series.

\>>> rng \= np.random.default\_rng(42)
\>>> s \= pd.Series(rng.uniform(size\=100))
\>>> pd.plotting.bootstrap\_plot(s)
<Figure size 640x480 with 6 Axes>

Copy to clipboard

![../../_images/pandas-plotting-bootstrap_plot-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-bootstrap_plot-1.png)

On this page