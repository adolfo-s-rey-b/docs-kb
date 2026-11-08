[Skip to main content](https://matplotlib.org/stable/gallery/widgets/range_slider.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/range_slider.html#sphx-glr-download-gallery-widgets-range-slider-py)
 to download the full example code.

Image scaling using a RangeSlider[#](https://matplotlib.org/stable/gallery/widgets/range_slider.html#image-scaling-using-a-rangeslider "Link to this heading")

===============================================================================================================================================================

Using the RangeSlider widget to control the thresholding of an image.

The RangeSlider widget can be used similarly to the [`widgets.Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 widget. The major difference is that RangeSlider's `val` attribute is a tuple of floats `(lower val, upper val)` rather than a single float.

See [Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)
 for an example of using a `Slider` to control a single float.

See [Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)
 for an example of having the `Slider` snap to discrete values.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import [RangeSlider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")

\# generate a fake image
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 128
[img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(10, 5))
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(bottom\=0.25)

[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].hist([img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.flatten(), bins\='auto')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('Histogram of pixel intensities')

\# Create the RangeSlider
[slider\_ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.20, 0.1, 0.60, 0.03))
[slider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")
 \= [RangeSlider](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")
([slider\_ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "Threshold", [img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min(), [img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max())

\# Create the Vertical lines on the histogram
[lower\_limit\_line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].axvline([slider.val](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], color\='k')
[upper\_limit\_line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].axvline([slider.val](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\], color\='k')

def update(val):
    \# The val passed to a callback by the RangeSlider will
    \# be a tuple of (min, max)

    \# Update the image's colormap
    [im.norm.vmin](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.norm "matplotlib.colorizer._ColorizerInterface.norm")
 \= val\[0\]
    [im.norm.vmax](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.norm "matplotlib.colorizer._ColorizerInterface.norm")
 \= val\[1\]

    \# Update the position of the vertical lines
    [lower\_limit\_line.set\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")
(\[val\[0\], val\[0\]\])
    [upper\_limit\_line.set\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")
(\[val\[1\], val\[1\]\])

    \# Redraw the figure to ensure it updates
    [fig.canvas.draw\_idle](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
()

[slider.on\_changed](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider.on_changed "matplotlib.widgets.RangeSlider.on_changed")
(update)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Histogram of pixel intensities](https://matplotlib.org/stable/_images/sphx_glr_range_slider_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.RangeSlider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")
    

**Total running time of the script:** (0 minutes 1.126 seconds)

[`Download Jupyter notebook: range_slider.ipynb`](https://matplotlib.org/stable/_downloads/b27df189079bff395fb2f320c928d3e1/range_slider.ipynb)

[`Download Python source code: range_slider.py`](https://matplotlib.org/stable/_downloads/5d09fa7f28b450731d677f4d2e54e675/range_slider.py)

[`Download zipped: range_slider.zip`](https://matplotlib.org/stable/_downloads/4d27ca59af4f848ec66f65039c934836/range_slider.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)