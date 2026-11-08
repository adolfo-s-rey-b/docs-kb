[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#main-content)

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
    

matplotlib.lines.AxLine[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib-lines-axline "Link to this heading")

==================================================================================================================================================

class matplotlib.lines.AxLine(_xy1_, _xy2_, _slope_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1515-L1673)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine "Link to this definition")

Bases: [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

A helper class that implements [`axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
, by recomputing the artist transform at draw time.

Parameters:

**xy1**(float, float)

The first set of (x, y) coordinates for the line to pass through.

**xy2**(float, float) or None

The second set of (x, y) coordinates for the line to pass through. Both _xy2_ and _slope_ must be passed, but one of them must be None.

**slope**float or None

The slope of the line. Both _xy2_ and _slope_ must be passed, but one of them must be None.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1586-L1588)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_slope()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1598-L1600)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.get_slope "Link to this definition")

Return the _slope_ value of the line.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1545-L1584)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance used by this artist.

get\_xy1()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1590-L1592)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.get_xy1 "Link to this definition")

Return the _xy1_ value of the line.

get\_xy2()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1594-L1596)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.get_xy2 "Link to this definition")

Return the _xy2_ value of the line.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _dash\_capstyle\=<UNSET>_, _dash\_joinstyle\=<UNSET>_, _dashes\=<UNSET>_, _data\=<UNSET>_, _drawstyle\=<UNSET>_, _fillstyle\=<UNSET>_, _gapcolor\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _marker\=<UNSET>_, _markeredgecolor\=<UNSET>_, _markeredgewidth\=<UNSET>_, _markerfacecolor\=<UNSET>_, _markerfacecoloralt\=<UNSET>_, _markersize\=<UNSET>_, _markevery\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _slope\=<UNSET>_, _snap\=<UNSET>_, _solid\_capstyle\=<UNSET>_, _solid\_joinstyle\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xdata\=<UNSET>_, _xy1\=<UNSET>_, _xy2\=<UNSET>_, _ydata\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set "Link to this definition")

Set multiple properties at once.

a.set(a\=A, b\=B, c\=C)

is equivalent to

a.set\_a(A)
a.set\_b(B)
a.set\_c(C)

In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.

The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.

Supported properties are

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "matplotlib.lines.Line2D.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "matplotlib.lines.Line2D.set_antialiased") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")<br> or [`c`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`dash_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "matplotlib.lines.Line2D.set_dash_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`dash_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle "matplotlib.lines.Line2D.set_dash_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`dashes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes") | sequence of floats (on/off ink in points) or (None, None) |
> | [`data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data") | (2, N) array or two 1D arrays |
> | [`drawstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle")<br> or [`ds`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle") | {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default' |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fillstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle "matplotlib.lines.Line2D.set_fillstyle") | {'full', 'left', 'right', 'bottom', 'top', 'none'} |
> | [`gapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "matplotlib.lines.Line2D.set_gapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth") | float |
> | [`marker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "matplotlib.lines.Line2D.set_marker") | marker style string, [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> or [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle") |
> | [`markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor")<br> or [`mec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`markeredgewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth")<br> or [`mew`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth") | float |
> | [`markerfacecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor")<br> or [`mfc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`markerfacecoloralt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt")<br> or [`mfcalt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`markersize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize")<br> or [`ms`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize") | float |
> | [`markevery`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery "matplotlib.lines.Line2D.set_markevery") | None or int or (int, int) or slice or list\[int\] or float or (float, float) or list\[bool\] |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "matplotlib.lines.Line2D.set_picker") | float or callable\[\[Artist, Event\], tuple\[bool, dict\]\] |
> | [`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius "matplotlib.lines.Line2D.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`slope`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_slope "matplotlib.lines.AxLine.set_slope") | float |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`solid_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle "matplotlib.lines.Line2D.set_solid_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`solid_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle "matplotlib.lines.Line2D.set_solid_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata") | 1D array |
> | [`xy1`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_xy1 "matplotlib.lines.AxLine.set_xy1") | unknown |
> | [`xy2`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_xy2 "matplotlib.lines.AxLine.set_xy2") | unknown |
> | [`ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata") | 1D array |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_slope(_slope_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1654-L1673)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_slope "Link to this definition")

Set the _slope_ value of the line.

Note

You can only set _slope_ if the line was created using the _slope_ parameter. If the line was created using _xy2_, please use [`set_xy2`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_xy2 "matplotlib.lines.AxLine.set_xy2")
.

Parameters:

**slope**float

The slope of the line.

set\_xy1(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1602-L1621)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_xy1 "Link to this definition")

Set the _xy1_ value of the line.

Parameters:

**xy1**tuple\[float, float\]

Points for the line to pass through.

set\_xy2(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1623-L1652)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_xy2 "Link to this definition")

Set the _xy2_ value of the line.

Note

You can only set _xy2_ if the line was created using the _xy2_ parameter. If the line was created using _slope_, please use [`set_slope`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine.set_slope "matplotlib.lines.AxLine.set_slope")
.

Parameters:

**xy2**tuple\[float, float\]

Points for the line to pass through.

On this page