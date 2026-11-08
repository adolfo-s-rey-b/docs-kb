[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/layer_images.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/layer_images.html#sphx-glr-download-gallery-images-contours-and-fields-layer-images-py)
 to download the full example code.

Layer images with alpha blending[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/layer_images.html#layer-images-with-alpha-blending "Link to this heading")

================================================================================================================================================================================

Layer images above one another using alpha blending

import matplotlib.pyplot as plt
import numpy as np

def func3([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    return (1 \- [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 2 + [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*5 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*3) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2))

\# make these smaller to increase the resolution
[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.05, 0.05

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3.0, 3.0, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3.0, 3.0, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# when layering multiple images, the images need to have the same
\# extent.  This does not mean they need to have the same shape, but
\# they both need to render to the same coordinate system determined by
\# xmin, xmax, ymin, ymax.  Note if you use different interpolations
\# for the images their apparent extent could be different due to
\# interpolation edge effects

[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(frameon\=False)

[Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= np.add.outer(range(8), range(8)) % 2  \# chessboard
[im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\="gray", interpolation\='nearest',
                 [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= func3([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[im2](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\="viridis", alpha\=.9, interpolation\='bilinear',
                 [extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[extent](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![layer images](https://matplotlib.org/stable/_images/sphx_glr_layer_images_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    

[`Download Jupyter notebook: layer_images.ipynb`](https://matplotlib.org/stable/_downloads/5b7da5d89a95404a194791fbd1c97d0d/layer_images.ipynb)

[`Download Python source code: layer_images.py`](https://matplotlib.org/stable/_downloads/36a5c3960fdb309b098795e7222235d5/layer_images.py)

[`Download zipped: layer_images.zip`](https://matplotlib.org/stable/_downloads/b42b0ae4400fbf527a4a818a48b16354/layer_images.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)