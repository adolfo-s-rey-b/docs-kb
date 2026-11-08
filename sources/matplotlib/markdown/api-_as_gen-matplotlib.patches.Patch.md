[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#main-content)

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
    

matplotlib.patches.Patch[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib-patches-patch "Link to this heading")

=====================================================================================================================================================

class matplotlib.patches.Patch(_\*_, _edgecolor\=None_, _facecolor\=None_, _color\=None_, _linewidth\=None_, _linestyle\=None_, _antialiased\=None_, _hatch\=None_, _fill\=True_, _capstyle\=None_, _joinstyle\=None_, _hatchcolor\=None_, _edgegapcolor\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L27-L766)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

A patch is a 2D artist with a face color and an edge color.

If any of _edgecolor_, _facecolor_, _linewidth_, or _antialiased_ are _None_, they default to their rc params setting.

The following kwarg properties are supported

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | unknown |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
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
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

contains(_mouseevent_, _radius\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L131-L181)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.contains "Link to this definition")

Test whether the mouse event occurred in the patch.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Where the user clicked.

**radius**float, optional

Additional margin on the patch in target coordinates of [`Patch.get_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_transform "matplotlib.patches.Patch.get_transform")
. See [`Path.contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
 for further details.

If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the default value depends on the state of the object:

*   If [`Artist.get_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_picker.html#matplotlib.artist.Artist.get_picker "matplotlib.artist.Artist.get_picker")
     is a number, the default is that value. This is so that picking works as expected.
    
*   Otherwise if the edge color has a non-zero alpha, the default is half of the linewidth. This is so that all the colored pixels are "in" the patch.
    
*   Finally, if the edge has 0 alpha, the default is 0. This is so that patches without a stroked edge do not have points outside of the filled region report as "in" due to an invisible edge.
    

Returns:

(bool, empty dict)

contains\_point(_point_, _radius\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L183-L243)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.contains_point "Link to this definition")

Return whether the given point is inside the patch.

Parameters:

**point**(float, float)

The point (x, y) to check, in target coordinates of `.Patch.get_transform()`. These are display coordinates for patches that are added to a figure or Axes.

**radius**float, optional

Additional margin on the patch in target coordinates of [`Patch.get_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_transform "matplotlib.patches.Patch.get_transform")
. See [`Path.contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
 for further details.

If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the default value depends on the state of the object:

*   If [`Artist.get_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_picker.html#matplotlib.artist.Artist.get_picker "matplotlib.artist.Artist.get_picker")
     is a number, the default is that value. This is so that picking works as expected.
    
*   Otherwise if the edge color has a non-zero alpha, the default is half of the linewidth. This is so that all the colored pixels are "in" the patch.
    
*   Finally, if the edge has 0 alpha, the default is 0. This is so that patches without a stroked edge do not have points outside of the filled region report as "in" due to an invisible edge.
    

Returns:

bool

Notes

The proper use of this method depends on the transform of the patch. Isolated patches do not have a transform. In this case, the patch creation coordinates and the point coordinates match. The following example checks that the center of a circle is within the circle

\>>> center \= 0, 0
\>>> c \= Circle(center, radius\=1)
\>>> c.contains\_point(center)
True

The convention of checking against the transformed patch stems from the fact that this method is predominantly used to check if display coordinates (e.g. from mouse events) are within the patch. If you want to do the above check with data coordinates, you have to properly transform them first:

\>>> center \= 0, 0
\>>> c \= Circle(center, radius\=3)
\>>> plt.gca().add\_patch(c)
\>>> transformed\_interior\_point \= c.get\_data\_transform().transform((0, 2))
\>>> c.contains\_point(transformed\_interior\_point)
True

contains\_points(_points_, _radius\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L245-L284)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.contains_points "Link to this definition")

Return whether the given points are inside the patch.

Parameters:

**points**(N, 2) array

The points to check, in target coordinates of `self.get_transform()`. These are display coordinates for patches that are added to a figure or Axes. Columns contain x and y values.

**radius**float, optional

Additional margin on the patch in target coordinates of [`Patch.get_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_transform "matplotlib.patches.Patch.get_transform")
. See [`Path.contains_point`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "matplotlib.path.Path.contains_point")
 for further details.

If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the default value depends on the state of the object:

*   If [`Artist.get_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_picker.html#matplotlib.artist.Artist.get_picker "matplotlib.artist.Artist.get_picker")
     is a number, the default is that value. This is so that picking works as expected.
    
*   Otherwise if the edge color has a non-zero alpha, the default is half of the linewidth. This is so that all the colored pixels are "in" the patch.
    
*   Finally, if the edge has 0 alpha, the default is 0. This is so that patches without a stroked edge do not have points outside of the filled region report as "in" due to an invisible edge.
    

Returns:

length-N bool array

Notes

The proper use of this method depends on the transform of the patch. See the notes on [`Patch.contains_point`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.contains_point "matplotlib.patches.Patch.contains_point")
.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L738-L753)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

property fill[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.fill "Link to this definition")

Return whether the patch is filled.

get\_aa()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L335-L337)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_aa "Link to this definition")

Alias for [`get_antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_antialiased "matplotlib.patches.Patch.get_antialiased")
.

get\_antialiased()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L335-L337)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_antialiased "Link to this definition")

Return whether antialiasing is used for drawing.

get\_capstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L595-L597)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_capstyle "Link to this definition")

Return the capstyle.

get\_data\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L317-L322)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_data_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 mapping data coordinates to physical coordinates.

get\_ec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L339-L341)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_ec "Link to this definition")

Alias for [`get_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_edgecolor "matplotlib.patches.Patch.get_edgecolor")
.

get\_edgecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L339-L341)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_edgecolor "Link to this definition")

Return the edge color.

get\_edgegapcolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L449-L457)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_edgegapcolor "Link to this definition")

Return the edge gap color.

Added in version 3.11.

See also [`set_edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor")
.

get\_extents()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L307-L311)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_extents "Link to this definition")

Return the [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
's axis-aligned extents as a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
.

get\_facecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L343-L345)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_facecolor "Link to this definition")

Return the face color.

get\_fc()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L343-L345)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_fc "Link to this definition")

Alias for [`get_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_facecolor "matplotlib.patches.Patch.get_facecolor")
.

get\_fill()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L570-L572)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_fill "Link to this definition")

Return whether the patch is filled.

get\_hatch()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L652-L654)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_hatch "Link to this definition")

Return the hatching pattern.

get\_hatch\_linewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L660-L662)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_hatch_linewidth "Link to this definition")

Return the hatch linewidth.

get\_hatchcolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L347-L353)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_hatchcolor "Link to this definition")

Return the hatch color.

get\_joinstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L615-L617)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_joinstyle "Link to this definition")

Return the joinstyle.

get\_linestyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L359-L361)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_linestyle "Link to this definition")

Return the linestyle.

get\_linewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L355-L357)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_linewidth "Link to this definition")

Return the line width in points.

get\_ls()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L359-L361)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_ls "Link to this definition")

Alias for [`get_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_linestyle "matplotlib.patches.Patch.get_linestyle")
.

get\_lw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L355-L357)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_lw "Link to this definition")

Alias for [`get_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_linewidth "matplotlib.patches.Patch.get_linewidth")
.

get\_patch\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L324-L333)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_patch_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance mapping patch coordinates to data coordinates.

For example, one may define a patch of a circle which represents a radius of 5 by providing coordinates for a unit circle, and a transform which scales the coordinates (the patch coordinate) by 5.

get\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L755-L757)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_path "Link to this definition")

Return the path of this patch.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L313-L315)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 applied to the [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
.

get\_verts()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L105-L117)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_verts "Link to this definition")

Return a copy of the vertices used in this patch.

If the patch contains Bézier curves, the curves will be interpolated by line segments. To access the curves as curves, use [`get_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_path "matplotlib.patches.Patch.get_path")
.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L759-L760)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_window_extent "Link to this definition")

Get the artist's bounding box in display space, ignoring clipping.

The bounding box's width and height are non-negative.

Subclasses should override for inclusion in the bounding box "tight" calculation. Default is to return an empty bounding box at 0, 0.

Warning

The extent can change due to any changes in the transform stack, such as changing the Axes limits, the figure size, the canvas used (as is done when saving a figure), or the DPI.

Relying on a once-retrieved window extent can lead to unexpected behavior in various cases such as interactive figures being resized or moved to a screen with different dpi, or figures that look fine on screen render incorrectly when saved to file.

To get accurate results you may need to manually call [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 or [`draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
 to have Matplotlib compute the rendered size.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

See also

[`Artist.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "matplotlib.artist.Artist.get_tightbbox")

Get the artist bounding box, taking clipping into account.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _capstyle\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _edgegapcolor\=<UNSET>_, _facecolor\=<UNSET>_, _fill\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | unknown |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
> | [`capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "matplotlib.patches.Patch.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "matplotlib.patches.Patch.set_fill") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "matplotlib.patches.Patch.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "matplotlib.patches.Patch.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' or None |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "matplotlib.patches.Patch.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth") | float or None |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_aa(_aa_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L363-L372)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_aa "Link to this definition")

Alias for [`set_antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")
.

set\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L485-L491)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_alpha "Link to this definition")

Set the alpha value used for blending - not supported on all backends.

Parameters:

**alpha**float or None

_alpha_ must be within the 0-1 range, inclusive.

set\_antialiased(_aa_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L363-L372)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "Link to this definition")

Set whether to use antialiased rendering.

Parameters:

**aa**bool or None

set\_capstyle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L579-L593)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "Link to this definition")

Set the [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
.

The default capstyle is 'round' for [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
 and 'butt' for all other patches.

Parameters:

**s**[`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or {'butt', 'projecting', 'round'}

set\_color(_c_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L413-L428)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "Link to this definition")

Set both the edgecolor and the facecolor.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

See also

[`Patch.set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
, [`Patch.set_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")

For setting the edge or face color individually.

set\_ec(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L385-L394)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_ec "Link to this definition")

Alias for [`set_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")
.

set\_edgecolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L385-L394)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "Link to this definition")

Set the patch edge color.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or None

set\_edgegapcolor(_edgegapcolor_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L459-L483)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "Link to this definition")

Set a color to fill the gaps in the dashed edge style.

Added in version 3.11.

Note

Striped edges are created by drawing two interleaved dashed lines. There can be overlaps between those two, which may result in artifacts when using transparency.

This functionality is experimental and may change.

Parameters:

**edgegapcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or None

The color with which to fill the gaps. If None, the gaps are unfilled.

set\_facecolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L402-L411)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "Link to this definition")

Set the patch face color.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or None

set\_fc(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L402-L411)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fc "Link to this definition")

Alias for [`set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
.

set\_fill(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L556-L568)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "Link to this definition")

Set whether to fill the patch.

Parameters:

**b**bool

set\_hatch(_hatch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L619-L650)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "Link to this definition")

Set the hatching pattern.

_hatch_ can be one of:

/   \- diagonal hatching
\\   \- back diagonal
|   \- vertical
\-   \- horizontal
+   \- crossed
x   \- crossed diagonal
o   \- small circle
O   \- large circle
.   \- dots
\*   \- stars

Letters can be combined, in which case all the specified hatchings are done. If same letter repeats, it increases the density of hatching of that pattern.

In regular (non-raw) Python strings, backslashes must be doubled: `'\\\\'` and `r'\\'` are both a double back-diagonal hatch.

Parameters:

**hatch**{'/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '\*'}

set\_hatch\_linewidth(_lw_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L656-L658)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "Link to this definition")

Set the hatch linewidth.

set\_hatchcolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L438-L447)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "Link to this definition")

Set the patch hatch color.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or 'edge' or None

set\_joinstyle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L599-L613)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "Link to this definition")

Set the [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
.

The default joinstyle is 'round' for [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
 and 'miter' for all other patches.

Parameters:

**s**[`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 or {'miter', 'round', 'bevel'}

set\_linestyle(_ls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L507-L554)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "Link to this definition")

Set the patch linestyle.

Parameters:

**ls**{'-', '--', '-.', ':', '', ...} or (offset, on-off-seq)

Possible values:

*   A string:
    
    | linestyle | description |
    | --- | --- |
    | `'-'` or `'solid'` | solid line |
    | `'--'` or `'dashed'` | dashed line |
    | `'-.'` or `'dashdot'` | dash-dotted line |
    | `':'` or `'dotted'` | dotted line |
    | `''` or `'none'` (discouraged: `'None'`, `' '`) | draw nothing |
    
*   A tuple describing the start position and lengths of dashes and spaces:
    
    > (offset, onoffseq)
    
    where
    
    *   _offset_ is a float specifying the offset (in points); i.e. how much is the dash pattern shifted.
        
    *   _onoffseq_ is a sequence of on and off ink in points. There can be arbitrary many pairs of on and off values.
        
    
    Example: The tuple `(0, (10, 5, 1, 5))` means that the pattern starts at the beginning of the line. It draws a 10 point long dash, then a 5 point long space, then a 1 point long dash, followed by a 5 point long space, and then the pattern repeats.
    

For examples see [Linestyles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)
.

set\_linewidth(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L493-L505)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "Link to this definition")

Set the patch linewidth in points.

Parameters:

**w**float or None

set\_ls(_ls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L507-L554)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_ls "Link to this definition")

Alias for [`set_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle")
.

set\_lw(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L493-L505)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_lw "Link to this definition")

Alias for [`set_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")
.

update\_from(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L286-L305)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.update_from "Link to this definition")

Copy properties from _other_ to _self_.

zorder \= 1[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.zorder "Link to this definition")

Examples using `matplotlib.patches.Patch`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#examples-using-matplotlib-patches-patch "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_thumb.png)

[Stairs Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html)

Stairs Demo

![](https://matplotlib.org/stable/_images/sphx_glr_image_demo_thumb.png)

[Many ways to plot images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html)

Many ways to plot images

![](https://matplotlib.org/stable/_images/sphx_glr_image_clip_path_thumb.png)

[Clipping images with patches](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html)

Clipping images with patches

![](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_thumb.png)

[Placing images, preserving relative sizes](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html)

Placing images, preserving relative sizes

![](https://matplotlib.org/stable/_images/sphx_glr_errorbars_and_boxes_thumb.png)

[Create boxes from error bars using PatchCollection](https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html)

Create boxes from error bars using PatchCollection

![](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_thumb.png)

[Plot a confidence ellipse of a two-dimensional dataset](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html)

Plot a confidence ellipse of a two-dimensional dataset

![](https://matplotlib.org/stable/_images/sphx_glr_curve_error_band_thumb.png)

[Curve with error band](https://matplotlib.org/stable/gallery/statistics/curve_error_band.html)

Curve with error band

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_thumb.png)

[Boxplots](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html)

Boxplots

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_axes_margins_thumb.png)

[Controlling view limits using margins and sticky\_edges](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html)

Controlling view limits using margins and sticky\_edges

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_axes_zoom_effect_thumb.png)

[Axes zoom effect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html)

Axes zoom effect

![](https://matplotlib.org/stable/_images/sphx_glr_text_alignment_thumb.png)

[Text alignment](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html)

Text alignment

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_rotation_mode_thumb.png)

[Text rotation mode](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_rotation_mode.html)

Text rotation mode

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_path_thumb.png)

[Using a text as a Path](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html)

Using a text as a Path

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_thumb.png)

[Angle annotations on bracket arrows](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html)

Angle annotations on bracket arrows

![](https://matplotlib.org/stable/_images/sphx_glr_placing_text_boxes_thumb.png)

[Placing text boxes](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html)

Placing text boxes

![](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_thumb.png)

[Artists as annotations](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html)

Artists as annotations

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_thumb.png)

[Compose custom legends](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html)

Compose custom legends

![](https://matplotlib.org/stable/_images/sphx_glr_arrow_guide_thumb.png)

[Arrow guide](https://matplotlib.org/stable/gallery/shapes_and_collections/arrow_guide.html)

Arrow guide

![](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_thumb.png)

[Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)

Reference for Matplotlib artists

![](https://matplotlib.org/stable/_images/sphx_glr_compound_path_thumb.png)

[Compound path](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html)

Compound path

![](https://matplotlib.org/stable/_images/sphx_glr_dolphin_thumb.png)

[Dolphins](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html)

Dolphins

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_arrow_thumb.png)

[Ellipse with orientation arrow demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html)

Ellipse with orientation arrow demo

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_thumb.png)

[Ellipse Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html)

Ellipse Demo

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

![](https://matplotlib.org/stable/_images/sphx_glr_hatch_demo_thumb.png)

[Hatch demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html)

Hatch demo

![](https://matplotlib.org/stable/_images/sphx_glr_hatch_style_reference_thumb.png)

[Hatch style reference](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html)

Hatch style reference

![](https://matplotlib.org/stable/_images/sphx_glr_hatchcolor_demo_thumb.png)

[Hatchcolor Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatchcolor_demo.html)

Hatchcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_patch_collection_thumb.png)

[Circles, Wedges and Polygons](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html)

Circles, Wedges and Polygons

![](https://matplotlib.org/stable/_images/sphx_glr_path_patch_thumb.png)

[PathPatch object](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html)

PathPatch object

![](https://matplotlib.org/stable/_images/sphx_glr_quad_bezier_thumb.png)

[Bezier curve](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html)

Bezier curve

![](https://matplotlib.org/stable/_images/sphx_glr_named_colors_thumb.png)

[List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)

List of named colors

![](https://matplotlib.org/stable/_images/sphx_glr_ggplot_thumb.png)

[ggplot style sheet](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html)

ggplot style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_grayscale_thumb.png)

[Grayscale style sheet](https://matplotlib.org/stable/gallery/style_sheets/grayscale.html)

Grayscale style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_petroff10_thumb.png)

[Petroff style sheets](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html)

Petroff style sheets

![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_thumb.png)

[Style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

Style sheets reference

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_thumb.png)

[Inset locator demo](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html)

Inset locator demo

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

![](https://matplotlib.org/stable/_images/sphx_glr_menu_thumb.png)

[Menu](https://matplotlib.org/stable/gallery/widgets/menu.html)

Menu

![](https://matplotlib.org/stable/_images/sphx_glr_looking_glass_thumb.png)

[Looking glass](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html)

Looking glass

![](https://matplotlib.org/stable/_images/sphx_glr_path_editor_thumb.png)

[Path editor](https://matplotlib.org/stable/gallery/event_handling/path_editor.html)

Path editor

![](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_thumb.png)

[Pick event demo](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html)

Pick event demo

![](https://matplotlib.org/stable/_images/sphx_glr_poly_editor_thumb.png)

[Polygon editor](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html)

Polygon editor

![](https://matplotlib.org/stable/_images/sphx_glr_trifinder_event_demo_thumb.png)

[Trifinder Event Demo](https://matplotlib.org/stable/gallery/event_handling/trifinder_event_demo.html)

Trifinder Event Demo

![](https://matplotlib.org/stable/_images/sphx_glr_viewlims_thumb.png)

[Viewlims](https://matplotlib.org/stable/gallery/event_handling/viewlims.html)

Viewlims

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_with_units_thumb.png)

[Ellipse with units](https://matplotlib.org/stable/gallery/units/ellipse_with_units.html)

Ellipse with units

![](https://matplotlib.org/stable/_images/sphx_glr_anchored_artists_thumb.png)

[Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)

Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_bbox_intersect_thumb.png)

[Identify whether artists intersect](https://matplotlib.org/stable/gallery/misc/bbox_intersect.html)

Identify whether artists intersect

![](https://matplotlib.org/stable/_images/sphx_glr_custom_projection_thumb.png)

[Custom projection](https://matplotlib.org/stable/gallery/misc/custom_projection.html)

Custom projection

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_path_thumb.png)

[Building histograms using Rectangles and PolyCollections](https://matplotlib.org/stable/gallery/misc/histogram_path.html)

Building histograms using Rectangles and PolyCollections

![](https://matplotlib.org/stable/_images/sphx_glr_logos2_thumb.png)

[Matplotlib logo](https://matplotlib.org/stable/gallery/misc/logos2.html)

Matplotlib logo

![](https://matplotlib.org/stable/_images/sphx_glr_packed_bubbles_thumb.png)

[Packed-bubble chart](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html)

Packed-bubble chart

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_pie_thumb.png)

[SVG filter pie](https://matplotlib.org/stable/gallery/misc/svg_filter_pie.html)

SVG filter pie

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_firefox_thumb.png)

[Firefox](https://matplotlib.org/stable/gallery/showcase/firefox.html)

Firefox

![](https://matplotlib.org/stable/_images/sphx_glr_integral_thumb.png)

[Integral as the area under a curve](https://matplotlib.org/stable/gallery/showcase/integral.html)

Integral as the area under a curve

![](https://matplotlib.org/stable/_images/sphx_glr_hinton_demo_thumb.png)

[Hinton diagrams](https://matplotlib.org/stable/gallery/specialty_plots/hinton_demo.html)

Hinton diagrams

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_radar_chart_thumb.png)

[Radar chart (aka spider or star chart)](https://matplotlib.org/stable/gallery/specialty_plots/radar_chart.html)

Radar chart (aka spider or star chart)

![](https://matplotlib.org/stable/_images/sphx_glr_skewt_thumb.png)

[SkewT-logP diagram: using transforms and custom projections](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

SkewT-logP diagram: using transforms and custom projections

![](https://matplotlib.org/stable/_images/sphx_glr_paths_thumb.png)

[Path Tutorial](https://matplotlib.org/stable/users/explain/artists/paths.html)

Path Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_thumb.png)

[Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)

Legend guide

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_text_props_thumb.png)

[Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html)

Text properties and layout

On this page