[Skip to main content](https://matplotlib.org/stable/plot_types/arrays/barbs.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/plot_types/arrays/barbs.html#sphx-glr-download-plot-types-arrays-barbs-py)
 to download the full example code.

barbs(X, Y, U, V)[#](https://matplotlib.org/stable/plot_types/arrays/barbs.html#barbs-x-y-u-v "Link to this heading")

======================================================================================================================

Plot a 2D field of wind barbs.

See [`barbs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html#matplotlib.axes.Axes.barbs "matplotlib.axes.Axes.barbs")
.

![barbs](https://matplotlib.org/stable/_images/sphx_glr_barbs_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('\_mpl-gallery-nogrid')

\# make data:
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(\[1, 2, 3, 4\], \[1, 2, 3, 4\])
[angle](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 180 \* [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[15., 30, 35, 45\],\
                                \[25., 40, 55, 60\],\
                                \[35., 50, 65, 75\],\
                                \[45., 60, 75, 90\]\])
[amplitude](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[5, 10, 25, 50\],\
                      \[10, 15, 30, 60\],\
                      \[15, 26, 50, 70\],\
                      \[20, 45, 80, 100\]\])
[U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [amplitude](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angle](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [amplitude](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angle](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# plot:
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.barbs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html#matplotlib.axes.Axes.barbs "matplotlib.axes.Axes.barbs")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, barbcolor\='C0', flagcolor\='C0', length\=7, linewidth\=1.5)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 4.5), ylim\=(0, 4.5))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: barbs.ipynb`](https://matplotlib.org/stable/_downloads/b6f78f97f7fbec71abb3c6aefc1d4c7d/barbs.ipynb)

[`Download Python source code: barbs.py`](https://matplotlib.org/stable/_downloads/417acbb12d2b6a185f7af1ca9b76b6ff/barbs.py)

[`Download zipped: barbs.zip`](https://matplotlib.org/stable/_downloads/bd94b7dc54ad2bd65502788388582524/barbs.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)