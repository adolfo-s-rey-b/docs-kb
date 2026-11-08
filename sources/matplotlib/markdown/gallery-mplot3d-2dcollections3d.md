[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html#sphx-glr-download-gallery-mplot3d-2dcollections3d-py)
 to download the full example code.

Plot 2D data on 3D plot[#](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html#plot-2d-data-on-3d-plot "Link to this heading")

==============================================================================================================================================

Demonstrates using ax.plot's _zdir_ keyword to plot 2D data on selective axes of a 3D plot.

import matplotlib.pyplot as plt
import numpy as np

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

\# Plot a sin curve using the x and y axes.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 100)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
) / 2 + 0.5
[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zs\=0, zdir\='z', label\='curve in (x, y)')

\# Plot scatterplot data (20 2D points per colour) on the x and z axes.
[colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ('r', 'g', 'b', 'k')

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.sample](https://numpy.org/doc/stable/reference/random/generated/numpy.random.sample.html#numpy.random.sample "numpy.random.sample")
(20 \* len([colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
))
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.sample](https://numpy.org/doc/stable/reference/random/generated/numpy.random.sample.html#numpy.random.sample "numpy.random.sample")
(20 \* len([colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
))
[c\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [c](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in [colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
:
    [c\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.extend(\[[c](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\] \* 20)
\# By using zdir='y', the y value of these points is fixed to the zs value 0
\# and the (x, y) points are plotted on the x and z axes.
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.Axes3D.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zs\=0, zdir\='y', [c](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[c\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\='points in (x, z)')

\# Make legend, set axes limits and labels
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.Axes3D.set_xlim")
(0, 1)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.Axes3D.set_ylim")
(0, 1)
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(0, 1)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Y')
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
('Z')

\# Customize the view angle so it's easier to see that the scatter points lie
\# on the plane y=0
[ax.view\_init](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "mpl_toolkits.mplot3d.Axes3D.view_init")
(elev\=20., azim\=-35, roll\=0)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![2dcollections3d](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: 2dcollections3d.ipynb`](https://matplotlib.org/stable/_downloads/87b02fdd47cd91a9a8a895daa970217b/2dcollections3d.ipynb)

[`Download Python source code: 2dcollections3d.py`](https://matplotlib.org/stable/_downloads/82806b819d5516f91bb92a2c94296201/2dcollections3d.py)

[`Download zipped: 2dcollections3d.zip`](https://matplotlib.org/stable/_downloads/47d3d4b718e5dfdded0e21af47e11e72/2dcollections3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)