[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#main-content)

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
    

matplotlib.figure.Figure.tight\_layout[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib-figure-figure-tight-layout "Link to this heading")

=============================================================================================================================================================================================

Figure.tight\_layout(_\*_, _pad\=1.08_, _h\_pad\=None_, _w\_pad\=None_, _rect\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L3633-L3671)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "Link to this definition")

Adjust the padding between and around subplots.

To exclude an artist on the Axes from the bounding box calculation that determines the subplot parameters (i.e. legend, or annotation), set `a.set_in_layout(False)` for that artist.

Parameters:

**pad**float, default: 1.08

Padding between the figure edge and the edges of subplots, as a fraction of the font size.

**h\_pad, w\_pad**float, default: _pad_

Padding (height/width) between edges of adjacent subplots, as a fraction of the font size.

**rect**tuple (left, bottom, right, top), default: (0, 0, 1, 1)

A rectangle in normalized figure coordinates into which the whole subplots area (including labels) will fit.

See also

[`Figure.set_layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine")

[`pyplot.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")

Examples using `matplotlib.figure.Figure.tight_layout`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#examples-using-matplotlib-figure-figure-tight-layout "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_thumb.png)

[Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)

Marker reference

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_demo2_thumb.png)

[Scatter Demo2](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html)

Scatter Demo2

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between_demo_thumb.png)

[Fill the area between two lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_demo.html)

Fill the area between two lines

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_quadmesh_demo_thumb.png)

[QuadMesh Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quadmesh_demo.html)

QuadMesh Demo

![](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_thumb.png)

[Triinterp Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html)

Triinterp Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_histtypes_thumb.png)

[Demo of the histogram function's different histtype settings](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html)

Demo of the histogram function's different histtype settings

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_multihist_thumb.png)

[The histogram (hist) function with multiple data sets](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html)

The histogram (hist) function with multiple data sets

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_thumb.png)

[Combine two subplots using subplots and GridSpec](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html)

Combine two subplots using subplots and GridSpec

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_axis_equal_demo_thumb.png)

[Equal axis aspect ratio](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html)

Equal axis aspect ratio

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_twin_axes_zorder_thumb.png)

[Twin Axes with delta\_zorder](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/twin_axes_zorder.html)

Twin Axes with delta\_zorder

![](https://matplotlib.org/stable/_images/sphx_glr_logit_demo_thumb.png)

[Logit scale](https://matplotlib.org/stable/gallery/scales/logit_demo.html)

Logit scale

![](https://matplotlib.org/stable/_images/sphx_glr_power_norm_thumb.png)

[Exploring normalizations](https://matplotlib.org/stable/gallery/scales/power_norm.html)

Exploring normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

![](https://matplotlib.org/stable/_images/sphx_glr_accented_text_thumb.png)

[Accented text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/accented_text.html)

Accented text

![](https://matplotlib.org/stable/_images/sphx_glr_mathtext_demo_thumb.png)

[Mathtext](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_demo.html)

Mathtext

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

![](https://matplotlib.org/stable/_images/sphx_glr_bar_demo2_thumb.png)

[Bar demo with units](https://matplotlib.org/stable/gallery/units/bar_demo2.html)

Bar demo with units

![](https://matplotlib.org/stable/_images/sphx_glr_radian_demo_thumb.png)

[Radian ticks](https://matplotlib.org/stable/gallery/units/radian_demo.html)

Radian ticks

![](https://matplotlib.org/stable/_images/sphx_glr_units_scatter_thumb.png)

[Unit handling](https://matplotlib.org/stable/gallery/units/units_scatter.html)

Unit handling

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormaps_thumb.png)

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

Choosing Colormaps in Matplotlib

On this page