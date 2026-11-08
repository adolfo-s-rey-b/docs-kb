[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html#sphx-glr-download-gallery-mplot3d-surface3d-3-py)
 to download the full example code.

3D surface (checkerboard)[#](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html#d-surface-checkerboard "Link to this heading")

===========================================================================================================================================

Demonstrates plotting a 3D surface colored in a checkerboard pattern.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import [LinearLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

\# Make data.
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-5, 5, 0.25)
[xlen](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-5, 5, 0.25)
[ylen](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
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

\# Create an empty array of strings with the same shape as the meshgrid, and
\# populate it with two colors in a checkerboard pattern.
[colortuple](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ('y', 'b')
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
([X.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, dtype\=str)
for [y](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([ylen](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    for [x](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([xlen](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
        [colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [x](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \= [colortuple](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[([x](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + [y](https://docs.python.org/3/library/functions.html#int "builtins.int")\
) % len([colortuple](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
)\]

\# Plot the surface with face colors taken from the array we made.
[surf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
 \= [ax.plot\_surface](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.Axes3D.plot_surface")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolors\=[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, linewidth\=0)

\# Customize the z axis.
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(\-1, 1)
[ax.zaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([LinearLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
(6))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![surface3d 3](https://matplotlib.org/stable/_images/sphx_glr_surface3d_3_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [styling: texture](https://matplotlib.org/stable/_tags/styling-texture.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: surface3d_3.ipynb`](https://matplotlib.org/stable/_downloads/f85a4826d5f863544b5245673efce070/surface3d_3.ipynb)

[`Download Python source code: surface3d_3.py`](https://matplotlib.org/stable/_downloads/b15db7f5b24291b354e391b3aea48b1b/surface3d_3.py)

[`Download zipped: surface3d_3.zip`](https://matplotlib.org/stable/_downloads/d80e1a51a3b125e4db53cf57de9990a8/surface3d_3.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)