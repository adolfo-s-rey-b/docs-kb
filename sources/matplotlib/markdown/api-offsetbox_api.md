[Skip to main content](https://matplotlib.org/stable/api/offsetbox_api.html#main-content)

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
    

`matplotlib.offsetbox`[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib-offsetbox "Link to this heading")

============================================================================================================================

Inheritance diagram of matplotlib.offsetbox

Container classes for [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s.

[`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

The base of all container artists defined in this module.

[`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
, [`AnchoredText`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")

Anchor and align an arbitrary [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or a text relative to the parent axes or a specific anchor point.

[`DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")

A container with fixed width and height. Children have a fixed position inside the container and may be clipped.

[`HPacker`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")
, [`VPacker`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.VPacker "matplotlib.offsetbox.VPacker")

Containers for layouting their children vertically or horizontally.

[`PaddedBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox "matplotlib.offsetbox.PaddedBox")

A container to add a padding around an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
.

[`TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")

Contains a single [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance.

class matplotlib.offsetbox.AnchoredOffsetbox(_loc_, _\*_, _pad\=0.4_, _borderpad\=0.5_, _child\=None_, _prop\=None_, _frameon\=True_, _bbox\_to\_anchor\=None_, _bbox\_transform\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L908-L1100)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

An OffsetBox placed according to location _loc_.

AnchoredOffsetbox has a single child. When multiple children are needed, use an extra OffsetBox to enclose them. By default, the offset box is anchored against its parent Axes. You may explicitly specify the _bbox\_to\_anchor_.

Parameters:

**loc**str

The box location. Valid locations are 'upper left', 'upper center', 'upper right', 'center left', 'center', 'center right', 'lower left', 'lower center', 'lower right'. For backward compatibility, numeric values are accepted as well. See the parameter _loc_ of [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 for details.

**pad**float, default: 0.4

Padding around the child as fraction of the fontsize.

**borderpad**float or (float, float), default: 0.5

Padding between the offsetbox frame and the _bbox\_to\_anchor_. If a float, the same padding is used for both x and y. If a tuple of two floats, it specifies the (x, y) padding.

Added in version 3.11: The _borderpad_ parameter now accepts a tuple of (x, y) paddings.

**child**[`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

The box that will be anchored.

**prop**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

This is only used as a reference for paddings. If not given, `[rcParams["legend.fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.fontsize#rcparam-legend-fontsize) ` (default: `'medium'`) is used.

**frameon**bool

Whether to draw a frame around the box.

**bbox\_to\_anchor**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
, 2-tuple, or 4-tuple of floats

Box that is used to position the legend in conjunction with _loc_.

**bbox\_transform**None or [`matplotlib.transforms.Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform for the bounding box (_bbox\_to\_anchor_).

**\*\*kwargs**

All other parameters are passed on to [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
.

Notes

See [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 for a detailed description of the anchoring mechanism.

codes \= {'center': 10, 'center left': 6, 'center right': 7, 'lower center': 8, 'lower left': 3, 'lower right': 4, 'right': 5, 'upper center': 9, 'upper left': 2, 'upper right': 1}[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.codes "Link to this definition")

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1086-L1100)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1018-L1022)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

get\_bbox\_to\_anchor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1024-L1033)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.get_bbox_to_anchor "Link to this definition")

Return the bbox that the box is anchored to.

get\_child()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1010-L1012)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.get_child "Link to this definition")

Return the child.

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1014-L1016)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.get_children "Link to this definition")

Return the list of children.

get\_offset(_bbox_, _renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1060-L1079)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.get_offset "Link to this definition")

Return the offset as a tuple (x, y).

The extent parameters have to be provided to handle the case where the offset is dynamically determined by a callable (see [`set_offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset")
).

Parameters:

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _bbox\_to\_anchor\=<UNSET>_, _child\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`bbox_to_anchor`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set_bbox_to_anchor "matplotlib.offsetbox.AnchoredOffsetbox.set_bbox_to_anchor") | unknown |
> | [`child`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set_child "matplotlib.offsetbox.AnchoredOffsetbox.set_child") | unknown |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_bbox\_to\_anchor(_bbox_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1035-L1058)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set_bbox_to_anchor "Link to this definition")

Set the bbox that the box is anchored to.

_bbox_ can be a Bbox instance, a list of \[left, bottom, width, height\], or a list of \[left, bottom\] where the width and height will be assumed to be zero. The bbox will be transformed to display coordinate by the given transform.

set\_child(_child_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1003-L1008)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set_child "Link to this definition")

Set the child to be anchored.

update\_frame(_bbox_, _fontsize\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1081-L1084)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.update_frame "Link to this definition")

zorder \= 5[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.zorder "Link to this definition")

class matplotlib.offsetbox.AnchoredText(_s_, _loc_, _\*_, _pad\=0.4_, _borderpad\=0.5_, _prop\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1115-L1155)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "Link to this definition")

Bases: [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")

AnchoredOffsetbox with Text.

Parameters:

**s**str

Text.

**loc**str

Location code. See [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
.

**pad**float, default: 0.4

Padding around the text as fraction of the fontsize.

**borderpad**float, default: 0.5

Spacing between the offsetbox frame and the _bbox\_to\_anchor_.

**prop**dict, optional

Dictionary of keyword parameters to be passed to the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance contained inside AnchoredText.

**\*\*kwargs**

All other parameters are passed to [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _bbox\_to\_anchor\=<UNSET>_, _child\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`bbox_to_anchor`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set_bbox_to_anchor "matplotlib.offsetbox.AnchoredOffsetbox.set_bbox_to_anchor") | unknown |
> | [`child`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox.set_child "matplotlib.offsetbox.AnchoredOffsetbox.set_child") | unknown |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.offsetbox.AnnotationBbox(_offsetbox_, _xy_, _xybox\=None_, _xycoords\='data'_, _boxcoords\=None_, _\*_, _frameon\=True_, _pad\=0.4_, _annotation\_clip\=None_, _box\_alignment\=(0.5, 0.5)_, _bboxprops\=None_, _arrowprops\=None_, _fontsize\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1291-L1531)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, `_AnnotationBase`

Container for an [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 referring to a specific position _xy_.

Optionally an arrow pointing from the offsetbox to _xy_ can be drawn.

This is like [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
, but with [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 instead of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

Parameters:

**offsetbox**[`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

**xy**(float, float)

The point _(x, y)_ to annotate. The coordinate system is determined by _xycoords_.

**xybox**(float, float), default: _xy_

The position _(x, y)_ to place the text at. The coordinate system is determined by _boxcoords_.

**xycoords**single or two-tuple of str or [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 or callable, default: 'data'

The coordinate system that _xy_ is given in. See the parameter _xycoords_ in [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 for a detailed description.

**boxcoords**single or two-tuple of str or [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 or callable, default: value of _xycoords_

The coordinate system that _xybox_ is given in. See the parameter _textcoords_ in [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 for a detailed description.

**frameon**bool, default: True

By default, the text is surrounded by a white [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 (accessible as the `patch` attribute of the [`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
). If _frameon_ is set to False, this patch is made invisible.

**annotation\_clip: bool or None, default: None**

Whether to clip (i.e. not draw) the annotation when the annotation point _xy_ is outside the Axes area.

*   If _True_, the annotation will be clipped when _xy_ is outside the Axes.
    
*   If _False_, the annotation will always be drawn.
    
*   If _None_, the annotation will be clipped when _xy_ is outside the Axes and _xycoords_ is 'data'.
    

**pad**float, default: 0.4

Padding around the offsetbox.

**box\_alignment**(float, float)

A tuple of two floats for a vertical and horizontal alignment of the offset box w.r.t. the _boxcoords_. The lower-left corner is (0, 0) and upper-right corner is (1, 1).

**bboxprops**dict, optional

A dictionary of properties to set for the annotation bounding box, for example _boxstyle_ and _alpha_. See [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 for details.

**arrowprops: dict, optional**

Arrow properties, see [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 for description.

**fontsize: float or str, optional**

Translated to points and passed as _mutation\_scale_ into [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 to scale attributes of the box style (e.g. pad or rounding\_size). The name is chosen in analogy to [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 where _fontsize_ defines the mutation scale as well. If not given, `[rcParams["legend.fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.fontsize#rcparam-legend-fontsize) ` (default: `'medium'`) is used. See [`Text.set_fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")
 for valid values.

**\*\*kwargs**

Other [`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
 properties. See [`AnnotationBbox.set`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.set "matplotlib.offsetbox.AnnotationBbox.set")
 for a list.

property anncoords[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.anncoords "Link to this definition")

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1431-L1437)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.contains "Link to this definition")

Test whether the artist contains the mouse event.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

An artist-specific dictionary of details of the event context, such as which points are contained in the pick radius. See the individual Artist subclasses for details.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1517-L1531)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1439-L1443)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.get_children "Link to this definition")

Return a list of the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s of this [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
.

get\_fontsize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1461-L1463)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.get_fontsize "Link to this definition")

Return the fontsize in points.

get\_tightbbox(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1473-L1479)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.get_tightbbox "Link to this definition")

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

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1465-L1471)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.get_window_extent "Link to this definition")

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

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _annotation\_clip\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _fontsize\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | `annotation_clip` | bool or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | unknown |
> | [`fontsize`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.set_fontsize "matplotlib.offsetbox.AnnotationBbox.set_fontsize") | unknown |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
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

set\_figure(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1445-L1449)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.set_figure "Link to this definition")

Set the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 instance the artist belongs to.

Warning

This function should typically not be called by users.

This is a low-level API and only modifies the internal state of the Artist. Only modifying this is not enough and will typically lead to an inconsistent state, because the state of the figure has to be changed as well.

Users should typically instead call one of the high-level APIs, i.e. [`Figure.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
 or one of the Axes methods [Adding artists](https://matplotlib.org/stable/api/axes_api.html#axes-api-adding-artists)
.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

set\_fontsize(_s\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1451-L1459)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.set_fontsize "Link to this definition")

Set the fontsize in points.

If _s_ is not given, reset to `[rcParams["legend.fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.fontsize#rcparam-legend-fontsize) ` (default: `'medium'`).

update\_positions(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1481-L1515)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.update_positions "Link to this definition")

Update pixel positions for the annotated point, the text, and the arrow.

property xyann[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.xyann "Link to this definition")

zorder \= 3[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.zorder "Link to this definition")

class matplotlib.offsetbox.AuxTransformBox(_aux\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L828-L905)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

An OffsetBox with an auxiliary transform.

All child artists are first transformed with _aux\_transform_, then translated with an offset (the same for all children) so the bounding box of the children matches the drawn box. (In other words, adding an arbitrary translation to _aux\_transform_ has no effect as it will be cancelled out by the later offsetting.)

[`AuxTransformBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
 is similar to [`DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
, except that the extent of the box is not predetermined but calculated from the window extent of its children, and the extent of the children will be calculated in the transformed coordinate.

add\_artist(_a_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L851-L855)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.add_artist "Link to this definition")

Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 to the container box.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L900-L905)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L886-L898)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L882-L884)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.get_offset "Link to this definition")

Return offset of the container.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L857-L861)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 applied to the children.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.set_offset "matplotlib.offsetbox.AuxTransformBox.set_offset") | (float, float) |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.set_transform "matplotlib.offsetbox.AuxTransformBox.set_transform") | unknown |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_offset(_xy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L868-L880)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.set_offset "Link to this definition")

Set the offset of the container.

Parameters:

**xy**(float, float)

The (x, y) coordinates of the offset in display units.

set\_transform(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L863-L866)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox.set_transform "Link to this definition")

set\_transform is ignored.

class matplotlib.offsetbox.DraggableAnnotation(_annotation_, _use\_blit\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1677-L1689)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableAnnotation "Link to this definition")

Bases: [`DraggableBase`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase "matplotlib.offsetbox.DraggableBase")

save\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1682-L1684)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableAnnotation.save_offset "Link to this definition")

update\_offset(_dx_, _dy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1686-L1689)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableAnnotation.update_offset "Link to this definition")

class matplotlib.offsetbox.DraggableBase(_ref\_artist_, _use\_blit\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1534-L1649)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Helper base class for a draggable artist (legend, offsetbox).

Derived classes must override the following methods:

def save\_offset(self):
    '''
    Called when the object is picked for dragging; should save the
    reference position of the artist.
    '''

def update\_offset(self, dx, dy):
    '''
    Called during the dragging; (\*dx\*, \*dy\*) is the pixel offset from
    the point where the mouse drag started.
    '''

Optionally, you may override the following method:

def finalize\_offset(self):
    '''Called when the mouse is released.'''

In the current implementation of [`DraggableLegend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.DraggableLegend "matplotlib.legend.DraggableLegend")
 and [`DraggableAnnotation`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableAnnotation "matplotlib.offsetbox.DraggableAnnotation")
, [`update_offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.update_offset "matplotlib.offsetbox.DraggableBase.update_offset")
 places the artists in display coordinates, and [`finalize_offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.finalize_offset "matplotlib.offsetbox.DraggableBase.finalize_offset")
 recalculates their position in axes coordinate and set a relevant attribute.

property canvas[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.canvas "Link to this definition")

property cids[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.cids "Link to this definition")

disconnect()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1637-L1640)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.disconnect "Link to this definition")

Disconnect the callbacks.

finalize\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1648-L1649)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.finalize_offset "Link to this definition")

on\_motion(_evt_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1592-L1603)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.on_motion "Link to this definition")

on\_pick(_evt_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1605-L1618)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.on_pick "Link to this definition")

on\_release(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1620-L1628)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.on_release "Link to this definition")

save\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1642-L1643)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.save_offset "Link to this definition")

update\_offset(_dx_, _dy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1645-L1646)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.update_offset "Link to this definition")

class matplotlib.offsetbox.DraggableOffsetBox(_ref\_artist_, _offsetbox_, _use\_blit\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1652-L1674)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableOffsetBox "Link to this definition")

Bases: [`DraggableBase`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase "matplotlib.offsetbox.DraggableBase")

get\_loc\_in\_canvas()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1668-L1674)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableOffsetBox.get_loc_in_canvas "Link to this definition")

save\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1657-L1662)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableOffsetBox.save_offset "Link to this definition")

update\_offset(_dx_, _dy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1664-L1666)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableOffsetBox.update_offset "Link to this definition")

class matplotlib.offsetbox.DrawingArea(_width_, _height_, _xdescent\=0.0_, _ydescent\=0.0_, _clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L597-L706)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

The DrawingArea can contain any Artist as a child. The DrawingArea has a fixed width and height. The position of children relative to the parent is fixed. The children can be clipped at the boundaries of the parent.

Parameters:

**width, height**float

Width and height of the container box.

**xdescent, ydescent**float

Descent of the box in x- and y-direction.

**clip**bool

Whether to clip the children to the box.

add\_artist(_a_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L674-L683)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "Link to this definition")

Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 to the container box.

property clip\_children[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.clip_children "Link to this definition")

If the children of this DrawingArea should be clipped by DrawingArea bounding box.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L685-L706)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L667-L672)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L663-L665)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.get_offset "Link to this definition")

Return offset of the container.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L638-L642)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.get_transform "Link to this definition")

Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 applied to the children.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.set_offset "matplotlib.offsetbox.DrawingArea.set_offset") | (float, float) |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.set_transform "matplotlib.offsetbox.DrawingArea.set_transform") | unknown |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_offset(_xy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L649-L661)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.set_offset "Link to this definition")

Set the offset of the container.

Parameters:

**xy**(float, float)

The (x, y) coordinates of the offset in display units.

set\_transform(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L644-L647)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.set_transform "Link to this definition")

set\_transform is ignored.

class matplotlib.offsetbox.HPacker(_pad\=0.0_, _sep\=0.0_, _width\=None_, _height\=None_, _align\='baseline'_, _mode\='fixed'_, _children\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L475-L506)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "Link to this definition")

Bases: [`PackerBase`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PackerBase "matplotlib.offsetbox.PackerBase")

HPacker packs its children horizontally, automatically adjusting their relative positions at draw time.

+-------------------------------+
| Child 1    Child 2    Child 3 |
+-------------------------------+

Parameters:

**pad**float, default: 0.0

The boundary padding in points.

**sep**float, default: 0.0

The spacing between items in points.

**width, height**float, optional

Width and height of the container box in pixels, calculated if _None_.

**align**{'top', 'bottom', 'left', 'right', 'center', 'baseline'}, default: 'baseline'

Alignment of boxes.

**mode**{'fixed', 'expand', 'equal'}, default: 'fixed'

The packing mode.

*   'fixed' packs the given [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
    s tight with _sep_ spacing.
    
*   'expand' uses the maximal available space to distribute the artists with equal spacing in between.
    
*   'equal': Each artist an equal fraction of the available space and is left-aligned (or top-aligned) therein.
    

**children**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The artists to pack.

Notes

_pad_ and _sep_ are in points and will be scaled with the renderer dpi, while _width_ and _height_ are in pixels.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.offsetbox.OffsetBox(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L202-L385)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "Link to this definition")

Bases: [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

A simple container artist.

The child artists are meant to be drawn at a relative position to its parent.

Being an artist itself, all keyword arguments are passed on to [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
.

property axes[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.axes "Link to this definition")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance the artist resides in, or _None_.

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L241-L271)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.contains "Link to this definition")

Delegate the mouse event contains-check to the children.

As a container, the [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 does not respond itself to mouseevents.

Parameters:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

Returns:

**contains**bool

Whether any values are within the radius.

**details**dict

An artist-specific dictionary of details of the event context, such as which points are contained in the pick radius. See the individual Artist subclasses for details.

See also

[`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains")

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L374-L385)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L358-L361)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L336-L338)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_children "Link to this definition")

Return a list of the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s.

get\_offset(_bbox_, _renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L291-L308)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_offset "Link to this definition")

Return the offset as a tuple (x, y).

The extent parameters have to be provided to handle the case where the offset is dynamically determined by a callable (see [`set_offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset")
).

Parameters:

**bbox**[`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

get\_visible\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L332-L334)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_visible_children "Link to this definition")

Return a list of the visible child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L363-L372)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.get_window_extent "Link to this definition")

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

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_figure(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L221-L231)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "Link to this definition")

Set the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 for the [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 and all its children.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

set\_height(_height_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L321-L330)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "Link to this definition")

Set the height of the box.

Parameters:

**height**float

set\_offset(_xy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L273-L289)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "Link to this definition")

Set the offset.

Parameters:

**xy**(float, float) or callable

The (x, y) coordinates of the offset in display units. These can either be given explicitly as a tuple (x, y), or by providing a function that converts the extent into the offset. This function must have the signature:

def offset(width, height, xdescent, ydescent, renderer) \-> (float, float)

set\_width(_width_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L310-L319)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "Link to this definition")

Set the width of the box.

Parameters:

**width**float

class matplotlib.offsetbox.OffsetImage(_arr_, _\*_, _zoom\=1_, _cmap\=None_, _norm\=None_, _interpolation\=None_, _origin\=None_, _filternorm\=True_, _filterrad\=4.0_, _resample\=False_, _dpi\_cor\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1158-L1288)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

Container artist for images.

Image data is displayed using [`BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
. This image is meant to be positioned relative to a parent artist.

Parameters:

**arr: array-like or \`PIL.Image.Image\`**

The data to be color-coded. The interpretation depends on the shape:

*   (M, N) [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     or masked array: values to be colormapped
    
*   (M, N, 3): RGB array
    
*   (M, N, 4): RGBA array
    

**zoom: float, default: 1**

zoom factor:

*   no zoom: factor =1
    
*   zoom in: factor > 1
    
*   zoom out: 0< factor < 1
    

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors. This parameter is ignored if X is RGB(A).

**norm**str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
, default: None

Maps luminance to 0-1. This parameter is ignored if X is RGB(A).

**interpolation**str, default: `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`)

Supported values are 'none', 'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'blackman'.

**origin**{'upper', 'lower'}, default: `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`)

Place the \[0, 0\] index of the array in the upper left or lower left corner of the Axes. The convention 'upper' is typically used for matrices and images.

**filternorm**bool, default: True

A parameter for the antigrain image resize filter (see the antigrain documentation). If filternorm is set, the filter normalizes integer values and corrects the rounding errors. It doesn't do anything with the source floating point values, it corrects only integers according to the rule of 1.0 which means that any sum of pixel weights must be equal to 1.0. So, the filter function must produce a graph of the proper shape.

**filterrad**float > 0, default: 4

The filter radius for filters that have a radius parameter, i.e. when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

**resample**bool, default: False

When True, use a full resampling method. When False, only resample when the output image is larger than the input image.

**dpi\_cor: bool, default: True**

Correct for the backend DPI setting

**\*\*kwargs**[`BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
 properties

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1284-L1288)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1276-L1282)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1273-L1274)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.get_children "Link to this definition")

Return a list of the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s.

get\_data()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1259-L1260)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.get_data "Link to this definition")

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1269-L1271)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.get_offset "Link to this definition")

Return offset of the container.

get\_zoom()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1266-L1267)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.get_zoom "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _data\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zoom\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`data`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.set_data "matplotlib.offsetbox.OffsetImage.set_data") | unknown |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zoom`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.set_zoom "matplotlib.offsetbox.OffsetImage.set_zoom") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_data(_arr_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1254-L1257)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.set_data "Link to this definition")

set\_zoom(_zoom_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L1262-L1264)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage.set_zoom "Link to this definition")

class matplotlib.offsetbox.PackerBase(_pad\=0.0_, _sep\=0.0_, _width\=None_, _height\=None_, _align\='baseline'_, _mode\='fixed'_, _children\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L388-L432)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PackerBase "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

Parameters:

**pad**float, default: 0.0

The boundary padding in points.

**sep**float, default: 0.0

The spacing between items in points.

**width, height**float, optional

Width and height of the container box in pixels, calculated if _None_.

**align**{'top', 'bottom', 'left', 'right', 'center', 'baseline'}, default: 'baseline'

Alignment of boxes.

**mode**{'fixed', 'expand', 'equal'}, default: 'fixed'

The packing mode.

*   'fixed' packs the given [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
    s tight with _sep_ spacing.
    
*   'expand' uses the maximal available space to distribute the artists with equal spacing in between.
    
*   'equal': Each artist an equal fraction of the available space and is left-aligned (or top-aligned) therein.
    

**children**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The artists to pack.

Notes

_pad_ and _sep_ are in points and will be scaled with the renderer dpi, while _width_ and _height_ are in pixels.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PackerBase.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.offsetbox.PaddedBox(_child_, _pad\=0.0_, _\*_, _draw\_frame\=False_, _patch\_attrs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L509-L594)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

A container to add a padding around an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
.

The [`PaddedBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox "matplotlib.offsetbox.PaddedBox")
 contains a [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 that is used to visualize it when rendering.

+----------------------------+
|                            |
|                            |
|                            |
| <--pad--> Artist           |
|             ^              |
|            pad             |
|             v              |
+----------------------------+

Attributes:

**pad**float

The padding in points.

**patch**[`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")

When _draw\_frame_ is True, this [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 is made visible and creates a border around the box.

Parameters:

**child**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The contained [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
.

**pad**float, default: 0.0

The padding in points. This will be scaled with the renderer dpi. In contrast, _width_ and _height_ are in _pixels_ and thus not scaled.

**draw\_frame**bool

Whether to draw the contained [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
.

**patch\_attrs**dict or None

Additional parameters passed to the contained [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L571-L583)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

draw\_frame(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L591-L594)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox.draw_frame "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

update\_frame(_bbox_, _fontsize\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L585-L589)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PaddedBox.update_frame "Link to this definition")

class matplotlib.offsetbox.TextArea(_s_, _\*_, _textprops\=None_, _multilinebaseline\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L709-L825)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "Link to this definition")

Bases: [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")

The TextArea is a container artist for a single Text instance.

The text is placed at (0, 0) with baseline+left alignment, by default. The width and height of the TextArea instance is the width and height of its child text.

Parameters:

**s**str

The text to be displayed.

**textprops**dict, default: {}

Dictionary of keyword parameters to be passed to the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance in the TextArea.

**multilinebaseline**bool, default: False

Whether the baseline for multiline text is adjusted so that it is (approximately) center-aligned with single-line text.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L821-L825)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.draw "Link to this definition")

Update the location of children if necessary and draw them to the given _renderer_.

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L796-L819)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

get\_multilinebaseline()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L767-L771)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.get_multilinebaseline "Link to this definition")

Get multilinebaseline.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L792-L794)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.get_offset "Link to this definition")

Return offset of the container.

get\_text()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L751-L753)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.get_text "Link to this definition")

Return the string representation of this area's text.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _multilinebaseline\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _text\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`multilinebaseline`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_multilinebaseline "matplotlib.offsetbox.TextArea.set_multilinebaseline") | unknown |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_offset "matplotlib.offsetbox.TextArea.set_offset") | (float, float) |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`text`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_text "matplotlib.offsetbox.TextArea.set_text") | unknown |
> | [`transform`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_transform "matplotlib.offsetbox.TextArea.set_transform") | unknown |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_multilinebaseline(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L755-L765)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_multilinebaseline "Link to this definition")

Set multilinebaseline.

If True, the baseline for multiline text is adjusted so that it is (approximately) center-aligned with single-line text. This is used e.g. by the legend implementation so that single-line labels are baseline-aligned, but multiline labels are "center"-aligned with them.

set\_offset(_xy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L778-L790)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_offset "Link to this definition")

Set the offset of the container.

Parameters:

**xy**(float, float)

The (x, y) coordinates of the offset in display units.

set\_text(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L746-L749)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_text "Link to this definition")

Set the text of this area as a string.

set\_transform(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L773-L776)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea.set_transform "Link to this definition")

set\_transform is ignored.

class matplotlib.offsetbox.VPacker(_pad\=0.0_, _sep\=0.0_, _width\=None_, _height\=None_, _align\='baseline'_, _mode\='fixed'_, _children\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/offsetbox.py#L435-L472)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.VPacker "Link to this definition")

Bases: [`PackerBase`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.PackerBase "matplotlib.offsetbox.PackerBase")

VPacker packs its children vertically, automatically adjusting their relative positions at draw time.

+---------+
| Child 1 |
| Child 2 |
| Child 3 |
+---------+

Parameters:

**pad**float, default: 0.0

The boundary padding in points.

**sep**float, default: 0.0

The spacing between items in points.

**width, height**float, optional

Width and height of the container box in pixels, calculated if _None_.

**align**{'top', 'bottom', 'left', 'right', 'center', 'baseline'}, default: 'baseline'

Alignment of boxes.

**mode**{'fixed', 'expand', 'equal'}, default: 'fixed'

The packing mode.

*   'fixed' packs the given [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
    s tight with _sep_ spacing.
    
*   'expand' uses the maximal available space to distribute the artists with equal spacing in between.
    
*   'equal': Each artist an equal fraction of the available space and is left-aligned (or top-aligned) therein.
    

**children**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The artists to pack.

Notes

_pad_ and _sep_ are in points and will be scaled with the renderer dpi, while _width_ and _height_ are in pixels.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.VPacker.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_figure "matplotlib.offsetbox.OffsetBox.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`height`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_height "matplotlib.offsetbox.OffsetBox.set_height") | float |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_offset "matplotlib.offsetbox.OffsetBox.set_offset") | (float, float) or callable |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`width`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox.set_width "matplotlib.offsetbox.OffsetBox.set_width") | float |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

On this page