[Skip to main content](https://matplotlib.org/stable/users/explain/figure/interactive.html#main-content)

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
    

Interactive figures[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-figures "Link to this heading")

=======================================================================================================================================

Interactivity can be invaluable when exploring plots. The pan/zoom and mouse-location tools built into the Matplotlib GUI windows are often sufficient, but you can also use the event system to build customized data exploration tools.

See also

[Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-intro)
.

Matplotlib ships with [backends](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
 binding to several GUI toolkits (Qt, Tk, Wx, GTK, macOS, JavaScript) and third party packages provide bindings to [kivy](https://github.com/kivy-garden/garden.matplotlib)
 and [Jupyter Lab](https://matplotlib.org/ipympl)
. For the figures to be responsive to mouse, keyboard, and paint events, the GUI event loop needs to be integrated with an interactive prompt. We recommend using IPython (see [below](https://matplotlib.org/stable/users/explain/figure/interactive.html#ipython-pylab)
).

The [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 module provides functions for explicitly creating figures that include interactive tools, a toolbar, a tool-tip, and [key bindings](https://matplotlib.org/stable/users/explain/figure/interactive.html#key-event-handling)
:

[`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")

Creates a new empty [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or selects an existing figure

[`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Creates a new [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 and fills it with a grid of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

[`pyplot.gcf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf")

Get the current [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. If there is current no figure on the pyplot figure stack, a new figure is created

[`pyplot.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")

Get the current [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. If there is current no Axes on the Figure, a new one is created

Almost all of the functions in [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 pass through the current [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 / [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 (or create one) as appropriate.

Matplotlib keeps a reference to all of the open figures created via [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 or [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 so that the figures will not be garbage collected. [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
s can be closed and deregistered from [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 individually via [`pyplot.close`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
; all open [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
s can be closed via `plt.close('all')`.

See also

For more discussion of Matplotlib's event system and integrated event loops: - [Interactive figures and asynchronous programming](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#interactive-figures-and-eventloops)
 - [Event handling and picking](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling)

IPython integration[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#ipython-integration "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

We recommend using IPython for an interactive shell. In addition to all of its features (improved tab-completion, magics, multiline editing, etc), it also ensures that the GUI toolkit event loop is properly integrated with the command line (see [Command prompt integration](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html#cp-integration)
).

In this example, we create and modify a figure via an IPython prompt. The figure displays in a QtAgg GUI window. To configure the integration and enable [interactive mode](https://matplotlib.org/stable/users/explain/figure/interactive.html#controlling-interactive)
 use the `%matplotlib` magic:

In \[1\]: %matplotlib
Using matplotlib backend: QtAgg

In \[2\]: import matplotlib.pyplot as plt

Create a new figure window:

In \[3\]: fig, ax \= plt.subplots()

Add a line plot of the data to the window:

In \[4\]: ln, \= ax.plot(range(5))

Change the color of the line from blue to orange:

In \[5\]: ln.set\_color('orange')

If you wish to disable automatic redrawing of the plot:

In \[6\]: plt.ioff()

If you wish to re-enable automatic redrawing of the plot:

In \[7\]: plt.ion()

In recent versions of `Matplotlib` and `IPython`, it is sufficient to import [`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 and call [`pyplot.ion`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "matplotlib.pyplot.ion")
. Using the `%` magic is guaranteed to work in all versions of Matplotlib and IPython.

Interactive mode[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-mode "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`pyplot.ion`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "matplotlib.pyplot.ion") | Enable interactive mode. |
| [`pyplot.ioff`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ioff.html#matplotlib.pyplot.ioff "matplotlib.pyplot.ioff") | Disable interactive mode. |
| [`pyplot.isinteractive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive "matplotlib.pyplot.isinteractive") | Return whether plots are updated after every plotting command. |

|     |     |
| --- | --- |
| [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show") | Display all open figures. |
| [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause") | Run the GUI event loop for _interval_ seconds. |

Interactive mode controls:

*   whether created figures are automatically shown
    
*   whether changes to artists automatically trigger re-drawing existing figures
    
*   when [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
     returns if given no arguments: immediately, or after all of the figures have been closed
    

If in interactive mode:

*   newly created figures will be displayed immediately
    
*   figures will automatically redraw when elements are changed
    
*   [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
     displays the figures and immediately returns
    

If not in interactive mode:

*   newly created figures and changes to figures are not displayed until
    
    *   [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
         is called
        
    *   [`pyplot.pause()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
         is called
        
    *   [`FigureCanvasBase.flush_events()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events")
         is called
        
*   [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
     runs the GUI event loop and does not return until all the plot windows are closed
    

If you are in non-interactive mode (or created figures while in non-interactive mode) you may need to explicitly call [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
 to display the windows on your screen. If you only want to run the GUI event loop for a fixed amount of time, you can use [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
. This will block the progress of your code as if you had called [`time.sleep`](https://docs.python.org/3/library/time.html#time.sleep "(in Python v3.14)")
, ensure the current window is shown and re-drawn if needed, and run the GUI event loop for the specified period of time.

The GUI event loop being integrated with your command prompt and the figures being in interactive mode are independent of each other. If you try to use [`pyplot.ion`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "matplotlib.pyplot.ion")
 without arranging for the event-loop integration, your figures will appear but will not be interactive while the prompt is waiting for input. You will not be able to pan/zoom and the figure may not even render (the window might appear black, transparent, or as a snapshot of the desktop under it). Conversely, if you configure the event loop integration, displayed figures will be responsive while waiting for input at the prompt, regardless of pyplot's "interactive mode".

No matter what combination of interactive mode setting and event loop integration, figures will be responsive if you use `pyplot.show(block=True)`, [`pyplot.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
, or run the GUI main loop in some other way.

Warning

Using [`Figure.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
, it is possible to display a figure on the screen without starting the event loop and without being in interactive mode. This may work (depending on the GUI toolkit) but will likely result in a non-responsive figure.

Default UI[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#default-ui "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

The windows created by [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 have an interactive toolbar with navigation buttons and a readout of the data values the cursor is pointing at.

Interactive navigation[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-navigation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

![../../../_images/toolbar.png](https://matplotlib.org/stable/_images/toolbar.png)

All figure windows come with a navigation toolbar, which can be used to navigate through the data set.

![../../../_images/home_large.png](https://matplotlib.org/stable/_images/home_large.png) ![../../../_images/back_large.png](https://matplotlib.org/stable/_images/back_large.png) ![../../../_images/forward_large.png](https://matplotlib.org/stable/_images/forward_large.png)

The `Home`, `Forward` and `Back` buttons

These are similar to a web browser's home, forward and back controls. `Forward` and `Back` are used to navigate back and forth between previously defined views. They have no meaning unless you have already navigated somewhere else using the pan and zoom buttons. This is analogous to trying to click `Back` on your web browser before visiting a new page or `Forward` before you have gone back to a page -- nothing happens. `Home` takes you to the first, default view of your data.

![../../../_images/move_large.png](https://matplotlib.org/stable/_images/move_large.png)

The `Pan/Zoom` button

This button has two modes: pan and zoom. Click the `Pan/Zoom` button to activate panning and zooming, then put your mouse somewhere over an axes. Press the left mouse button and hold it to pan the figure, dragging it to a new position. When you release it, the data under the point where you pressed will be moved to the point where you released. If you press 'x' or 'y' while panning the motion will be constrained to the x or y axis, respectively. Press the right mouse button to zoom, dragging it to a new position. The x axis will be zoomed in proportionately to the rightward movement and zoomed out proportionately to the leftward movement. The same is true for the y axis and up/down motions (up zooms in, down zooms out). The point under your mouse when you begin the zoom remains stationary, allowing you to zoom in or out around that point as much as you wish. You can use the modifier keys 'x', 'y' or 'CONTROL' to constrain the zoom to the x axis, the y axis, or aspect ratio preserve, respectively.

With polar plots, the pan and zoom functionality behaves differently. The radius axis labels can be dragged using the left mouse button. The radius scale can be zoomed in and out using the right mouse button.

![../../../_images/zoom_to_rect_large.png](https://matplotlib.org/stable/_images/zoom_to_rect_large.png)

The `Zoom-to-Rectangle` button

Put your mouse somewhere over an axes and press a mouse button. Define a rectangular region by dragging the mouse while holding the button to a new location. When using the left mouse button, the axes view limits will be zoomed to the defined region. When using the right mouse button, the axes view limits will be zoomed out, placing the original axes in the defined region.

![../../../_images/subplots_large.png](https://matplotlib.org/stable/_images/subplots_large.png)

The `Subplot-configuration` button

Use this button to configure the appearance of the subplot. You can stretch or compress the left, right, top, or bottom side of the subplot, or the space between the rows or space between the columns.

![../../../_images/filesave_large.png](https://matplotlib.org/stable/_images/filesave_large.png)

The `Save` button

Click this button to launch a file save dialog. You can save files with the following extensions: `png`, `ps`, `eps`, `svg` and `pdf`.

### Navigation keyboard shortcuts[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#navigation-keyboard-shortcuts "Link to this heading")

A number of helpful keybindings are registered by default. The following table holds all the default keys, which can be overwritten by use of your [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
.

| Command | Default key binding and rcParam |
| --- | --- |
| Home/Reset | `[rcParams["keymap.home"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.home#rcparam-keymap-home) ` (default: `['h', 'r', 'home']`) |
| Back | `[rcParams["keymap.back"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.back#rcparam-keymap-back) ` (default: `['left', 'c', 'backspace', 'MouseButton.BACK']`) |
| Forward | `[rcParams["keymap.forward"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.forward#rcparam-keymap-forward) ` (default: `['right', 'v', 'MouseButton.FORWARD']`) |
| Pan/Zoom | `[rcParams["keymap.pan"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.pan#rcparam-keymap-pan) ` (default: `['p']`) |
| Zoom-to-rect | `[rcParams["keymap.zoom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.zoom#rcparam-keymap-zoom) ` (default: `['o']`) |
| Save | `[rcParams["keymap.save"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.save#rcparam-keymap-save) ` (default: `['s', 'ctrl+s']`) |
| Toggle fullscreen | `[rcParams["keymap.fullscreen"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.fullscreen#rcparam-keymap-fullscreen) ` (default: `['f', 'ctrl+f']`) |
| Toggle major grids | `[rcParams["keymap.grid"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.grid#rcparam-keymap-grid) ` (default: `['g']`) |
| Toggle minor grids | `[rcParams["keymap.grid_minor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.grid_minor#rcparam-keymap-grid-minor) ` (default: `['G']`) |
| Toggle x axis scale (log/linear) | `[rcParams["keymap.xscale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.xscale#rcparam-keymap-xscale) ` (default: `['k', 'L']`) |
| Toggle y axis scale (log/linear) | `[rcParams["keymap.yscale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.yscale#rcparam-keymap-yscale) ` (default: `['l']`) |
| Close Figure | `[rcParams["keymap.quit"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=keymap.quit#rcparam-keymap-quit) ` (default: `['ctrl+w', 'cmd+w', 'q']`) |
| Constrain pan/zoom to x axis | hold **x** when panning/zooming with mouse |
| Constrain pan/zoom to y axis | hold **y** when panning/zooming with mouse |
| Preserve aspect ratio | hold **CONTROL** when panning/zooming with mouse |

Other Python prompts[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#other-python-prompts "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Interactive mode works in the default Python prompt:

\>>> import matplotlib.pyplot as plt
\>>> plt.ion()
\>>>

However, this does not ensure that the event hook is properly installed and your figures may not be responsive. Please consult the documentation of your GUI toolkit for details.

### Jupyter Notebooks / JupyterLab[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#jupyter-notebooks-jupyterlab "Link to this heading")

To get interactive figures in the 'classic' notebook or Jupyter lab, use the [ipympl](https://matplotlib.org/ipympl)
 backend (must be installed separately) which uses the **ipywidget** framework. If `ipympl` is installed use the magic:

%matplotlib widget

to select and enable it.

If you only need to use the classic notebook (i.e. `notebook<7`), you can use

%matplotlib notebook

which uses the [`backend_nbagg`](https://matplotlib.org/stable/api/backend_nbagg_api.html#module-matplotlib.backends.backend_nbagg "matplotlib.backends.backend_nbagg")
 backend provided by Matplotlib; however, nbagg does not work in Jupyter Lab.

Note

To get the interactive functionality described here, you must be using an interactive backend. The default backend in notebooks, the inline backend, is not. `ipykernel.pylab.backend_inline` renders the figure once and inserts a static image into the notebook when the cell is executed. Because the images are static, they cannot be panned / zoomed, take user input, or be updated from other cells.

#### GUIs + Jupyter[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#guis-jupyter "Link to this heading")

You can also use one of the non-`ipympl` GUI backends in a Jupyter Notebook. If you are running your Jupyter kernel locally, the GUI window will spawn on your desktop adjacent to your web browser. If you run your notebook on a remote server, the kernel will try to open the GUI window on the remote computer. Unless you have arranged to forward the xserver back to your desktop, you will not be able to see or interact with the window. It may also raise an exception.

### PyCharm, Spyder, and VSCode[#](https://matplotlib.org/stable/users/explain/figure/interactive.html#pycharm-spyder-and-vscode "Link to this heading")

Many IDEs have built-in integration with Matplotlib, please consult their documentation for configuration details.

On this page