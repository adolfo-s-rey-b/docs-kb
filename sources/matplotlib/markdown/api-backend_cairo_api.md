[Skip to main content](https://matplotlib.org/stable/api/backend_cairo_api.html#main-content)

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
    

`matplotlib.backends.backend_cairo`[#](https://matplotlib.org/stable/api/backend_cairo_api.html#module-matplotlib.backends.backend_cairo "Link to this heading")

=================================================================================================================================================================

A Cairo backend for Matplotlib[#](https://matplotlib.org/stable/api/backend_cairo_api.html#a-cairo-backend-for-matplotlib "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Author:

Steve Chaplin and others

This backend depends on cairocffi or pycairo.

matplotlib.backends.backend\_cairo.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L401-L521)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvas "Link to this definition")

alias of [`FigureCanvasCairo`](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo "matplotlib.backends.backend_cairo.FigureCanvasCairo")

class matplotlib.backends.backend\_cairo.FigureCanvasCairo(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L401-L521)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

copy\_from\_bbox(_bbox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L415-L432)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.copy_from_bbox "Link to this definition")

get\_renderer()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L412-L413)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.get_renderer "Link to this definition")

print\_pdf(_fobj_, _\*_, _orientation\='portrait'_)[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_pdf "Link to this definition")

print\_png(_fobj_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L448-L449)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_png "Link to this definition")

print\_ps(_fobj_, _\*_, _orientation\='portrait'_)[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_ps "Link to this definition")

print\_raw(_fobj_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L451-L455)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_raw "Link to this definition")

print\_rgba(_fobj_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L451-L455)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_rgba "Link to this definition")

print\_svg(_fobj_, _\*_, _orientation\='portrait'_)[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_svg "Link to this definition")

print\_svgz(_fobj_, _\*_, _orientation\='portrait'_)[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.print_svgz "Link to this definition")

restore\_region(_region_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L434-L446)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo.restore_region "Link to this definition")

class matplotlib.backends.backend\_cairo.GraphicsContextCairo(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L311-L392)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo "Link to this definition")

Bases: [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

get\_antialiased()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L340-L341)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.get_antialiased "Link to this definition")

Return whether the object should try to do antialiased rendering.

get\_rgb()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L383-L384)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.get_rgb "Link to this definition")

Return a tuple of three or four floats from 0-1.

restore()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L328-L329)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.restore "Link to this definition")

Restore the graphics context from the stack - needed only for backends that save graphics contexts on a stack.

set\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L331-L334)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_alpha "Link to this definition")

Set the alpha value used for blending - not supported on all backends.

If `alpha=None` (the default), the alpha components of the foreground and fill colors will be used to set their respective transparencies (where applicable); otherwise, `alpha` will override them.

set\_antialiased(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L336-L338)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_antialiased "Link to this definition")

Set whether object should be drawn with antialiased rendering.

set\_capstyle(_cs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L343-L345)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_capstyle "Link to this definition")

Set how to draw endpoints of lines.

Parameters:

**cs**[`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or {'butt', 'projecting', 'round'}

set\_clip\_path(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L356-L365)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_clip_path "Link to this definition")

Set the clip path to a [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")
 or None.

set\_clip\_rectangle(_rectangle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L347-L354)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_clip_rectangle "Link to this definition")

Set the clip rectangle to a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or None.

set\_dashes(_offset_, _dashes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L367-L374)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_dashes "Link to this definition")

Set the dash style for the gc.

Parameters:

**dash\_offset**float

Distance, in points, into the dash pattern at which to start the pattern. It is usually set to 0.

**dash\_list**array-like or None

The on-off sequence as points. None specifies a solid line. All values must otherwise be non-negative (\\(\\ge 0\\)).

Notes

See p. 666 of the PostScript [Language Reference](https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf)
 for more info.

set\_foreground(_fg_, _isRGBA\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L376-L381)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_foreground "Link to this definition")

Set the foreground color.

Parameters:

**fg**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

**isRGBA**bool

If _fg_ is known to be an `(r, g, b, a)` tuple, _isRGBA_ can be set to True to improve performance.

set\_joinstyle(_js_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L386-L388)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_joinstyle "Link to this definition")

Set how to draw connections between line segments.

Parameters:

**js**[`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 or {'miter', 'round', 'bevel'}

set\_linewidth(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L390-L392)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.GraphicsContextCairo.set_linewidth "Link to this definition")

Set the linewidth in points.

class matplotlib.backends.backend\_cairo.RendererCairo(_dpi_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L82-L308)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo "Link to this definition")

Bases: [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

draw\_image(_gc_, _x_, _y_, _im_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L204-L215)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.draw_image "Link to this definition")

Draw an RGBA image.

Parameters:

**gc**[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

A graphics context with clipping information.

**x**float

The distance in physical units (i.e., dots or pixels) from the left hand side of the canvas.

**y**float

The distance in physical units (i.e., dots or pixels) from the bottom side of the canvas.

**im**(N, M, 4) array of [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")

An array of RGBA pixels.

**transform**[`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

If and only if the concrete backend is written such that [`option_scale_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.option_scale_image "matplotlib.backend_bases.RendererBase.option_scale_image")
 returns `True`, an affine transformation (i.e., an [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")
) _may_ be passed to [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
. The translation vector of the transformation is given in physical units (i.e., dots or pixels). Note that the transformation does not override _x_ and _y_, and has to be applied _before_ translatingthe result by _x_ and _y_ (this can be accomplished by adding _x_ and _y_ to the translation vector defined by _transform_).

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L156-L202)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.draw_path "matplotlib.backends.backend_cairo.RendererCairo.draw_path")
. Backends may want to override this method in order to draw the marker only once and reuse it multiple times.

Parameters:

**gc**[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

The graphics context.

**marker\_path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

The path for the marker.

**marker\_trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

An affine transform applied to the marker.

**path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

The locations to draw the markers.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

An affine transform applied to the path.

**rgbFace**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L119-L154)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L217-L239)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.draw_text "Link to this definition")

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

get\_canvas\_width\_height()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L266-L268)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.get_canvas_width_height "Link to this definition")

Return the canvas width and height in display coords.

get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L270-L292)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.get_text_width_height_descent "Link to this definition")

Get the width, height, and descent (offset from the bottom to the baseline), in display coords, of the string _s_ with [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 _prop_.

Whitespace at the start and the end of _s_ is included in the reported width.

new\_gc()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L294-L304)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.new_gc "Link to this definition")

Return an instance of a [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
.

points\_to\_pixels(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L306-L308)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.points_to_pixels "Link to this definition")

Convert points to display units.

You need to override this function (unless your backend doesn't have a dpi, e.g., postscript or svg). Some imaging systems assume some value for pixels per inch:

points to pixels \= points \* pixels\_per\_inch/72 \* dpi/72

Parameters:

**points**float or array-like

Returns:

Points converted to pixels

set\_context(_ctx_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_cairo.py#L92-L108)
[#](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.RendererCairo.set_context "Link to this definition")

On this page