[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#main-content)

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
    

matplotlib.axes.Axes.pcolorfast[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib-axes-axes-pcolorfast "Link to this heading")

==========================================================================================================================================================================

Axes.pcolorfast(_\*args_, _alpha\=None_, _norm\=None_, _cmap\=None_, _vmin\=None_, _vmax\=None_, _colorizer\=None_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L6933-L7133)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "Link to this definition")

Create a pseudocolor plot with a non-regular rectangular grid.

Call signature:

ax.pcolorfast(\[X, Y\], C, /, \*\*kwargs)

The arguments _X_, _Y_, _C_ are positional-only.

This method is similar to [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
. It's designed to provide the fastest pcolor-type plotting with the Agg backend. To achieve this, it uses different algorithms internally depending on the complexity of the input grid (regular rectangular, non-regular rectangular or arbitrary quadrilateral).

Warning

This method is experimental. Compared to [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 or [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 it has some limitations:

*   It supports only flat shading (no outlines)
    
*   It lacks support for log scaling of the axes.
    
*   It does not have a pyplot wrapper.
    

Parameters:

**C**array-like

The image data. Supported array shapes are:

*   (M, N): an image with scalar data. Color-mapping is controlled by _cmap_, _norm_, _vmin_, and _vmax_.
    
*   (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
    
*   (M, N, 4): an image with RGBA values (0-1 float or 0-255 int), i.e. including transparency.
    

The first two dimensions (M, N) define the rows and columns of the image.

This parameter can only be passed positionally.

**X, Y**tuple or array-like, default: `(0, N)`, `(0, M)`

_X_ and _Y_ are used to specify the coordinates of the quadrilaterals. There are different ways to do this:

*   Use tuples `X=(xmin, xmax)` and `Y=(ymin, ymax)` to define a _uniform rectangular grid_.
    
    The tuples define the outer edges of the grid. All individual quadrilaterals will be of the same size. This is the fastest version.
    
*   Use 1D arrays _X_, _Y_ to specify a _non-uniform rectangular grid_.
    
    In this case _X_ and _Y_ have to be monotonic 1D arrays of length _N+1_ and _M+1_, specifying the x and y boundaries of the cells.
    
    The speed is intermediate. Note: The grid is checked, and if found to be uniform the fast version is used.
    
*   Use 2D arrays _X_, _Y_ if you need an _arbitrary quadrilateral grid_ (i.e. if the quadrilaterals are not rectangular).
    
    In this case _X_ and _Y_ are 2D arrays with shape (M + 1, N + 1), specifying the x and y coordinates of the corners of the colored quadrilaterals.
    
    This is the most general, but the slowest to render. It may produce faster and more compact output using ps, pdf, and svg backends, however.
    

These arguments can only be passed positionally.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

This parameter is ignored if _C_ is RGB(A).

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
    

This parameter is ignored if _C_ is RGB(A).

**vmin, vmax**float, optional

When using scalar data and no explicit _norm_, _vmin_ and _vmax_ define the data range that the colormap covers. By default, the colormap covers the complete value range of the supplied data. It is an error to use _vmin_/_vmax_ when a _norm_ instance is given (but using a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 _norm_ name together with _vmin_/_vmax_ is acceptable).

This parameter is ignored if _C_ is RGB(A).

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

This parameter is ignored if _C_ is RGB(A).

**alpha**float, default: None

The alpha blending value, between 0 (transparent) and 1 (opaque).

**snap**bool, default: False

Whether to snap the mesh to pixel boundaries.

Returns:

[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 or [`PcolorImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage "matplotlib.image.PcolorImage")
 or [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")

The return type depends on the type of grid:

*   [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
     for a regular rectangular grid.
    
*   [`PcolorImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage "matplotlib.image.PcolorImage")
     for a non-regular rectangular grid.
    
*   [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
     for a non-rectangular grid.
    

Other Parameters:

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

Supported additional parameters depend on the type of grid. See return types of _image_ for further description.

Examples using `matplotlib.axes.Axes.pcolorfast`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#examples-using-matplotlib-axes-axes-pcolorfast "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

On this page