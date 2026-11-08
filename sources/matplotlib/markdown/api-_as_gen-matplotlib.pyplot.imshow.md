[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#main-content)

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
    

matplotlib.pyplot.imshow[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib-pyplot-imshow "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.imshow(_X_, _cmap\=None_, _norm\=None_, _\*_, _aspect\=None_, _interpolation\=None_, _alpha\=None_, _vmin\=None_, _vmax\=None_, _colorizer\=None_, _origin\=None_, _extent\=None_, _interpolation\_stage\=None_, _filternorm\=True_, _filterrad\=4.0_, _resample\=None_, _url\=None_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3762-L3805)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "Link to this definition")

Display data as an image, i.e., on a 2D regular raster.

The input may either be actual RGB(A) data, or 2D scalar data, which will be rendered as a pseudocolor image. For displaying a grayscale image, set up the colormapping using the parameters `cmap='gray', vmin=0, vmax=255`.

The number of pixels used to render an image is set by the Axes size and the figure _dpi_. This can lead to aliasing artifacts when the image is resampled, because the displayed image size will usually not match the size of _X_ (see [Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)
). The resampling can be controlled via the _interpolation_ parameter and/or `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`).

Parameters:

**X**array-like or PIL image

The image data. Supported array shapes are:

*   (M, N): an image with scalar data. The values are mapped to colors using normalization and a colormap. See parameters _norm_, _cmap_, _vmin_, _vmax_.
    
*   (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
    
*   (M, N, 4): an image with RGBA values (0-1 float or 0-255 int), i.e. including transparency.
    

The first two dimensions (M, N) define the rows and columns of the image.

Out-of-range RGB(A) values are clipped.

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

**colorizer**[`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 or None, default: None

The Colorizer object used to map color to data. If None, a Colorizer object is created from a _norm_ and _cmap_.

This parameter is ignored if _X_ is RGB(A).

**aspect**{'equal', 'auto'} or float or None, default: None

The aspect ratio of the Axes. This parameter is particularly relevant for images since it determines whether data pixels are square.

This parameter is a shortcut for explicitly calling [`Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
. See there for further details.

*   'equal': Ensures an aspect ratio of 1. Pixels will be square (unless pixel sizes are explicitly made non-square in data coordinates using _extent_).
    
*   'auto': The Axes is kept fixed and the aspect is adjusted so that the data fit in the Axes. In general, this will result in non-square pixels.
    

Normally, None (the default) means to use `[rcParams["image.aspect"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.aspect#rcparam-image-aspect) ` (default: `'equal'`). However, if the image uses a transform that does not contain the axes data transform, then None means to not modify the axes aspect at all (in that case, directly call [`Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
 if desired).

**interpolation**str, default: `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`)

The interpolation method used.

Supported values are 'none', 'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'blackman'.

The data _X_ is resampled to the pixel size of the image on the figure canvas, using the interpolation method to either up- or downsample the data.

If _interpolation_ is 'none', then for the ps, pdf, and svg backends no down- or upsampling occurs, and the image data is passed to the backend as a native image. Note that different ps, pdf, and svg viewers may display these raw pixels differently. On other backends, 'none' is the same as 'nearest'.

If _interpolation_ is the default 'auto', then 'nearest' interpolation is used if the image is upsampled by more than a factor of three (i.e. the number of display pixels is at least three times the size of the data array). If the upsampling rate is smaller than 3, or the image is downsampled, then 'hanning' interpolation is used to act as an anti-aliasing filter, unless the image happens to be upsampled by exactly a factor of two or one.

See [Interpolations for imshow](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html)
 for an overview of the supported interpolation methods, and [Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)
 for a discussion of image antialiasing.

Some interpolation methods require an additional radius parameter, which can be set by _filterrad_. Additionally, the antigrain image resize filter is controlled by the parameter _filternorm_.

**interpolation\_stage**{'auto', 'data', 'rgba'}, default: 'auto'

Supported values:

*   'data': Interpolation is carried out on the data provided by the user This is useful if interpolating between pixels during upsampling.
    
*   'rgba': The interpolation is carried out in RGBA-space after the color-mapping has been applied. This is useful if downsampling and combining pixels visually.
    
*   'auto': Select a suitable interpolation stage automatically. This uses 'rgba' when downsampling, or upsampling at a rate less than 3, and 'data' when upsampling at a higher rate.
    

See [Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)
 for a discussion of image antialiasing.

**alpha**float or array-like, optional

The alpha blending value, between 0 (transparent) and 1 (opaque). If _alpha_ is an array, the alpha blending values are applied pixel by pixel, and _alpha_ must have the same shape as _X_.

**origin**{'upper', 'lower'}, default: `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`)

Place the \[0, 0\] index of the array in the upper left or lower left corner of the Axes. The convention (the default) 'upper' is typically used for matrices and images.

Note that the vertical axis points upward for 'lower' but downward for 'upper'.

See the [Positioning and orientation of imshow images](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#imshow-extent)
 tutorial for examples and a more detailed description.

**extent**floats (left, right, bottom, top), optional

The bounding box in data coordinates that the image will fill. These values may be unitful and match the units of the Axes. The image is stretched individually along x and y to fill the box.

The default extent is determined by the following conditions. Pixels have unit size in data coordinates. Their centers are on integer coordinates, and their center coordinates range from 0 to columns-1 horizontally and from 0 to rows-1 vertically.

Note that the direction of the vertical axis and thus the default values for top and bottom depend on _origin_:

*   For `origin == 'upper'` the default is `(-0.5, numcols-0.5, numrows-0.5, -0.5)`.
    
*   For `origin == 'lower'` the default is `(-0.5, numcols-0.5, -0.5, numrows-0.5)`.
    

See the [Positioning and orientation of imshow images](https://matplotlib.org/stable/users/explain/artists/imshow_extent.html#imshow-extent)
 tutorial for examples and a more detailed description.

**filternorm**bool, default: True

A parameter for the antigrain image resize filter (see the antigrain documentation). If _filternorm_ is set, the filter normalizes integer values and corrects the rounding errors. It doesn't do anything with the source floating point values, it corrects only integers according to the rule of 1.0 which means that any sum of pixel weights must be equal to 1.0. So, the filter function must produce a graph of the proper shape.

**filterrad**float > 0, default: 4.0

The filter radius for filters that have a radius parameter, i.e. when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

**resample**bool, default: `[rcParams["image.resample"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.resample#rcparam-image-resample) ` (default: `True`)

When _True_, use a full resampling method. When _False_, only resample when the output image is larger than the input image.

**url**str, optional

Set the url of the created [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
. See [`Artist.set_url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url")
.

Returns:

[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

Other Parameters:

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 properties

These parameters are passed on to the constructor of the [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 artist.

See also

[`matshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")

Plot a matrix or an array as an image.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

Unless _extent_ is used, pixel centers will be located at integer coordinates. In other words: the origin will coincide with the center of pixel (0, 0).

There are two common representations for RGB images with an alpha channel:

*   Straight (unassociated) alpha: R, G, and B channels represent the color of the pixel, disregarding its opacity.
    
*   Premultiplied (associated) alpha: R, G, and B channels represent the color of the pixel, adjusted for its opacity by multiplication.
    

[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
 expects RGB images adopting the straight (unassociated) alpha representation.

Examples using `matplotlib.pyplot.imshow`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#examples-using-matplotlib-pyplot-imshow "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_image_demo_thumb.png)

[Many ways to plot images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html)

Many ways to plot images

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_multi_image_thumb.png)

[Multiple images with one colorbar](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html)

Multiple images with one colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_interpolation_methods_thumb.png)

[Interpolations for imshow](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html)

Interpolations for imshow

![](https://matplotlib.org/stable/_images/sphx_glr_layer_images_thumb.png)

[Layer images with alpha blending](https://matplotlib.org/stable/gallery/images_contours_and_fields/layer_images.html)

Layer images with alpha blending

![](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_thumb.png)

[Blend transparency with color in 2D images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html)

Blend transparency with color in 2D images

![](https://matplotlib.org/stable/_images/sphx_glr_shading_example_thumb.png)

[Shading example](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html)

Shading example

![](https://matplotlib.org/stable/_images/sphx_glr_image_clip_path_thumb.png)

[Clipping images with patches](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html)

Clipping images with patches

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_affine_image_thumb.png)

[Affine transform of an image](https://matplotlib.org/stable/gallery/images_contours_and_fields/affine_image.html)

Affine transform of an image

![](https://matplotlib.org/stable/_images/sphx_glr_matshow_thumb.png)

[Visualize matrices with matshow](https://matplotlib.org/stable/gallery/images_contours_and_fields/matshow.html)

Visualize matrices with matshow

![](https://matplotlib.org/stable/_images/sphx_glr_barcode_demo_thumb.png)

[Barcode](https://matplotlib.org/stable/gallery/images_contours_and_fields/barcode_demo.html)

Barcode

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_adjust_thumb.png)

[Subplots spacings and margins](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_adjust.html)

Subplots spacings and margins

![](https://matplotlib.org/stable/_images/sphx_glr_dolphin_thumb.png)

[Dolphins](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html)

Dolphins

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_basics_thumb.png)

[Colorbar](https://matplotlib.org/stable/gallery/color/colorbar_basics.html)

Colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_hyperlinks_sgskip_thumb.png)

[Hyperlinks](https://matplotlib.org/stable/gallery/misc/hyperlinks_sgskip.html)

Hyperlinks

![](https://matplotlib.org/stable/_images/sphx_glr_images_thumb.png)

[Image tutorial](https://matplotlib.org/stable/tutorials/images.html)

Image tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page