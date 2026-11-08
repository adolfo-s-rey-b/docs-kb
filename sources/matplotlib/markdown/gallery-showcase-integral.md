[Skip to main content](https://matplotlib.org/stable/gallery/showcase/integral.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/showcase/integral.html#sphx-glr-download-gallery-showcase-integral-py)
 to download the full example code.

Integral as the area under a curve[#](https://matplotlib.org/stable/gallery/showcase/integral.html#integral-as-the-area-under-a-curve "Link to this heading")

==============================================================================================================================================================

Although this is a simple example, it demonstrates some important tweaks:

*   A simple line plot with custom color and line width.
    
*   A shaded region created using a Polygon patch.
    
*   A text label with mathtext rendering.
    
*   figtext calls to label the x- and y-axes.
    
*   Use of axis spines to hide the top and right spines.
    
*   Custom tick placement and labels.
    

![integral](https://matplotlib.org/stable/_images/sphx_glr_integral_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")

def func([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    return ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 3) \* ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 5) \* ([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 7) + 85

[a](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2, 9  \# integral limits
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= func([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'r', linewidth\=2)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(bottom\=0)

\# Make the shaded region
[ix](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([a](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[iy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= func([ix](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[verts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[([a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, 0), \*zip([ix](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [iy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
), ([b](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, 0)\]
[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 \= [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
([verts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, facecolor\='0.9', edgecolor\='0.5')
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)

[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5 \* ([a](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + [b](https://docs.python.org/3/library/functions.html#int "builtins.int")
), 30, r"$\\int\_a^b f(x)\\mathrm{d}x$",
        horizontalalignment\='center', fontsize\=20)

[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.9, 0.05, '$x$')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.1, 0.9, '$y$')

[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)
[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[[a](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [b](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], labels\=\['$a$', '$b$'\])
[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: integral.ipynb`](https://matplotlib.org/stable/_downloads/4c049ea5658fcb9dd1cac9c93938f784/integral.ipynb)

[`Download Python source code: integral.py`](https://matplotlib.org/stable/_downloads/392c2c1663693a62d3e8fec9c8b3de15/integral.py)

[`Download zipped: integral.zip`](https://matplotlib.org/stable/_downloads/964095706a313fa6552e1d414c407a5e/integral.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)