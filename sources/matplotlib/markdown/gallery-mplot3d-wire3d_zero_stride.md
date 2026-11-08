[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html#sphx-glr-download-gallery-mplot3d-wire3d-zero-stride-py)
 to download the full example code.

3D wireframe plots in one direction[#](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html#d-wireframe-plots-in-one-direction "Link to this heading")

========================================================================================================================================================================

Demonstrates that setting _rstride_ or _cstride_ to 0 causes wires to not be generated in the corresponding direction.

import matplotlib.pyplot as plt

from mpl\_toolkits.mplot3d import axes3d

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, [ax2](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    2, 1, figsize\=(8, 12), subplot\_kw\={'projection': '3d'})

\# Get the test data
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [axes3d.get\_test\_data](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.get_test_data.html#mpl_toolkits.mplot3d.axes3d.get_test_data "mpl_toolkits.mplot3d.axes3d.get_test_data")
(0.05)

\# Give the first plot only wireframes of the type y = c
[ax1.plot\_wireframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.Axes3D.plot_wireframe")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, rstride\=10, cstride\=0)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "mpl_toolkits.mplot3d.Axes3D.set_title")
("Column (x) stride set to 0")

\# Give the second plot only wireframes of the type x = c
[ax2.plot\_wireframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.Axes3D.plot_wireframe")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, rstride\=0, cstride\=10)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "mpl_toolkits.mplot3d.Axes3D.set_title")
("Row (y) stride set to 0")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Column (x) stride set to 0, Row (y) stride set to 0](https://matplotlib.org/stable/_images/sphx_glr_wire3d_zero_stride_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 1.985 seconds)

[`Download Jupyter notebook: wire3d_zero_stride.ipynb`](https://matplotlib.org/stable/_downloads/1a807ceff14dcd2b7a2d0847560e2c80/wire3d_zero_stride.ipynb)

[`Download Python source code: wire3d_zero_stride.py`](https://matplotlib.org/stable/_downloads/31c5575abc152a89dd97079ff1e2f646/wire3d_zero_stride.py)

[`Download zipped: wire3d_zero_stride.zip`](https://matplotlib.org/stable/_downloads/476639aed3c085ccafa38ebe239237c6/wire3d_zero_stride.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)