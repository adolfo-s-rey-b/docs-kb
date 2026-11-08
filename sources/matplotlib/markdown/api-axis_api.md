[Skip to main content](https://matplotlib.org/stable/api/axis_api.html#main-content)

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
    

`matplotlib.axis`[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib-axis "Link to this heading")

=============================================================================================================

Classes for the ticks and x- and y-axis.

[Inheritance](https://matplotlib.org/stable/api/axis_api.html#id1)
[#](https://matplotlib.org/stable/api/axis_api.html#inheritance "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Inheritance diagram of Tick, Ticker, XAxis, YAxis, XTick, YTick

[`Axis` objects](https://matplotlib.org/stable/api/axis_api.html#id2)
[#](https://matplotlib.org/stable/api/axis_api.html#axis-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

class matplotlib.axis.Axis(_axes_, _\*_, _pickradius\=15_, _clear\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L585-L2503)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "Link to this definition")

Base class for [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
 and [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")
.

Attributes:

**isDefault\_label**bool

[`axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axes.html#matplotlib.axis.Axis.axes "matplotlib.axis.Axis.axes")
[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance the artist resides in, or _None_.

**major**[`Ticker`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Ticker "matplotlib.axis.Ticker")

Determines the major tick positions and their label format.

**minor**[`Ticker`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Ticker "matplotlib.axis.Ticker")

Determines the minor tick positions and their label format.

**callbacks**[`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")

**label**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The axis label.

**labelpad**float

The distance between the axis label and the tick labels. Defaults to `[rcParams["axes.labelpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.labelpad#rcparam-axes-labelpad) ` (default: `4.0`).

**offsetText**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

A [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 object containing the data offset of the ticks (if any).

[`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.pickradius.html#matplotlib.axis.Axis.pickradius "matplotlib.axis.Axis.pickradius")
float

The acceptance radius for containment tests.

**majorTicks**list of [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")

The major ticks.

Warning

Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that changes to individual ticks will not survive if you work on the figure further (including also panning/zooming on a displayed figure).

Working on the individual ticks is a method of last resort. Use [`set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 instead if possible.

**minorTicks**list of [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")

The minor ticks.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to which the created Axis belongs.

**pickradius**float

The acceptance radius for containment tests. See also [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains")
.

**clear**bool, default: True

Whether to clear the Axis on creation. This is not required, e.g., when creating an Axis as part of an Axes, as `Axes.clear` will call `Axis.clear`. .. versionadded:: 3.8

class matplotlib.axis.XAxis(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2536-L2757)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "Link to this definition")

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to which the created Axis belongs.

**pickradius**float

The acceptance radius for containment tests. See also [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains")
.

**clear**bool, default: True

Whether to clear the Axis on creation. This is not required, e.g., when creating an Axis as part of an Axes, as `Axes.clear` will call `Axis.clear`. .. versionadded:: 3.8

class matplotlib.axis.YAxis(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2760-L2986)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "Link to this definition")

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to which the created Axis belongs.

**pickradius**float

The acceptance radius for containment tests. See also [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains")
.

**clear**bool, default: True

Whether to clear the Axis on creation. This is not required, e.g., when creating an Axis as part of an Axes, as `Axes.clear` will call `Axis.clear`. .. versionadded:: 3.8

class matplotlib.axis.Ticker[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L510-L548)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Ticker "Link to this definition")

A container for the objects defining tick position and format.

Attributes:

**locator**[`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 subclass

Determines the positions of the ticks.

**formatter**[`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 subclass

Determines the format of the tick labels.

|     |     |
| --- | --- |
| [`Axis.clear`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.clear.html#matplotlib.axis.Axis.clear "matplotlib.axis.Axis.clear") | Clear the axis. |
| [`Axis.get_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_scale.html#matplotlib.axis.Axis.get_scale "matplotlib.axis.Axis.get_scale") | Return this Axis' scale (as a str). |

### [Formatters and Locators](https://matplotlib.org/stable/api/axis_api.html#id3)
[#](https://matplotlib.org/stable/api/axis_api.html#formatters-and-locators "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.get_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_formatter.html#matplotlib.axis.Axis.get_major_formatter "matplotlib.axis.Axis.get_major_formatter") | Get the formatter of the major ticker. |
| [`Axis.get_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator") | Get the locator of the major ticker. |
| [`Axis.get_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minor_formatter.html#matplotlib.axis.Axis.get_minor_formatter "matplotlib.axis.Axis.get_minor_formatter") | Get the formatter of the minor ticker. |
| [`Axis.get_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minor_locator.html#matplotlib.axis.Axis.get_minor_locator "matplotlib.axis.Axis.get_minor_locator") | Get the locator of the minor ticker. |
| [`Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter") | Set the formatter of the major ticker. |
| [`Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator") | Set the locator of the major ticker. |
| [`Axis.set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter") | Set the formatter of the minor ticker. |
| [`Axis.set_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator") | Set the locator of the minor ticker. |
| [`Axis.remove_overlapping_locs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.remove_overlapping_locs.html#matplotlib.axis.Axis.remove_overlapping_locs "matplotlib.axis.Axis.remove_overlapping_locs") | If minor ticker locations that overlap with major ticker locations should be trimmed. |
| [`Axis.get_remove_overlapping_locs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_remove_overlapping_locs.html#matplotlib.axis.Axis.get_remove_overlapping_locs "matplotlib.axis.Axis.get_remove_overlapping_locs") |     |
| [`Axis.set_remove_overlapping_locs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_remove_overlapping_locs.html#matplotlib.axis.Axis.set_remove_overlapping_locs "matplotlib.axis.Axis.set_remove_overlapping_locs") |     |

### [Axis Label](https://matplotlib.org/stable/api/axis_api.html#id4)
[#](https://matplotlib.org/stable/api/axis_api.html#axis-label "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.label.html#matplotlib.axis.Axis.label "matplotlib.axis.Axis.label") | The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> object of the axis label. |
| [`Axis.set_label_coords`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords") | Set the coordinates of the label. |
| [`Axis.set_label_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_position.html#matplotlib.axis.Axis.set_label_position "matplotlib.axis.Axis.set_label_position") | Set the label position (top or bottom) |
| [`Axis.set_label_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text "matplotlib.axis.Axis.set_label_text") | Set the text value of the axis label. |
| [`Axis.get_label_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label_position.html#matplotlib.axis.Axis.get_label_position "matplotlib.axis.Axis.get_label_position") | Return the label position (top or bottom) |
| [`Axis.get_label_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label_text.html#matplotlib.axis.Axis.get_label_text "matplotlib.axis.Axis.get_label_text") | Get the text of the label. |

### [Ticks, tick labels and Offset text](https://matplotlib.org/stable/api/axis_api.html#id5)
[#](https://matplotlib.org/stable/api/axis_api.html#ticks-tick-labels-and-offset-text "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.get_major_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_ticks.html#matplotlib.axis.Axis.get_major_ticks "matplotlib.axis.Axis.get_major_ticks") | Return the list of major [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")<br>s. |
| [`Axis.get_majorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_majorticklabels.html#matplotlib.axis.Axis.get_majorticklabels "matplotlib.axis.Axis.get_majorticklabels") | Return this Axis' major tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`Axis.get_majorticklines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_majorticklines.html#matplotlib.axis.Axis.get_majorticklines "matplotlib.axis.Axis.get_majorticklines") | Return this Axis' major tick lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axis.get_majorticklocs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_majorticklocs.html#matplotlib.axis.Axis.get_majorticklocs "matplotlib.axis.Axis.get_majorticklocs") | Return this Axis' major tick locations in data coordinates. |
| [`Axis.get_minor_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minor_ticks.html#matplotlib.axis.Axis.get_minor_ticks "matplotlib.axis.Axis.get_minor_ticks") | Return the list of minor [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")<br>s. |
| [`Axis.get_minorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minorticklabels.html#matplotlib.axis.Axis.get_minorticklabels "matplotlib.axis.Axis.get_minorticklabels") | Return this Axis' minor tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`Axis.get_minorticklines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minorticklines.html#matplotlib.axis.Axis.get_minorticklines "matplotlib.axis.Axis.get_minorticklines") | Return this Axis' minor tick lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axis.get_minorticklocs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minorticklocs.html#matplotlib.axis.Axis.get_minorticklocs "matplotlib.axis.Axis.get_minorticklocs") | Return this Axis' minor tick locations in data coordinates. |
| [`Axis.get_offset_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_offset_text.html#matplotlib.axis.Axis.get_offset_text "matplotlib.axis.Axis.get_offset_text") | Return the axis offsetText as a Text instance. |
| [`Axis.get_tick_padding`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_padding.html#matplotlib.axis.Axis.get_tick_padding "matplotlib.axis.Axis.get_tick_padding") |     |
| [`Axis.get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params") | Get appearance parameters for ticks, ticklabels, and gridlines. |
| [`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels") | Get this Axis' tick labels. |
| [`Axis.get_ticklines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklines.html#matplotlib.axis.Axis.get_ticklines "matplotlib.axis.Axis.get_ticklines") | Return this Axis' tick lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axis.get_ticklocs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklocs.html#matplotlib.axis.Axis.get_ticklocs "matplotlib.axis.Axis.get_ticklocs") | Return this Axis' tick locations in data coordinates. |
| [`Axis.get_gridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_gridlines.html#matplotlib.axis.Axis.get_gridlines "matplotlib.axis.Axis.get_gridlines") | Return this Axis' grid lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axis.grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "matplotlib.axis.Axis.grid") | Configure the grid lines. |
| [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params") | Set appearance parameters for ticks, ticklabels, and gridlines. |
| [`Axis.axis_date`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#matplotlib.axis.Axis.axis_date "matplotlib.axis.Axis.axis_date") | Set up axis ticks and labels to treat data along this Axis as dates. |
| [`Axis.minorticks_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_off.html#matplotlib.axis.Axis.minorticks_off "matplotlib.axis.Axis.minorticks_off") | Remove minor ticks from the Axis. |
| [`Axis.minorticks_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#matplotlib.axis.Axis.minorticks_on "matplotlib.axis.Axis.minorticks_on") | Display default minor ticks on the Axis, depending on the scale ([`get_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_scale.html#matplotlib.axis.Axis.get_scale "matplotlib.axis.Axis.get_scale")<br>). |

### [Data and view intervals](https://matplotlib.org/stable/api/axis_api.html#id6)
[#](https://matplotlib.org/stable/api/axis_api.html#data-and-view-intervals "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.get_data_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_data_interval.html#matplotlib.axis.Axis.get_data_interval "matplotlib.axis.Axis.get_data_interval") | Return the `(min, max)` data limits of this axis. |
| [`Axis.get_view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_view_interval.html#matplotlib.axis.Axis.get_view_interval "matplotlib.axis.Axis.get_view_interval") | Return the `(min, max)` view limits of this axis. |
| [`Axis.get_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_inverted.html#matplotlib.axis.Axis.get_inverted "matplotlib.axis.Axis.get_inverted") | Return whether this Axis is oriented in the "inverse" direction. |
| [`Axis.set_data_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#matplotlib.axis.Axis.set_data_interval "matplotlib.axis.Axis.set_data_interval") | Set the axis data limits. |
| [`Axis.set_view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#matplotlib.axis.Axis.set_view_interval "matplotlib.axis.Axis.set_view_interval") | Set the axis view limits. |
| [`Axis.set_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted") | Set whether this Axis is oriented in the "inverse" direction. |

### [Rendering helpers](https://matplotlib.org/stable/api/axis_api.html#id7)
[#](https://matplotlib.org/stable/api/axis_api.html#rendering-helpers "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.get_minpos`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minpos.html#matplotlib.axis.Axis.get_minpos "matplotlib.axis.Axis.get_minpos") |     |
| [`Axis.get_tick_space`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_space.html#matplotlib.axis.Axis.get_tick_space "matplotlib.axis.Axis.get_tick_space") | Return the estimated number of ticks that can fit on the axis. |
| [`Axis.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tightbbox.html#matplotlib.axis.Axis.get_tightbbox "matplotlib.axis.Axis.get_tightbbox") | Return a bounding box that encloses the axis. |

### [Interactive](https://matplotlib.org/stable/api/axis_api.html#id8)
[#](https://matplotlib.org/stable/api/axis_api.html#interactive "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains") | Test whether the artist contains the mouse event. |
| [`Axis.pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.pickradius.html#matplotlib.axis.Axis.pickradius "matplotlib.axis.Axis.pickradius") | The acceptance radius for containment tests. |
| [`Axis.get_pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_pickradius.html#matplotlib.axis.Axis.get_pickradius "matplotlib.axis.Axis.get_pickradius") | Return the depth of the axis used by the picker. |
| [`Axis.set_pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_pickradius.html#matplotlib.axis.Axis.set_pickradius "matplotlib.axis.Axis.set_pickradius") | Set the depth of the axis used by the picker. |

### [Units](https://matplotlib.org/stable/api/axis_api.html#id9)
[#](https://matplotlib.org/stable/api/axis_api.html#units "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.convert_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.convert_units.html#matplotlib.axis.Axis.convert_units "matplotlib.axis.Axis.convert_units") |     |
| [`Axis.set_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units") | Set the units for axis. |
| [`Axis.get_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_units.html#matplotlib.axis.Axis.get_units "matplotlib.axis.Axis.get_units") | Return the units for axis. |
| [`Axis.set_converter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_converter.html#matplotlib.axis.Axis.set_converter "matplotlib.axis.Axis.set_converter") | Set the unit converter for axis. |
| [`Axis.get_converter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_converter.html#matplotlib.axis.Axis.get_converter "matplotlib.axis.Axis.get_converter") | Get the unit converter for axis. |
| [`Axis.update_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.update_units.html#matplotlib.axis.Axis.update_units "matplotlib.axis.Axis.update_units") | Introspect _data_ for units converter and update the `axis.get_converter` instance if necessary. |

### [XAxis Specific](https://matplotlib.org/stable/api/axis_api.html#id10)
[#](https://matplotlib.org/stable/api/axis_api.html#xaxis-specific "Link to this heading")

|     |     |
| --- | --- |
| [`XAxis.axis_name`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.axis_name.html#matplotlib.axis.XAxis.axis_name "matplotlib.axis.XAxis.axis_name") | Read-only name identifying the axis. |
| [`XAxis.get_ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.get_ticks_position.html#matplotlib.axis.XAxis.get_ticks_position "matplotlib.axis.XAxis.get_ticks_position") | Return the ticks position ("top", "bottom", "default", or "unknown"). |
| [`XAxis.set_ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position") | Set the ticks position. |
| [`XAxis.set_label_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_label_position.html#matplotlib.axis.XAxis.set_label_position "matplotlib.axis.XAxis.set_label_position") | Set the label position (top or bottom) |
| [`XAxis.tick_bottom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_bottom.html#matplotlib.axis.XAxis.tick_bottom "matplotlib.axis.XAxis.tick_bottom") | Move ticks and ticklabels (if present) to the bottom of the Axes. |
| [`XAxis.tick_top`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_top.html#matplotlib.axis.XAxis.tick_top "matplotlib.axis.XAxis.tick_top") | Move ticks and ticklabels (if present) to the top of the Axes. |

### [YAxis Specific](https://matplotlib.org/stable/api/axis_api.html#id11)
[#](https://matplotlib.org/stable/api/axis_api.html#yaxis-specific "Link to this heading")

|     |     |
| --- | --- |
| [`YAxis.axis_name`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.axis_name.html#matplotlib.axis.YAxis.axis_name "matplotlib.axis.YAxis.axis_name") | Read-only name identifying the axis. |
| [`YAxis.get_ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.get_ticks_position.html#matplotlib.axis.YAxis.get_ticks_position "matplotlib.axis.YAxis.get_ticks_position") | Return the ticks position ("left", "right", "default", or "unknown"). |
| [`YAxis.set_offset_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_offset_position.html#matplotlib.axis.YAxis.set_offset_position "matplotlib.axis.YAxis.set_offset_position") |     |
| [`YAxis.set_ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_ticks_position.html#matplotlib.axis.YAxis.set_ticks_position "matplotlib.axis.YAxis.set_ticks_position") | Set the ticks position. |
| [`YAxis.set_label_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_label_position.html#matplotlib.axis.YAxis.set_label_position "matplotlib.axis.YAxis.set_label_position") | Set the label position (left or right) |
| [`YAxis.tick_left`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.tick_left.html#matplotlib.axis.YAxis.tick_left "matplotlib.axis.YAxis.tick_left") | Move ticks and ticklabels (if present) to the left of the Axes. |
| [`YAxis.tick_right`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.tick_right.html#matplotlib.axis.YAxis.tick_right "matplotlib.axis.YAxis.tick_right") | Move ticks and ticklabels (if present) to the right of the Axes. |

### [Other](https://matplotlib.org/stable/api/axis_api.html#id12)
[#](https://matplotlib.org/stable/api/axis_api.html#other "Link to this heading")

|     |     |
| --- | --- |
| [`Axis.OFFSETTEXTPAD`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.OFFSETTEXTPAD.html#matplotlib.axis.Axis.OFFSETTEXTPAD "matplotlib.axis.Axis.OFFSETTEXTPAD") |     |
| [`Axis.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axes.html#matplotlib.axis.Axis.axes "matplotlib.axis.Axis.axes") | The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> instance the artist resides in, or _None_. |
| [`Axis.limit_range_for_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.limit_range_for_scale.html#matplotlib.axis.Axis.limit_range_for_scale "matplotlib.axis.Axis.limit_range_for_scale") | Return the range _vmin_, _vmax_, restricted to the domain supported by the current scale. |
| [`Axis.reset_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.reset_ticks.html#matplotlib.axis.Axis.reset_ticks "matplotlib.axis.Axis.reset_ticks") | Re-initialize the major and minor Tick lists. |
| [`Axis.set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_clip_path.html#matplotlib.axis.Axis.set_clip_path "matplotlib.axis.Axis.set_clip_path") | Set the artist's clip path. |
| [`Axis.set_default_intervals`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_default_intervals.html#matplotlib.axis.Axis.set_default_intervals "matplotlib.axis.Axis.set_default_intervals") | Set the default limits for the axis data and view interval if they have not been not mutated yet. |

### [Discouraged](https://matplotlib.org/stable/api/axis_api.html#id13)
[#](https://matplotlib.org/stable/api/axis_api.html#discouraged "Link to this heading")

These methods should be used together with care, calling `set_ticks` to specify the desired tick locations **before** calling `set_ticklabels` to specify a matching series of labels. Calling `set_ticks` makes a [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
; it's list of locations is then used by `set_ticklabels` to make an appropriate [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
.

|     |     |
| --- | --- |
| [`Axis.get_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label.html#matplotlib.axis.Axis.get_label "matplotlib.axis.Axis.get_label") | \[_Discouraged_\] Return the axis label as a Text instance. |
| [`Axis.set_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label.html#matplotlib.axis.Axis.set_label "matplotlib.axis.Axis.set_label") | Assigning legend labels is not supported. |
| [`Axis.set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks") | Set this Axis' tick locations and optionally tick labels. |
| [`Axis.set_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels") | \[_Discouraged_\] Set this Axis' tick labels with list of string labels. |

[`Tick` objects](https://matplotlib.org/stable/api/axis_api.html#id14)
[#](https://matplotlib.org/stable/api/axis_api.html#tick-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

class matplotlib.axis.Tick(_axes_, _loc_, _\*_, _size\=None_, _width\=None_, _color\=None_, _tickdir\=None_, _pad\=None_, _labelsize\=None_, _labelcolor\=None_, _labelfontfamily\=None_, _zorder\=None_, _gridOn\=None_, _tick1On\=True_, _tick2On\=True_, _label1On\=True_, _label2On\=False_, _major\=True_, _labelrotation\=0_, _labelrotation\_mode\=None_, _grid\_color\=None_, _grid\_linestyle\=None_, _grid\_linewidth\=None_, _grid\_alpha\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L38-L385)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "Link to this definition")

Abstract base class for the axis ticks, grid lines and labels.

Ticks mark a position on an Axis. They contain two lines as markers and two labels; one each for the bottom and top positions (in case of an [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
) or for the left and right positions (in case of a [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")
).

Attributes:

**tick1line**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The left/bottom tick marker.

**tick2line**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The right/top tick marker.

**gridline**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The grid line associated with the label position.

**label1**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The left/bottom tick label.

**label2**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The right/top tick label.

Notes

Ticks are managed though the autoscaling / view limit mechanism and therefore need very careful handling when explicitly accessed, see [Tick objects](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#axes-tick-objects)
.

The tick lines are implemented as [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances using the [`markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")
 TICKLEFT, TICKRIGHT, TICKDOWN, TICKUP. Therefore, properties are controlled via the marker, e.g. for the color [`Line2D.set_markeredgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor "matplotlib.lines.Line2D.set_markeredgecolor")
 and not [`Line2D.set_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")
.

Parameters:

**loc**

The tick location in data coords.

**size**

The tick size in points.

class matplotlib.axis.XTick(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L388-L446)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XTick "Link to this definition")

Contains all the Artists needed to make an x tick - the tick line, the label text and the grid line

Parameters:

**loc**

The tick location in data coords.

**size**

The tick size in points.

class matplotlib.axis.YTick(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L449-L507)
[#](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YTick "Link to this definition")

Contains all the Artists needed to make a Y tick - the tick line, the label text and the grid line

Parameters:

**loc**

The tick location in data coords.

**size**

The tick size in points.

|     |     |
| --- | --- |
| [`Tick.get_loc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.get_loc.html#matplotlib.axis.Tick.get_loc "matplotlib.axis.Tick.get_loc") | Return the tick location (data coords) as a scalar. |
| [`Tick.get_pad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.get_pad.html#matplotlib.axis.Tick.get_pad "matplotlib.axis.Tick.get_pad") | Get the value of the tick label pad in points. |
| [`Tick.get_tick_padding`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.get_tick_padding.html#matplotlib.axis.Tick.get_tick_padding "matplotlib.axis.Tick.get_tick_padding") | Get the length of the tick outside of the Axes. |
| [`Tick.get_tickdir`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.get_tickdir.html#matplotlib.axis.Tick.get_tickdir "matplotlib.axis.Tick.get_tickdir") |     |
| [`Tick.get_view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.get_view_interval.html#matplotlib.axis.Tick.get_view_interval "matplotlib.axis.Tick.get_view_interval") | Return the view limits `(min, max)` of the axis the tick belongs to. |
| [`Tick.set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_clip_path.html#matplotlib.axis.Tick.set_clip_path "matplotlib.axis.Tick.set_clip_path") | Set the artist's clip path. |
| [`Tick.set_pad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_pad.html#matplotlib.axis.Tick.set_pad "matplotlib.axis.Tick.set_pad") | Set the tick label pad in points |
| [`Tick.set_url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_url.html#matplotlib.axis.Tick.set_url "matplotlib.axis.Tick.set_url") | Set the url of label1 and label2. |
| [`Tick.update_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.update_position.html#matplotlib.axis.Tick.update_position "matplotlib.axis.Tick.update_position") | Set the location of tick in data coords with scalar _loc_. |

On this page