[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

matplotlib.axes.Axes.hist2d[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib-axes-axes-hist2d "Link to this heading")

==============================================================================================================================================================

Axes.hist2d(_x_, _y_, _bins\=10_, _\*_, _range\=None_, _density\=False_, _weights\=None_, _cmin\=None_, _cmax\=None_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L7791-L7899)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "Link to this definition")

Make a 2D histogram plot.

Parameters:

**x, y**array-like, shape (n, )

Input values

**bins**None or int or \[int, int\] or array-like or \[array, array\]

The bin specification:

*   If int, the number of bins for the two dimensions (`nx = ny = bins`).
    
*   If `[int, int]`, the number of bins in each dimension (`nx, ny = bins`).
    
*   If array-like, the bin edges for the two dimensions (`x_edges = y_edges = bins`).
    
*   If `[array, array]`, the bin edges in each dimension (`x_edges, y_edges = bins`).
    

The default value is 10.

**range**array-like shape(2, 2), optional

The leftmost and rightmost edges of the bins along each dimension (if not specified explicitly in the bins parameters): `[[xmin, xmax], [ymin, ymax]]`. All values outside of this range will be considered outliers and not tallied in the histogram.

**density**bool, default: False

Normalize histogram. See the documentation for the _density_ parameter of [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 for more details.

**weights**array-like, shape (n, ), optional

An array of values w\_i weighing each sample (x\_i, y\_i).

**cmin, cmax**float, default: None

All bins that has count less than _cmin_ or more than _cmax_ will not be displayed (set to NaN before passing to [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
) and these count values in the return value count histogram will also be set to nan upon return.

Returns:

**h**2D array

The bi-dimensional histogram of samples x and y. Values in x are histogrammed along the first dimension and values in y are histogrammed along the second dimension.

**xedges**1D array

The bin edges along the x-axis.

**yedges**1D array

The bin edges along the y-axis.

**image**[`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")

Other Parameters:

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

**norm**str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
, optional

The normalization method used to scale scalar data to the \[0, 1\] range before mapping to colors using _cmap_. By default, a linear scaling is used, mapping the lowest value to 0 and the highest to 1.

If given, this can be one of the following:

*   An instance of [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     or one of its subclasses (see [Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)
    ).
    
*   A scale name, i.e. one of "linear", "log", "symlog", "logit", etc. For a list of available scales, call [`matplotlib.scale.get_scale_names()`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.get_scale_names "matplotlib.scale.get_scale_names")
    . In that case, a suitable [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     subclass is dynamically generated and instantiated.
    

**vmin, vmax**float, optional

When using scalar data and no explicit _norm_, _vmin_ and _vmax_ define the data range that the colormap covers. By default, the colormap covers the complete value range of the supplied data. It is an error to use _vmin_/_vmax_ when a _norm_ instance is given (but using a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 _norm_ name together with _vmin_/_vmax_ is acceptable).

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

**alpha**`0 <= scalar <= 1` or `None`, optional

The alpha blending value.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_x_, _y_, _weights_

**\*\*kwargs**

Additional parameters are passed along to the [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 method and [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 constructor.

See also

[`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")

1D histogram plotting

[`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")

2D histogram with hexagonal bins

Notes

Rendering the histogram with a logarithmic color scale is accomplished by passing a [`colors.LogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
 instance to the _norm_ keyword argument. Likewise, power-law normalization (similar in effect to gamma correction) can be accomplished with [`colors.PowerNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")
.

Changed in version 3.11: Previously, [`hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
 would force the axes limits to match the extents of the histogram; now, autoscaling also takes other plot elements into account.

Examples using `matplotlib.axes.Axes.hist2d`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#examples-using-matplotlib-axes-axes-hist2d "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_hist_thumb.png)

[Histograms](https://matplotlib.org/stable/gallery/statistics/hist.html)

Histograms

![](https://matplotlib.org/stable/_images/sphx_glr_power_norm_thumb.png)

[Exploring normalizations](https://matplotlib.org/stable/gallery/scales/power_norm.html)

Exploring normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_hist2d_thumb.png)

[hist2d(x, y)](https://matplotlib.org/stable/plot_types/stats/hist2d.html)

hist2d(x, y)

On this page