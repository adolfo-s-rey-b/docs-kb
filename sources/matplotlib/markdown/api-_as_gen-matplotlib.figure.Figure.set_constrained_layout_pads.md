[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#main-content)

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
    

matplotlib.figure.Figure.set\_constrained\_layout\_pads[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib-figure-figure-set-constrained-layout-pads "Link to this heading")

============================================================================================================================================================================================================================================

Figure.set\_constrained\_layout\_pads(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2942-L2974)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib.figure.Figure.set_constrained_layout_pads "Link to this definition")

\[_Deprecated_\] Set padding for `constrained_layout`.

Tip: The parameters can be passed from a dictionary by using `fig.set_constrained_layout(**pad_dict)`.

See [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
.

Parameters:

**w\_pad**float, default: `[rcParams["figure.constrained_layout.w_pad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.w_pad#rcparam-figure-constrained-layout-w-pad) ` (default: `0.04167`)

Width padding in inches. This is the pad around Axes and is meant to make sure there is enough room for fonts to look good. Defaults to 3 pts = 0.04167 inches

**h\_pad**float, default: `[rcParams["figure.constrained_layout.h_pad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.h_pad#rcparam-figure-constrained-layout-h-pad) ` (default: `0.04167`)

Height padding in inches. Defaults to 3 pts.

**wspace**float, default: `[rcParams["figure.constrained_layout.wspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.wspace#rcparam-figure-constrained-layout-wspace) ` (default: `0.02`)

Width padding between subplots, expressed as a fraction of the subplot width. The total padding ends up being w\_pad + wspace.

**hspace**float, default: `[rcParams["figure.constrained_layout.hspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.hspace#rcparam-figure-constrained-layout-hspace) ` (default: `0.02`)

Height padding between subplots, expressed as a fraction of the subplot width. The total padding ends up being h\_pad + hspace.

Notes

Deprecated since version 3.6: Use figure.get\_layout\_engine().set() instead.

On this page