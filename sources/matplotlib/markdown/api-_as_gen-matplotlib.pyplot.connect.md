[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.connect.html#main-content)

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
    

matplotlib.pyplot.connect[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.connect.html#matplotlib-pyplot-connect "Link to this heading")

========================================================================================================================================================

matplotlib.pyplot.connect(_s_, _func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1258-L1260)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.connect.html#matplotlib.pyplot.connect "Link to this definition")

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

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`FigureCanvasBase.mpl_connect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
.

Examples

def on\_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)

cid \= canvas.mpl\_connect('button\_press\_event', on\_press)

Examples using `matplotlib.pyplot.connect`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.connect.html#examples-using-matplotlib-pyplot-connect "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_coords_demo_thumb.png)

[Mouse move and click events](https://matplotlib.org/stable/gallery/event_handling/coords_demo.html)

Mouse move and click events

On this page