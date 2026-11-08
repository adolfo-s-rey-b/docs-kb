[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html#sphx-glr-download-gallery-lines-bars-and-markers-hat-graph-py)
 to download the full example code.

Hat graph[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/hat_graph.html#hat-graph "Link to this heading")

===========================================================================================================================

This example shows how to create a [hat graph](https://doi.org/10.1186/s41235-019-0182-3)
 and how to annotate it with labels.

import matplotlib.pyplot as plt
import numpy as np

def hat\_graph([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [xlabels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, values, group\_labels):
    """
    Create a hat graph.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes to plot into.
    xlabels : list of str
        The category names to be displayed on the x-axis.
    values : (M, N) array-like
        The data values.
        Rows are the groups (len(group\_labels) == M).
        Columns are the categories (len(xlabels) == N).
    group\_labels : list of str
        The group labels displayed in the legend.
    """

    values \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(values)
    color\_cycle\_colors \= [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\].by\_key()\['color'\]

    \# Draw the hats
    bars \= [ax.grouped\_bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
(
        (values \- values\[0\]).T, bottom\=values\[0\], tick\_labels\=[xlabels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
        labels\=group\_labels, edgecolor\='black', group\_spacing\=0.8,
        colors\=\['none'\] + color\_cycle\_colors)

    \# Attach a text label on top of each bar
    for bc, heights in zip(bars.bar\_containers, values):
        [ax.bar\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
(bc, heights, padding\=4)

\# Initialise labels and a numpy array make sure you have
\# N labels of N number of values in the array
[xlabels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['I', 'II', 'III', 'IV', 'V'\]
[playerA](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[5, 15, 22, 20, 25\])
[playerB](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[25, 32, 34, 30, 27\])

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')

hat\_graph([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [xlabels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, \[[playerA](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [playerB](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\], \['Player A', 'Player B'\])

\# Add some text for labels, title and custom x-axis tick labels, etc.
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Games')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Score')
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 60)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Scores by number of game and players')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Scores by number of game and players](https://matplotlib.org/stable/_images/sphx_glr_hat_graph_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
     / [`matplotlib.pyplot.grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#matplotlib.pyplot.grouped_bar "matplotlib.pyplot.grouped_bar")
    
*   [`matplotlib.axes.Axes.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
     / [`matplotlib.pyplot.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html#matplotlib.pyplot.bar_label "matplotlib.pyplot.bar_label")
    

Tags: [component: annotation](https://matplotlib.org/stable/_tags/component-annotation.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: hat_graph.ipynb`](https://matplotlib.org/stable/_downloads/ccd61beeedafcda3efc12672963d956e/hat_graph.ipynb)

[`Download Python source code: hat_graph.py`](https://matplotlib.org/stable/_downloads/ff9b887ec7665e75d3992d3af408be52/hat_graph.py)

[`Download zipped: hat_graph.zip`](https://matplotlib.org/stable/_downloads/5709e6945b593be88bf9ea614f7b06f7/hat_graph.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)