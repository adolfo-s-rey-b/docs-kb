[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#main-content)

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
    

matplotlib.figure.Figure.set\_layout\_engine[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib-figure-figure-set-layout-engine "Link to this heading")

=============================================================================================================================================================================================================

Figure.set\_layout\_engine(_layout\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2688-L2753)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "Link to this definition")

Set the layout engine for this figure.

Parameters:

**layout**{'constrained', 'compressed', 'tight', 'none', [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
, None}

*   'constrained' will use [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
    
*   'compressed' will also use [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
    , but with a correction that attempts to make a good layout for fixed-aspect ratio Axes.
    
*   'tight' uses [`TightLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine "matplotlib.layout_engine.TightLayoutEngine")
    
*   'none' removes layout engine.
    

If a [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
 instance, that instance will be used.

If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the behavior is controlled by `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`) (which if [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 behaves as if 'tight' was passed) and `[rcParams["figure.constrained_layout.use"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.use#rcparam-figure-constrained-layout-use) ` (default: `False`) (which if [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 behaves as if 'constrained' was passed). If both are [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`) takes priority.

Users and libraries can define their own layout engines and pass the instance directly as well.

**\*\*kwargs**

The keyword arguments are passed to the layout engine to set things like padding and margin sizes. Only used if _layout_ is a string.

Examples using `matplotlib.figure.Figure.set_layout_engine`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#examples-using-matplotlib-figure-figure-set-layout-engine "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

On this page