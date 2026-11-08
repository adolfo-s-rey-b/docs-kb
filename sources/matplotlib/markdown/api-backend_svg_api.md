[Skip to main content](https://matplotlib.org/stable/api/backend_svg_api.html#main-content)

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
    

`matplotlib.backends.backend_svg`[#](https://matplotlib.org/stable/api/backend_svg_api.html#module-matplotlib.backends.backend_svg "Link to this heading")

===========================================================================================================================================================

matplotlib.backends.backend\_svg.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1317-L1379)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvas "Link to this definition")

alias of [`FigureCanvasSVG`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG "matplotlib.backends.backend_svg.FigureCanvasSVG")

class matplotlib.backends.backend\_svg.FigureCanvasSVG(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1317-L1379)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1377-L1379)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

filetypes \= {'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics'}[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.filetypes "Link to this definition")

fixed\_dpi \= 72[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.fixed_dpi "Link to this definition")

get\_default\_filetype()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1374-L1375)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.get_default_filetype "Link to this definition")

Return the default savefig file format as specified in `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

The returned string does not include a period. This method is overridden in backends that only support a single file type.

print\_svg(_filename_, _\*_, _bbox\_inches\_restore\=None_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1323-L1367)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg "Link to this definition")

Parameters:

**filename**str or path-like or file-like

Output target; if a string, a file will be opened for writing.

**metadata**dict\[str, Any\], optional

Metadata in the SVG file defined as key-value pairs of strings, datetimes, or lists of strings, e.g., `{'Creator': 'My software', 'Contributor': ['Me', 'My Friend'], 'Title': 'Awesome'}`.

The standard keys and their value types are:

*   _str_: `'Coverage'`, `'Description'`, `'Format'`, `'Identifier'`, `'Language'`, `'Relation'`, `'Source'`, `'Title'`, and `'Type'`.
    
*   _str_ or _list of str_: `'Contributor'`, `'Creator'`, `'Keywords'`, `'Publisher'`, and `'Rights'`.
    
*   _str_, _date_, _datetime_, or _tuple_ of same: `'Date'`. If a non-_str_, then it will be formatted as ISO 8601.
    

Values have been predefined for `'Creator'`, `'Date'`, `'Format'`, and `'Type'`. They can be removed by setting them to [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
.

Information is encoded as [Dublin Core Metadata](https://www.dublincore.org/specifications/dublin-core/)
.

print\_svgz(_filename_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1369-L1372)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.print_svgz "Link to this definition")

class matplotlib.backends.backend\_svg.RendererSVG(_width_, _height_, _svgwriter_, _basename\=None_, _image\_dpi\=72_, _\*_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L302-L1314)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG "Link to this definition")

Bases: [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

close\_group(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L672-L674)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.close_group "Link to this definition")

Close a grouping element with label _s_.

Only used by the SVG renderer.

draw\_gouraud\_triangles(_gc_, _triangles\_array_, _colors\_array_, _transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L913-L944)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_gouraud_triangles "Link to this definition")

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

draw\_image(_gc_, _x_, _y_, _im_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L953-L1022)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_image "Link to this definition")

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

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _trans_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L706-L747)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_path "matplotlib.backends.backend_svg.RendererSVG.draw_path")
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

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L690-L704)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_path\_collection(_gc_, _master\_transform_, _paths_, _all\_transforms_, _offsets_, _offset\_trans_, _facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiaseds_, _urls_, _offset\_position_, _\*_, _hatchcolors\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L749-L807)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_path_collection "Link to this definition")

Draw a collection of _paths_.

Each path is first transformed by the corresponding entry in _all\_transforms_ (a list of (3, 3) matrices) and then by _master\_transform_. They are then translated by the corresponding entry in _offsets_, which has been first transformed by _offset\_trans_.

_facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiased_ and _hatchcolors_ are lists that set the corresponding properties.

Added in version 3.11: Allow _hatchcolors_ to be specified.

_offset\_position_ is unused now, but the argument is kept for backwards compatibility.

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_path "matplotlib.backends.backend_svg.RendererSVG.draw_path")
. Backends may want to override this in order to render each set of path data only once, and then reference that path multiple times with the different offsets, colors, styles etc. The generator methods `_iter_collection_raw_paths` and `_iter_collection` are provided to help with (and standardize) the implementation across backends. It is highly recommended to use those generators, so that changes to the behavior of [`draw_path_collection`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_path_collection "matplotlib.backends.backend_svg.RendererSVG.draw_path_collection")
 can be made globally.

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1281-L1302)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_text "Link to this definition")

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

finalize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L357-L361)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.finalize "Link to this definition")

flipy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1304-L1306)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.flipy "Link to this definition")

Return whether y values increase from top to bottom.

Note that this only affects drawing of texts.

get\_canvas\_width\_height()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1308-L1310)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.get_canvas_width_height "Link to this definition")

Return the canvas width and height in display coords.

get\_image\_magnification()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L950-L951)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.get_image_magnification "Link to this definition")

Get the factor by which to magnify images passed to [`draw_image`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.draw_image "matplotlib.backends.backend_svg.RendererSVG.draw_image")
. Allows a backend to have images at a different resolution to other artists.

get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L1312-L1314)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.get_text_width_height_descent "Link to this definition")

Get the width, height, and descent (offset from the bottom to the baseline), in display coords, of the string _s_ with [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 _prop_.

Whitespace at the start and the end of _s_ is included in the reported width.

open\_group(_s_, _gid\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L664-L670)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.open_group "Link to this definition")

Open a grouping element with label _s_ and _gid_ (if set) as id.

Only used by the SVG renderer.

option\_image\_nocomposite()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L676-L678)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.option_image_nocomposite "Link to this definition")

Return whether image composition by Matplotlib should be skipped.

Raster backends should usually return False (letting the C-level rasterizer take care of image composition); vector backends should usually return `not rcParams["image.composite_image"]`.

option\_scale\_image()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_svg.py#L946-L948)
[#](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.RendererSVG.option_scale_image "Link to this definition")

Return whether arbitrary affine transformations in [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
 are supported (True for most vector backends).

On this page