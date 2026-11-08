[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.scatter_matrix.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.scatter_matrix.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.scatter_matrix.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.scatter_matrix.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.scatter_matrix.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.scatter_matrix.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.scatter_matrix.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.scatter_matrix.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.scatter_matrix.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.scatter_matrix.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.scatter_matrix.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.scatter_matrix.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.scatter\_matrix[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html#pandas-plotting-scatter-matrix "Link to this heading")

===========================================================================================================================================================================

pandas.plotting.scatter\_matrix(_frame_, _alpha\=0.5_, _figsize\=None_, _ax\=None_, _grid\=False_, _diagonal\='hist'_, _marker\='.'_, _density\_kwds\=None_, _hist\_kwds\=None_, _range\_padding\=0.05_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L177-L271)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html#pandas.plotting.scatter_matrix "Link to this definition")

Draw a matrix of scatter plots.

Each pair of numeric columns in the DataFrame is plotted against each other, resulting in a matrix of scatter plots. The diagonal plots can display either histograms or Kernel Density Estimation (KDE) plots for each variable.

Parameters:

**frame**DataFrame

The data to be plotted.

**alpha**float, optional

Amount of transparency applied.

**figsize**(float,float), optional

A tuple (width, height) in inches.

**ax**Matplotlib axis object, optional

An existing Matplotlib axis object for the plots. If None, a new axis is created.

**grid**bool, optional

Setting this to True will show the grid.

**diagonal**{‘hist’, ‘kde’}

Pick between ‘kde’ and ‘hist’ for either Kernel Density Estimation or Histogram plot in the diagonal.

**marker**str, optional

Matplotlib marker type, default ‘.’.

**density\_kwds**keywords

Keyword arguments to be passed to kernel density estimate plot.

**hist\_kwds**keywords

Keyword arguments to be passed to hist function.

**range\_padding**float, default 0.05

Relative extension of axis range in x and y with respect to (x\_max - x\_min) or (y\_max - y\_min).

**\*\*kwargs**

Keyword arguments to be passed to scatter function.

Returns:

numpy.ndarray

A matrix of scatter plots.

See also

`plotting.parallel_coordinates`

Plots parallel coordinates for multivariate data.

`plotting.andrews_curves`

Generates Andrews curves for visualizing clusters of multivariate data.

`plotting.radviz`

Creates a RadViz visualization.

`plotting.bootstrap_plot`

Visualizes uncertainty in data via bootstrap sampling.

Examples

\>>> data \= np.random.default\_rng(42).standard\_normal((1000, 4))
\>>> df \= pd.DataFrame(data, columns\=\["A", "B", "C", "D"\])
\>>> pd.plotting.scatter\_matrix(df, alpha\=0.2)
array(\[\[<Axes: xlabel='A', ylabel='A'>, <Axes: xlabel='B', ylabel='A'>,\
        <Axes: xlabel='C', ylabel='A'>, <Axes: xlabel='D', ylabel='A'>\],\
       \[<Axes: xlabel='A', ylabel='B'>, <Axes: xlabel='B', ylabel='B'>,\
        <Axes: xlabel='C', ylabel='B'>, <Axes: xlabel='D', ylabel='B'>\],\
       \[<Axes: xlabel='A', ylabel='C'>, <Axes: xlabel='B', ylabel='C'>,\
        <Axes: xlabel='C', ylabel='C'>, <Axes: xlabel='D', ylabel='C'>\],\
       \[<Axes: xlabel='A', ylabel='D'>, <Axes: xlabel='B', ylabel='D'>,\
        <Axes: xlabel='C', ylabel='D'>, <Axes: xlabel='D', ylabel='D'>\]\],
      dtype=object)

Copy to clipboard

![../../_images/pandas-plotting-scatter_matrix-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-scatter_matrix-1.png)

On this page