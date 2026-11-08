[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html#sphx-glr-download-gallery-subplots-axes-and-figures-align-labels-demo-py)
 to download the full example code.

Align labels and titles[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html#align-labels-and-titles "Link to this heading")

==================================================================================================================================================================

Aligning xlabel, ylabel, and title using [`Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")
, [`Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")
, and [`Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")
.

[`Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")
 wraps the x and y label functions.

We align the xlabels and ylabels using short calls to [`Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")
 and [`Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")
. We also show a manual way to align the ylabels using the [`set_label_coords`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords")
 method of the yaxis object. Note this requires knowing a good offset value which is hardcoded.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3, figsize\=(8.9, 5.5),
                        layout\='constrained', gridspec\_kw\={'wspace': 0.1})

\# add sample data and labels
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [scale](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2000 if [ax.get\_subplotspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_subplotspec.html#matplotlib.axes.Axes.get_subplotspec "matplotlib.axes.Axes.get_subplotspec")
().is\_first\_row() else 1
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([scale](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* (1 \- [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, 100))))
    if [ax.get\_subplotspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_subplotspec.html#matplotlib.axes.Axes.get_subplotspec "matplotlib.axes.Axes.get_subplotspec")
().is\_last\_row():
        [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('xlabel', bbox\=dict(facecolor\='yellow', pad\=5, alpha\=0.2))
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('ylabel', bbox\=dict(facecolor\='yellow', pad\=5, alpha\=0.2))
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, [scale](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Modify ticks to get different margins in some plots
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].xaxis.tick\_top()
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].tick\_params(axis\='x', rotation\=55)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('ylabels not aligned')

\# Align labels
[fig.align\_titles](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")
()            \# Align titles
[fig.align\_xlabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")
()           \# Align all x-axis labels
[fig.align\_ylabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")
([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\])  \# Align only the second column's y-labels
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title('fig.align\_ylabels()')

\# Manually adjust y-labels for the third column
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 2\]:
    [ax.yaxis.set\_label\_coords](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords")
(\-0.3, 0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title('ylabels manually aligned')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ylabels not aligned, fig.align_ylabels(), ylabels manually aligned](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")
    
*   [`matplotlib.figure.Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")
    
*   [`matplotlib.figure.Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")
    
*   [`matplotlib.figure.Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")
    
*   [`matplotlib.axis.Axis.set_label_coords`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords")
    
*   [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
     / [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
    
*   [`matplotlib.axes.Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
    
*   [`matplotlib.axes.Axes.set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
    
*   [`matplotlib.axes.Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
    

Tags: [component: label](https://matplotlib.org/stable/_tags/component-label.html)
 [component: title](https://matplotlib.org/stable/_tags/component-title.html)
 [styling: position](https://matplotlib.org/stable/_tags/styling-position.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 2.428 seconds)

[`Download Jupyter notebook: align_labels_demo.ipynb`](https://matplotlib.org/stable/_downloads/d47f0a12e13c29ce360f348eed4d373c/align_labels_demo.ipynb)

[`Download Python source code: align_labels_demo.py`](https://matplotlib.org/stable/_downloads/05fd218296847a32c17ab9a2fea8bbd7/align_labels_demo.py)

[`Download zipped: align_labels_demo.zip`](https://matplotlib.org/stable/_downloads/2a85db5795c032518d3f797a708cc610/align_labels_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)