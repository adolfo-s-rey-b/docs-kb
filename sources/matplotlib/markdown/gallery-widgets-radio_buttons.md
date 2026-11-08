[Skip to main content](https://matplotlib.org/stable/gallery/widgets/radio_buttons.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/radio_buttons.html#sphx-glr-download-gallery-widgets-radio-buttons-py)
 to download the full example code.

Radio Buttons[#](https://matplotlib.org/stable/gallery/widgets/radio_buttons.html#radio-buttons "Link to this heading")

========================================================================================================================

Using radio buttons to choose properties of your plot.

Radio buttons let you choose between multiple options in a visualization. In this case, the buttons let the user choose one of the three different sine waves to be shown in the plot.

Radio buttons may be styled using the _label\_props_ and _radio\_props_ parameters, which each take a dictionary with keys of artist property names and values of lists of settings with length matching the number of buttons.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [RadioButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")

[FREQUENCIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'1 Hz': 1, '2 Hz': 2, '4 Hz': 4}

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2.0, 0.01)

def f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, freq):
    return [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* freq \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(
    \[\
        \['main', 'freq'\],\
        \['main', 'color'\],\
        \['main', 'linestyle'\],\
    \],
    width\_ratios\=\[5, 1\],
    layout\='constrained',
)
([line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,) \= [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['main'\].plot([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, freq\=1), lw\=2, color\='red')
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['main'\].set(xlabel\="Time (s)", ylabel\="Amplitude", title\="Sine Wave")

[background\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '0.95'
[edge\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '0.8'

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['freq'\].set\_facecolor([background\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['freq'\].spines\[:\].set\_color([edge\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['freq'\].set\_title('Frequency')
[radio](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 \= [RadioButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['freq'\], labels\=list([FREQUENCIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys()),
                     label\_props\={'fontsize': \[12, 14, 16\]},
                     radio\_props\={'s': \[16, 32, 64\]})

def update\_frequency(label):
    ydata \= f([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, freq\=[FREQUENCIES](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[label\])
    [line.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
(ydata)
    [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()
[radio.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
(update\_frequency)

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['color'\].set\_facecolor([background\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['color'\].spines\[:\].set\_color([edge\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['color'\].set\_title('Color')
[radio2](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 \= [RadioButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
(
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['color'\], ('red', 'blue', 'green'),
    label\_props\={'color': \['red', 'blue', 'green'\]},
    radio\_props\={
        'facecolor': \['red', 'blue', 'green'\],
        'edgecolor': \['darkred', 'darkblue', 'darkgreen'\],
    })

def update\_color(label):
    [line.set\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")
(label)
    [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()
[radio2.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
(update\_color)

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['linestyle'\].set\_facecolor([background\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['linestyle'\].spines\[:\].set\_color([edge\_color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['linestyle'\].set\_title('Linestyle')
[radio3](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 \= [RadioButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['linestyle'\], ('solid', 'dashed', 'dashdot', 'dotted'))

def update\_linestyle(label):
    [line.set\_linestyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")
(label)
    [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()
[radio3.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
(update\_linestyle)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Sine Wave, Frequency, Color, Linestyle](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
    

**Total running time of the script:** (0 minutes 1.136 seconds)

[`Download Jupyter notebook: radio_buttons.ipynb`](https://matplotlib.org/stable/_downloads/11d081f31656d51c7272fc59dc20498e/radio_buttons.ipynb)

[`Download Python source code: radio_buttons.py`](https://matplotlib.org/stable/_downloads/51785ae53b1786fb0ed5b01f90362232/radio_buttons.py)

[`Download zipped: radio_buttons.zip`](https://matplotlib.org/stable/_downloads/1fbe75f27a0bb8cd3d09174d529eb7a3/radio_buttons.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)