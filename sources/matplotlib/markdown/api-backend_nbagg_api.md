[Skip to main content](https://matplotlib.org/stable/api/backend_nbagg_api.html#main-content)

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
    

`matplotlib.backends.backend_nbagg`[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#module-matplotlib.backends.backend_nbagg "Link to this heading")

=================================================================================================================================================================

Interactive figures in the IPython notebook.

class matplotlib.backends.backend\_nbagg.CommSocket(_manager_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L164-L238)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.CommSocket "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Manages the Comm connection between IPython and the browser (client).

Comms are 2 way, with the CommSocket being able to publish a message via the send\_json method, and handle a message with on\_message. On the JS side figure.send\_message and figure.ws.onmessage do the sending and receiving respectively.

is\_open()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L199-L200)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.CommSocket.is_open "Link to this definition")

on\_close()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L202-L210)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.CommSocket.on_close "Link to this definition")

on\_message(_message_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L225-L238)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.CommSocket.on_message "Link to this definition")

send\_binary(_blob_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L215-L223)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.CommSocket.send_binary "Link to this definition")

send\_json(_content_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L212-L213)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.CommSocket.send_json "Link to this definition")

matplotlib.backends.backend\_nbagg.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L160-L161)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureCanvas "Link to this definition")

alias of [`FigureCanvasNbAgg`](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureCanvasNbAgg "matplotlib.backends.backend_nbagg.FigureCanvasNbAgg")

class matplotlib.backends.backend\_nbagg.FigureCanvasNbAgg(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L160-L161)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureCanvasNbAgg "Link to this definition")

Bases: [`FigureCanvasWebAggCore`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore "matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore")

manager\_class[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L64-L157)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureCanvasNbAgg.manager_class "Link to this definition")

alias of [`FigureManagerNbAgg`](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg "matplotlib.backends.backend_nbagg.FigureManagerNbAgg")

matplotlib.backends.backend\_nbagg.FigureManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L64-L157)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManager "Link to this definition")

alias of [`FigureManagerNbAgg`](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg "matplotlib.backends.backend_nbagg.FigureManagerNbAgg")

class matplotlib.backends.backend\_nbagg.FigureManagerNbAgg(_canvas_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L64-L157)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg "Link to this definition")

Bases: [`FigureManagerWebAgg`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg "matplotlib.backends.backend_webagg_core.FigureManagerWebAgg")

ToolbarCls[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L53-L61)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.ToolbarCls "Link to this definition")

alias of [`NavigationIPy`](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.NavigationIPy "matplotlib.backends.backend_nbagg.NavigationIPy")

clearup\_closed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L147-L153)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.clearup_closed "Link to this definition")

Clear up any closed Comms.

property connected[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.connected "Link to this definition")

classmethod create\_with\_canvas(_canvas\_class_, _figure_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L71-L84)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.create_with_canvas "Link to this definition")

Create a manager for a given _figure_ using a specific _canvas\_class_.

Backends should override this method if they have specific needs for setting up the canvas or the manager.

destroy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L139-L145)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.destroy "Link to this definition")

display\_js()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L86-L90)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.display_js "Link to this definition")

classmethod get\_javascript(_stream\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L121-L132)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.get_javascript "Link to this definition")

remove\_comm(_comm\_id_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L155-L157)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.remove_comm "Link to this definition")

reshow()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L109-L115)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.reshow "Link to this definition")

A special method to re-show the figure in the notebook.

show()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L92-L107)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.FigureManagerNbAgg.show "Link to this definition")

For GUI backends, show the figure window and redraw. For non-GUI backends, raise an exception, unless running headless (i.e. on Linux with an unset DISPLAY); this exception is converted to a warning in [`Figure.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
.

class matplotlib.backends.backend\_nbagg.NavigationIPy(_canvas_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L53-L61)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.NavigationIPy "Link to this definition")

Bases: [`NavigationToolbar2WebAgg`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg "matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg")

toolitems \= \[('Home', 'Reset original view', 'fa fa-home', 'home'), ('Back', 'Back to previous view', 'fa fa-arrow-left', 'back'), ('Forward', 'Forward to next view', 'fa fa-arrow-right', 'forward'), (None, None, None, None), ('Pan', 'Left button pans, Right button zooms\\nx/y fixes axis, CTRL fixes aspect', 'fa fa-arrows', 'pan'), ('Zoom', 'Zoom to rectangle\\nx/y fixes axis', 'fa fa-square-o', 'zoom'), (None, None, None, None), ('Download', 'Download plot', 'fa fa-floppy-o', 'download')\][#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.NavigationIPy.toolitems "Link to this definition")

matplotlib.backends.backend\_nbagg.connection\_info()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_nbagg.py#L24-L39)
[#](https://matplotlib.org/stable/api/backend_nbagg_api.html#matplotlib.backends.backend_nbagg.connection_info "Link to this definition")

Return a string showing the figure and connection status for the backend.

This is intended as a diagnostic tool, and not for general use.

On this page