[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#main-content)

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
    

mpl\_toolkits.mplot3d.axis3d.Axis[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl-toolkits-mplot3d-axis3d-axis "Link to this heading")

==============================================================================================================================================================================

class mpl\_toolkits.mplot3d.axis3d.Axis(_axes_, _\*_, _rotate\_label\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L65-L782)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis "Link to this definition")

Bases: [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")

An Axis class for the 3D plots.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to which the created Axis belongs.

**pickradius**float

The acceptance radius for containment tests. See also [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains")
.

**clear**bool, default: True

Whether to clear the Axis on creation. This is not required, e.g., when creating an Axis as part of an Axes, as `Axes.clear` will call `Axis.clear`. .. versionadded:: 3.8

active\_pane()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L437-L448)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.active_pane "Link to this definition")

property adir[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.adir "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.6:

property d\_interval[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.d_interval "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.6: Use get\_data\_interval instead.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L687-L696)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

draw\_grid(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L698-L740)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.draw_grid "Link to this definition")

draw\_pane(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L450-L462)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.draw_pane "Link to this definition")

Draw pane.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

get\_label\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L253-L262)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.get_label_position "Link to this definition")

Get the label position.

Returns:

**str**{'lower', 'upper', 'both', 'default', 'none'}

The position of the axis label.

get\_major\_ticks(_numticks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L200-L206)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.get_major_ticks "Link to this definition")

Return the list of major [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
s.

Warning

Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that changes to individual ticks will not survive if you work on the figure further (including also panning/zooming on a displayed figure).

Working on the individual ticks is a method of last resort. Use [`set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 instead if possible.

get\_minor\_ticks(_numticks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L208-L214)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.get_minor_ticks "Link to this definition")

Return the list of minor [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
s.

Warning

Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that changes to individual ticks will not survive if you work on the figure further (including also panning/zooming on a displayed figure).

Working on the individual ticks is a method of last resort. Use [`set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 instead if possible.

get\_rotate\_label(_text_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L290-L294)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.get_rotate_label "Link to this definition")

get\_ticks\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L229-L238)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.get_ticks_position "Link to this definition")

Get the ticks position.

Returns:

**str**{'lower', 'upper', 'both', 'default', 'none'}

The position of the bolded axis lines, ticks, and tick labels.

get\_tightbbox(_renderer\=None_, _\*_, _for\_layout\_only\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L744-L773)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.get_tightbbox "Link to this definition")

Return a bounding box that encloses the axis. It only accounts tick labels, axis label, and offsetText.

If _for\_layout\_only_ is True, then the width of the label (if this is an x-axis) or the height of the label (if this is a y-axis) is collapsed to near zero. This allows tight/constrained\_layout to ignore too-long labels when doing their layout.

init3d()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L196-L198)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.init3d "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.6:

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _converter\=<UNSET>_, _data\_interval\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _inverted\=<UNSET>_, _label\=<UNSET>_, _label\_coords\=<UNSET>_, _label\_position\=<UNSET>_, _label\_text\=<UNSET>_, _major\_formatter\=<UNSET>_, _major\_locator\=<UNSET>_, _minor\_formatter\=<UNSET>_, _minor\_locator\=<UNSET>_, _mouseover\=<UNSET>_, _pane\_color\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _remove\_overlapping\_locs\=<UNSET>_, _rotate\_label\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _tick\_params\=<UNSET>_, _ticklabels\=<UNSET>_, _ticks\=<UNSET>_, _ticks\_position\=<UNSET>_, _transform\=<UNSET>_, _units\=<UNSET>_, _url\=<UNSET>_, _view\_interval\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set "Link to this definition")

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
> | [`converter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_converter.html#matplotlib.axis.Axis.set_converter "matplotlib.axis.Axis.set_converter") | [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface") |
> | [`data_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#matplotlib.axis.Axis.set_data_interval "matplotlib.axis.Axis.set_data_interval") | unknown |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted") | unknown |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label.html#matplotlib.axis.Axis.set_label "matplotlib.axis.Axis.set_label") | unknown |
> | [`label_coords`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords") | unknown |
> | [`label_position`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_label_position "mpl_toolkits.mplot3d.axis3d.Axis.set_label_position") | {'lower', 'upper', 'both', 'default', 'none'} |
> | [`label_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text "matplotlib.axis.Axis.set_label_text") | str |
> | [`major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter") | [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br>, `str`, or function |
> | [`major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator") | [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") |
> | [`minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter") | [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br>, `str`, or function |
> | [`minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator") | [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`pane_color`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_pane_color "mpl_toolkits.mplot3d.axis3d.Axis.set_pane_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_pickradius.html#matplotlib.axis.Axis.set_pickradius "matplotlib.axis.Axis.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`remove_overlapping_locs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_remove_overlapping_locs.html#matplotlib.axis.Axis.set_remove_overlapping_locs "matplotlib.axis.Axis.set_remove_overlapping_locs") | unknown |
> | [`rotate_label`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_rotate_label "mpl_toolkits.mplot3d.axis3d.Axis.set_rotate_label") | unknown |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params") | unknown |
> | [`ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels") | sequence of str or of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>s |
> | [`ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks") | 1D array-like |
> | [`ticks_position`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_ticks_position "mpl_toolkits.mplot3d.axis3d.Axis.set_ticks_position") | {'lower', 'upper', 'both', 'default', 'none'} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units") | units tag |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#matplotlib.axis.Axis.set_view_interval "matplotlib.axis.Axis.set_view_interval") | unknown |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_label\_position(_position_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L240-L251)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_label_position "Link to this definition")

Set the label position.

Parameters:

**position**{'lower', 'upper', 'both', 'default', 'none'}

The position of the axis label.

set\_pane\_color(_color_, _alpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L264-L280)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_pane_color "Link to this definition")

Set pane color.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Color for axis pane.

**alpha**float, optional

Alpha value for axis pane. If None, base it on _color_.

set\_rotate\_label(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L282-L288)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_rotate_label "Link to this definition")

Whether to rotate the axis label: True, False or None. If set to None the label will be rotated if longer than 4 chars.

set\_ticks\_position(_position_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axis3d.py#L216-L227)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.set_ticks_position "Link to this definition")

Set the ticks position.

Parameters:

**position**{'lower', 'upper', 'both', 'default', 'none'}

The position of the bolded axis lines, ticks, and tick labels.

property v\_interval[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis.v_interval "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.6: Use get\_view\_interval instead.

On this page