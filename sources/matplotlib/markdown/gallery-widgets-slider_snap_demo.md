[Skip to main content](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html#sphx-glr-download-gallery-widgets-slider-snap-demo-py)
 to download the full example code.

Snap sliders to discrete values[#](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html#snap-sliders-to-discrete-values "Link to this heading")

===============================================================================================================================================================

You can snap slider values to discrete values using the `valstep` argument.

In this example the Freq slider is constrained to be multiples of pi, and the Amp slider uses an array as the `valstep` argument to more densely sample the first part of its range.

See [Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)
 for an example of using a `Slider` to control a single float.

See [Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)
 for an example of using a `RangeSlider` to define a range of values.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
, [Slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 1.0, 0.001)
[a0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
[f0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 3
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [a0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [f0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(bottom\=0.25)
[l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2)

[ax\_freq](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.25, 0.1, 0.65, 0.03))
[ax\_amp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.25, 0.15, 0.65, 0.03))

\# define the values to use for snapping
[allowed\_amplitudes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(.1, 5, 100), \[6, 7, 8, 9\]\])

\# create the sliders
[samp](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 \= [Slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
(
    [ax\_amp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "Amp", 0.1, 9.0,
    valinit\=[a0](https://docs.python.org/3/library/functions.html#int "builtins.int")
, valstep\=[allowed\_amplitudes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
    color\="green"
)

[sfreq](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 \= [Slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
(
    [ax\_freq](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "Freq", 0, 10\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
    valinit\=2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, valstep\=[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
    initcolor\='none'  \# Remove the line marking the valinit position.
)

def update(val):
    amp \= [samp.val](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
    freq \= [sfreq.val](https://docs.python.org/3/library/functions.html#float "builtins.float")
    [l.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
(amp\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*freq\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
    [fig.canvas.draw\_idle](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
()

[sfreq.on\_changed](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.on_changed "matplotlib.widgets.Slider.on_changed")
(update)
[samp.on\_changed](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.on_changed "matplotlib.widgets.Slider.on_changed")
(update)

[ax\_reset](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.8, 0.025, 0.1, 0.04))
[button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
 \= [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
([ax\_reset](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'Reset', hovercolor\='0.975')

def reset(event):
    [sfreq.reset](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase.reset "matplotlib.widgets.SliderBase.reset")
()
    [samp.reset](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase.reset "matplotlib.widgets.SliderBase.reset")
()
[button.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.on_clicked "matplotlib.widgets.Button.on_clicked")
(reset)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![slider snap demo](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
    
*   [`matplotlib.widgets.Button`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
    

[`Download Jupyter notebook: slider_snap_demo.ipynb`](https://matplotlib.org/stable/_downloads/147390e13df0bd55a92bb4f7beac9c7a/slider_snap_demo.ipynb)

[`Download Python source code: slider_snap_demo.py`](https://matplotlib.org/stable/_downloads/68c95e07ab61a26521daa7870bba11fe/slider_snap_demo.py)

[`Download zipped: slider_snap_demo.zip`](https://matplotlib.org/stable/_downloads/f0e3b72c866b201f8106de81a6cceedd/slider_snap_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)