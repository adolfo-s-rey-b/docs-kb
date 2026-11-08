[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-titles-demo-py)
 to download the full example code.

Title positioning[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html#title-positioning "Link to this heading")

==================================================================================================================================================

Matplotlib can display plot titles centered, flush with the left side of a set of Axes, and flush with the right side of a set of Axes.

import matplotlib.pyplot as plt

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(range(10))

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Center Title')
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Left Title', loc\='left')
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Right Title', loc\='right')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Left Title, Center Title, Right Title](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_001_2_00x.png)

The vertical position is automatically chosen to avoid decorations (i.e. labels and ticks) on the topmost x-axis:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\='constrained')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))
[ax.xaxis.set\_label\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_label_position.html#matplotlib.axis.XAxis.set_label_position "matplotlib.axis.XAxis.set_label_position")
('top')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X-label')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Center Title')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))
[ax.xaxis.set\_label\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_label_position.html#matplotlib.axis.XAxis.set_label_position "matplotlib.axis.XAxis.set_label_position")
('top')
[ax.xaxis.tick\_top](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.tick_top.html#matplotlib.axis.XAxis.tick_top "matplotlib.axis.XAxis.tick_top")
()
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X-label')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Center Title')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Center Title, Center Title](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_002_2_00x.png)

Automatic positioning can be turned off by manually specifying the _y_ keyword argument for the title or setting `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`) in the rcParams.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\='constrained')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))
[ax.xaxis.set\_label\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_label_position.html#matplotlib.axis.XAxis.set_label_position "matplotlib.axis.XAxis.set_label_position")
('top')
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X-label')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Manual y', y\=1.0, pad\=-14)

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.titley'\] \= 1.0    \# y is in axes-relative coordinates.
[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.titlepad'\] \= \-14  \# pad is in points...
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X-label')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('rcParam y')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Manual y, rcParam y](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_003_2_00x.png)

**Total running time of the script:** (0 minutes 1.596 seconds)

[`Download Jupyter notebook: titles_demo.ipynb`](https://matplotlib.org/stable/_downloads/5b2b339ceb70cb94f3c5fc4e7d486a64/titles_demo.ipynb)

[`Download Python source code: titles_demo.py`](https://matplotlib.org/stable/_downloads/3f6f83882b13d7594b12c5868530ce0f/titles_demo.py)

[`Download zipped: titles_demo.zip`](https://matplotlib.org/stable/_downloads/21cdb8b46bd32b586c10b6815ad355dd/titles_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)