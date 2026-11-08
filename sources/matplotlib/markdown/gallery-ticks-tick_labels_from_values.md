[Skip to main content](https://matplotlib.org/stable/gallery/ticks/tick_labels_from_values.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/tick_labels_from_values.html#sphx-glr-download-gallery-ticks-tick-labels-from-values-py)
 to download the full example code.

Setting tick labels from a list of values[#](https://matplotlib.org/stable/gallery/ticks/tick_labels_from_values.html#setting-tick-labels-from-a-list-of-values "Link to this heading")

========================================================================================================================================================================================

Using [`Axes.set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
 causes the tick labels to be set on the currently chosen ticks. However, you may want to allow matplotlib to dynamically choose the number of ticks and their spacing.

In this case it may be better to determine the tick label from the value at the tick. The following example shows how to do this.

NB: The [`ticker.MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
 is used here to ensure that the tick values take integer values.

import matplotlib.pyplot as plt

from matplotlib.ticker import [MaxNLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[xs](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
 \= range(26)
[ys](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
 \= range(26)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list('abcdefghijklmnopqrstuvwxyz')

def format\_fn(tick\_val, tick\_pos):
    if int(tick\_val) in [xs](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
:
        return [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[int(tick\_val)\]
    else:
        return ''

\# A FuncFormatter is created automatically.
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(format\_fn)
[ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([MaxNLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
(integer\=True))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xs](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
, [ys](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tick labels from values](https://matplotlib.org/stable/_images/sphx_glr_tick_labels_from_values_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    
*   [`matplotlib.axis.Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
    
*   [`matplotlib.axis.Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
    
*   [`matplotlib.ticker.FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
    
*   [`matplotlib.ticker.MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
    

[`Download Jupyter notebook: tick_labels_from_values.ipynb`](https://matplotlib.org/stable/_downloads/13f68dc6df7acef348e1b1bfbb0768ad/tick_labels_from_values.ipynb)

[`Download Python source code: tick_labels_from_values.py`](https://matplotlib.org/stable/_downloads/2b7917f5efd95d93b11c49f7a421baeb/tick_labels_from_values.py)

[`Download zipped: tick_labels_from_values.zip`](https://matplotlib.org/stable/_downloads/e688e47bf463dac4e313e54e6203fc19/tick_labels_from_values.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)