[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html#sphx-glr-download-gallery-mplot3d-imshow3d-py)
 to download the full example code.

2D images in 3D[#](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html#d-images-in-3d "Link to this heading")

======================================================================================================================

This example demonstrates how to plot 2D color coded images (similar to [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
) as a plane in 3D.

Matplotlib does not have a native function for this. Below we build one by relying on [`Axes3D.plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")
. For simplicity, there are some differences to [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
: This function does not set the aspect of the Axes, hence pixels are not necessarily square. Also, pixel edges are on integer values rather than pixel centers. Furthermore, many optional parameters of [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 are not implemented.

Multiple calls of `imshow3d` use independent norms and thus different color scales by default. If you want to have a single common color scale, you need to construct a suitable norm beforehand and pass it to all `imshow3d` calls.

A fundamental limitation of the 3D plotting engine is that intersecting objects cannot be drawn correctly. One object will always be drawn after the other. Therefore, multiple image planes can well be used in the background as shown in this example. But this approach is not suitable if the planes intersect.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

def imshow3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, array, value\_direction\='z', pos\=0, norm\=None, cmap\=None):
    """
    Display a 2D array as a  color-coded 2D image embedded in 3d.

    The image will be in a plane perpendicular to the coordinate axis \*value\_direction\*.

    Parameters
    ----------
    ax : Axes3D
        The 3D Axes to plot into.
    array : 2D numpy array
        The image values.
    value\_direction : {'x', 'y', 'z'}
        The axis normal to the image plane.
    pos : float
        The numeric value on the \*value\_direction\* axis at which the image plane is
        located.
    norm : \`~matplotlib.colors.Normalize\`, default: Normalize
        The normalization method used to scale scalar data. See \`imshow()\`.
    cmap : str or \`~matplotlib.colors.Colormap\`, default: :rc:\`image.cmap\`
        The Colormap instance or registered colormap name used to map scalar data
        to colors.
    """
    if norm is None:
        norm \= [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
()
    colors \= [plt.get\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
(cmap)(norm(array))

    if value\_direction \== 'x':
        [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= array.shape
        zi, yi \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:[nz](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1, 0:[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1\]
        xi \= [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(yi, pos)
    elif value\_direction \== 'y':
        [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= array.shape
        xi, zi \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1, 0:[nz](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1\]
        yi \= [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(zi, pos)
    elif value\_direction \== 'z':
        [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= array.shape
        yi, xi \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1, 0:[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1\]
        zi \= [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(xi, pos)
    else:
        raise ValueError(f"Invalid value\_direction: {value\_direction!r}")
    [ax.plot\_surface](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.Axes3D.plot_surface")
(xi, yi, zi, rstride\=1, cstride\=1, facecolors\=colors, shade\=False)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='3d')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlabel\="x", ylabel\="y", zlabel\="z")

[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8, 10, 5
[data\_xy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
).reshape([ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 15 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(([ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
))
[data\_yz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
).reshape([nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 10 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(([nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
))
[data\_zx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
).reshape([nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 8 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(([nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

imshow3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, [data\_xy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
imshow3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, [data\_yz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, value\_direction\='x', cmap\='magma')
imshow3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, [data\_zx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, value\_direction\='y', pos\=[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, cmap\='plasma')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![imshow3d](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [styling: colormap](https://matplotlib.org/stable/_tags/styling-colormap.html)
 [level: advanced](https://matplotlib.org/stable/_tags/level-advanced.html)

[`Download Jupyter notebook: imshow3d.ipynb`](https://matplotlib.org/stable/_downloads/e367e4c881c30af8cfc97e5cbca60d6c/imshow3d.ipynb)

[`Download Python source code: imshow3d.py`](https://matplotlib.org/stable/_downloads/85c98843408756006b0ab8798a3b9590/imshow3d.py)

[`Download zipped: imshow3d.zip`](https://matplotlib.org/stable/_downloads/c92fd1bbf1dad4d756015a2c8f4c6d32/imshow3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)