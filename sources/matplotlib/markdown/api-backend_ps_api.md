[Skip to main content](https://matplotlib.org/stable/api/backend_ps_api.html#main-content)

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
    

`matplotlib.backends.backend_ps`[#](https://matplotlib.org/stable/api/backend_ps_api.html#module-matplotlib.backends.backend_ps "Link to this heading")

========================================================================================================================================================

A PostScript backend, which can produce both PostScript .ps and .eps.

matplotlib.backends.backend\_ps.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L966-L1234)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvas "Link to this definition")

alias of [`FigureCanvasPS`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS "matplotlib.backends.backend_ps.FigureCanvasPS")

class matplotlib.backends.backend\_ps.FigureCanvasPS(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L966-L1234)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L1232-L1234)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

filetypes \= {'eps': 'Encapsulated Postscript', 'ps': 'Postscript'}[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.filetypes "Link to this definition")

fixed\_dpi \= 72[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.fixed_dpi "Link to this definition")

get\_default\_filetype()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L971-L972)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.get_default_filetype "Link to this definition")

Return the default savefig file format as specified in `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

The returned string does not include a period. This method is overridden in backends that only support a single file type.

print\_eps(_outfile_, _\*_, _metadata\=None_, _papertype\=None_, _orientation\='portrait'_, _bbox\_inches\_restore\=None_, _\*\*kwargs_)[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.print_eps "Link to this definition")

print\_ps(_outfile_, _\*_, _metadata\=None_, _papertype\=None_, _orientation\='portrait'_, _bbox\_inches\_restore\=None_, _\*\*kwargs_)[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.FigureCanvasPS.print_ps "Link to this definition")

class matplotlib.backends.backend\_ps.RendererPS(_width_, _height_, _pswriter_, _imagedpi\=72_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L398-L956)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS "Link to this definition")

Bases: `RendererPDFPSBase`

The renderer handles all the drawing primitives using a graphics context instance that controls the colors/styles.

create\_hatch(_hatch_, _linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L509-L539)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.create_hatch "Link to this definition")

draw\_gouraud\_triangles(_gc_, _points_, _colors_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L859-L905)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_gouraud_triangles "Link to this definition")

Draw a series of Gouraud triangles.

Parameters:

**gc**[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

The graphics context.

**triangles\_array**(N, 3, 2) array-like

Array of _N_ (x, y) points for the triangles.

**colors\_array**(N, 3, 4) array-like

Array of _N_ RGBA colors for each point of the triangles.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

An affine transform to apply to the points.

draw\_image(_gc_, _x_, _y_, _im_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L580-L611)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_image "Link to this definition")

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

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _trans_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L621-L672)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_path "matplotlib.backends.backend_ps.RendererPS.draw_path")
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

draw\_mathtext(_gc_, _x_, _y_, _s_, _prop_, _angle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L830-L857)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_mathtext "Link to this definition")

Draw the math text using matplotlib.mathtext.

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L613-L619)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_path\_collection(_gc_, _master\_transform_, _paths_, _all\_transforms_, _offsets_, _offset\_trans_, _facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiaseds_, _urls_, _offset\_position_, _\*_, _hatchcolors\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L674-L719)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_path_collection "Link to this definition")

Draw a collection of _paths_.

Each path is first transformed by the corresponding entry in _all\_transforms_ (a list of (3, 3) matrices) and then by _master\_transform_. They are then translated by the corresponding entry in _offsets_, which has been first transformed by _offset\_trans_.

_facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiased_ and _hatchcolors_ are lists that set the corresponding properties.

Added in version 3.11: Allow _hatchcolors_ to be specified.

_offset\_position_ is unused now, but the argument is kept for backwards compatibility.

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_path "matplotlib.backends.backend_ps.RendererPS.draw_path")
. Backends may want to override this in order to render each set of path data only once, and then reference that path multiple times with the different offsets, colors, styles etc. The generator methods `_iter_collection_raw_paths` and `_iter_collection` are provided to help with (and standardize) the implementation across backends. It is highly recommended to use those generators, so that changes to the behavior of [`draw_path_collection`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_path_collection "matplotlib.backends.backend_ps.RendererPS.draw_path_collection")
 can be made globally.

draw\_tex(_gc_, _x_, _y_, _s_, _prop_, _angle_, _\*_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L721-L761)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_tex "Link to this definition")

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

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L763-L828)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.draw_text "Link to this definition")

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

get\_image\_magnification()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L541-L547)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.get_image_magnification "Link to this definition")

Get the factor by which to magnify images passed to draw\_image. Allows a backend to have images at a different resolution to other artists.

set\_color(_r_, _g_, _b_, _store\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L449-L455)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_color "Link to this definition")

set\_font(_fontname_, _fontsize_, _store\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L502-L507)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_font "Link to this definition")

set\_linecap(_linecap_, _store\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L484-L488)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_linecap "Link to this definition")

set\_linedash(_offset_, _seq_, _store\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L490-L500)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_linedash "Link to this definition")

set\_linejoin(_linejoin_, _store\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L471-L475)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_linejoin "Link to this definition")

set\_linewidth(_linewidth_, _store\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L457-L462)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS.set_linewidth "Link to this definition")

matplotlib.backends.backend\_ps.gs\_distill(_tmpfile_, _eps\=False_, _ptype\='letter'_, _bbox\=None_, _rotated\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L1294-L1330)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.gs_distill "Link to this definition")

Use ghostscript's pswrite or epswrite device to distill a file. This yields smaller files without illegal encapsulated postscript operators. The output is low-level, converting text to outlines.

matplotlib.backends.backend\_ps.pstoeps(_tmpfile_, _bbox\=None_, _rotated\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L1388-L1440)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.pstoeps "Link to this definition")

Convert the postscript to encapsulated postscript. The bbox of the eps file will be replaced with the given _bbox_ argument. If None, original bbox will be used.

matplotlib.backends.backend\_ps.xpdf\_distill(_tmpfile_, _eps\=False_, _ptype\='letter'_, _bbox\=None_, _rotated\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_ps.py#L1333-L1372)
[#](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.xpdf_distill "Link to this definition")

Use ghostscript's ps2pdf and xpdf's/poppler's pdftops to distill a file. This yields smaller files without illegal encapsulated postscript operators. This distiller is preferred, generating high-level postscript output that treats text as text.

On this page