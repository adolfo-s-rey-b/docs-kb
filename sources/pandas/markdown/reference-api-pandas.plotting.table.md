[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.table.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.table[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.table.html#pandas-plotting-table "Link to this heading")

===============================================================================================================================================

pandas.plotting.table(_ax_, _data_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L31-L82)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.table.html#pandas.plotting.table "Link to this definition")

Helper function to convert DataFrame and Series to matplotlib.table.

This method provides an easy way to visualize tabular data within a Matplotlib figure. It automatically extracts index and column labels from the DataFrame or Series, unless explicitly specified. This function is particularly useful when displaying summary tables alongside other plots or when creating static reports. It utilizes the matplotlib.pyplot.table backend and allows customization through various styling options available in Matplotlib.

Parameters:

**ax**Matplotlib axes object

The axes on which to draw the table.

**data**DataFrame or Series

Data for table contents.

**\*\*kwargs**

Keyword arguments to be passed to matplotlib.table.table. If rowLabels or colLabels is not specified, data index or column names will be used.

Returns:

matplotlib table object

The created table as a matplotlib Table object.

See also

`DataFrame.plot`

Make plots of DataFrame using matplotlib.

[`matplotlib.pyplot.table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table "(in Matplotlib v3.11.2)")

Create a table from data in a Matplotlib plot.

Examples

\>>> import matplotlib.pyplot as plt
\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> fig, ax \= plt.subplots()
\>>> ax.axis("off")
(np.float64(0.0), np.float64(1.0), np.float64(0.0), np.float64(1.0))
\>>> table \= pd.plotting.table(
...     ax, df, loc\="center", cellLoc\="center", colWidths\=\[0.2, 0.2\]
... )

Copy to clipboard

![../../_images/pandas-plotting-table-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-table-1.png)

On this page