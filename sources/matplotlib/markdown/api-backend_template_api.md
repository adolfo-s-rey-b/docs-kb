[Skip to main content](https://matplotlib.org/stable/api/backend_template_api.html#main-content)

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
    

`matplotlib.backends.backend_template`[#](https://matplotlib.org/stable/api/backend_template_api.html#module-matplotlib.backends.backend_template "Link to this heading")

==========================================================================================================================================================================

A fully functional, do-nothing backend intended as a template for backend writers. It is fully functional in that you can select it as a backend e.g. with

import matplotlib
matplotlib.use("template")

and your program will (should!) run without error, though no output is produced. This provides a starting point for backend writers; you can selectively implement drawing methods ([`draw_path`](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.draw_path "matplotlib.backends.backend_template.RendererTemplate.draw_path")
, [`draw_image`](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.draw_image "matplotlib.backends.backend_template.RendererTemplate.draw_image")
, etc.) and slowly see your figure come to life instead having to have a full-blown implementation before getting any results.

Copy this file to a directory outside the Matplotlib source tree, somewhere where Python can import it (by adding the directory to your `sys.path` or by packaging it as a normal Python package); if the backend is importable as `import my.backend` you can then select it using

import matplotlib
matplotlib.use("module://my.backend")

If your backend implements support for saving figures (i.e. has a `print_xyz` method), you can register it as the default handler for a given file type:

from matplotlib.backend\_bases import register\_backend
register\_backend('xyz', 'my\_backend', 'XYZ File Format')
...
plt.savefig("figure.xyz")

matplotlib.backends.backend\_template.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L149-L203)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvas "Link to this definition")

alias of [`FigureCanvasTemplate`](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate "matplotlib.backends.backend_template.FigureCanvasTemplate")

class matplotlib.backends.backend\_template.FigureCanvasTemplate(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L149-L203)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

The canvas the figure renders into. Calls the draw and print fig methods, creates the renderers, etc.

Note: GUI templates will want to connect events for button presses, mouse movements and key presses to functions that call the base class methods button\_press\_event, button\_release\_event, motion\_notify\_event, key\_press\_event, and key\_release\_event. See the implementations of the interactive backends for examples.

Attributes:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

A high-level Figure instance

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L171-L181)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate.draw "Link to this definition")

Draw the figure using the renderer.

It is important that this method actually walk the artist tree even if not output is produced because this will trigger deferred work (like computing limits auto-limits and tick values) that users may want access to before saving to disk.

filetypes \= {'avif': 'AV1 Image File Format', 'eps': 'Encapsulated Postscript', 'foo': 'My magic Foo format', 'gif': 'Graphics Interchange Format', 'jpeg': 'Joint Photographic Experts Group', 'jpg': 'Joint Photographic Experts Group', 'pdf': 'Portable Document Format', 'pgf': 'PGF code for LaTeX', 'png': 'Portable Network Graphics', 'ps': 'Postscript', 'raw': 'Raw RGBA bitmap', 'rgba': 'Raw RGBA bitmap', 'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics', 'tif': 'Tagged Image File Format', 'tiff': 'Tagged Image File Format', 'webp': 'WebP Image Format'}[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate.filetypes "Link to this definition")

get\_default\_filetype()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L202-L203)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate.get_default_filetype "Link to this definition")

Return the default savefig file format as specified in `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

The returned string does not include a period. This method is overridden in backends that only support a single file type.

manager\_class[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L139-L146)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate.manager_class "Link to this definition")

alias of [`FigureManagerTemplate`](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureManagerTemplate "matplotlib.backends.backend_template.FigureManagerTemplate")

print\_foo(_filename_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L190-L200)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate.print_foo "Link to this definition")

Write out format foo.

This method is normally called via [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 and [`FigureCanvasBase.print_figure`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.print_figure "matplotlib.backend_bases.FigureCanvasBase.print_figure")
, which take care of setting the figure facecolor, edgecolor, and dpi to the desired output values, and will restore them to the original values. Therefore, [`print_foo`](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureCanvasTemplate.print_foo "matplotlib.backends.backend_template.FigureCanvasTemplate.print_foo")
 does not need to handle these settings.

matplotlib.backends.backend\_template.FigureManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L139-L146)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureManager "Link to this definition")

alias of [`FigureManagerTemplate`](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureManagerTemplate "matplotlib.backends.backend_template.FigureManagerTemplate")

class matplotlib.backends.backend\_template.FigureManagerTemplate(_canvas_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L139-L146)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.FigureManagerTemplate "Link to this definition")

Bases: [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")

Helper class for pyplot mode, wraps everything up into a neat bundle.

For non-interactive backends, the base class is sufficient. For interactive backends, see the documentation of the [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
 class for the list of methods that can/should be overridden.

class matplotlib.backends.backend\_template.GraphicsContextTemplate[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L109-L128)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.GraphicsContextTemplate "Link to this definition")

Bases: [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

The graphics context provides the color, line styles, etc. See the cairo and postscript backends for examples of mapping the graphics context attributes (cap styles, join styles, line widths, colors) to a particular backend. In cairo this is done by wrapping a cairo.Context object and forwarding the appropriate calls to it using a dictionary mapping styles to gdk constants. In Postscript, all the work is done by the renderer, mapping line styles to postscript calls.

If it's more appropriate to do the mapping at the renderer level (as in the postscript backend), you don't need to override any of the GC methods. If it's more appropriate to wrap an instance (as in the cairo backend) and do the mapping here, you'll need to override several of the setter methods.

The base GraphicsContext stores colors as an RGB tuple on the unit interval, e.g., (0.5, 0.0, 1.0). You may need to map this to colors appropriate for your backend.

class matplotlib.backends.backend\_template.RendererTemplate(_dpi_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L39-L106)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate "Link to this definition")

Bases: [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

The renderer handles drawing/rendering operations.

This is a minimal do-nothing class that can be used to get started when writing a new backend. Refer to [`backend_bases.RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 for documentation of the methods.

draw\_image(_gc_, _x_, _y_, _im_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L79-L80)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.draw_image "Link to this definition")

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

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L52-L53)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L82-L83)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.draw_text "Link to this definition")

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

flipy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L85-L87)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.flipy "Link to this definition")

Return whether y values increase from top to bottom.

Note that this only affects drawing of texts.

get\_canvas\_width\_height()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L89-L91)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.get_canvas_width_height "Link to this definition")

Return the canvas width and height in display coords.

get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L93-L94)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.get_text_width_height_descent "Link to this definition")

Get the width, height, and descent (offset from the bottom to the baseline), in display coords, of the string _s_ with [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 _prop_.

Whitespace at the start and the end of _s_ is included in the reported width.

new\_gc()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L96-L98)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.new_gc "Link to this definition")

Return an instance of a [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
.

points\_to\_pixels(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_template.py#L100-L106)
[#](https://matplotlib.org/stable/api/backend_template_api.html#matplotlib.backends.backend_template.RendererTemplate.points_to_pixels "Link to this definition")

Convert points to display units.

You need to override this function (unless your backend doesn't have a dpi, e.g., postscript or svg). Some imaging systems assume some value for pixels per inch:

points to pixels \= points \* pixels\_per\_inch/72 \* dpi/72

Parameters:

**points**float or array-like

Returns:

Points converted to pixels

On this page