[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/affine_image.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/affine_image.html#sphx-glr-download-gallery-images-contours-and-fields-affine-image-py)
 to download the full example code.

Affine transform of an image[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/affine_image.html#affine-transform-of-an-image "Link to this heading")

========================================================================================================================================================================

Prepending an affine transformation ([`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
) to the [data transform](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#data-coords)
 of an image allows to manipulate the image's shape and orientation. This is an example of the concept of [transform chaining](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transformation-pipeline)
.

The image of the output should have its boundary match the dashed yellow rectangle.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.transforms as mtransforms

def get\_image():
    delta \= 0.25
    x \= y \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3.0, 3.0, delta)
    X, Y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(x, y)
    Z1 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-X\*\*2 \- Y\*\*2)
    Z2 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-(X \- 1)\*\*2 \- (Y \- 1)\*\*2)
    [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (Z1 \- Z2)
    return [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

def do\_plot(ax, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, transform):
    im \= ax.imshow([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\='none',
                   origin\='lower',
                   extent\=\[\-2, 4, \-3, 2\], clip\_on\=True)

    trans\_data \= transform + ax.transData
    im.set\_transform(trans\_data)

    \# display intended extent of the image
    x1, x2, y1, y2 \= im.get\_extent()
    ax.plot(\[x1, x2, x2, x1, x1\], \[y1, y1, y2, y2, y1\], "y--",
            transform\=trans\_data)
    ax.set\_xlim(\-5, 5)
    ax.set\_ylim(\-4, 4)

\# prepare image and figure
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= get\_image()

\# image rotation
do\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [mtransforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg(30))

\# image skew
do\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [mtransforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().skew\_deg(30, 15))

\# scale and reflection
do\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [mtransforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(\-1, .5))

\# everything and a translation
do\_plot([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [mtransforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().
        rotate\_deg(30).skew\_deg(30, 15).scale(\-1, .5).translate(.5, \-1))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![affine image](https://matplotlib.org/stable/_images/sphx_glr_affine_image_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.transforms.Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
    

[`Download Jupyter notebook: affine_image.ipynb`](https://matplotlib.org/stable/_downloads/cf1efe942fecc62438dcd76a6bfdb169/affine_image.ipynb)

[`Download Python source code: affine_image.py`](https://matplotlib.org/stable/_downloads/a0ba87a82fe3b31fd9b06f25a2c11522/affine_image.py)

[`Download zipped: affine_image.zip`](https://matplotlib.org/stable/_downloads/fddac3f367a343b601b586a982fe4a9b/affine_image.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)