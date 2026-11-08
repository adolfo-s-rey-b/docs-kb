[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.area.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.plot.area.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.area.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.plot.area.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.plot.area.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.plot.area.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.plot.area.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.plot.area.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.plot.area.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.plot.area.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.plot.area.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.plot.area.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.plot.area.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.plot.area.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.plot.area[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.area.html#pandas-series-plot-area "Link to this heading")

=====================================================================================================================================================

Series.plot.area(_x\=None_, _y\=None_, _stacked\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L2096-L2181)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.area.html#pandas.Series.plot.area "Link to this definition")

Make a stacked area plot.

An area plot displays quantitative data visually. This function wraps the matplotlib area function.

Parameters:

**x**label or position, optional

Coordinates for the X axis. By default uses the index.

**y**label or position, optional

Column to plot. By default uses all columns.

**stacked**bool, default True

Area plots are stacked by default. Set to False to create a unstacked plot.

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `legend`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
.

Returns:

matplotlib.axes.Axes or numpy.ndarray of them

An ndarray of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
 is returned when `subplots=True`.

See also

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

Examples

Draw an area plot based on basic business metrics:

\>>> df \= pd.DataFrame(
...     {
...         "sales": \[3, 2, 3, 9, 10, 6\],
...         "signups": \[5, 5, 6, 12, 14, 13\],
...         "visits": \[20, 42, 28, 62, 81, 50\],
...     },
...     index\=pd.date\_range(
...         start\="2018/01/01", end\="2018/07/01", freq\="ME"
...     ),
... )
\>>> ax \= df.plot.area()

Copy to clipboard

![../../_images/pandas-Series-plot-area-1.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-area-1.png)

Area plots are stacked by default. To produce an unstacked plot, pass `stacked=False`:

\>>> ax \= df.plot.area(stacked\=False)

Copy to clipboard

![../../_images/pandas-Series-plot-area-2.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-area-2.png)

Draw an area plot for a single column:

\>>> ax \= df.plot.area(y\="sales")

Copy to clipboard

![../../_images/pandas-Series-plot-area-3.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-area-3.png)

Draw with a different x:

\>>> df \= pd.DataFrame(
...     {
...         "sales": \[3, 2, 3\],
...         "visits": \[20, 42, 28\],
...         "day": \[1, 2, 3\],
...     }
... )
\>>> ax \= df.plot.area(x\="day")

Copy to clipboard

![../../_images/pandas-Series-plot-area-4.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-area-4.png)

On this page