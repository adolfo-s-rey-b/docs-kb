[Skip to main content](https://matplotlib.org/stable/gallery/animation/random_walk.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/random_walk.html#sphx-glr-download-gallery-animation-random-walk-py)
 to download the full example code.

Animated 3D random walk[#](https://matplotlib.org/stable/gallery/animation/random_walk.html#animated-3d-random-walk "Link to this heading")

============================================================================================================================================

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

def random\_walk([num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
, max\_step\=0.05):
    """Return a 3D random walk as (num\_steps, 3) array."""
    start\_pos \= [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(3)
    steps \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(\-max\_step, max\_step, size\=([num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 3))
    walk \= start\_pos + [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
(steps, axis\=0)
    return walk

def update\_lines(num, [walks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    for line, walk in zip([lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [walks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        line.set\_data\_3d(walk\[:num, :\].T)
    return [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

\# Data: 40 random walks as (num\_steps, 3) arrays
[num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 30
[walks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[random\_walk([num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")\
) for index in range(40)\]

\# Attaching 3D axis to the figure
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\="3d")

\# Create lines initially without data
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")\
(\[\], \[\], \[\])\[0\] for \_ in [walks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]

\# Setting the Axes properties
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim3d\=(0, 1), xlabel\='X')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(ylim3d\=(0, 1), ylabel\='Y')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(zlim3d\=(0, 1), zlabel\='Z')

\# Creating the Animation object
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, update\_lines, [num\_steps](https://docs.python.org/3/library/functions.html#int "builtins.int")
, fargs\=([walks](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), interval\=100)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)
 [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)

**Total running time of the script:** (0 minutes 12.972 seconds)

[`Download Jupyter notebook: random_walk.ipynb`](https://matplotlib.org/stable/_downloads/09240349fdbe840c8c1035b1e275de73/random_walk.ipynb)

[`Download Python source code: random_walk.py`](https://matplotlib.org/stable/_downloads/91e0d0fab354a73fa9330139a9fac0f5/random_walk.py)

[`Download zipped: random_walk.zip`](https://matplotlib.org/stable/_downloads/f72bb0386fa2ec994692d43579ea612f/random_walk.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)