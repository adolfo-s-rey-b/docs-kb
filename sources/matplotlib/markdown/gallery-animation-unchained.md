[Skip to main content](https://matplotlib.org/stable/gallery/animation/unchained.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/unchained.html#sphx-glr-download-gallery-animation-unchained-py)
 to download the full example code.

Matplotlib unchained[#](https://matplotlib.org/stable/gallery/animation/unchained.html#matplotlib-unchained "Link to this heading")

====================================================================================================================================

Comparative path demonstration of frequency from a fake signal of a pulsar (mostly known because of the cover for Joy Division's Unknown Pleasures).

Author: Nicolas P. Rougier

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# Create new Figure with black background
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 8), facecolor\='black')

\# Add a subplot with no frame
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(frameon\=False)

\# Generate random data
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(0, 1, (64, 75))
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 1, [data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[\-1\])
[G](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 1.5 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-4 \* [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\* 2)

\# Generate line plots
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(len([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)):
    \# Small reduction of the X extents to get a cheap perspective effect
    [xscale](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1 \- [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / 200.
    \# Same for linewidth (thicker strokes on bottom)
    [lw](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1.5 \- [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / 100.0
    [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xscale](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [G](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], color\="w", [lw](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[lw](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)

\# Set y limit (or first line is cropped because of thickness)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1, 70)

\# No ticks
[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[\])
[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[\])

\# 2 part titles to get different font weights
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 1.0, "MATPLOTLIB ", transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
        ha\="right", va\="bottom", color\="w",
        family\="sans-serif", fontweight\="light", fontsize\=16)
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 1.0, "UNCHAINED", transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
        ha\="left", va\="bottom", color\="w",
        family\="sans-serif", fontweight\="bold", fontsize\=16)

def update(\*args):
    \# Shift all data to the right
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1:\] \= [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, :\-1\]

    \# Fill-in new values
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\] \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(0, 1, len([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

    \# Update data
    for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(len([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)):
        [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\].set\_ydata([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [G](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])

    \# Return modified artists
    return [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

\# Construct the animation, using the update function as the animation director.
[anim](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, update, interval\=10, save\_count\=100)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

**Total running time of the script:** (0 minutes 12.307 seconds)

[`Download Jupyter notebook: unchained.ipynb`](https://matplotlib.org/stable/_downloads/43aba940936123ae3bf6a228b455360d/unchained.ipynb)

[`Download Python source code: unchained.py`](https://matplotlib.org/stable/_downloads/bf0c66d82443515f6ffc1625103c0329/unchained.py)

[`Download zipped: unchained.zip`](https://matplotlib.org/stable/_downloads/8926619bec5aa56707a7ceaa0907e19f/unchained.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)