[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html#main-content)

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
    

matplotlib.pyplot.figimage[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html#matplotlib-pyplot-figimage "Link to this heading")

===========================================================================================================================================================

matplotlib.pyplot.figimage(_X_, _xo\=0_, _yo\=0_, _alpha\=None_, _norm\=None_, _cmap\=None_, _vmin\=None_, _vmax\=None_, _origin\=None_, _resize\=False_, _\*_, _colorizer\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2890-L2919)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html#matplotlib.pyplot.figimage "Link to this definition")

Add a non-resampled image to the figure.

The image is attached to the lower or upper left corner depending on _origin_.

Parameters:

**X**

The image data. This is an array of one of the following shapes:

*   (M, N): an image with scalar data. Color-mapping is controlled by _cmap_, _norm_, _vmin_, and _vmax_.
    
*   (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
    
*   (M, N, 4): an image with RGBA values (0-1 float or 0-255 int), i.e. including transparency.
    

**xo, yo**int

The _x_/_y_ image offset in pixels.

**alpha**None or float

The alpha blending value.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

This parameter is ignored if _X_ is RGB(A).

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
    

This parameter is ignored if _X_ is RGB(A).

**vmin, vmax**float, optional

When using scalar data and no explicit _norm_, _vmin_ and _vmax_ define the data range that the colormap covers. By default, the colormap covers the complete value range of the supplied data. It is an error to use _vmin_/_vmax_ when a _norm_ instance is given (but using a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 _norm_ name together with _vmin_/_vmax_ is acceptable).

This parameter is ignored if _X_ is RGB(A).

**origin**{'upper', 'lower'}, default: `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`)

Indicates where the \[0, 0\] index of the array is in the upper left or lower left corner of the Axes.

**resize**bool

If _True_, resize the figure to match the given image size.

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

This parameter is ignored if _X_ is RGB(A).

Returns:

[`matplotlib.image.FigureImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "matplotlib.image.FigureImage")

Other Parameters:

**\*\*kwargs**

Additional kwargs are [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 kwargs passed on to [`FigureImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "matplotlib.image.FigureImage")
.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.figimage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage")
.

figimage complements the Axes image ([`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
) which will be resampled to fit the current Axes. If you want a resampled image to fill the entire figure, you can define an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 with extent \[0, 0, 1, 1\].

Examples

f \= plt.figure()
nx \= int(f.get\_figwidth() \* f.dpi)
ny \= int(f.get\_figheight() \* f.dpi)
data \= np.random.random((ny, nx))
f.figimage(data)
plt.show()

Examples using `matplotlib.pyplot.figimage`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html#examples-using-matplotlib-pyplot-figimage "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_figimage_demo_thumb.png)

[Figimage Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/figimage_demo.html)

Figimage Demo

On this page