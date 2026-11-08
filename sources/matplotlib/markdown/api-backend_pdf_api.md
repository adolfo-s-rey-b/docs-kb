[Skip to main content](https://matplotlib.org/stable/api/backend_pdf_api.html#main-content)

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
    

`matplotlib.backends.backend_pdf`[#](https://matplotlib.org/stable/api/backend_pdf_api.html#module-matplotlib.backends.backend_pdf "Link to this heading")

===========================================================================================================================================================

A PDF Matplotlib backend.

Author: Jouni K Seppänen <[jks@iki.fi](mailto:jks%40iki.fi)
\> and others.

matplotlib.backends.backend\_pdf.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2696-L2733)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvas "Link to this definition")

alias of [`FigureCanvasPdf`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf "matplotlib.backends.backend_pdf.FigureCanvasPdf")

class matplotlib.backends.backend\_pdf.FigureCanvasPdf(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2696-L2733)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf "Link to this definition")

Bases: [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2731-L2733)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

filetypes \= {'pdf': 'Portable Document Format'}[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf.filetypes "Link to this definition")

fixed\_dpi \= 72[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf.fixed_dpi "Link to this definition")

get\_default\_filetype()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2702-L2703)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf.get_default_filetype "Link to this definition")

Return the default savefig file format as specified in `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

The returned string does not include a period. This method is overridden in backends that only support a single file type.

print\_pdf(_filename_, _\*_, _bbox\_inches\_restore\=None_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2705-L2729)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.FigureCanvasPdf.print_pdf "Link to this definition")

class matplotlib.backends.backend\_pdf.GraphicsContextPdf(_file_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2378-L2580)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf "Link to this definition")

Bases: [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

alpha\_cmd(_alpha_, _forced_, _effective\_alphas_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2445-L2447)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.alpha_cmd "Link to this definition")

capstyle\_cmd(_style_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2429-L2430)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.capstyle_cmd "Link to this definition")

capstyles \= {'butt': 0, 'projecting': 2, 'round': 1}[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.capstyles "Link to this definition")

clip\_cmd(_cliprect_, _clippath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2490-L2508)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.clip_cmd "Link to this definition")

Set clip rectangle. Calls [`pop()`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.pop "matplotlib.backends.backend_pdf.GraphicsContextPdf.pop")
 and [`push()`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.push "matplotlib.backends.backend_pdf.GraphicsContextPdf.push")
.

commands \= ((('\_cliprect', '\_clippath'), <function GraphicsContextPdf.clip\_cmd>), (('\_alpha', '\_forced\_alpha', '\_effective\_alphas'), <function GraphicsContextPdf.alpha\_cmd>), (('\_capstyle',), <function GraphicsContextPdf.capstyle\_cmd>), (('\_fillcolor',), <function GraphicsContextPdf.fillcolor\_cmd>), (('\_joinstyle',), <function GraphicsContextPdf.joinstyle\_cmd>), (('\_linewidth',), <function GraphicsContextPdf.linewidth\_cmd>), (('\_dashes',), <function GraphicsContextPdf.dash\_cmd>), (('\_rgb',), <function GraphicsContextPdf.rgb\_cmd>), (('\_hatch', '\_hatch\_color', '\_hatch\_linewidth'), <function GraphicsContextPdf.hatch\_cmd>))[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.commands "Link to this definition")

copy\_properties(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2562-L2571)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.copy_properties "Link to this definition")

Copy properties of other into self.

dash\_cmd(_dashes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2438-L2443)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.dash_cmd "Link to this definition")

delta(_other_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2524-L2560)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.delta "Link to this definition")

Copy properties of other into self and return PDF commands needed to transform _self_ into _other_.

fill(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2404-L2417)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.fill "Link to this definition")

Predicate: does the path need to be filled?

An optional argument can be used to specify an alternative \_fillcolor, as needed by RendererPdf.draw\_markers.

fillcolor\_cmd(_rgb_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2469-L2475)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.fillcolor_cmd "Link to this definition")

finalize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2573-L2580)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.finalize "Link to this definition")

Make sure every pushed graphics state is popped.

hatch\_cmd(_hatch_, _hatch\_color_, _hatch\_linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2449-L2459)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.hatch_cmd "Link to this definition")

joinstyle\_cmd(_style_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2432-L2433)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.joinstyle_cmd "Link to this definition")

joinstyles \= {'bevel': 2, 'miter': 0, 'round': 1}[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.joinstyles "Link to this definition")

linewidth\_cmd(_width_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2435-L2436)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.linewidth_cmd "Link to this definition")

paint()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2419-L2424)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.paint "Link to this definition")

Return the appropriate pdf operator to cause the path to be stroked, filled, or both.

pop()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2484-L2488)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.pop "Link to this definition")

push()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2477-L2482)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.push "Link to this definition")

rgb\_cmd(_rgb_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2461-L2467)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.rgb_cmd "Link to this definition")

stroke()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2393-L2402)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.GraphicsContextPdf.stroke "Link to this definition")

Predicate: does the path need to be stroked (its outline drawn)? This tests for the various conditions that disable stroking the path, in which case it would presumably be filled.

class matplotlib.backends.backend\_pdf.Name(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L394-L425)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Name "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

PDF name object.

name[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Name.name "Link to this definition")

pdfRepr()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L424-L425)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Name.pdfRepr "Link to this definition")

class matplotlib.backends.backend\_pdf.Op(_\*values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L437-L503)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op "Link to this definition")

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)")

PDF operators (not an exhaustive list).

begin\_text \= b'BT'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.begin_text "Link to this definition")

clip \= b'W'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.clip "Link to this definition")

close\_fill\_stroke \= b'b'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.close_fill_stroke "Link to this definition")

close\_stroke \= b's'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.close_stroke "Link to this definition")

closepath \= b'h'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.closepath "Link to this definition")

concat\_matrix \= b'cm'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.concat_matrix "Link to this definition")

curveto \= b'c'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.curveto "Link to this definition")

end\_text \= b'ET'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.end_text "Link to this definition")

endpath \= b'n'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.endpath "Link to this definition")

fill \= b'f'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.fill "Link to this definition")

fill\_stroke \= b'B'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.fill_stroke "Link to this definition")

grestore \= b'Q'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.grestore "Link to this definition")

gsave \= b'q'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.gsave "Link to this definition")

lineto \= b'l'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.lineto "Link to this definition")

moveto \= b'm'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.moveto "Link to this definition")

classmethod paint\_path(_fill_, _stroke_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L482-L503)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.paint_path "Link to this definition")

Return the PDF operator to paint a path.

Parameters:

**fill**bool

Fill the path with the fill color.

**stroke**bool

Stroke the outline of the path with the line color.

pdfRepr()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L479-L480)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.pdfRepr "Link to this definition")

rectangle \= b're'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.rectangle "Link to this definition")

selectfont \= b'Tf'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.selectfont "Link to this definition")

setcolor\_nonstroke \= b'scn'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setcolor_nonstroke "Link to this definition")

setcolor\_stroke \= b'SCN'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setcolor_stroke "Link to this definition")

setcolorspace\_nonstroke \= b'cs'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setcolorspace_nonstroke "Link to this definition")

setcolorspace\_stroke \= b'CS'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setcolorspace_stroke "Link to this definition")

setdash \= b'd'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setdash "Link to this definition")

setgray\_nonstroke \= b'g'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setgray_nonstroke "Link to this definition")

setgray\_stroke \= b'G'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setgray_stroke "Link to this definition")

setgstate \= b'gs'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setgstate "Link to this definition")

setlinecap \= b'J'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setlinecap "Link to this definition")

setlinejoin \= b'j'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setlinejoin "Link to this definition")

setlinewidth \= b'w'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setlinewidth "Link to this definition")

setrgb\_nonstroke \= b'rg'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setrgb_nonstroke "Link to this definition")

setrgb\_stroke \= b'RG'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.setrgb_stroke "Link to this definition")

shading \= b'sh'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.shading "Link to this definition")

show \= b'Tj'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.show "Link to this definition")

showkern \= b'TJ'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.showkern "Link to this definition")

stroke \= b'S'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.stroke "Link to this definition")

textmatrix \= b'Tm'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.textmatrix "Link to this definition")

textpos \= b'Td'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.textpos "Link to this definition")

textrise \= b'Ts'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.textrise "Link to this definition")

use\_xobject \= b'Do'[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Op.use_xobject "Link to this definition")

class matplotlib.backends.backend\_pdf.PdfFile(_filename_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L623-L1871)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

PDF file object.

Parameters:

**filename**str or path-like or file-like

Output target; if a string, a file will be opened for writing.

**metadata**dict from strings to strings and dates

Information dictionary object (see PDF reference section 10.2.1 'Document Information Dictionary'), e.g.: `{'Creator': 'My software', 'Author': 'Me', 'Title': 'Awesome'}`.

The standard keys are 'Title', 'Author', 'Subject', 'Keywords', 'Creator', 'Producer', 'CreationDate', 'ModDate', and 'Trapped'. Values have been predefined for 'Creator', 'Producer' and 'CreationDate'. They can be removed by setting them to [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
.

addGouraudTriangles(_points_, _colors_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1521-L1542)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.addGouraudTriangles "Link to this definition")

Add a Gouraud triangle shading.

Parameters:

**points**np.ndarray

Triangle vertices, shape (n, 3, 2) where n = number of triangles, 3 = vertices, 2 = x, y.

**colors**np.ndarray

Vertex colors, shape (n, 3, 1) or (n, 3, 4) as with points, but last dimension is either (gray,) or (r, g, b, alpha).

Returns:

Name, Reference

alphaState(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1380-L1391)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.alphaState "Link to this definition")

Return name of an ExtGState that sets alpha to the given value.

beginStream(_id_, _len_, _extra\=None_, _png\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L872-L874)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.beginStream "Link to this definition")

close()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L851-L860)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.close "Link to this definition")

Flush all buffers and free all resources.

createType1Descriptor(_t1font_, _fontfile\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1029-L1098)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.createType1Descriptor "Link to this definition")

property dviFontInfo[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.dviFontInfo "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

dviFontName(_dvifont_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L923-L932)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.dviFontName "Link to this definition")

Given a dvi font object, return a name suitable for Op.selectfont.

Register the font internally (in `_dviFontInfo`) if not yet registered.

embedTTF(_filename_, _subset\_index_, _charmap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1121-L1378)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.embedTTF "Link to this definition")

Embed the TTF font from the named file into the document.

endStream()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L876-L879)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.endStream "Link to this definition")

finalize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L820-L849)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.finalize "Link to this definition")

Write out the various deferred objects and the pdf end matter.

fontName(_fontprop_, _subset\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L890-L921)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.fontName "Link to this definition")

Select a font based on fontprop and return a name suitable for `Op.selectfont`. If fontprop is a string, it will be interpreted as the filename of the font.

property fontNames[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.fontNames "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

hatchPattern(_hatch\_style_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1460-L1475)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.hatchPattern "Link to this definition")

property hatchPatterns[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.hatchPatterns "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.10:

imageObject(_image_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1588-L1598)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.imageObject "Link to this definition")

Return name of an image XObject representing the given image.

markerObject(_path_, _trans_, _fill_, _stroke_, _lw_, _joinstyle_, _capstyle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1725-L1752)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.markerObject "Link to this definition")

Return name of a marker XObject representing the given path.

property multi\_byte\_charprocs[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.multi_byte_charprocs "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

newPage(_width_, _height_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L755-L782)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.newPage "Link to this definition")

newTextnote(_text_, _positionRect\=\[-100, \-100, 0, 0\]_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L784-L791)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.newTextnote "Link to this definition")

output(_\*data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L868-L870)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.output "Link to this definition")

outputStream(_ref_, _data_, _\*_, _extra\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L881-L884)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.outputStream "Link to this definition")

pathCollectionObject(_gc_, _path_, _trans_, _padding_, _filled_, _stroked_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1776-L1782)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.pathCollectionObject "Link to this definition")

static pathOperations(_path_, _transform_, _clip\=None_, _simplify\=None_, _sketch\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1805-L1812)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.pathOperations "Link to this definition")

recordXref(_id_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1836-L1837)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.recordXref "Link to this definition")

reserveObject(_name\=''_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1825-L1834)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.reserveObject "Link to this definition")

Reserve an ID for an indirect object.

The name is used for debugging in case we forget to print out the object with writeObject.

property type1Descriptors[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.type1Descriptors "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

write(_data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L862-L866)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.write "Link to this definition")

writeExtGSTates()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1445-L1452)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeExtGSTates "Link to this definition")

writeFonts()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L934-L950)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeFonts "Link to this definition")

writeGouraudTriangles()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1544-L1586)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeGouraudTriangles "Link to this definition")

writeHatches()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1481-L1519)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeHatches "Link to this definition")

writeImages()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1715-L1723)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeImages "Link to this definition")

writeInfoDict()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1856-L1860)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeInfoDict "Link to this definition")

Write out the info dictionary, checking it for good form

writeMarkers()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1754-L1774)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeMarkers "Link to this definition")

writeObject(_object_, _contents_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1839-L1841)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeObject "Link to this definition")

writePath(_path_, _transform_, _clip\=False_, _sketch\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1814-L1823)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writePath "Link to this definition")

writePathCollectionTemplates()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1784-L1803)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writePathCollectionTemplates "Link to this definition")

writeTrailer()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1862-L1871)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeTrailer "Link to this definition")

Write out the PDF trailer.

writeXref()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1843-L1854)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeXref "Link to this definition")

Write out the xref table.

class matplotlib.backends.backend\_pdf.PdfPages(_filename_, _keep\_empty\=<deprecated parameter>_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2583-L2693)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A multi-page PDF file.

Notes

In reality [`PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
 is a thin wrapper around [`PdfFile`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile "matplotlib.backends.backend_pdf.PdfFile")
, in order to avoid confusion when using [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
 and forgetting the format argument.

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

**filename**str or path-like or file-like

Plots using [`PdfPages.savefig`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.savefig "matplotlib.backends.backend_pdf.PdfPages.savefig")
 will be written to a file at this location. The file is opened when a figure is saved for the first time (overwriting any older file with the same name).

**metadata**dict, optional

Information dictionary object (see PDF reference section 10.2.1 'Document Information Dictionary'), e.g.: `{'Creator': 'My software', 'Author': 'Me', 'Title': 'Awesome'}`.

The standard keys are 'Title', 'Author', 'Subject', 'Keywords', 'Creator', 'Producer', 'CreationDate', 'ModDate', and 'Trapped'. Values have been predefined for 'Creator', 'Producer' and 'CreationDate'. They can be removed by setting them to [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
.

attach\_note(_text_, _positionRect\=\[-100, \-100, 0, 0\]_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2686-L2693)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.attach_note "Link to this definition")

Add a new text note to the page to be saved next. The optional positionRect specifies the position of the new note on the page. It is outside the page per default to make sure it is invisible on printouts.

close()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2642-L2650)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.close "Link to this definition")

Finalize this object, making the underlying file a complete PDF file.

get\_pagecount()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2682-L2684)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.get_pagecount "Link to this definition")

Return the current number of pages in the multipage pdf file.

infodict()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2652-L2658)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.infodict "Link to this definition")

Return a modifiable information dictionary object (see PDF reference section 10.2.1 'Document Information Dictionary').

savefig(_figure\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2660-L2680)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.savefig "Link to this definition")

Save a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 to this file as a new page.

Any other keyword arguments are passed to [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

Parameters:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or int, default: the active figure

The figure, or index of the figure, that is saved to the file.

class matplotlib.backends.backend\_pdf.Reference(_id_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L371-L391)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Reference "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

PDF reference object.

Use PdfFile.reserveObject() to create References.

pdfRepr()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L384-L385)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Reference.pdfRepr "Link to this definition")

write(_contents_, _file_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L387-L391)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Reference.write "Link to this definition")

class matplotlib.backends.backend\_pdf.RendererPdf(_file_, _image\_dpi_, _height_, _width_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1874-L2375)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf "Link to this definition")

Bases: `RendererPDFPSBase`

check\_gc(_gc_, _fillcolor\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1888-L1913)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.check_gc "Link to this definition")

draw\_gouraud\_triangles(_gc_, _points_, _colors_, _trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2088-L2126)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_gouraud_triangles "Link to this definition")

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

draw\_image(_gc_, _x_, _y_, _im_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1918-L1946)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_image "Link to this definition")

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

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _trans_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2050-L2086)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_path "matplotlib.backends.backend_pdf.RendererPdf.draw_path")
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

draw\_mathtext(_gc_, _x_, _y_, _s_, _prop_, _angle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2138-L2181)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_mathtext "Link to this definition")

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1948-L1955)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_path\_collection(_gc_, _master\_transform_, _paths_, _all\_transforms_, _offsets_, _offset\_trans_, _facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiaseds_, _urls_, _offset\_position_, _\*_, _hatchcolors\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1957-L2048)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_path_collection "Link to this definition")

Draw a collection of _paths_.

Each path is first transformed by the corresponding entry in _all\_transforms_ (a list of (3, 3) matrices) and then by _master\_transform_. They are then translated by the corresponding entry in _offsets_, which has been first transformed by _offset\_trans_.

_facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiased_ and _hatchcolors_ are lists that set the corresponding properties.

Added in version 3.11: Allow _hatchcolors_ to be specified.

_offset\_position_ is unused now, but the argument is kept for backwards compatibility.

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_path "matplotlib.backends.backend_pdf.RendererPdf.draw_path")
. Backends may want to override this in order to render each set of path data only once, and then reference that path multiple times with the different offsets, colors, styles etc. The generator methods `_iter_collection_raw_paths` and `_iter_collection` are provided to help with (and standardize) the implementation across backends. It is highly recommended to use those generators, so that changes to the behavior of [`draw_path_collection`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_path_collection "matplotlib.backends.backend_pdf.RendererPdf.draw_path_collection")
 can be made globally.

draw\_tex(_gc_, _x_, _y_, _s_, _prop_, _angle_, _\*_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2183-L2265)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_tex "Link to this definition")

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

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2276-L2371)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_text "Link to this definition")

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

encode\_string(_s_, _fonttype_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2272-L2274)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.encode_string "Link to this definition")

finalize()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1885-L1886)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.finalize "Link to this definition")

get\_image\_magnification()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L1915-L1916)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.get_image_magnification "Link to this definition")

Get the factor by which to magnify images passed to [`draw_image`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.draw_image "matplotlib.backends.backend_pdf.RendererPdf.draw_image")
. Allows a backend to have images at a different resolution to other artists.

new\_gc()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L2373-L2375)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf.new_gc "Link to this definition")

Return an instance of a [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
.

class matplotlib.backends.backend\_pdf.Stream(_id_, _len_, _file_, _extra\=None_, _png\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L506-L596)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

PDF stream object.

This has no pdfRepr method. Instead, call begin(), then output the contents of the stream by calling write(), and finally call end().

Parameters:

**id**int

Object id of the stream.

**len**Reference or None

An unused Reference object for the length of the stream; None means to use a memory buffer so the length can be inlined.

**file**PdfFile

The underlying object to write the stream to.

**extra**dict from Name to anything, or None

Extra key-value pairs to include in the stream header.

**png**dict or None

If the data is already png encoded, the decode parameters.

compressobj[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.compressobj "Link to this definition")

end()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L565-L579)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.end "Link to this definition")

Finalize stream.

extra[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.extra "Link to this definition")

file[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.file "Link to this definition")

id[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.id "Link to this definition")

len[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.len "Link to this definition")

pdfFile[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.pdfFile "Link to this definition")

pos[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.pos "Link to this definition")

write(_data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L581-L588)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Stream.write "Link to this definition")

Write some data on the stream.

class matplotlib.backends.backend\_pdf.Verbatim(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L428-L434)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Verbatim "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Store verbatim PDF command content for later inclusion in the stream.

pdfRepr()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L433-L434)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.Verbatim.pdfRepr "Link to this definition")

matplotlib.backends.backend\_pdf.pdfRepr(_obj_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_pdf.py#L298-L368)
[#](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.pdfRepr "Link to this definition")

Map Python objects to PDF syntax.

On this page