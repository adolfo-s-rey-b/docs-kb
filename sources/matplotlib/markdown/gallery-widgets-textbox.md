[Skip to main content](https://matplotlib.org/stable/gallery/widgets/textbox.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/textbox.html#sphx-glr-download-gallery-widgets-textbox-py)
 to download the full example code.

Textbox[#](https://matplotlib.org/stable/gallery/widgets/textbox.html#textbox "Link to this heading")

======================================================================================================

The Textbox widget lets users interactively provide text input, including formulas. In this example, the plot is updated using the [`on_submit`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.on_submit "matplotlib.widgets.TextBox.on_submit")
 method. This method triggers the execution of the _submit_ function when the user presses enter in the textbox or leaves the textbox.

Note: The [`matplotlib.widgets.TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")
 widget is different from the following static elements: [Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)
 and [Placing text boxes](https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html)
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [TextBox](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(bottom\=0.2)

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-2.0, 2.0, 0.001)
[l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), lw\=2)

def submit(expression):
    """
    Update the plotted function to the new math \*expression\*.

    \*expression\* is a string using "t" as its independent variable, e.g.
    "t \*\* 3".
    """
    ydata \= eval(expression, {'np': np}, {'t': [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
})
    [l.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
(ydata)
    [ax.relim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
()
    [ax.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()
    [plt.draw](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw "matplotlib.pyplot.draw")
()

[axbox](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.1, 0.05, 0.8, 0.075))
[text\_box](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")
 \= [TextBox](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")
([axbox](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "Evaluate", textalignment\="center")
[text\_box.on\_submit](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.on_submit "matplotlib.widgets.TextBox.on_submit")
(submit)
[text\_box.set\_val](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox.set_val "matplotlib.widgets.TextBox.set_val")
("t \*\* 2")  \# Trigger \`submit\` with the initial string.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![textbox](https://matplotlib.org/stable/_images/sphx_glr_textbox_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")
    

[`Download Jupyter notebook: textbox.ipynb`](https://matplotlib.org/stable/_downloads/8d2bd91a918af716ba02647dda6668f5/textbox.ipynb)

[`Download Python source code: textbox.py`](https://matplotlib.org/stable/_downloads/9af1076c2fab3dbe816bfbf4cfe1b9f5/textbox.py)

[`Download zipped: textbox.zip`](https://matplotlib.org/stable/_downloads/d135504ae6b8c7d5d30091698936c539/textbox.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)