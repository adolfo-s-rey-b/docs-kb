[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html#sphx-glr-download-gallery-axes-grid1-inset-locator-demo-py)
 to download the full example code.

Inset locator demo[#](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo.html#inset-locator-demo "Link to this heading")

==========================================================================================================================================

The [`inset_locator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.html#module-mpl_toolkits.axes_grid1.inset_locator "mpl_toolkits.axes_grid1.inset_locator")
's [`inset_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
 allows easily placing insets in the corners of the Axes by specifying a width and height and optionally a location (loc) that accepts locations as codes, similar to [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
. By default, the inset is offset by some points from the axes, controlled via the _borderpad_ parameter.

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1.inset\_locator import [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=\[5.5, 2.8\])

\# Create inset of width 1.3 inches and height 0.9 inches
\# at the default upper right location.
axins \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\=1.3, height\=0.9)

\# Create inset of width 30% and height 40% of the parent Axes' bounding box
\# at the lower left corner.
axins2 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="30%", height\="40%", loc\="lower left")

\# Create inset of mixed specifications in the second subplot;
\# width is 30% of parent Axes' bounding box and
\# height is 1 inch at the upper left corner.
axins3 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="30%", height\=1., loc\="upper left")

\# Create an inset in the lower right corner with borderpad=1, i.e.
\# 10 points padding (as 10pt is the default fontsize) to the parent Axes.
axins4 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="20%", height\="20%", loc\="lower right", borderpad\=1)

\# Turn ticklabels of insets off
for [axi](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in \[axins, axins2, axins3, axins4\]:
    [axi.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labelleft\=False, labelbottom\=False)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![inset locator demo](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_001_2_00x.png)

The parameters _bbox\_to\_anchor_ and _bbox\_transform_ can be used for a more fine-grained control over the inset position and size or even to position the inset at completely arbitrary positions. The _bbox\_to\_anchor_ sets the bounding box in coordinates according to the _bbox\_transform_.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=\[5.5, 2.8\])
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(121)

\# We use the Axes transform as bbox\_transform. Therefore, the bounding box
\# needs to be specified in axes coordinates ((0, 0) is the lower left corner
\# of the Axes, (1, 1) is the upper right corner).
\# The bounding box (.2, .4, .6, .5) starts at (.2, .4) and ranges to (.8, .9)
\# in those coordinates.
\# Inside this bounding box an inset of half the bounding box' width and
\# three quarters of the bounding box' height is created. The lower left corner
\# of the inset is aligned to the lower left corner of the bounding box.
\# The inset is then offset by the default 0.5 in units of the font size.

axins \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="50%", height\="75%",
                   bbox\_to\_anchor\=(.2, .4, .6, .5),
                   bbox\_transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, loc\="lower left")

\# For visualization purposes we mark the bounding box by a rectangle
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([plt.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((.2, .4), .6, .5, ls\="--", ec\="c", fc\="none",
                           [transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedAffine2D "matplotlib.transforms.BlendedAffine2D")
\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
))

\# We set the axis limits to something other than the default, in order to not
\# distract from the fact that axes coordinates are used here.
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 10), ylim\=(0, 10))

\# Note how the two following insets are created at the same positions, one by
\# use of the default parent Axes' bbox and the other via a bbox in Axes
\# coordinates and the respective transform.
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(222)
axins2 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="30%", height\="50%")

[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(224)
axins3 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="100%", height\="100%",
                    bbox\_to\_anchor\=(.7, .5, .3, .5),
                    bbox\_transform\=[ax3.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

\# For visualization purposes we mark the bounding box by a rectangle
[ax2.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([plt.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((0, 0), 1, 1, ls\="--", lw\=2, ec\="c", fc\="none"))
[ax3.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([plt.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((.7, .5), .3, .5, ls\="--", lw\=2,
                            ec\="c", fc\="none"))

\# Turn ticklabels off
for [axi](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in \[axins2, axins3, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\]:
    [axi.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labelleft\=False, labelbottom\=False)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![inset locator demo](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_002_2_00x.png)

In the above the Axes transform together with 4-tuple bounding boxes has been used as it mostly is useful to specify an inset relative to the Axes it is an inset to. However, other use cases are equally possible. The following example examines some of those.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=\[5.5, 2.8\])
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(131)

\# Create an inset outside the Axes
axins \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="100%", height\="100%",
                   bbox\_to\_anchor\=(1.05, .6, .5, .4),
                   bbox\_transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, loc\="upper left", borderpad\=0)
[axins.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(left\=False, right\=True, labelleft\=False, labelright\=True)

\# Create an inset with a 2-tuple bounding box. Note that this creates a
\# bbox without extent. This hence only makes sense when specifying
\# width and height in absolute units (inches).
axins2 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\=0.5, height\=0.4,
                    bbox\_to\_anchor\=(0.33, 0.25),
                    bbox\_transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, loc\="lower left", borderpad\=0)

[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(133)
[ax2.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
("log")
[ax2.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(1e-6, 1e6), ylim\=(\-2, 6))

\# Create inset in data coordinates using ax.transData as transform
axins3 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="100%", height\="100%",
                    bbox\_to\_anchor\=(1e-2, 2, 1e3, 3),
                    bbox\_transform\=[ax2.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
, loc\="upper left", borderpad\=0)

\# Create an inset horizontally centered in figure coordinates and vertically
\# bound to line up with the Axes.
from matplotlib.transforms import [blended\_transform\_factory](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
  \# noqa

[transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedAffine2D "matplotlib.transforms.BlendedAffine2D")
 \= [blended\_transform\_factory](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
([fig.transFigure](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, [ax2.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)
axins4 \= [inset\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, width\="16%", height\="34%",
                    bbox\_to\_anchor\=(0, 0, 1, 1),
                    bbox\_transform\=[transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BlendedAffine2D "matplotlib.transforms.BlendedAffine2D")
, loc\="lower center", borderpad\=0)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![inset locator demo](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo_003_2_00x.png)

**Total running time of the script:** (0 minutes 1.526 seconds)

[`Download Jupyter notebook: inset_locator_demo.ipynb`](https://matplotlib.org/stable/_downloads/c62e99ea33f0dc4137dc1a890be60664/inset_locator_demo.ipynb)

[`Download Python source code: inset_locator_demo.py`](https://matplotlib.org/stable/_downloads/f8248729044d7fef8f20a43731251e38/inset_locator_demo.py)

[`Download zipped: inset_locator_demo.zip`](https://matplotlib.org/stable/_downloads/85a98be95e7eb886bc0fca3662906c35/inset_locator_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)