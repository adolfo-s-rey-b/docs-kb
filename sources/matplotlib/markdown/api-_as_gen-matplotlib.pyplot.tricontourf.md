[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#main-content)

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
    

matplotlib.pyplot.tricontourf[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib-pyplot-tricontourf "Link to this heading")

====================================================================================================================================================================

matplotlib.pyplot.tricontourf(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4430-L4435)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "Link to this definition")

Draw contour regions on an unstructured triangular grid.

Call signatures:

tricontourf(triangulation, z, \[levels\], ...)
tricontourf(x, y, z, \[levels\], \*, \[triangles\=triangles\], \[mask\=mask\], ...)

The triangular grid can be specified either by passing a [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 object as the first parameter, or by passing the points _x_, _y_ and optionally the _triangles_ and a _mask_. See [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 for an explanation of these parameters. If neither of _triangulation_ or _triangles_ are given, the triangulation is calculated on the fly.

It is possible to pass _triangles_ positionally, i.e. `tricontourf(x, y, triangles, z, ...)`. However, this is discouraged. For more clarity, pass _triangles_ via keyword argument.

Parameters:

**triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, optional

An already created triangular grid.

**x, y, triangles, mask**

Parameters defining the triangular grid. See [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
. This is mutually exclusive with specifying _triangulation_.

**z**array-like

The height values over which the contour is drawn. Color-mapping is controlled by _cmap_, _norm_, _vmin_, and _vmax_.

Note

All values in _z_ must be finite. Hence, nan and inf values must either be removed or [`set_mask`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
 be used.

**levels**int or array-like, optional

Determines the number and positions of the contour lines / regions.

If an int _n_, use [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
, which tries to automatically choose no more than _n+1_ "nice" contour levels between between minimum and maximum numeric values of _Z_.

If array-like, draw contour lines at the specified levels. The values must be in increasing order.

Returns:

[`TriContourSet`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "matplotlib.tri.TriContourSet")

Other Parameters:

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the levels, i.e., the contour regions.

The sequence is cycled for the levels in ascending order. If the sequence is shorter than the number of levels, it is repeated.

As a shortcut, single color strings may be used in place of one-element lists, i.e. `'red'` instead of `['red']` to color all levels with the same color. This shortcut does only work for color strings, not for other ways of specifying colors.

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

**origin**{_None_, 'upper', 'lower', 'image'}, default: None

Determines the orientation and exact position of _z_ by specifying the position of `z[0, 0]`. This is only relevant, if _X_, _Y_ are not given.

*   _None_: `z[0, 0]` is at X=0, Y=0 in the lower left corner.
    
*   'lower': `z[0, 0]` is at X=0.5, Y=0.5 in the lower left corner.
    
*   'upper': `z[0, 0]` is at X=N+0.5, Y=0.5 in the upper left corner.
    
*   'image': Use the value from `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`).
    

**extent**(x0, x1, y0, y1), optional

If _origin_ is not _None_, then _extent_ is interpreted as in [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
: it gives the outer pixel boundaries. In this case, the position of z\[0, 0\] is the center of the pixel, not a corner. If _origin_ is _None_, then (_x0_, _y0_) is the position of z\[0, 0\], and (_x1_, _y1_) is the position of z\[-1, -1\].

This argument is ignored if _X_ and _Y_ are specified in the call to contour.

**locator**ticker.Locator subclass, optional

The locator is used to determine the contour levels if they are not given explicitly via _levels_. Defaults to [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
.

**extend**{'neither', 'both', 'min', 'max'}, default: 'neither'

Determines the `tricontourf`\-coloring of values that are outside the _levels_ range.

If 'neither', values outside the _levels_ range are not colored. If 'min', 'max' or 'both', color the values below, above or below and above the _levels_ range.

Values below `min(levels)` and above `max(levels)` are mapped to the under/over values of the [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
. Note that most colormaps do not have dedicated colors for these by default, so that the over and under values are the edge values of the colormap. You may want to set these values explicitly using [`Colormap.set_under`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "matplotlib.colors.Colormap.set_under")
 and [`Colormap.set_over`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_over "matplotlib.colors.Colormap.set_over")
.

Note

An existing [`TriContourSet`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "matplotlib.tri.TriContourSet")
 does not get notified if properties of its colormap are changed. Therefore, an explicit call to [`ContourSet.changed()`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.changed "matplotlib.contour.ContourSet.changed")
 is needed after modifying the colormap. The explicit call can be left out, if a colorbar is assigned to the [`TriContourSet`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "matplotlib.tri.TriContourSet")
 because it internally calls [`ContourSet.changed()`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.changed "matplotlib.contour.ContourSet.changed")
.

**xunits, yunits**registered units, optional

Override axis units by specifying an instance of a [`matplotlib.units.ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
.

**antialiased**bool, optional

Enable antialiasing, overriding the defaults. For filled contours, the default is _True_. For line contours, it is taken from `[rcParams["lines.antialiased"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.antialiased#rcparam-lines-antialiased) ` (default: `True`).

**hatches**list\[str\], optional

A list of crosshatch patterns to use on the filled areas. If None, no hatching will be added to the contour.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
.

[`tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "matplotlib.pyplot.tricontourf")
 fills intervals that are closed at the top; that is, for boundaries _z1_ and _z2_, the filled region is:

z1 < Z <= z2

except for the lowest interval, which is closed on both sides (i.e. it includes the lowest value).

Examples using `matplotlib.pyplot.tricontourf`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#examples-using-matplotlib-pyplot-tricontourf "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_demo_thumb.png)

[Tricontour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_demo.html)

Tricontour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_user_thumb.png)

[Tricontour Smooth User](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_user.html)

Tricontour Smooth User

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_delaunay_thumb.png)

[Tricontour Smooth Delaunay](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html)

Tricontour Smooth Delaunay

![](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_thumb.png)

[Triinterp Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html)

Triinterp Demo

![](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_thumb.png)

[Contour plot of irregularly spaced data](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html)

Contour plot of irregularly spaced data

On this page