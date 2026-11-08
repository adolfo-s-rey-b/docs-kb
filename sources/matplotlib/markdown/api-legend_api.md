[Skip to main content](https://matplotlib.org/stable/api/legend_api.html#main-content)

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
    

`matplotlib.legend`[#](https://matplotlib.org/stable/api/legend_api.html#module-matplotlib.legend "Link to this heading")

==========================================================================================================================

The legend module defines the Legend class, which is responsible for drawing legends associated with Axes and/or figures.

Important

It is unlikely that you would ever create a Legend instance manually. Most users would normally create a legend via the [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 function. For more details on legends there is also a [legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
.

The [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 class is a container of legend handles and legend texts.

The legend handler map specifies how to create legend handles from artists (lines, patches, etc.) in the Axes or figures. Default legend handlers are defined in the [`legend_handler`](https://matplotlib.org/stable/api/legend_handler_api.html#module-matplotlib.legend_handler "matplotlib.legend_handler")
 module. While not all artist types are covered by the default legend handlers, custom legend handlers can be defined to support arbitrary objects.

See the :ref\`<legend\_guide>\` for more information.

class matplotlib.legend.DraggableLegend(_legend_, _use\_blit\=False_, _update\='loc'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L54-L95)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.DraggableLegend "Link to this definition")

Bases: [`DraggableOffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableOffsetBox "matplotlib.offsetbox.DraggableOffsetBox")

Wrapper around a [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 to support mouse dragging.

Parameters:

**legend**[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

The [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 instance to wrap.

**use\_blit**bool, optional

Use blitting for faster image composition. For details see [FuncAnimation](https://matplotlib.org/stable/api/animation_api.html#func-animation)
.

**update**{'loc', 'bbox'}, optional

If "loc", update the _loc_ parameter of the legend upon finalizing. If "bbox", update the _bbox\_to\_anchor_ parameter.

finalize\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L77-L81)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.DraggableLegend.finalize_offset "Link to this definition")

class matplotlib.legend.Legend(_parent_, _handles_, _labels_, _\*_, _loc\=None_, _numpoints\=None_, _markerscale\=None_, _markerfirst\=True_, _reverse\=False_, _scatterpoints\=None_, _scatteryoffsets\=None_, _prop\=None_, _fontsize\=None_, _labelcolor\=None_, _borderpad\=None_, _labelspacing\=None_, _handlelength\=None_, _handleheight\=None_, _handletextpad\=None_, _borderaxespad\=None_, _columnspacing\=None_, _ncols\=1_, _mode\=None_, _fancybox\=None_, _shadow\=None_, _title\=None_, _title\_fontsize\=None_, _framealpha\=None_, _edgecolor\=None_, _facecolor\=None_, _linewidth\=None_, _bbox\_to\_anchor\=None_, _bbox\_transform\=None_, _frameon\=None_, _handler\_map\=None_, _title\_fontproperties\=None_, _alignment\='center'_, _ncol\=1_, _draggable\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L362-L1257)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

Place a legend on the figure/axes.

Parameters:

**parent**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The artist that contains the legend.

**handles**list of ([`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or tuple of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
)

A list of Artists (lines, patches) to be added to the legend.

**labels**list of str

A list of labels to show next to the artists. The length of handles and labels should be the same. If they are not, they are truncated to the length of the shorter list.

Attributes:

**legend\_handles**

List of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 objects added as legend entries.

Added in version 3.7.

Other Parameters:

**loc**str or pair of floats, default: `[rcParams["legend.loc"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.loc#rcparam-legend-loc) ` (default: `'best'`) for Axes, 'upper right' for Figure

The location of the legend.

The string locations place the legend at the corresponding position within the bounding box, which by default is the full axes/figure area. The bounding box can be changed via _bbox\_to\_anchor_.

The positions are visualized below:

+--------------+--------------+---------------+
| 'upper left' |'upper center'| 'upper right' |
+--------------+--------------+---------------+
|'center left' |   'center'   |'center right' |
+--------------+--------------+---------------+
| 'lower left' |'lower center'| 'lower right' |
+--------------+--------------+---------------+

The string `'best'` places the legend at the location, among the nine locations defined so far, with the minimum overlap with other drawn artists. This currently takes into account most, but not all, artists added to the Axes via plotting functions. In particular it does not consider inset axes, titles, or axis labels.

The computation of the best position can be expensive for plots with large amounts of data. If speed becomes a concern, you may may benefit from providing a specific location.

The location can also be a 2-tuple giving the coordinates of the lower-left corner of the legend in axes/figure coordinates (in which case _bbox\_to\_anchor_ will be ignored).

For back-compatibility, `'center right'` (but no other location) can also be spelled `'right'`, and each "string" location can also be given as a numeric value:

| Location String | Location Code |
| --- | --- |
| 'best' (Axes only) | 0   |
| 'upper right' | 1   |
| 'upper left' | 2   |
| 'lower left' | 3   |
| 'lower right' | 4   |
| 'right' | 5   |
| 'center left' | 6   |
| 'center right' | 7   |
| 'lower center' | 8   |
| 'upper center' | 9   |
| 'center' | 10  |

If a figure is using the constrained layout manager, the string codes of the _loc_ keyword argument can get better layout behaviour using the prefix 'outside'. There is ambiguity at the corners, so 'outside upper right' will make space for the legend above the rest of the axes in the layout, and 'outside right upper' will make space on the right side of the layout. In addition to the values of _loc_ listed above, we have 'outside right upper', 'outside right lower', 'outside left upper', and 'outside left lower'. See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for more details.

**bbox\_to\_anchor**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
, 2-tuple, or 4-tuple of floats

Box that is used to position the legend in conjunction with _loc_. This is an advanced option for free placement of the legend. For most use cases, _loc_ alone is sufficient.

Defaults to `axes.bbox` (if called as a method to [`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
) or `figure.bbox` (if `figure.legend`).

Bbox coordinates are interpreted in the coordinate system given by _bbox\_transform_, with the default transform Axes or Figure coordinates, depending on which `legend` is called.

If a 4-tuple or [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
 is given, then it specifies the bbox `(x, y, width, height)` that the legend is placed in. To put the legend in the best location in the bottom right quadrant of the Axes (or figure):

loc\='best', bbox\_to\_anchor\=(0.5, 0., 0.5, 0.5)

A 2-tuple `(x, y)` places the corner of the legend specified by _loc_ at x, y. For example, to put the legend's upper right-hand corner in the center of the Axes (or figure) the following keywords can be used:

loc\='upper right', bbox\_to\_anchor\=(0.5, 0.5)

For more details on legend positioning, see the [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
.

**ncols**int, default: 1

The number of columns that the legend has.

For backward compatibility, the spelling _ncol_ is also supported but it is discouraged. If both are given, _ncols_ takes precedence.

**prop**None or [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 or dict

The font properties of the legend. If None (default), the current [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 will be used.

**fontsize**int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}

The font size of the legend. If the value is numeric the size will be the absolute font size in points. String values are relative to the current default font size. This argument is only used if _prop_ is not specified.

**labelcolor**str or list, default: `[rcParams["legend.labelcolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelcolor#rcparam-legend-labelcolor) ` (default: `'None'`)

The color of the text in the legend. Either a valid color string (for example, 'red'), or a list of color strings. The labelcolor can also be made to match the color of the line or marker using 'linecolor', 'markerfacecolor' (or 'mfc'), or 'markeredgecolor' (or 'mec').

Labelcolor can be set globally using `[rcParams["legend.labelcolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelcolor#rcparam-legend-labelcolor) ` (default: `'None'`). If None, use `[rcParams["text.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.color#rcparam-text-color) ` (default: `'black'`).

**numpoints**int, default: `[rcParams["legend.numpoints"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.numpoints#rcparam-legend-numpoints) ` (default: `1`)

The number of marker points in the legend when creating a legend entry for a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 (line).

**scatterpoints**int, default: `[rcParams["legend.scatterpoints"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.scatterpoints#rcparam-legend-scatterpoints) ` (default: `1`)

The number of marker points in the legend when creating a legend entry for a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 (scatter plot).

**scatteryoffsets**iterable of floats, default: `[0.375, 0.5, 0.3125]`

The vertical offset (relative to the font size) for the markers created for a scatter plot legend entry. 0.0 is at the base the legend text, and 1.0 is at the top. To draw all markers at the same height, set to `[0.5]`.

**markerscale**float, default: `[rcParams["legend.markerscale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.markerscale#rcparam-legend-markerscale) ` (default: `1.0`)

The relative size of legend markers compared to the originally drawn ones.

**markerfirst**bool, default: True

If _True_, legend marker is placed to the left of the legend label. If _False_, legend marker is placed to the right of the legend label.

**reverse**bool, default: False

If _True_, the legend labels are displayed in reverse order from the input. If _False_, the legend labels are displayed in the same order as the input.

Added in version 3.7.

**frameon**bool, default: `[rcParams["legend.frameon"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.frameon#rcparam-legend-frameon) ` (default: `True`)

Whether the legend should be drawn on a patch (frame).

**fancybox**bool, default: `[rcParams["legend.fancybox"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.fancybox#rcparam-legend-fancybox) ` (default: `True`)

Whether round edges should be enabled around the [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 which makes up the legend's background.

**shadow**None, bool or dict, default: `[rcParams["legend.shadow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.shadow#rcparam-legend-shadow) ` (default: `False`)

Whether to draw a shadow behind the legend. The shadow can be configured using [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 keywords. Customization via `[rcParams["legend.shadow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.shadow#rcparam-legend-shadow) ` (default: `False`) is currently not supported.

**framealpha**float, default: `[rcParams["legend.framealpha"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.framealpha#rcparam-legend-framealpha) ` (default: `0.8`)

The alpha transparency of the legend's background. If _shadow_ is activated and _framealpha_ is `None`, the default value is ignored.

**facecolor**"inherit" or color, default: `[rcParams["legend.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.facecolor#rcparam-legend-facecolor) ` (default: `'inherit'`)

The legend's background color. If `"inherit"`, use `[rcParams["axes.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.facecolor#rcparam-axes-facecolor) ` (default: `'white'`).

**edgecolor**"inherit" or color, default: `[rcParams["legend.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.edgecolor#rcparam-legend-edgecolor) ` (default: `'0.8'`)

The legend's background patch edge color. If `"inherit"`, use `[rcParams["axes.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.edgecolor#rcparam-axes-edgecolor) ` (default: `'black'`).

**linewidth**float or None, default: `[rcParams["legend.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.linewidth#rcparam-legend-linewidth) ` (default: `None`)

The legend's background patch edge linewidth. If `None`, use `[rcParams["patch.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.linewidth#rcparam-patch-linewidth) ` (default: `1.0`).

Added in version 3.11.

**mode**{"expand", None}

If _mode_ is set to `"expand"` the legend will be horizontally expanded to fill the Axes area (or _bbox\_to\_anchor_ if defines the legend's size).

**bbox\_transform**None or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform for the bounding box (_bbox\_to\_anchor_). For a value of `None` (default) the Axes' `matplotlib.axes.Axes.transAxes` transform will be used.

**title**str or None

The legend's title. Default is no title (`None`).

**title\_fontproperties**None or [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 or dict

The font properties of the legend's title. If None (default), the _title\_fontsize_ argument will be used if present; if _title\_fontsize_ is also None, the current `[rcParams["legend.title_fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.title_fontsize#rcparam-legend-title-fontsize) ` (default: `None`) will be used.

**title\_fontsize**int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}, default: `[rcParams["legend.title_fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.title_fontsize#rcparam-legend-title-fontsize) ` (default: `None`)

The font size of the legend's title. Note: This cannot be combined with _title\_fontproperties_. If you want to set the fontsize alongside other font properties, use the _size_ parameter in _title\_fontproperties_.

**alignment**{'center', 'left', 'right'}, default: 'center'

The alignment of the legend title and the box of entries. The entries are aligned as a single block, so that markers always lined up.

**borderpad**float, default: `[rcParams["legend.borderpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.borderpad#rcparam-legend-borderpad) ` (default: `0.4`)

The fractional whitespace inside the legend border, in font-size units.

**labelspacing**float, default: `[rcParams["legend.labelspacing"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelspacing#rcparam-legend-labelspacing) ` (default: `0.5`)

The vertical space between the legend entries, in font-size units.

**handlelength**float, default: `[rcParams["legend.handlelength"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.handlelength#rcparam-legend-handlelength) ` (default: `2.0`)

The length of the legend handles, in font-size units.

**handleheight**float, default: `[rcParams["legend.handleheight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.handleheight#rcparam-legend-handleheight) ` (default: `0.7`)

The height of the legend handles, in font-size units.

**handletextpad**float, default: `[rcParams["legend.handletextpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.handletextpad#rcparam-legend-handletextpad) ` (default: `0.8`)

The pad between the legend handle and text, in font-size units.

**borderaxespad**float, default: `[rcParams["legend.borderaxespad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.borderaxespad#rcparam-legend-borderaxespad) ` (default: `0.5`)

The pad between the Axes and legend border, in font-size units.

**columnspacing**float, default: `[rcParams["legend.columnspacing"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.columnspacing#rcparam-legend-columnspacing) ` (default: `2.0`)

The spacing between columns, in font-size units.

**handler\_map**dict or None

The custom dictionary mapping instances or types to a legend handler. This _handler\_map_ updates the default handler map found at [`matplotlib.legend.Legend.get_legend_handler_map`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_legend_handler_map "matplotlib.legend.Legend.get_legend_handler_map")
.

**draggable**bool, default: False

Whether the legend can be dragged with the mouse.

codes \= {'best': 0, 'center': 10, 'center left': 6, 'center right': 7, 'lower center': 8, 'lower left': 3, 'lower right': 4, 'right': 5, 'upper center': 9, 'upper left': 2, 'upper right': 1}[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.codes "Link to this definition")

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1218-L1219)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.contains "Link to this definition")

Test whether the artist contains the mouse event.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

An artist-specific dictionary of details of the event context, such as which points are contained in the pick radius. See the individual Artist subclasses for details.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L765-L797)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

draw\_frame(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1097-L1106)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.draw_frame "Link to this definition")

Set whether the legend box patch is drawn.

Parameters:

**b**bool

get\_alignment()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1046-L1048)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_alignment "Link to this definition")

Get the alignment value of the legend box

get\_bbox\_to\_anchor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1110-L1115)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_bbox_to_anchor "Link to this definition")

Return the bbox that the legend will be anchored to.

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1008-L1010)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_children "Link to this definition")

Return a list of the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s of this [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
.

classmethod get\_default\_handler\_map()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L822-L825)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_default_handler_map "Link to this definition")

Return the global default handler map, shared by all legends.

get\_draggable()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1255-L1257)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_draggable "Link to this definition")

Return `True` if the legend is draggable, `False` otherwise.

get\_frame()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1012-L1014)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_frame "Link to this definition")

Return the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 used to frame the legend.

get\_frame\_on()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1093-L1095)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_frame_on "Link to this definition")

Get whether the legend box patch is drawn.

static get\_legend\_handler(_legend\_handler\_map_, _orig\_handle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L843-L867)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_legend_handler "Link to this definition")

Return a legend handler from _legend\_handler\_map_ that corresponds to _orig\_handler_.

_legend\_handler\_map_ should be a dictionary object (that is returned by the get\_legend\_handler\_map method).

It first checks if the _orig\_handle_ itself is a key in the _legend\_handler\_map_ and return the associated value. Otherwise, it checks for each of the classes in its method-resolution-order. If no matching key is found, it returns `None`.

get\_legend\_handler\_map()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L837-L841)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_legend_handler_map "Link to this definition")

Return this legend instance's handler map.

get\_lines()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1016-L1018)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_lines "Link to this definition")

Return the list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
s in the legend.

get\_patches()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1020-L1024)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_patches "Link to this definition")

Return the list of [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
s in the legend.

get\_texts()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1026-L1028)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_texts "Link to this definition")

Return the list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
s in the legend.

get\_tightbbox(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1089-L1091)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_tightbbox "Link to this definition")

Get the artist's bounding box in display space, taking clipping into account.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

Returns:

[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or None

The enclosing bounding box (in figure pixel coordinates), or None if clipping results in no intersection.

See also

[`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")

Get the artist bounding box, ignoring clipping.

get\_title()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1079-L1081)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_title "Link to this definition")

Return the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance for the legend title.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1083-L1087)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_window_extent "Link to this definition")

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

set(_\*_, _agg\_filter\=<UNSET>_, _alignment\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _bbox\_to\_anchor\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _draggable\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _loc\=<UNSET>_, _mouseover\=<UNSET>_, _ncols\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set "Link to this definition")

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
> | [`alignment`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_alignment "matplotlib.legend.Legend.set_alignment") | {'center', 'left', 'right'}. |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`bbox_to_anchor`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_bbox_to_anchor "matplotlib.legend.Legend.set_bbox_to_anchor") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or tuple |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`draggable`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_draggable "matplotlib.legend.Legend.set_draggable") | bool |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`frame_on`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_frame_on "matplotlib.legend.Legend.set_frame_on") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`loc`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_loc "matplotlib.legend.Legend.set_loc") | str or pair of floats, default: `[rcParams["legend.loc"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.loc#rcparam-legend-loc) ` (default: `'best'`) for Axes, 'upper right' for Figure |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`ncols`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_ncols "matplotlib.legend.Legend.set_ncols") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`title`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_title "matplotlib.legend.Legend.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_alignment(_alignment_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1030-L1044)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_alignment "Link to this definition")

Set the alignment of the legend title and the box of entries.

The entries are aligned as a single block, so that markers always lined up.

Parameters:

**alignment**{'center', 'left', 'right'}.

set\_bbox\_to\_anchor(_bbox_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1117-L1158)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_bbox_to_anchor "Link to this definition")

Set the bbox that the legend will be anchored to.

Parameters:

**bbox**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
 or tuple

The bounding box can be specified in the following ways:

*   A [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
     instance
    
*   A tuple of `(left, bottom, width, height)` in the given transform (normalized axes coordinate if None)
    
*   A tuple of `(left, bottom)` where the width and height will be assumed to be zero.
    
*   _None_, to remove the bbox anchoring, and use the parent bbox.
    

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

A transform to apply to the bounding box. If not specified, this will use a transform to the bounding box of the parent.

classmethod set\_default\_handler\_map(_handler\_map_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L827-L830)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_default_handler_map "Link to this definition")

Set the global default handler map, shared by all legends.

set\_draggable(_state_, _use\_blit\=False_, _update\='loc'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1221-L1253)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_draggable "Link to this definition")

Enable or disable mouse dragging support of the legend.

Parameters:

**state**bool

Whether mouse dragging is enabled.

**use\_blit**bool, optional

Use blitting for faster image composition. For details see [FuncAnimation](https://matplotlib.org/stable/api/animation_api.html#func-animation)
.

**update**{'loc', 'bbox'}, optional

The legend parameter to be changed when dragged:

*   'loc': update the _loc_ parameter of the legend
    
*   'bbox': update the _bbox\_to\_anchor_ parameter of the legend
    

Returns:

[`DraggableLegend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.DraggableLegend "matplotlib.legend.DraggableLegend")
 or _None_

If _state_ is `True` this returns the [`DraggableLegend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.DraggableLegend "matplotlib.legend.DraggableLegend")
 helper instance. Otherwise this returns _None_.

set\_frame\_on(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1097-L1106)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_frame_on "Link to this definition")

Set whether the legend box patch is drawn.

Parameters:

**b**bool

set\_loc(_loc\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L663-L728)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_loc "Link to this definition")

Set the location of the legend.

Added in version 3.8.

Parameters:

**loc**str or pair of floats, default: `[rcParams["legend.loc"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.loc#rcparam-legend-loc) ` (default: `'best'`) for Axes, 'upper right' for Figure

The location of the legend.

The string locations place the legend at the corresponding position within the bounding box, which by default is the full axes/figure area. The bounding box can be changed via _bbox\_to\_anchor_.

The positions are visualized below:

+--------------+--------------+---------------+
| 'upper left' |'upper center'| 'upper right' |
+--------------+--------------+---------------+
|'center left' |   'center'   |'center right' |
+--------------+--------------+---------------+
| 'lower left' |'lower center'| 'lower right' |
+--------------+--------------+---------------+

The string `'best'` places the legend at the location, among the nine locations defined so far, with the minimum overlap with other drawn artists. This currently takes into account most, but not all, artists added to the Axes via plotting functions. In particular it does not consider inset axes, titles, or axis labels.

The computation of the best position can be expensive for plots with large amounts of data. If speed becomes a concern, you may may benefit from providing a specific location.

The location can also be a 2-tuple giving the coordinates of the lower-left corner of the legend in axes/figure coordinates (in which case _bbox\_to\_anchor_ will be ignored).

For back-compatibility, `'center right'` (but no other location) can also be spelled `'right'`, and each "string" location can also be given as a numeric value:

| Location String | Location Code |
| --- | --- |
| 'best' (Axes only) | 0   |
| 'upper right' | 1   |
| 'upper left' | 2   |
| 'lower left' | 3   |
| 'lower right' | 4   |
| 'right' | 5   |
| 'center left' | 6   |
| 'center right' | 7   |
| 'lower center' | 8   |
| 'upper center' | 9   |
| 'center' | 10  |

If a figure is using the constrained layout manager, the string codes of the _loc_ keyword argument can get better layout behaviour using the prefix 'outside'. There is ambiguity at the corners, so 'outside upper right' will make space for the legend above the rest of the axes in the layout, and 'outside right upper' will make space on the right side of the layout. In addition to the values of _loc_ listed above, we have 'outside right upper', 'outside right lower', 'outside left upper', and 'outside left lower'. See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for more details.

set\_ncols(_ncols_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L739-L741)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_ncols "Link to this definition")

Set the number of columns.

set\_title(_title_, _prop\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L1050-L1077)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_title "Link to this definition")

Set legend title and title style.

Parameters:

**title**str

The legend title.

**prop**[`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

The font properties of the legend title. If a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
, it is interpreted as a fontconfig pattern parsed by [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
. If a [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")
, it is interpreted as the absolute path to a font file.

classmethod update\_default\_handler\_map(_handler\_map_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/legend.py#L832-L835)
[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.update_default_handler_map "Link to this definition")

Update the global default handler map, shared by all legends.

zorder \= 5[#](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.zorder "Link to this definition")

On this page