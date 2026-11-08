[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/box3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/box3d.html#sphx-glr-download-gallery-mplot3d-box3d-py)
 to download the full example code.

3D box surface plot[#](https://matplotlib.org/stable/gallery/mplot3d/box3d.html#d-box-surface-plot "Link to this heading")

===========================================================================================================================

Given data on a gridded volume `X`, `Y`, `Z`, this example plots the data values on the volume surfaces.

The strategy is to select the data from each surface and plot contours separately using [`axes3d.Axes3D.contourf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.axes3d.Axes3D.contourf")
 with appropriate parameters _zdir_ and _offset_.

import matplotlib.pyplot as plt
import numpy as np

\# Define dimensions
[Nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [Ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [Nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100, 300, 500
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([Nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([Ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
), \-[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([Nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

\# Create fake data
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ((([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
+100)\*\*2 + ([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\-20)\*\*2 + 2\*[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)/1000+1)

[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'vmin': [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(),
    'vmax': [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max(),
    'levels': [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max(), 10),
}

\# Create a figure with 3D ax
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 4))
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(111, projection\='3d')

\# Plot contour surfaces
\_ \= [ax.contourf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.Axes3D.contourf")
(
    [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, :, 0\], [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, :, 0\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, :, 0\],
    zdir\='z', offset\=0, \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
\_ \= [ax.contourf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.Axes3D.contourf")
(
    [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :, :\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :, :\], [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :, :\],
    zdir\='y', offset\=0, \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
C \= [ax.contourf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.Axes3D.contourf")
(
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, \-1, :\], [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, \-1, :\], [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, \-1, :\],
    zdir\='x', offset\=[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max(), \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
\# --

\# Set limits of the plot from coord limits
[xmin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 \= [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()
[ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [ymax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 \= [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()
[zmin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [zmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 \= [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=([xmin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
), ylim\=([ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [ymax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
), zlim\=([zmin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [zmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
))

\# Plot edges
[edges\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(color\='0.4', linewidth\=1, zorder\=1e3)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")
(\[[xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], \[[ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [ymax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], 0, \*\*[edges\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")
(\[[xmin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], \[[ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], 0, \*\*[edges\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")
(\[[xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [xmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], \[[ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [ymin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], \[[zmin](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
, [zmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], \*\*[edges\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Set labels and zticks
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(
    xlabel\='X \[km\]',
    ylabel\='Y \[km\]',
    zlabel\='Z \[m\]',
    zticks\=\[0, \-150, \-300, \-450\],
)

\# Set zoom and angle view
[ax.view\_init](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "mpl_toolkits.mplot3d.Axes3D.view_init")
(40, \-30, 0)
[ax.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.Axes3D.set_box_aspect")
(None, zoom\=0.9)

\# Colorbar
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
(C, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
\=[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, fraction\=0.02, pad\=0.1, label\='Name \[units\]')

\# Show Figure
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![box3d](https://matplotlib.org/stable/_images/sphx_glr_box3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 4.064 seconds)

[`Download Jupyter notebook: box3d.ipynb`](https://matplotlib.org/stable/_downloads/a32d02eae468647297d6a1944c6a272e/box3d.ipynb)

[`Download Python source code: box3d.py`](https://matplotlib.org/stable/_downloads/2f55e7d3c6f1f46dcc05e217087e84df/box3d.py)

[`Download zipped: box3d.zip`](https://matplotlib.org/stable/_downloads/cb657af57dc65f9ca0865cab28654dea/box3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)