[Skip to main content](https://matplotlib.org/stable/api/backend_bases_api.html#main-content)

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
    

`matplotlib.backend_bases`[#](https://matplotlib.org/stable/api/backend_bases_api.html#module-matplotlib.backend_bases "Link to this heading")

===============================================================================================================================================

Abstract base classes define the primitives that renderers and graphics contexts must implement to serve as a Matplotlib backend.

[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

An abstract base class to handle drawing/rendering operations.

[`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

The abstraction layer that separates the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 from the backend specific details like a user interface drawing area.

[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

An abstract base class that provides color, line styles, etc.

[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The base class for all of the Matplotlib event handling. Derived classes such as [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent")
 and [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 store the meta data like keys and buttons pressed, x and y locations in pixel and [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 coordinates.

[`ShowBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ShowBase "matplotlib.backend_bases.ShowBase")

The base class for the `Show` class of each interactive backend; the 'show' callable is then set to `Show.__call__`.

[`ToolContainerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "matplotlib.backend_bases.ToolContainerBase")

The base class for the Toolbar class of each interactive backend.

class matplotlib.backend\_bases.CloseEvent(_name_, _canvas_, _guiEvent\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1253-L1254)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.CloseEvent "Link to this definition")

Bases: [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

An event triggered by a figure being closed.

class matplotlib.backend\_bases.DrawEvent(_name_, _canvas_, _renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1206-L1230)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.DrawEvent "Link to this definition")

Bases: [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

An event triggered by a draw operation on the canvas.

In most backends, callbacks subscribed to this event will be fired after the rendering is complete but before the screen is updated. Any extra artists drawn to the canvas's renderer will be reflected without an explicit call to `blit`.

Warning

Calling `canvas.draw` and `canvas.blit` in these callbacks may not be safe with all backends and may cause infinite recursion.

A DrawEvent has a number of special attributes in addition to those defined by the parent [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 class.

Attributes:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

The renderer for the draw event.

class matplotlib.backend\_bases.Event(_name_, _canvas_, _guiEvent\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1178-L1203)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A Matplotlib event.

The following attributes are defined and shown with their default values. Subclasses may define additional attributes.

Attributes:

**name**str

The event name.

**canvas**[`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

The backend-specific canvas instance generating the event.

**guiEvent**

The GUI event that triggered the Matplotlib event.

class matplotlib.backend\_bases.FigureCanvasBase(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1709-L2480)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The canvas the figure renders into.

Attributes:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

A high-level figure instance.

blit(_bbox\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1853-L1854)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.blit "Link to this definition")

Blit the canvas in bbox (default entire canvas).

property button\_pick\_id[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.button_pick_id "Link to this definition")

property callbacks[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.callbacks "Link to this definition")

property device\_pixel\_ratio[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.device_pixel_ratio "Link to this definition")

The ratio of physical to logical pixels used for the canvas on screen.

By default, this is 1, meaning physical and logical pixels are the same size. Subclasses that support High DPI screens may set this property to indicate that said ratio is different. All Matplotlib interaction, unless working directly with the canvas, remains in logical pixels.

draw(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1964-L1972)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "Link to this definition")

Render the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

This method must walk the artist tree, even if no output is produced, because it triggers deferred work that users may want to access before saving output to disk. For example computing limits, auto-limits, and tick values.

draw\_idle(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1974-L1989)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "Link to this definition")

Request a widget redraw once control returns to the GUI event loop.

Even if multiple calls to [`draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
 occur before control returns to the GUI event loop, the figure will only be rendered once.

Notes

Backends may choose to override the method and implement their own strategy to prevent multiple renderings.

events \= \['resize\_event', 'draw\_event', 'key\_press\_event', 'key\_release\_event', 'button\_press\_event', 'button\_release\_event', 'scroll\_event', 'motion\_notify\_event', 'pick\_event', 'figure\_enter\_event', 'figure\_leave\_event', 'axes\_enter\_event', 'axes\_leave\_event', 'close\_event'\][#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.events "Link to this definition")

filetypes \= {'avif': 'AV1 Image File Format', 'eps': 'Encapsulated Postscript', 'gif': 'Graphics Interchange Format', 'jpeg': 'Joint Photographic Experts Group', 'jpg': 'Joint Photographic Experts Group', 'pdf': 'Portable Document Format', 'pgf': 'PGF code for LaTeX', 'png': 'Portable Network Graphics', 'ps': 'Postscript', 'raw': 'Raw RGBA bitmap', 'rgba': 'Raw RGBA bitmap', 'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics', 'tif': 'Tagged Image File Format', 'tiff': 'Tagged Image File Format', 'webp': 'WebP Image Format'}[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.filetypes "Link to this definition")

fixed\_dpi \= None[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.fixed_dpi "Link to this definition")

flush\_events()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2438-L2443)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "Link to this definition")

Flush the GUI events for the figure.

Interactive backends need to reimplement this method.

get\_default\_filename()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2313-L2330)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.get_default_filename "Link to this definition")

Return a suitable default filename, including the extension.

classmethod get\_default\_filetype()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2302-L2311)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.get_default_filetype "Link to this definition")

Return the default savefig file format as specified in `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

The returned string does not include a period. This method is overridden in backends that only support a single file type.

classmethod get\_supported\_filetypes()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2074-L2077)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.get_supported_filetypes "Link to this definition")

Return dict of savefig file formats supported by this backend.

classmethod get\_supported\_filetypes\_grouped()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2079-L2091)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.get_supported_filetypes_grouped "Link to this definition")

Return a dict of savefig file formats supported by this backend, where the keys are a file type name, such as 'Joint Photographic Experts Group', and the values are a list of filename extensions used for that filetype, such as \['jpg', 'jpeg'\].

get\_width\_height(_\*_, _physical\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2042-L2072)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.get_width_height "Link to this definition")

Return the figure width and height in integral points or pixels.

When the figure is used on High DPI screens (and the backend supports it), the truncation to integers occurs after scaling by the device pixel ratio.

Parameters:

**physical**bool, default: False

Whether to return true physical pixels or logical pixels. Physical pixels may be used by backends that support HiDPI, but still configure the canvas using its actual size.

Returns:

**width, height**int

The size of the figure, in points or pixels, depending on the backend.

Notes

This method normally truncates the height/width to remove any fractional pixel. However, if the height/width is extremely close to the integer pixel (within 1e-8 pixel), the height/width is instead rounded up to account for floating-point precision effects.

grab\_mouse(_ax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1925-L1934)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.grab_mouse "Link to this definition")

Set the child [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 which is grabbing the mouse events.

Usually called by the widgets themselves. It is an error to call this if the mouse is already grabbed by another Axes.

inaxes(_xy_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1901-L1923)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.inaxes "Link to this definition")

Return the topmost visible [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 containing the point _xy_.

Parameters:

**xy**(float, float)

(x, y) pixel positions from left/bottom of the canvas.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or None

The topmost visible Axes containing the point, or None if there is no Axes at the point.

is\_saving()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1846-L1851)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.is_saving "Link to this definition")

Return whether the renderer is in the process of saving to a file, rather than rendering for an on-screen buffer.

manager\_class[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2704-L2914)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.manager_class "Link to this definition")

alias of [`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")

mpl\_connect(_s_, _func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2332-L2393)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "Link to this definition")

Bind function _func_ to event _s_.

Parameters:

**s**str

One of the following events ids:

*   'button\_press\_event'
    
*   'button\_release\_event'
    
*   'draw\_event'
    
*   'key\_press\_event'
    
*   'key\_release\_event'
    
*   'motion\_notify\_event'
    
*   'pick\_event'
    
*   'resize\_event'
    
*   'scroll\_event'
    
*   'figure\_enter\_event',
    
*   'figure\_leave\_event',
    
*   'axes\_enter\_event',
    
*   'axes\_leave\_event'
    
*   'close\_event'.
    

**func**callable

The callback function to be executed, which must have the signature:

def func(event: Event) \-> Any

For the location events (button and key press/release), if the mouse is over the Axes, the `inaxes` attribute of the event will be set to the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 the event occurs is over, and additionally, the variables `xdata` and `ydata` attributes will be set to the mouse location in data coordinates. See [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent")
 and [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 for more info.

Note

If func is a method, this only stores a weak reference to the method. Thus, the figure does not influence the lifetime of the associated object. Usually, you want to make sure that the object is kept alive throughout the lifetime of the figure by holding a reference to it.

Returns:

cid

A connection id that can be used with [`FigureCanvasBase.mpl_disconnect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_disconnect "matplotlib.backend_bases.FigureCanvasBase.mpl_disconnect")
.

Examples

def on\_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)

cid \= canvas.mpl\_connect('button\_press\_event', on\_press)

mpl\_disconnect(_cid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2395-L2407)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_disconnect "Link to this definition")

Disconnect the callback with id _cid_.

Examples

cid \= canvas.mpl\_connect('button\_press\_event', on\_press)
\# ... later
canvas.mpl\_disconnect(cid)

classmethod new\_manager(_figure_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1825-L1836)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.new_manager "Link to this definition")

Create a new figure manager for _figure_, using this canvas class.

Notes

This method should not be reimplemented in subclasses. If custom manager creation logic is needed, please reimplement `FigureManager.create_with_canvas`.

new\_timer(_interval\=None_, _callbacks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2413-L2436)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.new_timer "Link to this definition")

Create a new backend-specific subclass of [`TimerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase "matplotlib.backend_bases.TimerBase")
.

This is useful for getting periodic events through the backend's native event loop. Implemented only for backends with GUIs.

Parameters:

**interval**int

Timer interval in milliseconds.

**callbacks**list\[tuple\[callable, tuple, dict\]\]

Sequence of (func, args, kwargs) where `func(*args, **kwargs)` will be executed by the timer every _interval_.

Callbacks which return `False` or `0` will be removed from the timer.

Examples

\>>> timer \= fig.canvas.new\_timer(callbacks\=\[(f1, (1,), {'a': 3})\])

print\_figure(_filename_, _dpi\=None_, _facecolor\=None_, _edgecolor\=None_, _orientation\='portrait'_, _format\=None_, _\*_, _bbox\_inches\=None_, _pad\_inches\=None_, _bbox\_extra\_artists\=None_, _backend\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2155-L2300)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.print_figure "Link to this definition")

Render the figure to hardcopy. Set the figure patch face and edge colors. This is useful because some of the GUIs have a gray figure face color background and you'll probably want to override this on hardcopy.

Parameters:

**filename**str or path-like or file-like

The file where the figure is saved.

**dpi**float, default: `[rcParams["savefig.dpi"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.dpi#rcparam-savefig-dpi) ` (default: `'figure'`)

The dots per inch to save the figure in.

**facecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or 'auto', default: `[rcParams["savefig.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.facecolor#rcparam-savefig-facecolor) ` (default: `'auto'`)

The facecolor of the figure. If 'auto', use the current figure facecolor.

**edgecolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or 'auto', default: `[rcParams["savefig.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.edgecolor#rcparam-savefig-edgecolor) ` (default: `'auto'`)

The edgecolor of the figure. If 'auto', use the current figure edgecolor.

**orientation**{'landscape', 'portrait'}, default: 'portrait'

Only currently applies to PostScript printing.

**format**str, optional

Force a specific file format. If not given, the format is inferred from the _filename_ extension, and if that fails from `[rcParams["savefig.format"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.format#rcparam-savefig-format) ` (default: `'png'`).

**bbox\_inches**'tight' or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, default: `[rcParams["savefig.bbox"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.bbox#rcparam-savefig-bbox) ` (default: `None`)

Bounding box in inches: only the given portion of the figure is saved. If 'tight', try to figure out the tight bbox of the figure.

**pad\_inches**float or 'layout', default: `[rcParams["savefig.pad_inches"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.pad_inches#rcparam-savefig-pad-inches) ` (default: `0.1`)

Amount of padding in inches around the figure when bbox\_inches is 'tight'. If 'layout' use the padding from the constrained or compressed layout engine; ignored if one of those engines is not in use.

**bbox\_extra\_artists**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, optional

A list of extra artists that will be considered when the tight bbox is calculated.

**backend**str, optional

Use a non-default backend to render the file, e.g. to render a png file with the "cairo" backend rather than the default "agg", or a pdf file with the "pgf" backend rather than the default "pdf". Note that the default backend is normally sufficient. See [The builtin backends](https://matplotlib.org/stable/users/explain/figure/backends.html#the-builtin-backends)
 for a list of valid backends for each file format. Custom backends can be referenced as "module://...".

release\_mouse(_ax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1936-L1944)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.release_mouse "Link to this definition")

Release the mouse grab held by the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 _ax_.

Usually called by the widgets. It is ok to call this even if _ax_ doesn't have the mouse grab currently.

required\_interactive\_framework \= None[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.required_interactive_framework "Link to this definition")

property scroll\_pick\_id[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.scroll_pick_id "Link to this definition")

set\_cursor(_cursor_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1946-L1962)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.set_cursor "Link to this definition")

Set the current cursor.

This may have no effect if the backend does not display anything.

If required by the backend, this method should trigger an update in the backend event loop after the cursor is set, as this method may be called e.g. before a long-running task during which the GUI is not updated.

Parameters:

**cursor**[`Cursors`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")

The cursor to display over the canvas. Note: some backends may change the cursor for the entire window.

start\_event\_loop(_timeout\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2445-L2471)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.start_event_loop "Link to this definition")

Start a blocking event loop.

Such an event loop is used by interactive functions, such as [`ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.ginput.html#matplotlib.figure.Figure.ginput "matplotlib.figure.Figure.ginput")
 and [`waitforbuttonpress`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.waitforbuttonpress.html#matplotlib.figure.Figure.waitforbuttonpress "matplotlib.figure.Figure.waitforbuttonpress")
, to wait for events.

The event loop blocks until a callback function triggers [`stop_event_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.stop_event_loop "matplotlib.backend_bases.FigureCanvasBase.stop_event_loop")
, or _timeout_ is reached.

If _timeout_ is 0 or negative, never timeout.

Only interactive backends need to reimplement this method and it relies on [`flush_events`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events")
 being properly implemented.

Interactive backends should implement this in a more native way.

stop\_event\_loop()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2473-L2480)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.stop_event_loop "Link to this definition")

Stop the current blocking event loop.

Interactive backends need to reimplement this to match [`start_event_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.start_event_loop "matplotlib.backend_bases.FigureCanvasBase.start_event_loop")

supports\_blit \= False[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.supports_blit "Link to this definition")

class matplotlib.backend\_bases.FigureManagerBase(_canvas_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2704-L2914)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A backend-independent abstraction of a figure container and controller.

The figure manager is used by pyplot to interact with the window in a backend-independent way. It's an adapter for the real (GUI) framework that represents the visual figure on screen.

The figure manager is connected to a specific canvas instance, which in turn is connected to a specific figure instance. To access a figure manager for a given figure in user code, you typically use `fig.canvas.manager`.

GUI backends derive from this class to translate common operations such as _show_ or _resize_ to the GUI-specific code. Non-GUI backends do not support these operations and can just use the base class.

This following basic operations are accessible:

**Window operations**

*   [`show`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.show "matplotlib.backend_bases.FigureManagerBase.show")
    
*   [`destroy`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.destroy "matplotlib.backend_bases.FigureManagerBase.destroy")
    
*   [`full_screen_toggle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.full_screen_toggle "matplotlib.backend_bases.FigureManagerBase.full_screen_toggle")
    
*   [`resize`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.resize "matplotlib.backend_bases.FigureManagerBase.resize")
    
*   [`get_window_title`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.get_window_title "matplotlib.backend_bases.FigureManagerBase.get_window_title")
    
*   [`set_window_title`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.set_window_title "matplotlib.backend_bases.FigureManagerBase.set_window_title")
    

**Key and mouse button press handling**

The figure manager sets up default key and mouse button press handling by hooking up the [`key_press_handler`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.key_press_handler "matplotlib.backend_bases.key_press_handler")
 to the matplotlib event system. This ensures the same shortcuts and mouse actions across backends.

**Other operations**

Subclasses will have additional attributes and functions to access additional functionality. This is of course backend-specific. For example, most GUI backends have `window` and `toolbar` attributes that give access to the native GUI widgets of the respective framework.

Attributes:

**canvas**[`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")

The backend-specific canvas instance.

**num**int or str

The figure number.

**key\_press\_handler\_id**int

The default key handler cid, when using the toolmanager. To disable the default key press handling use:

figure.canvas.mpl\_disconnect(
    figure.canvas.manager.key\_press\_handler\_id)

**button\_press\_handler\_id**int

The default mouse button handler cid, when using the toolmanager. To disable the default button press handling use:

figure.canvas.mpl\_disconnect(
    figure.canvas.manager.button\_press\_handler\_id)

classmethod create\_with\_canvas(_canvas\_class_, _figure_, _num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2810-L2818)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.create_with_canvas "Link to this definition")

Create a manager for a given _figure_ using a specific _canvas\_class_.

Backends should override this method if they have specific needs for setting up the canvas or the manager.

destroy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2885-L2888)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.destroy "Link to this definition")

full\_screen\_toggle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2890-L2891)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.full_screen_toggle "Link to this definition")

get\_window\_title()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2896-L2898)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.get_window_title "Link to this definition")

Return the title text of the window containing the figure.

classmethod pyplot\_show(_\*_, _block\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2832-L2865)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.pyplot_show "Link to this definition")

Show all figures. This method is the implementation of [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
.

To customize the behavior of [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
, interactive backends should usually override [`start_main_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.start_main_loop "matplotlib.backend_bases.FigureManagerBase.start_main_loop")
; if more customized logic is necessary, [`pyplot_show`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.pyplot_show "matplotlib.backend_bases.FigureManagerBase.pyplot_show")
 can also be overridden.

Parameters:

**block**bool, optional

Whether to block by calling `start_main_loop`. The default, None, means to block if we are neither in IPython's `%pylab` mode nor in `interactive` mode.

resize(_w_, _h_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2893-L2894)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.resize "Link to this definition")

For GUI backends, resize the window (in physical pixels).

set\_window\_title(_title_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2900-L2914)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.set_window_title "Link to this definition")

Set the title text of the window containing the figure.

Examples

\>>> fig \= plt.figure()
\>>> fig.canvas.manager.set\_window\_title('My figure')

show()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2867-L2883)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.show "Link to this definition")

For GUI backends, show the figure window and redraw. For non-GUI backends, raise an exception, unless running headless (i.e. on Linux with an unset DISPLAY); this exception is converted to a warning in [`Figure.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
.

classmethod start\_main\_loop()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2820-L2830)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.start_main_loop "Link to this definition")

Start the main event loop.

This method is called by [`FigureManagerBase.pyplot_show`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.pyplot_show "matplotlib.backend_bases.FigureManagerBase.pyplot_show")
, which is the implementation of [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
. To customize the behavior of [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
, interactive backends should usually override [`start_main_loop`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.start_main_loop "matplotlib.backend_bases.FigureManagerBase.start_main_loop")
; if more customized logic is necessary, [`pyplot_show`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.pyplot_show "matplotlib.backend_bases.FigureManagerBase.pyplot_show")
 can also be overridden.

class matplotlib.backend\_bases.GraphicsContextBase[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L701-L1029)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

An abstract base class that provides color, line styles, etc.

copy\_properties(_gc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L724-L743)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.copy_properties "Link to this definition")

Copy properties from _gc_ to self.

get\_alpha()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L751-L756)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_alpha "Link to this definition")

Return the alpha value used for blending - not supported on all backends.

get\_antialiased()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L758-L760)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_antialiased "Link to this definition")

Return whether the object should try to do antialiased rendering.

get\_capstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L762-L764)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_capstyle "Link to this definition")

Return the [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
.

get\_clip\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L772-L785)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_clip_path "Link to this definition")

Return the clip path in the form (path, transform), where path is a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance, and transform is an affine transform to apply to the path before clipping.

get\_clip\_rectangle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L766-L770)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_clip_rectangle "Link to this definition")

Return the clip rectangle as a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 instance.

get\_dashes()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L787-L795)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_dashes "Link to this definition")

Return the dash style as an (offset, dash-list) pair.

See [`set_dashes`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_dashes "matplotlib.backend_bases.GraphicsContextBase.set_dashes")
 for details.

Default value is (None, None).

get\_forced\_alpha()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L797-L802)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_forced_alpha "Link to this definition")

Return whether the value given by get\_alpha() should be used to override any other alpha-channel values.

get\_gid()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L820-L822)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_gid "Link to this definition")

Return the object identifier if one is set, None otherwise.

get\_hatch()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L965-L967)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_hatch "Link to this definition")

Get the current hatch style.

get\_hatch\_color()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L976-L978)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_hatch_color "Link to this definition")

Get the hatch color.

get\_hatch\_linewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L984-L986)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_hatch_linewidth "Link to this definition")

Get the hatch linewidth.

get\_hatch\_path(_density\=6.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L969-L974)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_hatch_path "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for the current hatch.

get\_joinstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L804-L806)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_joinstyle "Link to this definition")

Return the [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
.

get\_linewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L808-L810)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_linewidth "Link to this definition")

Return the line width in points.

get\_rgb()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L812-L814)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_rgb "Link to this definition")

Return a tuple of three or four floats from 0-1.

get\_sketch\_params()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L992-L1010)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_sketch_params "Link to this definition")

Return the sketch parameters for the artist.

Returns:

tuple or [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

A 3-tuple with the following elements:

*   `scale`: The amplitude of the wiggle perpendicular to the source line.
    
*   `length`: The length of the wiggle along the line.
    
*   `randomness`: The scale factor by which the length is shrunken or expanded.
    

May return [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 if no sketch parameters were set.

get\_snap()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L824-L833)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_snap "Link to this definition")

Return the snap setting, which can be:

*   True: snap vertices to the nearest pixel center
    
*   False: leave vertices as-is
    
*   None: (auto) If the path contains only rectilinear line segments, round to the nearest pixel center
    

get\_url()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L816-L818)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_url "Link to this definition")

Return a url if one is set, None otherwise.

restore()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L745-L749)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.restore "Link to this definition")

Restore the graphics context from the stack - needed only for backends that save graphics contexts on a stack.

set\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L835-L850)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_alpha "Link to this definition")

Set the alpha value used for blending - not supported on all backends.

If `alpha=None` (the default), the alpha components of the foreground and fill colors will be used to set their respective transparencies (where applicable); otherwise, `alpha` will override them.

set\_antialiased(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L852-L855)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_antialiased "Link to this definition")

Set whether object should be drawn with antialiased rendering.

set\_capstyle(_cs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L857-L866)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_capstyle "Link to this definition")

Set how to draw endpoints of lines.

Parameters:

**cs**[`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or {'butt', 'projecting', 'round'}

set\_clip\_path(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L872-L875)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_clip_path "Link to this definition")

Set the clip path to a [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")
 or None.

set\_clip\_rectangle(_rectangle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L868-L870)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_clip_rectangle "Link to this definition")

Set the clip rectangle to a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 or None.

set\_dashes(_dash\_offset_, _dash\_list_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L877-L905)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_dashes "Link to this definition")

Set the dash style for the gc.

Parameters:

**dash\_offset**float

Distance, in points, into the dash pattern at which to start the pattern. It is usually set to 0.

**dash\_list**array-like or None

The on-off sequence as points. None specifies a solid line. All values must otherwise be non-negative (\\(\\ge 0\\)).

Notes

See p. 666 of the PostScript [Language Reference](https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf)
 for more info.

set\_foreground(_fg_, _isRGBA\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L907-L925)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_foreground "Link to this definition")

Set the foreground color.

Parameters:

**fg**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

**isRGBA**bool

If _fg_ is known to be an `(r, g, b, a)` tuple, _isRGBA_ can be set to True to improve performance.

set\_gid(_id_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L946-L948)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_gid "Link to this definition")

Set the id.

set\_hatch(_hatch_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L961-L963)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_hatch "Link to this definition")

Set the hatch style (for fills).

set\_hatch\_color(_hatch\_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L980-L982)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_hatch_color "Link to this definition")

Set the hatch color.

set\_hatch\_linewidth(_hatch\_linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L988-L990)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_hatch_linewidth "Link to this definition")

Set the hatch linewidth.

set\_joinstyle(_js_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L927-L936)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_joinstyle "Link to this definition")

Set how to draw connections between line segments.

Parameters:

**js**[`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 or {'miter', 'round', 'bevel'}

set\_linewidth(_w_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L938-L940)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_linewidth "Link to this definition")

Set the linewidth in points.

set\_sketch\_params(_scale\=None_, _length\=None_, _randomness\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1012-L1029)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_sketch_params "Link to this definition")

Set the sketch parameters.

Parameters:

**scale**float, optional

The amplitude of the wiggle perpendicular to the source line, in pixels. If scale is [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, or not provided, no sketch filter will be provided.

**length**float, default: 128

The length of the wiggle along the line, in pixels.

**randomness**float, default: 16

The scale factor by which the length is shrunken or expanded.

set\_snap(_snap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L950-L959)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_snap "Link to this definition")

Set the snap setting which may be:

*   True: snap vertices to the nearest pixel center
    
*   False: leave vertices as-is
    
*   None: (auto) If the path contains only rectilinear line segments, round to the nearest pixel center
    

set\_url(_url_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L942-L944)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_url "Link to this definition")

Set the url for links in compatible backends.

class matplotlib.backend\_bases.KeyEvent(_name_, _canvas_, _key_, _x\=0_, _y\=0_, _guiEvent\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1497-L1547)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "Link to this definition")

Bases: [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent")

A key event (key press, key release).

A KeyEvent has a number of special attributes in addition to those defined by the parent [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 and [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent")
 classes.

Attributes:

**key**None or str

The key(s) pressed. Could be _None_, a single case sensitive Unicode character ("g", "G", "#", etc.), a special key ("control", "shift", "f1", "up", etc.) or a combination of the above (e.g., "ctrl+alt+g", "ctrl+alt+G").

Notes

Modifier keys will be prefixed to the pressed key and will be in the order "ctrl", "alt", "super". The exception to this rule is when the pressed key is itself a modifier key, therefore "ctrl+alt" and "alt+control" can both be valid key values.

Examples

def on\_key(event):
    print('you pressed', event.key, event.xdata, event.ydata)

cid \= fig.canvas.mpl\_connect('key\_press\_event', on\_key)

class matplotlib.backend\_bases.LocationEvent(_name_, _canvas_, _x_, _y_, _guiEvent\=None_, _\*_, _modifiers\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1257-L1312)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "Link to this definition")

Bases: [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

An event that has a screen location.

A LocationEvent has a number of special attributes in addition to those defined by the parent [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 class.

Attributes:

**x, y**int or None

Event location in pixels from bottom left of canvas.

**inaxes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or None

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance over which the mouse is, if any.

**xdata, ydata**float or None

Data coordinates of the mouse within _inaxes_, or _None_ if the mouse is not over an Axes.

**modifiers**frozenset\[str\]

The keyboard modifiers currently being pressed (except for KeyEvent).

class matplotlib.backend\_bases.MouseButton(_\*values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1315-L1320)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "Link to this definition")

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python v3.14)")

BACK \= 8[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.BACK "Link to this definition")

FORWARD \= 9[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.FORWARD "Link to this definition")

LEFT \= 1[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.LEFT "Link to this definition")

MIDDLE \= 2[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.MIDDLE "Link to this definition")

RIGHT \= 3[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.RIGHT "Link to this definition")

class matplotlib.backend\_bases.MouseEvent(_name_, _canvas_, _x_, _y_, _button\=None_, _key\=None_, _step\=0_, _dblclick\=False_, _guiEvent\=None_, _\*_, _buttons\=None_, _modifiers\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1323-L1445)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "Link to this definition")

Bases: [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent")

A mouse event ('button\_press\_event', 'button\_release\_event', 'scroll\_event', 'motion\_notify\_event').

A MouseEvent has a number of special attributes in addition to those defined by the parent [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 and [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent")
 classes.

Attributes:

**button**None or [`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
 or {'up', 'down'}

The button pressed. 'up' and 'down' are used for scroll events.

Note that LEFT and RIGHT actually refer to the "primary" and "secondary" buttons, i.e. if the user inverts their left and right buttons ("left-handed setting") then the LEFT button will be the one physically on the right.

If this is unset, _name_ is "scroll\_event", and _step_ is nonzero, then this will be set to "up" or "down" depending on the sign of _step_.

**buttons**None or frozenset

For 'motion\_notify\_event', the mouse buttons currently being pressed (a set of zero or more MouseButtons); for other events, None.

Note

For 'motion\_notify\_event', this attribute is more accurate than the `button` (singular) attribute, which is obtained from the last 'button\_press\_event' or 'button\_release\_event' that occurred within the canvas (and thus 1. be wrong if the last change in mouse state occurred when the canvas did not have focus, and 2. cannot report when multiple buttons are pressed).

This attribute is not set for 'button\_press\_event' and 'button\_release\_event' because GUI toolkits are inconsistent as to whether they report the button state _before_ or _after_ the press/release occurred.

Warning

On macOS, the Tk backends only report a single button even if multiple buttons are pressed.

**key**None or str

The key pressed when the mouse event triggered, e.g. 'shift'. See [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent")
.

Warning

This key is currently obtained from the last 'key\_press\_event' or 'key\_release\_event' that occurred within the canvas. Thus, if the last change of keyboard state occurred while the canvas did not have focus, this attribute will be wrong. On the other hand, the `modifiers` attribute should always be correct, but it can only report on modifier keys.

**step**float

The number of scroll steps (positive for 'up', negative for 'down'). This applies only to 'scroll\_event' and defaults to 0 otherwise.

**dblclick**bool

Whether the event is a double-click. This applies only to 'button\_press\_event' and is False otherwise. In particular, it's not used in 'button\_release\_event'.

Examples

def on\_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)

cid \= fig.canvas.mpl\_connect('button\_press\_event', on\_press)

class matplotlib.backend\_bases.NavigationToolbar2(_canvas_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2929-L3441)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Base class for the navigation cursor, version 2.

Backends must implement a canvas that handles connections for 'button\_press\_event' and 'button\_release\_event'. See [`FigureCanvasBase.mpl_connect()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
 for more information.

They must also define

[`save_figure()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.save_figure "matplotlib.backend_bases.NavigationToolbar2.save_figure")

Save the current figure.

[`draw_rubberband()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.draw_rubberband "matplotlib.backend_bases.NavigationToolbar2.draw_rubberband")
 (optional)

Draw the zoom to rect "rubberband" rectangle.

[`set_message()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.set_message "matplotlib.backend_bases.NavigationToolbar2.set_message")
 (optional)

Display message.

[`set_history_buttons()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.set_history_buttons "matplotlib.backend_bases.NavigationToolbar2.set_history_buttons")
 (optional)

You can change the history back / forward buttons to indicate disabled / enabled state.

and override `__init__` to set up the toolbar -- without forgetting to call the base-class init. Typically, `__init__` needs to set up toolbar buttons connected to the [`home`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.home "matplotlib.backend_bases.NavigationToolbar2.home")
, [`back`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.back "matplotlib.backend_bases.NavigationToolbar2.back")
, [`forward`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.forward "matplotlib.backend_bases.NavigationToolbar2.forward")
, [`pan`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.pan "matplotlib.backend_bases.NavigationToolbar2.pan")
, [`zoom`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.zoom "matplotlib.backend_bases.NavigationToolbar2.zoom")
, and [`save_figure`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.save_figure "matplotlib.backend_bases.NavigationToolbar2.save_figure")
 methods and using standard icons in the "images" subdirectory of the data path.

That's it, we'll do the rest!

UNKNOWN\_SAVED\_STATUS \= <object object>[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS "Link to this definition")

back(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3029-L3039)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.back "Link to this definition")

Move back up the view lim stack.

For convenience of being directly connected as a GUI callback, which often get passed additional parameters, this method accepts arbitrary parameters, but does not use them.

configure\_subplots(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3389-L3410)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.configure_subplots "Link to this definition")

drag\_pan(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3221-L3232)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.drag_pan "Link to this definition")

Callback for dragging in pan/zoom mode.

drag\_zoom(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3287-L3310)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.drag_zoom "Link to this definition")

Callback for dragging in zoom mode.

draw\_rubberband(_event_, _x0_, _y0_, _x1_, _y1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3007-L3012)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.draw_rubberband "Link to this definition")

Draw a rectangle rubberband to indicate zoom limits.

Note that it is not guaranteed that `x0 <= x1` and `y0 <= y1`.

forward(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3041-L3051)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.forward "Link to this definition")

Move forward in the view lim stack.

For convenience of being directly connected as a GUI callback, which often get passed additional parameters, this method accepts arbitrary parameters, but does not use them.

home(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3017-L3027)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.home "Link to this definition")

Restore the original view.

For convenience of being directly connected as a GUI callback, which often get passed additional parameters, this method accepts arbitrary parameters, but does not use them.

mouse\_move(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3114-L3116)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.mouse_move "Link to this definition")

pan(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3183-L3197)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.pan "Link to this definition")

Toggle the pan/zoom tool.

Pan with left button, zoom with right.

press\_pan(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3201-L3219)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.press_pan "Link to this definition")

Callback for mouse button press in pan/zoom mode.

press\_zoom(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3261-L3285)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.press_zoom "Link to this definition")

Callback for mouse button press in zoom to rect mode.

push\_current()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3360-L3369)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.push_current "Link to this definition")

Push the current view limits and position onto the stack.

release\_pan(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3234-L3245)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.release_pan "Link to this definition")

Callback for mouse button release in pan/zoom mode.

release\_zoom(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3312-L3350)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.release_zoom "Link to this definition")

Callback for mouse button release in zoom to rect mode.

remove\_rubberband()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3014-L3015)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.remove_rubberband "Link to this definition")

Remove the rubberband.

save\_figure(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3412-L3433)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.save_figure "Link to this definition")

Save the current figure.

Backend implementations may choose to return the absolute path of the saved file, if any, as a string.

If no file is created then [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 is returned.

If the backend does not implement this functionality then [`NavigationToolbar2.UNKNOWN_SAVED_STATUS`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS "matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS")
 is returned.

Returns:

str or [`NavigationToolbar2.UNKNOWN_SAVED_STATUS`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS "matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS")
 or [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

The filepath of the saved figure. Returns [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 if figure is not saved. Returns [`NavigationToolbar2.UNKNOWN_SAVED_STATUS`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS "matplotlib.backend_bases.NavigationToolbar2.UNKNOWN_SAVED_STATUS")
 when the backend does not provide the information.

set\_history\_buttons()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3440-L3441)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.set_history_buttons "Link to this definition")

Enable or disable the back/forward button.

set\_message(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3004-L3005)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.set_message "Link to this definition")

Display a message on toolbar or in status bar.

toolitems \= (('Home', 'Reset original view', 'home', 'home'), ('Back', 'Back to previous view', 'back', 'back'), ('Forward', 'Forward to next view', 'forward', 'forward'), (None, None, None, None), ('Pan', 'Left button pans, Right button zooms\\nx/y fixes axis, CTRL fixes aspect', 'move', 'pan'), ('Zoom', 'Zoom to rectangle\\nx/y fixes axis', 'zoom\_to\_rect', 'zoom'), ('Subplots', 'Configure subplots', 'subplots', 'configure\_subplots'), (None, None, None, None), ('Save', 'Save the figure', 'filesave', 'save\_figure'))[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.toolitems "Link to this definition")

update()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3435-L3438)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.update "Link to this definition")

Reset the Axes stack.

zoom(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3247-L3257)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2.zoom "Link to this definition")

exception matplotlib.backend\_bases.NonGuiException[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2699-L2701)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NonGuiException "Link to this definition")

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")

Raised when trying show a figure in a non-GUI backend.

class matplotlib.backend\_bases.PickEvent(_name_, _canvas_, _mouseevent_, _artist_, _guiEvent\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1448-L1494)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent "Link to this definition")

Bases: [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

A pick event.

This event is fired when the user picks a location on the canvas sufficiently close to an artist that has been made pickable with [`Artist.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker")
.

A PickEvent has a number of special attributes in addition to those defined by the parent [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 class.

Attributes:

**mouseevent**[`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

The mouse event that generated the pick.

**artist**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The picked artist. Note that artists are not pickable by default (see [`Artist.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker")
).

**other**

Additional attributes may be present depending on the type of the picked object; e.g., a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 pick may define different extra attributes than a [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 pick.

Examples

Bind a function `on_pick()` to pick events, that prints the coordinates of the picked data point:

ax.plot(np.rand(100), 'o', picker\=5)  \# 5 points tolerance

def on\_pick(event):
    line \= event.artist
    xdata, ydata \= line.get\_data()
    ind \= event.ind
    print(f'on pick line: {xdata\[ind\]:.3f}, {ydata\[ind\]:.3f}')

cid \= fig.canvas.mpl\_connect('pick\_event', on\_pick)

class matplotlib.backend\_bases.RendererBase[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L134-L698)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

An abstract base class to handle drawing/rendering operations.

The following methods must be implemented in the backend for full functionality (though just implementing [`draw_path`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
 alone would give a highly capable backend):

*   [`draw_path`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
    
*   [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
    
*   [`draw_gouraud_triangles`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_gouraud_triangles "matplotlib.backend_bases.RendererBase.draw_gouraud_triangles")
    

The following methods _should_ be implemented in the backend for optimization reasons:

*   [`draw_text`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_text "matplotlib.backend_bases.RendererBase.draw_text")
    
*   [`draw_markers`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_markers "matplotlib.backend_bases.RendererBase.draw_markers")
    
*   [`draw_path_collection`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path_collection "matplotlib.backend_bases.RendererBase.draw_path_collection")
    
*   [`draw_quad_mesh`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_quad_mesh "matplotlib.backend_bases.RendererBase.draw_quad_mesh")
    

close\_group(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L168-L173)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.close_group "Link to this definition")

Close a grouping element with label _s_.

Only used by the SVG renderer.

draw\_gouraud\_triangles(_gc_, _triangles\_array_, _colors\_array_, _transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L282-L298)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_gouraud_triangles "Link to this definition")

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

draw\_image(_gc_, _x_, _y_, _im_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L438-L469)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "Link to this definition")

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

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _trans_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L179-L208)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
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

draw\_path(_gc_, _path_, _transform_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L175-L177)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_path\_collection(_gc_, _master\_transform_, _paths_, _all\_transforms_, _offsets_, _offset\_trans_, _facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiaseds_, _urls_, _offset\_position_, _\*_, _hatchcolors\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L210-L259)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path_collection "Link to this definition")

Draw a collection of _paths_.

Each path is first transformed by the corresponding entry in _all\_transforms_ (a list of (3, 3) matrices) and then by _master\_transform_. They are then translated by the corresponding entry in _offsets_, which has been first transformed by _offset\_trans_.

_facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiased_ and _hatchcolors_ are lists that set the corresponding properties.

Added in version 3.11: Allow _hatchcolors_ to be specified.

_offset\_position_ is unused now, but the argument is kept for backwards compatibility.

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
. Backends may want to override this in order to render each set of path data only once, and then reference that path multiple times with the different offsets, colors, styles etc. The generator methods `_iter_collection_raw_paths` and `_iter_collection` are provided to help with (and standardize) the implementation across backends. It is highly recommended to use those generators, so that changes to the behavior of [`draw_path_collection`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path_collection "matplotlib.backend_bases.RendererBase.draw_path_collection")
 can be made globally.

draw\_quad\_mesh(_gc_, _master\_transform_, _meshWidth_, _meshHeight_, _coordinates_, _offsets_, _offsetTrans_, _facecolors_, _antialiased_, _edgecolors_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L261-L280)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_quad_mesh "Link to this definition")

Draw a quadmesh.

The base (fallback) implementation converts the quadmesh to paths and then calls [`draw_path_collection`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path_collection "matplotlib.backend_bases.RendererBase.draw_path_collection")
.

draw\_tex(_gc_, _x_, _y_, _s_, _prop_, _angle_, _\*_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L488-L509)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_tex "Link to this definition")

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

draw\_text(_gc_, _x_, _y_, _s_, _prop_, _angle_, _ismath\=False_, _mtext\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L511-L543)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_text "Link to this definition")

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

flipy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L609-L615)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.flipy "Link to this definition")

Return whether y values increase from top to bottom.

Note that this only affects drawing of texts.

get\_canvas\_width\_height()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L617-L619)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.get_canvas_width_height "Link to this definition")

Return the canvas width and height in display coords.

get\_image\_magnification()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L430-L436)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.get_image_magnification "Link to this definition")

Get the factor by which to magnify images passed to [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
. Allows a backend to have images at a different resolution to other artists.

get\_texmanager()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L621-L625)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.get_texmanager "Link to this definition")

Return the [`TexManager`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "matplotlib.texmanager.TexManager")
 instance.

get\_text\_width\_height\_descent(_s_, _prop_, _ismath_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L578-L607)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.get_text_width_height_descent "Link to this definition")

Get the width, height, and descent (offset from the bottom to the baseline), in display coords, of the string _s_ with [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 _prop_.

Whitespace at the start and the end of _s_ is included in the reported width.

new\_gc()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L627-L629)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.new_gc "Link to this definition")

Return an instance of a [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
.

open\_group(_s_, _gid\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L161-L166)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.open_group "Link to this definition")

Open a grouping element with label _s_ and _gid_ (if set) as id.

Only used by the SVG renderer.

option\_image\_nocomposite()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L471-L479)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.option_image_nocomposite "Link to this definition")

Return whether image composition by Matplotlib should be skipped.

Raster backends should usually return False (letting the C-level rasterizer take care of image composition); vector backends should usually return `not rcParams["image.composite_image"]`.

option\_scale\_image()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L481-L486)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.option_scale_image "Link to this definition")

Return whether arbitrary affine transformations in [`draw_image`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
 are supported (True for most vector backends).

points\_to\_pixels(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L631-L649)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.points_to_pixels "Link to this definition")

Convert points to display units.

You need to override this function (unless your backend doesn't have a dpi, e.g., postscript or svg). Some imaging systems assume some value for pixels per inch:

points to pixels \= points \* pixels\_per\_inch/72 \* dpi/72

Parameters:

**points**float or array-like

Returns:

Points converted to pixels

start\_filter()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L666-L671)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.start_filter "Link to this definition")

Switch to a temporary renderer for image filtering effects.

Currently only supported by the agg renderer.

start\_rasterizing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L651-L656)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.start_rasterizing "Link to this definition")

Switch to the raster renderer.

Used by [`MixedModeRenderer`](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer "matplotlib.backends.backend_mixed.MixedModeRenderer")
.

stop\_filter(_filter\_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L673-L680)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.stop_filter "Link to this definition")

Switch back to the original renderer. The contents of the temporary renderer is processed with the _filter\_func_ and is drawn on the original renderer as an image.

Currently only supported by the agg renderer.

stop\_rasterizing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L658-L664)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.stop_rasterizing "Link to this definition")

Switch back to the vector renderer and draw the contents of the raster renderer as an image on the vector renderer.

Used by [`MixedModeRenderer`](https://matplotlib.org/stable/api/backend_mixed_api.html#matplotlib.backends.backend_mixed.MixedModeRenderer "matplotlib.backends.backend_mixed.MixedModeRenderer")
.

class matplotlib.backend\_bases.ResizeEvent(_name_, _canvas_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1233-L1250)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ResizeEvent "Link to this definition")

Bases: [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

An event triggered by a canvas resize.

A ResizeEvent has a number of special attributes in addition to those defined by the parent [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 class.

Attributes:

**width**int

Width of the canvas in pixels.

**height**int

Height of the canvas in pixels.

class matplotlib.backend\_bases.ShowBase[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3737-L3745)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ShowBase "Link to this definition")

Bases: `_Backend`

Simple base class to generate a `show()` function in backends.

Subclass must override `mainloop()` method.

class matplotlib.backend\_bases.TimerBase(_interval\=None_, _callbacks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1032-L1175)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A base class for providing timer events, useful for things animations. Backends need to implement a few specific methods in order to use their own timing mechanisms so that the timer events are integrated into their event loops.

Subclasses must override the following methods:

*   `_timer_start`: Backend-specific code for starting the timer.
    
*   `_timer_stop`: Backend-specific code for stopping the timer.
    

Subclasses may additionally override the following methods:

*   `_timer_set_single_shot`: Code for setting the timer to single shot operating mode, if supported by the timer object. If not, the [`TimerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase "matplotlib.backend_bases.TimerBase")
     class itself will store the flag and the `_on_timer` method should be overridden to support such behavior.
    
*   `_timer_set_interval`: Code for setting the interval on the timer, if there is a method for doing so on the timer object.
    
*   `_on_timer`: The internal function that any timer object should call, which will handle the task of running all callbacks that have been set.
    

Parameters:

**interval**int, default: 1000ms

The time between timer events in milliseconds. Will be stored as `timer.interval`.

**callbacks**list\[tuple\[callable, tuple, dict\]\]

List of (func, args, kwargs) tuples that will be called upon timer events. This list is accessible as `timer.callbacks` and can be manipulated directly, or the functions [`add_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.add_callback "matplotlib.backend_bases.TimerBase.add_callback")
 and [`remove_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.remove_callback "matplotlib.backend_bases.TimerBase.remove_callback")
 can be used.

add\_callback(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1118-L1127)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.add_callback "Link to this definition")

Register _func_ to be called by timer when the event fires. Any additional arguments provided will be passed to _func_.

This function returns _func_, which makes it possible to use it as a decorator.

property interval[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.interval "Link to this definition")

The time between timer events, in milliseconds.

remove\_callback(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1129-L1150)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.remove_callback "Link to this definition")

Remove _func_ from list of callbacks.

_args_ and _kwargs_ are optional and used to distinguish between copies of the same function registered to be called with different arguments. This behavior is deprecated. In the future, `*args, **kwargs` won't be considered anymore; to keep a specific callback removable by itself, pass it to [`add_callback`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.add_callback "matplotlib.backend_bases.TimerBase.add_callback")
 as a [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.14)")
 object.

property single\_shot[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.single_shot "Link to this definition")

Whether this timer should stop after a single run.

start()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1080-L1082)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.start "Link to this definition")

Start the timer.

stop()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L1084-L1086)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.TimerBase.stop "Link to this definition")

Stop the timer.

class matplotlib.backend\_bases.ToolContainerBase(_toolmanager_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3444-L3630)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Base class for all tool containers, e.g. toolbars.

Attributes:

**toolmanager**[`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")

The tools with which this [`ToolContainerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "matplotlib.backend_bases.ToolContainerBase")
 wants to communicate.

add\_tool(_tool_, _group_, _position\=\-1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3478-L3501)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.add_tool "Link to this definition")

Add a tool to this container.

Parameters:

**tool**tool\_like

The tool to add, see [`ToolManager.get_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.get_tool "matplotlib.backend_managers.ToolManager.get_tool")
.

**group**str

The name of the group to add this tool to.

**position**int, default: -1

The position within the group to place this tool.

add\_toolitem(_name_, _group_, _position_, _image_, _description_, _toggle_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3539-L3573)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.add_toolitem "Link to this definition")

A hook to add a toolitem to the container.

This hook must be implemented in each backend and contains the backend-specific code to add an element to the toolbar.

Warning

This is part of the backend implementation and should not be called by end-users. They should instead call [`ToolContainerBase.add_tool`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.add_tool "matplotlib.backend_bases.ToolContainerBase.add_tool")
.

The callback associated with the button click event must be _exactly_ `self.trigger_tool(name)`.

Parameters:

**name**str

Name of the tool to add, this gets used as the tool's ID and as the default label of the buttons.

**group**str

Name of the group that this tool belongs to.

**position**int

Position of the tool within its group, if -1 it goes at the end.

**image**str

Filename of the image for the button or [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
.

**description**str

Description of the tool, used for the tooltips.

**toggle**bool

*   [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
     : The button is a toggle (change the pressed/unpressed state between consecutive clicks).
    
*   [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
     : The button is a normal button (returns to unpressed state after release).
    

remove\_toolitem(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3597-L3619)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.remove_toolitem "Link to this definition")

A hook to remove a toolitem from the container.

This hook must be implemented in each backend and contains the backend-specific code to remove an element from the toolbar; it is called when [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 emits a `tool_removed_event`.

Because some tools are present only on the [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 but not on the [`ToolContainerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "matplotlib.backend_bases.ToolContainerBase")
, this method must be a no-op when called on a tool absent from the container.

Warning

This is part of the backend implementation and should not be called by end-users. They should instead call [`ToolManager.remove_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.remove_tool "matplotlib.backend_managers.ToolManager.remove_tool")
.

Parameters:

**name**str

Name of the tool to remove.

set\_message(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3621-L3630)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.set_message "Link to this definition")

Display a message on the toolbar.

Parameters:

**s**str

Message text.

toggle\_toolitem(_name_, _toggled_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3575-L3595)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.toggle_toolitem "Link to this definition")

A hook to toggle a toolitem without firing an event.

This hook must be implemented in each backend and contains the backend-specific code to silently toggle a toolbar element.

Warning

This is part of the backend implementation and should not be called by end-users. They should instead call [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
 or [`ToolContainerBase.trigger_tool`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.trigger_tool "matplotlib.backend_bases.ToolContainerBase.trigger_tool")
 (which are equivalent).

Parameters:

**name**str

Id of the tool to toggle.

**toggled**bool

Whether to set this tool as toggled or not.

trigger\_tool(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L3528-L3537)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.trigger_tool "Link to this definition")

Trigger the tool.

Parameters:

**name**str

Name (id) of the tool triggered from within the container.

matplotlib.backend\_bases.button\_press\_handler(_event_, _canvas\=None_, _toolbar\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2624-L2640)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.button_press_handler "Link to this definition")

The default Matplotlib button actions for extra mouse buttons.

Parameters are as for [`key_press_handler`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.key_press_handler "matplotlib.backend_bases.key_press_handler")
, except that _event_ is a [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
.

matplotlib.backend\_bases.get\_registered\_canvas\_class(_format_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L120-L131)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.get_registered_canvas_class "Link to this definition")

Return the registered default canvas for given file format. Handles deferred import of required backend.

matplotlib.backend\_bases.key\_press\_handler(_event_, _canvas\=None_, _toolbar\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2483-L2621)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.key_press_handler "Link to this definition")

Implement the default Matplotlib key bindings for the canvas and toolbar described at [Navigation keyboard shortcuts](https://matplotlib.org/stable/users/explain/figure/interactive.html#key-event-handling)
.

Parameters:

**event**[`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent")

A key press/release event.

**canvas**[`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
, default: `event.canvas`

The backend-specific canvas instance. This parameter is kept for back-compatibility, but, if set, should always be equal to `event.canvas`.

**toolbar**[`NavigationToolbar2`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "matplotlib.backend_bases.NavigationToolbar2")
, default: `event.canvas.toolbar`

The navigation cursor toolbar. This parameter is kept for back-compatibility, but, if set, should always be equal to `event.canvas.toolbar`.

matplotlib.backend\_bases.register\_backend(_format_, _backend_, _description\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L101-L117)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.register_backend "Link to this definition")

Register a backend for saving to a given file format.

Parameters:

**format**str

File extension

**backend**module string or canvas class

Backend for handling file output

**description**str, default: ""

Description of the file type.

matplotlib.backend\_bases.scroll\_handler(_event_, _canvas\=None_, _toolbar\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_bases.py#L2643-L2696)
[#](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.scroll_handler "Link to this definition")

On this page