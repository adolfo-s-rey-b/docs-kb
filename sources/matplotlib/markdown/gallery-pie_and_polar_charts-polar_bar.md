[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_bar.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_bar.html#sphx-glr-download-gallery-pie-and-polar-charts-polar-bar-py)
 to download the full example code.

Bar chart on polar axis[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_bar.html#bar-chart-on-polar-axis "Link to this heading")

=====================================================================================================================================================

Demo of bar plot on a polar axis.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# Compute pie slices
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 20
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, endpoint\=False)
[radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 10 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[width](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 4 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["viridis"\]([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 10.)

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(projection\='polar')
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [width](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[width](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bottom\=0.0, color\=[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.5)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![polar bar](https://matplotlib.org/stable/_images/sphx_glr_polar_bar_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     / [`matplotlib.pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
    
*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    

Tags: [plot-type: pie](https://matplotlib.org/stable/_tags/plot-type-pie.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: polar_bar.ipynb`](https://matplotlib.org/stable/_downloads/c9d805dc2da30933aec9cd00f489e347/polar_bar.ipynb)

[`Download Python source code: polar_bar.py`](https://matplotlib.org/stable/_downloads/0d94160c338d1cb111a4d38e5df5307f/polar_bar.py)

[`Download zipped: polar_bar.zip`](https://matplotlib.org/stable/_downloads/13437c2dd0ae038862bc5eb484b5eaa6/polar_bar.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)