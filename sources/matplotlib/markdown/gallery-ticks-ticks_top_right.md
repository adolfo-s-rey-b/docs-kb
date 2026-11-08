[Skip to main content](https://matplotlib.org/stable/gallery/ticks/ticks_top_right.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/ticks_top_right.html#sphx-glr-download-gallery-ticks-ticks-top-right-py)
 to download the full example code.

Move x/y-axis ticks and labels on top and right[#](https://matplotlib.org/stable/gallery/ticks/ticks_top_right.html#move-x-y-axis-ticks-and-labels-on-top-and-right "Link to this heading")

============================================================================================================================================================================================

[`axes.Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 can be used to move tick marks and tick labels to the top or right side of the Axes:

[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(top\=True, labeltop\=True, bottom\=False, labelbottom\=False)
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(right\=True, labelright\=True, left\=False, labelleft\=False)

To also reposition the axes labels (xlabel/ylabel), use `Axes.xaxis.set_label_position` and `Axes.yaxis.set_label_position`.

Note

To apply this globally for all future plots, set the rcParams:

*   `[rcParams["xtick.top"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.top#rcparam-xtick-top) ` (default: `False`)
    
*   `[rcParams["xtick.labeltop"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.labeltop#rcparam-xtick-labeltop) ` (default: `False`)
    
*   `[rcParams["xtick.bottom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.bottom#rcparam-xtick-bottom) ` (default: `True`)
    
*   `[rcParams["xtick.labelbottom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.labelbottom#rcparam-xtick-labelbottom) ` (default: `True`)
    
*   `[rcParams["ytick.right"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.right#rcparam-ytick-right) ` (default: `False`)
    
*   `[rcParams["ytick.labelright"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.labelright#rcparam-ytick-labelright) ` (default: `False`)
    
*   `[rcParams["ytick.left"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.left#rcparam-ytick-left) ` (default: `True`)
    
*   `[rcParams["ytick.labelleft"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.labelleft#rcparam-ytick-labelleft) ` (default: `True`)
    

![ticks top right](https://matplotlib.org/stable/_images/sphx_glr_ticks_top_right_001_2_00x.png)

import matplotlib.pyplot as plt

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))

\# Move ticks marks and tick labels
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(
    top\=True, labeltop\=True,
    bottom\=False, labelbottom\=False,
    right\=True, labelright\=True,
    left\=False, labelleft\=False,
)

\# Move axis labels
[ax.xaxis.set\_label\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_label_position.html#matplotlib.axis.XAxis.set_label_position "matplotlib.axis.XAxis.set_label_position")
("top")
[ax.yaxis.set\_label\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_label_position.html#matplotlib.axis.YAxis.set_label_position "matplotlib.axis.YAxis.set_label_position")
("right")

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("X label")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Y label")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: ticks_top_right.ipynb`](https://matplotlib.org/stable/_downloads/7028727c55d3e939096705164bc5589b/ticks_top_right.ipynb)

[`Download Python source code: ticks_top_right.py`](https://matplotlib.org/stable/_downloads/81ffea951390c5158e75624323d7cd8c/ticks_top_right.py)

[`Download zipped: ticks_top_right.zip`](https://matplotlib.org/stable/_downloads/3c9239dc170ae30aec34a3793ab2dd9c/ticks_top_right.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)