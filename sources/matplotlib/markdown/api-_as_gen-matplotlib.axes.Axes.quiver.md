[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#main-content)

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
    

matplotlib.axes.Axes.quiver[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib-axes-axes-quiver "Link to this heading")

==============================================================================================================================================================

Axes.quiver(_\*args_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L5930-L5938)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "Link to this definition")

Plot a 2D field of arrows.

Call signature:

quiver(\[X, Y\], U, V, \[C\], /, \*\*kwargs)

_X_, _Y_ define the arrow locations, _U_, _V_ define the arrow directions, and _C_ optionally sets the color. The arguments _X_, _Y_, _U_, _V_, _C_ are positional-only.

**Arrow length**

The default settings auto-scales the length of the arrows to a reasonable size. To change this behavior see the _scale_ and _scale\_units_ parameters.

**Arrow shape**

The arrow shape is determined by _width_, _headwidth_, _headlength_ and _headaxislength_. See the notes below.

**Arrow styling**

Each arrow is internally represented by a filled polygon with a default edge linewidth of 0. As a result, an arrow is rather a filled area, not a line with a head, and [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 properties like _linewidth_, _edgecolor_, _facecolor_, etc. act accordingly.

Parameters:

**X, Y**1D or 2D array-like, optional

The x and y coordinates of the arrow locations.

If not given, they will be generated as a uniform integer meshgrid based on the dimensions of _U_ and _V_.

If _X_ and _Y_ are 1D but _U_, _V_ are 2D, _X_, _Y_ are expanded to 2D using `X, Y = np.meshgrid(X, Y)`. In this case `len(X)` and `len(Y)` must match the column and row dimensions of _U_ and _V_.

**U, V**1D or 2D array-like

The x and y direction components of the arrow vectors. The interpretation of these components (in data or in screen space) depends on _angles_.

_U_ and _V_ must have the same number of elements, matching the number of arrow locations in _X_, _Y_. _U_ and _V_ may be masked. Locations masked in any of _U_, _V_, and _C_ will not be drawn.

**C**1D or 2D array-like, optional

Numeric data that defines the arrow colors by colormapping via _norm_ and _cmap_.

This does not support explicit colors. If you want to set colors directly, use _color_ instead. The size of _C_ must match the number of arrow locations.

**angles**{'uv', 'xy'} or array-like, default: 'uv'

Method for determining the angle of the arrows.

*   'uv': Arrow directions are based on [display coordinates](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#coordinate-systems)
    ; i.e. a 45° angle will always show up as diagonal on the screen, irrespective of figure or Axes aspect ratio or Axes data ranges. This is useful when the arrows represent a quantity whose direction is not tied to the x and y data coordinates.
    
    If _U_ == _V_ the orientation of the arrow on the plot is 45 degrees counter-clockwise from the horizontal axis (positive to the right).
    
*   'xy': Arrow direction in data coordinates, i.e. the arrows point from (x, y) to (x+u, y+v). This is ideal for vector fields or gradient plots where the arrows should directly represent movements or gradients in the x and y directions.
    
*   Arbitrary angles may be specified explicitly as an array of values in degrees, counter-clockwise from the horizontal axis.
    
    In this case _U_, _V_ is only used to determine the length of the arrows.
    
    For example, `angles=[30, 60, 90]` will orient the arrows at 30, 60, and 90 degrees respectively, regardless of the _U_ and _V_ components.
    

Note: inverting a data axis will correspondingly invert the arrows only with `angles='xy'`.

**pivot**{'tail', 'middle', 'tip'}, default: 'tail'

The part of the arrow that is anchored to the _X_, _Y_ grid. The arrow rotates about this point.

Discouraged

'mid' is a synonym for 'middle', which is retained for backwards compatibility. New code should use 'middle'.

**scale**float, optional

Scales the length of the arrow inversely.

Number of data values represented by one unit of arrow length on the plot. For example, if the data represents velocity in meters per second (m/s), the scale parameter determines how many meters per second correspond to one unit of arrow length relative to the width of the plot. Smaller scale parameter makes the arrow longer.

By default, an autoscaling algorithm is used to scale the arrow length to a reasonable size, which is based on the average vector length and the number of vectors.

The arrow length unit is given by the _scale\_units_ parameter.

**scale\_units**{'width', 'height', 'dots', 'inches', 'x', 'y', 'xy'}, default: 'width'

The physical image unit, which is used for rendering the scaled arrow data U, V.

The rendered arrow length is given by:

*   length in x direction = \\(\\frac{u}{\\mathrm{scale}}\\,\\mathrm{scale\\\_unit}\\)
    
*   length in y direction = \\(\\frac{v}{\\mathrm{scale}}\\,\\mathrm{scale\\\_unit}\\)
    

For example, `(u, v) = (0.5, 0)` with `scale=10, scale_units="width"` results in a horizontal arrow with a length of _0.5 / 10 \* "width"_, i.e. 0.05 times the Axes width.

Supported values are:

*   'width' or 'height': The arrow length is scaled relative to the width or height
    
    of the Axes. For example, `scale_units='width', scale=1.0`, will result in an arrow length of width of the Axes.
    
*   'dots': The arrow length of the arrows is in measured in display dots (pixels).
    
*   'inches': Arrow lengths are scaled based on the DPI (dots per inch) of the figure.
    
    This ensures that the arrows have a consistent physical size on the figure, in inches, regardless of data values or plot scaling. For example, `(u, v) = (1, 0)` with `scale_units='inches', scale=2` results in a 0.5 inch-long arrow.
    
*   'x' or 'y': The arrow length is scaled relative to the x or y axis units.
    
    For example, `(u, v) = (0, 1)` with `scale_units='x', scale=1` results in a vertical arrow with the length of 1 x-axis unit.
    
*   'xy': Arrow length will be same as 'x' or 'y' units.
    
    This is useful for creating vectors in the x-y plane where u and v have the same units as x and y. To plot vectors in the x-y plane with u and v having the same units as x and y, use `angles='xy', scale_units='xy', scale=1`.
    

Note: Setting _scale\_units_ without setting scale does not have any effect because the scale units only differ by a constant factor and that is rescaled through autoscaling.

**units**{'width', 'height', 'dots', 'inches', 'x', 'y', 'xy'}, default: 'width'

Affects the arrow size (except for the length). In particular, the shaft _width_ is measured in multiples of this unit.

Supported values are:

*   'width', 'height': The width or height of the Axes.
    
*   'dots', 'inches': Pixels or inches based on the figure dpi.
    
*   'x', 'y', 'xy': _X_, _Y_ or \\(\\\\sqrt{X^2 + Y^2}\\) in data units.
    

The following table summarizes how these values affect the visible arrow size under zooming and figure size changes:

| units | zoom | figure size change |
| --- | --- | --- |
| 'x', 'y', 'xy' | arrow size scales | —   |
| 'width', 'height' | —   | arrow size scales |
| 'dots', 'inches' | —   | —   |

**width**float, optional

Shaft width in arrow units. All head parameters are relative to _width_.

The default depends on choice of _units_ above, and number of vectors; a typical starting value is about 0.005 times the width of the plot.

**headwidth**float, default: 3

Head width as multiple of shaft _width_. See the notes below.

**headlength**float, default: 5

Head length as multiple of shaft _width_. See the notes below.

**headaxislength**float, default: 4.5

Head length at shaft intersection as multiple of shaft _width_. See the notes below.

**minshaft**float, default: 1

Length below which arrow scales, in units of head length. Do not set this to less than 1, or small arrows will look terrible!

**minlength**float, default: 1

Minimum length as a multiple of shaft width; if an arrow length is less than this, plot a dot (hexagon) of this diameter instead.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

Explicit color(s) for the arrows. If _C_ has been set, _color_ has no effect.

This is a synonym for the [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 _facecolor_ parameter.

Returns:

[`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")

Other Parameters:

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**[`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 properties, optional

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

[`Axes.quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey")

Add a key to a quiver plot.

Notes

**Arrow shape**

The arrow is drawn as a polygon using the nodes as shown below. The values _headwidth_, _headlength_, and _headaxislength_ are in units of _width_.

[![../../_images/quiver_sizes.svg](https://matplotlib.org/stable/_images/quiver_sizes.svg)](https://matplotlib.org/stable/_images/quiver_sizes.svg)

The defaults give a slightly swept-back arrow. Here are some guidelines how to get other head shapes:

*   To make the head a triangle, make _headaxislength_ the same as _headlength_.
    
*   To make the arrow more pointed, reduce _headwidth_ or increase _headlength_ and _headaxislength_.
    
*   To make the head smaller relative to the shaft, scale down all the head parameters proportionally.
    
*   To remove the head completely, set all _head_ parameters to 0.
    
*   To get a diamond-shaped head, make _headaxislength_ larger than _headlength_.
    
*   Warning: For _headaxislength_ < (_headlength_ / _headwidth_), the "headaxis" nodes (i.e. the ones connecting the head with the shaft) will protrude out of the head in forward direction so that the arrow head looks broken.
    

Examples using `matplotlib.axes.Axes.quiver`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#examples-using-matplotlib-axes-axes-quiver "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_trigradient_demo_thumb.png)

[Trigradient Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html)

Trigradient Demo

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_simple_demo_thumb.png)

[Quiver Simple Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html)

Quiver Simple Demo

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_demo_thumb.png)

[Advanced quiver and quiverkey functions](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_demo.html)

Advanced quiver and quiverkey functions

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_thumb.png)

[3D quiver plot](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html)

3D quiver plot

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_thumb.png)

[quiver(X, Y, U, V)](https://matplotlib.org/stable/plot_types/arrays/quiver.html)

quiver(X, Y, U, V)

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_simple_thumb.png)

[quiver(X, Y, Z, U, V, W)](https://matplotlib.org/stable/plot_types/3D/quiver3d_simple.html)

quiver(X, Y, Z, U, V, W)

On this page