[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/barb_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/barb_demo.html#sphx-glr-download-gallery-images-contours-and-fields-barb-demo-py)
 to download the full example code.

Wind barbs[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/barb_demo.html#wind-barbs "Link to this heading")

=================================================================================================================================

Demonstration of wind barb plots.

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, 5)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 12 \* [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 12 \* [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[(\-1.5, .5, \-6, \-6),\
        (1, \-1, \-46, 46),\
        (\-3, \-1, 11, \-11),\
        (1, 1.5, 80, 80),\
        (0.5, 0.25, 25, 15),\
        (\-1.5, \-0.5, \-5, 40)\]

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, dtype\=\[('x', [np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")\
), ('y', [np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")\
),\
                             ('u', [np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")\
), ('v', [np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")\
)\])

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)
\# Default parameters, uniform grid
[axs1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].barbs([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Arbitrary set of vectors, make them longer and change the pivot point
\# (point around which they're rotated) to be the middle
[axs1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].barbs(
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['x'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['y'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['u'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['v'\], length\=8, pivot\='middle')

\# Showing colormapping with uniform grid.  Fill the circle for an empty barb,
\# don't round the values, and change some of the size parameters
[axs1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].barbs(
    [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\* 2 + [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\* 2), fill\_empty\=True, rounding\=False,
    sizes\=dict(emptybarb\=0.25, spacing\=0.2, height\=0.3))

\# Change colors as well as the increments for parts of the barbs
[axs1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].barbs([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['x'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['y'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['u'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['v'\], flagcolor\='r',
                 barbcolor\=\['b', 'g'\], flip\_barb\=True,
                 barb\_increments\=dict(half\=10, full\=20, flag\=100))

\# Masked arrays are also supported
[masked\_u](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.ma.masked\_array](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['u'\])
[masked\_u](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\[4\] \= 1000  \# Bad value that should not be plotted when masked
[masked\_u](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\[4\] \= [np.ma.masked](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")

![barb demo](https://matplotlib.org/stable/_images/sphx_glr_barb_demo_001_2_00x.png)

Identical plot to panel 2 in the first figure, but with the point at (0.5, 0.25) missing (masked)

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax2.barbs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html#matplotlib.axes.Axes.barbs "matplotlib.axes.Axes.barbs")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['x'\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['y'\], [masked\_u](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['v'\], length\=8, pivot\='middle')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![barb demo](https://matplotlib.org/stable/_images/sphx_glr_barb_demo_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.barbs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html#matplotlib.axes.Axes.barbs "matplotlib.axes.Axes.barbs")
     / [`matplotlib.pyplot.barbs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barbs.html#matplotlib.pyplot.barbs "matplotlib.pyplot.barbs")
    

**Total running time of the script:** (0 minutes 1.171 seconds)

[`Download Jupyter notebook: barb_demo.ipynb`](https://matplotlib.org/stable/_downloads/bab4843756699babb62930efa5ac44d0/barb_demo.ipynb)

[`Download Python source code: barb_demo.py`](https://matplotlib.org/stable/_downloads/bd67ba4ff04d8ab5785fdcdf1d0f2c9c/barb_demo.py)

[`Download zipped: barb_demo.zip`](https://matplotlib.org/stable/_downloads/20a326842422149af9d41e78579e80a8/barb_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)