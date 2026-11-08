[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_log.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_log.html#sphx-glr-download-gallery-images-contours-and-fields-contourf-log-py)
 to download the full example code.

Contourf and log color scale[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_log.html#contourf-and-log-color-scale "Link to this heading")

========================================================================================================================================================================

Demonstrate use of a log color scale in contourf

import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

from matplotlib import ticker

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3.0, 3.0, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-2.0, 2.0, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# A low hump with a spike coming out.
\# Needs to have z/colour axis on a log scale, so we see both hump and spike.
\# A linear scale only shows the spike.
[Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 10)\*\*2 \- ([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 10)\*\*2)
[z](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 50 \* [Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

\# Put in some negative values (lower left corner) to cause trouble with logs:
[z](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\[:5, :5\] \= \-1

\# The following is not strictly essential, but it will eliminate
\# a warning.  Comment it out to see the warning.
[z](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [ma.masked\_where](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")
([z](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 <= 0, [z](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
)

\# Automatic selection of levels works; setting the
\# log locator tells contourf to use a log scale:
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[cs](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, locator\=[ticker.LogLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
(), cmap\="PuBu\_r")

\# Alternatively, you can manually set the levels
\# and the norm:
\# lev\_exp = np.arange(np.floor(np.log10(z.min())-1),
\#                    np.ceil(np.log10(z.max())+1))
\# levs = np.power(10, lev\_exp)
\# cs = ax.contourf(X, Y, z, levs, norm=colors.LogNorm())

[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cs](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![contourf log](https://matplotlib.org/stable/_images/sphx_glr_contourf_log_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
     / [`matplotlib.pyplot.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    
*   [`matplotlib.axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
     / [`matplotlib.pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
    
*   [`matplotlib.ticker.LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
    

[`Download Jupyter notebook: contourf_log.ipynb`](https://matplotlib.org/stable/_downloads/a18365d572242ad1c2a687108c0c710c/contourf_log.ipynb)

[`Download Python source code: contourf_log.py`](https://matplotlib.org/stable/_downloads/bdf1327bcdd8760e8c91d7fc29b81b8e/contourf_log.py)

[`Download zipped: contourf_log.zip`](https://matplotlib.org/stable/_downloads/7485caeb81d5ada89e051776c1eac0bf/contourf_log.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)