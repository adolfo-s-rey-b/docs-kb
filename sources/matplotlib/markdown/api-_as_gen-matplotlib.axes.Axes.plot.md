[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#main-content)

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
    

matplotlib.axes.Axes.plot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib-axes-axes-plot "Link to this heading")

========================================================================================================================================================

Axes.plot(_\*args_, _scalex\=True_, _scaley\=True_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L1547-L1799)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "Link to this definition")

Plot y versus x as lines and/or markers.

Call signatures:

plot(\[x\], y, \[fmt\], \*, data\=None, \*\*kwargs)
plot(\[x\], y, \[fmt\], \[x2\], y2, \[fmt2\], ..., \*\*kwargs)

The coordinates of the points or line nodes are given by _x_, _y_.

The optional parameter _fmt_ is a convenient way for defining basic formatting like color, marker and linestyle. It's a shortcut string notation described in the _Notes_ section below.

\>>> plot(x, y)        \# plot x and y using default line style and color
\>>> plot(x, y, 'bo')  \# plot x and y using blue circle markers
\>>> plot(y)           \# plot y using x as index array 0..N-1
\>>> plot(y, 'r+')     \# ditto, but with red plusses

You can use [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties as keyword arguments for more control on the appearance. Line properties and _fmt_ can be mixed. The following two calls yield identical results:

\>>> plot(x, y, 'go--', linewidth\=2, markersize\=12)
\>>> plot(x, y, color\='green', marker\='o', linestyle\='dashed',
...      linewidth\=2, markersize\=12)

When conflicting with _fmt_, keyword arguments take precedence.

**Plotting labelled data**

There's a convenient way for plotting objects with labelled data (i.e. data that can be accessed by index `obj['y']`). Instead of giving the data in _x_ and _y_, you can provide the object in the _data_ parameter and just give the labels for _x_ and _y_:

\>>> plot('xlabel', 'ylabel', data\=obj)

All indexable objects are supported. This could e.g. be a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
, a [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
 or a structured numpy array.

**Plotting multiple sets of data**

There are various ways to plot multiple sets of data.

*   The most straight forward way is just to call [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
     multiple times. Example:
    
    \>>> plot(x1, y1, 'bo')
    \>>> plot(x2, y2, 'go')
    
*   If _x_ and/or _y_ are 2D arrays, a separate data set will be drawn for every column. If both _x_ and _y_ are 2D, they must have the same shape. If only one of them is 2D with shape (N, m) the other must have length N and will be used for every data set m.
    
    Example:
    
    \>>> x \= \[1, 2, 3\]
    \>>> y \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
    \>>> plot(x, y)
    
    is equivalent to:
    
    \>>> for col in range(y.shape\[1\]):
    ...     plot(x, y\[:, col\])
    
*   The third way is to specify multiple sets of _\[x\]_, _y_, _\[fmt\]_ groups:
    
    \>>> plot(x1, y1, 'g^', x2, y2, 'g-')
    
    In this case, any additional keyword argument applies to all datasets. Also, this syntax cannot be combined with the _data_ parameter.
    

By default, each line is assigned a different style specified by a 'style cycle'. The _fmt_ and line property parameters are only necessary if you want explicit deviations from these defaults. Alternatively, you can also change the style cycle using `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`).

Parameters:

**x, y**array-like or float

The horizontal / vertical coordinates of the data points. _x_ values are optional and default to `range(len(y))`.

Commonly, these parameters are 1D arrays.

They can also be scalars, or two-dimensional (in that case, the columns represent separate data sets).

These arguments cannot be passed as keywords.

**fmt**str, optional

A format string, e.g. 'ro' for red circles. See the _Notes_ section for a full description of the format strings.

Format strings are just an abbreviation for quickly setting basic line properties. All of these and more can also be controlled by keyword arguments.

This argument cannot be passed as keyword.

**data**indexable object, optional

An object with labelled data. If given, provide the label names to plot in _x_ and _y_.

Note

Technically there's a slight ambiguity in calls where the second label is a valid _fmt_. `plot('n', 'o', data=obj)` could be `plt(x, y)` or `plt(y, fmt)`. In such cases, the former interpretation is chosen, but a warning is issued. You may suppress the warning by adding an empty format string `plot('n', 'o', '', data=obj)`.

Returns:

list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

A list of lines representing the plotted data.

Other Parameters:

**scalex, scaley**bool, default: True

These parameters determine if the view limits are adapted to the data limits. The values are passed on to [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
.

**\*\*kwargs**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties, optional

_kwargs_ are used to specify properties like a line label (for auto legends), linewidth, antialiasing, marker face color. Example:

\>>> plot(\[1, 2, 3\], \[1, 2, 3\], 'go-', label\='line 1', linewidth\=2)
\>>> plot(\[1, 2, 3\], \[1, 4, 9\], 'rs', label\='line 2')

If you specify multiple lines with one plot call, the kwargs apply to all those lines. In case the label object is iterable, each element is used as labels for each set of data.

Here is a list of available [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties:

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

See also

[`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")

XY scatter plot with markers of varying size and/or color ( sometimes also called bubble chart).

Notes

**Format Strings**

A format string consists of a part for color, marker and line:

fmt \= '\[marker\]\[line\]\[color\]'

Each of them is optional. If not provided, the value from the style cycle is used. Exception: If `line` is given, but no `marker`, the data will be a line without markers.

Other combinations such as `[color][marker][line]` are also supported, but note that their parsing may be ambiguous.

**Markers**

| character | description |
| --- | --- |
| `'.'` | point marker |
| `','` | pixel marker |
| `'o'` | circle marker |
| `'v'` | triangle\_down marker |
| `'^'` | triangle\_up marker |
| `'<'` | triangle\_left marker |
| `'>'` | triangle\_right marker |
| `'1'` | tri\_down marker |
| `'2'` | tri\_up marker |
| `'3'` | tri\_left marker |
| `'4'` | tri\_right marker |
| `'8'` | octagon marker |
| `'s'` | square marker |
| `'p'` | pentagon marker |
| `'P'` | plus (filled) marker |
| `'*'` | star marker |
| `'h'` | hexagon1 marker |
| `'H'` | hexagon2 marker |
| `'+'` | plus marker |
| `'x'` | x marker |
| `'X'` | x (filled) marker |
| `'D'` | diamond marker |
| `'d'` | thin\_diamond marker |
| `'\|'` | vline marker |
| `'_'` | hline marker |

**Line Styles**

| character | description |
| --- | --- |
| `'-'` | solid line style |
| `'--'` | dashed line style |
| `'-.'` | dash-dot line style |
| `':'` | dotted line style |

Example format strings:

'b'    \# blue markers with default shape
'or'   \# red circles
'-g'   \# green solid line
'--'   \# dashed line with default color
'^k:'  \# black triangle\_up markers connected by a dotted line

**Colors**

The supported color abbreviations are the single letter codes

| character | color |
| --- | --- |
| `'b'` | blue |
| `'g'` | green |
| `'r'` | red |
| `'c'` | cyan |
| `'m'` | magenta |
| `'y'` | yellow |
| `'k'` | black |
| `'w'` | white |

and the `'CN'` colors that index into the default property cycle.

If the color is the only part of the format string, you can additionally use any [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
 spec, e.g. full names (`'green'`) or hex strings (`'#008000'`).

Examples using `matplotlib.axes.Axes.plot`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#examples-using-matplotlib-axes-axes-plot "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_simple_plot_thumb.png)

[Line plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)

Line plot

![](https://matplotlib.org/stable/_images/sphx_glr_line_demo_dash_control_thumb.png)

[Dashed line style configuration](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html)

Dashed line style configuration

![](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_thumb.png)

[Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)

Markevery Demo

![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_thumb.png)

[Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)

Marker reference

![](https://matplotlib.org/stable/_images/sphx_glr_axline_thumb.png)

[Infinite lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html)

Infinite lines

![](https://matplotlib.org/stable/_images/sphx_glr_lines_with_ticks_demo_thumb.png)

[Lines with a ticked patheffect](https://matplotlib.org/stable/gallery/lines_bars_and_markers/lines_with_ticks_demo.html)

Lines with a ticked patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_step_demo_thumb.png)

[Step Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/step_demo.html)

Step Demo

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_alpha_thumb.png)

[fill\_between with transparency](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html)

fill\_between with transparency

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_demo_thumb.png)

[Fill the area between two lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html)

Fill the area between two lines

![](https://matplotlib.org/stable/_images/sphx_glr_fill_betweenx_demo_thumb.png)

[Fill the area between two vertical lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_betweenx_demo.html)

Fill the area between two vertical lines

![](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_thumb.png)

[EventCollection Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html)

EventCollection Demo

![](https://matplotlib.org/stable/_images/sphx_glr_timeline_thumb.png)

[Timeline with lines, dates, and text](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html)

Timeline with lines, dates, and text

![](https://matplotlib.org/stable/_images/sphx_glr_vline_hline_demo_thumb.png)

[hlines and vlines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html)

hlines and vlines

![](https://matplotlib.org/stable/_images/sphx_glr_span_regions_thumb.png)

[Shade regions defined by a logical mask using fill\_between](https://matplotlib.org/stable/gallery/lines_bars_and_markers/span_regions.html)

Shade regions defined by a logical mask using fill\_between

![](https://matplotlib.org/stable/_images/sphx_glr_categorical_variables_thumb.png)

[Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)

Plotting categorical variables

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_grids_thumb.png)

[pcolormesh grids and shading](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html)

pcolormesh grids and shading

![](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_thumb.png)

[Triinterp Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html)

Triinterp Demo

![](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_thumb.png)

[Contour plot of irregularly spaced data](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html)

Contour plot of irregularly spaced data

![](https://matplotlib.org/stable/_images/sphx_glr_contour_corner_mask_thumb.png)

[Contour corner mask](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_corner_mask.html)

Contour corner mask

![](https://matplotlib.org/stable/_images/sphx_glr_specgram_demo_thumb.png)

[Spectrogram](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html)

Spectrogram

![](https://matplotlib.org/stable/_images/sphx_glr_curve_error_band_thumb.png)

[Curve with error band](https://matplotlib.org/stable/gallery/statistics/curve_error_band.html)

Curve with error band

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_psd_demo_thumb.png)

[Power spectral density (PSD)](https://matplotlib.org/stable/gallery/statistics/psd_demo.html)

Power spectral density (PSD)

![](https://matplotlib.org/stable/_images/sphx_glr_csd_demo_thumb.png)

[Cross spectral density (CSD)](https://matplotlib.org/stable/gallery/statistics/csd_demo.html)

Cross spectral density (CSD)

![](https://matplotlib.org/stable/_images/sphx_glr_polar_demo_thumb.png)

[Polar plot](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)

Polar plot

![](https://matplotlib.org/stable/_images/sphx_glr_polar_legend_thumb.png)

[Polar legend](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html)

Polar legend

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_axes_demo_thumb.png)

[Axes Demo](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_demo.html)

Axes Demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_auto_subplots_adjust_thumb.png)

[Programmatically control subplot adjustment](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html)

Programmatically control subplot adjustment

![](https://matplotlib.org/stable/_images/sphx_glr_axes_margins_thumb.png)

[Controlling view limits using margins and sticky\_edges](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html)

Controlling view limits using margins and sticky\_edges

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_shared_axis_demo_thumb.png)

[Shared axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html)

Shared axis

![](https://matplotlib.org/stable/_images/sphx_glr_invert_axes_thumb.png)

[Inverted axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/invert_axes.html)

Inverted axis

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

![](https://matplotlib.org/stable/_images/sphx_glr_twin_axes_zorder_thumb.png)

[Twin Axes with delta\_zorder](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/twin_axes_zorder.html)

Twin Axes with delta\_zorder

![](https://matplotlib.org/stable/_images/sphx_glr_secondary_axis_thumb.png)

[Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html)

Secondary Axis

![](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_thumb.png)

[Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Align labels and titles

![](https://matplotlib.org/stable/_images/sphx_glr_axes_props_thumb.png)

[Axes properties](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_props.html)

Axes properties

![](https://matplotlib.org/stable/_images/sphx_glr_figure_title_thumb.png)

[Figure labels: suptitle, supxlabel, supylabel](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html)

Figure labels: suptitle, supxlabel, supylabel

![](https://matplotlib.org/stable/_images/sphx_glr_broken_axis_thumb.png)

[Broken axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html)

Broken axis

![](https://matplotlib.org/stable/_images/sphx_glr_axhspan_demo_thumb.png)

[Draw regions that span an Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html)

Draw regions that span an Axes

![](https://matplotlib.org/stable/_images/sphx_glr_major_minor_demo_thumb.png)

[Major and minor ticks](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html)

Major and minor ticks

![](https://matplotlib.org/stable/_images/sphx_glr_ticks_top_right_thumb.png)

[Move x/y-axis ticks and labels on top and right](https://matplotlib.org/stable/gallery/ticks/ticks_top_right.html)

Move x/y-axis ticks and labels on top and right

![](https://matplotlib.org/stable/_images/sphx_glr_centered_ticklabels_thumb.png)

[Center labels between ticks](https://matplotlib.org/stable/gallery/ticks/centered_ticklabels.html)

Center labels between ticks

![](https://matplotlib.org/stable/_images/sphx_glr_multilevel_ticks_thumb.png)

[Multilevel (nested) ticks](https://matplotlib.org/stable/gallery/ticks/multilevel_ticks.html)

Multilevel (nested) ticks

![](https://matplotlib.org/stable/_images/sphx_glr_dollar_ticks_thumb.png)

[Dollar ticks](https://matplotlib.org/stable/gallery/ticks/dollar_ticks.html)

Dollar ticks

![](https://matplotlib.org/stable/_images/sphx_glr_engineering_formatter_thumb.png)

[Format ticks using engineering notation](https://matplotlib.org/stable/gallery/ticks/engineering_formatter.html)

Format ticks using engineering notation

![](https://matplotlib.org/stable/_images/sphx_glr_engformatter_offset_thumb.png)

[SI prefixed offsets and natural order of magnitudes](https://matplotlib.org/stable/gallery/ticks/engformatter_offset.html)

SI prefixed offsets and natural order of magnitudes

![](https://matplotlib.org/stable/_images/sphx_glr_tick_labels_from_values_thumb.png)

[Setting tick labels from a list of values](https://matplotlib.org/stable/gallery/ticks/tick_labels_from_values.html)

Setting tick labels from a list of values

![](https://matplotlib.org/stable/_images/sphx_glr_date_thumb.png)

[Date tick labels](https://matplotlib.org/stable/gallery/ticks/date.html)

Date tick labels

![](https://matplotlib.org/stable/_images/sphx_glr_date_concise_formatter_thumb.png)

[Format date ticks using ConciseDateFormatter](https://matplotlib.org/stable/gallery/ticks/date_concise_formatter.html)

Format date ticks using ConciseDateFormatter

![](https://matplotlib.org/stable/_images/sphx_glr_date_demo_convert_thumb.png)

[Date converter demo](https://matplotlib.org/stable/gallery/ticks/date_demo_convert.html)

Date converter demo

![](https://matplotlib.org/stable/_images/sphx_glr_date_index_formatter_thumb.png)

[Custom tick formatter for time series](https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html)

Custom tick formatter for time series

![](https://matplotlib.org/stable/_images/sphx_glr_date_precision_and_epochs_thumb.png)

[Date precision and epochs](https://matplotlib.org/stable/gallery/ticks/date_precision_and_epochs.html)

Date precision and epochs

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

![](https://matplotlib.org/stable/_images/sphx_glr_spines_thumb.png)

[Spines](https://matplotlib.org/stable/gallery/spines/spines.html)

Spines

![](https://matplotlib.org/stable/_images/sphx_glr_spine_placement_demo_thumb.png)

[Spine placement](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html)

Spine placement

![](https://matplotlib.org/stable/_images/sphx_glr_centered_spines_with_arrows_thumb.png)

[Centered spines with arrows](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html)

Centered spines with arrows

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_text_rotation_relative_to_line_thumb.png)

[Text rotation angle in data coordinates](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_rotation_relative_to_line.html)

Text rotation angle in data coordinates

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

![](https://matplotlib.org/stable/_images/sphx_glr_legend_thumb.png)

[Legend using pre-defined labels](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend.html)

Legend using pre-defined labels

![](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_thumb.png)

[Compose custom legends](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html)

Compose custom legends

![](https://matplotlib.org/stable/_images/sphx_glr_accented_text_thumb.png)

[Accented text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html)

Accented text

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_demo_thumb.png)

[Mathtext](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_demo.html)

Mathtext

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_fontfamily_example_thumb.png)

[Math fontfamily](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_fontfamily_example.html)

Math fontfamily

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_thumb.png)

[Title positioning](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html)

Title positioning

![](https://matplotlib.org/stable/_images/sphx_glr_watermark_text_thumb.png)

[Text watermark](https://matplotlib.org/stable/gallery/text_labels_and_annotations/watermark_text.html)

Text watermark

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_arrow_thumb.png)

[Ellipse with orientation arrow demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html)

Ellipse with orientation arrow demo

![](https://matplotlib.org/stable/_images/sphx_glr_path_patch_thumb.png)

[PathPatch object](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html)

PathPatch object

![](https://matplotlib.org/stable/_images/sphx_glr_quad_bezier_thumb.png)

[Bezier curve](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html)

Bezier curve

![](https://matplotlib.org/stable/_images/sphx_glr_color_demo_thumb.png)

[Color Demo](https://matplotlib.org/stable/gallery/color/color_demo.html)

Color Demo

![](https://matplotlib.org/stable/_images/sphx_glr_color_by_yvalue_thumb.png)

[Color by y-value](https://matplotlib.org/stable/gallery/color/color_by_yvalue.html)

Color by y-value

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_default_thumb.png)

[Colors in the default property cycle](https://matplotlib.org/stable/gallery/color/color_cycle_default.html)

Colors in the default property cycle

![](https://matplotlib.org/stable/_images/sphx_glr_individual_colors_from_cmap_thumb.png)

[Selecting individual colors from a colormap](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html)

Selecting individual colors from a colormap

![](https://matplotlib.org/stable/_images/sphx_glr_dark_background_thumb.png)

[Dark background style sheet](https://matplotlib.org/stable/gallery/style_sheets/dark_background.html)

Dark background style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_fivethirtyeight_thumb.png)

[FiveThirtyEight style sheet](https://matplotlib.org/stable/gallery/style_sheets/fivethirtyeight.html)

FiveThirtyEight style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_ggplot_thumb.png)

[ggplot style sheet](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html)

ggplot style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_lines3d_thumb.png)

[Parametric curve](https://matplotlib.org/stable/gallery/mplot3d/lines3d.html)

Parametric curve

![](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_thumb.png)

[Lorenz attractor](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html)

Lorenz attractor

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_scales3d_thumb.png)

[Scales on 3D (Log, Symlog, etc.)](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html)

Scales on 3D (Log, Symlog, etc.)

![](https://matplotlib.org/stable/_images/sphx_glr_demo_fixed_size_axes_thumb.png)

[Axes with a fixed physical size](https://matplotlib.org/stable/gallery/axes_grid1/demo_fixed_size_axes.html)

Axes with a fixed physical size

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple_thumb.png)

[Parasite Simple](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple.html)

Parasite Simple

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline4_thumb.png)

[Simple Axisline4](https://matplotlib.org/stable/gallery/axes_grid1/simple_axisline4.html)

Simple Axisline4

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axisline_style_thumb.png)

[Axis line styles](https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html)

Axis line styles

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes_thumb.png)

[Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)

Parasite Axes demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_thumb.png)

[Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)

Parasite axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisartist1_thumb.png)

[Custom spines with axisartist](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html)

Custom spines with axisartist

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_thumb.png)

[Simple Axisline](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html)

Simple Axisline

![](https://matplotlib.org/stable/_images/sphx_glr_simple_anim_thumb.gif)

[Basic animated line plot](https://matplotlib.org/stable/gallery/animation/simple_anim.html)

Basic animated line plot

![](https://matplotlib.org/stable/_images/sphx_glr_animate_decay_thumb.gif)

[Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)

Decay

![](https://matplotlib.org/stable/_images/sphx_glr_bayes_update_thumb.gif)

[The Bayes update](https://matplotlib.org/stable/gallery/animation/bayes_update.html)

The Bayes update

![](https://matplotlib.org/stable/_images/sphx_glr_double_pendulum_thumb.gif)

[The double pendulum problem](https://matplotlib.org/stable/gallery/animation/double_pendulum.html)

The double pendulum problem

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

![](https://matplotlib.org/stable/_images/sphx_glr_random_walk_thumb.gif)

[Animated 3D random walk](https://matplotlib.org/stable/gallery/animation/random_walk.html)

Animated 3D random walk

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

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_thumb.png)

[Cursor](https://matplotlib.org/stable/gallery/widgets/cursor.html)

Cursor

![](https://matplotlib.org/stable/_images/sphx_glr_multicursor_thumb.png)

[Multicursor](https://matplotlib.org/stable/gallery/widgets/multicursor.html)

Multicursor

![](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_thumb.png)

[Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)

Radio Buttons Grid

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

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

![](https://matplotlib.org/stable/_images/sphx_glr_coords_demo_thumb.png)

[Mouse move and click events](https://matplotlib.org/stable/gallery/event_handling/coords_demo.html)

Mouse move and click events

![](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_thumb.png)

[Cross-hair cursor](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html)

Cross-hair cursor

![](https://matplotlib.org/stable/_images/sphx_glr_data_browser_thumb.png)

[Data browser](https://matplotlib.org/stable/gallery/event_handling/data_browser.html)

Data browser

![](https://matplotlib.org/stable/_images/sphx_glr_keypress_demo_thumb.png)

[Keypress event](https://matplotlib.org/stable/gallery/event_handling/keypress_demo.html)

Keypress event

![](https://matplotlib.org/stable/_images/sphx_glr_legend_picking_thumb.png)

[Legend picking](https://matplotlib.org/stable/gallery/event_handling/legend_picking.html)

Legend picking

![](https://matplotlib.org/stable/_images/sphx_glr_looking_glass_thumb.png)

[Looking glass](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html)

Looking glass

![](https://matplotlib.org/stable/_images/sphx_glr_path_editor_thumb.png)

[Path editor](https://matplotlib.org/stable/gallery/event_handling/path_editor.html)

Path editor

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo2_thumb.png)

[Pick event demo 2](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo2.html)

Pick event demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_resample_thumb.png)

[Resampling Data](https://matplotlib.org/stable/gallery/event_handling/resample.html)

Resampling Data

![](https://matplotlib.org/stable/_images/sphx_glr_timers_thumb.png)

[Timers](https://matplotlib.org/stable/gallery/event_handling/timers.html)

Timers

![](https://matplotlib.org/stable/_images/sphx_glr_canvasagg_thumb.png)

[CanvasAgg demo](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html)

CanvasAgg demo

![](https://matplotlib.org/stable/_images/sphx_glr_evans_test_thumb.png)

[Evans test](https://matplotlib.org/stable/gallery/units/evans_test.html)

Evans test

![](https://matplotlib.org/stable/_images/sphx_glr_bbox_intersect_thumb.png)

[Identify whether artists intersect](https://matplotlib.org/stable/gallery/misc/bbox_intersect.html)

Identify whether artists intersect

![](https://matplotlib.org/stable/_images/sphx_glr_custom_projection_thumb.png)

[Custom projection](https://matplotlib.org/stable/gallery/misc/custom_projection.html)

Custom projection

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_line_thumb.png)

[Apply SVG filter to a line](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html)

Apply SVG filter to a line

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_zorder_demo_thumb.png)

[Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)

Zorder Demo

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_integral_thumb.png)

[Integral as the area under a curve](https://matplotlib.org/stable/gallery/showcase/integral.html)

Integral as the area under a curve

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_anscombe_thumb.png)

[Anscombe's quartet](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html)

Anscombe's quartet

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_radar_chart_thumb.png)

[Radar chart (aka spider or star chart)](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html)

Radar chart (aka spider or star chart)

![](https://matplotlib.org/stable/_images/sphx_glr_artists_thumb.png)

[Artist tutorial](https://matplotlib.org/stable/tutorials/artists.html)

Artist tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_thumb.png)

[Coding shortcuts](https://matplotlib.org/stable/tutorials/coding_shortcuts.html)

Coding shortcuts

![](https://matplotlib.org/stable/_images/sphx_glr_plot_thumb.png)

[plot(x, y)](https://matplotlib.org/stable/plot_types/basic/plot.html)

plot(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_thumb.png)

[fill\_between(x, y1, y2)](https://matplotlib.org/stable/plot_types/basic/fill_between.html)

fill\_between(x, y1, y2)

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_thumb.png)

[tricontour(x, y, z)](https://matplotlib.org/stable/plot_types/unstructured/tricontour.html)

tricontour(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_tricontourf_thumb.png)

[tricontourf(x, y, z)](https://matplotlib.org/stable/plot_types/unstructured/tricontourf.html)

tricontourf(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_tripcolor_thumb.png)

[tripcolor(x, y, z)](https://matplotlib.org/stable/plot_types/unstructured/tripcolor.html)

tripcolor(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between3d_simple_thumb.png)

[fill\_between(x1, y1, z1, x2, y2, z2)](https://matplotlib.org/stable/plot_types/3D/fill_between3d_simple.html)

fill\_between(x1, y1, z1, x2, y2, z2)

![](https://matplotlib.org/stable/_images/sphx_glr_plot3d_simple_thumb.png)

[plot(xs, ys, zs)](https://matplotlib.org/stable/plot_types/3D/plot3d_simple.html)

plot(xs, ys, zs)

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_animations_thumb.gif)

[Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html)

Animations using Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_blitting_thumb.png)

[Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html)

Faster rendering by using blitting

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_thumb.png)

[Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html)

Styling with cycler

![](https://matplotlib.org/stable/_images/sphx_glr_paths_thumb.png)

[Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html)

Path Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_autoscale_thumb.png)

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)

Axis autoscaling

![](https://matplotlib.org/stable/_images/sphx_glr_axes_scales_thumb.png)

[Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)

Axis scales

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

![](https://matplotlib.org/stable/_images/sphx_glr_axes_units_thumb.png)

[Plotting dates and strings](https://matplotlib.org/stable/users/explain/axes/axes_units.html)

Plotting dates and strings

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_thumb.png)

[Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)

Legend guide

![](https://matplotlib.org/stable/_images/sphx_glr_mosaic_thumb.png)

[Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html)

Complex and semantic figure composition (subplot\_mosaic)

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page