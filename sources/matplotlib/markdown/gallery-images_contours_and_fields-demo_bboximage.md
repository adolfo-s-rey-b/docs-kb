[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/demo_bboximage.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/demo_bboximage.html#sphx-glr-download-gallery-images-contours-and-fields-demo-bboximage-py)
 to download the full example code.

BboxImage Demo[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/demo_bboximage.html#bboximage-demo "Link to this heading")

==============================================================================================================================================

A [`BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
 can be used to position an image according to a bounding box. This demo shows how to show an image inside a [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
's bounding box as well as how to manually create a bounding box for the image.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.image import [BboxImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
from matplotlib.transforms import Bbox, [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2)

\# ----------------------------
\# Create a BboxImage with Text
\# ----------------------------
[txt](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [ax1.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, "test", size\=30, ha\="center", color\="w")
[ax1.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(
    [BboxImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
([txt.get\_window\_extent](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_window_extent "matplotlib.text.Text.get_window_extent")
, data\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(256).reshape((1, \-1))))

\# ------------------------------------
\# Create a BboxImage for each colormap
\# ------------------------------------
\# List of all colormaps; skip reversed colormaps.
[cmap\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= sorted(m for m in [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
 if not m.endswith("\_r"))

[ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2
[nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([cmap\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) // [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1

[xpad\_fraction](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.3
[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1 / ([ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [xpad\_fraction](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* ([ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 1))

[ypad\_fraction](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.3
[dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1 / ([nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [ypad\_fraction](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* ([nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 1))

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [cmap\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([cmap\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ix](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [iy](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= divmod([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [bbox0](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 \= [Bbox.from\_bounds](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_bounds "matplotlib.transforms.Bbox.from_bounds")
([ix](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*(1+[xpad\_fraction](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
                             1 \- [iy](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*(1+[ypad\_fraction](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \- [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
                             [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    [bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
 \= [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
([bbox0](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
, [ax2.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)
    [ax2.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(
        [BboxImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
([bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
, cmap\=[cmap\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, data\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(256).reshape((1, \-1))))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo bboximage](https://matplotlib.org/stable/_images/sphx_glr_demo_bboximage_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.image.BboxImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.BboxImage "matplotlib.image.BboxImage")
    
*   [`matplotlib.transforms.Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    
*   [`matplotlib.transforms.TransformedBbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
    
*   [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
    

[`Download Jupyter notebook: demo_bboximage.ipynb`](https://matplotlib.org/stable/_downloads/296762be8feb600deae3a83309b7ec7d/demo_bboximage.ipynb)

[`Download Python source code: demo_bboximage.py`](https://matplotlib.org/stable/_downloads/ee266dc4f781adee6f25e7723fd7089c/demo_bboximage.py)

[`Download zipped: demo_bboximage.zip`](https://matplotlib.org/stable/_downloads/7c44d600b5aa551e1b751900bedc8550/demo_bboximage.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)