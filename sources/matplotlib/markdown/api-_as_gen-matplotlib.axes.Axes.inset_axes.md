[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#main-content)

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
    

matplotlib.axes.Axes.inset\_axes[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib-axes-axes-inset-axes "Link to this heading")

===========================================================================================================================================================================

Axes.inset\_axes(_bounds_, _\*_, _transform\=None_, _zorder\=5_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L359-L429)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "Link to this definition")

Add a child inset Axes to this existing Axes.

Parameters:

**bounds**\[x0, y0, width, height\]

Lower-left corner of inset Axes, and its width and height.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Defaults to `ax.transAxes`, i.e. the units of _rect_ are in Axes-relative coordinates.

**projection**{None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional

The projection type of the inset [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. _str_ is the name of a custom projection, see [`projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
. The default None results in a 'rectilinear' projection.

**polar**bool, default: False

If True, equivalent to projection='polar'.

**axes\_class**subclass type of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclass that is instantiated. This parameter is incompatible with _projection_ and _polar_. See [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)
 for examples.

**zorder**number

Defaults to 5 (same as [`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
). Adjust higher or lower to change whether it is above or below data plotted on the parent Axes.

**\*\*kwargs**

Other keyword arguments are passed on to the inset Axes class.

Returns:

ax

The created [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance.

Examples

This example makes two inset Axes, the first is in Axes-relative coordinates, and the second in data-coordinates:

fig, ax \= plt.subplots()
ax.plot(range(10))
axin1 \= ax.inset\_axes(\[0.8, 0.1, 0.15, 0.15\])
axin2 \= ax.inset\_axes(
        \[5, 7, 2.3, 2.3\], transform\=ax.transData)

Examples using `matplotlib.axes.Axes.inset_axes`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#examples-using-matplotlib-axes-axes-inset-axes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_thumb.png)

[Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)

Scatter plot with histograms

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_zoom_inset_axes_thumb.png)

[Zoom region inset Axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html)

Zoom region inset Axes

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_check_buttons_thumb.png)

[Check buttons](https://matplotlib.org/stable/gallery/widgets/check_buttons.html)

Check buttons

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_placement_thumb.png)

[Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)

Placing colorbars

On this page