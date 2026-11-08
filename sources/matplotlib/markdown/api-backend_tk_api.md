[Skip to main content](https://matplotlib.org/stable/api/backend_tk_api.html#main-content)

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
    

`matplotlib.backends.backend_tkagg`, `matplotlib.backends.backend_tkcairo`[#](https://matplotlib.org/stable/api/backend_tk_api.html#module-matplotlib.backends.backend_tkagg "Link to this heading")

=====================================================================================================================================================================================================

matplotlib.backends.backend\_tkagg.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkagg.py#L8-L15)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvas "Link to this definition")

alias of [`FigureCanvasTkAgg`](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvasTkAgg "matplotlib.backends.backend_tkagg.FigureCanvasTkAgg")

class matplotlib.backends.backend\_tkagg.FigureCanvasTkAgg(_figure\=None_, _master\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkagg.py#L8-L15)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvasTkAgg "Link to this definition")

Bases: [`FigureCanvasAgg`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
, `FigureCanvasTk`

blit(_bbox\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkagg.py#L13-L15)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvasTkAgg.blit "Link to this definition")

Blit the canvas in bbox (default entire canvas).

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkagg.py#L9-L11)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvasTkAgg.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

matplotlib.backends.backend\_tkcairo.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkcairo.py#L9-L18)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkcairo.FigureCanvas "Link to this definition")

alias of [`FigureCanvasTkCairo`](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkcairo.FigureCanvasTkCairo "matplotlib.backends.backend_tkcairo.FigureCanvasTkCairo")

class matplotlib.backends.backend\_tkcairo.FigureCanvasTkCairo(_figure\=None_, _master\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkcairo.py#L9-L18)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkcairo.FigureCanvasTkCairo "Link to this definition")

Bases: [`FigureCanvasCairo`](https://matplotlib.org/stable/api/backend_cairo_api.html#matplotlib.backends.backend_cairo.FigureCanvasCairo "matplotlib.backends.backend_cairo.FigureCanvasCairo")
, `FigureCanvasTk`

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_tkcairo.py#L10-L18)
[#](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkcairo.FigureCanvasTkCairo.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

On this page