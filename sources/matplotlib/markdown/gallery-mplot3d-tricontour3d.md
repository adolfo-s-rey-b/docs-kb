[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html#sphx-glr-download-gallery-mplot3d-tricontour3d-py)
 to download the full example code.

Triangular 3D contour plot[#](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html#triangular-3d-contour-plot "Link to this heading")

=================================================================================================================================================

Contour plots of unstructured triangular grids.

The data used is the same as in the second plot of [More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html)
. [Triangular 3D filled contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontourf3d.html)
 shows the filled version of this example.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.tri as tri

[n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 48
[n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8
[min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.25

\# Create the mesh in polar coordinates and compute x, y, z.
[radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.95, [n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
, endpoint\=False)
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[..., [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\], [n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
, axis\=1)
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1::2\] += [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/[n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(3\*[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()

\# Create a custom triangulation.
[triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [tri.Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Mask off unwanted triangles.
[triang.set\_mask](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
([np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[triang.triangles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\].mean(axis\=1),
                         [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[triang.triangles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\].mean(axis\=1))
                < [min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')
[ax.tricontour](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour "mpl_toolkits.mplot3d.Axes3D.tricontour")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\="CMRmap")

\# Customize the view angle so it's easier to understand the plot.
[ax.view\_init](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "mpl_toolkits.mplot3d.Axes3D.view_init")
(elev\=45.)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tricontour3d](https://matplotlib.org/stable/_images/sphx_glr_tricontour3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [plot-type: specialty](https://matplotlib.org/stable/_tags/plot-type-specialty.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: tricontour3d.ipynb`](https://matplotlib.org/stable/_downloads/68a5283fe87ca0970437bffeab79056d/tricontour3d.ipynb)

[`Download Python source code: tricontour3d.py`](https://matplotlib.org/stable/_downloads/7a5a489f18d567fe1ed8c65dd4806079/tricontour3d.py)

[`Download zipped: tricontour3d.zip`](https://matplotlib.org/stable/_downloads/d8c78a64fa24e2f7a29709650b2ebf2e/tricontour3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)