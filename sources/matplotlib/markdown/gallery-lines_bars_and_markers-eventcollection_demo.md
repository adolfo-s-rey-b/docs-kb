[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-eventcollection-demo-py)
 to download the full example code.

EventCollection Demo[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html#eventcollection-demo "Link to this heading")

============================================================================================================================================================

Plot two curves, then use [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
s to mark the locations of the x and y data points on the respective Axes for each curve.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import [EventCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# create random data
[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(\[2, 10\])

\# split the data into two parts
[xdata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :\]
[xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, :\]

\# sort the data so it makes clean curves
[xdata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.sort()
[xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.sort()

\# create some y data points
[ydata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [xdata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\* 2
[ydata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 1 \- [xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\* 3

\# plot the data
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 1, 1)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xdata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ydata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='tab:blue')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ydata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='tab:orange')

\# create the events marking the x data points
[xevents1](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 \= [EventCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
([xdata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='tab:blue', linelength\=0.05)
[xevents2](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 \= [EventCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='tab:orange', linelength\=0.05)

\# create the events marking the y data points
[yevents1](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 \= [EventCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
([ydata1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='tab:blue', linelength\=0.05,
                           orientation\='vertical')
[yevents2](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 \= [EventCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
([ydata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='tab:orange', linelength\=0.05,
                           orientation\='vertical')

\# add the events to the axis
[ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([xevents1](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
)
[ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([xevents2](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
)
[ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([yevents1](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
)
[ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([yevents2](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
)

\# set the limits
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 1)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 1)

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('line plot with data points')

\# display the plot
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![line plot with data points](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_001_2_00x.png)

Tags: [plot-type: eventplot](https://matplotlib.org/stable/_tags/plot-type-eventplot.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: eventcollection_demo.ipynb`](https://matplotlib.org/stable/_downloads/150e433ef8e8b66582a04e38bc02c49c/eventcollection_demo.ipynb)

[`Download Python source code: eventcollection_demo.py`](https://matplotlib.org/stable/_downloads/3dc88c562de73f85d87e1851e2afa1db/eventcollection_demo.py)

[`Download zipped: eventcollection_demo.zip`](https://matplotlib.org/stable/_downloads/2810b27b5cbdc04428e9e1999e527212/eventcollection_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)