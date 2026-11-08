[Skip to main content](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html#sphx-glr-download-gallery-style-sheets-petroff10-py)
 to download the full example code.

Petroff style sheets[#](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html#petroff-style-sheets "Link to this heading")

=======================================================================================================================================

This example demonstrates the "petroffN" styles, which implement the 6-, 8- and 10-color sequences developed by Matthew A. Petroff [\[1\]](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html#id2)
 for accessible data visualization. The styles balance aesthetics with accessibility considerations, making them suitable for various types of plots while ensuring readability and distinction between data series.

![petroff10](https://matplotlib.org/stable/_images/sphx_glr_petroff10_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

def colored\_lines\_example(ax):
    t \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-10, 10, 100)
    nb\_colors \= len([plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\])
    shifts \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, nb\_colors)
    amplitudes \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(1, 1.5, nb\_colors)
    for t0, a in zip(shifts, amplitudes):
        y \= a / (1 + [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-(t \- t0)))
        line, \= ax.plot(t, y, '-')
        point\_indices \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, len(t) \- 1, 20, dtype\=int)
        ax.plot(t\[point\_indices\], y\[point\_indices\], 'o', color\=line.get\_color())
    ax.set\_xlim(\-10, 10)

def image\_and\_patch\_example(ax):
    ax.imshow([np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(size\=(20, 20)), interpolation\='none')
    c \= [plt.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((5, 5), radius\=5, label\='patch')
    ax.add\_patch(c)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6.4, 9.6), layout\='compressed')
[sfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(nrows\=3)

for [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [sfig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 in zip(\['petroff6', 'petroff8', 'petroff10'\], [sfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [sfig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
(f"'{[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}' style sheet")
    with plt.[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.context([style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
):
        [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [sfig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
(ncols\=2)
        colored\_lines\_example([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
        image\_and\_patch\_example([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.907 seconds)

[`Download Jupyter notebook: petroff10.ipynb`](https://matplotlib.org/stable/_downloads/7579f6571f658ca6f415183c275c1d80/petroff10.ipynb)

[`Download Python source code: petroff10.py`](https://matplotlib.org/stable/_downloads/e2c39e6f3401571735d4016ca6837593/petroff10.py)

[`Download zipped: petroff10.zip`](https://matplotlib.org/stable/_downloads/64ba42d315309c6f41dcd62374245f29/petroff10.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)