[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_inset_locator.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_inset_locator.html#sphx-glr-download-gallery-axes-grid1-demo-colorbar-with-inset-locator-py)
 to download the full example code.

Control the position and size of a colorbar with inset\_locator.inset\_axes[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_inset_locator.html#control-the-position-and-size-of-a-colorbar-with-inset-locator-inset-axes "Link to this heading")

========================================================================================================================================================================================================================================================================

This example shows how to control the position, height, and width of colorbars using [`inset_locator.inset_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
.

[`inset_locator.inset_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
 placement is controlled as for legends: either by providing a _loc_ option ("upper right", "best", ...), or by providing a locator with respect to the parent bbox. Parameters such as _bbox\_to\_anchor_ and _borderpad_ likewise work in the same way, and are also demonstrated here.

Users should consider using [`Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 instead (see [Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html#colorbar-placement)
).

![demo colorbar with inset locator](https://matplotlib.org/stable/_images/sphx_glr_demo_colorbar_with_inset_locator_001_2_00x.png)

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1 import inset\_locator

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=\[6, 3\])

[im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[1, 2\], \[2, 3\]\])
axins1 \= [inset\_locator.inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
(
    [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    width\="50%",  \# width: 50% of parent\_bbox width
    height\="5%",  \# height: 5%
    loc\="upper right",
)
[axins1.xaxis.set\_ticks\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
("bottom")
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, cax\=axins1, orientation\="horizontal", ticks\=\[1, 2, 3\])

[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[1, 2\], \[2, 3\]\])
axins \= [inset\_locator.inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
(
    [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    width\="5%",  \# width: 5% of parent\_bbox width
    height\="50%",  \# height: 50%
    loc\="lower left",
    bbox\_to\_anchor\=(1.05, 0., 1, 1),
    bbox\_transform\=[ax2.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
    borderpad\=0,
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, cax\=axins, ticks\=\[1, 2, 3\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_colorbar_with_inset_locator.ipynb`](https://matplotlib.org/stable/_downloads/9084981113f3192721fe8f707418ceae/demo_colorbar_with_inset_locator.ipynb)

[`Download Python source code: demo_colorbar_with_inset_locator.py`](https://matplotlib.org/stable/_downloads/fef8ebea91f3e2d936a0356c1b573cd8/demo_colorbar_with_inset_locator.py)

[`Download zipped: demo_colorbar_with_inset_locator.zip`](https://matplotlib.org/stable/_downloads/29f64de712d58edc87c63edf1732d639/demo_colorbar_with_inset_locator.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)