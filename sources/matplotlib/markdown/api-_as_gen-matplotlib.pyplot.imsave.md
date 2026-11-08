[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#main-content)

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
    

matplotlib.pyplot.imsave[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib-pyplot-imsave "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.imsave(_fname_, _arr_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2766-L2770)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib.pyplot.imsave "Link to this definition")

Colormap and save an array as an image file.

RGB(A) images are passed through. Single channel images will be colormapped according to _cmap_ and _norm_.

Note

If you want to save a single channel image as gray scale please use an image I/O library (such as pillow, tifffile, or imageio) directly.

Parameters:

**fname**str or path-like or file-like

A path or a file-like object to store the image in. If _format_ is not set, then the output format is inferred from the extension of _fname_, if any, and from `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`) otherwise. If _format_ is set, it determines the output format.

**arr**array-like

The image data. Accepts NumPy arrays or sequences (e.g., lists or tuples). The shape can be one of MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA).

**vmin, vmax**float, optional

_vmin_ and _vmax_ set the color scaling for the image by fixing the values that map to the colormap color limits. If either _vmin_ or _vmax_ is None, that limit is determined from the _arr_ min/max value.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

A Colormap instance or registered colormap name. The colormap maps scalar data to colors. It is ignored for RGB(A) data.

**format**str, optional

The file format, e.g. 'png', 'pdf', 'svg', ... The behavior when this is unset is documented under _fname_.

**origin**{'upper', 'lower'}, default: `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`)

Indicates whether the `(0, 0)` index of the array is in the upper left or lower left corner of the Axes.

**dpi**float

The DPI to store in the metadata of the file. This does not affect the resolution of the output image. Depending on file format, this may be rounded to the nearest integer.

**metadata**dict, optional

Metadata in the image file. The supported keys depend on the output format, see the documentation of the respective backends for more information. Currently only supported for "png", "pdf", "ps", "eps", and "svg".

**pil\_kwargs**dict, optional

Keyword arguments passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
. If the 'pnginfo' key is present, it completely overrides _metadata_, including the default 'Software' key.

Notes

Note

This is equivalent to [`matplotlib.image.imsave`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imsave "matplotlib.image.imsave")
.

On this page