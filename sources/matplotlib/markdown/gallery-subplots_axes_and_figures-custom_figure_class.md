[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/custom_figure_class.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/custom_figure_class.html#sphx-glr-download-gallery-subplots-axes-and-figures-custom-figure-class-py)
 to download the full example code.

Custom Figure subclasses[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/custom_figure_class.html#custom-figure-subclasses "Link to this heading")

======================================================================================================================================================================

You can pass a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 subclass to [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 if you want to change the default behavior of the figure.

This example defines a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 subclass `WatermarkFigure` that accepts an additional parameter `watermark` to display a custom watermark text. The figure is created using the `FigureClass` parameter of [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
. The additional `watermark` parameter is passed on to the subclass constructor.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

class WatermarkFigure([Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """A figure with a text watermark."""

    def \_\_init\_\_(self, \*args, watermark\=None, \*\*kwargs):
        super().\_\_init\_\_(\*args, \*\*kwargs)

        if watermark is not None:
            bbox \= dict(boxstyle\='square', lw\=3, ec\='gray',
                        fc\=(0.9, 0.9, .9, .5), alpha\=0.5)
            self.text(0.5, 0.5, watermark,
                      ha\='center', va\='center', rotation\=30,
                      fontsize\=40, color\='gray', alpha\=0.5, bbox\=bbox)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 201)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.tanh](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + 0.1 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(5 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(FigureClass\=[WatermarkFigure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, watermark\='draft')
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![custom figure class](https://matplotlib.org/stable/_images/sphx_glr_custom_figure_class_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
    
*   [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
    
*   [`matplotlib.figure.Figure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
    

Tags: [component: figure](https://matplotlib.org/stable/_tags/component-figure.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: custom_figure_class.ipynb`](https://matplotlib.org/stable/_downloads/5ad4cd4affa59bdbc02196aedf4b9e4b/custom_figure_class.ipynb)

[`Download Python source code: custom_figure_class.py`](https://matplotlib.org/stable/_downloads/c959932316ffd40d04ead8bdf210461d/custom_figure_class.py)

[`Download zipped: custom_figure_class.zip`](https://matplotlib.org/stable/_downloads/17027d13900028cfd5995dd107ea0b2d/custom_figure_class.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)