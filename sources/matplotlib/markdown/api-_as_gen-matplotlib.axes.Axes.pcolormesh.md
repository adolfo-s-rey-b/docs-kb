[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#main-content)

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
    

matplotlib.axes.Axes.pcolormesh[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib-axes-axes-pcolormesh "Link to this heading")

==========================================================================================================================================================================

Axes.pcolormesh(_\*args_, _alpha\=None_, _norm\=None_, _cmap\=None_, _vmin\=None_, _vmax\=None_, _colorizer\=None_, _shading\=None_, _antialiased\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L6701-L6908)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "Link to this definition")

Create a pseudocolor plot with a non-regular rectangular grid.

Call signature:

pcolormesh(\[X, Y,\] C, /, \*\*kwargs)

_X_ and _Y_ can be used to specify the corners of the quadrilaterals.

The arguments _X_, _Y_, _C_ are positional-only.

Hint

[`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 is similar to [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
. It is much faster and preferred in most cases. For a detailed discussion on the differences see [Differences between pcolor() and pcolormesh()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#differences-pcolor-pcolormesh)
.

Parameters:

**C**array-like

The mesh data. Supported array shapes are:

*   (M, N) or M\*N: a mesh with scalar data. The values are mapped to colors using normalization and a colormap. See parameters _norm_, _cmap_, _vmin_, _vmax_.
    
*   (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
    
*   (M, N, 4): an image with RGBA values (0-1 float or 0-255 int), i.e. including transparency.
    

The first two dimensions (M, N) define the rows and columns of the mesh data.

**X, Y**array-like, optional

The coordinates of the corners of quadrilaterals of a pcolormesh:

(X\[i+1, j\], Y\[i+1, j\])       (X\[i+1, j+1\], Y\[i+1, j+1\])
                      ●╶───╴●
                      │     │
                      ●╶───╴●
    (X\[i, j\], Y\[i, j\])       (X\[i, j+1\], Y\[i, j+1\])

Note that the column index corresponds to the x-coordinate, and the row index corresponds to y. For details, see the [Notes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#axes-pcolormesh-grid-orientation)
 section below.

If `shading='flat'` the dimensions of _X_ and _Y_ should be one greater than those of _C_, otherwise a TypeError is raised. The quadrilateral is colored due to the value at `C[i, j]`.

If `shading='nearest'` or `'gouraud'`, the dimensions of _X_ and _Y_ should be the same as those of _C_ (if not, a TypeError will be raised). For `'nearest'` the color `C[i, j]` is centered on `(X[i, j], Y[i, j])`. For `'gouraud'`, a smooth interpolation is carried out between the quadrilateral corners.

If _X_ and/or _Y_ are 1-D arrays or column vectors they will be expanded as needed into the appropriate 2D arrays, making a rectangular grid.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

**norm**str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
, optional

The normalization method used to scale scalar data to the \[0, 1\] range before mapping to colors using _cmap_. By default, a linear scaling is used, mapping the lowest value to 0 and the highest to 1.

If given, this can be one of the following:

*   An instance of [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     or one of its subclasses (see [Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)
    ).
    
*   A scale name, i.e. one of "linear", "log", "symlog", "logit", etc. For a list of available scales, call [`matplotlib.scale.get_scale_names()`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.get_scale_names "matplotlib.scale.get_scale_names")
    . In that case, a suitable [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
     subclass is dynamically generated and instantiated.
    

**vmin, vmax**float, optional

When using scalar data and no explicit _norm_, _vmin_ and _vmax_ define the data range that the colormap covers. By default, the colormap covers the complete value range of the supplied data. It is an error to use _vmin_/_vmax_ when a _norm_ instance is given (but using a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 _norm_ name together with _vmin_/_vmax_ is acceptable).

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

**edgecolors**{'none', None, 'face', color, color sequence}, optional

The color of the edges. Defaults to 'none'. Possible values:

*   'none' or '': No edge.
    
*   _None_: `[rcParams["patch.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.edgecolor#rcparam-patch-edgecolor) ` (default: `'black'`) will be used. Note that currently `[rcParams["patch.force_edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.force_edgecolor#rcparam-patch-force-edgecolor) ` (default: `False`) has to be True for this to work.
    
*   'face': Use the adjacent face color.
    
*   A color or sequence of colors will set the edge color.
    

The singular form _edgecolor_ works as an alias.

**alpha**float, default: None

The alpha blending value, between 0 (transparent) and 1 (opaque).

**shading**{'flat', 'nearest', 'gouraud', 'auto'}, optional

The fill style for the quadrilateral; defaults to `[rcParams["pcolor.shading"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pcolor.shading#rcparam-pcolor-shading) ` (default: `'auto'`). Possible values:

*   'flat': A solid color is used for each quad. The color of the quad (i, j), (i+1, j), (i, j+1), (i+1, j+1) is given by `C[i, j]`. The dimensions of _X_ and _Y_ should be one greater than those of _C_.
    
*   'nearest': Each grid point will have a color centered on it, extending halfway between the adjacent grid centers. The dimensions of _X_ and _Y_ must be the same as _C_.
    
*   'gouraud': Each quad will be Gouraud shaded: The color of the corners (i', j') are given by `C[i', j']`. The color values of the area in between is interpolated from the corner values. The dimensions of _X_ and _Y_ must be the same as _C_. When Gouraud shading is used, _edgecolors_ is ignored.
    
*   'auto': Choose 'flat' if dimensions of _X_ and _Y_ are one larger than _C_. Choose 'nearest' if dimensions are the same.
    

See [pcolormesh grids and shading](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html)
 for more description.

**snap**bool, default: `[rcParams["pcolormesh.snap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pcolormesh.snap#rcparam-pcolormesh-snap) ` (default: `True`)

Whether to snap the mesh to pixel boundaries.

Changed in version 3.4.0: The default value changed from _False_ to _True_ to improve transparency handling. See [What's new in Matplotlib 3.4.0 (Mar 26, 2021)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#whats-new-3-4-0)
 for details.

**rasterized**bool, optional

Rasterize the pcolormesh when drawing vector graphics. This can speed up rendering and produce smaller files for large data sets. See also [Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)
.

Returns:

[`matplotlib.collections.QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")

Other Parameters:

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

Additionally, the following arguments are allowed. They are passed along to the [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 constructor:

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |
| [`array`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections._MeshData.set_array "matplotlib.collections._MeshData.set_array") | array-like |
| [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
| [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
| [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_color "matplotlib.collections.Collection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of RGBA tuples |
| [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |
| [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
| [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |
| [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |
| [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
| [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")

An alternative implementation with slightly different features. For a detailed discussion on the differences see [Differences between pcolor() and pcolormesh()](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#differences-pcolor-pcolormesh)
.

[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")

If _X_ and _Y_ are each equidistant, [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 can be a faster alternative.

Notes

**Masked arrays**

_C_ may be a masked array. If `C[i, j]` is masked, the corresponding quadrilateral will be transparent. Masking of _X_ and _Y_ is not supported. Use [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 if you need this functionality.

**Grid orientation**

The grid orientation follows the standard matrix convention: An array _C_ with shape (nrows, ncolumns) is plotted with the column number as _X_ and the row number as _Y_.

**Differences between pcolor() and pcolormesh()**

Both methods are used to create a pseudocolor plot of a 2D array using quadrilaterals.

The main difference lies in the created object and internal data handling: While [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 returns a [`PolyQuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyQuadMesh "matplotlib.collections.PolyQuadMesh")
, [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 returns a [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
. The latter is more specialized for the given purpose and thus is faster. It should almost always be preferred.

There is also a slight difference in the handling of masked arrays. Both [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 support masked arrays for _C_. However, only [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 supports masked arrays for _X_ and _Y_. The reason lies in the internal handling of the masked values. [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 leaves out the respective polygons from the PolyQuadMesh. [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 sets the facecolor of the masked elements to transparent. You can see the difference when using edgecolors. While all edges are drawn irrespective of masking in a QuadMesh, the edge between two adjacent masked quadrilaterals in [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 is not drawn as the corresponding polygons do not exist in the PolyQuadMesh. Because PolyQuadMesh draws each individual polygon, it also supports applying hatches and linestyles to the collection.

Another difference is the support of Gouraud shading in [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
, which is not available with [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
.

Examples using `matplotlib.axes.Axes.pcolormesh`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#examples-using-matplotlib-axes-axes-pcolormesh "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_grids_thumb.png)

[pcolormesh grids and shading](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html)

pcolormesh grids and shading

![](https://matplotlib.org/stable/_images/sphx_glr_quadmesh_demo_thumb.png)

[QuadMesh Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quadmesh_demo.html)

QuadMesh Demo

![](https://matplotlib.org/stable/_images/sphx_glr_time_series_histogram_thumb.png)

[Time Series Histogram](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html)

Time Series Histogram

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_thumb.png)

[pcolormesh(X, Y, Z)](https://matplotlib.org/stable/plot_types/arrays/pcolormesh.html)

pcolormesh(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_placement_thumb.png)

[Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)

Placing colorbars

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_thumb.png)

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html)

Creating Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page