[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-download-gallery-lines-bars-and-markers-barchart-py)
 to download the full example code.

Grouped bar chart with labels[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#grouped-bar-chart-with-labels "Link to this heading")

==================================================================================================================================================================

This example shows a how to create a grouped bar chart and how to annotate bars with labels.

\# data from https://allisonhorst.github.io/palmerpenguins/

import matplotlib.pyplot as plt

[species](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ("Adelie", "Chinstrap", "Gentoo")
[penguin\_means](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')

res \= [ax.grouped\_bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
([penguin\_means](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, tick\_labels\=[species](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, group\_spacing\=1)
for [container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 in [res.bar\_containers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [ax.bar\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
([container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
, padding\=3)

\# Add some text for labels, title, etc.
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Length (mm)')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Penguin attributes by species')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\='upper left', ncols\=3)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 250)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Penguin attributes by species](https://matplotlib.org/stable/_images/sphx_glr_barchart_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     / [`matplotlib.pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
    
*   [`matplotlib.axes.Axes.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
     / [`matplotlib.pyplot.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html#matplotlib.pyplot.bar_label "matplotlib.pyplot.bar_label")
    

Tags: [component: label](https://matplotlib.org/stable/_tags/component-label.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: barchart.ipynb`](https://matplotlib.org/stable/_downloads/84f8193e80e39b9696e1bb5bd6522192/barchart.ipynb)

[`Download Python source code: barchart.py`](https://matplotlib.org/stable/_downloads/9079c7956239a0c7507bbae7d553ce77/barchart.py)

[`Download zipped: barchart.zip`](https://matplotlib.org/stable/_downloads/47cf3594d65a6e855dec277235119005/barchart.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)