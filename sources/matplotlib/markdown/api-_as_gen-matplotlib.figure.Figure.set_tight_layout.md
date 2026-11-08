[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#main-content)

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
    

matplotlib.figure.Figure.set\_tight\_layout[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib-figure-figure-set-tight-layout "Link to this heading")

==========================================================================================================================================================================================================

Figure.set\_tight\_layout(_tight_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2891-L2909)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "Link to this definition")

\[_Deprecated_\] Set whether and how [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 is called when drawing.

Parameters:

**tight**bool or dict with keys "pad", "w\_pad", "h\_pad", "rect" or None

If a bool, sets whether to call [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 upon drawing. If `None`, use `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`) instead. If a dict, pass it as kwargs to [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
, overriding the default paddings.

Notes

Deprecated since version 3.6: Use set\_layout\_engine instead.

On this page