[Skip to main content](https://matplotlib.org/stable/plot_types/3D/trisurf3d_simple.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/plot_types/3D/trisurf3d_simple.html#sphx-glr-download-plot-types-3d-trisurf3d-simple-py)
 to download the full example code.

plot\_trisurf(x, y, z)[#](https://matplotlib.org/stable/plot_types/3D/trisurf3d_simple.html#plot-trisurf-x-y-z "Link to this heading")

=======================================================================================================================================

See [`plot_trisurf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf")
.

![trisurf3d simple](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_simple_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('\_mpl-gallery')

[n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8
[n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 36

\# Make radii and angles spaces
[radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.125, 1.0, [n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
, endpoint\=False)\[..., [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

\# Convert polar (radii, angles) coords to cartesian (x, y) coords.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(0, ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten())
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(0, ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten())
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Plot
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\={'projection': '3d'})
[ax.plot\_trisurf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.Axes3D.plot_trisurf")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min() \* 2, cmap\="Blues")

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xticklabels\=\[\],
       yticklabels\=\[\],
       zticklabels\=\[\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: trisurf3d_simple.ipynb`](https://matplotlib.org/stable/_downloads/cd674f07796f1263c2618071b6eb1746/trisurf3d_simple.ipynb)

[`Download Python source code: trisurf3d_simple.py`](https://matplotlib.org/stable/_downloads/e3e638c790e8cedaa78c03303fd6f563/trisurf3d_simple.py)

[`Download zipped: trisurf3d_simple.zip`](https://matplotlib.org/stable/_downloads/feaa60e57c5df8addf5e8058d10efe16/trisurf3d_simple.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)