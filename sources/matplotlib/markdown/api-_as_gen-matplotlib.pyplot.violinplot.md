[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#main-content)

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
    

matplotlib.pyplot.violinplot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib-pyplot-violinplot "Link to this heading")

=================================================================================================================================================================

matplotlib.pyplot.violinplot(_dataset_, _positions\=None_, _\*_, _vert\=None_, _orientation\='vertical'_, _widths\=0.5_, _showmeans\=False_, _showextrema\=True_, _showmedians\=False_, _quantiles\=None_, _points\=100_, _bw\_method\=None_, _side\='both'_, _facecolor\=None_, _linecolor\=None_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4473-L4510)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot "Link to this definition")

Make a violin plot.

Make a violin plot for each column of _dataset_ or each vector in sequence _dataset_. Each filled area extends to represent the entire data range, with optional lines at the mean, the median, the minimum, the maximum, and user-specified quantiles.

Parameters:

**dataset**1D array or sequence of 1D arrays or 2D array

The input data. Possible values:

*   1D array: A single violin is drawn.
    
*   sequence of 1D arrays: A violin is drawn for each array in the sequence.
    
*   2D array: A violin is drawn for each column in the array.
    

Non-finite and masked values are ignored.

**positions**array-like, default: \[1, 2, ..., n\]

The positions of the violins; i.e. coordinates on the x-axis for vertical violins (or y-axis for horizontal violins).

**vert**bool, optional

Deprecated since version 3.10: Use _orientation_ instead.

If this is given during the deprecation period, it overrides the _orientation_ parameter.

If True, plots the violins vertically. If False, plots the violins horizontally.

**orientation**{'vertical', 'horizontal'}, default: 'vertical'

If 'horizontal', plots the violins horizontally. Otherwise, plots the violins vertically.

Added in version 3.10.

**widths**float or array-like, default: 0.5

The maximum width of each violin in units of the _positions_ axis. The default is 0.5, which is half the available space when using default _positions_.

**showmeans**bool, default: False

Whether to show the mean with a line.

**showextrema**bool, default: True

Whether to show extrema with a line.

**showmedians**bool, default: False

Whether to show the median with a line.

**quantiles**array-like, default: None

If not None, set a list of floats in interval \[0, 1\] for each violin, which stands for the quantiles that will be rendered for that violin.

**points**int, default: 100

The number of points to evaluate each of the gaussian kernel density estimations at.

**bw\_method**{'scott', 'silverman'} or float or callable, default: 'scott'

The method used to calculate the estimator bandwidth. If a float, this will be used directly as `kde.factor`. If a callable, it should take a [`matplotlib.mlab.GaussianKDE`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE "matplotlib.mlab.GaussianKDE")
 instance as its only parameter and return a float.

**side**{'both', 'low', 'high'}, default: 'both'

'both' plots standard violins. 'low'/'high' only plots the side below/above the positions value.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

If provided, will set the face color(s) of the violins.

Added in version 3.11.

**linecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

If provided, will set the line color(s) of the violins (the horizontal and vertical spines and body edges).

Added in version 3.11.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_dataset_

Returns:

dict

A dictionary mapping each component of the violinplot to a list of the corresponding collection instances created. The dictionary has the following keys:

*   `bodies`: A list of the [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
     instances containing the filled area of each violin.
    
*   `cmeans`: A [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     instance that marks the mean values of each of the violin's distribution.
    
*   `cmins`: A [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     instance that marks the bottom of each violin's distribution.
    
*   `cmaxes`: A [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     instance that marks the top of each violin's distribution.
    
*   `cbars`: A [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     instance that marks the centers of each violin's distribution.
    
*   `cmedians`: A [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     instance that marks the median values of each of the violin's distribution.
    
*   `cquantiles`: A [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     instance created to identify the quantile values of each of the violin's distribution.
    

See also

[`Axes.violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin")

Draw a violin from pre-computed statistics.

[`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")

Draw a box and whisker plot.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
.

Examples using `matplotlib.pyplot.violinplot`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#examples-using-matplotlib-pyplot-violinplot "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_vs_violin_thumb.png)

[Box plot vs. violin plot comparison](https://matplotlib.org/stable/gallery/statistics/boxplot_vs_violin.html)

Box plot vs. violin plot comparison

![](https://matplotlib.org/stable/_images/sphx_glr_violinplot_thumb.png)

[Violin plot basics](https://matplotlib.org/stable/gallery/statistics/violinplot.html)

Violin plot basics

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

On this page