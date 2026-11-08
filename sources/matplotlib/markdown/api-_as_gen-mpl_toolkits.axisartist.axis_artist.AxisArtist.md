[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#main-content)

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
    

mpl\_toolkits.axisartist.axis\_artist.AxisArtist[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl-toolkits-axisartist-axis-artist-axisartist "Link to this heading")

=========================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.axis\_artist.AxisArtist(_axes_, _helper_, _offset\=None_, _axis\_direction\='bottom'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L680-L1147)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

An artist which draws axis (a line along which the n-th axes coord is constant) line, ticks, tick labels, and axis label.

Parameters:

**axes**[`mpl_toolkits.axisartist.axislines.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")

**helper**[`AxisArtistHelper`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxisArtistHelper.html#mpl_toolkits.axisartist.axislines.AxisArtistHelper "mpl_toolkits.axisartist.axislines.AxisArtistHelper")

property LABELPAD[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.LABELPAD "Link to this definition")

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L1098-L1108)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_axisline\_style()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L857-L859)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.get_axisline_style "Link to this definition")

Return the current axisline style.

get\_helper()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L818-L822)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.get_helper "Link to this definition")

Return axis artist helper instance.

get\_tightbbox(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L1073-L1096)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.get_tightbbox "Link to this definition")

Get the artist's bounding box in display space, taking clipping into account.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

Returns:

[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or None

The enclosing bounding box (in figure pixel coordinates), or None if clipping results in no intersection.

See also

[`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")

Get the artist bounding box, ignoring clipping.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L815-L816)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance used by this artist.

invert\_ticklabel\_direction()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L796-L799)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.invert_ticklabel_direction "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _axis\_direction\=<UNSET>_, _axislabel\_direction\=<UNSET>_, _axisline\_style\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _ticklabel\_direction\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set "Link to this definition")

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
> | [`axis_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction") | {"left", "bottom", "right", "top"} |
> | [`axislabel_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axislabel_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axislabel_direction") | {"+", "-"} |
> | [`axisline_style`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axisline_style "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axisline_style") | str or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`ticklabel_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_ticklabel_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_ticklabel_direction") | {"+", "-"} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_axis\_direction(_axis\_direction_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L742-L780)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction "Link to this definition")

Adjust the direction, text angle, and text alignment of tick labels and axis labels following the Matplotlib convention for the rectangle axes.

The _axis\_direction_ must be one of \[left, right, bottom, top\].

| Property | left | bottom | right | top |
| --- | --- | --- | --- | --- |
| ticklabel direction | "-" | "+" | "+" | "-" |
| axislabel direction | "-" | "+" | "+" | "-" |
| ticklabel angle | 90  | 0   | \-90 | 180 |
| ticklabel va | center | baseline | center | baseline |
| ticklabel ha | right | center | right | center |
| axislabel angle | 180 | 0   | 0   | 180 |
| axislabel va | center | top | center | bottom |
| axislabel ha | right | center | right | center |

Note that the direction "+" and "-" are relative to the direction of the increasing coordinate. Also, the text angles are actually relative to (90 + angle of the direction to the ticklabel), which gives 0 for bottom axis.

Parameters:

**axis\_direction**{"left", "bottom", "right", "top"}

set\_axislabel\_direction(_label\_direction_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L801-L813)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axislabel_direction "Link to this definition")

Adjust the direction of the axis label.

Note that the _label\_direction_s '+' and '-' are relative to the direction of the increasing coordinate.

Parameters:

**label\_direction**{"+", "-"}

set\_axisline\_style(_axisline\_style\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L824-L855)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axisline_style "Link to this definition")

Set the axisline style.

The new style is completely defined by the passed attributes. Existing style attributes are forgotten.

Parameters:

**axisline\_style**str or None

The line style, e.g. '->', optionally followed by a comma-separated list of attributes. Alternatively, the attributes can be provided as keywords.

If _None_ this returns a string containing the available styles.

Examples

The following two commands are equal:

\>>> set\_axisline\_style("->,size=1.5")
\>>> set\_axisline\_style("->", size\=1.5)

set\_label(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L1069-L1071)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_label "Link to this definition")

Set a label that will be displayed in the legend.

Parameters:

**s**object

_s_ will be converted to a string by calling [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
.

set\_ticklabel\_direction(_tick\_direction_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L782-L794)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_ticklabel_direction "Link to this definition")

Adjust the direction of the tick labels.

Note that the _tick\_direction_s '+' and '-' are relative to the direction of the increasing coordinate.

Parameters:

**tick\_direction**{"+", "-"}

toggle(_all\=None_, _ticks\=None_, _ticklabels\=None_, _label\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L1110-L1147)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.toggle "Link to this definition")

Toggle visibility of ticks, ticklabels, and (axis) label. To turn all off,

axis.toggle(all\=False)

To turn all off but ticks on

axis.toggle(all\=False, ticks\=True)

To turn all on but (axis) label off

axis.toggle(all\=True, label\=False)

zorder \= 2.5[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.zorder "Link to this definition")

Examples using `mpl_toolkits.axisartist.axis_artist.AxisArtist`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#examples-using-mpl-toolkits-axisartist-axis-artist-axisartist "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_direction_thumb.png)

[Ticklabel direction](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_direction.html)

Ticklabel direction

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

On this page