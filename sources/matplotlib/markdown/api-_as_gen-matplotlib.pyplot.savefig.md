[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#main-content)

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
    

matplotlib.pyplot.savefig[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib-pyplot-savefig "Link to this heading")

========================================================================================================================================================

matplotlib.pyplot.savefig(_fname_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1341-L1348)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "Link to this definition")

Save the current figure as an image or vector graphic to a file.

Call signature:

savefig(fname, \*, transparent\=None, dpi\='figure', format\=None,
        metadata\=None, bbox\_inches\=None, pad\_inches\=0.1,
        facecolor\='auto', edgecolor\='auto', backend\=None,
        \*\*kwargs
       )

The available output formats depend on the backend being used.

Parameters:

**fname**str or path-like or binary file-like

A path, or a Python file-like object, or possibly some backend-dependent object such as [`matplotlib.backends.backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
.

If _format_ is set, it determines the output format, and the file is saved as _fname_. Note that _fname_ is used verbatim, and there is no attempt to make the extension, if any, of _fname_ match _format_, and no extension is appended.

If _format_ is not set, then the format is inferred from the extension of _fname_, if there is one. If _format_ is not set and _fname_ has no extension, then the file is saved with `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`) and the appropriate extension is appended to _fname_.

Other Parameters:

**transparent**bool, default: `[rcParams["savefig.transparent"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.transparent#rcparam-savefig-transparent) ` (default: `False`)

If _True_, the Axes patches will all be transparent; the Figure patch will also be transparent unless _facecolor_ and/or _edgecolor_ are specified via kwargs.

If _False_ has no effect and the color of the Axes and Figure patches are unchanged (unless the Figure patch is specified via the _facecolor_ and/or _edgecolor_ keyword arguments in which case those colors are used).

The transparency of these patches will be restored to their original values upon exit of this function.

This is useful, for example, for displaying a plot on top of a colored background on a web page.

**dpi**float or 'figure', default: `[rcParams["savefig.dpi"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.dpi#rcparam-savefig-dpi) ` (default: `'figure'`)

The resolution in dots per inch. If 'figure', use the figure's dpi value.

**format**str

The file format, e.g. 'png', 'pdf', 'svg', ... The behavior when this is unset is documented under _fname_.

**metadata**dict, optional

Key/value pairs to store in the image metadata. The supported keys and defaults depend on the image format and backend:

*   'png' with Agg backend: See the parameter `metadata` of [`print_png`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.print_png "matplotlib.backends.backend_agg.FigureCanvasAgg.print_png")
    .
    
*   'pdf' with pdf backend: See the parameter `metadata` of [`PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
    .
    
*   'svg' with svg backend: See the parameter `metadata` of [`print_svg`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg "matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg")
    .
    
*   'eps' and 'ps' with PS backend: Only 'Creator' is supported.
    

Not supported for 'pgf', 'raw', and 'rgba' as those formats do not support embedding metadata. Does not currently support 'jpg', 'tiff', or 'webp', but may include embedding EXIF metadata in the future.

**bbox\_inches**str or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, default: `[rcParams["savefig.bbox"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.bbox#rcparam-savefig-bbox) ` (default: `None`)

Bounding box in inches: only the given portion of the figure is saved. If 'tight', try to figure out the tight bbox of the figure.

**pad\_inches**float or 'layout', default: `[rcParams["savefig.pad_inches"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.pad_inches#rcparam-savefig-pad-inches) ` (default: `0.1`)

Amount of padding in inches around the figure when bbox\_inches is 'tight'. If 'layout' use the padding from the constrained or compressed layout engine; ignored if one of those engines is not in use.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or 'auto', default: `[rcParams["savefig.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.facecolor#rcparam-savefig-facecolor) ` (default: `'auto'`)

The facecolor of the figure. If 'auto', use the current figure facecolor.

**edgecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or 'auto', default: `[rcParams["savefig.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.edgecolor#rcparam-savefig-edgecolor) ` (default: `'auto'`)

The edgecolor of the figure. If 'auto', use the current figure edgecolor.

**backend**str, optional

Use a non-default backend to render the file, e.g. to render a png file with the "cairo" backend rather than the default "agg", or a pdf file with the "pgf" backend rather than the default "pdf". Note that the default backend is normally sufficient. See [The builtin backends](https://matplotlib.org/stable/users/explain/figure/backends.html#the-builtin-backends)
 for a list of valid backends for each file format. Custom backends can be referenced as "module://...".

**orientation**{'landscape', 'portrait'}

Currently only supported by the postscript backend.

**papertype**str

One of 'letter', 'legal', 'executive', 'ledger', 'a0' through 'a10', 'b0' through 'b10'. Only supported for postscript output.

**bbox\_extra\_artists**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, optional

A list of extra artists that will be considered when the tight bbox is calculated.

**pil\_kwargs**dict, optional

Additional keyword arguments that are passed to [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 when saving the figure.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

Examples using `matplotlib.pyplot.savefig`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#examples-using-matplotlib-pyplot-savefig "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_canvasagg_thumb.png)

[CanvasAgg demo](https://matplotlib.org/stable/gallery/user_interfaces/canvasagg.html)

CanvasAgg demo

![](https://matplotlib.org/stable/_images/sphx_glr_svg_histogram_sgskip_thumb.svg)

[SVG Histogram](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html)

SVG Histogram

![](https://matplotlib.org/stable/_images/sphx_glr_svg_tooltip_sgskip_thumb.svg)

[SVG Tooltip](https://matplotlib.org/stable/gallery/user_interfaces/svg_tooltip_sgskip.html)

SVG Tooltip

![](https://matplotlib.org/stable/_images/sphx_glr_print_stdout_sgskip_thumb.png)

[Print image to stdout](https://matplotlib.org/stable/gallery/misc/print_stdout_sgskip.html)

Print image to stdout

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_line_thumb.png)

[Apply SVG filter to a line](https://matplotlib.org/stable/gallery/misc/svg_filter_line.html)

Apply SVG filter to a line

![](https://matplotlib.org/stable/_images/sphx_glr_svg_filter_pie_thumb.png)

[SVG filter pie](https://matplotlib.org/stable/gallery/misc/svg_filter_pie.html)

SVG filter pie

On this page