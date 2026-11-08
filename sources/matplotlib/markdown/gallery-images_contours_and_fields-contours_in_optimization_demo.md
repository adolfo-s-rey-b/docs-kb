[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html#sphx-glr-download-gallery-images-contours-and-fields-contours-in-optimization-demo-py)
 to download the full example code.

Contouring the solution space of optimizations[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html#contouring-the-solution-space-of-optimizations "Link to this heading")

=============================================================================================================================================================================================================================

Contour plotting is particularly handy when illustrating the solution space of optimization problems. Not only can [`axes.Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 be used to represent the topography of the objective function, it can be used to generate boundary curves of the constraint functions. The constraint lines can be drawn with [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")
 to distinguish the valid and invalid sides of the constraint boundaries.

[`axes.Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 generates curves with larger values to the left of the contour. The angle parameter is measured zero ahead with increasing values to the left. Consequently, when using [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")
 to illustrate a constraint in a typical optimization problem, the angle should be set between zero and 180 degrees.

![contours in optimization demo](https://matplotlib.org/stable/_images/sphx_glr_contours_in_optimization_demo_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))

[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 101
[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 105

\# Set up survey vectors
[xvec](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.001, 4.0, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[yvec](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.001, 4.0, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Set up survey matrices.  Design disk loading and gear ratio.
[x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([xvec](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yvec](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Evaluate some stuff to plot
[obj](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- 2\*[x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 2\*[x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 2
[g1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \-(3\*[x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 5.5)
[g2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \-([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 2\*[x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 4.5)
[g3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.8 + [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*-3 \- [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[cntr](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [obj](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[0.01, 0.1, 0.5, 1, 2, 4, 8, 16\],
                  colors\='black')
[ax.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
([cntr](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
, fmt\="%2.1f", use\_clabeltext\=True)

[cg1](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [g1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[0\], colors\='sandybrown')
[cg1.set](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet.set "matplotlib.contour.QuadContourSet.set")
(path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(angle\=135)\])

[cg2](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [g2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[0\], colors\='orangered')
[cg2.set](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet.set "matplotlib.contour.QuadContourSet.set")
(path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(angle\=60, length\=2)\])

[cg3](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [g3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[0\], colors\='mediumblue')
[cg3.set](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet.set "matplotlib.contour.QuadContourSet.set")
(path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(spacing\=7)\])

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 4)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 4)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: contours_in_optimization_demo.ipynb`](https://matplotlib.org/stable/_downloads/98351e64c40ec8099262729ba5f5ba0e/contours_in_optimization_demo.ipynb)

[`Download Python source code: contours_in_optimization_demo.py`](https://matplotlib.org/stable/_downloads/1218cd5e94040ae915edce0c78b0043b/contours_in_optimization_demo.py)

[`Download zipped: contours_in_optimization_demo.zip`](https://matplotlib.org/stable/_downloads/1df19f7028d6f96346d34d403d986a4c/contours_in_optimization_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)