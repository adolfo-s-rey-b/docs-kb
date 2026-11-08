[Skip to main content](https://matplotlib.org/stable/gallery/widgets/check_buttons.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/check_buttons.html#sphx-glr-download-gallery-widgets-check-buttons-py)
 to download the full example code.

Check buttons[#](https://matplotlib.org/stable/gallery/widgets/check_buttons.html#check-buttons "Link to this heading")

========================================================================================================================

Turning visual elements on and off with check buttons.

This program shows the use of [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
 which is similar to check boxes. There are 3 different sine waves shown, and we can choose which waves are displayed with the check buttons.

Check buttons may be styled using the _check\_props_, _frame\_props_, and _label\_props_ parameters. The parameters each take a dictionary with keys of artist property names and values of lists of settings with length matching the number of buttons.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [CheckButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2.0, 0.01)
[s0](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[s1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[s2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(6\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[l0](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s0](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, visible\=False, lw\=2, color\='black', label\='1 Hz')
[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2, color\='red', label\='2 Hz')
[l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2, color\='blue', label\='3 Hz')

[lines\_by\_label](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {l.get\_label(): l for l in \[[l0](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\]}
[line\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[l.get\_color() for l in [lines\_by\_label](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")\
.values()\]

\# Make checkbuttons with all plotted lines with correct visibility
[rax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax.inset\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
(\[0.0, 0.0, 0.12, 0.2\])
[check](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
 \= [CheckButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
(
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[rax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    labels\=[lines\_by\_label](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys(),
    actives\=\[l.get\_visible() for l in [lines\_by\_label](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")\
.values()\],
    label\_props\={'color': [line\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
},
    frame\_props\={'edgecolor': [line\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
},
    check\_props\={'facecolor': [line\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
},
)

def callback(label):
    ln \= [lines\_by\_label](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[label\]
    ln.set\_visible(not ln.get\_visible())
    ln.figure.canvas.draw\_idle()

[check.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
(callback)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![check buttons](https://matplotlib.org/stable/_images/sphx_glr_check_buttons_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
    

[`Download Jupyter notebook: check_buttons.ipynb`](https://matplotlib.org/stable/_downloads/a6e1d0880cb91e957d5659661029eb9d/check_buttons.ipynb)

[`Download Python source code: check_buttons.py`](https://matplotlib.org/stable/_downloads/c08881ff905bac0ced64da581a650859/check_buttons.py)

[`Download zipped: check_buttons.zip`](https://matplotlib.org/stable/_downloads/1495092d87383b1209d63712d7b97fc3/check_buttons.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)