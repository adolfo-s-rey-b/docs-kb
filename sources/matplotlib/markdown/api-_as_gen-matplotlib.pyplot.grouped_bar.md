[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#main-content)

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
    

matplotlib.pyplot.grouped\_bar[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#matplotlib-pyplot-grouped-bar "Link to this heading")

=====================================================================================================================================================================

matplotlib.pyplot.grouped\_bar(_heights_, _\*_, _positions\=None_, _group\_spacing\=1.5_, _bar\_spacing\=0_, _tick\_labels\=None_, _labels\=None_, _orientation\='vertical'_, _colors\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3556-L3579)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#matplotlib.pyplot.grouped_bar "Link to this definition")

Make a grouped bar plot.

Added in version 3.11: The API is still provisional. We may still fine-tune some aspects based on user-feedback.

Grouped bar charts visualize a collection of categorical datasets. Each value in a dataset belongs to a distinct category and these categories are the same across all datasets. The categories typically have string names, but could also be dates or index keys. The values in each dataset are represented by a sequence of bars of the same color. The bars of all datasets are grouped together by their shared categories. The category names are drawn as the tick labels for each bar group. Each dataset has a distinct bar color, and can optionally get a label that is used for the legend.

Example:

grouped\_bar(\[dataset\_0, dataset\_1, dataset\_2\],
            tick\_labels\=\['A', 'B'\],
            labels\=\['dataset 0', 'dataset 1', 'dataset 2'\])

([`Source code`](https://matplotlib.org/stable/_downloads/c812a88242d269496de6d6c914c08aba/grouped_bar.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c7ffb53f33e269e9d058b705fe773972/grouped_bar.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8e7f8052b20a0d1ece379805b6435ad5/grouped_bar.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-grouped_bar.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-grouped_bar.2x.png)

Parameters:

**heights**list of array-like or dict of array-like or 2D array or pandas.DataFrame

The heights for all x and groups. One of:

*   list of array-like: A list of datasets, each dataset must have the same number of elements.
    
    \#           category\_A, category\_B
    dataset\_0 = \[value\_0\_A, value\_0\_B\]
    dataset\_1 = \[value\_1\_A, value\_1\_B\]
    dataset\_2 = \[value\_2\_A, value\_2\_B\]
    
    Example call:
    
    grouped\_bar(\[dataset\_0, dataset\_1, dataset\_2\])
    
*   dict of array-like: A mapping from names to datasets. Each dataset (dict value) must have the same number of elements.
    
    Example call:
    
    data\_dict \= {'ds0': dataset\_0, 'ds1': dataset\_1, 'ds2': dataset\_2}
    grouped\_bar(data\_dict)
    
    The names are used as _labels_, i.e. this is equivalent to
    
    grouped\_bar(data\_dict.values(), labels\=data\_dict.keys())
    
    When using a dict input, you must not pass _labels_ explicitly.
    
*   a 2D array: The rows are the categories, the columns are the different datasets.
    
                dataset\_0 dataset\_1 dataset\_2
    category\_A    ds0\_a     ds1\_a     ds2\_a
    category\_B    ds0\_b     ds1\_b     ds2\_b
    
    Example call:
    
    categories \= \["A", "B"\]
    dataset\_labels \= \["dataset\_0", "dataset\_1", "dataset\_2"\]
    array \= np.random.random((2, 3))
    grouped\_bar(array, tick\_labels\=categories, labels\=dataset\_labels)
    
*   a [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
    .
    
    The index is used for the categories, the columns are used for the datasets.
    
    df \= pd.DataFrame(
        np.random.random((2, 3)),
        index\=\["A", "B"\],
        columns\=\["dataset\_0", "dataset\_1", "dataset\_2"\]
    )
    grouped\_bar(df)
    
    i.e. this is equivalent to
    
    grouped\_bar(df.to\_numpy(), tick\_labels\=df.index, labels\=df.columns)
    
    Note that `grouped_bar(df)` produces a structurally equivalent plot like `df.plot.bar()`.
    

**positions**array-like, optional

The center positions of the bar groups. The values have to be equidistant. If not given, a sequence of integer positions 0, 1, 2, ... is used.

**tick\_labels**list of str, optional

The category labels, which are placed on ticks at the center _positions_ of the bar groups. If not set, the axis ticks (positions and labels) are left unchanged.

**labels**list of str, optional

The labels of the datasets, i.e. the bars within one group. These will show up in the legend.

**group\_spacing**float, default: 1.5

The space between two bar groups as a multiple of bar width.

The default value of 1.5 thus means that there's a gap of 1.5 bar widths between bar groups.

**bar\_spacing**float, default: 0

The space between bars as a multiple of bar width.

**orientation**{"vertical", "horizontal"}, default: "vertical"

The direction of the bars.

**colors**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

A sequence of colors to be cycled through and used to color bars of the different datasets. The sequence need not be exactly the same length as the number of provided y, in which case the colors will repeat from the beginning.

If not specified, the colors from the Axes property cycle will be used.

**\*\*kwargs**[`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 properties

Properties applied to all bars. The following properties additionally accept a sequence of values corresponding to the datasets in _heights_:

*   _edgecolor_
    
*   _facecolor_
    
*   _linewidth_
    
*   _linestyle_
    
*   _hatch_
    

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

Returns:

\_GroupedBarReturn

A provisional result object. This will be refined in the future. For now, the guaranteed API on the returned object is limited to

*   the attribute `bar_containers`, which is a list of [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
    , i.e. the results of the individual [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     calls for each dataset.
    
*   a `remove()` method, that remove all bars from the Axes. See also [`Artist.remove()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove")
    .
    

See also

[`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")

A lower-level API for bar plots, with more degrees of freedom like individual bar sizes and colors.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
.

For a better understanding, we compare the [`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
 API with those of [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
.

**Comparison to bar()**

[`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
 intentionally deviates from the [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 API in some aspects. `bar(x, y)` is a lower-level API and places bars with height _y_ at explicit positions _x_. It also allows to specify individual bar widths and colors. This kind of detailed control and flexibility is difficult to manage and often not needed when plotting multiple datasets as a grouped bar plot. Therefore, `grouped_bar` focusses on the abstraction of bar plots as visualization of categorical data.

The following examples may help to transfer from `bar` to `grouped_bar`.

Positions are de-emphasized due to categories, and default to integer values. If you have used `range(N)` as positions, you can leave that value out:

bar(range(N), heights)
grouped\_bar(\[heights\])

If needed, positions can be passed as keyword arguments:

bar(x, heights)
grouped\_bar(\[heights\], positions\=x)

To place category labels in [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 you could use the argument _tick\_label_ or use a list of category names as _x_. [`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
 expects them in the argument _tick\_labels_:

bar(range(N), heights, tick\_label\=\["A", "B"\])
bar(\["A", "B"\], heights)
grouped\_bar(\[heights\], tick\_labels\=\["A", "B"\])

Dataset labels, which are shown in the legend, are still passed via the _label_ parameter:

bar(..., label\="dataset")
grouped\_bar(..., label\=\["dataset"\])

**Comparison to boxplot()**

Both, [`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
 and [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 visualize categorical data from multiple datasets. The basic API on _tick\_labels_ and _positions_ is the same, so that you can easily switch between plotting all individual values as [`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
 or the statistical distribution per category as [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
:

grouped\_bar(values, positions\=..., tick\_labels\=...)
boxplot(values, positions\=..., tick\_labels\=...)

Examples using `matplotlib.pyplot.grouped_bar`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#examples-using-matplotlib-pyplot-grouped-bar "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_hat_graph_thumb.png)

[Hat graph](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html)

Hat graph

On this page