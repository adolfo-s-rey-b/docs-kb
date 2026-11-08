[Skip to main content](https://matplotlib.org/stable/gallery/widgets/slider_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/slider_demo.html#sphx-glr-download-gallery-widgets-slider-demo-py)
 to download the full example code.

Slider[#](https://matplotlib.org/stable/gallery/widgets/slider_demo.html#slider "Link to this heading")

========================================================================================================

In this example, sliders are used to control the frequency and amplitude of a sine wave.

See [Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)
 for an example of having the `Slider` snap to discrete values.

See [Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)
 for an example of using a `RangeSlider` to define a range of values.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
, [Slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")

\# The parametrized function to be plotted
def f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, amplitude, frequency):
    return amplitude \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* frequency \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 1000)

\# Define initial parameters
[init\_amplitude](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
[init\_frequency](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 3

\# Create the figure and the line that we will manipulate
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [init\_amplitude](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [init\_frequency](https://docs.python.org/3/library/functions.html#int "builtins.int")
), lw\=2)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Time \[s\]')

\# adjust the main plot to make room for the sliders
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.25, bottom\=0.25)

\# Make a horizontal slider to control the frequency.
[axfreq](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.25, 0.1, 0.65, 0.03))
[freq\_slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 \= [Slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
(
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axfreq](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    label\='Frequency \[Hz\]',
    valmin\=0.1,
    valmax\=30,
    valinit\=[init\_frequency](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
)

\# Make a vertically oriented slider to control the amplitude
[axamp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.1, 0.25, 0.0225, 0.63))
[amp\_slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 \= [Slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
(
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axamp](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
    label\="Amplitude",
    valmin\=0,
    valmax\=10,
    valinit\=[init\_amplitude](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
    orientation\="vertical"
)

\# The function to be called anytime a slider's value changes
def update(val):
    [line.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
(f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [amp\_slider.val](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [freq\_slider.val](https://docs.python.org/3/library/functions.html#int "builtins.int")
))
    [fig.canvas.draw\_idle](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
()

\# register the update function with each slider
[freq\_slider.on\_changed](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.on_changed "matplotlib.widgets.Slider.on_changed")
(update)
[amp\_slider.on\_changed](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider.on_changed "matplotlib.widgets.Slider.on_changed")
(update)

\# Create a \`matplotlib.widgets.Button\` to reset the sliders to initial values.
[resetax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.8, 0.025, 0.1, 0.04))
[button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
 \= [Button](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
([resetax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, 'Reset', hovercolor\='0.975')

def reset(event):
    [freq\_slider.reset](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase.reset "matplotlib.widgets.SliderBase.reset")
()
    [amp\_slider.reset](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase.reset "matplotlib.widgets.SliderBase.reset")
()
[button.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button.on_clicked "matplotlib.widgets.Button.on_clicked")
(reset)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![slider demo](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.Button`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Button.html#matplotlib.widgets.Button "matplotlib.widgets.Button")
    
*   [`matplotlib.widgets.Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
    

[`Download Jupyter notebook: slider_demo.ipynb`](https://matplotlib.org/stable/_downloads/1e6db8af19c1edba2cc57d797c35bc28/slider_demo.ipynb)

[`Download Python source code: slider_demo.py`](https://matplotlib.org/stable/_downloads/34827ebbd80a7be269c66280f4b258ee/slider_demo.py)

[`Download zipped: slider_demo.zip`](https://matplotlib.org/stable/_downloads/d01d8f442cbce4f966f57f5e05421d97/slider_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)