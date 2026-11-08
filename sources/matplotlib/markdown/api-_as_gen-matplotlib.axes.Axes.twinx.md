[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#main-content)

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
    

matplotlib.axes.Axes.twinx[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib-axes-axes-twinx "Link to this heading")

===========================================================================================================================================================

Axes.twinx(_axes\_class\=None_, _\*_, _delta\_zorder\=0.0_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L4856-L4908)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "Link to this definition")

Create a twin Axes sharing the xaxis.

Create a new Axes with an invisible x-axis and an independent y-axis positioned opposite to the original one (i.e. at right). The x-axis autoscale setting will be inherited from the original Axes. To ensure that the tick marks of both y-axes align, see [`LinearLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
.

Parameters:

**axes\_class**subclass type of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclass that is instantiated. This parameter is incompatible with _projection_ and _polar_. See [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)
 for examples.

By default, [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 is used.

Added in version 3.11.

**delta\_zorder**float, default: 0

A zorder offset for the twin Axes, relative to the original Axes. The twin's zorder is set to `self.get_zorder() + delta_zorder`. By default (_delta\_zorder_ is 0), the twin has the same zorder as the original Axes.

**kwargs**dict

The keyword arguments passed to [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 or [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
.

Added in version 3.11.

Returns:

Axes

The newly created Axes instance

Notes

For those who are 'picking' artists while using twinx, pick events are only called for the artists in the top-most Axes.

Examples using `matplotlib.axes.Axes.twinx`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#examples-using-matplotlib-axes-axes-twinx "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_yaxis_with_spines_thumb.png)

[Multiple y-axis with Spines](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_yaxis_with_spines.html)

Multiple y-axis with Spines

![](https://matplotlib.org/stable/_images/sphx_glr_twin_axes_zorder_thumb.png)

[Twin Axes with delta\_zorder](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/twin_axes_zorder.html)

Twin Axes with delta\_zorder

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple_thumb.png)

[Parasite Simple](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple.html)

Parasite Simple

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_thumb.png)

[Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)

Parasite axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_pan_zoom_overlap_thumb.png)

[Pan/zoom events of overlapping axes](https://matplotlib.org/stable/gallery/showcase/pan_zoom_overlap.html)

Pan/zoom events of overlapping axes

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

On this page