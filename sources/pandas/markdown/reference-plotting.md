[Skip to main content](https://pandas.pydata.org/docs/reference/plotting.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/plotting.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/plotting.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/plotting.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/plotting.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/plotting.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/plotting.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/plotting.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/plotting.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/plotting.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/plotting.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/plotting.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/plotting.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/plotting.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Plotting[#](https://pandas.pydata.org/docs/reference/plotting.html#plotting "Link to this heading")

====================================================================================================

Note

For an overview, see [Chart visualization](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization)
.

The following functions are contained in the `pandas.plotting` module.

|     |     |
| --- | --- |
| [`andrews_curves`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html#pandas.plotting.andrews_curves "pandas.plotting.andrews_curves")<br>(frame, class\_column\[, ax, ...\]) | Generate a matplotlib plot for visualizing clusters of multivariate data. |
| [`autocorrelation_plot`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.autocorrelation_plot.html#pandas.plotting.autocorrelation_plot "pandas.plotting.autocorrelation_plot")<br>(series\[, ax\]) | Autocorrelation plot for time series. |
| [`bootstrap_plot`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.bootstrap_plot.html#pandas.plotting.bootstrap_plot "pandas.plotting.bootstrap_plot")<br>(series\[, fig, size, samples\]) | Bootstrap plot on mean, median and mid-range statistics. |
| [`boxplot`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.boxplot.html#pandas.plotting.boxplot "pandas.plotting.boxplot")<br>(data\[, column, by, ax, fontsize, ...\]) | Make a box plot from DataFrame columns. |
| [`deregister_matplotlib_converters`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.deregister_matplotlib_converters.html#pandas.plotting.deregister_matplotlib_converters "pandas.plotting.deregister_matplotlib_converters")<br>() | Remove pandas formatters and converters. |
| [`lag_plot`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.lag_plot.html#pandas.plotting.lag_plot "pandas.plotting.lag_plot")<br>(series\[, lag, ax\]) | Lag plot for time series. |
| [`parallel_coordinates`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.parallel_coordinates.html#pandas.plotting.parallel_coordinates "pandas.plotting.parallel_coordinates")<br>(frame, class\_column\[, ...\]) | Parallel coordinates plotting. |
| [`plot_params`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.plot_params.html#pandas.plotting.plot_params "pandas.plotting.plot_params") | Stores pandas plotting options. |
| [`radviz`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html#pandas.plotting.radviz "pandas.plotting.radviz")<br>(frame, class\_column\[, ax, color, ...\]) | Plot a multidimensional dataset in 2D. |
| [`register_matplotlib_converters`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.register_matplotlib_converters.html#pandas.plotting.register_matplotlib_converters "pandas.plotting.register_matplotlib_converters")<br>() | Register pandas formatters and converters with matplotlib. |
| [`scatter_matrix`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html#pandas.plotting.scatter_matrix "pandas.plotting.scatter_matrix")<br>(frame\[, alpha, figsize, ax, ...\]) | Draw a matrix of scatter plots. |
| [`table`](https://pandas.pydata.org/docs/reference/api/pandas.plotting.table.html#pandas.plotting.table "pandas.plotting.table")<br>(ax, data, \*\*kwargs) | Helper function to convert DataFrame and Series to matplotlib.table. |