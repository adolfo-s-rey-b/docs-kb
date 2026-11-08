[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#main-content)

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
    

matplotlib.axes.Axes.hist[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib-axes-axes-hist "Link to this heading")

========================================================================================================================================================

Axes.hist(_x_, _bins\=None_, _\*_, _range\=None_, _density\=False_, _weights\=None_, _cumulative\=False_, _bottom\=None_, _histtype\='bar'_, _align\='mid'_, _orientation\='vertical'_, _rwidth\=None_, _log\=False_, _color\=None_, _label\=None_, _stacked\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L7193-L7688)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "Link to this definition")

Compute and plot a histogram.

This method uses [`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "(in NumPy v2.5)")
 to bin the data in _x_ and count the number of values in each bin, then draws the distribution either as a [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 or [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
. The _bins_, _range_, _density_, and _weights_ parameters are forwarded to [`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "(in NumPy v2.5)")
.

If the data has already been binned and counted, use [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 or [`stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs")
 to plot the distribution:

counts, bins \= np.histogram(x)
plt.stairs(counts, bins)

Alternatively, plot pre-computed bins and counts using `hist()` by treating each bin as a single point with a weight equal to its count:

plt.hist(bins\[:\-1\], bins, weights\=counts)

The data input _x_ can be a singular array, a list of datasets of potentially different lengths (\[_x0_, _x1_, ...\]), or a 2D ndarray in which each column is a dataset. Note that the ndarray form is transposed relative to the list form. If the input is an array, then the return value is a tuple (_n_, _bins_, _patches_); if the input is a sequence of arrays, then the return value is a tuple (\[_n0_, _n1_, ...\], _bins_, \[_patches0_, _patches1_, ...\]).

Masked arrays are not supported.

Parameters:

**x**(n,) array or sequence of (n,) arrays

Input values, this takes either a single array or a sequence of arrays which are not required to be of the same length.

**bins**int or sequence or str, default: `[rcParams["hist.bins"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=hist.bins#rcparam-hist-bins) ` (default: `10`)

If _bins_ is an integer, it defines the number of equal-width bins in the range.

If _bins_ is a sequence, it defines the bin edges, including the left edge of the first bin and the right edge of the last bin; in this case, bins may be unequally spaced. All but the last (righthand-most) bin is half-open. In other words, if _bins_ is:

\[1, 2, 3, 4\]

then the first bin is `[1, 2)` (including 1, but excluding 2) and the second `[2, 3)`. The last bin, however, is `[3, 4]`, which _includes_ 4.\
\
If _bins_ is a string, it is one of the binning strategies supported by [`numpy.histogram_bin_edges`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "(in NumPy v2.5)")\
: 'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', or 'sqrt'.\
\
**range**tuple or None, default: None\
\
The lower and upper range of the bins. Lower and upper outliers are ignored. If not provided, _range_ is `(x.min(), x.max())`. Range has no effect if _bins_ is a sequence.\
\
If _bins_ is a sequence or _range_ is specified, autoscaling is based on the specified bin range instead of the range of x.\
\
**density**bool, default: False\
\
If `True`, draw and return a probability density: each bin will display the bin's raw count divided by the total number of counts _and the bin width_ (`density = counts / (sum(counts) * np.diff(bins))`), so that the area under the histogram integrates to 1 (`np.sum(density * np.diff(bins)) == 1`).\
\
If _stacked_ is also `True`, the sum of the histograms is normalized to 1.\
\
**weights**(n,) array-like or None, default: None\
\
An array of weights, of the same shape as _x_. Each value in _x_ only contributes its associated weight towards the bin count (instead of 1). If _density_ is `True`, the weights are normalized, so that the integral of the density over the range remains 1.\
\
**cumulative**bool or -1, default: False\
\
If `True`, then a histogram is computed where each bin gives the counts in that bin plus all bins for smaller values. The last bin gives the total number of datapoints.\
\
If _density_ is also `True` then the histogram is normalized such that the last bin equals 1.\
\
If _cumulative_ is a number less than 0 (e.g., -1), the direction of accumulation is reversed. In this case, if _density_ is also `True`, then the histogram is normalized such that the first bin equals 1.\
\
**bottom**array-like or float, default: 0\
\
Location of the bottom of each bin, i.e. bins are drawn from `bottom` to `bottom + hist(x, bins)` If a scalar, the bottom of each bin is shifted by the same amount. If an array, each bin is shifted independently and the length of bottom must match the number of bins. If None, defaults to 0.\
\
**histtype**{'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'\
\
The type of histogram to draw.\
\
*   'bar' is a traditional bar-type histogram. If multiple data are given the bars are arranged side by side.\
    \
*   'barstacked' is a bar-type histogram where multiple data are stacked on top of each other.\
    \
*   'step' generates a lineplot that is by default unfilled.\
    \
*   'stepfilled' generates a lineplot that is by default filled.\
    \
\
**align**{'left', 'mid', 'right'}, default: 'mid'\
\
The horizontal alignment of the histogram bars.\
\
*   'left': bars are centered on the left bin edges.\
    \
*   'mid': bars are centered between the bin edges.\
    \
*   'right': bars are centered on the right bin edges.\
    \
\
**orientation**{'vertical', 'horizontal'}, default: 'vertical'\
\
If 'horizontal', [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")\
 will be used for bar-type histograms and the _bottom_ kwarg will be the left edges.\
\
**rwidth**float or None, default: None\
\
The relative width of the bars as a fraction of the bin width. If `None`, automatically compute the width.\
\
Ignored if _histtype_ is 'step' or 'stepfilled'.\
\
**log**bool, default: False\
\
If `True`, the histogram axis will be set to a log scale.\
\
**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)\
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)\
 or None, default: None\
\
Color or sequence of colors, one per dataset. Default (`None`) uses the standard line color sequence.\
\
Added in version 3.10: It is now possible to use a single color with multiple datasets.\
\
**label**str or list of str, optional\
\
String, or sequence of strings to match multiple datasets. Bar charts yield multiple patches per dataset, but only the first gets the label, so that [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")\
 will work as expected.\
\
**stacked**bool, default: False\
\
If `True`, multiple data are stacked on top of each other If `False` multiple data are arranged side by side if histtype is 'bar' or on top of each other if histtype is 'step'\
\
Returns:\
\
**n**array or list of arrays\
\
The values of the histogram bins. See _density_ and _weights_ for a description of the possible semantics. If input _x_ is an array, then this is an array of length _nbins_. If input is a sequence of arrays `[data1, data2, ...]`, then this is a list of arrays with the values of the histograms for each of the arrays in the same order. The dtype of the array _n_ (or of its element arrays) will always be float even if no weighting or normalization is used.\
\
**bins**array\
\
The edges of the bins. Length nbins + 1 (nbins left edges and right edge of last bin). Always a single array even when multiple data sets are passed in.\
\
**patches**[`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
 or list of a single [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")\
 or list of such objects\
\
Container of individual artists used to create the histogram or list of such containers if there are multiple input datasets.\
\
Other Parameters:\
\
**data**indexable object, optional\
\
If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:\
\
_x_, _weights_\
\
**\*\*kwargs**\
\
[`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
 properties. The following properties additionally accept a sequence of values corresponding to the datasets in _x_: _edgecolor_, _facecolor_, _linewidth_, _linestyle_, _hatch_.\
\
Added in version 3.10: Allowing sequences of values in above listed Patch properties.\
\
See also\
\
[`hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")\
\
2D histogram with rectangular bins\
\
[`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")\
\
2D histogram with hexagonal bins\
\
[`stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs")\
\
Plot a pre-computed histogram\
\
[`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")\
\
Plot a pre-computed histogram\
\
Notes\
\
For large numbers of bins (>1000), plotting can be significantly accelerated by using [`stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs")\
 to plot a pre-computed histogram (`plt.stairs(*np.histogram(data))`), or by setting _histtype_ to 'step' or 'stepfilled' rather than 'bar' or 'barstacked'.\
\
Examples using `matplotlib.axes.Axes.hist`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#examples-using-matplotlib-axes-axes-hist "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_thumb.png)\
\
[Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)\
\
Scatter plot with histograms\
\
![](https://matplotlib.org/stable/_images/sphx_glr_hist_thumb.png)\
\
[Histograms](https://matplotlib.org/stable/gallery/statistics/hist.html)\
\
Histograms\
\
![](https://matplotlib.org/stable/_images/sphx_glr_histogram_histtypes_thumb.png)\
\
[Demo of the histogram function's different histtype settings](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html)\
\
Demo of the histogram function's different histtype settings\
\
![](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_thumb.png)\
\
[Histogram bins, density, and weight](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html)\
\
Histogram bins, density, and weight\
\
![](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_thumb.png)\
\
[The histogram (hist) function with multiple data sets](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html)\
\
The histogram (hist) function with multiple data sets\
\
![](https://matplotlib.org/stable/_images/sphx_glr_histogram_bihistogram_thumb.png)\
\
[Bihistogram](https://matplotlib.org/stable/gallery/statistics/histogram_bihistogram.html)\
\
Bihistogram\
\
![](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_thumb.png)\
\
[Cumulative distributions](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html)\
\
Cumulative distributions\
\
![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)\
\
[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)\
\
Axes Demo\
\
![](https://matplotlib.org/stable/_images/sphx_glr_placing_text_boxes_thumb.png)\
\
[Placing text boxes](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html)\
\
Placing text boxes\
\
![](https://matplotlib.org/stable/_images/sphx_glr_bmh_thumb.png)\
\
[Bayesian Methods for Hackers style sheet](https://matplotlib.org/stable/gallery/style_sheets/bmh.html)\
\
Bayesian Methods for Hackers style sheet\
\
![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_locatable_axes_thumb.png)\
\
[Align histogram to scatter plot using locatable Axes](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html)\
\
Align histogram to scatter plot using locatable Axes\
\
![](https://matplotlib.org/stable/_images/sphx_glr_animated_histogram_thumb.gif)\
\
[Animated histogram](https://matplotlib.org/stable/gallery/animation/animated_histogram.html)\
\
Animated histogram\
\
![](https://matplotlib.org/stable/_images/sphx_glr_histogram_path_thumb.png)\
\
[Building histograms using Rectangles and PolyCollections](https://matplotlib.org/stable/gallery/misc/histogram_path.html)\
\
Building histograms using Rectangles and PolyCollections\
\
![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)\
\
[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)\
\
Artist tutorial\
\
![](https://matplotlib.org/stable/_images/sphx_glr_hist_plot_thumb.png)\
\
[hist(x)](https://matplotlib.org/stable/plot_types/stats/hist_plot.html)\
\
hist(x)\
\
![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)\
\
[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)\
\
Quick start guide\
\
![](https://matplotlib.org/stable/_images/sphx_glr_paths_thumb.png)\
\
[Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html)\
\
Path Tutorial\
\
![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)\
\
[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)\
\
Transformations Tutorial\
\
On this page