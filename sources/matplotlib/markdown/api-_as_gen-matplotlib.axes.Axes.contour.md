[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#main-content)

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
    

matplotlib.axes.Axes.contour[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib-axes-axes-contour "Link to this heading")

=================================================================================================================================================================

Axes.contour(_\*args_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L7135-L7151)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "Link to this definition")

Plot contour lines.

Call signature:

contour(\[X, Y,\] Z, /, \[levels\], \*\*kwargs)

The arguments _X_, _Y_, _Z_ are positional-only.

[`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 draw contour lines and filled contours, respectively. Except as noted, function signatures and return values are the same for both versions.

Parameters:

**X, Y**array-like, optional

The coordinates of the values in _Z_.

_X_ and _Y_ must both be 2D with the same shape as _Z_ (e.g. created via [`numpy.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "(in NumPy v2.5)")
), or they must both be 1-D such that `len(X) == N` is the number of columns in _Z_ and `len(Y) == M` is the number of rows in _Z_.

_X_ and _Y_ must both be ordered monotonically.

If not given, they are assumed to be integer indices, i.e. `X = range(N)`, `Y = range(M)`.

**Z**(M, N) array-like

The height values over which the contour is drawn. Color-mapping is controlled by _cmap_, _norm_, _vmin_, and _vmax_.

**levels**int or array-like, optional

Determines the number and positions of the contour lines / regions.

If an int _n_, use [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
, which tries to automatically choose no more than _n+2_ "nice" contour level boundaries between the minimum and maximum numeric values of _Z_. These boundaries define where lines are drawn (for [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
) or where filled regions are separated (for [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
).

If not given, a reasonable default is chosen; for linear scales, [\*](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#id1)
n\*=7 is the default.

If array-like, draw contour lines at the specified levels. The values must be in increasing order.

If not specified, a reasonable default is automatically chosen. For linear scales, this corresponds to _levels=7_. For logarithmic scales, [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
 is used instead.

Returns:

[`QuadContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")

Other Parameters:

**corner\_mask**bool, default: `[rcParams["contour.corner_mask"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.corner_mask#rcparam-contour-corner-mask) ` (default: `True`)

Enable/disable corner masking, which only has an effect if _Z_ is a masked array. If `False`, any quad touching a masked point is masked out. If `True`, only the triangular corners of quads nearest those points are always masked out, other triangular corners comprising three unmasked points are contoured as usual.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the levels, i.e. the lines for [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and the areas for [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
.

The sequence is cycled for the levels in ascending order. If the sequence is shorter than the number of levels, it's repeated.

As a shortcut, a single color may be used in place of one-element lists, i.e. `'red'` instead of `['red']` to color all levels with the same color.

Changed in version 3.10: Previously a single color had to be expressed as a string, but now any valid color format may be passed.

By default (value _None_), the colormap specified by _cmap_ will be used.

**alpha**float, default: 1

The alpha blending value, between 0 (transparent) and 1 (opaque).

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

This parameter is ignored if _colors_ is set.

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
    

This parameter is ignored if _colors_ is set.

**vmin, vmax**float, optional

When using scalar data and no explicit _norm_, _vmin_ and _vmax_ define the data range that the colormap covers. By default, the colormap covers the complete value range of the supplied data. It is an error to use _vmin_/_vmax_ when a _norm_ instance is given (but using a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 _norm_ name together with _vmin_/_vmax_ is acceptable).

If _vmin_ or _vmax_ are not given, the default color scaling is based on _levels_.

This parameter is ignored if _colors_ is set.

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

This parameter is ignored if _colors_ is set.

**origin**{_None_, 'upper', 'lower', 'image'}, default: None

Determines the orientation and exact position of _Z_ by specifying the position of `Z[0, 0]`. This is only relevant, if _X_, _Y_ are not given.

*   _None_: `Z[0, 0]` is at X=0, Y=0 in the lower left corner.
    
*   'lower': `Z[0, 0]` is at X=0.5, Y=0.5 in the lower left corner.
    
*   'upper': `Z[0, 0]` is at X=N+0.5, Y=0.5 in the upper left corner.
    
*   'image': Use the value from `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`).
    

**extent**(x0, x1, y0, y1), optional

If _origin_ is not _None_, then _extent_ is interpreted as in [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
: it gives the outer pixel boundaries. In this case, the position of Z\[0, 0\] is the center of the pixel, not a corner. If _origin_ is _None_, then (_x0_, _y0_) is the position of Z\[0, 0\], and (_x1_, _y1_) is the position of Z\[-1, -1\].

This argument is ignored if _X_ and _Y_ are specified in the call to contour.

**locator**ticker.Locator subclass, optional

The locator is used to determine the contour levels if they are not given explicitly via _levels_. Defaults to [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
.

**extend**{'neither', 'both', 'min', 'max'}, default: 'neither'

Determines the `contourf`\-coloring of values that are outside the _levels_ range.

If 'neither', values outside the _levels_ range are not colored. If 'min', 'max' or 'both', color the values below, above or below and above the _levels_ range.

Values below `min(levels)` and above `max(levels)` are mapped to the under/over values of the [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
. Note that most colormaps do not have dedicated colors for these by default, so that the over and under values are the edge values of the colormap. You may want to set these values explicitly using [`Colormap.set_under`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "matplotlib.colors.Colormap.set_under")
 and [`Colormap.set_over`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_over "matplotlib.colors.Colormap.set_over")
.

Note

An existing [`QuadContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 does not get notified if properties of its colormap are changed. Therefore, an explicit call [`changed()`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.changed "matplotlib.contour.ContourSet.changed")
 is needed after modifying the colormap. The explicit call can be left out, if a colorbar is assigned to the [`QuadContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 because it internally calls [`changed()`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.changed "matplotlib.contour.ContourSet.changed")
.

Example:

x \= np.arange(1, 10)
y \= x.reshape(\-1, 1)
h \= x \* y

cs \= plt.contourf(h, levels\=\[10, 30, 50\],
    colors\=\['#808080', '#A0A0A0', '#C0C0C0'\], extend\='both')
cs.cmap.set\_over('red')
cs.cmap.set\_under('blue')
cs.changed()

**xunits, yunits**registered units, optional

Override axis units by specifying an instance of a [`matplotlib.units.ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
.

**antialiased**bool, optional

Enable antialiasing, overriding the defaults. For filled contours, the default is _False_. For line contours, it is taken from `[rcParams["lines.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.antialiased#rcparam-lines-antialiased) ` (default: `True`).

**nchunk**int >= 0, optional

If 0, no subdivision of the domain. Specify a positive integer to divide the domain into subdomains of _nchunk_ by _nchunk_ quads. Chunking reduces the maximum length of polygons generated by the contouring algorithm which reduces the rendering workload passed on to the backend and also requires slightly less RAM. It can however introduce rendering artifacts at chunk boundaries depending on the backend, the _antialiased_ flag and value of _alpha_.

**linewidths**float or array-like, default: `[rcParams["contour.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.linewidth#rcparam-contour-linewidth) ` (default: `None`)

_Only applies to_ [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

The line width of the contour lines.

If a number, all levels will be plotted with this linewidth.

If a sequence, the levels in ascending order will be plotted with the linewidths in the order specified.

If None, this falls back to `[rcParams["lines.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.linewidth#rcparam-lines-linewidth) ` (default: `1.5`).

**linestyles**{_None_, 'solid', 'dashed', 'dashdot', 'dotted'}, optional

_Only applies to_ [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

If _linestyles_ is _None_, the default is 'solid' unless the lines are monochrome. In that case, negative contours will instead take their linestyle from the _negative\_linestyles_ argument.

_linestyles_ can also be an iterable of the above strings specifying a set of linestyles to be used. If this iterable is shorter than the number of contour levels it will be repeated as necessary.

**negative\_linestyles**{_None_, 'solid', 'dashed', 'dashdot', 'dotted'}, optional

_Only applies to_ [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

If _linestyles_ is _None_ and the lines are monochrome, this argument specifies the line style for negative contours.

If _negative\_linestyles_ is _None_, the default is taken from `[rcParams["contour.negative_linestyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.negative_linestyle#rcparam-contour-negative-linestyle) ` (default: `'dashed'`).

_negative\_linestyles_ can also be an iterable of the above strings specifying a set of linestyles to be used. If this iterable is shorter than the number of contour levels it will be repeated as necessary.

**hatches**list\[str\], optional

_Only applies to_ [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
.

A list of cross hatch patterns to use on the filled areas. If None, no hatching will be added to the contour.

**algorithm**{'mpl2005', 'mpl2014', 'serial', 'threaded'}, optional

Which contouring algorithm to use to calculate the contour lines and polygons. The algorithms are implemented in [ContourPy](https://github.com/contourpy/contourpy)
, consult the [ContourPy documentation](https://contourpy.readthedocs.io/)
 for further information.

The default is taken from `[rcParams["contour.algorithm"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.algorithm#rcparam-contour-algorithm) ` (default: `'mpl2014'`).

**clip\_path**[`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 or [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 or [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")

Set the clip path. See [`set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
.

Added in version 3.8.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**rasterized**bool, optional

_Only applies to_ [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
. Rasterize the contour plot when drawing vector graphics. This can speed up rendering and produce smaller files for large data sets. See also [Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)
.

Notes

1.  [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
     differs from the MATLAB version in that it does not draw the polygon edges. To draw edges, add line contours with calls to [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
    .
    
2.  [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
     fills intervals that are closed at the top; that is, for boundaries _z1_ and _z2_, the filled region is:
    
    z1 < Z <= z2
    
    except for the lowest interval, which is closed on both sides (i.e. it includes the lowest value).
    
3.  [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
     and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
     use a [marching squares](https://en.wikipedia.org/wiki/Marching_squares)
     algorithm to compute contour locations. More information can be found in [ContourPy documentation](https://contourpy.readthedocs.io/)
    .
    

Examples using `matplotlib.axes.Axes.contour`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#examples-using-matplotlib-axes-axes-contour "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_thumb.png)

[Blend transparency with color in 2D images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html)

Blend transparency with color in 2D images

![](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_thumb.png)

[Contour plot of irregularly spaced data](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html)

Contour plot of irregularly spaced data

![](https://matplotlib.org/stable/_images/sphx_glr_contour_demo_thumb.png)

[Contour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html)

Contour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_label_demo_thumb.png)

[Contour Label Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_label_demo.html)

Contour Label Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)

[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)

Contourf demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_hatching_thumb.png)

[Contourf hatching](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html)

Contourf hatching

![](https://matplotlib.org/stable/_images/sphx_glr_contour_corner_mask_thumb.png)

[Contour corner mask](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_corner_mask.html)

Contour corner mask

![](https://matplotlib.org/stable/_images/sphx_glr_contours_in_optimization_demo_thumb.png)

[Contouring the solution space of optimizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html)

Contouring the solution space of optimizations

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_thumb.png)

[Plot contour (level) curves in 3D](https://matplotlib.org/stable/gallery/mplot3d/contour3d.html)

Plot contour (level) curves in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_2_thumb.png)

[Plot contour (level) curves in 3D using the extend3d option](https://matplotlib.org/stable/gallery/mplot3d/contour3d_2.html)

Plot contour (level) curves in 3D using the extend3d option

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_thumb.png)

[Project contour profiles onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html)

Project contour profiles onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_contour_thumb.png)

[contour(X, Y, Z)](https://matplotlib.org/stable/plot_types/arrays/contour.html)

contour(X, Y, Z)

On this page