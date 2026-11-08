[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html#sphx-glr-download-gallery-mplot3d-quiver3d-py)
 to download the full example code.

3D quiver plot[#](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html#d-quiver-plot "Link to this heading")

====================================================================================================================

Demonstrates plotting directional arrows at points on a 3D meshgrid.

import matplotlib.pyplot as plt
import numpy as np

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

\# Make the grid
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-0.8, 1, 0.2),
                      [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-0.8, 1, 0.2),
                      [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-0.8, 1, 0.8))

\# Make the direction data for the arrows
[u](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[v](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \-[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[w](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2.0 / 3.0) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \*
     [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[ax.quiver](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl_toolkits.mplot3d.axes3d.Axes3D.quiver "mpl_toolkits.mplot3d.Axes3D.quiver")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [u](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [v](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [w](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, length\=0.1, normalize\=True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![quiver3d](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: quiver3d.ipynb`](https://matplotlib.org/stable/_downloads/703b29cbf7edd050cdb2a0013bb4c7fb/quiver3d.ipynb)

[`Download Python source code: quiver3d.py`](https://matplotlib.org/stable/_downloads/19a0072d80eefa5dc179a38243c1da91/quiver3d.py)

[`Download zipped: quiver3d.zip`](https://matplotlib.org/stable/_downloads/ac162f20935a1c9ed15784588091784d/quiver3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)