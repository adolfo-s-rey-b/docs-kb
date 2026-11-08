[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html#sphx-glr-download-gallery-shapes-and-collections-fancybox-demo-py)
 to download the full example code.

Drawing fancy boxes[#](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html#drawing-fancy-boxes "Link to this heading")

===================================================================================================================================================

The following examples show how to plot boxes ([`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
) with different visual properties.

import inspect

import matplotlib.pyplot as plt

import matplotlib.patches as mpatch
from matplotlib.patches import [FancyBboxPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
import matplotlib.transforms as mtransforms

Box styles[#](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html#box-styles "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

[`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 supports different [`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")
s. Note that [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
 allows to draw a box around the text by adding the `bbox` parameter. Therefore, you don't see explicit [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 and [`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")
 calls in the following example.

[styles](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= mpatch.BoxStyle.get\_styles()
[ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2
[nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= (len([styles](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
) + 1) // [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(3 \* [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 1 + [nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
))
       .add\_gridspec(1 + [nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
, wspace\=.5).subplots())
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :\]:
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.2, .5, "boxstyle",
            transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, size\="large", color\="tab:blue",
            horizontalalignment\="right", verticalalignment\="center")
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.4, .5, "default parameters",
            transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            horizontalalignment\="left", verticalalignment\="center")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, ([stylename](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [stylecls](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Roundtooth "matplotlib.patches.BoxStyle.Roundtooth")
) in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, :\].T.flat, [styles](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items()):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.2, .5, [stylename](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, bbox\=dict(boxstyle\=[stylename](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fc\="w", ec\="k"),
            transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, size\="large", color\="tab:blue",
            horizontalalignment\="right", verticalalignment\="center")
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(.4, .5, str([inspect.signature](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
([stylecls](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Roundtooth "matplotlib.patches.BoxStyle.Roundtooth")
))\[1:\-1\].replace(", ", "\\n"),
            transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            horizontalalignment\="left", verticalalignment\="center")

![fancybox demo](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_001_2_00x.png)

Parameters for modifying the box[#](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html#parameters-for-modifying-the-box "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")
s have additional parameters to configure their appearance. For example, "round" boxes can have `pad` and `rounding`.

Additionally, the [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 parameters `mutation_scale` and `mutation_aspect` scale the box appearance.

def add\_fancy\_patch\_around([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, \*\*kwargs):
    kwargs \= {
        'facecolor': (1, 0.8, 1, 0.5),
        'edgecolor': (1, 0.5, 1, 0.5),
        \*\*kwargs
    }
    [fancy](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 \= [FancyBboxPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
([bb.p0](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.p0 "matplotlib.transforms.Bbox.p0")
, [bb.width](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.width "matplotlib.transforms.BboxBase.width")
, [bb.height](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.height "matplotlib.transforms.BboxBase.height")
, \*\*kwargs)
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([fancy](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
)
    return [fancy](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")

def draw\_control\_points\_for\_patches([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    for patch in [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.patches:
        patch.axes.plot(\*patch.get\_path().vertices.T, ".",
                        c\=patch.get\_edgecolor())

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(8, 8))

\# Bbox object around which the fancy box will be drawn.
[bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 \= [mtransforms.Bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
(\[\[0.3, 0.4\], \[0.7, 0.6\]\])

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\]
\# a fancy box with round corners. pad=0.1
add\_fancy\_patch\_around([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="round,pad=0.1")
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 1), ylim\=(0, 1), aspect\=1,
       title\='boxstyle="round,pad=0.1"')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\]
\# bbox=round has two optional arguments: pad and rounding\_size.
\# They can be set during the initialization.
[fancy](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 \= add\_fancy\_patch\_around([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="round,pad=0.1")
\# The boxstyle and its argument can be later modified with set\_boxstyle().
\# Note that the old attributes are simply forgotten even if the boxstyle name
\# is same.
[fancy.set\_boxstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch.set_boxstyle "matplotlib.patches.FancyBboxPatch.set_boxstyle")
("round,pad=0.1,rounding\_size=0.2")
\# or: fancy.set\_boxstyle("round", pad=0.1, rounding\_size=0.2)
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 1), ylim\=(0, 1), aspect\=1,
       title\='boxstyle="round,pad=0.1,rounding\_size=0.2"')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\]
\# mutation\_scale determines the overall scale of the mutation, i.e. both pad
\# and rounding\_size is scaled according to this value.
add\_fancy\_patch\_around([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="round,pad=0.1", mutation\_scale\=2)
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 1), ylim\=(0, 1), aspect\=1,
       title\='boxstyle="round,pad=0.1"\\n mutation\_scale=2')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\]
\# mutation\_aspect scales the vertical influence of the parameters (technically,
\# it scales the height of the box down by mutation\_aspect, applies the box parameters
\# and scales the result back up). In effect, the vertical pad is scaled to
\# pad \* mutation\_aspect, e.g. mutation\_aspect=0.5 halves the vertical pad.
add\_fancy\_patch\_around([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="round,pad=0.1", mutation\_aspect\=0.5)
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 1), ylim\=(0, 1),
       title\='boxstyle="round,pad=0.1"\\nmutation\_aspect=0.5')

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    draw\_control\_points\_for\_patches([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
    \# Draw the original bbox (using boxstyle=square with pad=0).
    add\_fancy\_patch\_around([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="square,pad=0",
                           edgecolor\="black", facecolor\="none", zorder\=10)

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![boxstyle=](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_002_2_00x.png)

Creating visually constant padding on non-equal aspect Axes[#](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html#creating-visually-constant-padding-on-non-equal-aspect-axes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Since padding is in box coordinates, i.e. usually data coordinates, a given padding is rendered to different visual sizes if the Axes aspect is not 1. To get visually equal vertical and horizontal padding, set the mutation\_aspect to the inverse of the Axes aspect. This scales the vertical padding appropriately.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(6.5, 5))

\# original boxes
[bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 \= [mtransforms.Bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
(\[\[\-0.5, \-0.5\], \[0.5, 0.5\]\])
add\_fancy\_patch\_around([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="square,pad=0",
                       edgecolor\="black", facecolor\="none", zorder\=10)
add\_fancy\_patch\_around([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="square,pad=0",
                       edgecolor\="black", facecolor\="none", zorder\=10)
[ax1.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-1.5, 1.5), ylim\=(\-1.5, 1.5), aspect\=2)
[ax2.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-1.5, 1.5), ylim\=(\-1.5, 1.5), aspect\=2)

[fancy](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 \= add\_fancy\_patch\_around(
    [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="round,pad=0.5")
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("aspect=2\\nmutation\_aspect=1")

[fancy](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 \= add\_fancy\_patch\_around(
    [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bb](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, boxstyle\="round,pad=0.5", mutation\_aspect\=0.5)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("aspect=2\\nmutation\_aspect=0.5")

![aspect=2 mutation_aspect=1, aspect=2 mutation_aspect=0.5](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
    
*   [`matplotlib.patches.BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")
    
*   `matplotlib.patches.BoxStyle.get_styles`
    
*   [`matplotlib.transforms.Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    
*   [`matplotlib.figure.Figure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
    

**Total running time of the script:** (0 minutes 2.873 seconds)

[`Download Jupyter notebook: fancybox_demo.ipynb`](https://matplotlib.org/stable/_downloads/210021ff118a667d0bea86dcb158be37/fancybox_demo.ipynb)

[`Download Python source code: fancybox_demo.py`](https://matplotlib.org/stable/_downloads/bf03b3b7a1c4e04acbb2d88dcedc0f39/fancybox_demo.py)

[`Download zipped: fancybox_demo.zip`](https://matplotlib.org/stable/_downloads/c6246b2650c326bee2b88818b710c78d/fancybox_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page