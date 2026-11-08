[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html#sphx-glr-download-gallery-mplot3d-stem3d-demo-py)
 to download the full example code.

3D stem[#](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html#d-stem "Link to this heading")

=========================================================================================================

Demonstration of a stem plot in 3D, which plots vertical lines from a baseline to the _z_\-coordinate and places a marker at the tip.

import matplotlib.pyplot as plt
import numpy as np

[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2)
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(projection\='3d'))
[ax.stem](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem "mpl_toolkits.mplot3d.Axes3D.stem")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stem3d demo](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_001_2_00x.png)

The position of the baseline can be adapted using _bottom_. The parameters _linefmt_, _markerfmt_, and _basefmt_ control basic format properties of the plot. However, in contrast to [`plot`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.axes3d.Axes3D.plot")
 not all properties are configurable via keyword arguments. For more advanced control adapt the line objects returned by [`stem`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem "mpl_toolkits.mplot3d.axes3d.Axes3D.stem")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(projection\='3d'))
[markerline](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
, [stemlines](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
, [baseline](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
 \= [ax.stem](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem "mpl_toolkits.mplot3d.Axes3D.stem")
(
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, linefmt\='grey', markerfmt\='D', bottom\=[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[markerline.set\_markerfacecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor "matplotlib.lines.Line2D.set_markerfacecolor")
('none')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stem3d demo](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_002_2_00x.png)

The orientation of the stems and baseline can be changed using _orientation_. This determines in which direction the stems are projected from the head points, towards the _bottom_ baseline.

For examples, by setting `orientation='x'`, the stems are projected along the _x_\-direction, and the baseline is in the _yz_\-plane.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(projection\='3d'))
[markerline](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
, [stemlines](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")
, [baseline](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
 \= [ax.stem](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem "mpl_toolkits.mplot3d.Axes3D.stem")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bottom\=-1, orientation\='x')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlabel\='x', ylabel\='y', zlabel\='z')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![stem3d demo](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_003_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [plot-type: specialty](https://matplotlib.org/stable/_tags/plot-type-specialty.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.616 seconds)

[`Download Jupyter notebook: stem3d_demo.ipynb`](https://matplotlib.org/stable/_downloads/09caab4922c225ce6337f112aa57234a/stem3d_demo.ipynb)

[`Download Python source code: stem3d_demo.py`](https://matplotlib.org/stable/_downloads/c0fc774cc7f31ac97da140bcecf8167e/stem3d_demo.py)

[`Download zipped: stem3d_demo.zip`](https://matplotlib.org/stable/_downloads/4f09ee780eb3756f66b05e21bcf2b36d/stem3d_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)