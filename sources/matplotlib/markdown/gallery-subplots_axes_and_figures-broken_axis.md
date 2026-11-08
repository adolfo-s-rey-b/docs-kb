[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html#sphx-glr-download-gallery-subplots-axes-and-figures-broken-axis-py)
 to download the full example code.

Broken axis[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html#broken-axis "Link to this heading")

====================================================================================================================================

Broken axis example, where the y-axis will have a portion cut out.

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[pts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(30)\*.2
\# Now let's make two outlier points which are far away from everything.
[pts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\[3, 14\]\] += .8

\# If we were to simply plot pts, we'd lose most of the interesting
\# details due to the outliers. So let's 'break' or 'cut-out' the y-axis
\# into two portions - use the top (ax1) for the outliers, and the bottom
\# (ax2) for the details of the majority of our data
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, sharex\=True)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(hspace\=0.05)  \# adjust space between Axes

\# plot the same data on both Axes
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([pts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([pts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# zoom-in / limit the view to different portions of the data
[ax1.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(.78, 1.)  \# outliers only
[ax2.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, .22)  \# most of the data

\# hide the spines between ax and ax2
[ax1.spines.bottom.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
[ax2.spines.top.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)
[ax1.xaxis.tick\_top](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_top.html#matplotlib.axis.XAxis.tick_top "matplotlib.axis.XAxis.tick_top")
()
[ax1.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labeltop\=False)  \# don't put tick labels at the top
[ax2.xaxis.tick\_bottom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_bottom.html#matplotlib.axis.XAxis.tick_bottom "matplotlib.axis.XAxis.tick_bottom")
()

\# Now, let's turn towards the cut-out slanted lines.
\# We create line objects in axes coordinates, in which (0,0), (0,1),
\# (1,0), and (1,1) are the four corners of the Axes.
\# The slanted lines themselves are markers at those locations, such that the
\# lines keep their angle and position, independent of the Axes size or scale
\# Finally, we need to disable clipping.

[d](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= .5  \# proportion of vertical to horizontal extent of the slanted line
[kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(marker\=\[(\-1, \-[d](https://docs.python.org/3/library/functions.html#float "builtins.float")\
), (1, [d](https://docs.python.org/3/library/functions.html#float "builtins.float")\
)\], markersize\=12,
              linestyle\="none", color\='k', mec\='k', mew\=1, clip\_on\=False)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1\], \[0, 0\], transform\=[ax1.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, \*\*[kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1\], \[1, 1\], transform\=[ax2.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, \*\*[kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![broken axis](https://matplotlib.org/stable/_images/sphx_glr_broken_axis_001_2_00x.png)

Tags: [component: axis](https://matplotlib.org/stable/_tags/component-axis.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: broken_axis.ipynb`](https://matplotlib.org/stable/_downloads/31d312b3fca8102ce334ea92d3b3c448/broken_axis.ipynb)

[`Download Python source code: broken_axis.py`](https://matplotlib.org/stable/_downloads/5c94489dd50eebf5ed1e62b297d004ec/broken_axis.py)

[`Download zipped: broken_axis.zip`](https://matplotlib.org/stable/_downloads/41fcc8a6024ff2bd451ee4b5c826d77c/broken_axis.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)