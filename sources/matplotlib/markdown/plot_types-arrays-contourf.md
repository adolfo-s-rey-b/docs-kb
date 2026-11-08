[Skip to main content](https://matplotlib.org/stable/plot_types/arrays/contourf.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/plot_types/arrays/contourf.html#sphx-glr-download-plot-types-arrays-contourf-py)
 to download the full example code.

contourf(X, Y, Z)[#](https://matplotlib.org/stable/plot_types/arrays/contourf.html#contourf-x-y-z "Link to this heading")

==========================================================================================================================

Plot filled contours.

See [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
.

![contourf](https://matplotlib.org/stable/_images/sphx_glr_contourf_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('\_mpl-gallery-nogrid')

\# make data
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 256), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 256))
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (1 \- [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/2 + [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*5 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*3) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max(), 7)

\# plot
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: contourf.ipynb`](https://matplotlib.org/stable/_downloads/8d57aae9d22353bda3cdaff9a6c97986/contourf.ipynb)

[`Download Python source code: contourf.py`](https://matplotlib.org/stable/_downloads/df733f9bc8fdc992fa8ea76034ce706a/contourf.py)

[`Download zipped: contourf.zip`](https://matplotlib.org/stable/_downloads/c3a33ab4a3ff9d6f680f8b0487fa7a60/contourf.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)