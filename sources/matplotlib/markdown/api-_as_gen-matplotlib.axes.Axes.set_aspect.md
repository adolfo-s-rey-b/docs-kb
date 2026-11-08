[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#main-content)

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
    

matplotlib.axes.Axes.set\_aspect[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib-axes-axes-set-aspect "Link to this heading")

===========================================================================================================================================================================

Axes.set\_aspect(_aspect_, _adjustable\=None_, _anchor\=None_, _share\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1708-L1787)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "Link to this definition")

Set the aspect ratio of the Axes scaling, i.e. y/x-scale.

Parameters:

**aspect**{'auto', 'equal'} or float

Possible values:

*   'auto': fill the position rectangle with data.
    
*   'equal': same as `aspect=1`, i.e. same scaling for x and y.
    
*   _float_: The displayed size of 1 unit in y-data coordinates will be _aspect_ times the displayed size of 1 unit in x-data coordinates; e.g. for `aspect=2` a square in data coordinates will be rendered with a height of twice its width.
    

**adjustable**None or {'box', 'datalim'}, optional

If not `None`, this defines which parameter will be adjusted to meet the required aspect. See [`set_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable")
 for further details.

**anchor**None or str or (float, float), optional

If not `None`, this defines where the Axes will be drawn if there is extra space due to aspect constraints. The most common way to specify the anchor are abbreviations of cardinal directions:

| value | description |
| --- | --- |
| 'C' | centered |
| 'SW' | lower left corner |
| 'S' | middle of bottom edge |
| 'SE' | lower right corner |
| etc. |     |

See [`set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor")
 for further details.

**share**bool, default: False

If `True`, apply the settings to all shared Axes.

See also

[`matplotlib.axes.Axes.set_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable")

Set how the Axes adjusts to achieve the required aspect ratio.

[`matplotlib.axes.Axes.set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor")

Set the position in case of extra space.

[`matplotlib.axes.Axes.apply_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.apply_aspect.html#matplotlib.axes.Axes.apply_aspect "matplotlib.axes.Axes.apply_aspect")

Force the update required to meet the aspect ratio to happen immediately.

Notes

The aspect will require an update of the Axes position or limits (which one depends on _adjustable_). This update is applied lazily, the latest when the figure is drawn. Use [`apply_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.apply_aspect.html#matplotlib.axes.Axes.apply_aspect "matplotlib.axes.Axes.apply_aspect")
 to force an update.

Examples using `matplotlib.axes.Axes.set_aspect`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#examples-using-matplotlib-axes-axes-set-aspect "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_thumb.png)

[Scatter plot with histograms](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)

Scatter plot with histograms

![](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_thumb.png)

[Triplot Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html)

Triplot Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tripcolor_demo_thumb.png)

[Tripcolor Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tripcolor_demo.html)

Tripcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_demo_thumb.png)

[Tricontour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_demo.html)

Tricontour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_user_thumb.png)

[Tricontour Smooth User](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_user.html)

Tricontour Smooth User

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_delaunay_thumb.png)

[Tricontour Smooth Delaunay](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html)

Tricontour Smooth Delaunay

![](https://matplotlib.org/stable/_images/sphx_glr_trigradient_demo_thumb.png)

[Trigradient Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html)

Trigradient Demo

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_axes_margins_thumb.png)

[Controlling view limits using margins and sticky\_edges](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_margins.html)

Controlling view limits using margins and sticky\_edges

![](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_thumb.png)

[Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)

Axes box aspect

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_line_collection_thumb.png)

[Plot multiple lines using a LineCollection](https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html)

Plot multiple lines using a LineCollection

![](https://matplotlib.org/stable/_images/sphx_glr_polys3d_thumb.png)

[Generate 3D polygons](https://matplotlib.org/stable/gallery/mplot3d/polys3d.html)

Generate 3D polygons

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_2_thumb.png)

[3D surface (solid color)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html)

3D surface (solid color)

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_thumb.png)

[3D voxel plot of the NumPy logo](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html)

3D voxel plot of the NumPy logo

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_rgb_thumb.png)

[3D voxel / volumetric plot with RGB colors](https://matplotlib.org/stable/gallery/mplot3d/voxels_rgb.html)

3D voxel / volumetric plot with RGB colors

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_thumb.png)

[Inset locator demo 2](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)

Inset locator demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_locatable_axes_thumb.png)

[Align histogram to scatter plot using locatable Axes](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html)

Align histogram to scatter plot using locatable Axes

![](https://matplotlib.org/stable/_images/sphx_glr_simple_anchored_artists_thumb.png)

[Simple Anchored Artists](https://matplotlib.org/stable/gallery/axes_grid1/simple_anchored_artists.html)

Simple Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_double_pendulum_thumb.gif)

[The double pendulum problem](https://matplotlib.org/stable/gallery/animation/double_pendulum.html)

The double pendulum problem

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_axes_thumb.gif)

[Multiple Axes animation](https://matplotlib.org/stable/gallery/animation/multiple_axes.html)

Multiple Axes animation

![](https://matplotlib.org/stable/_images/sphx_glr_anchored_artists_thumb.png)

[Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)

Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_rasterization_demo_thumb.png)

[Rasterization for vector graphics](https://matplotlib.org/stable/gallery/misc/rasterization_demo.html)

Rasterization for vector graphics

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page