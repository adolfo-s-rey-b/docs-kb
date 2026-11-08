[Skip to main content](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html#sphx-glr-download-gallery-units-bar-unit-demo-py)
 to download the full example code.

Group barchart with units[#](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html#group-barchart-with-units "Link to this heading")

==============================================================================================================================================

This is the same example as [the barchart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)
 in centimeters.

This example requires [`basic_units.py`](https://matplotlib.org/stable/_downloads/0f0fd288c7d4a6a16f4835b96343f597/basic_units.py)

![Cup height by group and beverage choice](https://matplotlib.org/stable/_images/sphx_glr_bar_unit_demo_001_2_00x.png)

from basic\_units import cm, inch

import matplotlib.pyplot as plt
import numpy as np

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
[tea\_means](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[15\*cm, 10\*cm, 8\*cm, 12\*cm, 5\*cm\]
[tea\_std](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[2\*cm, 1\*cm, 1\*cm, 4\*cm, 2\*cm\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.yaxis.set\_units](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units")
(inch)

[ind](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)    \# the x locations for the groups
[width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.35         \# the width of the bars
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([ind](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [tea\_means](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, bottom\=0\*cm, yerr\=[tea\_std](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\='Tea')

[coffee\_means](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (14\*cm, 19\*cm, 7\*cm, 5\*cm, 10\*cm)
[coffee\_std](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (3\*cm, 5\*cm, 2\*cm, 1\*cm, 2\*cm)
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([ind](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [coffee\_means](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, bottom\=0\*cm, yerr\=[coffee\_std](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
       label\='Coffee')

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Cup height by group and beverage choice')
[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
([ind](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2, labels\=\['G1', 'G2', 'G3', 'G4', 'G5'\])

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: bar_unit_demo.ipynb`](https://matplotlib.org/stable/_downloads/d07d41c9d29de2e2b49c8645d4072882/bar_unit_demo.ipynb)

[`Download Python source code: bar_unit_demo.py`](https://matplotlib.org/stable/_downloads/38d07bdf9a4f5342c0f463c1f5171e58/bar_unit_demo.py)

[`Download zipped: bar_unit_demo.zip`](https://matplotlib.org/stable/_downloads/a6e1c1e8897d6b17c570f170ddcad68e/bar_unit_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)