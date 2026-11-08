[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#main-content)

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
    

matplotlib.pyplot.clabel[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib-pyplot-clabel "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.clabel(_CS_, _levels\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3288-L3290)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "Link to this definition")

Label a contour plot.

Adds labels to line contours in given [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
.

Parameters:

**CS**[`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 instance

Line contours to label.

**levels**array-like, optional

A list of level values, that should be labeled. The list must be a subset of `CS.levels`. If not given, all levels are labeled.

**\*\*kwargs**

All other parameters are documented in [`clabel`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.clabel "matplotlib.contour.ContourLabeler.clabel")
.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
.

Examples using `matplotlib.pyplot.clabel`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#examples-using-matplotlib-pyplot-clabel "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_contour_demo_thumb.png)

[Contour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html)

Contour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_label_demo_thumb.png)

[Contour Label Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_label_demo.html)

Contour Label Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)

[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)

Contourf demo

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

On this page