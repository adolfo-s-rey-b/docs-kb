[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html#sphx-glr-download-gallery-mplot3d-subplot3d-py)
 to download the full example code.

3D plots as subplots[#](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html#d-plots-as-subplots "Link to this heading")

=================================================================================================================================

Demonstrate including 3D plots as subplots.

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits.mplot3d.axes3d import [get\_test\_data](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.get_test_data.html#mpl_toolkits.mplot3d.axes3d.get_test_data "mpl_toolkits.mplot3d.axes3d.get_test_data")

\# set up a figure twice as wide as it is tall
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=plt.figaspect(0.5))

\# =============
\# First subplot
\# =============
\# set up the Axes for the first plot
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 2, 1, projection\='3d')

\# plot a 3D surface like in the example mplot3d/surface3d\_demo
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-5, 5, 0.25)
[Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-5, 5, 0.25)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[surf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
 \= [ax.plot\_surface](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.Axes3D.plot_surface")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, rstride\=1, cstride\=1, cmap\="coolwarm",
                       linewidth\=0, antialiased\=False)
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(\-1.01, 1.01)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([surf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
, shrink\=0.5, aspect\=10)

\# ==============
\# Second subplot
\# ==============
\# set up the Axes for the second plot
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 2, 2, projection\='3d')

\# plot a 3D wireframe like in the example mplot3d/wire3d\_demo
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [get\_test\_data](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.get_test_data.html#mpl_toolkits.mplot3d.axes3d.get_test_data "mpl_toolkits.mplot3d.axes3d.get_test_data")
(0.05)
[ax.plot\_wireframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.Axes3D.plot_wireframe")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, rstride\=10, cstride\=10)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![subplot3d](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [level: advanced](https://matplotlib.org/stable/_tags/level-advanced.html)

[`Download Jupyter notebook: subplot3d.ipynb`](https://matplotlib.org/stable/_downloads/c13493368b9c88973db36ca69a3f3288/subplot3d.ipynb)

[`Download Python source code: subplot3d.py`](https://matplotlib.org/stable/_downloads/c4f54a042d9a81d3afae26490415434f/subplot3d.py)

[`Download zipped: subplot3d.zip`](https://matplotlib.org/stable/_downloads/710b031ac741dd0133a51864c0ac7b50/subplot3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)