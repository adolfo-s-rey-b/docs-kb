[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html#sphx-glr-download-gallery-axisartist-simple-axisline-py)
 to download the full example code.

Simple Axisline[#](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html#simple-axisline "Link to this heading")

=================================================================================================================================

![simple axisline](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_001_2_00x.png)

import matplotlib.pyplot as plt

from mpl\_toolkits.axisartist.axislines import [AxesZero](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(right\=0.85)
[ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(axes\_class\=[AxesZero](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")
)

\# make right and top axis invisible
[ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].set\_visible(False)
[ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["top"\].set\_visible(False)

\# make xzero axis (horizontal axis line through y=0) visible.
[ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["xzero"\].set\_visible(True)
[ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["xzero"\].label.set\_text("Axis Zero")

[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-2, 4)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("Label X")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Label Y")
\# Or:
\# ax.axis\["bottom"\].label.set\_text("Label X")
\# ax.axis\["left"\].label.set\_text("Label Y")

\# make new (right-side) yaxis, but with some offset
[ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right2"\] \= [ax.new\_fixed\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_fixed_axis "mpl_toolkits.axisartist.Axes.new_fixed_axis")
(loc\="right", offset\=(20, 0))
[ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right2"\].label.set\_text("Label Y2")

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[\-2, 3, 2\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: simple_axisline.ipynb`](https://matplotlib.org/stable/_downloads/0aef4bdb1e5aa7434cc8d86d9e094e37/simple_axisline.ipynb)

[`Download Python source code: simple_axisline.py`](https://matplotlib.org/stable/_downloads/bb682f022912692f490c5c3e20e0b35b/simple_axisline.py)

[`Download zipped: simple_axisline.zip`](https://matplotlib.org/stable/_downloads/966f6ee85170719c0123022ee365c85d/simple_axisline.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)