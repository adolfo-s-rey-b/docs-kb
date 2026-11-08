[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html#sphx-glr-download-gallery-lines-bars-and-markers-gradient-bar-py)
 to download the full example code.

Bar chart with gradients[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/gradient_bar.html#bar-chart-with-gradients "Link to this heading")

============================================================================================================================================================

Matplotlib does not natively support gradients. However, we can emulate a gradient-filled rectangle by an [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 of the right size and coloring.

In particular, we use a colormap to generate the actual colors. It is then sufficient to define the underlying values on the corners of the image and let bicubic interpolation fill out the area. We define the gradient direction by a unit vector _v_. The values at the corners are then obtained by the lengths of the projections of the corner vectors on _v_.

A similar approach can be used to create a gradient background for an Axes. In that case, it is helpful to use Axes coordinates (`extent=(0, 1, 0, 1), transform=ax.transAxes`) to be independent of the data coordinates.

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

def gradient\_image([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, direction\=0.3, cmap\_range\=(0, 1), \*\*kwargs):
    """
    Draw a gradient image based on a colormap.

    Parameters
    ----------
    ax : Axes
        The Axes to draw on.
    direction : float
        The direction of the gradient. This is a number in
        range 0 (=vertical) to 1 (=horizontal).
    cmap\_range : float, float
        The fraction (cmin, cmax) of the colormap that should be
        used for the gradient, where the complete colormap is (0, 1).
    \*\*kwargs
        Other parameters are passed on to \`.Axes.imshow()\`.
        In particular, \*cmap\*, \*extent\*, and \*transform\* may be useful.
    """
    phi \= direction \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2
    v \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(phi), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(phi)\])
    X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[v @ \[1, 0\], v @ \[1, 1\]\],\
                  \[v @ \[0, 0\], v @ \[0, 1\]\]\])
    a, b \= cmap\_range
    X \= a + (b \- a) / X.max() \* X
    im \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(X, interpolation\='bicubic', clim\=(0, 1),
                   aspect\='auto', \*\*kwargs)
    return im

def gradient\_bar([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, width\=0.5, bottom\=0):
    for left, top in zip([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
        right \= left + width
        gradient\_image([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, extent\=(left, right, bottom, top),
                       cmap\="Blues\_r", cmap\_range\=(0, 0.8))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 10), ylim\=(0, 1))

\# background image
gradient\_image([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, direction\=1, extent\=(0, 1, 0, 1), transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
               cmap\="RdYlGn", cmap\_range\=(0.2, 0.8), alpha\=0.5)

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 0.15
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
gradient\_bar([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, width\=0.7)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![gradient bar](https://matplotlib.org/stable/_images/sphx_glr_gradient_bar_001_2_00x.png)

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [plot-type: imshow](https://matplotlib.org/stable/_tags/plot-type-imshow.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: gradient_bar.ipynb`](https://matplotlib.org/stable/_downloads/87449719f97c0e3326a57c1a90dc3325/gradient_bar.ipynb)

[`Download Python source code: gradient_bar.py`](https://matplotlib.org/stable/_downloads/e83fa918d4012d4ca7e2bd48e7ab0935/gradient_bar.py)

[`Download zipped: gradient_bar.zip`](https://matplotlib.org/stable/_downloads/241001f1b7bbf3d091c50a4701ffc1f5/gradient_bar.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)