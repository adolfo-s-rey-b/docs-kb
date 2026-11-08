[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html#sphx-glr-download-gallery-mplot3d-scatter3d-py)
 to download the full example code.

3D scatterplot[#](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html#d-scatterplot "Link to this heading")

=====================================================================================================================

Demonstration of a basic scatterplot in 3D.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

def randrange([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax \- vmin)\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + vmin

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='3d')

[n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100

\# For each set of style and range settings, plot n random points in the box
\# defined by x in \[23, 32\], y in \[0, 100\], z in \[zlow, zhigh\].
for [m](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [zlow](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [zhigh](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in \[('o', \-50, \-25), ('^', \-30, \-5)\]:
    [xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= randrange([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 23, 32)
    [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= randrange([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 0, 100)
    [zs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= randrange([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [zlow](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [zhigh](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax.scatter](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.Axes3D.scatter")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\=[m](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X Label')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Y Label')
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
('Z Label')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scatter3d](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: scatter3d.ipynb`](https://matplotlib.org/stable/_downloads/03ed879008811eb700082f93269e95f9/scatter3d.ipynb)

[`Download Python source code: scatter3d.py`](https://matplotlib.org/stable/_downloads/faa507e7c87c72109d38e6eaffdc42e0/scatter3d.py)

[`Download zipped: scatter3d.zip`](https://matplotlib.org/stable/_downloads/2dc3f6f1bb6bf77a4e3af07b85a500de/scatter3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)