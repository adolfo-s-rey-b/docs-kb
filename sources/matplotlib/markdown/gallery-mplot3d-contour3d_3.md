[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html#sphx-glr-download-gallery-mplot3d-contour3d-3-py)
 to download the full example code.

Project contour profiles onto a graph[#](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html#project-contour-profiles-onto-a-graph "Link to this heading")

======================================================================================================================================================================

Demonstrates displaying a 3D surface while also projecting contour 'profiles' onto the 'walls' of the graph. See [Project filled contour onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html)
 for the filled version.

import matplotlib.pyplot as plt

from mpl\_toolkits.mplot3d import axes3d

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [axes3d.get\_test\_data](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.get_test_data.html#mpl_toolkits.mplot3d.axes3d.get_test_data "mpl_toolkits.mplot3d.axes3d.get_test_data")
(0.05)

\# Plot the 3D surface
[ax.plot\_surface](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.Axes3D.plot_surface")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='royalblue', lw\=0.5, rstride\=8, cstride\=8,
                alpha\=0.3)

\# Plot projections of the contours for each dimension.  By choosing offsets
\# that match the appropriate axes limits, the projected contours will sit on
\# the 'walls' of the graph.
[ax.contour](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contour "mpl_toolkits.mplot3d.Axes3D.contour")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zdir\='z', offset\=-100, cmap\='coolwarm')
[ax.contour](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contour "mpl_toolkits.mplot3d.Axes3D.contour")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zdir\='x', offset\=-40, cmap\='coolwarm')
[ax.contour](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contour "mpl_toolkits.mplot3d.Axes3D.contour")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zdir\='y', offset\=40, cmap\='coolwarm')

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-40, 40), ylim\=(\-40, 40), zlim\=(\-100, 100),
       xlabel\='X', ylabel\='Y', zlabel\='Z')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![contour3d 3](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: contour3d_3.ipynb`](https://matplotlib.org/stable/_downloads/724f50707805745b41a77c01741edb61/contour3d_3.ipynb)

[`Download Python source code: contour3d_3.py`](https://matplotlib.org/stable/_downloads/b38e7e6affb8627f98fe832e54458e99/contour3d_3.py)

[`Download zipped: contour3d_3.zip`](https://matplotlib.org/stable/_downloads/a9a7fb32a05e53431e537a4dd4150e0a/contour3d_3.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)