[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#main-content)

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
    

matplotlib.pyplot.bar[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib-pyplot-bar "Link to this heading")

============================================================================================================================================

matplotlib.pyplot.bar(_x_, _height_, _width\=0.8_, _bottom\=None_, _\*_, _align\='center'_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3127-L3146)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "Link to this definition")

Make a bar plot.

The bars are positioned at _x_ with the given _align_ment. Their dimensions are given by _height_ and _width_. The vertical baseline is _bottom_ (default 0).

Many parameters can take either a single value applying to all bars or a sequence of values, one for each bar.

Parameters:

**x**float or array-like

The x coordinates of the bars. See also _align_ for the alignment of the bars to the coordinates.

Bars are often used for categorical data, i.e. string labels below the bars. You can provide a list of strings directly to _x_. `bar(['A', 'B', 'C'], [1, 2, 3])` is often a shorter and more convenient notation compared to `bar(range(3), [1, 2, 3], tick_label=['A', 'B', 'C'])`. They are equivalent as long as the names are unique. The explicit _tick\_label_ notation draws the names in the sequence given. However, when having duplicate values in categorical _x_ data, these values map to the same numerical x coordinate, and hence the corresponding bars are drawn on top of each other.

**height**float or array-like

The height(s) of the bars.

Note that if _bottom_ has units (e.g. datetime), _height_ should be in units that are a difference from the value of _bottom_ (e.g. timedelta).

**width**float or array-like, default: 0.8

The width(s) of the bars.

Note that if _x_ has units (e.g. datetime), then _width_ should be in units that are a difference (e.g. timedelta) around the _x_ values.

**bottom**float or array-like, default: 0

The y coordinate(s) of the bottom side(s) of the bars.

Note that if _bottom_ has units, then the y-axis will get a Locator and Formatter appropriate for the units (e.g. dates, or categorical).

**align**{'center', 'edge'}, default: 'center'

Alignment of the bars to the _x_ coordinates:

*   'center': Center the base on the _x_ positions.
    
*   'edge': Align the left edges of the bars with the _x_ positions.
    

To align the bars on the right edge pass a negative _width_ and `align='edge'`.

Returns:

[`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")

Container with all the bars and optionally errorbars.

Other Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the bar faces. This is an alias for _facecolor_. If both are given, _facecolor_ takes precedence.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the bar faces. If both _color_ and _facecolor are given, \*facecolor_ takes precedence.

**edgecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the bar edges.

**linewidth**float or array-like, optional

Width of the bar edge(s). If 0, don't draw edges.

**tick\_label**str or list of str, optional

The tick labels of the bars. Default: None (Use default numeric labels.)

**label**str or list of str, optional

A single label is attached to the resulting [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 as a legend label for the whole dataset. If a list is provided, it must be the same length as _x_ and labels the individual bars. Repeated labels are not de-duplicated and will cause repeated label entries, so this is best used when bars also differ in style (e.g., by passing a list to _color_).

Tip: Use [`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html#matplotlib.pyplot.bar_label "matplotlib.pyplot.bar_label")
 to place labels on the bars.

**xerr, yerr**float or array-like of shape(N,) or shape(2, N), optional

If not _None_, add horizontal / vertical errorbars to the bar tips. The values are +/- sizes relative to the data:

*   scalar: symmetric +/- values for all bars
    
*   shape(N,): symmetric +/- values for each bar
    
*   shape(2, N): Separate - and + values for each bar. First row contains the lower errors, the second row contains the upper errors.
    
*   _None_: No errorbar. (Default)
    

This is a convenience shortcut for an extra [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 call. See its documentation and [Different ways of specifying error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_features.html)
 for an example on the usage of _xerr_ and _yerr_.

**ecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'black'

The line color of the errorbars. Multiple colors are only supported if the errorbars do not have caps. If you need individually colored errorbars with caps, instead use explicit [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 calls for each data point.

**capsize**float, default: `[rcParams["errorbar.capsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=errorbar.capsize#rcparam-errorbar-capsize) ` (default: `0.0`)

The length of the error bar caps in points.

**error\_kw**dict, optional

Dictionary of keyword arguments to be passed to the [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 method. Values of _ecolor_ or _capsize_ defined here take precedence over the independent keyword arguments.

**log**bool, default: False

If _True_, set the y-axis to be log scale.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**[`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 properties

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`angle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_angle "matplotlib.patches.Rectangle.set_angle") | unknown |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
| [`bounds`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_bounds "matplotlib.patches.Rectangle.set_bounds") | (left, bottom, width, height) |
| [`capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "matplotlib.patches.Patch.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "matplotlib.patches.Patch.set_fill") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
| [`hatch_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "matplotlib.patches.Patch.set_hatch_linewidth") | unknown |
| [`hatchcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "matplotlib.patches.Patch.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' or None |
| [`height`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_height "matplotlib.patches.Rectangle.set_height") | unknown |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "matplotlib.patches.Patch.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
| [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth") | float or None |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`width`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_width "matplotlib.patches.Rectangle.set_width") | unknown |
| [`x`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_x "matplotlib.patches.Rectangle.set_x") | unknown |
| [`xy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_xy "matplotlib.patches.Rectangle.set_xy") | (float, float) |
| [`y`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_y "matplotlib.patches.Rectangle.set_y") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh "matplotlib.pyplot.barh")

Plot a horizontal bar plot.

[`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#matplotlib.pyplot.grouped_bar "matplotlib.pyplot.grouped_bar")

Plot multiple datasets as grouped bar plot.

[`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html#matplotlib.pyplot.bar_label "matplotlib.pyplot.bar_label")

Add labels to bars.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
.

Stacked bars can be achieved by passing individual _bottom_ values per bar. See [Stacked bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html)
.

Examples using `matplotlib.pyplot.bar`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#examples-using-matplotlib-pyplot-bar "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_barchart_thumb.png)

[Grouped bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)

Grouped bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_bar_label_demo_thumb.png)

[Bar chart with labels](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)

Bar chart with labels

![](https://matplotlib.org/stable/_images/sphx_glr_bar_stacked_thumb.png)

[Stacked bar chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html)

Stacked bar chart

![](https://matplotlib.org/stable/_images/sphx_glr_bar_colors_thumb.png)

[Bar chart with individual bar colors](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html)

Bar chart with individual bar colors

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_thumb.png)

[Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)

Nested pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_polar_bar_thumb.png)

[Bar chart on polar axis](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_bar.html)

Bar chart on polar axis

![](https://matplotlib.org/stable/_images/sphx_glr_hatch_demo_thumb.png)

[Hatch demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html)

Hatch demo

![](https://matplotlib.org/stable/_images/sphx_glr_hatchcolor_demo_thumb.png)

[Hatchcolor Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatchcolor_demo.html)

Hatchcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_table_demo_thumb.png)

[Table Demo](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

On this page