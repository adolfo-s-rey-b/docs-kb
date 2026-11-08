[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html#sphx-glr-download-gallery-pie-and-polar-charts-polar-demo-py)
 to download the full example code.

Polar plot[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html#polar-plot "Link to this heading")

============================================================================================================================

Demo of a line plot on a polar axis.

The second plot shows the same data, but with the radial axis starting at r=1 and the angular axis starting at 0 degrees and ending at 225 degrees. Setting the origin of the radial axis to 0 allows the radial ticks to be placed at the same location as the first plot.

import matplotlib.pyplot as plt
import numpy as np

[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2, 0.01)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(5, 8), subplot\_kw\={'projection': 'polar'},
                        layout\='constrained')
ax \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
ax.set\_rmax(2)
ax.set\_rticks(\[0.5, 1, 1.5, 2\])  \# Fewer radial ticks
ax.set\_rlabel\_position(\-22.5)  \# Move radial labels away from plotted line
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("A line plot on a polar axis", va\='bottom')

ax \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
ax.set\_rmax(2)
ax.set\_rmin(1)  \# Change the radial axis to only go from 1 to 2
ax.set\_rorigin(0)  \# Set the origin of the radial axis to 0
ax.set\_thetamin(0)
ax.set\_thetamax(225)
ax.set\_rticks(\[1, 1.5, 2\])  \# Fewer radial ticks
ax.set\_rlabel\_position(\-22.5)  \# Move radial labels away from plotted line

[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Same plot, but with reduced axis limits", va\='bottom')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![A line plot on a polar axis, Same plot, but with reduced axis limits](https://matplotlib.org/stable/_images/sphx_glr_polar_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
     / [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
    
*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    
*   [`matplotlib.projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
    
*   [`matplotlib.projections.polar.PolarAxes.set_rticks`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rticks "matplotlib.projections.polar.PolarAxes.set_rticks")
    
*   [`matplotlib.projections.polar.PolarAxes.set_rmin`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rmin "matplotlib.projections.polar.PolarAxes.set_rmin")
    
*   [`matplotlib.projections.polar.PolarAxes.set_rorigin`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rorigin "matplotlib.projections.polar.PolarAxes.set_rorigin")
    
*   [`matplotlib.projections.polar.PolarAxes.set_rmax`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rmax "matplotlib.projections.polar.PolarAxes.set_rmax")
    
*   [`matplotlib.projections.polar.PolarAxes.set_rlabel_position`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rlabel_position "matplotlib.projections.polar.PolarAxes.set_rlabel_position")
    

Tags: [plot-type: polar](https://matplotlib.org/stable/_tags/plot-type-polar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.425 seconds)

[`Download Jupyter notebook: polar_demo.ipynb`](https://matplotlib.org/stable/_downloads/779e848506cf7b3883ee44dd8065793e/polar_demo.ipynb)

[`Download Python source code: polar_demo.py`](https://matplotlib.org/stable/_downloads/71f6f1571f197ea4d33c60225bfb2213/polar_demo.py)

[`Download zipped: polar_demo.zip`](https://matplotlib.org/stable/_downloads/072917bc771e7922dab81ccc839f4721/polar_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)