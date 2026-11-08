[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html#main-content)

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
    

matplotlib.pyplot.figlegend[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib-pyplot-figlegend "Link to this heading")

==============================================================================================================================================================

matplotlib.pyplot.figlegend(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1354-L1355)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend "Link to this definition")

Place a legend on the figure.

Call signatures:

figlegend()
figlegend(handles, labels)
figlegend(handles\=handles)
figlegend(labels)

The call signatures correspond to the following different ways to use this method:

**1\. Automatic detection of elements to be shown in the legend**

The elements to be added to the legend are automatically determined, when you do not pass in any extra arguments.

In this case, the labels are taken from the artist. You can specify them either at artist creation or by calling the [`set_label()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label")
 method on the artist:

plt.plot(\[1, 2, 3\], label\='Inline label')
plt.figlegend()

or:

line, \= plt.plot(\[1, 2, 3\])
line.set\_label('Label via method')
plt.figlegend()

Specific lines can be excluded from the automatic legend element selection by defining a label starting with an underscore. This is default for all artists, so calling [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 without any arguments and without setting the labels manually will result in no legend being drawn.

**2\. Explicitly listing the artists and labels in the legend**

For full control of which artists have a legend entry, it is possible to pass an iterable of legend artists followed by an iterable of legend labels respectively:

plt.figlegend(\[line1, line2, line3\], \['label1', 'label2', 'label3'\])

**3\. Explicitly listing the artists in the legend**

This is similar to 2, but the labels are taken from the artists' label properties. Example:

line1, \= ax1.plot(\[1, 2, 3\], label\='label1')
line2, \= ax2.plot(\[1, 2, 3\], label\='label2')
plt.figlegend(handles\=\[line1, line2\])

**4\. Labeling existing plot elements**

Discouraged

This call signature is discouraged, because the relation between plot elements and labels is only implicit by their order and can easily be mixed up.

To make a legend for all artists on all Axes, call this function with an iterable of strings, one for each legend item. For example:

fig, (ax1, ax2) \= plt.subplots(1, 2)
ax1.plot(\[1, 3, 5\], color\='blue')
ax2.plot(\[2, 4, 6\], color\='red')
plt.figlegend(\['the blues', 'the reds'\])

Parameters:

**handles**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, optional

A list of Artists (lines, patches) to be added to the legend. Use this together with _labels_, if you need full control on what is shown in the legend and the automatic mechanism described above is not sufficient.

The length of handles and labels should be the same in this case. If they are not, they are truncated to the smaller length.

**labels**list of str, optional

A list of labels to show next to the artists. Use this together with _handles_, if you need full control on what is shown in the legend and the automatic mechanism described above is not sufficient.

Returns:

[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

Other Parameters:

**loc**str or pair of floats, default: 'upper right'

The location of the legend.

The string locations place the legend at the corresponding position within the bounding box, which by default is the full figure area. The bounding box can be changed via _bbox\_to\_anchor_.

The positions are visualized below:

+--------------+--------------+---------------+
| 'upper left' |'upper center'| 'upper right' |
+--------------+--------------+---------------+
|'center left' |   'center'   |'center right' |
+--------------+--------------+---------------+
| 'lower left' |'lower center'| 'lower right' |
+--------------+--------------+---------------+

The location can also be a 2-tuple giving the coordinates of the lower-left corner of the legend in figure coordinates (in which case _bbox\_to\_anchor_ will be ignored).

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

See also

[`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")

Notes

Some artists are not supported by this function. See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for details.

On this page