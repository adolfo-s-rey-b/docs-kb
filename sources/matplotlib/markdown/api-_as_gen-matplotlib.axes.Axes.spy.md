[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#main-content)

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
    

matplotlib.axes.Axes.spy[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib-axes-axes-spy "Link to this heading")

=====================================================================================================================================================

Axes.spy(_Z_, _\*_, _precision\=0_, _marker\=None_, _markersize\=None_, _aspect\='equal'_, _origin\='upper'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L8672-L8810)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "Link to this definition")

Plot the sparsity pattern of a 2D array.

This visualizes the non-zero values of the array.

Two plotting styles are available: image and marker. Both are available for full arrays, but only the marker style works for [`scipy.sparse.spmatrix`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.spmatrix.html#scipy.sparse.spmatrix "(in SciPy v1.18.0)")
 instances.

**Image style**

If _marker_ and _markersize_ are _None_, [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 is used. Any extra remaining keyword arguments are passed to this method.

**Marker style**

If _Z_ is a [`scipy.sparse.spmatrix`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.spmatrix.html#scipy.sparse.spmatrix "(in SciPy v1.18.0)")
 or _marker_ or _markersize_ are _None_, a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 object will be returned with the value of marker determining the marker type, and any remaining keyword arguments passed to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
.

Parameters:

**Z**(M, N) array-like

The array to be plotted.

**precision**float or 'present', default: 0

If _precision_ is 0, any non-zero value will be plotted. Otherwise, values of \\(|Z| > precision\\) will be plotted.

For [`scipy.sparse.spmatrix`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.spmatrix.html#scipy.sparse.spmatrix "(in SciPy v1.18.0)")
 instances, you can also pass 'present'. In this case any value present in the array will be plotted, even if it is identically zero.

**aspect**{'equal', 'auto', None} or float, default: 'equal'

The aspect ratio of the Axes. This parameter is particularly relevant for images since it determines whether data pixels are square.

This parameter is a shortcut for explicitly calling [`Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
. See there for further details.

*   'equal': Ensures an aspect ratio of 1. Pixels will be square.
    
*   'auto': The Axes is kept fixed and the aspect is adjusted so that the data fit in the Axes. In general, this will result in non-square pixels.
    
*   _None_: Use `[rcParams["image.aspect"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.aspect#rcparam-image-aspect) ` (default: `'equal'`).
    

**origin**{'upper', 'lower'}, default: `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`)

Place the \[0, 0\] index of the array in the upper left or lower left corner of the Axes. The convention 'upper' is typically used for matrices and images.

Returns:

[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 or [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The return type depends on the plotting style (see above).

Other Parameters:

**\*\*kwargs**

The supported additional parameters depend on the plotting style.

For the image style, you can pass the following additional parameters of [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
:

*   _cmap_
    
*   _alpha_
    
*   _url_
    
*   any [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
     properties (passed on to the [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
    )
    

For the marker style, you can pass any [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 property except for _linestyle_:

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "matplotlib.lines.Line2D.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "matplotlib.lines.Line2D.set_antialiased") | bool |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")<br> or [`c`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`dash_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "matplotlib.lines.Line2D.set_dash_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
| [`dash_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle "matplotlib.lines.Line2D.set_dash_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
| [`dashes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes") | sequence of floats (on/off ink in points) or (None, None) |
| [`data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data") | (2, N) array or two 1D arrays |
| [`drawstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle")<br> or [`ds`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle") | {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default' |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fillstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle "matplotlib.lines.Line2D.set_fillstyle") | {'full', 'left', 'right', 'bottom', 'top', 'none'} |
| [`gapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "matplotlib.lines.Line2D.set_gapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
| [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth") | float |
| [`marker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "matplotlib.lines.Line2D.set_marker") | marker style string, [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> or [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle") |
| [`markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor")<br> or [`mec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`markeredgewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth")<br> or [`mew`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth") | float |
| [`markerfacecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor")<br> or [`mfc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`markerfacecoloralt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt")<br> or [`mfcalt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`markersize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize")<br> or [`ms`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize") | float |
| [`markevery`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery "matplotlib.lines.Line2D.set_markevery") | None or int or (int, int) or slice or list\[int\] or float or (float, float) or list\[bool\] |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "matplotlib.lines.Line2D.set_picker") | float or callable\[\[Artist, Event\], tuple\[bool, dict\]\] |
| [`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius "matplotlib.lines.Line2D.set_pickradius") | float |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`solid_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle "matplotlib.lines.Line2D.set_solid_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
| [`solid_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle "matplotlib.lines.Line2D.set_solid_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | unknown |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata") | 1D array |
| [`ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata") | 1D array |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Examples using `matplotlib.axes.Axes.spy`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#examples-using-matplotlib-axes-axes-spy "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_spy_demos_thumb.png)

[Spy Demos](https://matplotlib.org/stable/gallery/images_contours_and_fields/spy_demos.html)

Spy Demos

On this page