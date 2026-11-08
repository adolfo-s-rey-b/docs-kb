[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#main-content)

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
    

matplotlib.pyplot.table[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#matplotlib-pyplot-table "Link to this heading")

==================================================================================================================================================

matplotlib.pyplot.table(_cellText\=None_, _cellColours\=None_, _cellLoc\='right'_, _colWidths\=None_, _rowLabels\=None_, _rowColours\=None_, _rowLoc\='left'_, _colLabels\=None_, _colColours\=None_, _colLoc\='center'_, _loc\='bottom'_, _bbox\=None_, _edges\='closed'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4350-L4382)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table "Link to this definition")

Add a table to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

Note

`table()` has some fundamental design limitations and will not be developed further. If you need more functionality, consider [blume](https://github.com/swfiua/blume)
.

At least one of _cellText_ or _cellColours_ must be specified. These parameters must be 2D lists, in which the outer lists define the rows and the inner list define the column values per row. Each row must have the same number of elements.

The table can optionally have row and column headers, which are configured using _rowLabels_, _rowColours_, _rowLoc_ and _colLabels_, _colColours_, _colLoc_ respectively.

For finer grained control over tables, use the [`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 class and add it to the Axes with [`Axes.add_table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_table.html#matplotlib.axes.Axes.add_table "matplotlib.axes.Axes.add_table")
.

Parameters:

**cellText**2D list of str or pandas.DataFrame, optional

The texts to place into the table cells.

_Note_: Line breaks in the strings are currently not accounted for and will result in the text exceeding the cell boundaries.

**cellColours**2D list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The background colors of the cells.

**cellLoc**{'right', 'center', 'left'}

The alignment of the text within the cells.

**colWidths**list of float, optional

The column widths in units of the axes. If not given, all columns will have a width of _1 / ncols_.

**rowLabels**list of str, optional

The text of the row header cells.

**rowColours**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the row header cells.

**rowLoc**{'left', 'center', 'right'}

The text alignment of the row header cells.

**colLabels**list of str, optional

The text of the column header cells.

**colColours**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

The colors of the column header cells.

**colLoc**{'center', 'left', 'right'}

The text alignment of the column header cells.

**loc**str, default: 'bottom'

The position of the cell with respect to _ax_. This must be one of the [`codes`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.codes "matplotlib.table.Table.codes")
.

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or \[xmin, ymin, width, height\], optional

A bounding box to draw the table into. If this is not _None_, this overrides _loc_.

**edges**{'closed', 'open', 'horizontal', 'vertical'} or substring of 'BRTL'

The cell edges to be drawn with a line. See also [`visible_edges`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Cell.visible_edges "matplotlib.table.Cell.visible_edges")
.

Returns:

[`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")

The created table.

Other Parameters:

**\*\*kwargs**

[`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 properties.

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fontsize`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table.set_fontsize "matplotlib.table.Table.set_fontsize") | float |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.table.html#matplotlib.axes.Axes.table "matplotlib.axes.Axes.table")
.

Examples using `matplotlib.pyplot.table`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#examples-using-matplotlib-pyplot-table "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_table_demo_thumb.png)

[Table Demo](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

On this page