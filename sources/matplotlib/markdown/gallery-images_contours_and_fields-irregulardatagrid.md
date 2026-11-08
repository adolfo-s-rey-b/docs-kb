[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html#sphx-glr-download-gallery-images-contours-and-fields-irregulardatagrid-py)
 to download the full example code.

Contour plot of irregularly spaced data[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html#contour-plot-of-irregularly-spaced-data "Link to this heading")

===================================================================================================================================================================================================

Comparison of a contour plot of irregularly spaced data interpolated on a regular grid versus a tricontour plot for an unstructured triangular grid.

Since [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 expect the data to live on a regular grid, plotting a contour plot of irregularly spaced data requires different methods. The two options are:

*   Interpolate the data to a regular grid first. This can be done with on-board means, e.g. via [`LinearTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
     or using external functionality e.g. via [`scipy.interpolate.griddata`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html#scipy.interpolate.griddata "(in SciPy v1.18.0)")
    . Then plot the interpolated data with the usual [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
    .
    
*   Directly use [`tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
     or [`tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
     which will perform a triangulation internally.
    

This example shows both methods in action.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.tri as tri

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
[ngridx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[ngridy](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(\-2, 2, [npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(\-2, 2, [npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2)

\# -----------------------
\# Interpolation on a grid
\# -----------------------
\# A contour plot of irregularly spaced data coordinates
\# via interpolation on a grid.

\# Create grid values first.
[xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-2.1, 2.1, [ngridx](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-2.1, 2.1, [ngridy](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Linearly interpolate the data (x, y) on a grid defined by (xi, yi).
[triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [tri.Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[interpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
 \= [tri.LinearTriInterpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[Xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[zi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [interpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
([Xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Note that scipy.interpolate provides means to interpolate data on a grid
\# as well. The following would be an alternative to the four lines above:
\# from scipy.interpolate import griddata
\# zi = griddata((x, y), z, (xi\[None, :\], yi\[:, None\]), method='linear')

[ax1.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, levels\=14, linewidths\=0.5, colors\='k')
[cntr1](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax1.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, levels\=14, cmap\="RdBu\_r")

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cntr1](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
, ax\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'ko', ms\=3)
[ax1.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-2, 2), ylim\=(\-2, 2))
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('grid and contour (%d points, %d grid points)' %
              ([npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ngridx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [ngridy](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

\# ----------
\# Tricontour
\# ----------
\# Directly supply the unordered, irregularly spaced coordinates
\# to tricontour.

[ax2.tricontour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, levels\=14, linewidths\=0.5, colors\='k')
[cntr2](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "matplotlib.tri.TriContourSet")
 \= [ax2.tricontourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, levels\=14, cmap\="RdBu\_r")

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cntr2](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "matplotlib.tri.TriContourSet")
, ax\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'ko', ms\=3)
[ax2.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-2, 2), ylim\=(\-2, 2))
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('tricontour (%d points)' % [npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(hspace\=0.5)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![grid and contour (200 points, 20000 grid points), tricontour (200 points)](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
     / [`matplotlib.pyplot.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
    
*   [`matplotlib.axes.Axes.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
     / [`matplotlib.pyplot.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
    
*   [`matplotlib.axes.Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
     / [`matplotlib.pyplot.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontour.html#matplotlib.pyplot.tricontour "matplotlib.pyplot.tricontour")
    
*   [`matplotlib.axes.Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
     / [`matplotlib.pyplot.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "matplotlib.pyplot.tricontourf")
    

**Total running time of the script:** (0 minutes 1.072 seconds)

[`Download Jupyter notebook: irregulardatagrid.ipynb`](https://matplotlib.org/stable/_downloads/dbebf5e34b56820f67ad4cfeeacefaa9/irregulardatagrid.ipynb)

[`Download Python source code: irregulardatagrid.py`](https://matplotlib.org/stable/_downloads/758c39512ff467ae08f5d49cccfb7f30/irregulardatagrid.py)

[`Download zipped: irregulardatagrid.zip`](https://matplotlib.org/stable/_downloads/96dd97c30ea1233604567352a6b8d90b/irregulardatagrid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)