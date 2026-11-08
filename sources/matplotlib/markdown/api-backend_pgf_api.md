[Skip to main content](https://matplotlib.org/stable/api/backend_pgf_api.html#main-content)

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
    

`matplotlib.backends.backend_pgf`[#](https://matplotlib.org/stable/api/backend_pgf_api.html#module-matplotlib.backends.backend_pgf "Link to this heading")

===========================================================================================================================================================

matplotlib.backends.backend\_pgf.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L770-L895)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvas "Link to this definition")

alias of [`FigureCanvasPgf`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf "matplotlib.backends.backend_pgf.FigureCanvasPgf")

class matplotlib.backends.backend\_pgf.FigureCanvasPgf(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L770-L895)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L893-L895)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

filetypes \= {'pdf': 'LaTeX compiled PGF picture', 'pgf': 'LaTeX PGF picture', 'png': 'Portable Network Graphics'}[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.filetypes "Link to this definition")

get\_default\_filetype()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L775-L776)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.get_default_filetype "Link to this definition")

Return the default savefig file format as specified in `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

The returned string does not include a period. This method is overridden in backends that only support a single file type.

get\_renderer()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L890-L891)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.get_renderer "Link to this definition")

print\_pdf(_fname\_or\_fh_, _\*_, _metadata\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L844-L875)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.print_pdf "Link to this definition")

Use LaTeX to compile a pgf generated figure to pdf.

print\_pgf(_fname\_or\_fh_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L834-L842)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.print_pgf "Link to this definition")

Output pgf macros for drawing the figure so it can be included and rendered in latex documents.

print\_png(_fname\_or\_fh_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L877-L888)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.FigureCanvasPgf.print_png "Link to this definition")

Use LaTeX to compile a pgf figure to pdf and convert it to png.

exception matplotlib.backends.backend\_pgf.LatexError(_message_, _latex\_output\=''_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L196-L205)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.LatexError "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")

class matplotlib.backends.backend\_pgf.LatexManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L208-L357)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.LatexManager "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The LatexManager opens an instance of the LaTeX application for determining the metrics of text elements. The LaTeX environment can be modified by setting fonts and/or a custom preamble in [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

get\_width\_height\_descent(_text_, _prop_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L321-L326)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.LatexManager.get_width_height_descent "Link to this definition")

Get the width, total height, and descent (in TeX points) for a text typeset by the current LaTeX environment.

class matplotlib.backends.backend\_pgf.PdfPages(_filename_, _\*_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L906-L1031)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A multi-page PDF file using the pgf backend

Examples

\>>> import matplotlib.pyplot as plt
\>>> \# Initialize:
\>>> with PdfPages('foo.pdf') as pdf:
...     \# As many times as you like, create a figure fig and save it:
...     fig \= plt.figure()
...     pdf.savefig(fig)
...     \# When no figure is specified the current figure is saved
...     pdf.savefig()

Create a new PdfPages object.

Parameters:

**filename**str or path-like

Plots using [`PdfPages.savefig`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages.savefig "matplotlib.backends.backend_pgf.PdfPages.savefig")
 will be written to a file at this location. Any older file with the same name is overwritten.

**metadata**dict, optional

Information dictionary object (see PDF reference section 10.2.1 'Document Information Dictionary'), e.g.: `{'Creator': 'My software', 'Author': 'Me', 'Title': 'Awesome'}`.

The standard keys are 'Title', 'Author', 'Subject', 'Keywords', 'Creator', 'Producer', 'CreationDate', 'ModDate', and 'Trapped'. Values have been predefined for 'Creator', 'Producer' and 'CreationDate'. They can be removed by setting them to [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
.

Note that some versions of LaTeX engines may ignore the 'Producer' key and set it to themselves.

close()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L972-L980)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages.close "Link to this definition")

Finalize this object, running LaTeX in a temporary directory and moving the final pdf file to _filename_.

get\_pagecount()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L1029-L1031)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages.get_pagecount "Link to this definition")

Return the current number of pages in the multipage pdf file.

savefig(_figure\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L993-L1027)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages.savefig "Link to this definition")

Save a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 to this file as a new page.

Any other keyword arguments are passed to [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

Parameters:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or int, default: the active figure

The figure, or index of the figure, that is saved to the file.

class matplotlib.backends.backend\_pgf.RendererPgf(_figure_, _fh_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L376-L767)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf "Link to this definition")

Bases: [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

Create a new PGF renderer that translates any drawing instruction into text commands to be interpreted in a latex pgfpicture environment.

Attributes:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

Matplotlib figure to initialize height, width and dpi from.

**fh**file-like

File handle for the output of the drawing commands.

draw\_image(_gc_, _x_, _y_, _im_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L652-L691)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.draw_image "Link to this definition")

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

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _trans_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L397-L433)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.draw_path "matplotlib.backends.backend_pgf.RendererPgf.draw_path")
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

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L435-L497)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_tex(_gc_, _x_, _y_, _s_, _prop_, _angle_, _\*_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L693-L695)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.draw_tex "Link to this definition")

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

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L697-L743)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.draw_text "Link to this definition")

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

flipy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L756-L758)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.flipy "Link to this definition")

Return whether y values increase from top to bottom.

Note that this only affects drawing of texts.

get\_canvas\_width\_height()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L760-L763)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.get_canvas_width_height "Link to this definition")

Return the canvas width and height in display coords.

get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L745-L754)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.get_text_width_height_descent "Link to this definition")

Get the width, height, and descent (offset from the bottom to the baseline), in display coords, of the string _s_ with [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 _prop_.

Whitespace at the start and the end of _s_ is included in the reported width.

option\_image\_nocomposite()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L648-L650)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.option_image_nocomposite "Link to this definition")

Return whether image composition by Matplotlib should be skipped.

Raster backends should usually return False (letting the C-level rasterizer take care of image composition); vector backends should usually return `not rcParams["image.composite_image"]`.

option\_scale\_image()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L644-L646)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.option_scale_image "Link to this definition")

Return whether arbitrary affine transformations in [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
 are supported (True for most vector backends).

points\_to\_pixels(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L765-L767)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf.points_to_pixels "Link to this definition")

Convert points to display units.

You need to override this function (unless your backend doesn't have a dpi, e.g., postscript or svg). Some imaging systems assume some value for pixels per inch:

points to pixels \= points \* pixels\_per\_inch/72 \* dpi/72

Parameters:

**points**float or array-like

Returns:

Points converted to pixels

matplotlib.backends.backend\_pgf.make\_pdf\_to\_png\_converter()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pgf.py#L169-L193)
[#](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.make_pdf_to_png_converter "Link to this definition")

Return a function that converts a pdf file to a png file.

On this page