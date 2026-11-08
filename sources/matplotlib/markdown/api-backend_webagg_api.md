[Skip to main content](https://matplotlib.org/stable/api/backend_webagg_api.html#main-content)

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
    

`matplotlib.backends.backend_webagg`[#](https://matplotlib.org/stable/api/backend_webagg_api.html#module-matplotlib.backends.backend_webagg "Link to this heading")

====================================================================================================================================================================

Displays Agg images in the browser, with interactivity.

matplotlib.backends.backend\_webagg.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L64-L65)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureCanvas "Link to this definition")

alias of [`FigureCanvasWebAgg`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureCanvasWebAgg "matplotlib.backends.backend_webagg.FigureCanvasWebAgg")

class matplotlib.backends.backend\_webagg.FigureCanvasWebAgg(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L64-L65)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureCanvasWebAgg "Link to this definition")

Bases: [`FigureCanvasWebAggCore`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore "matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore")

manager\_class[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L42-L61)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureCanvasWebAgg.manager_class "Link to this definition")

alias of [`FigureManagerWebAgg`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureManagerWebAgg "matplotlib.backends.backend_webagg.FigureManagerWebAgg")

matplotlib.backends.backend\_webagg.FigureManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L42-L61)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureManager "Link to this definition")

alias of [`FigureManagerWebAgg`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureManagerWebAgg "matplotlib.backends.backend_webagg.FigureManagerWebAgg")

class matplotlib.backends.backend\_webagg.FigureManagerWebAgg(_canvas_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L42-L61)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureManagerWebAgg "Link to this definition")

Bases: [`FigureManagerWebAgg`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg "matplotlib.backends.backend_webagg_core.FigureManagerWebAgg")

classmethod pyplot\_show(_\*_, _block\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L45-L61)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.FigureManagerWebAgg.pyplot_show "Link to this definition")

Show all figures. This method is the implementation of [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
.

To customize the behavior of [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
, interactive backends should usually override [`start_main_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.start_main_loop "matplotlib.backend_bases.FigureManagerBase.start_main_loop")
; if more customized logic is necessary, [`pyplot_show`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.pyplot_show "matplotlib.backend_bases.FigureManagerBase.pyplot_show")
 can also be overridden.

Parameters:

**block**bool, optional

Whether to block by calling `start_main_loop`. The default, None, means to block if we are neither in IPython's `%pylab` mode nor in `interactive` mode.

class matplotlib.backends.backend\_webagg.WebAggApplication(_url\_prefix\=''_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L68-L297)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication "Link to this definition")

Bases: [`Application`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.Application "(in Tornado v6.5.8)")

class AllFiguresPage(_application_, _request_, _\*_, _url\_prefix\=''_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L96-L108)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.AllFiguresPage "Link to this definition")

Bases: [`RequestHandler`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "(in Tornado v6.5.8)")

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L101-L108)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.AllFiguresPage.get "Link to this definition")

class Download(_application_, _request_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L118-L126)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.Download "Link to this definition")

Bases: [`RequestHandler`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "(in Tornado v6.5.8)")

get(_fignum_, _fmt_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L119-L126)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.Download.get "Link to this definition")

class FavIcon(_application_, _request_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L72-L76)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.FavIcon "Link to this definition")

Bases: [`RequestHandler`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "(in Tornado v6.5.8)")

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L73-L76)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.FavIcon.get "Link to this definition")

class MplJs(_application_, _request_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L110-L116)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.MplJs "Link to this definition")

Bases: [`RequestHandler`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "(in Tornado v6.5.8)")

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L111-L116)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.MplJs.get "Link to this definition")

class SingleFigurePage(_application_, _request_, _\*_, _url\_prefix\=''_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L78-L94)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.SingleFigurePage "Link to this definition")

Bases: [`RequestHandler`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "(in Tornado v6.5.8)")

get(_fignum_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L83-L94)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.SingleFigurePage.get "Link to this definition")

class WebSocket(_application_, _request_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L128-L165)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket "Link to this definition")

Bases: [`WebSocketHandler`](https://www.tornadoweb.org/en/stable/websocket.html#tornado.websocket.WebSocketHandler "(in Tornado v6.5.8)")

on\_close()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L138-L139)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.on_close "Link to this definition")

Invoked when the WebSocket is closed.

If the connection was closed cleanly and a status code or reason phrase was supplied, these values will be available as the attributes `self.close_code` and `self.close_reason`.

Changed in version 4.0: Added `close_code` and `close_reason` attributes.

on\_message(_message_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L141-L154)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.on_message "Link to this definition")

Handle incoming messages on the WebSocket

This method must be overridden.

Changed in version 4.5: `on_message` can be a coroutine.

open(_fignum_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L131-L136)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open "Link to this definition")

Invoked when a new WebSocket is opened.

The arguments to [`open`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open "matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open")
 are extracted from the [`tornado.web.URLSpec`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.URLSpec "(in Tornado v6.5.8)")
 regular expression, just like the arguments to [`tornado.web.RequestHandler.get`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.get "(in Tornado v6.5.8)")
.

[`open`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open "matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open")
 may be a coroutine. [`on_message`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.on_message "matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.on_message")
 will not be called until [`open`](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open "matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.open")
 has returned.

Changed in version 5.1: `open` may be a coroutine.

send\_binary(_blob_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L159-L165)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.send_binary "Link to this definition")

send\_json(_content_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L156-L157)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.send_json "Link to this definition")

supports\_binary \= True[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.WebSocket.supports_binary "Link to this definition")

classmethod initialize(_url\_prefix\=''_, _port\=None_, _address\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L207-L251)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.initialize "Link to this definition")

initialized \= False[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.initialized "Link to this definition")

classmethod start()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L253-L297)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.start "Link to this definition")

started \= False[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.WebAggApplication.started "Link to this definition")

matplotlib.backends.backend\_webagg.ipython\_inline\_display(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg.py#L300-L320)
[#](https://matplotlib.org/stable/api/backend_webagg_api.html#matplotlib.backends.backend_webagg.ipython_inline_display "Link to this definition")

On this page