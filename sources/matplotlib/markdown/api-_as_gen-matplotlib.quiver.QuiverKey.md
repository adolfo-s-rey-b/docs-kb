[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#main-content)

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
    

matplotlib.quiver.QuiverKey[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib-quiver-quiverkey "Link to this heading")

==============================================================================================================================================================

class matplotlib.quiver.QuiverKey(_Q_, _X_, _Y_, _U_, _label_, _\*_, _angle\=0_, _coordinates\='axes'_, _color\=None_, _labelsep\=0.1_, _labelpos\='N'_, _labelcolor\=None_, _fontproperties\=None_, _zorder\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/quiver.py#L277-L438)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

Labelled arrow for use as a quiver plot scale key.

Add a key to a quiver plot.

The positioning of the key depends on _X_, _Y_, _coordinates_, and _labelpos_. If _labelpos_ is 'N' or 'S', _X_, _Y_ give the position of the middle of the key arrow. If _labelpos_ is 'E', _X_, _Y_ positions the head, and if _labelpos_ is 'W', _X_, _Y_ positions the tail; in either of these two cases, _X_, _Y_ is somewhere in the middle of the arrow+label key object.

Parameters:

**Q**[`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")

A [`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
 object as returned by a call to [`quiver()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
.

**X, Y**float

The location of the key.

**U**float

The length of the key.

**label**str

The key label (e.g., length and units of the key).

**angle**float, default: 0

The angle of the key arrow, in degrees anti-clockwise from the horizontal axis.

**coordinates**{'axes', 'figure', 'data', 'inches'}, default: 'axes'

Coordinate system and units for _X_, _Y_: 'axes' and 'figure' are normalized coordinate systems with (0, 0) in the lower left and (1, 1) in the upper right; 'data' are the axes data coordinates (used for the locations of the vectors in the quiver plot itself); 'inches' is position in the figure in inches, with (0, 0) at the lower left corner.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Overrides face and edge colors from _Q_.

**labelpos**{'N', 'S', 'E', 'W'}

Position the label above, below, to the right, to the left of the arrow, respectively.

**labelsep**float, default: 0.1

Distance in inches between the arrow and the label.

**labelcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: `[rcParams["text.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.color#rcparam-text-color) ` (default: `'black'`)

Label color.

**fontproperties**dict, optional

A dictionary with keyword arguments accepted by the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 initializer: _family_, _style_, _variant_, _size_, _weight_.

**zorder**float

The zorder of the key. The default is 0.1 above _Q_.

**\*\*kwargs**

Any additional keyword arguments are used to override vector properties taken from _Q_.

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/quiver.py#L430-L438)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.contains "Link to this definition")

Test whether the artist contains the mouse event.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

An artist-specific dictionary of details of the event context, such as which points are contained in the pick radius. See the individual Artist subclasses for details.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/quiver.py#L408-L415)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

property fontproperties[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.fontproperties "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use quiverkey.text.get\_fontproperties() instead.

halign \= {'E': 'left', 'N': 'center', 'S': 'center', 'W': 'right'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.halign "Link to this definition")

property kw[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.kw "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

property labelcolor[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.labelcolor "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use quiverkey.text.get\_color() instead.

property labelsep[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.labelsep "Link to this definition")

pivot \= {'E': 'tip', 'N': 'middle', 'S': 'middle', 'W': 'tail'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.pivot "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.set "Link to this definition")

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
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | unknown |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_figure(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/quiver.py#L426-L428)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.set_figure "Link to this definition")

Set the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 instance the artist belongs to.

Warning

This function should typically not be called by users.

This is a low-level API and only modifies the internal state of the Artist. Only modifying this is not enough and will typically lead to an inconsistent state, because the state of the figure has to be changed as well.

Users should typically instead call one of the high-level APIs, i.e. [`Figure.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
 or one of the Axes methods [Adding artists](https://matplotlib.org/stable/api/axes_api.html#axes-api-adding-artists)
.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

valign \= {'E': 'center', 'N': 'bottom', 'S': 'top', 'W': 'center'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.valign "Link to this definition")

property verts[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey.verts "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use \[p.vertices for p in quiverkey.vector.get\_paths()\] instead.

Examples using `matplotlib.quiver.QuiverKey`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#examples-using-matplotlib-quiver-quiverkey "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_demo_thumb.png)

[Advanced quiver and quiverkey functions](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_demo.html)

Advanced quiver and quiverkey functions

On this page