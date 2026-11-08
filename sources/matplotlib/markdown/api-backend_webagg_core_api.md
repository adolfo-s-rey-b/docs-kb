[Skip to main content](https://matplotlib.org/stable/api/backend_webagg_core_api.html#main-content)

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
    

`matplotlib.backends.backend_webagg_core`[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#module-matplotlib.backends.backend_webagg_core "Link to this heading")

===================================================================================================================================================================================

Displays Agg images in the browser, with interactivity.

matplotlib.backends.backend\_webagg\_core.FigureCanvas[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L155-L402)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvas "Link to this definition")

alias of [`FigureCanvasWebAggCore`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore "matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore")

class matplotlib.backends.backend\_webagg\_core.FigureCanvasWebAggCore(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L155-L402)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore "Link to this definition")

Bases: [`FigureCanvasAgg`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")

blit(_bbox\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L196-L198)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.blit "Link to this definition")

Blit the canvas in bbox (default entire canvas).

draw()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L189-L194)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

draw\_idle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L200-L201)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.draw_idle "Link to this definition")

Request a widget redraw once control returns to the GUI event loop.

Even if multiple calls to [`draw_idle`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.draw_idle "matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.draw_idle")
 occur before control returns to the GUI event loop, the figure will only be rendered once.

Notes

Backends may choose to override the method and implement their own strategy to prevent multiple renderings.

get\_capture\_scroll()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L242-L250)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.get_capture_scroll "Link to this definition")

Get whether scroll events are currently captured by the canvas.

Returns:

bool

get\_diff\_image()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L252-L283)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.get_diff_image "Link to this definition")

handle\_ack(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L294-L301)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_ack "Link to this definition")

handle\_button\_press(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_button_press "Link to this definition")

handle\_button\_release(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_button_release "Link to this definition")

handle\_dblclick(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_dblclick "Link to this definition")

handle\_draw(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L303-L304)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_draw "Link to this definition")

handle\_event(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L285-L289)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_event "Link to this definition")

handle\_figure\_enter(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_figure_enter "Link to this definition")

handle\_figure\_leave(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_figure_leave "Link to this definition")

handle\_key\_press(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L345-L348)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_key_press "Link to this definition")

handle\_key\_release(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L345-L348)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_key_release "Link to this definition")

handle\_motion\_notify(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_motion_notify "Link to this definition")

handle\_refresh(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L358-L368)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_refresh "Link to this definition")

handle\_resize(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L370-L382)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_resize "Link to this definition")

handle\_scroll(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L306-L339)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_scroll "Link to this definition")

handle\_send\_image\_mode(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L384-L386)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_send_image_mode "Link to this definition")

handle\_set\_device\_pixel\_ratio(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L388-L389)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_set_device_pixel_ratio "Link to this definition")

handle\_set\_dpi\_ratio(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L391-L393)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_set_dpi_ratio "Link to this definition")

handle\_toolbar\_button(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L351-L356)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_toolbar_button "Link to this definition")

handle\_unknown\_event(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L291-L292)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.handle_unknown_event "Link to this definition")

manager\_class[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L462-L549)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.manager_class "Link to this definition")

alias of [`FigureManagerWebAgg`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg "matplotlib.backends.backend_webagg_core.FigureManagerWebAgg")

send\_event(_event\_type_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L400-L402)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.send_event "Link to this definition")

set\_capture\_scroll(_capture_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L230-L240)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.set_capture_scroll "Link to this definition")

Set whether the scroll events on the canvas will scroll the page.

Parameters:

**capture**bool

set\_cursor(_cursor_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L203-L214)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.set_cursor "Link to this definition")

Set the current cursor.

This may have no effect if the backend does not display anything.

If required by the backend, this method should trigger an update in the backend event loop after the cursor is set, as this method may be called e.g. before a long-running task during which the GUI is not updated.

Parameters:

**cursor**[`Cursors`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")

The cursor to display over the canvas. Note: some backends may change the cursor for the entire window.

set\_image\_mode(_mode_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L216-L228)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.set_image_mode "Link to this definition")

Set the image mode for any subsequent images which will be sent to the clients. The modes may currently be either 'full' or 'diff'.

Note: diff images may not contain transparency, therefore upon draw this mode may be changed if the resulting image has any transparent component.

show()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L184-L187)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.show "Link to this definition")

supports\_blit \= False[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.supports_blit "Link to this definition")

matplotlib.backends.backend\_webagg\_core.FigureManager[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L462-L549)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManager "Link to this definition")

alias of [`FigureManagerWebAgg`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg "matplotlib.backends.backend_webagg_core.FigureManagerWebAgg")

class matplotlib.backends.backend\_webagg\_core.FigureManagerWebAgg(_canvas_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L462-L549)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg "Link to this definition")

Bases: [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")

ToolbarCls[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L416-L459)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.ToolbarCls "Link to this definition")

alias of [`NavigationToolbar2WebAgg`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg "matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg")

add\_web\_socket(_web\_socket_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L491-L496)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.add_web_socket "Link to this definition")

classmethod get\_javascript(_stream\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L511-L540)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.get_javascript "Link to this definition")

classmethod get\_static\_file\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L542-L544)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.get_static_file_path "Link to this definition")

get\_window\_title()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L486-L487)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.get_window_title "Link to this definition")

Return the title text of the window containing the figure.

handle\_json(_content_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L501-L502)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.handle_json "Link to this definition")

refresh\_all()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L504-L509)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.refresh_all "Link to this definition")

remove\_web\_socket(_web\_socket_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L498-L499)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.remove_web_socket "Link to this definition")

resize(_w_, _h_, _forward\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L475-L480)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.resize "Link to this definition")

For GUI backends, resize the window (in physical pixels).

set\_window\_title(_title_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L482-L484)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.set_window_title "Link to this definition")

Set the title text of the window containing the figure.

Examples

\>>> fig \= plt.figure()
\>>> fig.canvas.manager.set\_window\_title('My figure')

show()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L472-L473)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureManagerWebAgg.show "Link to this definition")

For GUI backends, show the figure window and redraw. For non-GUI backends, raise an exception, unless running headless (i.e. on Linux with an unset DISPLAY); this exception is converted to a warning in [`Figure.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
.

class matplotlib.backends.backend\_webagg\_core.NavigationToolbar2WebAgg(_canvas_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L416-L459)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg "Link to this definition")

Bases: [`NavigationToolbar2`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "matplotlib.backend_bases.NavigationToolbar2")

draw\_rubberband(_event_, _x0_, _y0_, _x1_, _y1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L436-L437)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.draw_rubberband "Link to this definition")

Draw a rectangle rubberband to indicate zoom limits.

Note that it is not guaranteed that `x0 <= x1` and `y0 <= y1`.

pan()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L447-L449)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.pan "Link to this definition")

Toggle the pan/zoom tool.

Pan with left button, zoom with right.

remove\_rubberband()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L439-L440)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.remove_rubberband "Link to this definition")

Remove the rubberband.

save\_figure(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L442-L445)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.save_figure "Link to this definition")

Save the current figure.

set\_history\_buttons()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L455-L459)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.set_history_buttons "Link to this definition")

Enable or disable the back/forward button.

set\_message(_message_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L431-L434)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.set_message "Link to this definition")

Display a message on toolbar or in status bar.

toolitems \= \[('Home', 'Reset original view', 'home', 'home'), ('Back', 'Back to previous view', 'back', 'back'), ('Forward', 'Forward to next view', 'forward', 'forward'), (None, None, None, None), ('Pan', 'Left button pans, Right button zooms\\nx/y fixes axis, CTRL fixes aspect', 'move', 'pan'), ('Zoom', 'Zoom to rectangle\\nx/y fixes axis', 'zoom\_to\_rect', 'zoom'), (None, None, None, None), ('Download', 'Download plot', 'filesave', 'download')\][#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.toolitems "Link to this definition")

zoom()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L451-L453)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.NavigationToolbar2WebAgg.zoom "Link to this definition")

class matplotlib.backends.backend\_webagg\_core.TimerAsyncio(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L120-L152)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.TimerAsyncio "Link to this definition")

Bases: [`TimerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase "matplotlib.backend_bases.TimerBase")

Parameters:

**interval**int, default: 1000ms

The time between timer events in milliseconds. Will be stored as `timer.interval`.

**callbacks**list\[tuple\[callable, tuple, dict\]\]

List of (func, args, kwargs) tuples that will be called upon timer events. This list is accessible as `timer.callbacks` and can be manipulated directly, or the functions [`add_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.add_callback "matplotlib.backend_bases.TimerBase.add_callback")
 and [`remove_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.remove_callback "matplotlib.backend_bases.TimerBase.remove_callback")
 can be used.

class matplotlib.backends.backend\_webagg\_core.TimerTornado(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backends/backend_webagg_core.py#L81-L117)
[#](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.TimerTornado "Link to this definition")

Bases: [`TimerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase "matplotlib.backend_bases.TimerBase")

Parameters:

**interval**int, default: 1000ms

The time between timer events in milliseconds. Will be stored as `timer.interval`.

**callbacks**list\[tuple\[callable, tuple, dict\]\]

List of (func, args, kwargs) tuples that will be called upon timer events. This list is accessible as `timer.callbacks` and can be manipulated directly, or the functions [`add_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.add_callback "matplotlib.backend_bases.TimerBase.add_callback")
 and [`remove_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.remove_callback "matplotlib.backend_bases.TimerBase.remove_callback")
 can be used.

On this page