[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/offset.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/offset.html#sphx-glr-download-gallery-mplot3d-offset-py)
 to download the full example code.

Automatic text offsetting[#](https://matplotlib.org/stable/gallery/mplot3d/offset.html#automatic-text-offsetting "Link to this heading")

=========================================================================================================================================

This example demonstrates mplot3d's offset text display. As one rotates the 3D figure, the offsets should remain oriented the same way as the axis label, and should also be located "away" from the center of the plot.

This demo triggers the display of the offset text for the x- and y-axis by adding 1e5 to X and Y. Anything less would not automatically trigger it.

import matplotlib.pyplot as plt
import numpy as np

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:6\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
:0.25, 0:4\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
:0.25\]
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)))

[ax.plot\_surface](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.Axes3D.plot_surface")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 1e5, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 1e5, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='autumn', cstride\=2, rstride\=2)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("X label")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Y label")
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
("Z label")
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(0, 2)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![offset](https://matplotlib.org/stable/_images/sphx_glr_offset_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: label](https://matplotlib.org/stable/_tags/component-label.html)
 [interactivity: pan](https://matplotlib.org/stable/_tags/interactivity-pan.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: offset.ipynb`](https://matplotlib.org/stable/_downloads/0bf9e51dec88ec25526322495c8e6273/offset.ipynb)

[`Download Python source code: offset.py`](https://matplotlib.org/stable/_downloads/83a4da0793b08ae8f45786e3c9b4e373/offset.py)

[`Download zipped: offset.zip`](https://matplotlib.org/stable/_downloads/5a62c04ed80b04c20b3ecc8c78c12cd3/offset.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)