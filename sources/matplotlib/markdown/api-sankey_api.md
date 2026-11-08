[Skip to main content](https://matplotlib.org/stable/api/sankey_api.html#main-content)

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
    

`matplotlib.sankey`[#](https://matplotlib.org/stable/api/sankey_api.html#module-matplotlib.sankey "Link to this heading")

==========================================================================================================================

Module for creating Sankey diagrams using Matplotlib.

class matplotlib.sankey.Sankey(_ax\=None_, _scale\=1.0_, _unit\=''_, _format\='%G'_, _gap\=0.25_, _radius\=0.1_, _shoulder\=0.03_, _offset\=0.15_, _head\_angle\=100_, _margin\=0.4_, _tolerance\=1e-06_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sankey.py#L30-L814)
[#](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Sankey diagram.

> Sankey diagrams are a specific type of flow diagram, in which the width of the arrows is shown proportionally to the flow quantity. They are typically used to visualize energy or material or cost transfers between processes. [Wikipedia (6/1/2011)](https://en.wikipedia.org/wiki/Sankey_diagram)

Create a new Sankey instance.

The optional arguments listed below are applied to all subdiagrams so that there is consistent alignment and formatting.

In order to draw a complex Sankey diagram, create an instance of [`Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 by calling it without any kwargs:

sankey \= Sankey()

Then add simple Sankey sub-diagrams:

sankey.add() \# 1
sankey.add() \# 2
#...
sankey.add() \# n

Finally, create the full diagram:

sankey.finish()

Or, instead, simply daisy-chain those calls:

Sankey().add().add...  .add().finish()

Other Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Axes onto which the data should be plotted. If _ax_ isn't provided, new Axes will be created.

**scale**float

Scaling factor for the flows. _scale_ sizes the width of the paths in order to maintain proper layout. The same scale is applied to all subdiagrams. The value should be chosen such that the product of the scale and the sum of the inputs is approximately 1.0 (and the product of the scale and the sum of the outputs is approximately -1.0).

**unit**str

The physical unit associated with the flow quantities. If _unit_ is None, then none of the quantities are labeled.

**format**str or callable

A Python number formatting string or callable used to label the flows with their quantities (i.e., a number times a unit, where the unit is given). If a format string is given, the label will be `format % quantity`. If a callable is given, it will be called with `quantity` as an argument.

**gap**float

Space between paths that break in/break away to/from the top or bottom.

**radius**float

Inner radius of the vertical paths.

**shoulder**float

Size of the shoulders of output arrows.

**offset**float

Text offset (from the dip or tip of the arrow).

**head\_angle**float

Angle, in degrees, of the arrow heads (and negative of the angle of the tails).

**margin**float

Minimum space between Sankey outlines and the edge of the plot area.

**tolerance**float

Acceptable maximum of the magnitude of the sum of flows. The magnitude of the sum of connected flows cannot be greater than _tolerance_.

**\*\*kwargs**

Any additional keyword arguments will be passed to [`add`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")
, which will create the first subdiagram.

See also

[`Sankey.add`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")

[`Sankey.finish`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/6ebc861042ece642ba51273d41af4e25/sankey_basics.py)
)

[![](https://matplotlib.org/stable/_images/api-sankey_basics_00_00.2x.png)](https://matplotlib.org/stable/_images/api-sankey_basics_00_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/4c46d2fc3b23393f779e4c8566c6b441/sankey_basics_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/be66781f00169a6fa482b64fb39597b9/sankey_basics_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-sankey_basics_00_01.2x.png)](https://matplotlib.org/stable/_images/api-sankey_basics_00_01.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/ae00d44d3fc2c265545891aea3779945/sankey_basics_00_01.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f7d5233fc27195a60f0089e1c27fcc95/sankey_basics_00_01.png)
)

[![](https://matplotlib.org/stable/_images/api-sankey_basics_00_02.2x.png)](https://matplotlib.org/stable/_images/api-sankey_basics_00_02.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/61a4f4c9482764065b274f8fdcdb1da2/sankey_basics_00_02.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ee9ff2d7b4cb13f2c00df80842cbce0d/sankey_basics_00_02.png)
)

add(_patchlabel\=''_, _flows\=None_, _orientations\=None_, _labels\=''_, _trunklength\=1.0_, _pathlengths\=0.25_, _prior\=None_, _connect\=(0, 0)_, _rotation\=0_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sankey.py#L350-L776)
[#](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "Link to this definition")

Add a simple Sankey diagram with flows at the same hierarchical level.

Parameters:

**patchlabel**str

Label to be placed at the center of the diagram. Note that _label_ (not _patchlabel_) can be passed as keyword argument to create an entry in the legend.

**flows**list of float

Array of flow values. By convention, inputs are positive and outputs are negative.

Flows are placed along the top of the diagram from the inside out in order of their index within _flows_. They are placed along the sides of the diagram from the top down and along the bottom from the outside in.

If the sum of the inputs and outputs is nonzero, the discrepancy will appear as a cubic Bézier curve along the top and bottom edges of the trunk.

**orientations**list of {-1, 0, 1}

List of orientations of the flows (or a single orientation to be used for all flows). Valid values are 0 (inputs from the left, outputs to the right), 1 (from and to the top) or -1 (from and to the bottom).

**labels**list of (str or None)

List of labels for the flows (or a single label to be used for all flows). Each label may be _None_ (no label), or a labeling string. If an entry is a (possibly empty) string, then the quantity for the corresponding flow will be shown below the string. However, if the _unit_ of the main diagram is None, then quantities are never shown, regardless of the value of this argument.

**trunklength**float

Length between the bases of the input and output groups (in data-space units).

**pathlengths**list of float

List of lengths of the vertical arrows before break-in or after break-away. If a single value is given, then it will be applied to the first (inside) paths on the top and bottom, and the length of all other arrows will be justified accordingly. The _pathlengths_ are not applied to the horizontal inputs and outputs.

**prior**int

Index of the prior diagram to which this diagram should be connected.

**connect**(int, int)

A (prior, this) tuple indexing the flow of the prior diagram and the flow of this diagram which should be connected. If this is the first diagram or _prior_ is _None_, _connect_ will be ignored.

**rotation**float

Angle of rotation of the diagram in degrees. The interpretation of the _orientations_ argument will be rotated accordingly (e.g., if _rotation_ == 90, an _orientations_ entry of 1 means to/from the left). _rotation_ is ignored if this diagram is connected to an existing one (using _prior_ and _connect_).

Returns:

Sankey

The current [`Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 instance.

Other Parameters:

**\*\*kwargs**

Additional keyword arguments set [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 properties, listed below. For example, one may want to use `fill=False` or `label="A legend entry"`.

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | unknown |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased "matplotlib.patches.Patch.set_antialiased") | bool or None |
> | [`capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle "matplotlib.patches.Patch.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor "matplotlib.patches.Patch.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`edgegapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgegapcolor "matplotlib.patches.Patch.set_edgegapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill "matplotlib.patches.Patch.set_fill") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch_linewidth "matplotlib.patches.Patch.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatchcolor "matplotlib.patches.Patch.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' or None |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle "matplotlib.patches.Patch.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle "matplotlib.patches.Patch.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) |
> | [`linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth") | float or None |
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

See also

[`Sankey.finish`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "matplotlib.sankey.Sankey.finish")

finish()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/sankey.py#L778-L814)
[#](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.finish "Link to this definition")

Adjust the Axes and return a list of information about the Sankey subdiagram(s).

Returns a list of subdiagrams with the following fields:

| Field | Description |
| --- | --- |
| _patch_ | Sankey outline (a [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")<br>). |
| _flows_ | Flow values (positive for input, negative for output). |
| _angles_ | List of angles of the arrows \[deg/90\]. For example, if the diagram has not been rotated, an input to the top side has an angle of 3 (DOWN), and an output from the top side has an angle of 1 (UP). If a flow has been skipped (because its magnitude is less than _tolerance_), then its angle will be _None_. |
| _tips_ | (N, 2)-array of the (x, y) positions of the tips (or "dips") of the flow paths. If the magnitude of a flow is less the _tolerance_ of this [`Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")<br> instance, the flow is skipped and its tip will be at the center of the diagram. |
| _text_ | [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> instance for the diagram label. |
| _texts_ | List of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> instances for the flow labels. |

See also

[`Sankey.add`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey.add "matplotlib.sankey.Sankey.add")

On this page