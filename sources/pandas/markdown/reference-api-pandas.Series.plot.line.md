[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.line.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.plot.line.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.line.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.plot.line.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.plot.line.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.plot.line.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.plot.line.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.plot.line.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.plot.line.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.plot.line.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.plot.line.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.plot.line.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.plot.line.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.plot.line.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.plot.line[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.line.html#pandas-series-plot-line "Link to this heading")

=====================================================================================================================================================

Series.plot.line(_x\=None_, _y\=None_, _color\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L1437-L1550)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.line.html#pandas.Series.plot.line "Link to this definition")

Make a line plot of a Series or DataFrame.

This function is useful to plot lines using DataFrame’s values as coordinates.

Parameters:

**x**label or position, optional

Allows plotting of one column versus another. If not specified, the index of the DataFrame is used.

**y**label or position, optional

Allows plotting of one column versus another. If not specified, all numerical columns are used.

**color**str, array-like, or dict, optional

The color for each of the DataFrame’s columns. Possible values are:

*   A single color string referred to by name, RGB or RGBA code, for instance ‘red’ or ‘#a98d19’.
    
*   A sequence of color strings referred to by name, RGB or RGBA code, which will be used for each column recursively. For instance \[‘green’,’yellow’\] each column’s line will be filled in green or yellow, alternatively. If there is only a single column to be plotted, then only the first color from the color list will be used.
    
*   A dict of the form {column name : color}, so that each column will be colored accordingly. For example, if your columns are called a and b, then passing {‘a’: ‘green’, ‘b’: ‘red’} will color lines for column a in green and lines for column b in red.
    

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `legend`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
. In addition, passing `x_compat=True` suppresses pandas’ automatic tick resolution adjustment for regular frequency time-series data in favor of the default matplotlib tick locators and formatters. See [Suppressing tick resolution adjustment](https://pandas.pydata.org/docs/user_guide/visualization.html#plotting-x-compat)
 for more.

Returns:

matplotlib.axes.Axes or numpy.ndarray of them

An ndarray of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
 is returned when `subplots=True`.

See also

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

[`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "(in Matplotlib v3.11.2)")

Plot y versus x as lines and/or markers.

Examples

\>>> s \= pd.Series(\[1, 3, 2\])
\>>> s.plot.line()

Copy to clipboard

![../../_images/pandas-Series-plot-line-1.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-line-1.png)

The following example shows the populations for some animals over the years.

\>>> df \= pd.DataFrame(
...     {
...         "pig": \[20, 18, 489, 675, 1776\],
...         "horse": \[4, 25, 281, 600, 1900\],
...     },
...     index\=\[1990, 1997, 2003, 2009, 2014\],
... )
\>>> lines \= df.plot.line()

Copy to clipboard

![../../_images/pandas-Series-plot-line-2.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-line-2.png)

An example with subplots, so an array of axes is returned.

\>>> axes \= df.plot.line(subplots\=True)
\>>> type(axes)
<class 'numpy.ndarray'>

Copy to clipboard

![../../_images/pandas-Series-plot-line-3.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-line-3.png)

Let’s repeat the same example, but specifying colors for each column (in this case, for each animal).

\>>> axes \= df.plot.line(
...     subplots\=True, color\={"pig": "pink", "horse": "#742802"}
... )

Copy to clipboard

![../../_images/pandas-Series-plot-line-4.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-line-4.png)

The following example shows the relationship between both populations.

\>>> lines \= df.plot.line(x\="pig", y\="horse")

Copy to clipboard

![../../_images/pandas-Series-plot-line-5.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-line-5.png)

On this page