[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html#sphx-glr-download-gallery-mplot3d-scales3d-py)
 to download the full example code.

Scales on 3D (Log, Symlog, etc.)[#](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html#scales-on-3d-log-symlog-etc "Link to this heading")

====================================================================================================================================================

Demonstrate how to use non-linear scales such as logarithmic scales on 3D axes.

3D axes support the same axis scales as 2D plots: 'linear', 'log', 'symlog', 'logit', 'asinh', and custom 'function' scales. This example shows a mix of scales: linear on X, log on Y, and symlog on Z.

For a complete list of built-in scales, see [`matplotlib.scale`](https://matplotlib.org/stable/api/scale_api.html#module-matplotlib.scale "matplotlib.scale")
. For an overview of scale transformations, see [Scales overview](https://matplotlib.org/stable/gallery/scales/scales.html)
.

import matplotlib.pyplot as plt
import numpy as np

\# A sine chirp with increasing frequency and amplitude
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 400)  \# time
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 10 \*\* (2 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)  \# frequency, growing exponentially from 1 to 100 Hz
[phase](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* (10 \*\* (2 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \- 1) / (2 \* [np.log](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(10))
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([phase](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\*2 \* 10  \# amplitude, growing quadratically

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='3d')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.Axes3D.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Time (linear)')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Frequency, Hz (log)')
[ax.set\_zlabel](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.Axes3D.set_zlabel")
('Amplitude (symlog)')

[ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale "mpl_toolkits.mplot3d.Axes3D.set_yscale")
('log')
[ax.set\_zscale](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale "mpl_toolkits.mplot3d.Axes3D.set_zscale")
('symlog')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![scales3d](https://matplotlib.org/stable/_images/sphx_glr_scales3d_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale")
    
*   [`mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale")
    
*   [`mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale")
    
*   [`matplotlib.scale`](https://matplotlib.org/stable/api/scale_api.html#module-matplotlib.scale "matplotlib.scale")
    

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: scales3d.ipynb`](https://matplotlib.org/stable/_downloads/48232d1ddf2472de2480ed9f9cb373c4/scales3d.ipynb)

[`Download Python source code: scales3d.py`](https://matplotlib.org/stable/_downloads/2637bc5a7405d854e4919bf868aa08f8/scales3d.py)

[`Download zipped: scales3d.zip`](https://matplotlib.org/stable/_downloads/c1e43c85a6a52caaecc52c4e013e6c04/scales3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)