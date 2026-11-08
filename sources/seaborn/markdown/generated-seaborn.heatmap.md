 

 Ctrl+K

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
    
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
    
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
    
*   [API](https://seaborn.pydata.org/api.html)
    
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
    
*   [Citing](https://seaborn.pydata.org/citing.html)
    
*   [FAQ](https://seaborn.pydata.org/faq.html)
    

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
    
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
    
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")
    

On this page

seaborn.heatmap[#](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn-heatmap "Permalink to this heading")

==========================================================================================================================

seaborn.heatmap(_data_, _\*_, _vmin\=None_, _vmax\=None_, _cmap\=None_, _center\=None_, _robust\=False_, _annot\=None_, _fmt\='.2g'_, _annot\_kws\=None_, _linewidths\=0_, _linecolor\='white'_, _cbar\=True_, _cbar\_kws\=None_, _cbar\_ax\=None_, _square\=False_, _xticklabels\='auto'_, _yticklabels\='auto'_, _mask\=None_, _ax\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "Permalink to this definition")

Plot rectangular data as a color-encoded matrix.

This is an Axes-level function and will draw the heatmap into the currently-active Axes if none is provided to the `ax` argument. Part of this Axes space will be taken and used to plot a colormap, unless `cbar` is False or a separate Axes is provided to `cbar_ax`.

Parameters:

**data**rectangular dataset

2D dataset that can be coerced into an ndarray. If a Pandas DataFrame is provided, the index/column information will be used to label the columns and rows.

**vmin, vmax**floats, optional

Values to anchor the colormap, otherwise they are inferred from the data and other keyword arguments.

**cmap**matplotlib colormap name or object, or list of colors, optional

The mapping from data values to color space. If not provided, the default will depend on whether `center` is set.

**center**float, optional

The value at which to center the colormap when plotting divergent data. Using this parameter will change the default `cmap` if none is specified.

**robust**bool, optional

If True and `vmin` or `vmax` are absent, the colormap range is computed with robust quantiles instead of the extreme values.

**annot**bool or rectangular dataset, optional

If True, write the data value in each cell. If an array-like with the same shape as `data`, then use this to annotate the heatmap instead of the data. Note that DataFrames will match on position, not index.

**fmt**str, optional

String formatting code to use when adding annotations.

**annot\_kws**dict of key, value mappings, optional

Keyword arguments for [`matplotlib.axes.Axes.text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "(in Matplotlib v3.8.2)")
 when `annot` is True.

**linewidths**float, optional

Width of the lines that will divide each cell.

**linecolor**color, optional

Color of the lines that will divide each cell.

**cbar**bool, optional

Whether to draw a colorbar.

**cbar\_kws**dict of key, value mappings, optional

Keyword arguments for [`matplotlib.figure.Figure.colorbar()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.colorbar "(in Matplotlib v3.8.2)")
.

**cbar\_ax**matplotlib Axes, optional

Axes in which to draw the colorbar, otherwise take space from the main Axes.

**square**bool, optional

If True, set the Axes aspect to “equal” so each cell will be square-shaped.

**xticklabels, yticklabels**“auto”, bool, list-like, or int, optional

If True, plot the column names of the dataframe. If False, don’t plot the column names. If list-like, plot these alternate labels as the xticklabels. If an integer, use the column names but plot only every n label. If “auto”, try to densely plot non-overlapping labels.

**mask**bool array or DataFrame, optional

If passed, data will not be shown in cells where `mask` is True. Cells with missing values are automatically masked.

**ax**matplotlib Axes, optional

Axes in which to draw the plot, otherwise use the currently-active Axes.

**kwargs**other keyword arguments

All other keyword arguments are passed to [`matplotlib.axes.Axes.pcolormesh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "(in Matplotlib v3.8.2)")
.

Returns:

**ax**matplotlib Axes

Axes object with the heatmap.

See also

[`clustermap`](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap "seaborn.clustermap")

Plot a matrix using hierarchical clustering to arrange the rows and columns.

Examples

Pass a `DataFrame` to plot with indices as row/column labels:

glue \= sns.load\_dataset("glue").pivot(index\="Model", columns\="Task", values\="Score")
sns.heatmap(glue)

Copy to clipboard

![../_images/heatmap_1_0.png](https://seaborn.pydata.org/_images/heatmap_1_0.png)

Use `annot` to represent the cell values with text:

sns.heatmap(glue, annot\=True)

Copy to clipboard

![../_images/heatmap_3_0.png](https://seaborn.pydata.org/_images/heatmap_3_0.png)

Control the annotations with a formatting string:

sns.heatmap(glue, annot\=True, fmt\=".1f")

Copy to clipboard

![../_images/heatmap_5_0.png](https://seaborn.pydata.org/_images/heatmap_5_0.png)

Use a separate dataframe for the annotations:

sns.heatmap(glue, annot\=glue.rank(axis\="columns"))

Copy to clipboard

![../_images/heatmap_7_0.png](https://seaborn.pydata.org/_images/heatmap_7_0.png)

Add lines between cells:

sns.heatmap(glue, annot\=True, linewidth\=.5)

Copy to clipboard

![../_images/heatmap_9_0.png](https://seaborn.pydata.org/_images/heatmap_9_0.png)

Select a different colormap by name:

sns.heatmap(glue, cmap\="crest")

Copy to clipboard

![../_images/heatmap_11_0.png](https://seaborn.pydata.org/_images/heatmap_11_0.png)

Or pass a colormap object:

sns.heatmap(glue, cmap\=sns.cubehelix\_palette(as\_cmap\=True))

Copy to clipboard

![../_images/heatmap_13_0.png](https://seaborn.pydata.org/_images/heatmap_13_0.png)

Set the colormap norm (data values corresponding to minimum and maximum points):

sns.heatmap(glue, vmin\=50, vmax\=100)

Copy to clipboard

![../_images/heatmap_15_0.png](https://seaborn.pydata.org/_images/heatmap_15_0.png)

Use methods on the [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")
 object to tweak the plot:

ax \= sns.heatmap(glue, annot\=True)
ax.set(xlabel\="", ylabel\="")
ax.xaxis.tick\_top()

Copy to clipboard

![../_images/heatmap_17_0.png](https://seaborn.pydata.org/_images/heatmap_17_0.png)