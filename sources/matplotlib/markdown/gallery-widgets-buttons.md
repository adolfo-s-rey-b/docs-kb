[Skip to main content](https://matplotlib.org/stable/gallery/widgets/buttons.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/buttons.html#sphx-glr-download-gallery-widgets-buttons-py)
 to download the full example code.

Buttons[#](https://matplotlib.org/stable/gallery/widgets/buttons.html#buttons "Link to this heading")

======================================================================================================

Constructing a simple button GUI to modify a sine wave.

The `next` and `previous` button widget helps visualize the wave with new frequencies.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")

[freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(2, 20, 3)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(bottom\=0.2)
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 1.0, 0.001)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2)

class Index:
    ind \= 0

    def next(self, event):
        self.ind += 1
        i \= self.ind % len([freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
        ydata \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[i\]\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
        [l.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
(ydata)
        [plt.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw "matplotlib.pyplot.draw")
()

    def prev(self, event):
        self.ind \-= 1
        i \= self.ind % len([freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
        ydata \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[i\]\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
        [l.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
(ydata)
        [plt.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw "matplotlib.pyplot.draw")
()

callback \= Index()
[axprev](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.7, 0.05, 0.1, 0.075))
[axnext](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.81, 0.05, 0.1, 0.075))
[bnext](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
 \= [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
([axnext](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'Next')
[bnext.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.on_clicked "matplotlib.widgets.Button.on_clicked")
(callback.next)
[bprev](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
 \= [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
([axprev](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'Previous')
[bprev.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.on_clicked "matplotlib.widgets.Button.on_clicked")
(callback.prev)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![buttons](https://matplotlib.org/stable/_images/sphx_glr_buttons_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.Button`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
    

[`Download Jupyter notebook: buttons.ipynb`](https://matplotlib.org/stable/_downloads/58a1433a8b9b492045a15224c16f35ee/buttons.ipynb)

[`Download Python source code: buttons.py`](https://matplotlib.org/stable/_downloads/1396177ce1d23fee4cbc40e2635021b2/buttons.py)

[`Download zipped: buttons.zip`](https://matplotlib.org/stable/_downloads/eae94f16e63d2f3f633a51325520ac02/buttons.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)