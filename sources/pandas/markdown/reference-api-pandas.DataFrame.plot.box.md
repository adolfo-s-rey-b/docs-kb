[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.plot.box.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.plot.box.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.plot.box.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.plot.box.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.plot.box.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.plot.box.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.plot.box.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.plot.box.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.plot.box.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.plot.box.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.plot.box.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.plot.box.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.plot.box[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html#pandas-dataframe-plot-box "Link to this heading")

===========================================================================================================================================================

DataFrame.plot.box(_by\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L1842-L1905)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html#pandas.DataFrame.plot.box "Link to this definition")

Make a box plot of the DataFrame columns.

A box plot is a method for graphically depicting groups of numerical data through their quartiles. The box extends from the Q1 to Q3 quartile values of the data, with a line at the median (Q2). The whiskers extend from the edges of box to show the range of the data. The position of the whiskers is set by default to 1.5\*IQR (IQR = Q3 - Q1) from the edges of the box. Outlier points are those past the end of the whiskers.

For further details see Wikipedia’s entry for [boxplot](https://en.wikipedia.org/wiki/Box_plot)
.

A consideration when using this chart is that the box and the whiskers can overlap, which is very common when plotting small sets of data.

Parameters:

**by**str or sequence

Column in the DataFrame to group by.

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `grid`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
.

Returns:

matplotlib.axes.Axes or Series of them

A Series of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
 is returned when `subplots=True` or `by` is given.

See also

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

[`DataFrame.boxplot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html#pandas.DataFrame.boxplot "pandas.DataFrame.boxplot")

Another method to draw a box plot.

[`Series.plot.box`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.box.html#pandas.Series.plot.box "pandas.Series.plot.box")

Draw a box plot from a Series object.

[`matplotlib.pyplot.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "(in Matplotlib v3.11.2)")

Draw a box plot in matplotlib.

Examples

Draw a box plot from a DataFrame with four columns of randomly generated data.

\>>> data \= np.random.default\_rng(42).standard\_normal((25, 4))
\>>> df \= pd.DataFrame(data, columns\=list("ABCD"))
\>>> ax \= df.plot.box()

Copy to clipboard

![../../_images/pandas-DataFrame-plot-box-1.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-box-1.png)

You can also generate groupings if you specify the by parameter (which can take a column name, or a list or tuple of column names):

\>>> age\_list \= \[8, 10, 12, 14, 72, 74, 76, 78, 20, 25, 30, 35, 60, 85\]
\>>> df \= pd.DataFrame({"gender": list("MMMMMMMMFFFFFF"), "age": age\_list})
\>>> ax \= df.plot.box(column\="age", by\="gender", figsize\=(10, 8))

Copy to clipboard

![../../_images/pandas-DataFrame-plot-box-2.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-box-2.png)

On this page