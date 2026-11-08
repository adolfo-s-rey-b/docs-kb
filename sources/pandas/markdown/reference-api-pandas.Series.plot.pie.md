[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.plot.pie.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.plot.pie.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.plot.pie.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.plot.pie.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.plot.pie.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.plot.pie.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.plot.pie.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.plot.pie.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.plot.pie.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.plot.pie.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.plot.pie.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.plot.pie.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.plot.pie[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html#pandas-series-plot-pie "Link to this heading")

==================================================================================================================================================

Series.plot.pie(_y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L2183-L2242)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html#pandas.Series.plot.pie "Link to this definition")

Make a pie plot.

A pie plot is a proportional representation of the numerical data in a column. This function wraps `matplotlib.pyplot.pie()` for the specified column. If no column reference is passed and `subplots=True` a pie plot is drawn for each numerical column independently.

Parameters:

**y**int or label, optional

Label or position of the column to plot. If not provided, `subplots=True` argument must be passed.

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `legend`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
.

Returns:

matplotlib.axes.Axes or numpy.ndarray of them

An ndarray of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
 is returned when `subplots=True`.

See also

[`Series.plot.pie`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html#pandas.Series.plot.pie "pandas.Series.plot.pie")

Generate a pie plot for a Series.

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

Examples

In the example below we have a DataFrame with the information about planet’s mass and radius. We pass the ‘mass’ column to the pie function to get a pie plot.

\>>> df \= pd.DataFrame(
...     {"mass": \[0.330, 4.87, 5.97\], "radius": \[2439.7, 6051.8, 6378.1\]},
...     index\=\["Mercury", "Venus", "Earth"\],
... )
\>>> plot \= df.plot.pie(y\="mass", figsize\=(5, 5))

Copy to clipboard

![../../_images/pandas-Series-plot-pie-1.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-pie-1.png)

\>>> plot \= df.plot.pie(subplots\=True, figsize\=(11, 6))

Copy to clipboard

![../../_images/pandas-Series-plot-pie-2.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-pie-2.png)

On this page