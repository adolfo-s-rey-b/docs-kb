[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#main-content)

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
    

matplotlib.axes.Axes.violin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib-axes-axes-violin "Link to this heading")

==============================================================================================================================================================

Axes.violin(_vpstats_, _positions\=None_, _\*_, _vert\=None_, _orientation\='vertical'_, _widths\=0.5_, _showmeans\=False_, _showextrema\=True_, _showmedians\=False_, _side\='both'_, _facecolor\=None_, _linecolor\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L8998-L9290)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "Link to this definition")

Draw a violin plot from pre-computed statistics.

Draw a violin plot for each column of _vpstats_. Each filled area extends to represent the entire data range, with optional lines at the mean, the median, the minimum, the maximum, and the quantiles values.

Parameters:

**vpstats**list of dicts

A list of dictionaries containing stats for each violin plot. Required keys are:

*   `coords`: A list of scalars containing the coordinates that the violin's kernel density estimate were evaluated at.
    
*   `vals`: A list of scalars containing the values of the kernel density estimate at each of the coordinates given in _coords_.
    
*   `mean`: The mean value for this violin's dataset.
    
*   `median`: The median value for this violin's dataset.
    
*   `min`: The minimum value for this violin's dataset.
    
*   `max`: The maximum value for this violin's dataset.
    

Optional keys are:

*   `quantiles`: A list of scalars containing the quantile values for this violin's dataset.
    

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

The maximum width of each violin in units of the _positions_ axis. The default is 0.5, which is half available space when using default _positions_.

**showmeans**bool, default: False

Whether to show the mean with a line.

**showextrema**bool, default: True

Whether to show extrema with a line.

**showmedians**bool, default: False

Whether to show the median with a line.

**side**{'both', 'low', 'high'}, default: 'both'

'both' plots standard violins. 'low'/'high' only plots the side below/above the positions value.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

If provided, will set the face color(s) of the violins.

Added in version 3.11.

For backward compatibility, if _facecolor_ is not given, the body will get an Artist-level transparency [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha")
 of 0.3, which will persist if you afterwards change the facecolor, e.g. via `result['bodies'][0].set_facecolor('red')`. If _facecolor_ is given, there is no Artist-level transparency. To set transparency for _facecolor_ or _edgecolor_ use `(color, alpha)` tuples.

**linecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

If provided, will set the line color(s) of the violins (the horizontal and vertical spines and body edges).

Added in version 3.11.

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
     instance created to identify the quantiles values of each of the violin's distribution.
    

See also

[`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")

Draw a violin plot from data instead of pre-computed statistics.

[`cbook.violin_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")

Calculate a _vpstats_ dictionary from data, suitable for passing to violin.

On this page