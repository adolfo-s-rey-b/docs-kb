[Skip to main content](https://matplotlib.org/stable/users/explain/artists/performance.html#main-content)

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
    

Performance[#](https://matplotlib.org/stable/users/explain/artists/performance.html#performance "Link to this heading")

========================================================================================================================

Whether exploring data in interactive mode or programmatically saving lots of plots, rendering performance can be a challenging bottleneck in your pipeline. Matplotlib provides multiple ways to greatly reduce rendering time at the cost of a slight change (to a settable tolerance) in your plot's appearance. The methods available to reduce rendering time depend on the type of plot that is being created.

Line segment simplification[#](https://matplotlib.org/stable/users/explain/artists/performance.html#line-segment-simplification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

For plots that have line segments (e.g. typical line plots, outlines of polygons, etc.), rendering performance can be controlled by `[rcParams["path.simplify"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=path.simplify#rcparam-path-simplify) ` (default: `True`) and `[rcParams["path.simplify_threshold"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=path.simplify_threshold#rcparam-path-simplify-threshold) ` (default: `0.111111111111`), which can be defined e.g. in the `matplotlibrc` file (see [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
 for more information about the `matplotlibrc` file). `[rcParams["path.simplify"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=path.simplify#rcparam-path-simplify) ` (default: `True`) is a Boolean indicating whether or not line segments are simplified at all. `[rcParams["path.simplify_threshold"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=path.simplify_threshold#rcparam-path-simplify-threshold) ` (default: `0.111111111111`) controls how much line segments are simplified; higher thresholds result in quicker rendering.

The following script will first display the data without any simplification, and then display the same data with simplification. Try interacting with both of them:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

\# Setup, and create the data to plot
y \= np.random.rand(100000)
y\[50000:\] \*= 2
y\[np.geomspace(10, 50000, 400).astype(int)\] \= \-1
mpl.rcParams\['path.simplify'\] \= True

mpl.rcParams\['path.simplify\_threshold'\] \= 0.0
plt.plot(y)
plt.show()

mpl.rcParams\['path.simplify\_threshold'\] \= 1.0
plt.plot(y)
plt.show()

Matplotlib currently defaults to a conservative simplification threshold of `1/9`. To change default settings to use a different value, change the `matplotlibrc` file. Alternatively, users can create a new style for interactive plotting (with maximal simplification) and another style for publication quality plotting (with minimal simplification) and activate them as necessary. See [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
 for instructions on how to perform these actions.

The simplification works by iteratively merging line segments into a single vector until the next line segment's perpendicular distance to the vector (measured in display-coordinate space) is greater than the `path.simplify_threshold` parameter.

Note

Changes related to how line segments are simplified were made in version 2.1. Rendering time will still be improved by these parameters prior to 2.1, but rendering time for some kinds of data will be vastly improved in versions 2.1 and greater.

Marker subsampling[#](https://matplotlib.org/stable/users/explain/artists/performance.html#marker-subsampling "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Markers can also be simplified, albeit less robustly than line segments. Marker subsampling is only available to [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 objects (through the `markevery` property). Wherever [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 construction parameters are passed through, such as [`pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
 and [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, the `markevery` parameter can be used:

plt.plot(x, y, markevery\=10)

The `markevery` argument allows for naive subsampling, or an attempt at evenly spaced (along the _x_ axis) sampling. See the [Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)
 for more information.

Splitting lines into smaller chunks[#](https://matplotlib.org/stable/users/explain/artists/performance.html#splitting-lines-into-smaller-chunks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are using the Agg backend (see [What is a backend?](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
), then you can make use of `[rcParams["agg.path.chunksize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=agg.path.chunksize#rcparam-agg-path-chunksize) ` (default: `0`) This allows users to specify a chunk size, and any lines with greater than that many vertices will be split into multiple lines, each of which has no more than `agg.path.chunksize` many vertices. (Unless `agg.path.chunksize` is zero, in which case there is no chunking.) For some kind of data, chunking the line up into reasonable sizes can greatly decrease rendering time.

The following script will first display the data without any chunk size restriction, and then display the same data with a chunk size of 10,000. The difference can best be seen when the figures are large, try maximizing the GUI and then interacting with them:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams\['path.simplify\_threshold'\] \= 1.0

\# Setup, and create the data to plot
y \= np.random.rand(100000)
y\[50000:\] \*= 2
y\[np.geomspace(10, 50000, 400).astype(int)\] \= \-1
mpl.rcParams\['path.simplify'\] \= True

mpl.rcParams\['agg.path.chunksize'\] \= 0
plt.plot(y)
plt.show()

mpl.rcParams\['agg.path.chunksize'\] \= 10000
plt.plot(y)
plt.show()

Legends[#](https://matplotlib.org/stable/users/explain/artists/performance.html#legends "Link to this heading")

----------------------------------------------------------------------------------------------------------------

The default legend behavior for axes attempts to find the location that covers the fewest data points (`loc='best'`). This can be a very expensive computation if there are lots of data points. In this case, you may want to provide a specific location.

Using the _fast_ style[#](https://matplotlib.org/stable/users/explain/artists/performance.html#using-the-fast-style "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The _fast_ style can be used to automatically set simplification and chunking parameters to reasonable settings to speed up plotting large amounts of data. The following code runs it:

import matplotlib.style as mplstyle
mplstyle.use('fast')

It is very lightweight, so it works well with other styles. Be sure the fast style is applied last so that other styles do not overwrite the settings:

mplstyle.use(\['dark\_background', 'ggplot', 'fast'\])

On this page