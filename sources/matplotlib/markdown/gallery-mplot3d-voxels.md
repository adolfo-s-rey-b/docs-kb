[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/voxels.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/voxels.html#sphx-glr-download-gallery-mplot3d-voxels-py)
 to download the full example code.

3D voxel / volumetric plot[#](https://matplotlib.org/stable/gallery/mplot3d/voxels.html#d-voxel-volumetric-plot "Link to this heading")

========================================================================================================================================

Demonstrates plotting 3D volumetric objects with [`Axes3D.voxels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.axes3d.Axes3D.voxels")
.

import matplotlib.pyplot as plt
import numpy as np

\# prepare some coordinates
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.indices](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
((8, 8, 8))

\# draw cuboids in the top left and bottom right corners, and a link between
\# them
[cube1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 < 3) & ([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 < 3) & ([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 < 3)
[cube2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \>= 5) & ([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \>= 5) & ([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \>= 5)
[link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= abs([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + abs([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + abs([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) <= 2

\# combine the objects into a single boolean array
[voxelarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cube1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 | [cube2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 | [link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

\# set the colors of each object
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
([voxelarray.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, dtype\=object)
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\] \= 'red'
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[cube1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\] \= 'blue'
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[cube2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\] \= 'green'

\# and plot everything
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')
[ax.voxels](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.Axes3D.voxels")
([voxelarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolors\=[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='k')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![voxels](https://matplotlib.org/stable/_images/sphx_glr_voxels_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: voxels.ipynb`](https://matplotlib.org/stable/_downloads/6047bad52557db0e45848d3712c94cf5/voxels.ipynb)

[`Download Python source code: voxels.py`](https://matplotlib.org/stable/_downloads/fd67d226fbaf03bb9e4e8ad72f1fba81/voxels.py)

[`Download zipped: voxels.zip`](https://matplotlib.org/stable/_downloads/8818e4c8ceee86d4ecd5aa0a37141c4f/voxels.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)