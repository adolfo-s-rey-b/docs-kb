[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html#sphx-glr-download-gallery-pie-and-polar-charts-polar-legend-py)
 to download the full example code.

Polar legend[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_legend.html#polar-legend "Link to this heading")

==================================================================================================================================

Using a legend on a polar-axis plot.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\="polar", facecolor\="lightgoldenrodyellow")

[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 3, 301)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="tab:orange", lw\=3, label\="a line")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(0.5 \* [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="tab:blue", ls\="--", lw\=3, label\="another line")
[ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(grid\_color\="palegoldenrod")
\# For polar Axes, it may be useful to move the legend slightly away from the
\# Axes center, to avoid overlap between the legend and the Axes.  The following
\# snippet places the legend's lower left corner just outside the polar Axes
\# at an angle of 67.5 degrees in polar coordinates.
[angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(67.5)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\="lower left",
          bbox\_to\_anchor\=(.5 + [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)/2, .5 + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)/2))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![polar legend](https://matplotlib.org/stable/_images/sphx_glr_polar_legend_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
     / [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
    
*   [`matplotlib.axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
     / [`matplotlib.pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
    
*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    
*   [`matplotlib.projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
    

Tags: [component: legend](https://matplotlib.org/stable/_tags/component-legend.html)
 [plot-type: polar](https://matplotlib.org/stable/_tags/plot-type-polar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: polar_legend.ipynb`](https://matplotlib.org/stable/_downloads/eb09b496b073828e9d736e0ec0b27360/polar_legend.ipynb)

[`Download Python source code: polar_legend.py`](https://matplotlib.org/stable/_downloads/c2271ead33e5ab00cba2a86f335aabb3/polar_legend.py)

[`Download zipped: polar_legend.zip`](https://matplotlib.org/stable/_downloads/f45fd3b8f6b8d3d1fecff9b18e491223/polar_legend.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)