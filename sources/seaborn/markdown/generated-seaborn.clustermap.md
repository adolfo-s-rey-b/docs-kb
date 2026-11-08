 

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

seaborn.clustermap[#](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn-clustermap "Permalink to this heading")

===================================================================================================================================

seaborn.clustermap(_data_, _\*_, _pivot\_kws\=None_, _method\='average'_, _metric\='euclidean'_, _z\_score\=None_, _standard\_scale\=None_, _figsize\=(10, 10)_, _cbar\_kws\=None_, _row\_cluster\=True_, _col\_cluster\=True_, _row\_linkage\=None_, _col\_linkage\=None_, _row\_colors\=None_, _col\_colors\=None_, _mask\=None_, _dendrogram\_ratio\=0.2_, _colors\_ratio\=0.03_, _cbar\_pos\=(0.02, 0.8, 0.05, 0.18)_, _tree\_kws\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap "Permalink to this definition")

Plot a matrix dataset as a hierarchically-clustered heatmap.

This function requires scipy to be available.

Parameters:

**data**2D array-like

Rectangular data for clustering. Cannot contain NAs.

**pivot\_kws**dict, optional

If `data` is a tidy dataframe, can provide keyword arguments for pivot to create a rectangular dataframe.

**method**str, optional

Linkage method to use for calculating clusters. See [`scipy.cluster.hierarchy.linkage()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage "(in SciPy v1.12.0)")
 documentation for more information.

**metric**str, optional

Distance metric to use for the data. See [`scipy.spatial.distance.pdist()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist "(in SciPy v1.12.0)")
 documentation for more options. To use different metrics (or methods) for rows and columns, you may construct each linkage matrix yourself and provide them as `{row,col}_linkage`.

**z\_score**int or None, optional

Either 0 (rows) or 1 (columns). Whether or not to calculate z-scores for the rows or the columns. Z scores are: z = (x - mean)/std, so values in each row (column) will get the mean of the row (column) subtracted, then divided by the standard deviation of the row (column). This ensures that each row (column) has mean of 0 and variance of 1.

**standard\_scale**int or None, optional

Either 0 (rows) or 1 (columns). Whether or not to standardize that dimension, meaning for each row or column, subtract the minimum and divide each by its maximum.

**figsize**tuple of (width, height), optional

Overall size of the figure.

**cbar\_kws**dict, optional

Keyword arguments to pass to `cbar_kws` in [`heatmap()`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")
, e.g. to add a label to the colorbar.

**{row,col}\_cluster**bool, optional

If `True`, cluster the {rows, columns}.

**{row,col}\_linkage**[`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
, optional

Precomputed linkage matrix for the rows or columns. See [`scipy.cluster.hierarchy.linkage()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage "(in SciPy v1.12.0)")
 for specific formats.

**{row,col}\_colors**list-like or pandas DataFrame/Series, optional

List of colors to label for either the rows or columns. Useful to evaluate whether samples within a group are clustered together. Can use nested lists or DataFrame for multiple color levels of labeling. If given as a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
 or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "(in pandas v2.2.0)")
, labels for the colors are extracted from the DataFrames column names or from the name of the Series. DataFrame/Series colors are also matched to the data by their index, ensuring colors are drawn in the correct order.

**mask**bool array or DataFrame, optional

If passed, data will not be shown in cells where `mask` is True. Cells with missing values are automatically masked. Only used for visualizing, not for calculating.

**{dendrogram,colors}\_ratio**float, or pair of floats, optional

Proportion of the figure size devoted to the two marginal elements. If a pair is given, they correspond to (row, col) ratios.

**cbar\_pos**tuple of (left, bottom, width, height), optional

Position of the colorbar axes in the figure. Setting to `None` will disable the colorbar.

**tree\_kws**dict, optional

Parameters for the [`matplotlib.collections.LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "(in Matplotlib v3.8.2)")
 that is used to plot the lines of the dendrogram tree.

**kwargs**other keyword arguments

All other keyword arguments are passed to [`heatmap()`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")
.

Returns:

`ClusterGrid`

A `ClusterGrid` instance.

See also

[`heatmap`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")

Plot rectangular data as a color-encoded matrix.

Notes

The returned object has a `savefig` method that should be used if you want to save the figure object without clipping the dendrograms.

To access the reordered row indices, use: `clustergrid.dendrogram_row.reordered_ind`

Column indices, use: `clustergrid.dendrogram_col.reordered_ind`

Examples

Plot a heatmap with row and column clustering:

iris \= sns.load\_dataset("iris")
species \= iris.pop("species")
sns.clustermap(iris)

Copy to clipboard

![../_images/clustermap_1_0.png](https://seaborn.pydata.org/_images/clustermap_1_0.png)

Change the size and layout of the figure:

sns.clustermap(
    iris,
    figsize\=(7, 5),
    row\_cluster\=False,
    dendrogram\_ratio\=(.1, .2),
    cbar\_pos\=(0, .2, .03, .4)
)

Copy to clipboard

![../_images/clustermap_3_0.png](https://seaborn.pydata.org/_images/clustermap_3_0.png)

Add colored labels to identify observations:

lut \= dict(zip(species.unique(), "rbg"))
row\_colors \= species.map(lut)
sns.clustermap(iris, row\_colors\=row\_colors)

Copy to clipboard

![../_images/clustermap_5_0.png](https://seaborn.pydata.org/_images/clustermap_5_0.png)

Use a different colormap and adjust the limits of the color range:

sns.clustermap(iris, cmap\="mako", vmin\=0, vmax\=10)

Copy to clipboard

![../_images/clustermap_7_0.png](https://seaborn.pydata.org/_images/clustermap_7_0.png)

Use differente clustering parameters:

sns.clustermap(iris, metric\="correlation", method\="single")

Copy to clipboard

![../_images/clustermap_9_0.png](https://seaborn.pydata.org/_images/clustermap_9_0.png)

Standardize the data within the columns:

sns.clustermap(iris, standard\_scale\=1)

Copy to clipboard

![../_images/clustermap_11_0.png](https://seaborn.pydata.org/_images/clustermap_11_0.png)

Normalize the data within rows:

sns.clustermap(iris, z\_score\=0, cmap\="vlag", center\=0)

Copy to clipboard

![../_images/clustermap_13_0.png](https://seaborn.pydata.org/_images/clustermap_13_0.png)