[Skip to main content](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#main-content)

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
    

Writing a backend -- the pyplot interface[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#writing-a-backend-the-pyplot-interface "Link to this heading")

=======================================================================================================================================================================================================

This page assumes general understanding of the information in the [Backends](https://matplotlib.org/stable/users/explain/figure/backends.html#backends)
 page, and is instead intended as reference for third-party backend implementers. It also only deals with the interaction between backends and [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
, not with the rendering side, which is described in [`backend_template`](https://matplotlib.org/stable/api/backend_template_api.html#module-matplotlib.backends.backend_template "matplotlib.backends.backend_template")
.

There are two APIs for defining backends: a new canvas-based API (introduced in Matplotlib 3.6), and an older function-based API. The new API is simpler to implement because many methods can be inherited from "parent backends". It is recommended if back-compatibility for Matplotlib < 3.6 is not a concern. However, the old API remains supported.

Fundamentally, a backend module needs to provide information to [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
, so that

1.  [`pyplot.figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
     can create a new [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
     instance and associate it with an instance of a backend-provided canvas class, itself hosted in an instance of a backend-provided manager class.
    
2.  [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
     can show all figures and start the GUI event loop (if any).
    

To do so, the backend module must define a `backend_module.FigureCanvas` subclass of [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
. In the canvas-based API, this is the only strict requirement for backend modules. The function-based API additionally requires many module-level functions to be defined.

Canvas-based API (Matplotlib >= 3.6)[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#canvas-based-api-matplotlib-3-6 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  **Creating a figure**: [`pyplot.figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
     calls `figure = Figure(); FigureCanvas.new_manager(figure, num)` (`new_manager` is a classmethod) to instantiate a canvas and a manager and set up the `figure.canvas` and `figure.canvas.manager` attributes. Figure unpickling uses the same approach, but replaces the newly instantiated `Figure()` by the unpickled figure.
    
    Interactive backends should customize the effect of `new_manager` by setting the `FigureCanvas.manager_class` attribute to the desired manager class, and additionally (if the canvas cannot be created before the manager, as in the case of the wx backends) by overriding the `FigureManager.create_with_canvas` classmethod. (Non-interactive backends can normally use a trivial `FigureManagerBase` and can therefore skip this step.)
    
    After a new figure is registered with [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
     (either via [`pyplot.figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
     or via unpickling), if in interactive mode, [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
     will call its canvas' `draw_idle()` method, which can be overridden as desired.
    
2.  **Showing figures**: [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
     calls `FigureCanvas.manager_class.pyplot_show()` (a classmethod), forwarding any arguments, to start the main event loop.
    
    By default, `pyplot_show()` checks whether there are any `managers` registered with [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
     (exiting early if not), calls `manager.show()` on all such managers, and then, if called with `block=True` (or with the default `block=None` and out of IPython's pylab mode and not in interactive mode), calls `FigureCanvas.manager_class.start_main_loop()` (a classmethod) to start the main event loop. Interactive backends should therefore override the `FigureCanvas.manager_class.start_main_loop` classmethod accordingly (or alternatively, they may also directly override `FigureCanvas.manager_class.pyplot_show` directly).
    

Function-based API[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#function-based-api "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  **Creating a figure**: [`pyplot.figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
     calls `new_figure_manager(num, *args, **kwargs)` (which also takes care of creating the new figure as `Figure(*args, **kwargs)`); unpickling calls `new_figure_manager_given_figure(num, figure)`.
    
    Furthermore, in interactive mode, the first draw of the newly registered figure can be customized by providing a module-level `draw_if_interactive()` function. (In the new canvas-based API, this function is not taken into account anymore.)
    
2.  **Showing figures**: [`pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
     calls a module-level `show()` function, which is typically generated via the `ShowBase` class and its `mainloop` method.
    

Registering a backend[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#registering-a-backend "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

For a new backend to be usable via `matplotlib.use()` or IPython `%matplotlib` magic command, it must be compatible with one of the three ways supported by the [`BackendRegistry`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry "matplotlib.backends.registry.BackendRegistry")
:

### Built-in[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#built-in "Link to this heading")

A backend built into Matplotlib must have its name and `FigureCanvas.required_interactive_framework` hard-coded in the [`BackendRegistry`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry "matplotlib.backends.registry.BackendRegistry")
. If the backend module is not `f"matplotlib.backends.backend_{backend_name.lower()}"` then there must also be an entry in the `BackendRegistry._name_to_module`.

### module:// syntax[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#module-syntax "Link to this heading")

Any backend in a separate module (not built into Matplotlib) can be used by specifying the path to the module in the form `module://some.backend.module`. An example is `module://mplcairo.qt` for [mplcairo](https://github.com/matplotlib/mplcairo)
. The backend's interactive framework will be taken from its `FigureCanvas.required_interactive_framework`.

### Entry point[#](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html#entry-point "Link to this heading")

An external backend module can self-register as a backend using an `entry point` in its `pyproject.toml` such as the one used by `matplotlib-inline`:

\[project.entry-points."matplotlib.backend"\]
inline \= "matplotlib\_inline.backend\_inline"

The backend's interactive framework will be taken from its `FigureCanvas.required_interactive_framework`. All entry points are loaded together but only when first needed, such as when a backend name is not recognised as a built-in backend, or when [`list_all()`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry.list_all "matplotlib.backends.registry.BackendRegistry.list_all")
 is first called.

On this page