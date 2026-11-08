[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#sphx-glr-download-gallery-subplots-axes-and-figures-axes-box-aspect-py)
 to download the full example code.

Axes box aspect[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#axes-box-aspect "Link to this heading")

================================================================================================================================================

This demo shows how to set the aspect of an Axes box directly via [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
. The box aspect is the ratio between Axes height and Axes width in physical units, independent of the data limits. This is useful to e.g. produce a square plot, independent of the data it contains, or to have a usual plot with the same axes dimensions next to an image plot with fixed (data-)aspect.

The following lists a few use cases for [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
.

A square Axes, independent of data[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#a-square-axes-independent-of-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Produce a square Axes, no matter what the data limits are.

import matplotlib.pyplot as plt
import numpy as np

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(300, 400)
[ax.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
(1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_001_2_00x.png)

Shared square Axes[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#shared-square-axes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

Produce shared subplots that are squared in size.

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, sharey\=True)

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 5\], \[0, 10\])
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[100, 500\], \[10, 15\])

[ax.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
(1)
[ax2.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
(1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_002_2_00x.png)

Square twin Axes[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#square-twin-axes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Produce a square Axes, with a twin Axes. The twinned Axes takes over the box aspect of the parent.

[fig3](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.twinx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
()

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 10\])
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[12, 10\])

[ax.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
(1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_003_2_00x.png)

Normal plot next to image[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#normal-plot-next-to-image "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

When creating an image plot with fixed data aspect and the default `adjustable="box"` next to a normal plot, the Axes would be unequal in height. [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
 provides an easy solution to that by allowing to have the normal plot's Axes use the images dimensions as box aspect.

This example also shows that _constrained layout_ interplays nicely with a fixed box aspect.

[fig4](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, layout\="constrained")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)  \# Fixing random state for reproducibility
[im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(16, 27)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[23, 45\])
[ax2.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
([im.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]/[im.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_004_2_00x.png)

Square joint/marginal plot[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#square-joint-marginal-plot "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

It may be desirable to show marginal distributions next to a plot of joint data. The following creates a square plot with the box aspect of the marginal Axes being equal to the width- and height-ratios of the gridspec. This ensures that all Axes align perfectly, independent on the size of the figure.

[fig5](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, sharex\="col", sharey\="row",
                         gridspec\_kw\=dict(height\_ratios\=\[1, 3\],
                                          width\_ratios\=\[3, 1\]))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_visible(False)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_box\_aspect(1/3)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_box\_aspect(1)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_box\_aspect(3/1)

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)  \# Fixing random state for reproducibility
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(2, 400) \* \[\[.5\], \[180\]\]
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].scatter([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].hist([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].hist([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, orientation\="horizontal")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_005_2_00x.png)

Set data aspect with box aspect[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#set-data-aspect-with-box-aspect "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When setting the box aspect, one may still set the data aspect as well. Here we create an Axes with a box twice as long as it is tall and use an "equal" data aspect for its contents, i.e. the circle actually stays circular.

[fig6](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([plt.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((5, 3), 1))
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
("equal", adjustable\="datalim")
[ax.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
(0.5)
[ax.autoscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_006_2_00x.png)

Box aspect for many subplots[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html#box-aspect-for-many-subplots "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to pass the box aspect to an Axes at initialization. The following creates a 2 by 3 subplot grid with all square Axes.

[fig7](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3, subplot\_kw\=dict(box\_aspect\=1),
                         sharex\=True, sharey\=True, layout\="constrained")

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
):
    [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 % 3, \-(([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 3) \- 0.5)\*200, c\=\[[plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")\
\["hsv"\]([i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 6)\], s\=300)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axes box aspect](https://matplotlib.org/stable/_images/sphx_glr_axes_box_aspect_007_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
    

Tags: [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [styling: size](https://matplotlib.org/stable/_tags/styling-size.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 3.508 seconds)

[`Download Jupyter notebook: axes_box_aspect.ipynb`](https://matplotlib.org/stable/_downloads/0f6515ec907616925c0b1cb0bd925d01/axes_box_aspect.ipynb)

[`Download Python source code: axes_box_aspect.py`](https://matplotlib.org/stable/_downloads/a0e86663d543ed61329cd06205bcdd62/axes_box_aspect.py)

[`Download zipped: axes_box_aspect.zip`](https://matplotlib.org/stable/_downloads/25199d689a9593cdf1af811ae2fd0420/axes_box_aspect.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page