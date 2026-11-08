[Skip to main content](https://matplotlib.org/stable/api/texmanager_api.html#main-content)

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
    

`matplotlib.texmanager`[#](https://matplotlib.org/stable/api/texmanager_api.html#module-matplotlib.texmanager "Link to this heading")

======================================================================================================================================

Support for embedded TeX expressions in Matplotlib.

Requirements:

*   LaTeX.
    
*   \*Agg backends: dvipng>=1.6.
    
*   PS backend: PSfrag, dvips, and Ghostscript>=9.0.
    
*   PDF and SVG backends: if LuaTeX is present, it will be used to speed up some post-processing steps, but note that it is not used to parse the TeX string itself (only LaTeX is supported).
    

To enable TeX rendering of all text in your Matplotlib figure, set `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) to True.

TeX and dvipng/dvips processing results are cached in ~/.matplotlib/tex.cache for reuse between sessions.

[`TexManager.get_rgba`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_rgba "matplotlib.texmanager.TexManager.get_rgba")
 can also be used to directly obtain raster output as RGBA NumPy arrays.

class matplotlib.texmanager.TexManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L55-L374)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Convert strings to dvi files using TeX, caching the results to a directory.

The cache directory is called `tex.cache` and is located in the directory returned by [`get_cachedir`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_cachedir "matplotlib.get_cachedir")
.

Repeated calls to this constructor always return the same instance.

classmethod get\_basefile(_tex_, _fontsize_, _dpi\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L187-L192)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_basefile "Link to this definition")

Return a filename based on a hash of the string, fontsize, and dpi.

classmethod get\_custom\_preamble()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L202-L205)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_custom_preamble "Link to this definition")

Return a string containing user additions to the tex preamble.

classmethod get\_font\_preamble()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L194-L200)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_font_preamble "Link to this definition")

Return a string containing font configuration for the tex preamble.

classmethod get\_grey(_tex_, _fontsize\=None_, _dpi\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L334-L345)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_grey "Link to this definition")

Return the alpha channel.

classmethod get\_rgba(_tex_, _fontsize\=None_, _dpi\=None_, _rgb\=(0, 0, 0)_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L347-L362)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_rgba "Link to this definition")

Return latex's rendering of the tex string as an RGBA array.

Examples

\>>> texmanager \= TexManager()
\>>> s \= r"\\TeX\\ is $\\displaystyle\\sum\_n\\frac{-e^{i\\pi}}{2^n}$!"
\>>> Z \= texmanager.get\_rgba(s, fontsize\=12, dpi\=80, rgb\=(1, 0, 0))

classmethod get\_text\_width\_height\_descent(_tex_, _fontsize_, _renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L364-L374)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.get_text_width_height_descent "Link to this definition")

Return width, height and descent of the text.

classmethod make\_dvi(_tex_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L280-L308)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.make_dvi "Link to this definition")

Generate a dvi file containing latex's layout of tex string.

Return the file name.

classmethod make\_png(_tex_, _fontsize_, _dpi_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L310-L332)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.make_png "Link to this definition")

Generate a png file containing latex's rendering of tex string.

Return the file name.

classmethod make\_tex(_tex_, _fontsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/texmanager.py#L243-L252)
[#](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager.make_tex "Link to this definition")

Generate a tex file to render the tex string at a specific font size.

Return the file name.

On this page