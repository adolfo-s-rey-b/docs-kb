[Skip to main content](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html#sphx-glr-download-gallery-widgets-radio-buttons-grid-py)
 to download the full example code.

Radio Buttons Grid[#](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html#radio-buttons-grid "Link to this heading")

=======================================================================================================================================

Using radio buttons in a 2D grid layout.

Radio buttons can be arranged in a 2D grid by passing a `(rows, cols)` tuple to the _layout_ parameter. This is useful when you have multiple related options that are best displayed in a grid format rather than a vertical list.

In this example, we create a color picker using a 2D grid of radio buttons to select the line color of a plot.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [RadioButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")

\# Generate sample data
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax\_buttons](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    1,
    2,
    figsize\=(8, 4),
    width\_ratios\=\[4, 1.4\],
)

\# Create initial plot
([line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,) \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2, color\="red")
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlabel\="Time (s)", ylabel\="Amplitude", title\="Sine Wave - Click a color!")

\# Configure the radio buttons axes
[ax\_buttons.set\_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")
("0.95")
[ax\_buttons.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[:\].set\_color("0.8")
[ax\_buttons.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Line Color")
\# Create a 2D grid of color options (3 rows x 2 columns)
[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["red", "yellow", "green", "purple", "brown", "gray"\]
[radio](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 \= [RadioButtons](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
([ax\_buttons](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, layout\=(3, 2))

def update\_color(label):
    """Update the line color based on selected button."""
    [line.set\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")
(label)
    [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()
[radio.on\_clicked](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets._Buttons.html#matplotlib.widgets._Buttons.on_clicked "matplotlib.widgets._Buttons.on_clicked")
(update\_color)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Sine Wave - Click a color!, Line Color](https://matplotlib.org/stable/_images/sphx_glr_radio_buttons_grid_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
    

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [styling: conditional](https://matplotlib.org/stable/_tags/styling-conditional.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: radio_buttons_grid.ipynb`](https://matplotlib.org/stable/_downloads/99917bd4836b35060dd8ee14b29ae088/radio_buttons_grid.ipynb)

[`Download Python source code: radio_buttons_grid.py`](https://matplotlib.org/stable/_downloads/06a61f45fb8fb20b007b881e9bc2f8b7/radio_buttons_grid.py)

[`Download zipped: radio_buttons_grid.zip`](https://matplotlib.org/stable/_downloads/424f94ac8c38a037c79d00c8ace40d5f/radio_buttons_grid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)