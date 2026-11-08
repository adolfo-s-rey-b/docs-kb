[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.anchored\_artists.AnchoredDirectionArrows[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl-toolkits-axes-grid1-anchored-artists-anchoreddirectionarrows "Link to this heading")

================================================================================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.anchored\_artists.AnchoredDirectionArrows(_transform_, _label\_x_, _label\_y_, _length\=0.15_, _fontsize\=0.08_, _loc\='upper left'_, _angle\=0_, _aspect\_ratio\=1_, _pad\=0.4_, _borderpad\=0.4_, _frameon\=False_, _color\='w'_, _alpha\=1_, _sep\_x\=0.01_, _sep\_y\=0_, _fontproperties\=None_, _back\_length\=0.15_, _head\_width\=10_, _head\_length\=15_, _tail\_width\=2_, _text\_props\=None_, _arrow\_props\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/anchored_artists.py#L244-L414)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "Link to this definition")

Bases: [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")

Draw two perpendicular arrows to indicate directions.

Parameters:

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transformation object for the coordinate system in use, i.e., `matplotlib.axes.Axes.transAxes`.

**label\_x, label\_y**str

Label text for the x and y arrows

**length**float, default: 0.15

Length of the arrow, given in coordinates of _transform_.

**fontsize**float, default: 0.08

Size of label strings, given in coordinates of _transform_.

**loc**str, default: 'upper left'

Location of the arrow. Valid locations are 'upper left', 'upper center', 'upper right', 'center left', 'center', 'center right', 'lower left', 'lower center', 'lower right'. For backward compatibility, numeric values are accepted as well. See the parameter _loc_ of [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 for details.

**angle**float, default: 0

The angle of the arrows in degrees.

**aspect\_ratio**float, default: 1

The ratio of the length of arrow\_x and arrow\_y. Negative numbers can be used to change the direction.

**pad**float, default: 0.4

Padding around the labels and arrows, in fraction of the font size.

**borderpad**float, default: 0.4

Border padding, in fraction of the font size.

**frameon**bool, default: False

If True, draw a box around the arrows and labels.

**color**str, default: 'white'

Color for the arrows and labels.

**alpha**float, default: 1

Alpha values of the arrows and labels

**sep\_x, sep\_y**float, default: 0.01 and 0 respectively

Separation between the arrows and labels in coordinates of _transform_.

**fontproperties**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
, optional

Font properties for the label text.

**back\_length**float, default: 0.15

Fraction of the arrow behind the arrow crossing.

**head\_width**float, default: 10

Width of arrow head, sent to [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
.

**head\_length**float, default: 15

Length of arrow head, sent to [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
.

**tail\_width**float, default: 2

Width of arrow tail, sent to [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
.

**text\_props, arrow\_props**dict

Properties of the text and arrows, passed to [`TextPath`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "matplotlib.text.TextPath")
 and [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
.

**\*\*kwargs**

Keyword arguments forwarded to [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
.

Attributes:

**arrow\_x, arrow\_y**[`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")

Arrow x and y

**text\_path\_x, text\_path\_y**[`TextPath`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "matplotlib.text.TextPath")

Path for arrow labels

**p\_x, p\_y**[`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")

Patch for arrow labels

**box**[`AuxTransformBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")

Container for the arrows and labels.

Notes

If _prop_ is passed as a keyword argument, but _fontproperties_ is not, then _prop_ is assumed to be the intended _fontproperties_. Using both _prop_ and _fontproperties_ is not supported.

Examples

\>>> import matplotlib.pyplot as plt
\>>> import numpy as np
\>>> from mpl\_toolkits.axes\_grid1.anchored\_artists import (
...     AnchoredDirectionArrows)
\>>> fig, ax \= plt.subplots()
\>>> ax.imshow(np.random.random((10, 10)))
\>>> arrows \= AnchoredDirectionArrows(ax.transAxes, '111', '110')
\>>> ax.add\_artist(arrows)
\>>> fig.show()

Using several of the optional parameters, creating downward pointing arrow and high contrast text labels.

\>>> import matplotlib.font\_manager as fm
\>>> fontprops \= fm.FontProperties(family\='monospace')
\>>> arrows \= AnchoredDirectionArrows(ax.transAxes, 'East', 'South',
...                                  loc\='lower left', color\='k',
...                                  aspect\_ratio\=-1, sep\_x\=0.02,
...                                  sep\_y\=-0.01,
...                                  text\_props\={'ec':'w', 'fc':'k'},
...                                  fontproperties\=fontprops)

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _bbox\_to\_anchor\=<UNSET>_, _child\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _height\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _offset\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _width\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.set "Link to this definition")

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

Examples using `mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#examples-using-mpl-toolkits-axes-grid1-anchored-artists-anchoreddirectionarrows "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_anchored_direction_arrows_thumb.png)

[Anchored Direction Arrow](https://matplotlib.org/stable/gallery/axes_grid1/demo_anchored_direction_arrows.html)

Anchored Direction Arrow

On this page