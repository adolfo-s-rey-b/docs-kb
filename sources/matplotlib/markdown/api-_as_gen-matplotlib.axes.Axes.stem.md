[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#main-content)

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
    

matplotlib.axes.Axes.stem[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib-axes-axes-stem "Link to this heading")

========================================================================================================================================================

Axes.stem(_\*args_, _linefmt\=None_, _markerfmt\=None_, _basefmt\=None_, _bottom\=0_, _label\=None_, _orientation\='vertical'_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L3375-L3535)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "Link to this definition")

Create a stem plot.

A stem plot draws lines perpendicular to a baseline at each location _locs_ from the baseline to _heads_, and places a marker there. For vertical stem plots (the default), the _locs_ are _x_ positions, and the _heads_ are _y_ values. For horizontal stem plots, the _locs_ are _y_ positions, and the _heads_ are _x_ values.

Call signature:

stem(\[locs,\] heads, linefmt\=None, markerfmt\=None, basefmt\=None)

The _locs_\-positions are optional. _linefmt_ may be provided as positional, but all other formats must be provided as keyword arguments.

Parameters:

**locs**array-like, default: (0, 1, ..., len(heads) - 1)

For vertical stem plots, the x-positions of the stems. For horizontal stem plots, the y-positions of the stems.

**heads**array-like

For vertical stem plots, the y-values of the stem heads. For horizontal stem plots, the x-values of the stem heads.

**linefmt**str, optional

A string defining the color and/or linestyle of the vertical lines:

| Character | Line Style |
| --- | --- |
| `'-'` | solid line |
| `'--'` | dashed line |
| `'-.'` | dash-dot line |
| `':'` | dotted line |

Default: 'C0-', i.e. solid line with the first color of the color cycle.

Note: Markers specified through this parameter (e.g. 'x') will be silently ignored. Instead, markers should be specified using _markerfmt_.

**markerfmt**str, optional

A string defining the color and/or shape of the markers at the stem heads. If the marker is not given, use the marker 'o', i.e. filled circles. If the color is not given, use the color from _linefmt_.

**basefmt**str, default: 'C3-' ('C2-' in classic mode)

A format string defining the properties of the baseline.

**orientation**{'vertical', 'horizontal'}, default: 'vertical'

The orientation of the stems.

**bottom**float, default: 0

The y/x-position of the baseline (depending on _orientation_).

**label**str, optional

The label to use for the stems in legends.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

Returns:

[`StemContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.StemContainer "matplotlib.container.StemContainer")

The container may be treated like a tuple (_markerline_, _stemlines_, _baseline_)

Notes

See also

The MATLAB function [stem](https://www.mathworks.com/help/matlab/ref/stem.html)
 which inspired this method.

Examples using `matplotlib.axes.Axes.stem`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#examples-using-matplotlib-axes-axes-stem "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_stem_plot_thumb.png)

[Stem plot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html)

Stem plot

![](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_thumb.png)

[Legend Demo](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

Legend Demo

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_thumb.png)

[3D stem](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html)

3D stem

![](https://matplotlib.org/stable/_images/sphx_glr_stem_thumb.png)

[stem(x, y)](https://matplotlib.org/stable/plot_types/basic/stem.html)

stem(x, y)

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_thumb.png)

[stem(x, y, z)](https://matplotlib.org/stable/plot_types/3D/stem3d.html)

stem(x, y, z)

On this page