[Skip to main content](https://matplotlib.org/stable/api/contour_api.html#main-content)

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
    

`matplotlib.contour`[#](https://matplotlib.org/stable/api/contour_api.html#module-matplotlib.contour "Link to this heading")

=============================================================================================================================

Classes to support contour plotting and labelling for the Axes class.

class matplotlib.contour.ContourLabeler[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L59-L530)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Mixin to provide labelling capability to [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
.

add\_label(_x_, _y_, _rotation_, _lev_, _cvalue_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L423-L443)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.add_label "Link to this definition")

Add a contour label, respecting whether _use\_clabeltext_ was set.

add\_label\_near(_x_, _y_, _inline\=True_, _inline\_spacing\=5_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L445-L485)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.add_label_near "Link to this definition")

Add a label near the point `(x, y)`.

Parameters:

**x, y**float

The approximate location of the label.

**inline**bool, default: True

If _True_ remove the segment of the contour beneath the label.

**inline\_spacing**int, default: 5

Space in pixels to leave on each side of label when placing inline. This spacing will be exact for labels at locations where the contour is straight, less so for labels on curved contours.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 or [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
, default: `self.axes.transData`

A transform applied to `(x, y)` before labeling. The default causes `(x, y)` to be interpreted as data coordinates. [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
 is a synonym for [`IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
; i.e. `(x, y)` should be interpreted as display coordinates.

clabel(_levels\=None_, _\*_, _fontsize\=None_, _inline\=True_, _inline\_spacing\=5_, _fmt\=None_, _colors\=None_, _use\_clabeltext\=False_, _manual\=False_, _rightside\_up\=True_, _zorder\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L62-L231)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.clabel "Link to this definition")

Label a contour plot.

Adds labels to line contours in this [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 (which inherits from this mixin class).

Parameters:

**levels**array-like, optional

A list of level values, that should be labeled. The list must be a subset of `cs.levels`. If not given, all levels are labeled.

**fontsize**str or float, default: `[rcParams["font.size"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.size#rcparam-font-size) ` (default: `10.0`)

Size in points or relative size e.g., 'small', 'x-large'. See [`Text.set_size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "matplotlib.text.Text.set_size")
 for accepted string values.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or colors or None, default: None

The label colors:

*   If _None_, the color of each label matches the color of the corresponding contour.
    
*   If one string color, e.g., _colors_ = 'r' or _colors_ = 'red', all labels will be plotted in this color.
    
*   If a tuple of colors (string, float, RGB, etc), different labels will be plotted in different colors in the order specified.
    

**inline**bool, default: True

If `True` the underlying contour is removed where the label is placed.

**inline\_spacing**float, default: 5

Space in pixels to leave on each side of label when placing inline.

This spacing will be exact for labels at locations where the contour is straight, less so for labels on curved contours.

**fmt**[`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 or str or callable or dict, optional

How the levels are formatted:

*   If a [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
    , it is used to format all levels at once, using its [`Formatter.format_ticks`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_ticks "matplotlib.ticker.Formatter.format_ticks")
     method.
    
*   If a str, it is interpreted as a %-style format string.
    
*   If a callable, it is called with one level at a time and should return the corresponding label.
    
*   If a dict, it should directly map levels to labels.
    

The default is to use a standard [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
.

**manual**bool or iterable, default: False

If `True`, contour labels will be placed manually using mouse clicks. Click the first button near a contour to add a label, click the second button (or potentially both mouse buttons at once) to finish adding labels. The third button can be used to remove the last label added, but only if labels are not inline. Alternatively, the keyboard can be used to select label locations (enter to end label placement, delete or backspace act like the third mouse button, and any other key will select a label location).

_manual_ can also be an iterable object of (x, y) tuples. Contour labels will be created as if mouse is clicked at each (x, y) position.

**rightside\_up**bool, default: True

If `True`, label rotations will always be plus or minus 90 degrees from level.

**use\_clabeltext**bool, default: False

If `True`, use [`Text.set_transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text")
 to ensure that label rotation is updated whenever the Axes aspect changes.

**zorder**float or None, default: `(2 + contour.get_zorder())`

zorder of the contour labels.

Returns:

labels

A list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instances for the labels.

Note: The returned Text instances should not be individually removed or have their geometry modified, e.g. by changing text or font size. If you need such a modification, remove the entire [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 and recreate it.

get\_text(_lev_, _fmt_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L254-L265)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.get_text "Link to this definition")

Get the text of the label.

labels(_inline_, _inline\_spacing_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L493-L518)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.labels "Link to this definition")

locate\_label(_linecontour_, _labelwidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L267-L299)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.locate_label "Link to this definition")

Find good place to draw a label (relatively flat part of the contour).

pop\_label(_index\=\-1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L487-L491)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.pop_label "Link to this definition")

Defaults to removing last label, but any index can be supplied

print\_label(_linecontour_, _labelwidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L233-L237)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.print_label "Link to this definition")

Return whether a contour is long enough to hold a label.

remove()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L520-L530)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.remove "Link to this definition")

too\_close(_x_, _y_, _lw_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L239-L243)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.too_close "Link to this definition")

Return whether a label is already near this location.

class matplotlib.contour.ContourSet(_ax_, _\*args_, _levels\=None_, _filled\=False_, _linewidths\=None_, _linestyles\=None_, _hatches\=(None,)_, _alpha\=None_, _origin\=None_, _extent\=None_, _cmap\=None_, _colors\=None_, _norm\=None_, _vmin\=None_, _vmax\=None_, _colorizer\=None_, _extend\='neither'_, _antialiased\=None_, _nchunk\=0_, _locator\=None_, _transform\=None_, _negative\_linestyles\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L581-L1304)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "Link to this definition")

Bases: [`ContourLabeler`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler "matplotlib.contour.ContourLabeler")
, [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")

Store a set of contour lines or filled regions.

User-callable method: [`clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

**levels**\[level0, level1, ..., leveln\]

A list of floating point numbers indicating the contour levels.

**allsegs**\[level0segs, level1segs, ...\]

List of all the polygon segments for all the _levels_. For contour lines `len(allsegs) == len(levels)`, and for filled contour regions `len(allsegs) = len(levels)-1`. The lists should look like

level0segs \= \[polygon0, polygon1, ...\]
polygon0 \= \[\[x0, y0\], \[x1, y1\], ...\]

**allkinds**`None` or \[level0kinds, level1kinds, ...\]

Optional list of all the polygon vertex kinds (code types), as described and used in Path. This is used to allow multiply- connected paths such as holes within filled polygons. If not `None`, `len(allkinds) == len(allsegs)`. The lists should look like

level0kinds \= \[polygon0kinds, ...\]
polygon0kinds \= \[vertexcode0, vertexcode1, ...\]

If _allkinds_ is not `None`, usually all polygons for a particular contour level are grouped together so that `level0segs = [polygon0]` and `level0kinds = [polygon0kinds]`.

**\*\*kwargs**

Keyword arguments are as described in the docstring of [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

Attributes:

**levels**array

The values of the contour levels.

**layers**array

Same as levels for line contours; half-way between levels for filled contours. See `ContourSet._process_colors`.

Draw contour lines or filled regions, depending on whether keyword arg _filled_ is `False` (default) or `True`.

Call signature:

ContourSet(ax, levels, allsegs, \[allkinds\], \*\*kwargs)

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object to draw on.

**levels**\[level0, level1, ..., leveln\]

A list of floating point numbers indicating the contour levels.

**allsegs**\[level0segs, level1segs, ...\]

List of all the polygon segments for all the _levels_. For contour lines `len(allsegs) == len(levels)`, and for filled contour regions `len(allsegs) = len(levels)-1`. The lists should look like

level0segs \= \[polygon0, polygon1, ...\]
polygon0 \= \[\[x0, y0\], \[x1, y1\], ...\]

**allkinds**\[level0kinds, level1kinds, ...\], optional

Optional list of all the polygon vertex kinds (code types), as described and used in Path. This is used to allow multiply- connected paths such as holes within filled polygons. If not `None`, `len(allkinds) == len(allsegs)`. The lists should look like

level0kinds \= \[polygon0kinds, ...\]
polygon0kinds \= \[vertexcode0, vertexcode1, ...\]

If _allkinds_ is not `None`, usually all polygons for a particular contour level are grouped together so that `level0segs = [polygon0]` and `level0kinds = [polygon0kinds]`.

**\*\*kwargs**

Keyword arguments are as described in the docstring of [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

property allkinds[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.allkinds "Link to this definition")

property allsegs[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.allsegs "Link to this definition")

property alpha[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.alpha "Link to this definition")

changed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L966-L980)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.changed "Link to this definition")

Call this whenever the mappable is changed to notify all the callbackSM listeners to the 'changed' signal.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L1284-L1304)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

find\_nearest\_contour(_x_, _y_, _indices\=None_, _pixel\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L1230-L1282)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.find_nearest_contour "Link to this definition")

Find the point in the contour plot that is closest to `(x, y)`.

This method does not support filled contours.

Parameters:

**x, y**float

The reference point.

**indices**list of int or None, default: None

Indices of contour levels to consider. If None (the default), all levels are considered.

**pixel**bool, default: True

If _True_, measure distance in pixel (screen) space, which is useful for manual contour labeling; else, measure distance in axes space.

Returns:

**path**int

The index of the path that is closest to `(x, y)`. Each path corresponds to one contour level.

**subpath**int

The index within that closest path of the subpath that is closest to `(x, y)`. Each subpath corresponds to one unbroken contour line.

**index**int

The index of the vertices within that subpath that are closest to `(x, y)`.

**xmin, ymin**float

The point in the contour plot that is closest to `(x, y)`.

**d2**float

The squared distance from `(xmin, ymin)` to `(x, y)`.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L823-L830)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 instance used by this ContourSet.

legend\_elements(_variable\_name\='x'_, _str\_format\=<class 'str'>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L840-L892)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.legend_elements "Link to this definition")

Return a list of artists and labels suitable for passing through to [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 which represent this ContourSet.

The labels have the form "0 < x <= 1" stating the data ranges which the artists represent.

Parameters:

**variable\_name**str

The string used inside the inequality used on the labels.

**str\_format**function: float -> str

Function used to format the numbers in the labels.

Returns:

**artists**list\[[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
\]

A list of the artists.

**labels**list\[str\]

A list of the labels.

property linestyles[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.linestyles "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _array\=<UNSET>_, _capstyle\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _offset\_transform\=<UNSET>_, _offsets\=<UNSET>_, _path\_effects\=<UNSET>_, _paths\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _urls\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |
> | [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |
> | [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_color "matplotlib.collections.Collection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of RGBA tuples |
> | [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |
> | [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |
> | [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_paths "matplotlib.collections.Collection.set_paths") | unknown |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.contour.QuadContourSet(_ax_, _\*args_, _levels\=None_, _filled\=False_, _linewidths\=None_, _linestyles\=None_, _hatches\=(None,)_, _alpha\=None_, _origin\=None_, _extent\=None_, _cmap\=None_, _colors\=None_, _norm\=None_, _vmin\=None_, _vmax\=None_, _colorizer\=None_, _extend\='neither'_, _antialiased\=None_, _nchunk\=0_, _locator\=None_, _transform\=None_, _negative\_linestyles\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/contour.py#L1307-L1484)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "Link to this definition")

Bases: [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")

Create and store a set of contour lines or filled regions.

This class is typically not instantiated directly by the user but by [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
.

Attributes:

**levels**array

The values of the contour levels.

**layers**array

Same as levels for line contours; half-way between levels for filled contours. See `ContourSet._process_colors`.

Draw contour lines or filled regions, depending on whether keyword arg _filled_ is `False` (default) or `True`.

Call signature:

ContourSet(ax, levels, allsegs, \[allkinds\], \*\*kwargs)

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object to draw on.

**levels**\[level0, level1, ..., leveln\]

A list of floating point numbers indicating the contour levels.

**allsegs**\[level0segs, level1segs, ...\]

List of all the polygon segments for all the _levels_. For contour lines `len(allsegs) == len(levels)`, and for filled contour regions `len(allsegs) = len(levels)-1`. The lists should look like

level0segs \= \[polygon0, polygon1, ...\]
polygon0 \= \[\[x0, y0\], \[x1, y1\], ...\]

**allkinds**\[level0kinds, level1kinds, ...\], optional

Optional list of all the polygon vertex kinds (code types), as described and used in Path. This is used to allow multiply- connected paths such as holes within filled polygons. If not `None`, `len(allkinds) == len(allsegs)`. The lists should look like

level0kinds \= \[polygon0kinds, ...\]
polygon0kinds \= \[vertexcode0, vertexcode1, ...\]

If _allkinds_ is not `None`, usually all polygons for a particular contour level are grouped together so that `level0segs = [polygon0]` and `level0kinds = [polygon0kinds]`.

**\*\*kwargs**

Keyword arguments are as described in the docstring of [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _array\=<UNSET>_, _capstyle\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _offset\_transform\=<UNSET>_, _offsets\=<UNSET>_, _path\_effects\=<UNSET>_, _paths\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _urls\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |
> | [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |
> | [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_color "matplotlib.collections.Collection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of RGBA tuples |
> | [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |
> | [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |
> | [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_paths "matplotlib.collections.Collection.set_paths") | unknown |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

On this page