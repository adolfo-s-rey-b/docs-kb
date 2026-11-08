[Skip to main content](https://matplotlib.org/stable/gallery/animation/rain.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/rain.html#sphx-glr-download-gallery-animation-rain-py)
 to download the full example code.

Rain simulation[#](https://matplotlib.org/stable/gallery/animation/rain.html#rain-simulation "Link to this heading")

=====================================================================================================================

Simulates rain drops on a surface by animating the scale and opacity of 50 scatter points.

Author: Nicolas P. Rougier

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import [FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# Create new Figure and an Axes which fills it.
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 7))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1), frameon\=False)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 1), [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[\])
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 1), [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[\])

\# Create rain data
[n\_drops](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 50
[rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
([n\_drops](https://docs.python.org/3/library/functions.html#int "builtins.int")
, dtype\=\[('position', float, (2,)),\
                                      ('size',     float),\
                                      ('growth',   float),\
                                      ('color',    float, (4,))\])

\# Initialize the raindrops in random positions and with
\# random growth rates.
[rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['position'\] \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(0, 1, ([n\_drops](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2))
[rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['growth'\] \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(50, 200, [n\_drops](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Construct the scatter which we will update during animation
\# as the raindrops develop.
[scat](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['position'\]\[:, 0\], [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['position'\]\[:, 1\],
                  s\=[rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['size'\], lw\=0.5, edgecolors\=[rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['color'\],
                  facecolors\='none')

def update(frame\_number):
    \# Get an index which we can use to re-spawn the oldest raindrop.
    current\_index \= frame\_number % [n\_drops](https://docs.python.org/3/library/functions.html#int "builtins.int")

    \# Make all colors more transparent as time progresses.
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['color'\]\[:, 3\] \-= 1.0/len([rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['color'\]\[:, 3\] \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
([rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['color'\]\[:, 3\], 0, 1)

    \# Make all circles bigger.
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['size'\] += [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['growth'\]

    \# Pick a new position for oldest rain drop, resetting its size,
    \# color and growth factor.
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['position'\]\[current\_index\] \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(0, 1, 2)
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['size'\]\[current\_index\] \= 5
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['color'\]\[current\_index\] \= (0, 0, 0, 1)
    [rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['growth'\]\[current\_index\] \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(50, 200)

    \# Update the scatter collection, with the new colors, sizes and positions.
    [scat.set\_edgecolors](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.set_edgecolors "matplotlib.collections.PathCollection.set_edgecolors")
([rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['color'\])
    [scat.set\_sizes](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.set_sizes "matplotlib.collections.PathCollection.set_sizes")
([rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['size'\])
    [scat.set\_offsets](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.set_offsets "matplotlib.collections.PathCollection.set_offsets")
([rain\_drops](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\['position'\])
    return \[[scat](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")\
\]

\# Construct the animation, using the update function as the animation director.
[animation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, update, interval\=10, save\_count\=100, blit\=True)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

**Total running time of the script:** (0 minutes 4.325 seconds)

[`Download Jupyter notebook: rain.ipynb`](https://matplotlib.org/stable/_downloads/aa47bfddb399ef4c2137b19dcf36813e/rain.ipynb)

[`Download Python source code: rain.py`](https://matplotlib.org/stable/_downloads/82a9940f7742825edaf57f41ee952e31/rain.py)

[`Download zipped: rain.zip`](https://matplotlib.org/stable/_downloads/a90c02b9cc4da0f26ae962b0c5993cdf/rain.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)