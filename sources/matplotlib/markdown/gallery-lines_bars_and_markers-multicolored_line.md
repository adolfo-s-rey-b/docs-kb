[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#sphx-glr-download-gallery-lines-bars-and-markers-multicolored-line-py)
 to download the full example code.

Multicolored lines[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#multicolored-lines "Link to this heading")

=====================================================================================================================================================

The example shows two ways to plot a line with the a varying color defined by a third value. The first example defines the color at each (x, y) point. The second example defines the color between pairs of points, so the length of the color value list is one less than the length of the x and y lists.

Color values at points[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#color-values-at-points "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

import warnings

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

def colored\_line([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=None, \*\*lc\_kwargs):
    """
    Plot a line with a color specified along the line by a third value.

    It does this by creating a collection of line segments. Each line segment is
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should be the same size as x and y.
    ax : matplotlib.axes.Axes, optional
        The axes to plot on. If not provided, the current axes will be used.
    \*\*lc\_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
    """
    if "array" in lc\_kwargs:
        [warnings.warn](https://docs.python.org/3/library/warnings.html#warnings.warn "warnings.warn")
(
            'The provided "array" keyword argument will be overridden',
            UserWarning,
            stacklevel\=2,
        )

    xy \= [np.stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
(([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), axis\=-1)
    xy\_mid \= [np.concat](https://numpy.org/doc/stable/reference/generated/numpy.concat.html#numpy.concat "numpy.concat")
(
        (xy\[0, :\]\[None, :\], (xy\[:\-1, :\] + xy\[1:, :\]) / 2, xy\[\-1, :\]\[None, :\]), axis\=0
    )
    segments \= [np.stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
((xy\_mid\[:\-1, :\], xy, xy\_mid\[1:, :\]), axis\=-2)
    \# Note that
    \# segments\[0, :, :\] is \[xy\[0, :\], xy\[0, :\], (xy\[0, :\] + xy\[1, :\]) / 2\]
    \# segments\[i, :, :\] is \[(xy\[i - 1, :\] + xy\[i, :\]) / 2, xy\[i, :\],\
    \#     (xy\[i, :\] + xy\[i + 1, :\]) / 2\] if i not in {0, len(x) - 1}
    \# segments\[-1, :, :\] is \[(xy\[-2, :\] + xy\[-1, :\]) / 2, xy\[-1, :\], xy\[-1, :\]\]

    lc\_kwargs\["array"\] \= [c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
    lc \= [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(segments, \*\*lc\_kwargs)

    \# Plot the line collection to the axes
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
    [ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
(lc)

    return lc

\# -------------- Create and show plot --------------
\# Some arbitrary function that gives x, y, and color values
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-7.4, \-0.5, 200)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.9 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.9 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1.6 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[color](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2, [t.size](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Create a figure and plot the line on it
[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[lines](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= colored\_line([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [color](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, linewidth\=10, cmap\="plasma")
[fig1.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([lines](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
)  \# add a color legend

[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Color at each point")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Color at each point](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_001_2_00x.png)

This method is designed to give a smooth impression when distances and color differences between adjacent points are not too large. The following example does not meet this criteria and by that serves to illustrate the segmentation and coloring mechanism.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[0, 1, 2, 3, 4\]
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[0, 1, 2, 1, 1\]
[c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 2, 3, 4, 5\]
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, cmap\='rainbow')
colored\_line([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, cmap\='rainbow')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![multicolored line](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_002_2_00x.png)

Color values between points[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#color-values-between-points "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def colored\_line\_between\_pts([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, \*\*lc\_kwargs):
    """
    Plot a line with a color specified between (x, y) points by a third value.

    It does this by creating a collection of line segments between each pair of
    neighboring points. The color of each segment is determined by the
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should have a size one less than that of x and y.
    ax : Axes
        Axis object on which to plot the colored line.
    \*\*lc\_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
    """
    if "array" in lc\_kwargs:
        [warnings.warn](https://docs.python.org/3/library/warnings.html#warnings.warn "warnings.warn")
('The provided "array" keyword argument will be overridden')

    \# Check color array size (LineCollection still works, but values are unused)
    if len([c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) != len([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \- 1:
        [warnings.warn](https://docs.python.org/3/library/warnings.html#warnings.warn "warnings.warn")
(
            "The c argument should have a length one less than the length of x and y. "
            "If it has the same length, use the colored\_line function instead."
        )

    \# Create a set of line segments so that we can color them individually
    \# This creates the points as an N x 1 x 2 array so that we can stack points
    \# together easily to get the segments. The segments array for line collection
    \# needs to be (numlines) x (points per line) x 2 (for x and y)
    points \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]).T.reshape(\-1, 1, 2)
    segments \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[points\[:\-1\], points\[1:\]\], axis\=1)
    lc \= [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(segments, \*\*lc\_kwargs)

    \# Set the values used for colormapping
    lc.set\_array([c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

    return [ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
(lc)

\# -------------- Create and show plot --------------
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 3 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 500)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[dydx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(0.5 \* ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\] + [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:\]))  \# first derivative

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[line](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= colored\_line\_between\_pts([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [dydx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, linewidth\=2, cmap\="viridis")
[fig2.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([line](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, label\="dy/dx")

[ax2.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max())
[ax2.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1.1, 1.1)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Color between points")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Color between points](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_003_2_00x.png)

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [styling: linestyle](https://matplotlib.org/stable/_tags/styling-linestyle.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 1.897 seconds)

[`Download Jupyter notebook: multicolored_line.ipynb`](https://matplotlib.org/stable/_downloads/45d5685f3e8405991417776a213850fc/multicolored_line.ipynb)

[`Download Python source code: multicolored_line.py`](https://matplotlib.org/stable/_downloads/dde8bce4a3266a4b3702098ddc49f236/multicolored_line.py)

[`Download zipped: multicolored_line.zip`](https://matplotlib.org/stable/_downloads/a6d1c231fbd6dd5192b9066570caf3b2/multicolored_line.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page