[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html#sphx-glr-download-gallery-lines-bars-and-markers-horizontal-barchart-distribution-py)
 to download the full example code.

Discrete distribution as horizontal bar chart[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html#discrete-distribution-as-horizontal-bar-chart "Link to this heading")

==========================================================================================================================================================================================================================

Stacked bar charts can be used to visualize discrete distributions.

This example visualizes the result of a survey in which people could rate their agreement to questions on a five-element scale.

The horizontal stacking is achieved by calling [`barh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 for each category and passing the starting point as the cumulative sum of the already drawn bars via the parameter `left`.

import matplotlib.pyplot as plt
import numpy as np

[category\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['Strongly disagree', 'Disagree',\
                  'Neither agree nor disagree', 'Agree', 'Strongly agree'\]
[results](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'Question 1': \[10, 15, 17, 32, 26\],
    'Question 2': \[26, 22, 29, 10, 13\],
    'Question 3': \[35, 37, 7, 2, 19\],
    'Question 4': \[32, 11, 9, 15, 33\],
    'Question 5': \[21, 29, 5, 5, 40\],
    'Question 6': \[8, 19, 5, 30, 38\]
}

def survey([results](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [category\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of \*category\_names\*.
    category\_names : list of str
        The category labels.
    """
    labels \= list([results](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys())
    data \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(list([results](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values()))
    data\_cum \= data.cumsum(axis\=1)
    category\_colors \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['RdYlGn'\](
        [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.15, 0.85, data.shape\[1\]))

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(9.2, 5))
    ax.invert\_yaxis()
    ax.xaxis.set\_visible(False)
    ax.set\_xlim(0, [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(data, axis\=1).max())

    for i, (colname, color) in enumerate(zip([category\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, category\_colors)):
        widths \= data\[:, i\]
        starts \= data\_cum\[:, i\] \- widths
        rects \= ax.barh(labels, widths, left\=starts, height\=0.5,
                        label\=colname, color\=color)

        r, g, b, \_ \= color
        text\_color \= 'white' if r \* g \* b < 0.5 else 'darkgrey'
        ax.bar\_label(rects, label\_type\='center', color\=text\_color)
    ax.legend(ncols\=len([category\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), bbox\_to\_anchor\=(0, 1),
              loc\='lower left', fontsize\='small')

    return fig, ax

survey([results](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [category\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![horizontal barchart distribution](https://matplotlib.org/stable/_images/sphx_glr_horizontal_barchart_distribution_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
     / [`matplotlib.pyplot.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh "matplotlib.pyplot.barh")
    
*   [`matplotlib.axes.Axes.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
     / [`matplotlib.pyplot.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html#matplotlib.pyplot.bar_label "matplotlib.pyplot.bar_label")
    
*   [`matplotlib.axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
     / [`matplotlib.pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
    

Tags: [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [component: label](https://matplotlib.org/stable/_tags/component-label.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: horizontal_barchart_distribution.ipynb`](https://matplotlib.org/stable/_downloads/157bf147fc929e11134758e75c6f6110/horizontal_barchart_distribution.ipynb)

[`Download Python source code: horizontal_barchart_distribution.py`](https://matplotlib.org/stable/_downloads/77d0d6c2d02582d80df43b9b9e78610c/horizontal_barchart_distribution.py)

[`Download zipped: horizontal_barchart_distribution.zip`](https://matplotlib.org/stable/_downloads/32189259497007d39a62c3495172650b/horizontal_barchart_distribution.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)