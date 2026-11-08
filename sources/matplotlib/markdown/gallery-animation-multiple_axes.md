[Skip to main content](https://matplotlib.org/stable/gallery/animation/multiple_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/multiple_axes.html#sphx-glr-download-gallery-animation-multiple-axes-py)
 to download the full example code.

Multiple Axes animation[#](https://matplotlib.org/stable/gallery/animation/multiple_axes.html#multiple-axes-animation "Link to this heading")

==============================================================================================================================================

This example showcases:

*   how animation across multiple subplots works,
    
*   using a figure artist in the animation.
    

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from matplotlib.patches import [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([axl](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [axr](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    ncols\=2,
    sharey\=True,
    figsize\=(6, 2),
    gridspec\_kw\=dict(width\_ratios\=\[1, 3\], wspace\=0),
)
[axl.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
(1)
[axr.set\_box\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
(1 / 3)
[axr.yaxis.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
[axr.xaxis.set\_ticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")
(\[0, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\], \["0", r"$\\pi$", r"$2\\pi$"\])

\# draw circle with initial point in left Axes
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 50)
[axl.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), "k", lw\=0.3)
[point](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [axl.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(0, 0, "o")

\# draw full curve to set view limits in right Axes
[sine](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [axr.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

\# draw connecting line between both graphs
[con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 \= [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA\=[axl](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    axesB\=[axr](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    color\="C0",
    ls\="dotted",
)
[fig.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
([con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
)

def animate(i):
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, i, int(i \* 25 / [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
    [sine.set\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, y \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(i), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(i)
    [point.set\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")
(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\], \[y\])
    [con.xy1](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, y
    [con.xy2](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= i, y
    return [point](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [sine](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
(
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
,
    animate,
    interval\=50,
    blit\=False,  \# blitting can't be used with Figure artists
    frames\=[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
    repeat\_delay\=100,
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches.ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
    
*   [`matplotlib.animation.FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
    

Tags: [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)

**Total running time of the script:** (0 minutes 8.429 seconds)

[`Download Jupyter notebook: multiple_axes.ipynb`](https://matplotlib.org/stable/_downloads/960239d3f64b4258e36a9994f62084da/multiple_axes.ipynb)

[`Download Python source code: multiple_axes.py`](https://matplotlib.org/stable/_downloads/56668c23ff52cd09bd1cdfc0b36b50e1/multiple_axes.py)

[`Download zipped: multiple_axes.zip`](https://matplotlib.org/stable/_downloads/9a3bb9735f3223ac009be3aca4e1ac8e/multiple_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)