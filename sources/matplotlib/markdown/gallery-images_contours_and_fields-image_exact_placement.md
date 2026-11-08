[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html#sphx-glr-download-gallery-images-contours-and-fields-image-exact-placement-py)
 to download the full example code.

Placing images, preserving relative sizes[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html#placing-images-preserving-relative-sizes "Link to this heading")

==========================================================================================================================================================================================================

By default Matplotlib resamples images created with [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 to fit inside the parent [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. This can mean that images that have very different original sizes can end up appearing similar in size.

This example shows how to keep the images the same relative size, or how to make the images keep exactly the same pixels as the original data.

Preserving relative sizes[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html#preserving-relative-sizes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default the two images are made a similar size, despite one being 1.5 times the width of the other:

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.patches as mpatches

\# make the data:
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 450
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
) / [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
) / [N](https://docs.python.org/3/library/functions.html#int "builtins.int")

[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[f0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
[k](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 2 \* ([f0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 / 2))
[A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:100, :300\]
[B](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:40, :200\]

\# default layout: both axes have the same size
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, facecolor\='aliceblue')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].imshow([B](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)

def annotate\_rect([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    \# add a rectangle that is the size of the B matrix
    rect \= [mpatches.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((0, 0), 200, 40, linewidth\=1,
                              edgecolor\='r', facecolor\='none')
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
(rect)
    return rect

annotate\_rect([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\])

![image exact placement](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_001_2_00x.png)

Note that both images have an aspect ratio of 1 (i.e. pixels are square), but pixels sizes differ because the images are scaled to the same width.

If the size of the images are amenable, we can preserve the relative sizes of two images by using either the _width\_ratio_ or _height\_ratio_ of the subplots. Which one you use depends on the shape of the image and the size of the figure. We can control the relative sizes using the _width\_ratios_ argument _if_ the images are wider than they are tall and shown side by side, as is the case here.

While we are making changes, let us also make the aspect ratio of the figure closer to the aspect ratio of the axes using _figsize_ so that the figure does not have so much white space. Note that you could alternatively trim extra blank space when saving a figure by passing `bbox_inches="tight"` to [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, width\_ratios\=\[300/200, 1\],
                        figsize\=(6.4, 2), facecolor\='aliceblue')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)
annotate\_rect([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\])

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].imshow([B](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)

![image exact placement](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_002_2_00x.png)

Given that the data subsample is in the upper left of the larger image, it might make sense if the top of the smaller Axes aligned with the top of the larger. This can be done manually by using [`set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor")
, and using "NW" (for northwest).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, width\_ratios\=\[300/200, 1\],
                        figsize\=(6.4, 2), facecolor\='aliceblue')

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)
annotate\_rect([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\])

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_anchor('NW')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].imshow([B](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_anchor('NW')

![image exact placement](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_003_2_00x.png)

Explicit placement[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_exact_placement.html#explicit-placement "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

The above approach with adjusting `figsize` and `width_ratios` does not generalize well, because it needs manual parameter tuning, and possibly even code changes to using `height_ratios` instead of `width_ratios` depending on the aspects and layout of the images.

We can alternative calculate positions explicitly and place Axes at absolute coordinates using [`add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
. This takes the position in the form `[left bottom width height]` and is in [figure coordinates](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)
. In the following, we determine figure size and Axes positions so that one image data point is rendered exactly to one figure pixel.

[dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100  \# 100 pixels is one inch

\# All variables from here are in pixels:
[buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.35 \* [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
  \# pixels

\# Get the position of A axes
[left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")
[bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")
[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [np.shape](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
([A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[posA](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[left](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
\# we know this is tallest, so we can already get the fig height (in pixels)
[fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")

\# place the B axes to the right of the A axes
[left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")

[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [np.shape](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
([B](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\# align the bottom so that the top lines up with the top of the A axes:
[bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- [buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \- [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
[posB](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[left](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]

\# now we can get the fig width (in pixels)
[fig\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [left](https://docs.python.org/3/library/functions.html#float "builtins.float")
 + [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [buffer](https://docs.python.org/3/library/functions.html#float "builtins.float")

\# figsize must be in inches:
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=([fig\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
), facecolor\='aliceblue')

\# the position posA must be normalized by the figure width and height:
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
(([posA](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\] / [fig\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [posA](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\] / [fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
                   [posA](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[2\] / [fig\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [posA](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[3\] / [fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([A](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)
annotate\_rect([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
(([posB](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\] / [fig\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [posB](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\] / [fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
                   [posB](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[2\] / [fig\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [posB](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[3\] / [fig\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([B](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-1, vmax\=1)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![image exact placement](https://matplotlib.org/stable/_images/sphx_glr_image_exact_placement_004_2_00x.png)

Inspection of the image will show that it is exactly 3\* 35 + 300 + 200 = 605 pixels wide, and 2 \* 35 + 100 = 170 pixels high (or twice that if the 2x version is used by the browser instead). The images should be rendered with exactly 1 pixel per data point (or four, if 2x).

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
    
*   [`matplotlib.figure.Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
    

Tags: [component: figure](https://matplotlib.org/stable/_tags/component-figure.html)
 [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [styling: position](https://matplotlib.org/stable/_tags/styling-position.html)
 [plot-type: image](https://matplotlib.org/stable/_tags/plot-type-image.html)

**Total running time of the script:** (0 minutes 1.458 seconds)

[`Download Jupyter notebook: image_exact_placement.ipynb`](https://matplotlib.org/stable/_downloads/852168cefca53447cd871ef7216a4f8e/image_exact_placement.ipynb)

[`Download Python source code: image_exact_placement.py`](https://matplotlib.org/stable/_downloads/1dd89079d5db7a72664d8a071938462a/image_exact_placement.py)

[`Download zipped: image_exact_placement.zip`](https://matplotlib.org/stable/_downloads/77e5877b8f4714aa09ae0fbfefaeca7e/image_exact_placement.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page