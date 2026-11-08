[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#main-content)

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
    

matplotlib.pyplot.plot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib-pyplot-plot "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.plot(_\*args_, _scalex\=True_, _scaley\=True_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4035-L4049)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "Link to this definition")

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

*   The most straight forward way is just to call [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
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

[`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")

XY scatter plot with markers of varying size and/or color ( sometimes also called bubble chart).

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
.

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

Examples using `matplotlib.pyplot.plot`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#examples-using-matplotlib-pyplot-plot "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_simple_plot_thumb.png)

[Line plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)

Line plot

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_masked_thumb.png)

[Scatter plot with masked values](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_masked.html)

Scatter plot with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_thumb.png)

[Stairs Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html)

Stairs Demo

![](https://matplotlib.org/stable/_images/sphx_glr_step_demo_thumb.png)

[Step Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/step_demo.html)

Step Demo

![](https://matplotlib.org/stable/_images/sphx_glr_masked_demo_thumb.png)

[Plotting masked and NaN values](https://matplotlib.org/stable/gallery/lines_bars_and_markers/masked_demo.html)

Plotting masked and NaN values

![](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_thumb.png)

[Triinterp Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html)

Triinterp Demo

![](https://matplotlib.org/stable/_images/sphx_glr_polar_demo_thumb.png)

[Polar plot](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)

Polar plot

![](https://matplotlib.org/stable/_images/sphx_glr_polar_legend_thumb.png)

[Polar legend](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html)

Polar legend

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_figs_demo_thumb.png)

[Manage multiple figures in pyplot](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_figs_demo.html)

Manage multiple figures in pyplot

![](https://matplotlib.org/stable/_images/sphx_glr_custom_figure_class_thumb.png)

[Custom Figure subclasses](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/custom_figure_class.html)

Custom Figure subclasses

![](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_thumb.png)

[Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Align labels and titles

![](https://matplotlib.org/stable/_images/sphx_glr_date_demo_rrule_thumb.png)

[Placing date ticks using recurrence rules](https://matplotlib.org/stable/gallery/ticks/date_demo_rrule.html)

Placing date ticks using recurrence rules

![](https://matplotlib.org/stable/_images/sphx_glr_custom_scale_thumb.png)

[Custom scale](https://matplotlib.org/stable/gallery/scales/custom_scale.html)

Custom scale

![](https://matplotlib.org/stable/_images/sphx_glr_text_fontdict_thumb.png)

[Controlling style of text and labels using a dictionary](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html)

Controlling style of text and labels using a dictionary

![](https://matplotlib.org/stable/_images/sphx_glr_legend_thumb.png)

[Legend using pre-defined labels](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend.html)

Legend using pre-defined labels

![](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_thumb.png)

[Title positioning](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html)

Title positioning

![](https://matplotlib.org/stable/_images/sphx_glr_dolphin_thumb.png)

[Dolphins](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html)

Dolphins

![](https://matplotlib.org/stable/_images/sphx_glr_color_by_yvalue_thumb.png)

[Color by y-value](https://matplotlib.org/stable/gallery/color/color_by_yvalue.html)

Color by y-value

![](https://matplotlib.org/stable/_images/sphx_glr_plot_solarizedlight2_thumb.png)

[Solarized Light stylesheet](https://matplotlib.org/stable/gallery/style_sheets/plot_solarizedlight2.html)

Solarized Light stylesheet

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_simple_thumb.png)

[Basic plot](https://matplotlib.org/stable/gallery/pyplots/pyplot_simple.html)

Basic plot

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_two_subplots_thumb.png)

[Two subplots using pyplot](https://matplotlib.org/stable/gallery/pyplots/pyplot_two_subplots.html)

Two subplots using pyplot

![](https://matplotlib.org/stable/_images/sphx_glr_frame_grabbing_sgskip_thumb.png)

[Frame grabbing](https://matplotlib.org/stable/gallery/animation/frame_grabbing_sgskip.html)

Frame grabbing

![](https://matplotlib.org/stable/_images/sphx_glr_canvasagg_thumb.png)

[CanvasAgg demo](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html)

CanvasAgg demo

![](https://matplotlib.org/stable/_images/sphx_glr_toolmanager_sgskip_thumb.png)

[Tool Manager](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html)

Tool Manager

![](https://matplotlib.org/stable/_images/sphx_glr_coords_report_thumb.png)

[Coords Report](https://matplotlib.org/stable/gallery/misc/coords_report.html)

Coords Report

![](https://matplotlib.org/stable/_images/sphx_glr_customize_rc_thumb.png)

[Customize Rc](https://matplotlib.org/stable/gallery/misc/customize_rc.html)

Customize Rc

![](https://matplotlib.org/stable/_images/sphx_glr_findobj_demo_thumb.png)

[Findobj Demo](https://matplotlib.org/stable/gallery/misc/findobj_demo.html)

Findobj Demo

![](https://matplotlib.org/stable/_images/sphx_glr_multipage_pdf_thumb.svg)

[Multipage PDF](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html)

Multipage PDF

![](https://matplotlib.org/stable/_images/sphx_glr_print_stdout_sgskip_thumb.png)

[Print image to stdout](https://matplotlib.org/stable/gallery/misc/print_stdout_sgskip.html)

Print image to stdout

![](https://matplotlib.org/stable/_images/sphx_glr_set_and_get_thumb.png)

[Set and get properties](https://matplotlib.org/stable/gallery/misc/set_and_get.html)

Set and get properties

![](https://matplotlib.org/stable/_images/sphx_glr_transoffset_thumb.png)

[transforms.offset\_copy](https://matplotlib.org/stable/gallery/misc/transoffset.html)

transforms.offset\_copy

![](https://matplotlib.org/stable/_images/sphx_glr_zorder_demo_thumb.png)

[Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)

Zorder Demo

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_customizing_thumb.png)

[Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)

Customizing Matplotlib with style sheets and rcParams

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_patheffects_guide_thumb.png)

[Path effects guide](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html)

Path effects guide

On this page