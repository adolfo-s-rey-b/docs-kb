[Skip to main content](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#sphx-glr-download-gallery-misc-tickedstroke-demo-py)
 to download the full example code.

TickedStroke patheffect[#](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#tickedstroke-patheffect "Link to this heading")

=============================================================================================================================================

Matplotlib's [`patheffects`](https://matplotlib.org/stable/api/patheffects_api.html#module-matplotlib.patheffects "matplotlib.patheffects")
 can be used to alter the way paths are drawn at a low enough level that they can affect almost anything.

The [patheffects guide](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#patheffects-guide)
 details the use of patheffects.

The [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")
 patheffect illustrated here draws a path with a ticked style. The spacing, length, and angle of ticks can be controlled.

See also the [Lines with a ticked patheffect](https://matplotlib.org/stable/gallery/lines_bars_and_markers/lines_with_ticks_demo.html)
 example.

See also the [Contouring the solution space of optimizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html)
 example.

import matplotlib.pyplot as plt
import numpy as np

Applying TickedStroke to paths[#](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#applying-tickedstroke-to-paths "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.patheffects as patheffects

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
[path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [Path.unit\_circle](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_circle "matplotlib.path.Path.unit_circle")
()
[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [patches.PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, facecolor\='none', lw\=2, path\_effects\=\[\
    [patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(angle\=-90, spacing\=10, length\=1)\])

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('equal')
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-2, 2)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-2, 2)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tickedstroke demo](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_001_2_00x.png)

Applying TickedStroke to lines[#](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#applying-tickedstroke-to-lines "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1\], \[0, 1\], label\="Line",
        path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(spacing\=7, angle\=135)\])

[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 101
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.3\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*8) + 0.4
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\="Curve", path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
()\])

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tickedstroke demo](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_002_2_00x.png)

Applying TickedStroke to contour plots[#](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#applying-tickedstroke-to-contour-plots "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Contour plot with objective and constraints. Curves generated by contour to represent a typical constraint in an optimization problem should be plotted with angles between zero and 180 degrees.

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

![tickedstroke demo](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_003_2_00x.png)

Direction/side of the ticks[#](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html#direction-side-of-the-ticks "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

To change which side of the line the ticks are drawn, change the sign of the angle.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
[line\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [line\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0, 1\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([line\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [line\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\="Line",
        path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(spacing\=7, angle\=135)\])

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([line\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [line\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\="Opposite side",
        path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(spacing\=7, angle\=-135)\])

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tickedstroke demo](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_004_2_00x.png)

**Total running time of the script:** (0 minutes 2.672 seconds)

[`Download Jupyter notebook: tickedstroke_demo.ipynb`](https://matplotlib.org/stable/_downloads/4a760e0d904e497acc2e1fc6618ba903/tickedstroke_demo.ipynb)

[`Download Python source code: tickedstroke_demo.py`](https://matplotlib.org/stable/_downloads/ee238568c97acaa88c1fecf30916a9a7/tickedstroke_demo.py)

[`Download zipped: tickedstroke_demo.zip`](https://matplotlib.org/stable/_downloads/d33bff2b8b5a30a6eb1c871bc5a0a0da/tickedstroke_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page