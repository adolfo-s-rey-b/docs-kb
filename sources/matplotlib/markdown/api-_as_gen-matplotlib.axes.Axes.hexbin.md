[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#main-content)

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
    

matplotlib.axes.Axes.hexbin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib-axes-axes-hexbin "Link to this heading")

==============================================================================================================================================================

Axes.hexbin(_x_, _y_, _C\=None_, _\*_, _gridsize\=100_, _bins\=None_, _xscale\='linear'_, _yscale\='linear'_, _extent\=None_, _cmap\=None_, _norm\=None_, _vmin\=None_, _vmax\=None_, _alpha\=None_, _linewidths\=None_, _edgecolors\='face'_, _reduce\_C\_function\=<function mean>_, _mincnt\=None_, _marginals\=False_, _colorizer\=None_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L5470-L5873)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "Link to this definition")

Make a 2D hexagonal binning plot of points _x_, _y_.

If _C_ is _None_, the value of the hexagon is determined by the number of points in the hexagon. Otherwise, _C_ specifies values at the coordinate (x\[i\], y\[i\]). For each hexagon, these values are reduced using _reduce\_C\_function_.

Parameters:

**x, y**array-like

The data positions. _x_ and _y_ must be of the same length.

**C**array-like, optional

If given, these values are accumulated in the bins. Otherwise, every point has a value of 1. Must be of the same length as _x_ and _y_.

**gridsize**int or (int, int), default: 100

If a single int, the number of hexagons in the _x_\-direction. The number of hexagons in the _y_\-direction is chosen such that the hexagons are approximately regular.

Alternatively, if a tuple (_nx_, _ny_), the number of hexagons in the _x_\-direction and the _y_\-direction. In the _y_\-direction, counting is done along vertically aligned hexagons, not along the zig-zag chains of hexagons; see the following illustration.

([`Source code`](https://matplotlib.org/stable/_downloads/88851d628db237a7a1585dcc2f33be66/matplotlib-axes-Axes-hexbin-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/04d2547f092619b5bb93ed156962ae71/matplotlib-axes-Axes-hexbin-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/721ce2627070f0d244556b2f94a1cf0e/matplotlib-axes-Axes-hexbin-1.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-matplotlib-axes-Axes-hexbin-1.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-matplotlib-axes-Axes-hexbin-1.2x.png)

To get approximately regular hexagons, choose \\(n\_x = \\sqrt{3}\\,n\_y\\).

**bins**'log' or int or sequence, default: None

Discretization of the hexagon values.

*   If _None_, no binning is applied; the color of each hexagon directly corresponds to its count value.
    
*   If 'log', use a logarithmic scale for the colormap. Internally, \\(log\_{10}(i)\\) is used to determine the hexagon color. This is equivalent to `norm=LogNorm()`. Note that 0 counts are thus marked with the "bad" color.
    
*   If an integer, divide the counts in the specified number of bins, and color the hexagons accordingly.
    
*   If a sequence of values, the values of the lower bound of the bins to be used.
    

**xscale**{'linear', 'log'}, default: 'linear'

Use a linear or log10 scale on the horizontal axis.

**yscale**{'linear', 'log'}, default: 'linear'

Use a linear or log10 scale on the vertical axis.

**mincnt**int >= 0, default: _None_

If not _None_, only display cells with at least _mincnt_ number of points in the cell.

**marginals**bool, default: _False_

If marginals is _True_, plot the marginal density as colormapped rectangles along the bottom of the x-axis and left of the y-axis.

**extent**4-tuple of float, default: _None_

The limits of the bins (xmin, xmax, ymin, ymax). The default assigns the limits based on _gridsize_, _x_, _y_, _xscale_ and _yscale_.

If _xscale_ or _yscale_ is set to 'log', the limits are expected to be the exponent for a power of 10. E.g. for x-limits of 1 and 50 in 'linear' scale and y-limits of 10 and 1000 in 'log' scale, enter (1, 50, 1, 3).

Returns:

[`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")

A [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 defining the hexagonal bins.

*   [`PolyCollection.get_offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.get_offsets "matplotlib.collections.PolyCollection.get_offsets")
     contains a Mx2 array containing the x, y positions of the M hexagon centers in data coordinates.
    
*   [`PolyCollection.get_array`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.get_array "matplotlib.collections.PolyCollection.get_array")
     contains the values of the M hexagons.
    

If _marginals_ is _True_, horizontal bar and vertical bar (both PolyCollections) will be attached to the return collection as attributes _hbar_ and _vbar_.

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

**alpha**float between 0 and 1, optional

The alpha blending value, between 0 (transparent) and 1 (opaque).

**linewidths**float, default: _None_

If _None_, defaults to `[rcParams["patch.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.linewidth#rcparam-patch-linewidth) ` (default: `1.0`).

**edgecolors**{'face', 'none', _None_} or color, default: 'face'

The color of the hexagon edges. Possible values are:

*   'face': Draw the edges in the same color as the fill color.
    
*   'none': No edges are drawn. This can sometimes lead to unsightly unpainted pixels between the hexagons.
    
*   _None_: Draw outlines in the default color.
    
*   An explicit color.
    

**reduce\_C\_function**callable, default: [`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "(in NumPy v2.5)")

The function to aggregate _C_ within the bins. It is ignored if _C_ is not given. This must have the signature:

def reduce\_C\_function(C: array) \-> float

Commonly used functions are:

*   [`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "(in NumPy v2.5)")
    : average of the points
    
*   [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "(in NumPy v2.5)")
    : integral of the point values
    
*   [`numpy.amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "(in NumPy v2.5)")
    : value taken from the largest point
    

By default will only reduce cells with at least 1 point because some reduction functions (such as [`numpy.amax`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html#numpy.amax "(in NumPy v2.5)")
) will error/warn with empty input. Changing _mincnt_ will adjust the cutoff, and if set to 0 will pass empty input to the reduction function.

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_x_, _y_, _C_

**\*\*kwargs**[`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 properties

All other keyword arguments are passed on to [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
:

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |
| [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |
| [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
| [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
| [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_color "matplotlib.collections.Collection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of RGBA tuples |
| [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |
| [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
| [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |
| [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |
| [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
| [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts "matplotlib.collections.PolyCollection.set_verts") | list of array-like |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sizes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections._CollectionWithSizes.set_sizes "matplotlib.collections._CollectionWithSizes.set_sizes") | [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")<br> or None |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
| [`verts`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts "matplotlib.collections.PolyCollection.set_verts") | list of array-like |
| [`verts_and_codes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts_and_codes "matplotlib.collections.PolyCollection.set_verts_and_codes") | unknown |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")

2D histogram rectangular bins

Examples using `matplotlib.axes.Axes.hexbin`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#examples-using-matplotlib-axes-axes-hexbin "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_hexbin_demo_thumb.png)

[Hexagonal binned plot](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html)

Hexagonal binned plot

![](https://matplotlib.org/stable/_images/sphx_glr_hexbin_thumb.png)

[hexbin(x, y, C)](https://matplotlib.org/stable/plot_types/stats/hexbin.html)

hexbin(x, y, C)

On this page