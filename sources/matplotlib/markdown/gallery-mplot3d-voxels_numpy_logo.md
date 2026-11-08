[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html#sphx-glr-download-gallery-mplot3d-voxels-numpy-logo-py)
 to download the full example code.

3D voxel plot of the NumPy logo[#](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html#d-voxel-plot-of-the-numpy-logo "Link to this heading")

===============================================================================================================================================================

Demonstrates using [`Axes3D.voxels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.axes3d.Axes3D.voxels")
 with uneven coordinates.

import matplotlib.pyplot as plt
import numpy as np

def explode(data):
    size \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(data.shape)\*2
    data\_e \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(size \- 1, dtype\=data.dtype)
    data\_e\[::2, ::2, ::2\] \= data
    return data\_e

\# build up the numpy logo
[n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((4, 3, 4), dtype\=bool)
[n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0, :\] \= True
[n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1, 0, :\] \= True
[n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0, 2\] \= True
[n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 0, 1\] \= True
[facecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
([n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, '#FFD65DC0', '#7A88CCC0')
[edgecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
([n\_voxels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, '#BFAB6E', '#7D84A6')
[filled](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
([n\_voxels.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

\# upscale the above voxel image, leaving gaps
[filled\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= explode([filled](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fcolors\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= explode([facecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ecolors\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= explode([edgecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Shrink the gaps
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.indices](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
([np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
([filled\_2.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
) + 1).astype(float) // 2
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0::2, :, :\] += 0.05
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0::2, :\] += 0.05
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, :, 0::2\] += 0.05
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1::2, :, :\] += 0.95
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1::2, :\] += 0.95
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, :, 1::2\] += 0.95

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')
[ax.voxels](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.Axes3D.voxels")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [filled\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [facecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[fcolors\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [edgecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[ecolors\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect "mpl_toolkits.mplot3d.Axes3D.set_aspect")
('equal')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![voxels numpy logo](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

[`Download Jupyter notebook: voxels_numpy_logo.ipynb`](https://matplotlib.org/stable/_downloads/33618e5946569f09d6d05a6462fb6a50/voxels_numpy_logo.ipynb)

[`Download Python source code: voxels_numpy_logo.py`](https://matplotlib.org/stable/_downloads/867a604be5ec8886b7254918995d5a2a/voxels_numpy_logo.py)

[`Download zipped: voxels_numpy_logo.zip`](https://matplotlib.org/stable/_downloads/334d8756f608f2fd68905c5431151425/voxels_numpy_logo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)