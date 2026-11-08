[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.plot.barh.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.plot.barh.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.plot.barh.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.plot.barh.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.plot.barh.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.plot.barh.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.plot.barh.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.plot.barh.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.plot.barh.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.plot.barh.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.plot.barh.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.plot.barh.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.plot.barh[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html#pandas-dataframe-plot-barh "Link to this heading")

==============================================================================================================================================================

DataFrame.plot.barh(_x\=None_, _y\=None_, _color\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L1698-L1840)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html#pandas.DataFrame.plot.barh "Link to this definition")

Make a horizontal bar plot.

A horizontal bar plot is a plot that presents quantitative data with rectangular bars with lengths proportional to the values that they represent. A bar plot shows comparisons among discrete categories. One axis of the plot shows the specific categories being compared, and the other axis represents a measured value.

Parameters:

**x**label or position, optional

Allows plotting of one column versus another. If not specified, the index of the DataFrame is used.

**y**label or position, optional

Allows plotting of one column versus another. If not specified, all numerical columns are used.

**color**str, array-like, or dict, optional

The color for each of the DataFrame’s columns. Possible values are:

*   A single color string referred to by name, RGB or RGBA code, for instance ‘red’ or ‘#a98d19’.
    
*   A sequence of color strings referred to by name, RGB or RGBA code, which will be used for each column recursively. For instance \[‘green’,’yellow’\] each column’s bar will be filled in green or yellow, alternatively. If there is only a single column to be plotted, then only the first color from the color list will be used.
    
*   A dict of the form {column name : color}, so that each column will be colored accordingly. For example, if your columns are called a and b, then passing {‘a’: ‘green’, ‘b’: ‘red’} will color bars for column a in green and bars for column b in red.
    

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `legend`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
.

Returns:

matplotlib.axes.Axes or numpy.ndarray of them

An ndarray of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
 is returned when `subplots=True`.

See also

[`DataFrame.plot.bar`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html#pandas.DataFrame.plot.bar "pandas.DataFrame.plot.bar")

Vertical bar plot.

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

[`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "(in Matplotlib v3.11.2)")

Plot a vertical bar plot using matplotlib.

Examples

Basic example

\>>> df \= pd.DataFrame({"lab": \["A", "B", "C"\], "val": \[10, 30, 20\]})
\>>> ax \= df.plot.barh(x\="lab", y\="val")

Copy to clipboard

![../../_images/pandas-DataFrame-plot-barh-1.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-barh-1.png)

Plot a whole DataFrame to a horizontal bar plot

\>>> speed \= \[0.1, 17.5, 40, 48, 52, 69, 88\]
\>>> lifespan \= \[2, 8, 70, 1.5, 25, 12, 28\]
\>>> index \= \[\
...     "snail",\
...     "pig",\
...     "elephant",\
...     "rabbit",\
...     "giraffe",\
...     "coyote",\
...     "horse",\
... \]
\>>> df \= pd.DataFrame({"speed": speed, "lifespan": lifespan}, index\=index)
\>>> ax \= df.plot.barh()

Copy to clipboard

![../../_images/pandas-DataFrame-plot-barh-2.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-barh-2.png)

Plot stacked barh charts for the DataFrame

\>>> ax \= df.plot.barh(stacked\=True)

Copy to clipboard

![../../_images/pandas-DataFrame-plot-barh-3.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-barh-3.png)

We can specify colors for each column

\>>> ax \= df.plot.barh(color\={"speed": "red", "lifespan": "green"})

Copy to clipboard

![../../_images/pandas-DataFrame-plot-barh-4.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-barh-4.png)

Plot a column of the DataFrame to a horizontal bar plot

\>>> speed \= \[0.1, 17.5, 40, 48, 52, 69, 88\]
\>>> lifespan \= \[2, 8, 70, 1.5, 25, 12, 28\]
\>>> index \= \[\
...     "snail",\
...     "pig",\
...     "elephant",\
...     "rabbit",\
...     "giraffe",\
...     "coyote",\
...     "horse",\
... \]
\>>> df \= pd.DataFrame({"speed": speed, "lifespan": lifespan}, index\=index)
\>>> ax \= df.plot.barh(y\="speed")

Copy to clipboard

![../../_images/pandas-DataFrame-plot-barh-5.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-barh-5.png)

Plot DataFrame versus the desired column

\>>> speed \= \[0.1, 17.5, 40, 48, 52, 69, 88\]
\>>> lifespan \= \[2, 8, 70, 1.5, 25, 12, 28\]
\>>> index \= \[\
...     "snail",\
...     "pig",\
...     "elephant",\
...     "rabbit",\
...     "giraffe",\
...     "coyote",\
...     "horse",\
... \]
\>>> df \= pd.DataFrame({"speed": speed, "lifespan": lifespan}, index\=index)
\>>> ax \= df.plot.barh(x\="lifespan")

Copy to clipboard

![../../_images/pandas-DataFrame-plot-barh-6.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-barh-6.png)

On this page