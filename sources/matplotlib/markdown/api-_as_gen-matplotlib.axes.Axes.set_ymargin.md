[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#main-content)

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
    

matplotlib.axes.Axes.set\_ymargin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib-axes-axes-set-ymargin "Link to this heading")

==============================================================================================================================================================================

Axes.set\_ymargin(_m_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L2903-L2929)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "Link to this definition")

Set padding of Y data limits prior to autoscaling.

_m_ times the data interval will be added to each end of that interval before it is used in autoscaling. If _m_ is negative, this will clip the data range instead of expanding it.

For example, if your data is in the range \[0, 2\], a margin of 0.1 will result in a range \[-0.2, 2.2\]; a margin of -0.1 will result in a range of \[0.2, 1.8\].

Parameters:

**m**float greater than -0.5

See also

[Margins](https://matplotlib.org/stable/users/explain/axes/autoscale.html#autoscale-margins)

[`matplotlib.axes.Axes.margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")

[`matplotlib.axes.Axes.get_ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymargin.html#matplotlib.axes.Axes.get_ymargin "matplotlib.axes.Axes.get_ymargin")

On this page