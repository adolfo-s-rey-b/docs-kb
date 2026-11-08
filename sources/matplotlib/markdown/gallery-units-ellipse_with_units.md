[Skip to main content](https://matplotlib.org/stable/gallery/units/ellipse_with_units.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/units/ellipse_with_units.html#sphx-glr-download-gallery-units-ellipse-with-units-py)
 to download the full example code.

Ellipse with units[#](https://matplotlib.org/stable/gallery/units/ellipse_with_units.html#ellipse-with-units "Link to this heading")

=====================================================================================================================================

Compare the ellipse generated with arcs versus a polygonal approximation.

This example requires [`basic_units.py`](https://matplotlib.org/stable/_downloads/0f0fd288c7d4a6a16f4835b96343f597/basic_units.py)

from basic\_units import cm

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patches

xcenter, ycenter \= 0.38\*cm, 0.52\*cm
width, height \= 1e-1\*cm, 3e-1\*cm
[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= \-30

[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 360.0, 1.0))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.5 \* width \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.5 \* height \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[rtheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.radians](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\
    \[[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([rtheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
), \-[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([rtheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
)\],\
    \[[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([rtheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
),  [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([rtheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
)\],\
    \])

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += xcenter
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += ycenter

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(211, aspect\='auto')
[ax.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.2, facecolor\='yellow',
        edgecolor\='yellow', linewidth\=1, zorder\=1)

[e1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
 \= [patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((xcenter, ycenter), width, height,
                     [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
, linewidth\=2, fill\=False, zorder\=2)

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([e1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(212, aspect\='equal')
[ax.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.2, facecolor\='green', edgecolor\='green', zorder\=1)
[e2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
 \= [patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((xcenter, ycenter), width, height,
                     [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
, linewidth\=2, fill\=False, zorder\=2)

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([e2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
)
[fig.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
('ellipse\_compare')

![ellipse with units](https://matplotlib.org/stable/_images/sphx_glr_ellipse_with_units_001_2_00x.png)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(211, aspect\='auto')
[ax.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.2, facecolor\='yellow',
        edgecolor\='yellow', linewidth\=1, zorder\=1)

[e1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
 \= [patches.Arc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
((xcenter, ycenter), width, height,
                 [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
, linewidth\=2, fill\=False, zorder\=2)

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([e1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(212, aspect\='equal')
[ax.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.2, facecolor\='green', edgecolor\='green', zorder\=1)
[e2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
 \= [patches.Arc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
((xcenter, ycenter), width, height,
                 [angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[angle](https://docs.python.org/3/library/functions.html#int "builtins.int")
, linewidth\=2, fill\=False, zorder\=2)

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([e2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
)
[fig.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
('arc\_compare')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ellipse with units](https://matplotlib.org/stable/_images/sphx_glr_ellipse_with_units_002_2_00x.png)

**Total running time of the script:** (0 minutes 1.633 seconds)

[`Download Jupyter notebook: ellipse_with_units.ipynb`](https://matplotlib.org/stable/_downloads/89b6330816c5203d51e34d94d7e7659a/ellipse_with_units.ipynb)

[`Download Python source code: ellipse_with_units.py`](https://matplotlib.org/stable/_downloads/a3a9db5b6392224a898cf24c11b2f368/ellipse_with_units.py)

[`Download zipped: ellipse_with_units.zip`](https://matplotlib.org/stable/_downloads/9f43ff26fa39274f72dcdab02ba0938e/ellipse_with_units.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)