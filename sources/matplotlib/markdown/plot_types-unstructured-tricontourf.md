[Skip to main content](https://matplotlib.org/stable/plot_types/unstructured/tricontourf.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/plot_types/unstructured/tricontourf.html#sphx-glr-download-plot-types-unstructured-tricontourf-py)
 to download the full example code.

tricontourf(x, y, z)[#](https://matplotlib.org/stable/plot_types/unstructured/tricontourf.html#tricontourf-x-y-z "Link to this heading")

=========================================================================================================================================

Draw contour regions on an unstructured triangular grid.

See [`tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
.

![tricontourf](https://matplotlib.org/stable/_images/sphx_glr_tricontourf_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('\_mpl-gallery-nogrid')

\# make data:
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(1)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(\-3, 3, 256)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(\-3, 3, 256)
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (1 \- [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/2 + [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*5 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*3) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max(), 7)

\# plot:
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o', markersize\=2, color\='grey')
[ax.tricontourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-3, 3), ylim\=(\-3, 3))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: tricontourf.ipynb`](https://matplotlib.org/stable/_downloads/06d8568c9c6f02bf1c64744e15c4a416/tricontourf.ipynb)

[`Download Python source code: tricontourf.py`](https://matplotlib.org/stable/_downloads/e41d1680a93a490689990af0797a91bd/tricontourf.py)

[`Download zipped: tricontourf.zip`](https://matplotlib.org/stable/_downloads/523aaf766630dad5e0af80f4cfffce7f/tricontourf.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)