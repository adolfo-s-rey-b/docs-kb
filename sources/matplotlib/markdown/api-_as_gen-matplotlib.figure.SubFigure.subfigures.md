[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subfigures.html#main-content)

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
    

matplotlib.figure.SubFigure.subfigures[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subfigures.html#matplotlib-figure-subfigure-subfigures "Link to this heading")

===============================================================================================================================================================================================

SubFigure.subfigures(_nrows\=1_, _ncols\=1_, _squeeze\=True_, _wspace\=None_, _hspace\=None_, _width\_ratios\=None_, _height\_ratios\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1611-L1678)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subfigures.html#matplotlib.figure.SubFigure.subfigures "Link to this definition")

Add a set of subfigures to this figure or subfigure.

A subfigure has the same artist methods as a figure, and is logically the same as a figure, but cannot print itself. See [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)
.

Changed in version 3.10: subfigures are now added in row-major order.

Parameters:

**nrows, ncols**int, default: 1

Number of rows/columns of the subfigure grid.

**squeeze**bool, default: True

If True, extra dimensions are squeezed out from the returned array of subfigures.

**wspace, hspace**float, default: None

The amount of width/height reserved for space between subfigures, expressed as a fraction of the average subfigure width/height. If not given, the values will be inferred from rcParams if using constrained layout (see [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
), or zero if not using a layout engine.

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height.

On this page