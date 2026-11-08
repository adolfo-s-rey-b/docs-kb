[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.Poly3DCollection[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl-toolkits-mplot3d-art3d-poly3dcollection "Link to this heading")

===============================================================================================================================================================================================================

class mpl\_toolkits.mplot3d.art3d.Poly3DCollection(_verts_, _\*args_, _zsort\='average'_, _shade\=False_, _lightsource\=None_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1229-L1552)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "Link to this definition")

Bases: [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")

A collection of 3D polygons.

Note

**Filling of 3D polygons**

There is no simple definition of the enclosed surface of a 3D polygon unless the polygon is planar.

In practice, Matplotlib fills the 2D projection of the polygon. This gives a correct filling appearance only for planar polygons. For all other polygons, you'll find orientations in which the edges of the polygon intersect in the projection. This will lead to an incorrect visualization of the 3D area.

If you need filled areas, it is recommended to create them via [`plot_trisurf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf")
, which creates a triangulation and thus generates consistent surfaces.

Parameters:

**verts**list of (N, 3) array-like

The sequence of polygons \[_verts0_, _verts1_, ...\] where each element _verts\_i_ defines the vertices of polygon _i_ as a 2D array-like of shape (N, 3).

**zsort**{'average', 'min', 'max'}, default: 'average'

The calculation method for the z-order. See [`set_zsort`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_zsort "mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_zsort")
 for details.

**shade**bool, default: False

Whether to shade _facecolors_ and _edgecolors_. When activating _shade_, _facecolors_ and/or _edgecolors_ must be provided.

Added in version 3.7.

**lightsource**[`LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
, optional

The lightsource to use when _shade_ is True.

Added in version 3.7.

**axlim\_clip**bool, default: False

Whether to hide polygons with a vertex outside the view limits.

Added in version 3.10.

**\*args, \*\*kwargs**

All other parameters are forwarded to [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
.

Notes

Note that this class does a bit of magic with the \_facecolors and \_edgecolors properties.

do\_3d\_projection()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1412-L1511)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.do_3d_projection "Link to this definition")

Perform the 3D projection for this object.

get\_edgecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1546-L1552)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.get_edgecolor "Link to this definition")

get\_facecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1538-L1544)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.get_facecolor "Link to this definition")

get\_vector(_segments3d_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1334-L1336)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.get_vector "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.10:

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _array\=<UNSET>_, _capstyle\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _offset\_transform\=<UNSET>_, _offsets\=<UNSET>_, _path\_effects\=<UNSET>_, _paths\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sizes\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _sort\_zpos\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _urls\=<UNSET>_, _verts\=<UNSET>_, _verts\_and\_codes\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_, _zsort\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set "Link to this definition")

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
> | [`3d_properties`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_3d_properties "mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_3d_properties") | unknown |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | unknown |
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
> | [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | unknown |
> | [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | unknown |
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
> | [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts "matplotlib.collections.PolyCollection.set_verts") | list of array-like |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sizes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections._CollectionWithSizes.set_sizes "matplotlib.collections._CollectionWithSizes.set_sizes") | [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")<br> or None |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`sort_zpos`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_sort_zpos "mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_sort_zpos") | unknown |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
> | [`verts`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_verts "mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_verts") | list of (N, 3) array-like |
> | [`verts_and_codes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_verts_and_codes "mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_verts_and_codes") | unknown |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |
> | [`zsort`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_zsort "mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_zsort") | {'average', 'min', 'max'} |

set\_3d\_properties(_axlim\_clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1396-L1405)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_3d_properties "Link to this definition")

set\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1523-L1536)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_alpha "Link to this definition")

Set the alpha value used for blending - not supported on all backends.

Parameters:

**alpha**array-like or float or None

All values must be within the 0-1 range, inclusive. Masked values and nans are not supported.

set\_edgecolor(_colors_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1518-L1521)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_edgecolor "Link to this definition")

Set the edgecolor(s) of the collection.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or 'face'

The collection edgecolor(s). If a sequence, the patches cycle through it. If 'face', match the facecolor.

set\_facecolor(_colors_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1513-L1516)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_facecolor "Link to this definition")

Set the facecolor(s) of the collection. _c_ can be a color (all patches have same color), or a sequence of colors; if it is a sequence the patches will cycle through the sequence.

If _c_ is 'none', the patch will not be filled.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_sort\_zpos(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1407-L1410)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_sort_zpos "Link to this definition")

Set the position to use for z-sorting.

set\_verts(_verts_, _closed\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1369-L1386)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_verts "Link to this definition")

Set 3D vertices.

Parameters:

**verts**list of (N, 3) array-like

The sequence of polygons \[_verts0_, _verts1_, ...\] where each element _verts\_i_ defines the vertices of polygon _i_ as a 2D array-like of shape (N, 3).

**closed**bool, default: True

Whether the polygon should be closed by adding a CLOSEPOLY connection at the end.

set\_verts\_and\_codes(_verts_, _codes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1388-L1394)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_verts_and_codes "Link to this definition")

Set 3D vertices with path codes.

set\_zsort(_zsort_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1320-L1332)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection.set_zsort "Link to this definition")

Set the calculation method for the z-order.

Parameters:

**zsort**{'average', 'min', 'max'}

The function applied on the z-coordinates of the vertices in the viewer's coordinate system, to determine the z-order.

Examples using `mpl_toolkits.mplot3d.art3d.Poly3DCollection`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#examples-using-mpl-toolkits-mplot3d-art3d-poly3dcollection "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_custom_shaded_3d_surface_thumb.png)

[Custom hillshading in a 3D surface plot](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html)

Custom hillshading in a 3D surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_polys3d_thumb.png)

[Generate 3D polygons](https://matplotlib.org/stable/gallery/mplot3d/polys3d.html)

Generate 3D polygons

![](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_thumb.png)

[3D plots as subplots](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html)

3D plots as subplots

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_thumb.png)

[3D surface (colormap)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

3D surface (colormap)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_3_thumb.png)

[3D surface (checkerboard)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html)

3D surface (checkerboard)

On this page