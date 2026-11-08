[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.inset\_locator.AnchoredZoomLocator[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.html#mpl-toolkits-axes-grid1-inset-locator-anchoredzoomlocator "Link to this heading")

===========================================================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.inset\_locator.AnchoredZoomLocator(_parent\_axes_, _zoom_, _loc_, _borderpad\=0.5_, _bbox\_to\_anchor\=None_, _bbox\_transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/inset_locator.py#L65-L85)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator "Link to this definition")

Bases: [`AnchoredLocatorBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredLocatorBase.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredLocatorBase "mpl_toolkits.axes_grid1.inset_locator.AnchoredLocatorBase")

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

get\_bbox(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/inset_locator.py#L78-L85)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.get_bbox "Link to this definition")

Return the bbox of the offsetbox, ignoring parent offsets.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _bbox\_to\_anchor\=<UNSET>_, _child\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.set "Link to this definition")

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

On this page