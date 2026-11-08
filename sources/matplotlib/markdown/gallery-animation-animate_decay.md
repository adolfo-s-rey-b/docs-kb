[Skip to main content](https://matplotlib.org/stable/gallery/animation/animate_decay.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/animate_decay.html#sphx-glr-download-gallery-animation-animate-decay-py)
 to download the full example code.

Decay[#](https://matplotlib.org/stable/gallery/animation/animate_decay.html#decay "Link to this heading")

==========================================================================================================

This example showcases:

*   using a generator to drive an animation,
    
*   changing axes limits during an animation.
    

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import itertools

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

def data\_gen():
    for cnt in [itertools.count](https://docs.python.org/3/library/itertools.html#itertools.count "itertools.count")
():
        t \= cnt / 10
        yield t, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*t) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-t/10.)

def init():
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1.1, 1.1)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 1)
    del [xdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[:\]
    del [ydata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[:\]
    [line.set\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
([xdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ydata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    return [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[\], \[\], lw\=2)
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[xdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ydata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\], \[\]

def run(data):
    \# update the data
    t, y \= data
    [xdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append(t)
    [ydata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append(y)
    xmin, xmax \= [ax.get\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib.axes.Axes.get_xlim "matplotlib.axes.Axes.get_xlim")
()

    if t \>= xmax:
        [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(xmin, 2\*xmax)
        [ax.figure.canvas.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
()
    [line.set\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
([xdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ydata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

    return [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,

\# Only save last 100 frames, but run forever
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, run, data\_gen, interval\=100, init\_func\=init,
                              save\_count\=100)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 36.297 seconds)

[`Download Jupyter notebook: animate_decay.ipynb`](https://matplotlib.org/stable/_downloads/cfbd1208088e34becd3522566eb8852f/animate_decay.ipynb)

[`Download Python source code: animate_decay.py`](https://matplotlib.org/stable/_downloads/da849a0c4ef3902883df5d0cb7e42c6d/animate_decay.py)

[`Download zipped: animate_decay.zip`](https://matplotlib.org/stable/_downloads/ef5a80619e5e5314951b8b79c57aa431/animate_decay.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)