[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.Path3DCollection[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl-toolkits-mplot3d-art3d-path3dcollection "Link to this heading")

===============================================================================================================================================================================================================

class mpl\_toolkits.mplot3d.art3d.Path3DCollection(_\*args_, _zs\=0_, _zdir\='z'_, _depthshade\=None_, _depthshade\_minalpha\=None_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L941-L1175)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection "Link to this definition")

Bases: [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")

A collection of 3D paths.

Create a collection of flat 3D paths with its normal vector pointed in _zdir_ direction, and located at _zs_ on the _zdir_ axis. 'zs' can be a scalar or an array-like of the same length as the number of paths in the collection.

Constructor arguments are the same as for [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
. In addition, keywords _zs=0_ and _zdir='z'_ are available.

Also, the keyword argument _depthshade_ is available to indicate whether or not to shade the patches in order to give the appearance of depth (default is _True_). This is typically desired in scatter plots.

_depthshade\_minalpha_ sets the minimum alpha value applied by depth-shading.

do\_3d\_projection()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1084-L1127)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.do_3d_projection "Link to this definition")

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L985-L988)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

get\_depthshade()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1057-L1058)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.get_depthshade "Link to this definition")

get\_edgecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1169-L1175)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.get_edgecolor "Link to this definition")

get\_facecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1166-L1167)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.get_facecolor "Link to this definition")

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _array\=<UNSET>_, _capstyle\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _color\=<UNSET>_, _depthshade\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _offset\_transform\=<UNSET>_, _offsets\=<UNSET>_, _path\_effects\=<UNSET>_, _paths\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sizes\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _sort\_zpos\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _urls\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set "Link to this definition")

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
> | [`3d_properties`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_3d_properties "mpl_toolkits.mplot3d.art3d.Path3DCollection.set_3d_properties") | float or array of floats |
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
> | [`depthshade`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_depthshade "mpl_toolkits.mplot3d.art3d.Path3DCollection.set_depthshade") | bool |
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
> | [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_paths "matplotlib.collections.Collection.set_paths") | unknown |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sizes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections._CollectionWithSizes.set_sizes "matplotlib.collections._CollectionWithSizes.set_sizes") | unknown |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`sort_zpos`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_sort_zpos "mpl_toolkits.mplot3d.art3d.Path3DCollection.set_sort_zpos") | unknown |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_3d\_properties(_zs_, _zdir_, _axlim\_clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L995-L1045)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_3d_properties "Link to this definition")

Set the _z_ positions and direction of the paths.

Parameters:

**zs**float or array of floats

The location or locations to place the paths in the collection along the _zdir_ axis.

**zdir**{'x', 'y', 'z'}

Plane to plot paths orthogonal to. All paths must have the same direction. See [`get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")
 for a description of the values.

**axlim\_clip**bool, default: False

Whether to hide paths with a vertex outside the axes view limits.

Added in version 3.10.

set\_depthshade(_depthshade_, _depthshade\_minalpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1060-L1082)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_depthshade "Link to this definition")

Set whether depth shading is performed on collection members.

Parameters:

**depthshade**bool

Whether to shade the patches in order to give the appearance of depth.

**depthshade\_minalpha**float

Sets the minimum alpha value used by depth-shading.

Added in version 3.11.

set\_linewidth(_lw_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1052-L1055)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_linewidth "Link to this definition")

Set the linewidth(s) for the collection. _lw_ can be a scalar or a sequence; if it is a sequence the patches will cycle through the sequence

Parameters:

**lw**float or list of floats

set\_sizes(_sizes_, _dpi\=72.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1047-L1050)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_sizes "Link to this definition")

Set the sizes of each member of the collection.

Parameters:

**sizes**[`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 or None

The size to set for each element of the collection. The value is the 'area' of the element.

**dpi**float, default: 72

The dpi of the canvas.

set\_sort\_zpos(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L990-L993)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection.set_sort_zpos "Link to this definition")

Set the position to use for z-sorting.

On this page