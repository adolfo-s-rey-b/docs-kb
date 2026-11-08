[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#main-content)

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
    

matplotlib.axes.Axes.vlines[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib-axes-axes-vlines "Link to this heading")

==============================================================================================================================================================

Axes.vlines(_x_, _ymin_, _ymax_, _colors\=None_, _linestyles\='solid'_, _\*_, _label\=''_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L1205-L1295)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "Link to this definition")

Plot vertical lines at each _x_ from _ymin_ to _ymax_.

Parameters:

**x**float or array-like

x-indexes where to plot the lines.

**ymin, ymax**float or array-like

Respective beginning and end of each line. If scalars are provided, all lines will have the same length.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of color, default: `[rcParams["lines.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.color#rcparam-lines-color) ` (default: `'C0'`)

**linestyles**{'solid', 'dashed', 'dashdot', 'dotted'}, default: 'solid'

**label**str, default: ''

Returns:

[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

Other Parameters:

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_x_, _ymin_, _ymax_, _colors_

**\*\*kwargs**[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 properties.

See also

[`hlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html#matplotlib.axes.Axes.hlines "matplotlib.axes.Axes.hlines")

horizontal lines

[`axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")

vertical line across the Axes

Examples using `matplotlib.axes.Axes.vlines`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#examples-using-matplotlib-axes-axes-vlines "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_timeline_thumb.png)

[Timeline with lines, dates, and text](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html)

Timeline with lines, dates, and text

![](https://matplotlib.org/stable/_images/sphx_glr_vline_hline_demo_thumb.png)

[hlines and vlines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/vline_hline_demo.html)

hlines and vlines

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_thumb.png)

[Angle annotations on bracket arrows](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html)

Angle annotations on bracket arrows

On this page