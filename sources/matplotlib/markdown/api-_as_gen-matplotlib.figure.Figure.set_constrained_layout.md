[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout.html#main-content)

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
    

matplotlib.figure.Figure.set\_constrained\_layout[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout.html#matplotlib-figure-figure-set-constrained-layout "Link to this heading")

============================================================================================================================================================================================================================

Figure.set\_constrained\_layout(_constrained_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2919-L2940)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout.html#matplotlib.figure.Figure.set_constrained_layout "Link to this definition")

\[_Deprecated_\] Set whether `constrained_layout` is used upon drawing.

If None, `[rcParams["figure.constrained_layout.use"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.use#rcparam-figure-constrained-layout-use) ` (default: `False`) value will be used.

When providing a dict containing the keys `w_pad`, `h_pad` the default `constrained_layout` paddings will be overridden. These pads are in inches and default to 3.0/72.0. `w_pad` is the width padding and `h_pad` is the height padding.

Parameters:

**constrained**bool or dict or None

Notes

Deprecated since version 3.6: Use set\_layout\_engine('constrained') instead.

On this page