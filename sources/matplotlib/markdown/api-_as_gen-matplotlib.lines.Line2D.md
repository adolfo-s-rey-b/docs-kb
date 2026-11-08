[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#main-content)

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
    

matplotlib.lines.Line2D[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib-lines-line2d "Link to this heading")

==================================================================================================================================================

class matplotlib.lines.Line2D(_xdata_, _ydata_, _\*_, _linewidth\=None_, _linestyle\=None_, _color\=None_, _gapcolor\=None_, _marker\=None_, _markersize\=None_, _markeredgewidth\=None_, _markeredgecolor\=None_, _markerfacecolor\=None_, _markerfacecoloralt\='none'_, _fillstyle\=None_, _antialiased\=None_, _dash\_capstyle\=None_, _solid\_capstyle\=None_, _dash\_joinstyle\=None_, _solid\_joinstyle\=None_, _pickradius\=5_, _drawstyle\=None_, _markevery\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L252-L1512)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

A line - the line can have both a solid linestyle connecting all the vertices, and a marker at each vertex. Additionally, the drawing of the solid line is influenced by the drawstyle, e.g., one can create "stepped" lines in various styles.

Create a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instance with _x_ and _y_ data in sequences of _xdata_, _ydata_.

Additional keyword arguments are [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties:

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
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`solid_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle "matplotlib.lines.Line2D.set_solid_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`solid_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle "matplotlib.lines.Line2D.set_solid_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | unknown |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata") | 1D array |
> | [`ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata") | 1D array |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See [`set_linestyle()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")
 for a description of the line styles, [`set_marker()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "matplotlib.lines.Line2D.set_marker")
 for a description of the markers, and [`set_drawstyle()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle")
 for a description of the draw styles.

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L452-L520)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.contains "Link to this definition")

Test whether _mouseevent_ occurred on the line.

An event is deemed to have occurred "on" the line if it is less than `self.pickradius` (default: 5 points) away from it. Use [`get_pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_pickradius "matplotlib.lines.Line2D.get_pickradius")
 or [`set_pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius "matplotlib.lines.Line2D.set_pickradius")
 to get or set the pick radius.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

A dictionary `{'ind': pointlist}`, where _pointlist_ is a list of points of the line that are within the pickradius around the event position.

TODO: sort returned indices by distance

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L776-L926)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

drawStyleKeys \= \['default', 'steps-mid', 'steps-pre', 'steps-post', 'steps'\][#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.drawStyleKeys "Link to this definition")

drawStyles \= {'default': '\_draw\_lines', 'steps': '\_draw\_steps\_pre', 'steps-mid': '\_draw\_steps\_mid', 'steps-post': '\_draw\_steps\_post', 'steps-pre': '\_draw\_steps\_pre'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.drawStyles "Link to this definition")

fillStyles \= ('full', 'left', 'right', 'bottom', 'top', 'none')[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.fillStyles "Link to this definition")

filled\_markers \= ('.', 'o', 'v', '^', '<', '>', '8', 's', 'p', '\*', 'h', 'H', 'D', 'd', 'P', 'X')[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.filled_markers "Link to this definition")

get\_aa()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L928-L930)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_aa "Link to this definition")

Alias for [`get_antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_antialiased "matplotlib.lines.Line2D.get_antialiased")
.

get\_antialiased()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L928-L930)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_antialiased "Link to this definition")

Return whether antialiased rendering is used.

get\_bbox()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L655-L659)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_bbox "Link to this definition")

Get the bounding box of this line.

get\_c()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L932-L938)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_c "Link to this definition")

Alias for [`get_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "matplotlib.lines.Line2D.get_color")
.

get\_color()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L932-L938)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_color "Link to this definition")

Return the line color.

See also [`set_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")
.

get\_dash\_capstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1487-L1493)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_dash_capstyle "Link to this definition")

Return the [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 for dashed lines.

See also [`set_dash_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "matplotlib.lines.Line2D.set_dash_capstyle")
.

get\_dash\_joinstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1439-L1445)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_dash_joinstyle "Link to this definition")

Return the [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 for dashed lines.

See also [`set_dash_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle "matplotlib.lines.Line2D.set_dash_joinstyle")
.

get\_data(_orig\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1039-L1045)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_data "Link to this definition")

Return the line data as an `(xdata, ydata)` pair.

If _orig_ is _True_, return the original data.

get\_drawstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L940-L946)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_drawstyle "Link to this definition")

Return the drawstyle.

See also [`set_drawstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle")
.

get\_ds()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L940-L946)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ds "Link to this definition")

Alias for [`get_drawstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_drawstyle "matplotlib.lines.Line2D.get_drawstyle")
.

get\_fillstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L547-L553)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_fillstyle "Link to this definition")

Return the marker fill style.

See also [`set_fillstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle "matplotlib.lines.Line2D.set_fillstyle")
.

get\_gapcolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L948-L954)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_gapcolor "Link to this definition")

Return the line gapcolor.

See also [`set_gapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "matplotlib.lines.Line2D.set_gapcolor")
.

get\_linestyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L956-L962)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_linestyle "Link to this definition")

Return the linestyle.

See also [`set_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")
.

get\_linewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L964-L970)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_linewidth "Link to this definition")

Return the linewidth in points.

See also [`set_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth")
.

get\_ls()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L956-L962)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ls "Link to this definition")

Alias for [`get_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_linestyle "matplotlib.lines.Line2D.get_linestyle")
.

get\_lw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L964-L970)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_lw "Link to this definition")

Alias for [`get_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_linewidth "matplotlib.lines.Line2D.get_linewidth")
.

get\_marker()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L972-L978)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_marker "Link to this definition")

Return the line marker.

See also [`set_marker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "matplotlib.lines.Line2D.set_marker")
.

get\_markeredgecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L980-L996)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markeredgecolor "Link to this definition")

Return the marker edge color.

See also [`set_markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor")
.

get\_markeredgewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L998-L1004)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markeredgewidth "Link to this definition")

Return the marker edge width in points.

See also [`set_markeredgewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth")
.

get\_markerfacecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1015-L1021)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markerfacecolor "Link to this definition")

Return the marker face color.

See also [`set_markerfacecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor")
.

get\_markerfacecoloralt()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1023-L1029)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markerfacecoloralt "Link to this definition")

Return the alternate marker face color.

See also [`set_markerfacecoloralt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt")
.

get\_markersize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1031-L1037)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markersize "Link to this definition")

Return the marker size in points.

See also [`set_markersize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize")
.

get\_markevery()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L634-L640)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markevery "Link to this definition")

Return the markevery setting for marker subsampling.

See also [`set_markevery`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery "matplotlib.lines.Line2D.set_markevery")
.

get\_mec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L980-L996)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_mec "Link to this definition")

Alias for [`get_markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markeredgecolor "matplotlib.lines.Line2D.get_markeredgecolor")
.

get\_mew()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L998-L1004)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_mew "Link to this definition")

Alias for [`get_markeredgewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markeredgewidth "matplotlib.lines.Line2D.get_markeredgewidth")
.

get\_mfc()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1015-L1021)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_mfc "Link to this definition")

Alias for [`get_markerfacecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markerfacecolor "matplotlib.lines.Line2D.get_markerfacecolor")
.

get\_mfcalt()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1023-L1029)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_mfcalt "Link to this definition")

Alias for [`get_markerfacecoloralt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markerfacecoloralt "matplotlib.lines.Line2D.get_markerfacecoloralt")
.

get\_ms()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1031-L1037)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ms "Link to this definition")

Alias for [`get_markersize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_markersize "matplotlib.lines.Line2D.get_markersize")
.

get\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1073-L1077)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_path "Link to this definition")

Return the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 associated with this line.

get\_pickradius()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L522-L528)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_pickradius "Link to this definition")

Return the pick radius used for containment tests.

See [`contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.contains "matplotlib.lines.Line2D.contains")
 for more details.

get\_solid\_capstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1495-L1501)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_solid_capstyle "Link to this definition")

Return the [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 for solid lines.

See also [`set_solid_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle "matplotlib.lines.Line2D.set_solid_capstyle")
.

get\_solid\_joinstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1447-L1453)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_solid_joinstyle "Link to this definition")

Return the [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 for solid lines.

See also [`set_solid_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle "matplotlib.lines.Line2D.set_solid_joinstyle")
.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L661-L670)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_window_extent "Link to this definition")

Get the artist's bounding box in display space, ignoring clipping.

The bounding box's width and height are non-negative.

Subclasses should override for inclusion in the bounding box "tight" calculation. Default is to return an empty bounding box at 0, 0.

Warning

The extent can change due to any changes in the transform stack, such as changing the Axes limits, the figure size, the canvas used (as is done when saving a figure), or the DPI.

Relying on a once-retrieved window extent can lead to unexpected behavior in various cases such as interactive figures being resized or moved to a screen with different dpi, or figures that look fine on screen render incorrectly when saved to file.

To get accurate results you may need to manually call [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 or [`draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
 to have Matplotlib compute the rendered size.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

See also

[`Artist.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "matplotlib.artist.Artist.get_tightbbox")

Get the artist bounding box, taking clipping into account.

get\_xdata(_orig\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1047-L1058)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xdata "Link to this definition")

Return the xdata.

If _orig_ is _True_, return the original data, else the processed data.

get\_xydata()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1079-L1083)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xydata "Link to this definition")

Return the _xy_ data as a (N, 2) array.

get\_ydata(_orig\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1060-L1071)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ydata "Link to this definition")

Return the ydata.

If _orig_ is _True_, return the original data, else the processed data.

is\_dashed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1503-L1512)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.is_dashed "Link to this definition")

Return whether line has a dashed linestyle.

A custom linestyle is assumed to be dashed, we do not inspect the `onoffseq` directly.

See also [`set_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")
.

lineStyles \= {'': '\_draw\_nothing', ' ': '\_draw\_nothing', '-': '\_draw\_solid', '--': '\_draw\_dashed', '-.': '\_draw\_dash\_dot', ':': '\_draw\_dotted', 'None': '\_draw\_nothing'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.lineStyles "Link to this definition")

markers \= {' ': 'nothing', '': 'nothing', '\*': 'star', '+': 'plus', ',': 'pixel', '.': 'point', '1': 'tri\_down', '2': 'tri\_up', '3': 'tri\_left', '4': 'tri\_right', '8': 'octagon', '<': 'triangle\_left', '>': 'triangle\_right', 'D': 'diamond', 'H': 'hexagon2', 'None': 'nothing', 'P': 'plus\_filled', 'X': 'x\_filled', '^': 'triangle\_up', '\_': 'hline', 'd': 'thin\_diamond', 'h': 'hexagon1', 'none': 'nothing', 'o': 'circle', 'p': 'pentagon', 's': 'square', 'v': 'triangle\_down', 'x': 'x', '|': 'vline', 0: 'tickleft', 1: 'tickright', 10: 'caretupbase', 11: 'caretdownbase', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.markers "Link to this definition")

property pickradius[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.pickradius "Link to this definition")

Return the pick radius used for containment tests.

See [`contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.contains "matplotlib.lines.Line2D.contains")
 for more details.

recache(_always\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L696-L743)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.recache "Link to this definition")

recache\_always()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L693-L694)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.recache_always "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _dash\_capstyle\=<UNSET>_, _dash\_joinstyle\=<UNSET>_, _dashes\=<UNSET>_, _data\=<UNSET>_, _drawstyle\=<UNSET>_, _fillstyle\=<UNSET>_, _gapcolor\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _marker\=<UNSET>_, _markeredgecolor\=<UNSET>_, _markeredgewidth\=<UNSET>_, _markerfacecolor\=<UNSET>_, _markerfacecoloralt\=<UNSET>_, _markersize\=<UNSET>_, _markevery\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _solid\_capstyle\=<UNSET>_, _solid\_joinstyle\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xdata\=<UNSET>_, _ydata\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set "Link to this definition")

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
> | [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "matplotlib.lines.Line2D.set_antialiased") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`dash_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "matplotlib.lines.Line2D.set_dash_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`dash_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle "matplotlib.lines.Line2D.set_dash_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`dashes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes") | sequence of floats (on/off ink in points) or (None, None) |
> | [`data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data") | (2, N) array or two 1D arrays |
> | [`drawstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle") | {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default' |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fillstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle "matplotlib.lines.Line2D.set_fillstyle") | {'full', 'left', 'right', 'bottom', 'top', 'none'} |
> | [`gapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "matplotlib.lines.Line2D.set_gapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth") | float |
> | [`marker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "matplotlib.lines.Line2D.set_marker") | marker style string, [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> or [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle") |
> | [`markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`markeredgewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth") | float |
> | [`markerfacecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`markerfacecoloralt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`markersize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize") | float |
> | [`markevery`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery "matplotlib.lines.Line2D.set_markevery") | None or int or (int, int) or slice or list\[int\] or float or (float, float) or list\[bool\] |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "matplotlib.lines.Line2D.set_picker") | float or callable\[\[Artist, Event\], tuple\[bool, dict\]\] |
> | [`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius "matplotlib.lines.Line2D.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`solid_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle "matplotlib.lines.Line2D.set_solid_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`solid_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle "matplotlib.lines.Line2D.set_solid_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | unknown |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata") | 1D array |
> | [`ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata") | 1D array |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_aa(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1085-L1095)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_aa "Link to this definition")

Alias for [`set_antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "matplotlib.lines.Line2D.set_antialiased")
.

set\_antialiased(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1085-L1095)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased "Link to this definition")

Set whether to use antialiased rendering.

Parameters:

**b**bool

set\_c(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1097-L1107)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_c "Link to this definition")

Alias for [`set_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")
.

set\_color(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1097-L1107)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "Link to this definition")

Set the color of the line.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_dash\_capstyle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1455-L1469)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "Link to this definition")

How to draw the end caps if the line is [`is_dashed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.is_dashed "matplotlib.lines.Line2D.is_dashed")
.

The default capstyle is `[rcParams["lines.dash_capstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.dash_capstyle#rcparam-lines-dash-capstyle) ` (default: `<CapStyle.butt: 'butt'>`).

Parameters:

**s**[`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or {'butt', 'projecting', 'round'}

set\_dash\_joinstyle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1407-L1421)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle "Link to this definition")

How to join segments of the line if it [`is_dashed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.is_dashed "matplotlib.lines.Line2D.is_dashed")
.

The default joinstyle is `[rcParams["lines.dash_joinstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.dash_joinstyle#rcparam-lines-dash-joinstyle) ` (default: `<JoinStyle.round: 'round'>`).

Parameters:

**s**[`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 or {'miter', 'round', 'bevel'}

set\_dashes(_seq_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1361-L1383)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "Link to this definition")

Set the dash sequence.

The dash sequence is a sequence of floats of even length describing the length of dashes and spaces in points.

For example, (5, 2, 1, 2) describes a sequence of 5 point and 1 point dashes separated by 2 point spaces.

See also [`set_gapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "matplotlib.lines.Line2D.set_gapcolor")
, which allows those spaces to be filled with a color.

Parameters:

**seq**sequence of floats (on/off ink in points) or (None, None)

If _seq_ is empty or `(None, None)`, the linestyle will be set to solid.

set\_data(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L672-L691)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "Link to this definition")

Set the x and y data.

Parameters:

**\*args**(2, N) array or two 1D arrays

See also

[`set_xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")

[`set_ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")

set\_drawstyle(_drawstyle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1109-L1142)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "Link to this definition")

Set the drawstyle of the plot.

The drawstyle determines how the points are connected.

Parameters:

**drawstyle**{'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default'

For 'default', the points are connected with straight lines.

The steps variants connect the points with step-like lines, i.e. horizontal lines with vertical steps. They differ in the location of the step:

*   'steps-pre': The step is at the beginning of the line segment, i.e. the line will be at the y-value of point to the right.
    
*   'steps-mid': The step is halfway between the points.
    
*   'steps-post: The step is at the end of the line segment, i.e. the line will be at the y-value of the point to the left.
    
*   'steps' is equal to 'steps-pre' and is maintained for backward-compatibility.
    

For examples see [Step Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/step_demo.html)
.

set\_ds(_drawstyle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1109-L1142)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ds "Link to this definition")

Alias for [`set_drawstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle "matplotlib.lines.Line2D.set_drawstyle")
.

set\_fillstyle(_fs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L555-L573)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle "Link to this definition")

Set the marker fill style.

Parameters:

**fs**{'full', 'left', 'right', 'bottom', 'top', 'none'}

Possible values:

*   'full': Fill the whole marker with the _markerfacecolor_.
    
*   'left', 'right', 'bottom', 'top': Fill the marker half at the given side with the _markerfacecolor_. The other half of the marker is filled with _markerfacecoloralt_.
    
*   'none': No filling.
    

For examples see [Marker fill styles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html#marker-fill-styles)
.

set\_gapcolor(_gapcolor_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1144-L1165)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "Link to this definition")

Set a color to fill the gaps in the dashed line style.

Note

Striped lines are created by drawing two interleaved dashed lines. There can be overlaps between those two, which may result in artifacts when using transparency.

This functionality is experimental and may change.

Parameters:

**gapcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or None

The color with which to fill the gaps. If None, the gaps are unfilled.

set\_linestyle(_ls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1182-L1235)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "Link to this definition")

Set the linestyle of the line.

Parameters:

**ls**{'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)

Possible values:

*   A string:
    
    | linestyle | description |
    | --- | --- |
    | `'-'` or `'solid'` | solid line |
    | `'--'` or `'dashed'` | dashed line |
    | `'-.'` or `'dashdot'` | dash-dotted line |
    | `':'` or `'dotted'` | dotted line |
    | `''` or `'none'` (discouraged: `'None'`, `' '`) | draw nothing |
    
*   A tuple describing the start position and lengths of dashes and spaces:
    
    > (offset, onoffseq)
    
    where
    
    *   _offset_ is a float specifying the offset (in points); i.e. how much is the dash pattern shifted.
        
    *   _onoffseq_ is a sequence of on and off ink in points. There can be arbitrary many pairs of on and off values.
        
    
    Example: The tuple `(0, (10, 5, 1, 5))` means that the pattern starts at the beginning of the line. It draws a 10 point long dash, then a 5 point long space, then a 1 point long dash, followed by a 5 point long space, and then the pattern repeats.
    
    See also [`set_dashes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes")
    .
    

For examples see [Linestyles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)
.

set\_linewidth(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1167-L1180)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "Link to this definition")

Set the line width in points.

Parameters:

**w**float

Line width, in points.

set\_ls(_ls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1182-L1235)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ls "Link to this definition")

Alias for [`set_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")
.

set\_lw(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1167-L1180)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_lw "Link to this definition")

Alias for [`set_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth")
.

set\_marker(_marker_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1237-L1249)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker "Link to this definition")

Set the line marker.

Parameters:

**marker**marker style string, [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 or [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")

See [`markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")
 for full description of possible arguments.

set\_markeredgecolor(_ec_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1265-L1273)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "Link to this definition")

Set the marker edge color.

Parameters:

**ec**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_markeredgewidth(_ew_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1295-L1307)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "Link to this definition")

Set the marker edge width in points.

Parameters:

**ew**float

Marker edge width, in points.

set\_markerfacecolor(_fc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1275-L1283)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "Link to this definition")

Set the marker face color.

Parameters:

**fc**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_markerfacecoloralt(_fc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1285-L1293)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "Link to this definition")

Set the alternate marker face color.

Parameters:

**fc**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_markersize(_sz_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1309-L1321)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "Link to this definition")

Set the marker size in points.

Parameters:

**sz**float

Marker size, in points.

set\_markevery(_every_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L575-L632)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery "Link to this definition")

Set the markevery property to subsample the plot when using markers.

e.g., if `every=5`, every 5-th marker will be plotted.

Parameters:

**every**None or int or (int, int) or slice or list\[int\] or float or (float, float) or list\[bool\]

Which markers to plot.

*   `every=None`: every point will be plotted.
    
*   `every=N`: every N-th marker will be plotted starting with marker 0.
    
*   `every=(start, N)`: every N-th marker, starting at index _start_, will be plotted.
    
*   `every=slice(start, end, N)`: every N-th marker, starting at index _start_, up to but not including index _end_, will be plotted.
    
*   `every=[i, j, m, ...]`: only markers at the given indices will be plotted.
    
*   `every=[True, False, True, ...]`: only positions that are True will be plotted. The list must have the same length as the data points.
    
*   `every=0.1`, (i.e. a float): markers will be spaced at approximately equal visual distances along the line; the distance along the line between markers is determined by multiplying the display-coordinate distance of the Axes bounding-box diagonal by the value of _every_.
    
*   `every=(0.5, 0.1)` (i.e. a length-2 tuple of float): similar to `every=0.1` but the first marker will be offset along the line by 0.5 multiplied by the display-coordinate-diagonal-distance along the line.
    

For examples see [Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)
.

Notes

Setting _markevery_ will still only draw markers at actual data points. While the float argument form aims for uniform visual spacing, it has to coerce from the ideal spacing to the nearest available data point. Depending on the number and distribution of data points, the result may still not look evenly spaced.

When using a start offset to specify the first marker, the offset will be from the first data point which may be different from the first the visible data point if the plot is zoomed in.

If zooming in on a plot when using float arguments then the actual data points that have markers will change because the distance between markers is always determined from the display-coordinates axes-bounding-box-diagonal regardless of the actual axes data limits.

set\_mec(_ec_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1265-L1273)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_mec "Link to this definition")

Alias for [`set_markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor")
.

set\_mew(_ew_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1295-L1307)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_mew "Link to this definition")

Alias for [`set_markeredgewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth "matplotlib.lines.Line2D.set_markeredgewidth")
.

set\_mfc(_fc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1275-L1283)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_mfc "Link to this definition")

Alias for [`set_markerfacecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor")
.

set\_mfcalt(_fc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1285-L1293)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_mfcalt "Link to this definition")

Alias for [`set_markerfacecoloralt`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt "matplotlib.lines.Line2D.set_markerfacecoloralt")
.

set\_ms(_sz_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1309-L1321)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ms "Link to this definition")

Alias for [`set_markersize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize "matplotlib.lines.Line2D.set_markersize")
.

set\_picker(_p_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L642-L653)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker "Link to this definition")

Set the event picker details for the line.

Parameters:

**p**float or callable\[\[Artist, Event\], tuple\[bool, dict\]\]

If a float, it is used as the pick radius in points.

set\_pickradius(_pickradius_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L530-L543)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius "Link to this definition")

Set the pick radius used for containment tests.

See [`contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.contains "matplotlib.lines.Line2D.contains")
 for more details.

Parameters:

**pickradius**float

Pick radius, in points.

set\_solid\_capstyle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1471-L1485)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle "Link to this definition")

How to draw the end caps if the line is solid (not [`is_dashed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.is_dashed "matplotlib.lines.Line2D.is_dashed")
)

The default capstyle is `[rcParams["lines.solid_capstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.solid_capstyle#rcparam-lines-solid-capstyle) ` (default: `<CapStyle.projecting: 'projecting'>`).

Parameters:

**s**[`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or {'butt', 'projecting', 'round'}

set\_solid\_joinstyle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1423-L1437)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle "Link to this definition")

How to join segments if the line is solid (not [`is_dashed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.is_dashed "matplotlib.lines.Line2D.is_dashed")
).

The default joinstyle is `[rcParams["lines.solid_joinstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.solid_joinstyle#rcparam-lines-solid-joinstyle) ` (default: `<JoinStyle.round: 'round'>`).

Parameters:

**s**[`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 or {'miter', 'round', 'bevel'}

set\_transform(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L770-L774)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_transform "Link to this definition")

Set the artist transform.

Parameters:

**t**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

set\_xdata(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1323-L1340)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "Link to this definition")

Set the data array for x.

Parameters:

**x**1D array

See also

[`set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")

[`set_ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")

set\_ydata(_y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1342-L1359)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "Link to this definition")

Set the data array for y.

Parameters:

**y**1D array

See also

[`set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")

[`set_xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")

update\_from(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1385-L1405)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.update_from "Link to this definition")

Copy properties from _other_ to self.

zorder \= 2[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.zorder "Link to this definition")

Examples using `matplotlib.lines.Line2D`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#examples-using-matplotlib-lines-line2d "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_line_demo_dash_control_thumb.png)

[Dashed line style configuration](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html)

Dashed line style configuration

![](https://matplotlib.org/stable/_images/sphx_glr_stem_plot_thumb.png)

[Stem plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html)

Stem plot

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

![](https://matplotlib.org/stable/_images/sphx_glr_figure_title_thumb.png)

[Figure labels: suptitle, supxlabel, supylabel](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html)

Figure labels: suptitle, supxlabel, supylabel

![](https://matplotlib.org/stable/_images/sphx_glr_date_index_formatter_thumb.png)

[Custom tick formatter for time series](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html)

Custom tick formatter for time series

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_basic_thumb.png)

[Annotating a plot](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_basic.html)

Annotating a plot

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_polar_thumb.png)

[Annotate polar plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_polar.html)

Annotate polar plots

![](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_thumb.png)

[Annotation arrow style reference](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html)

Annotation arrow style reference

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_thumb.png)

[Legend Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

Legend Demo

![](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_thumb.png)

[Compose custom legends](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html)

Compose custom legends

![](https://matplotlib.org/stable/_images/sphx_glr_line_with_text_thumb.png)

[Artist within an artist](https://matplotlib.org/stable/gallery/text_labels_and_annotations/line_with_text.html)

Artist within an artist

![](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_thumb.png)

[Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)

Reference for Matplotlib artists

![](https://matplotlib.org/stable/_images/sphx_glr_path_patch_thumb.png)

[PathPatch object](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html)

PathPatch object

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple_thumb.png)

[Parasite Simple](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple.html)

Parasite Simple

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes_thumb.png)

[Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)

Parasite Axes demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_thumb.png)

[Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)

Parasite axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_simple_anim_thumb.gif)

[Basic animated line plot](https://matplotlib.org/stable/gallery/animation/simple_anim.html)

Basic animated line plot

![](https://matplotlib.org/stable/_images/sphx_glr_animate_decay_thumb.gif)

[Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)

Decay

![](https://matplotlib.org/stable/_images/sphx_glr_double_pendulum_thumb.gif)

[The double pendulum problem](https://matplotlib.org/stable/gallery/animation/double_pendulum.html)

The double pendulum problem

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

![](https://matplotlib.org/stable/_images/sphx_glr_strip_chart_thumb.gif)

[Oscilloscope](https://matplotlib.org/stable/gallery/animation/strip_chart.html)

Oscilloscope

![](https://matplotlib.org/stable/_images/sphx_glr_unchained_thumb.gif)

[Matplotlib unchained](https://matplotlib.org/stable/gallery/animation/unchained.html)

Matplotlib unchained

![](https://matplotlib.org/stable/_images/sphx_glr_annotated_cursor_thumb.png)

[Annotated cursor](https://matplotlib.org/stable/gallery/widgets/annotated_cursor.html)

Annotated cursor

![](https://matplotlib.org/stable/_images/sphx_glr_buttons_thumb.png)

[Buttons](https://matplotlib.org/stable/gallery/widgets/buttons.html)

Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_check_buttons_thumb.png)

[Check buttons](https://matplotlib.org/stable/gallery/widgets/check_buttons.html)

Check buttons

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_thumb.png)

[Radio Buttons](https://matplotlib.org/stable/gallery/widgets/radio_buttons.html)

Radio Buttons

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

![](https://matplotlib.org/stable/_images/sphx_glr_range_slider_thumb.png)

[Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)

Image scaling using a RangeSlider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

![](https://matplotlib.org/stable/_images/sphx_glr_span_selector_thumb.png)

[Span Selector](https://matplotlib.org/stable/gallery/widgets/span_selector.html)

Span Selector

![](https://matplotlib.org/stable/_images/sphx_glr_textbox_thumb.png)

[Textbox](https://matplotlib.org/stable/gallery/widgets/textbox.html)

Textbox

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_thumb.png)

[Cross-hair cursor](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html)

Cross-hair cursor

![](https://matplotlib.org/stable/_images/sphx_glr_data_browser_thumb.png)

[Data browser](https://matplotlib.org/stable/gallery/event_handling/data_browser.html)

Data browser

![](https://matplotlib.org/stable/_images/sphx_glr_legend_picking_thumb.png)

[Legend picking](https://matplotlib.org/stable/gallery/event_handling/legend_picking.html)

Legend picking

![](https://matplotlib.org/stable/_images/sphx_glr_looking_glass_thumb.png)

[Looking glass](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html)

Looking glass

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo2_thumb.png)

[Pick event demo 2](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo2.html)

Pick event demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_poly_editor_thumb.png)

[Polygon editor](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html)

Polygon editor

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

![](https://matplotlib.org/stable/_images/sphx_glr_anchored_artists_thumb.png)

[Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)

Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_fig_x_thumb.png)

[Add lines directly to a figure](https://matplotlib.org/stable/gallery/misc/fig_x.html)

Add lines directly to a figure

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_set_and_get_thumb.png)

[Set and get properties](https://matplotlib.org/stable/gallery/misc/set_and_get.html)

Set and get properties

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_line_thumb.png)

[Apply SVG filter to a line](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html)

Apply SVG filter to a line

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_skewt_thumb.png)

[SkewT-logP diagram: using transforms and custom projections](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

SkewT-logP diagram: using transforms and custom projections

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)

[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)

Artist tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_animations_thumb.gif)

[Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html)

Animations using Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_blitting_thumb.png)

[Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html)

Faster rendering by using blitting

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_thumb.png)

[Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)

Legend guide

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

On this page