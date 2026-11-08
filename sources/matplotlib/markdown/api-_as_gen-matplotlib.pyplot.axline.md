[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html#main-content)

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
    

matplotlib.pyplot.axline[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html#matplotlib-pyplot-axline "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.axline(_xy1_, _xy2\=None_, _\*_, _slope\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3101-L3109)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html#matplotlib.pyplot.axline "Link to this definition")

Add an infinitely long straight line.

The line can be defined either by two points _xy1_ and _xy2_, or by one point _xy1_ and a _slope_.

This draws a straight line "on the screen", regardless of the x and y scales, and is thus also suitable for drawing exponential decays in semilog plots, power laws in loglog plots, etc. However, _slope_ should only be used with linear scales; It has no clear meaning for all other scales, and thus the behavior is undefined. Please specify the line using the points _xy1_, _xy2_ for non-linear scales.

The _transform_ keyword argument only applies to the points _xy1_, _xy2_. The _slope_ (if given) is always in data coordinates. This can be used e.g. with `ax.transAxes` for drawing grid lines with a fixed slope.

Parameters:

**xy1, xy2**(float, float)

Points for the line to pass through. Either _xy2_ or _slope_ has to be given.

**slope**float, optional

The slope of the line. Either _xy2_ or _slope_ has to be given.

Returns:

[`AxLine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine "matplotlib.lines.AxLine")

Other Parameters:

**\*\*kwargs**

Valid kwargs are [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 properties

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

[`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline")

for horizontal lines

[`axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")

for vertical lines

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
.

Examples

Draw a thick red line passing through (0, 0) and (1, 1):

\>>> axline((0, 0), (1, 1), linewidth\=4, color\='r')

Examples using `matplotlib.pyplot.axline`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html#examples-using-matplotlib-pyplot-axline "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_axline_thumb.png)

[Infinite lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/axline.html)

Infinite lines

![](https://matplotlib.org/stable/_images/sphx_glr_anscombe_thumb.png)

[Anscombe's quartet](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html)

Anscombe's quartet

On this page