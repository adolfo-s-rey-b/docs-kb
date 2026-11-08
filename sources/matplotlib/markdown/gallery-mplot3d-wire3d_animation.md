[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html#sphx-glr-download-gallery-mplot3d-wire3d-animation-py)
 to download the full example code.

Animate a 3D wireframe plot[#](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html#animate-a-3d-wireframe-plot "Link to this heading")

=======================================================================================================================================================

A very simple "animation" of a 3D plot. See also [Rotating a 3D plot](https://matplotlib.org/stable/gallery/mplot3d/rotate_axes3d_sgskip.html)
.

import time

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation

[FRAMES](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 25
[FPS](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 25

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='3d')

\# Make the X, Y meshgrid.
[xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 1, 50)
[ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 1, 50)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Set the z axis limits, so they aren't recalculated each frame.
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(\-1, 1)

\# Begin plotting.
[wframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
 \= None
[tstart](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

def animate(i):
    global [wframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
    \# If a line collection is already there, remove it before drawing.
    if [wframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
:
        [wframe.remove](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.remove "matplotlib.collections.LineCollection.remove")
()
    \# Generate data.
    phi \= i / [FRAMES](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
    Z \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + phi) \* (1 \- [np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
    \# Plot the new wireframe.
    [wframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
 \= [ax.plot\_wireframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.Axes3D.plot_wireframe")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, Z, rstride\=2, cstride\=2)
    if i \== [FRAMES](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 1:  \# Print FPS at the end of the loop.
        global [tstart](https://docs.python.org/3/library/functions.html#float "builtins.float")
        fps \= [FRAMES](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / ([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- [tstart](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
        print(f'Expected FPS: {[FPS](https://docs.python.org/3/library/functions.html#int "builtins.int")
}; Average FPS: {fps}')
        [tstart](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, animate, interval\=1000 / [FPS](https://docs.python.org/3/library/functions.html#int "builtins.int")
, frames\=[FRAMES](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 7.930 seconds)

[`Download Jupyter notebook: wire3d_animation.ipynb`](https://matplotlib.org/stable/_downloads/7d10b19f3ad63ee10e868a77a9ed217d/wire3d_animation.ipynb)

[`Download Python source code: wire3d_animation.py`](https://matplotlib.org/stable/_downloads/6d68debb7e627042420b2f4fe2e7b95b/wire3d_animation.py)

[`Download zipped: wire3d_animation.zip`](https://matplotlib.org/stable/_downloads/14f53e675babc307f8a23695809b9271/wire3d_animation.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)