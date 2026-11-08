[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#main-content)

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
    

matplotlib.axes.Axes.fill\_between[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib-axes-axes-fill-between "Link to this heading")

=================================================================================================================================================================================

Axes.fill\_between(_x_, _y1_, _y2\=0_, _where\=None_, _interpolate\=False_, _step\=None_, _\*_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L6115-L6119)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "Link to this definition")

Fill the area between two horizontal curves.

The curves are defined by the points (_x_, _y1_) and (_x_, _y2_). This creates one or multiple polygons describing the filled area.

You may exclude some horizontal sections from filling using _where_.

By default, the edges connect the given points directly. Use _step_ if the filling should be a step function, i.e. constant in between _x_.

Parameters:

**x**array-like

The x coordinates of the nodes defining the curves.

**y1**array-like or float

The y coordinates of the nodes defining the first curve.

**y2**array-like or float, default: 0

The y coordinates of the nodes defining the second curve.

**where**array-like of bool, optional

Define _where_ to exclude some horizontal regions from being filled. The filled regions are defined by the coordinates `x[where]`. More precisely, fill between `x[i]` and `x[i+1]` if `where[i] and where[i+1]`. Note that this definition implies that an isolated _True_ value between two _False_ values in _where_ will not result in filling. Both sides of the _True_ position remain unfilled due to the adjacent _False_ values.

**interpolate**bool, default: False

This option is only relevant if _where_ is used and the two curves are crossing each other.

Semantically, _where_ is often used for _y1_ > _y2_ or similar. By default, the nodes of the polygon defining the filled region will only be placed at the positions in the _x_ array. Such a polygon cannot describe the above semantics close to the intersection. The x-sections containing the intersection are simply clipped.

Setting _interpolate_ to _True_ will calculate the actual intersection point and extend the filled region up to this point.

**step**{'pre', 'post', 'mid'}, optional

Define _step_ if the filling should be a step function, i.e. constant in between _x_. The value determines where the step will occur:

*   'pre': The y value is continued constantly to the left from every _x_ position, i.e. the interval `(x[i-1], x[i]]` has the value `y[i]`.
    
*   'post': The y value is continued constantly to the right from every _x_ position, i.e. the interval `[x[i], x[i+1])` has the value `y[i]`.\
    \
*   'mid': Steps occur half-way between the _x_ positions.\
    \
\
Returns:\
\
[`FillBetweenPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection "matplotlib.collections.FillBetweenPolyCollection")\
\
A [`FillBetweenPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection "matplotlib.collections.FillBetweenPolyCollection")\
 containing the plotted polygons.\
\
Other Parameters:\
\
**data**indexable object, optional\
\
If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:\
\
_x_, _y1_, _y2_, _where_\
\
**\*\*kwargs**\
\
All other keyword arguments are passed on to [`FillBetweenPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection "matplotlib.collections.FillBetweenPolyCollection")\
. They control the [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")\
 properties:\
\
| Property | Description |\
| --- | --- |\
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |\
| [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |\
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |\
| [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |\
| [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |\
| [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |\
| [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |\
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |\
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |\
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |\
| [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |\
| [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_color "matplotlib.collections.Collection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of RGBA tuples |\
| [`data`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection.set_data "matplotlib.collections.FillBetweenPolyCollection.set_data") | array-like |\
| [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |\
| [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |\
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |\
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |\
| [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |\
| [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |\
| [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |\
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |\
| [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |\
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |\
| [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |\
| [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |\
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |\
| [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |\
| [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |\
| [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |\
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |\
| [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts "matplotlib.collections.PolyCollection.set_verts") | list of array-like |\
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |\
| [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |\
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |\
| [`sizes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections._CollectionWithSizes.set_sizes "matplotlib.collections._CollectionWithSizes.set_sizes") | [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")<br> or None |\
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |\
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |\
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |\
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |\
| [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |\
| [`verts`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts "matplotlib.collections.PolyCollection.set_verts") | list of array-like |\
| [`verts_and_codes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts_and_codes "matplotlib.collections.PolyCollection.set_verts_and_codes") | unknown |\
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |\
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |\
\
See also\
\
[`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")\
\
Fill between two sets of y-values.\
\
[`fill_betweenx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")\
\
Fill between two sets of x-values.\
\
Examples using `matplotlib.axes.Axes.fill_between`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#examples-using-matplotlib-axes-axes-fill-between "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)\
\
[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)\
\
fill\_between with transparency\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_demo_thumb.png)\
\
[Fill the area between two lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html)\
\
Fill the area between two lines\
\
![](https://matplotlib.org/stable/_images/sphx_glr_span_regions_thumb.png)\
\
[Shade regions defined by a logical mask using fill\_between](https://matplotlib.org/stable/gallery/lines_bars_and_markers/span_regions.html)\
\
Shade regions defined by a logical mask using fill\_between\
\
![](https://matplotlib.org/stable/_images/sphx_glr_twin_axes_zorder_thumb.png)\
\
[Twin Axes with delta\_zorder](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/twin_axes_zorder.html)\
\
Twin Axes with delta\_zorder\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fillbetween3d_thumb.png)\
\
[Fill between 3D lines](https://matplotlib.org/stable/gallery/mplot3d/fillbetween3d.html)\
\
Fill between 3D lines\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fillunder3d_thumb.png)\
\
[Fill under 3D line graphs](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html)\
\
Fill under 3D line graphs\
\
![](https://matplotlib.org/stable/_images/sphx_glr_resample_thumb.png)\
\
[Resampling Data](https://matplotlib.org/stable/gallery/event_handling/resample.html)\
\
Resampling Data\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_thumb.png)\
\
[fill\_between(x, y1, y2)](https://matplotlib.org/stable/plot_types/basic/fill_between.html)\
\
fill\_between(x, y1, y2)\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fill_between3d_simple_thumb.png)\
\
[fill\_between(x1, y1, z1, x2, y2, z2)](https://matplotlib.org/stable/plot_types/3D/fill_between3d_simple.html)\
\
fill\_between(x1, y1, z1, x2, y2, z2)\
\
On this page