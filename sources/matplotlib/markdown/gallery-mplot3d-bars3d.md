[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html#sphx-glr-download-gallery-mplot3d-bars3d-py)
 to download the full example code.

Create 2D bar graphs in different planes[#](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html#create-2d-bar-graphs-in-different-planes "Link to this heading")

=======================================================================================================================================================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto planes y=0, y=1, etc.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='3d')

[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['r', 'g', 'b', 'y'\]
[yticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[3, 2, 1, 0\]
for [c](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in zip([colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [yticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    \# Generate the random data for the y=k 'layer'.
    [xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(20)
    [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(20)

    \# You can provide either a single color or an array with the same length as
    \# xs and ys. To demonstrate this, we color the first bar of each set cyan.
    [cs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[c](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\] \* len([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [cs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\] \= 'c'

    \# Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    [ax.bar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar "mpl_toolkits.mplot3d.Axes3D.bar")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, zs\=[k](https://docs.python.org/3/library/functions.html#int "builtins.int")
, zdir\='y', color\=[cs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, alpha\=0.8)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Y')
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
('Z')

\# On the y-axis let's only label the discrete values that we have data for.
[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
([yticks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![bars3d](https://matplotlib.org/stable/_images/sphx_glr_bars3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: bars3d.ipynb`](https://matplotlib.org/stable/_downloads/7282c789d1e66884fa31d4ac7d4a5e0a/bars3d.ipynb)

[`Download Python source code: bars3d.py`](https://matplotlib.org/stable/_downloads/5b023f7fea1b0a1fc6abfea4090951a1/bars3d.py)

[`Download zipped: bars3d.zip`](https://matplotlib.org/stable/_downloads/3ea0fd4f26f308ef6b871fcc9bfd54a5/bars3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)