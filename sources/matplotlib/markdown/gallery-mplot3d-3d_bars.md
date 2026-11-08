[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html#sphx-glr-download-gallery-mplot3d-3d-bars-py)
 to download the full example code.

Demo of 3D bar charts[#](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html#demo-of-3d-bar-charts "Link to this heading")

==================================================================================================================================

A basic demo of how to plot 3D bars with and without shading.

import matplotlib.pyplot as plt
import numpy as np

\# set up the figure and Axes
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 3))
[ax1](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(121, projection\='3d')
[ax2](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(122, projection\='3d')

\# fake data
[\_x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(4)
[\_y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(5)
[\_xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [\_yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([\_x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [\_y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [\_xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.ravel(), [\_yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.ravel()

[top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
([top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[width](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [depth](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 1

[ax1.bar3d](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d "mpl_toolkits.mplot3d.Axes3D.bar3d")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [width](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [depth](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, shade\=True)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "mpl_toolkits.mplot3d.Axes3D.set_title")
('Shaded')

[ax2.bar3d](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d "mpl_toolkits.mplot3d.Axes3D.bar3d")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [width](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [depth](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, shade\=False)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "mpl_toolkits.mplot3d.Axes3D.set_title")
('Not Shaded')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Shaded, Not Shaded](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [styling: texture](https://matplotlib.org/stable/_tags/styling-texture.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: 3d_bars.ipynb`](https://matplotlib.org/stable/_downloads/5dd201ca4ff3aaad7278c3fe8219badd/3d_bars.ipynb)

[`Download Python source code: 3d_bars.py`](https://matplotlib.org/stable/_downloads/b2426003d482f6dc8125fd971aafd3d4/3d_bars.py)

[`Download zipped: 3d_bars.zip`](https://matplotlib.org/stable/_downloads/1fbcf16b9737e33c9dff5eab12969a83/3d_bars.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)