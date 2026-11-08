[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout_pads.html#main-content)

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
    

matplotlib.figure.Figure.get\_constrained\_layout\_pads[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout_pads.html#matplotlib-figure-figure-get-constrained-layout-pads "Link to this heading")

============================================================================================================================================================================================================================================

Figure.get\_constrained\_layout\_pads(_relative\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2976-L3007)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout_pads.html#matplotlib.figure.Figure.get_constrained_layout_pads "Link to this definition")

\[_Deprecated_\] Get padding for `constrained_layout`.

Returns a list of `w_pad, h_pad` in inches and `wspace` and `hspace` as fractions of the subplot. All values are None if `constrained_layout` is not used.

See [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
.

Parameters:

**relative**bool

If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, then convert from inches to figure relative.

Notes

Deprecated since version 3.6: Use fig.get\_layout\_engine().get() instead.

On this page