[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/broken_barh.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/broken_barh.html#sphx-glr-download-gallery-lines-bars-and-markers-broken-barh-py)
 to download the full example code.

Broken horizontal bars[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/broken_barh.html#broken-horizontal-bars "Link to this heading")

=======================================================================================================================================================

[`broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
 creates sequences of horizontal bars. This example shows a timing diagram.

import matplotlib.pyplot as plt
import numpy as np

\# data is a sequence of (start, duration) tuples
[cpu\_1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(0, 3), (3.5, 1), (5, 5)\]
[cpu\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 9, 10), [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")\
(10, 0.5)\])
[cpu\_3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[10\*[np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")\
(61), [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")\
(61, 0.05)\])
[cpu\_4](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(2, 1.7), (7, 1.2)\]
[disk](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(1, 1.5)\]
[network](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[10\*[np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")\
(10), [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")\
(10, 0.05)\])

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
\# broken\_barh(xranges, (ypos, height))
[ax.broken\_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
([cpu\_1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, ("CPU 1", 0.4), align\="center")
[ax.broken\_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
([cpu\_2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ("CPU 2", 0.4), align\="center")
[ax.broken\_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
([cpu\_3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ("CPU 3", 0.4), align\="center")
[ax.broken\_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
([cpu\_4](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, ("CPU 4", 0.4), align\="center")
[ax.broken\_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
([disk](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, ("disk", 0.4), align\="center", color\="tab:orange")
[ax.broken\_barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
([network](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ("network", 0.4), align\="center", color\="tab:green")
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 10)
[ax.invert\_yaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
()  \# order the bars from top to bottom
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Resource usage")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Resource usage](https://matplotlib.org/stable/_images/sphx_glr_broken_barh_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
     / [`matplotlib.pyplot.broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.broken_barh.html#matplotlib.pyplot.broken_barh "matplotlib.pyplot.broken_barh")
    
*   [`matplotlib.axes.Axes.invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
    
*   [`matplotlib.axes.Axes.set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
    

Tags: [component: annotation](https://matplotlib.org/stable/_tags/component-annotation.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: broken_barh.ipynb`](https://matplotlib.org/stable/_downloads/78d8b84f45e360f3a04b9d33e9119ad8/broken_barh.ipynb)

[`Download Python source code: broken_barh.py`](https://matplotlib.org/stable/_downloads/2f350cc3d27096728668e15f21c44289/broken_barh.py)

[`Download zipped: broken_barh.zip`](https://matplotlib.org/stable/_downloads/0d1e1e97120a88a68986943eba454a94/broken_barh.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)