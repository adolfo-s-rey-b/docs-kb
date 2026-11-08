[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#main-content)

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
    

matplotlib.pyplot.gca[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib-pyplot-gca "Link to this heading")

============================================================================================================================================

matplotlib.pyplot.gca()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2931-L2933)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "Link to this definition")

Get the current Axes.

If there is currently no Axes on this Figure, a new one is created using [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
. (To test whether there is currently an Axes on a Figure, check whether `figure.axes` is empty. To test whether there is currently a Figure on the pyplot figure stack, check whether [`pyplot.get_fignums()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_fignums.html#matplotlib.pyplot.get_fignums "matplotlib.pyplot.get_fignums")
 is empty.)

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "matplotlib.figure.Figure.gca")
.

Examples using `matplotlib.pyplot.gca`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#examples-using-matplotlib-pyplot-gca "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_thumb.png)

[Multicolored lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html)

Multicolored lines

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_multiple_figs_demo_thumb.png)

[Manage multiple figures in pyplot](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_figs_demo.html)

Manage multiple figures in pyplot

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_set_and_get_thumb.png)

[Set and get properties](https://matplotlib.org/stable/gallery/misc/set_and_get.html)

Set and get properties

![](https://matplotlib.org/stable/_images/sphx_glr_hinton_demo_thumb.png)

[Hinton diagrams](https://matplotlib.org/stable/gallery/specialty_plots/hinton_demo.html)

Hinton diagrams

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page