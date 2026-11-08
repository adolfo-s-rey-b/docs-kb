[Skip to main content](https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html#sphx-glr-download-plot-types-3d-scatter3d-simple-py)
 to download the full example code.

scatter(xs, ys, zs)[#](https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html#scatter-xs-ys-zs "Link to this heading")

==================================================================================================================================

See [`scatter`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.axes3d.Axes3D.scatter")
.

![scatter3d simple](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_simple_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('\_mpl-gallery')

\# Make data
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
()
[xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")
(23, 32, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")
(0, 100, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[zs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html#numpy.random.Generator.uniform "numpy.random.Generator.uniform")
(\-50, \-25, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Plot
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\={"projection": "3d"})
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.Axes3D.scatter")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xticklabels\=\[\],
       yticklabels\=\[\],
       zticklabels\=\[\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: scatter3d_simple.ipynb`](https://matplotlib.org/stable/_downloads/6456ec22210b5ac17dfa7e88c007d7fc/scatter3d_simple.ipynb)

[`Download Python source code: scatter3d_simple.py`](https://matplotlib.org/stable/_downloads/7ace3c2232efcb0fd94e4999de5d1b3d/scatter3d_simple.py)

[`Download zipped: scatter3d_simple.zip`](https://matplotlib.org/stable/_downloads/03688ffb75eaa3d3d0993b54c34ec69c/scatter3d_simple.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)