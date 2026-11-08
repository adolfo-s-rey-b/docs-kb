[Skip to main content](https://matplotlib.org/stable/api/image_api.html#main-content)

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
    

`matplotlib.image`[#](https://matplotlib.org/stable/api/image_api.html#module-matplotlib.image "Link to this heading")

=======================================================================================================================

The image module supports basic image loading, rescaling and display operations.

class matplotlib.image.AxesImage(_ax_, _\*_, _cmap\=None_, _norm\=None_, _colorizer\=None_, _interpolation\=None_, _origin\=None_, _extent\=None_, _filternorm\=True_, _filterrad\=4.0_, _resample\=False_, _interpolation\_stage\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L850-L1035)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "Link to this definition")

Bases: `_ImageBase`

An image with pixels on a regular grid, attached to an Axes.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes the image will belong to.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

**norm**str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

Maps luminance to 0-1.

**interpolation**str, default: `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`)

Supported values are 'none', 'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'blackman'.

**interpolation\_stage**{'data', 'rgba'}, default: 'data'

If 'data', interpolation is carried out on the data provided by the user. If 'rgba', the interpolation is carried out after the colormapping has been applied (visual interpolation).

**origin**{'upper', 'lower'}, default: `[rcParams["image.origin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.origin#rcparam-image-origin) ` (default: `'upper'`)

Place the \[0, 0\] index of the array in the upper left or lower left corner of the Axes. The convention 'upper' is typically used for matrices and images.

**extent**tuple, optional

The data axes (left, right, bottom, top) for making image plots registered with data plots. Default is to label the pixel centers with the zero-based row and column indices.

**filternorm**bool, default: True

A parameter for the antigrain image resize filter (see the antigrain documentation). If filternorm is set, the filter normalizes integer values and corrects the rounding errors. It doesn't do anything with the source floating point values, it corrects only integers according to the rule of 1.0 which means that any sum of pixel weights must be equal to 1.0. So, the filter function must produce a graph of the proper shape.

**filterrad**float > 0, default: 4

The filter radius for filters that have a radius parameter, i.e. when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

**resample**bool, default: False

When True, use a full resampling method. When False, only resample when the output image is larger than the input image.

**\*\*kwargs**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 properties

Parameters:

**colorizer**[`colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")

get\_cursor\_data(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1010-L1035)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.get_cursor_data "Link to this definition")

Return the image value at the event position or _None_ if the event is outside the image.

See also

[`matplotlib.artist.Artist.get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib.artist.Artist.get_cursor_data "matplotlib.artist.Artist.get_cursor_data")

get\_extent()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L998-L1008)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.get_extent "Link to this definition")

Return the image extent as tuple (left, right, bottom, top).

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L929-L932)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.get_window_extent "Link to this definition")

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

make\_image(_renderer_, _magnification\=1.0_, _unsampled\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L934-L944)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.make_image "Link to this definition")

Normalize, rescale, and colormap this image's data for rendering using _renderer_, with the given _magnification_.

If _unsampled_ is True, the image will not be scaled, but an appropriate affine transformation will be returned instead.

Returns:

**image**(M, N, 4) [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 array

The RGBA image, resampled unless _unsampled_ is True.

**x, y**float

The upper left corner where the image should be drawn, in pixel space.

**trans**[`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

The affine transformation from image to pixel space.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _array\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _data\=<UNSET>_, _extent\=<UNSET>_, _filternorm\=<UNSET>_, _filterrad\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _interpolation\=<UNSET>_, _interpolation\_stage\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _resample\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.set "Link to this definition")

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
> | `alpha` | float or 2D array-like or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | `array` | array-like |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | `data` | array-like or [`PIL.Image.Image`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image "(in Pillow (PIL Fork) v12.3.0)") |
> | [`extent`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.set_extent "matplotlib.image.AxesImage.set_extent") | 4-tuple of float |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | `filternorm` | bool |
> | `filterrad` | positive float |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | `interpolation` | {'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'none'} or None |
> | `interpolation_stage` | {'data', 'rgba', 'auto'}, default: `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | `resample` | bool, default: `[rcParams["image.resample"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.resample#rcparam-image-resample) ` (default: `True`) |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_extent(_extent_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L950-L996)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.set_extent "Link to this definition")

Set the image extent.

Parameters:

**extent**4-tuple of float

The position and size of the image as tuple `(left, right, bottom, top)` in data coordinates.

**\*\*kwargs**

Other parameters from which unit info (i.e., the _xunits_, _yunits_, _zunits_ (for 3D Axes), _runits_ and _thetaunits_ (for polar Axes) entries are applied, if present.

Notes

This updates [`Axes.dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
, and, if autoscaling, sets [`Axes.viewLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
 to tightly fit the image, regardless of [`dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
. Autoscaling state is not changed, so a subsequent call to [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
 will redo the autoscaling in accord with [`dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
.

class matplotlib.image.BboxImage(_bbox_, _\*_, _cmap\=None_, _norm\=None_, _colorizer\=None_, _interpolation\=None_, _origin\=None_, _filternorm\=True_, _filterrad\=4.0_, _resample\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1417-L1519)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "Link to this definition")

Bases: `_ImageBase`

The Image class whose size is determined by the given bbox.

Parameters:

**bbox**BboxBase or Callable\[RendererBase, BboxBase\]

The bbox or a function to generate the bbox

Warning

If using [`matplotlib.artist.Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
 as the callable ensure that the other artist is drawn first (lower zorder) or you may need to renderer the figure twice to ensure that the computed bbox is accurate.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors. This parameter is ignored if X is RGB(A).

**norm**str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

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

**\*\*kwargs**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 properties

Parameters:

**colorizer**[`colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1501-L1507)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage.contains "Link to this definition")

Test whether the mouse event occurred within the image.

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1491-L1499)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage.get_window_extent "Link to this definition")

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

make\_image(_renderer_, _magnification\=1.0_, _unsampled\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1509-L1519)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage.make_image "Link to this definition")

Normalize, rescale, and colormap this image's data for rendering using _renderer_, with the given _magnification_.

If _unsampled_ is True, the image will not be scaled, but an appropriate affine transformation will be returned instead.

Returns:

**image**(M, N, 4) [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 array

The RGBA image, resampled unless _unsampled_ is True.

**x, y**float

The upper left corner where the image should be drawn, in pixel space.

**trans**[`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

The affine transformation from image to pixel space.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _array\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _data\=<UNSET>_, _filternorm\=<UNSET>_, _filterrad\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _interpolation\=<UNSET>_, _interpolation\_stage\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _resample\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage.set "Link to this definition")

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
> | `alpha` | float or 2D array-like or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | `array` | array-like |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | `data` | array-like or [`PIL.Image.Image`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image "(in Pillow (PIL Fork) v12.3.0)") |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | `filternorm` | bool |
> | `filterrad` | positive float |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | `interpolation` | {'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'none'} or None |
> | `interpolation_stage` | {'data', 'rgba', 'auto'}, default: `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | `resample` | bool, default: `[rcParams["image.resample"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.resample#rcparam-image-resample) ` (default: `True`) |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.image.FigureImage(_fig_, _\*_, _cmap\=None_, _norm\=None_, _colorizer\=None_, _offsetx\=0_, _offsety\=0_, _origin\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1351-L1414)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "Link to this definition")

Bases: `_ImageBase`

An image attached to a figure.

cmap is a colors.Colormap instance norm is a colors.Normalize instance to map luminance to 0-1

kwargs are an optional list of Artist keyword args

get\_extent()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1387-L1391)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage.get_extent "Link to this definition")

Return the image extent as tuple (left, right, bottom, top).

make\_image(_renderer_, _magnification\=1.0_, _unsampled\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1393-L1409)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage.make_image "Link to this definition")

Normalize, rescale, and colormap this image's data for rendering using _renderer_, with the given _magnification_.

If _unsampled_ is True, the image will not be scaled, but an appropriate affine transformation will be returned instead.

Returns:

**image**(M, N, 4) [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 array

The RGBA image, resampled unless _unsampled_ is True.

**x, y**float

The upper left corner where the image should be drawn, in pixel space.

**trans**[`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

The affine transformation from image to pixel space.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _array\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _data\=<UNSET>_, _filternorm\=<UNSET>_, _filterrad\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _interpolation\=<UNSET>_, _interpolation\_stage\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _resample\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage.set "Link to this definition")

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
> | `alpha` | float or 2D array-like or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | `array` | array-like |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`data`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage.set_data "matplotlib.image.FigureImage.set_data") | unknown |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | `filternorm` | bool |
> | `filterrad` | positive float |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | `interpolation` | {'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'none'} or None |
> | `interpolation_stage` | {'data', 'rgba', 'auto'}, default: `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | `resample` | bool, default: `[rcParams["image.resample"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.resample#rcparam-image-resample) ` (default: `True`) |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_data(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1411-L1414)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage.set_data "Link to this definition")

Set the image array.

zorder \= 0[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage.zorder "Link to this definition")

class matplotlib.image.NonUniformImage(_ax_, _\*_, _interpolation\='nearest'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1038-L1211)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "Link to this definition")

Bases: [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

An image with pixels on a rectilinear grid.

In contrast to [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, where pixels are on a regular grid, NonUniformImage allows rows and columns with individual heights / widths.

See also [Image nonuniform](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html)
.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes the image will belong to.

**interpolation**{'nearest', 'bilinear'}, default: 'nearest'

The interpolation scheme used in the resampling.

**\*\*kwargs**

All other keyword arguments are identical to those of [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
.

get\_cursor\_data(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1203-L1211)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.get_cursor_data "Link to this definition")

Return the image value at the event position or _None_ if the event is outside the image.

See also

[`matplotlib.artist.Artist.get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib.artist.Artist.get_cursor_data "matplotlib.artist.Artist.get_cursor_data")

get\_extent()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1182-L1185)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.get_extent "Link to this definition")

Return the image extent as tuple (left, right, bottom, top).

make\_image(_renderer_, _magnification\=1.0_, _unsampled\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1066-L1141)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.make_image "Link to this definition")

Normalize, rescale, and colormap this image's data for rendering using _renderer_, with the given _magnification_.

If _unsampled_ is True, the image will not be scaled, but an appropriate affine transformation will be returned instead.

Returns:

**image**(M, N, 4) [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 array

The RGBA image, resampled unless _unsampled_ is True.

**x, y**float

The upper left corner where the image should be drawn, in pixel space.

**trans**[`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

The affine transformation from image to pixel space.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _array\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _data\=<UNSET>_, _extent\=<UNSET>_, _filternorm\=<UNSET>_, _filterrad\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _interpolation\=<UNSET>_, _interpolation\_stage\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _resample\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set "Link to this definition")

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
> | `alpha` | float or 2D array-like or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | `array` | unknown |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | unknown |
> | [`data`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_data "matplotlib.image.NonUniformImage.set_data") | unknown |
> | [`extent`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.set_extent "matplotlib.image.AxesImage.set_extent") | 4-tuple of float |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | `filternorm` | unknown |
> | `filterrad` | unknown |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`interpolation`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_interpolation "matplotlib.image.NonUniformImage.set_interpolation") | {'nearest', 'bilinear'} or None |
> | `interpolation_stage` | {'data', 'rgba', 'auto'}, default: `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | `resample` | bool, default: `[rcParams["image.resample"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.resample#rcparam-image-resample) ` (default: `True`) |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_array(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1167-L1168)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_array "Link to this definition")

Retained for backwards compatibility - use set\_data instead.

Parameters:

**A**array-like

set\_cmap(_cmap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1198-L1201)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_cmap "Link to this definition")

Set the colormap for luminance data.

Parameters:

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 or str or None

set\_data(_x_, _y_, _A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1143-L1165)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_data "Link to this definition")

Set the grid for the pixel centers, and the pixel values.

Parameters:

**x, y**1D array-like

Monotonic arrays of shapes (N,) and (M,), respectively, specifying pixel centers.

**A**array-like

(M, N) [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 or masked array of values to be colormapped, or (M, N, 3) RGB array, or (M, N, 4) RGBA array.

set\_filternorm(_filternorm_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1187-L1188)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_filternorm "Link to this definition")

Set whether the resize filter normalizes the weights.

See help for [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

Parameters:

**filternorm**bool

set\_filterrad(_filterrad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1190-L1191)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_filterrad "Link to this definition")

Set the resize filter radius (only applicable to some interpolation schemes).

See help for [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

Parameters:

**filterrad**positive float

set\_interpolation(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1170-L1180)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_interpolation "Link to this definition")

Parameters:

**s**{'nearest', 'bilinear'} or None

If None, use `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`).

set\_norm(_norm_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1193-L1196)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_norm "Link to this definition")

Set the normalization instance.

Parameters:

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 or str or None

Notes

If there are any colorbars using the mappable for this norm, setting the norm of the mappable will reset the norm, locator, and formatters on the colorbar to default.

class matplotlib.image.PcolorImage(_ax_, _x\=None_, _y\=None_, _A\=None_, _\*_, _cmap\=None_, _norm\=None_, _colorizer\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1214-L1348)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage "Link to this definition")

Bases: [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

Make a pcolor-style plot with an irregular rectangular grid.

This uses a variation of the original irregular image code, and it is used by pcolorfast for the corresponding grid type.

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes the image will belong to.

**x, y**1D array-like, optional

Monotonic arrays of length N+1 and M+1, respectively, specifying rectangle boundaries. If not given, will default to `range(N + 1)` and `range(M + 1)`, respectively.

**A**array-like

The data to be color-coded. The interpretation depends on the shape:

*   (M, N) [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     or masked array: values to be colormapped
    
*   (M, N, 3): RGB array
    
*   (M, N, 4): RGBA array
    

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The Colormap instance or registered colormap name used to map scalar data to colors.

**norm**str or [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

Maps luminance to 0-1.

**\*\*kwargs**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 properties

get\_cursor\_data(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1340-L1348)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage.get_cursor_data "Link to this definition")

Return the image value at the event position or _None_ if the event is outside the image.

See also

[`matplotlib.artist.Artist.get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib.artist.Artist.get_cursor_data "matplotlib.artist.Artist.get_cursor_data")

make\_image(_renderer_, _magnification\=1.0_, _unsampled\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1261-L1294)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage.make_image "Link to this definition")

Normalize, rescale, and colormap this image's data for rendering using _renderer_, with the given _magnification_.

If _unsampled_ is True, the image will not be scaled, but an appropriate affine transformation will be returned instead.

Returns:

**image**(M, N, 4) [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 array

The RGBA image, resampled unless _unsampled_ is True.

**x, y**float

The upper left corner where the image should be drawn, in pixel space.

**trans**[`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

The affine transformation from image to pixel space.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _array\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _data\=<UNSET>_, _extent\=<UNSET>_, _filternorm\=<UNSET>_, _filterrad\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _interpolation\=<UNSET>_, _interpolation\_stage\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _resample\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage.set "Link to this definition")

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
> | `alpha` | float or 2D array-like or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | `array` | unknown |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`data`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage.set_data "matplotlib.image.PcolorImage.set_data") | unknown |
> | [`extent`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.set_extent "matplotlib.image.AxesImage.set_extent") | 4-tuple of float |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | `filternorm` | bool |
> | `filterrad` | positive float |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | `interpolation` | {'auto', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'none'} or None |
> | `interpolation_stage` | {'data', 'rgba', 'auto'}, default: `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | `resample` | bool, default: `[rcParams["image.resample"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.resample#rcparam-image-resample) ` (default: `True`) |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_array(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1337-L1338)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage.set_array "Link to this definition")

Retained for backwards compatibility - use set\_data instead.

Parameters:

**A**array-like

set\_data(_x_, _y_, _A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1299-L1335)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage.set_data "Link to this definition")

Set the grid for the rectangle boundaries, and the data values.

Parameters:

**x, y**1D array-like, optional

Monotonic arrays of length N+1 and M+1, respectively, specifying rectangle boundaries. If not given, will default to `range(N + 1)` and `range(M + 1)`, respectively.

**A**array-like

The data to be color-coded. The interpretation depends on the shape:

*   (M, N) [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     or masked array: values to be colormapped
    
*   (M, N, 3): RGB array
    
*   (M, N, 4): RGBA array
    

matplotlib.image.composite\_images(_images_, _renderer_, _magnification\=1.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L59-L112)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.composite_images "Link to this definition")

Composite a number of RGBA images into one. The images are composited in the order in which they appear in the _images_ list.

Parameters:

**images**list of Images

Each must have a `make_image` method. For each image, `can_composite` should return [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, though this is not enforced by this function. Each image must have a purely affine transformation with no shear.

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

**magnification**float, default: 1

The additional magnification to apply for the renderer in use.

Returns:

**image**(M, N, 4) [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 array

The composited RGBA image.

**offset\_x, offset\_y**float

The (left, bottom) offset where the composited image should be placed in the output figure.

matplotlib.image.imread(_fname_, _format\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1522-L1597)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imread "Link to this definition")

Read an image from a file into an array.

Note

This function exists for historical reasons. It is recommended to use [`PIL.Image.open`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "(in Pillow (PIL Fork) v12.3.0)")
 instead for loading images.

Parameters:

**fname**str or file-like

The image file to read: a filename, a URL or a file-like object opened in read-binary mode.

Passing a URL is deprecated. Please open the URL for reading and pass the result to Pillow, e.g. with `np.array(PIL.Image.open(urllib.request.urlopen(url)))`.

**format**str, optional

The image file format assumed for reading the data. The image is loaded as a PNG file if _format_ is set to "png", if _fname_ is a path or opened file with a ".png" extension, or if it is a URL. In all other cases, _format_ is ignored and the format is auto-detected by [`PIL.Image.open`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "(in Pillow (PIL Fork) v12.3.0)")
.

Returns:

[`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")

The image data. The returned array has shape

*   (M, N) for grayscale images.
    
*   (M, N, 3) for RGB images.
    
*   (M, N, 4) for RGBA images.
    

PNG images are returned as float arrays (0-1). All other formats are returned as int arrays, with a bit depth determined by the file's contents.

matplotlib.image.imsave(_fname_, _arr_, _vmin\=None_, _vmax\=None_, _cmap\=None_, _format\=None_, _origin\=None_, _dpi\=100_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1600-L1729)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imsave "Link to this definition")

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

matplotlib.image.pil\_to\_array(_pilImage_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1732-L1764)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.pil_to_array "Link to this definition")

Load a [PIL image](https://pillow.readthedocs.io/en/latest/reference/Image.html)
 and return it as a numpy int array.

Returns:

numpy.array

The array shape depends on the image type:

*   (M, N) for grayscale images.
    
*   (M, N, 3) for RGB images.
    
*   (M, N, 4) for RGBA images.
    

matplotlib.image.thumbnail(_infile_, _thumbfile_, _scale\=0.1_, _interpolation\='bilinear'_, _preview\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/image.py#L1797-L1860)
[#](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.thumbnail "Link to this definition")

\[_Deprecated_\] Make a thumbnail of image in _infile_ with output filename _thumbfile_.

See [Pillow for a replacement](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#create-jpeg-thumbnails)
.

Parameters:

**infile**str or file-like

The image file. Matplotlib relies on [Pillow](https://python-pillow.github.io/)
 for image reading, and thus supports a wide range of file formats, including PNG, JPG, TIFF and others.

**thumbfile**str or file-like

The thumbnail filename.

**scale**float, default: 0.1

The scale factor for the thumbnail.

**interpolation**str, default: 'bilinear'

The interpolation scheme used in the resampling. See the _interpolation_ parameter of [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 for possible values.

**preview**bool, default: False

If True, the default backend (presumably a user interface backend) will be used which will cause a figure to be raised if [`show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
 is called. If it is False, the figure is created using [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 and the drawing backend is selected as [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 would normally do.

Returns:

[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure instance containing the thumbnail.

Notes

Deprecated since version 3.11: Use Pillow's [`PIL.Image.Image.thumbnail`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail "(in Pillow (PIL Fork) v12.3.0)")
 instead.

On this page