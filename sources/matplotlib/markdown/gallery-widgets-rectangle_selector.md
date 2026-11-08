[Skip to main content](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html#sphx-glr-download-gallery-widgets-rectangle-selector-py)
 to download the full example code.

Rectangle and ellipse selectors[#](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html#rectangle-and-ellipse-selectors "Link to this heading")

=================================================================================================================================================================

Click somewhere, move the mouse, and release the mouse button. [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 and [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
 draw a rectangle or an ellipse from the initial click position to the current mouse position (within the same axes) until the button is released. A connected callback receives the click- and release-events.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [EllipseSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
, [RectangleSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")

def select\_callback(eclick, erelease):
    """
    Callback for line selection.

    \*eclick\* and \*erelease\* are the press and release events.
    """
    x1, y1 \= eclick.xdata, eclick.ydata
    x2, y2 \= erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")

def toggle\_selector(event):
    print('Key pressed.')
    if event.key \== 't':
        for selector in [selectors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
            name \= type(selector).\_\_name\_\_
            if selector.active:
                print(f'{name} deactivated.')
                selector.set\_active(False)
            else:
                print(f'{name} activated.')
                selector.set\_active(True)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\='constrained')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(2)

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100000  \# If N is large one can see improvement by using blitting.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[selectors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [selector\_class](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[[RectangleSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")\
, [EllipseSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")\
\]):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))  \# plot something
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f"Click and drag to draw a {[selector\_class](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
.\_\_name\_\_}.")
    [selectors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([selector\_class](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
(
        [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, select\_callback,
        useblit\=True,
        button\=\[1, 3\],  \# disable middle button
        minspanx\=5, minspany\=5,
        spancoords\='pixels',
        interactive\=True))
    [fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('key\_press\_event', toggle\_selector)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title("Press 't' to toggle the selectors on and off.\\n"
                 + [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].get\_title())
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Press 't' to toggle the selectors on and off. Click and drag to draw a RectangleSelector., Click and drag to draw a EllipseSelector.](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
    
*   [`matplotlib.widgets.EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
    

**Total running time of the script:** (0 minutes 1.052 seconds)

[`Download Jupyter notebook: rectangle_selector.ipynb`](https://matplotlib.org/stable/_downloads/53a74678188ab0b3f2aeb2edb30669f1/rectangle_selector.ipynb)

[`Download Python source code: rectangle_selector.py`](https://matplotlib.org/stable/_downloads/6fd8c57479cccb2b7f96c0257b4200d1/rectangle_selector.py)

[`Download zipped: rectangle_selector.zip`](https://matplotlib.org/stable/_downloads/db4932402b162dcd2ed40f9ad55eb876/rectangle_selector.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)