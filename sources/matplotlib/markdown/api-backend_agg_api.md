[Skip to main content](https://matplotlib.org/stable/api/backend_agg_api.html#main-content)

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
    

`matplotlib.backends.backend_agg`[#](https://matplotlib.org/stable/api/backend_agg_api.html#module-matplotlib.backends.backend_agg "Link to this heading")

===========================================================================================================================================================

An [Anti-Grain Geometry](http://agg.sourceforge.net/antigrain.com)
 (AGG) backend.

Features that are implemented:

*   capstyles and join styles
    
*   dashes
    
*   linewidth
    
*   lines, rectangles, ellipses
    
*   clipping to a rectangle
    
*   output to RGBA and Pillow-supported image formats
    
*   alpha blending
    
*   DPI scaling properly - everything scales properly (dashes, linewidths, etc)
    
*   draw polygon
    
*   freetype2 w/ ft2font
    

Still TODO:

*   integrate screen dpi w/ ppi and text
    

matplotlib.backends.backend\_agg.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L418-L595)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvas "Link to this definition")

alias of [`FigureCanvasAgg`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")

class matplotlib.backends.backend\_agg.FigureCanvasAgg(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L418-L595)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

buffer\_rgba()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L461-L468)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.buffer_rgba "Link to this definition")

Get the image as a [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)")
 to the renderer's buffer.

[`draw`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.draw "matplotlib.backends.backend_agg.FigureCanvasAgg.draw")
 must be called at least once before this function will work and to update the renderer for any subsequent changes to the Figure.

copy\_from\_bbox(_bbox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L423-L425)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.copy_from_bbox "Link to this definition")

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L431-L441)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

get\_renderer()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L443-L450)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.get_renderer "Link to this definition")

print\_avif(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L569-L575)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_avif "Link to this definition")

Write the figure to a AVIF file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

print\_gif(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L549-L550)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_gif "Link to this definition")

Write the figure to a GIF file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

print\_jpeg(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L552-L557)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_jpeg "Link to this definition")

Write the figure to a JPEG file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

print\_jpg(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L552-L557)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_jpg "Link to this definition")

Write the figure to a JPEG file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

print\_png(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L490-L537)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_png "Link to this definition")

Write the figure to a PNG file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**dict, optional

Metadata in the PNG file as key-value pairs of bytes or latin-1 encodable strings. According to the PNG specification, keys must be shorter than 79 chars.

The [PNG specification](https://www.w3.org/TR/2003/REC-PNG-20031110/#11keywords)
 defines some common keywords that may be used as appropriate:

*   Title: Short (one line) title or caption for image.
    
*   Author: Name of image's creator.
    
*   Description: Description of image (possibly long).
    
*   Copyright: Copyright notice.
    
*   Creation Time: Time of original image creation (usually RFC 1123 format).
    
*   Software: Software used to create the image.
    
*   Disclaimer: Legal disclaimer.
    
*   Warning: Warning of nature of content.
    
*   Source: Device used to create the image.
    
*   Comment: Miscellaneous comment; conversion from other image format.
    

Other keywords may be invented for other purposes.

If 'Software' is not given, an autogenerated value for Matplotlib will be used. This can be removed by setting it to _None_.

For more details see the [PNG specification](https://www.w3.org/TR/2003/REC-PNG-20031110/#11keywords)
.

**pil\_kwargs**dict, optional

Keyword arguments passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
.

If the 'pnginfo' key is present, it completely overrides _metadata_, including the default 'Software' key.

print\_raw(_filename\_or\_obj_, _\*_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L470-L476)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_raw "Link to this definition")

print\_rgba(_filename\_or\_obj_, _\*_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L470-L476)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_rgba "Link to this definition")

print\_tif(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L561-L562)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_tif "Link to this definition")

Write the figure to a TIFF file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

print\_tiff(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L561-L562)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_tiff "Link to this definition")

Write the figure to a TIFF file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

print\_to\_buffer()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L539-L543)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_to_buffer "Link to this definition")

print\_webp(_filename\_or\_obj_, _\*_, _metadata\=None_, _pil\_kwargs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L566-L567)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_webp "Link to this definition")

Write the figure to a WebP file.

Parameters:

**filename\_or\_obj**str or path-like or file-like

The file to write to.

**metadata**None

Unused for pillow-based writers. All supported options can be passed via _pil\_kwargs_.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

restore\_region(_region_, _bbox\=None_, _xy\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L427-L429)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.restore_region "Link to this definition")

tostring\_argb()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L452-L459)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.tostring_argb "Link to this definition")

Get the image as ARGB [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")
.

[`draw`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.draw "matplotlib.backends.backend_agg.FigureCanvasAgg.draw")
 must be called at least once before this function will work and to update the renderer for any subsequent changes to the Figure.

class matplotlib.backends.backend\_agg.RendererAgg(_width_, _height_, _dpi_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L59-L415)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg "Link to this definition")

Bases: [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

The renderer handles all the drawing primitives using a graphics context instance that controls the colors/styles

buffer\_rgba()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L318-L319)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.buffer_rgba "Link to this definition")

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L324-L325)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.clear "Link to this definition")

draw\_mathtext(_gc_, _x_, _y_, _s_, _prop_, _angle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L225-L233)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.draw_mathtext "Link to this definition")

Draw mathtext using [`matplotlib.mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")
.

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L95-L173)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_tex(_gc_, _x_, _y_, _s_, _prop_, _angle_, _\*_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L271-L298)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.draw_tex "Link to this definition")

Draw a TeX instance.

Parameters:

**gc**[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

The graphics context.

**x**float

The x location of the text in display coords.

**y**float

The y location of the text baseline in display coords.

**s**str

The TeX text string.

**prop**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

The font properties.

**angle**float

The rotation angle in degrees anti-clockwise.

**mtext**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The original text object to be rendered.

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L235-L249)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.draw_text "Link to this definition")

Draw a text instance.

Parameters:

**gc**[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

The graphics context.

**x**float

The x location of the text in display coords.

**y**float

The y location of the text baseline in display coords.

**s**str

The text string.

**prop**[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

The font properties.

**angle**float

The rotation angle in degrees anti-clockwise.

**ismath**bool or "TeX"

If True, use mathtext parser.

**mtext**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The original text object to be rendered.

Notes

**Notes for backend implementers:**

[`RendererBase.draw_text`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_text "matplotlib.backend_bases.RendererBase.draw_text")
 also supports passing "TeX" to the _ismath_ parameter to use TeX rendering, but this is not required for actual rendering backends, and indeed many builtin backends do not support this. Rather, TeX rendering is provided by [`draw_tex`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_tex "matplotlib.backend_bases.RendererBase.draw_tex")
.

get\_canvas\_width\_height()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L300-L302)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.get_canvas_width_height "Link to this definition")

Return the canvas width and height in display coords.

get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L251-L269)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.get_text_width_height_descent "Link to this definition")

Get the width, height, and descent (offset from the bottom to the baseline), in display coords, of the string _s_ with [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 _prop_.

Whitespace at the start and the end of _s_ is included in the reported width.

option\_image\_nocomposite()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L327-L333)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.option_image_nocomposite "Link to this definition")

Return whether image composition by Matplotlib should be skipped.

Raster backends should usually return False (letting the C-level rasterizer take care of image composition); vector backends should usually return `not rcParams["image.composite_image"]`.

option\_scale\_image()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L335-L337)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.option_scale_image "Link to this definition")

Return whether arbitrary affine transformations in [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
 are supported (True for most vector backends).

points\_to\_pixels(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L314-L316)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.points_to_pixels "Link to this definition")

Convert points to display units.

You need to override this function (unless your backend doesn't have a dpi, e.g., postscript or svg). Some imaging systems assume some value for pixels per inch:

points to pixels \= points \* pixels\_per\_inch/72 \* dpi/72

Parameters:

**points**float or array-like

Returns:

Points converted to pixels

restore\_region(_region_, _bbox\=None_, _xy\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L339-L372)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.restore_region "Link to this definition")

Restore the saved region. If bbox (instance of BboxBase, or its extents) is given, only the region specified by the bbox will be restored. _xy_ (a pair of floats) optionally specifies the new position (the LLC of the original region, not the LLC of the bbox) where the region will be restored.

\>>> region \= renderer.copy\_from\_bbox()
\>>> x1, y1, x2, y2 \= region.get\_extents()
\>>> renderer.restore\_region(region, bbox\=(x1+dx, y1, x2, y2),
...                         xy\=(x1\-dx, y1))

start\_filter()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L374-L381)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.start_filter "Link to this definition")

Start filtering. It simply creates a new canvas (the old one is saved).

stop\_filter(_post\_processing_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L383-L415)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.stop_filter "Link to this definition")

Save the current canvas as an image and apply post processing.

The _post\_processing_ function:

def post\_processing(image, dpi):
  \# ny, nx, depth = image.shape
  \# image (numpy array) has RGBA channels and has a depth of 4.
  ...
  \# create a new\_image (numpy array of 4 channels, size can be
  \# different). The resulting image may have offsets from
  \# lower-left corner of the original image
  return new\_image, offset\_x, offset\_y

The saved renderer is restored and the returned image from post\_processing is plotted (using draw\_image) on it.

tostring\_argb()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L321-L322)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.tostring_argb "Link to this definition")

matplotlib.backends.backend\_agg.get\_hinting\_flag()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_agg.py#L43-L56)
[#](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.get_hinting_flag "Link to this definition")

On this page