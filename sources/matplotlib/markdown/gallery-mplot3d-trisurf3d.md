[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html#sphx-glr-download-gallery-mplot3d-trisurf3d-py)
 to download the full example code.

Triangular 3D surfaces[#](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html#triangular-3d-surfaces "Link to this heading")

======================================================================================================================================

Plot a 3D surface with a triangular mesh.

import matplotlib.pyplot as plt
import numpy as np

[n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8
[n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 36

\# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
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
\# (0, 0) is manually added at this stage,  so there will be no duplicate
\# points in the (x, y) plane.
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

\# Compute z to make the pringle surface.
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

[ax.plot\_trisurf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.Axes3D.plot_trisurf")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, linewidth\=0.2, antialiased\=True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![trisurf3d](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: trisurf3d.ipynb`](https://matplotlib.org/stable/_downloads/e9dad76e7dc8b245cfd741fea5807c99/trisurf3d.ipynb)

[`Download Python source code: trisurf3d.py`](https://matplotlib.org/stable/_downloads/5ba35d292df2f5c2bdb433ab0de992f5/trisurf3d.py)

[`Download zipped: trisurf3d.zip`](https://matplotlib.org/stable/_downloads/9e0b430fddf4005f895f92a42b2b5adf/trisurf3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)