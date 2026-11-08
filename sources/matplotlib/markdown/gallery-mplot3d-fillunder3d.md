[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html#sphx-glr-download-gallery-mplot3d-fillunder3d-py)
 to download the full example code.

Fill under 3D line graphs[#](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html#fill-under-3d-line-graphs "Link to this heading")

==============================================================================================================================================

Demonstrate how to create polygons which fill the space under a line graph. In this example polygons are semi-transparent, creating a sort of 'jagged stained glass' effect.

import math

import matplotlib.pyplot as plt
import numpy as np

[gamma](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")
 \= [np.vectorize](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")
([math.gamma](https://docs.python.org/3/library/math.html#math.gamma "math.gamma")
)
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 31
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0., 10., [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[lambdas](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
 \= range(1, 9)

[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(projection\='3d')

[facecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['viridis\_r'\]([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, len([lambdas](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
)))

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [l](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in enumerate([lambdas](https://docs.python.org/3/library/stdtypes.html#range "builtins.range")
):
    \# Note fill\_between can take coordinates as length N vectors, or scalars
    [ax.fill\_between](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between "mpl_toolkits.mplot3d.Axes3D.fill_between")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [l](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [l](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[l](https://docs.python.org/3/library/functions.html#int "builtins.int")
) / [gamma](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 1),
                    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [l](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 0,
                    [facecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[facecolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], alpha\=.7)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 10), ylim\=(1, 9), zlim\=(0, 0.35),
       xlabel\='x', ylabel\=r'$\\lambda$', zlabel\='probability')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![fillunder3d](https://matplotlib.org/stable/_images/sphx_glr_fillunder3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [plot-type: fill\_between](https://matplotlib.org/stable/_tags/plot-type-fill_between.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: fillunder3d.ipynb`](https://matplotlib.org/stable/_downloads/f24b4cb40cfad97d2eb39732a5945875/fillunder3d.ipynb)

[`Download Python source code: fillunder3d.py`](https://matplotlib.org/stable/_downloads/76b7ceeb0e946ed74946217ca457ef89/fillunder3d.py)

[`Download zipped: fillunder3d.zip`](https://matplotlib.org/stable/_downloads/025a5da5932878208d30e0b01fad0dfe/fillunder3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)