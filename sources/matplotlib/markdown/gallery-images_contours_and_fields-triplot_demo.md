[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html#sphx-glr-download-gallery-images-contours-and-fields-triplot-demo-py)
 to download the full example code.

Triplot Demo[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html#triplot-demo "Link to this heading")

========================================================================================================================================

Creating and plotting unstructured triangular grids.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.tri as tri

Creating a Triangulation without specifying the triangles results in the Delaunay triangulation of the points.

\# First create the x and y coordinates of the points.
[n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 36
[n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8
[min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.25
[radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.95, [n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
, endpoint\=False)
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[..., [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\], [n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
, axis\=1)
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1::2\] += [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / [n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()

\# Create the Triangulation; no triangles so Delaunay triangulation created.
[triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [tri.Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Mask off unwanted triangles.
[triang.set\_mask](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
([np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[triang.triangles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\].mean(axis\=1),
                         [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[triang.triangles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\].mean(axis\=1))
                < [min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

Plot the triangulation.

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax1.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
('equal')
[ax1.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, 'bo-', lw\=1)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('triplot of Delaunay triangulation')

![triplot of Delaunay triangulation](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_001_2_00x.png)

You can specify your own triangulation rather than perform a Delaunay triangulation of the points, where each triangle is given by the indices of the three points that make up the triangle, ordered in either a clockwise or anticlockwise manner.

[xy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(\[\
    \[\-0.101, 0.872\], \[\-0.080, 0.883\], \[\-0.069, 0.888\], \[\-0.054, 0.890\],\
    \[\-0.045, 0.897\], \[\-0.057, 0.895\], \[\-0.073, 0.900\], \[\-0.087, 0.898\],\
    \[\-0.090, 0.904\], \[\-0.069, 0.907\], \[\-0.069, 0.921\], \[\-0.080, 0.919\],\
    \[\-0.073, 0.928\], \[\-0.052, 0.930\], \[\-0.048, 0.942\], \[\-0.062, 0.949\],\
    \[\-0.054, 0.958\], \[\-0.069, 0.954\], \[\-0.087, 0.952\], \[\-0.087, 0.959\],\
    \[\-0.080, 0.966\], \[\-0.085, 0.973\], \[\-0.087, 0.965\], \[\-0.097, 0.965\],\
    \[\-0.097, 0.975\], \[\-0.092, 0.984\], \[\-0.101, 0.980\], \[\-0.108, 0.980\],\
    \[\-0.104, 0.987\], \[\-0.102, 0.993\], \[\-0.115, 1.001\], \[\-0.099, 0.996\],\
    \[\-0.101, 1.007\], \[\-0.090, 1.010\], \[\-0.087, 1.021\], \[\-0.069, 1.021\],\
    \[\-0.052, 1.022\], \[\-0.052, 1.017\], \[\-0.069, 1.010\], \[\-0.064, 1.005\],\
    \[\-0.048, 1.005\], \[\-0.031, 1.005\], \[\-0.031, 0.996\], \[\-0.040, 0.987\],\
    \[\-0.045, 0.980\], \[\-0.052, 0.975\], \[\-0.040, 0.973\], \[\-0.026, 0.968\],\
    \[\-0.020, 0.954\], \[\-0.006, 0.947\], \[ 0.003, 0.935\], \[ 0.006, 0.926\],\
    \[ 0.005, 0.921\], \[ 0.022, 0.923\], \[ 0.033, 0.912\], \[ 0.029, 0.905\],\
    \[ 0.017, 0.900\], \[ 0.012, 0.895\], \[ 0.027, 0.893\], \[ 0.019, 0.886\],\
    \[ 0.001, 0.883\], \[\-0.012, 0.884\], \[\-0.029, 0.883\], \[\-0.038, 0.879\],\
    \[\-0.057, 0.881\], \[\-0.062, 0.876\], \[\-0.078, 0.876\], \[\-0.087, 0.872\],\
    \[\-0.030, 0.907\], \[\-0.007, 0.905\], \[\-0.057, 0.916\], \[\-0.025, 0.933\],\
    \[\-0.077, 0.990\], \[\-0.059, 0.993\]\])
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.degrees](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([xy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\])
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.degrees](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([xy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\])

[triangles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(\[\
    \[67, 66,  1\], \[65,  2, 66\], \[ 1, 66,  2\], \[64,  2, 65\], \[63,  3, 64\],\
    \[60, 59, 57\], \[ 2, 64,  3\], \[ 3, 63,  4\], \[ 0, 67,  1\], \[62,  4, 63\],\
    \[57, 59, 56\], \[59, 58, 56\], \[61, 60, 69\], \[57, 69, 60\], \[ 4, 62, 68\],\
    \[ 6,  5,  9\], \[61, 68, 62\], \[69, 68, 61\], \[ 9,  5, 70\], \[ 6,  8,  7\],\
    \[ 4, 70,  5\], \[ 8,  6,  9\], \[56, 69, 57\], \[69, 56, 52\], \[70, 10,  9\],\
    \[54, 53, 55\], \[56, 55, 53\], \[68, 70,  4\], \[52, 56, 53\], \[11, 10, 12\],\
    \[69, 71, 68\], \[68, 13, 70\], \[10, 70, 13\], \[51, 50, 52\], \[13, 68, 71\],\
    \[52, 71, 69\], \[12, 10, 13\], \[71, 52, 50\], \[71, 14, 13\], \[50, 49, 71\],\
    \[49, 48, 71\], \[14, 16, 15\], \[14, 71, 48\], \[17, 19, 18\], \[17, 20, 19\],\
    \[48, 16, 14\], \[48, 47, 16\], \[47, 46, 16\], \[16, 46, 45\], \[23, 22, 24\],\
    \[21, 24, 22\], \[17, 16, 45\], \[20, 17, 45\], \[21, 25, 24\], \[27, 26, 28\],\
    \[20, 72, 21\], \[25, 21, 72\], \[45, 72, 20\], \[25, 28, 26\], \[44, 73, 45\],\
    \[72, 45, 73\], \[28, 25, 29\], \[29, 25, 31\], \[43, 73, 44\], \[73, 43, 40\],\
    \[72, 73, 39\], \[72, 31, 25\], \[42, 40, 43\], \[31, 30, 29\], \[39, 73, 40\],\
    \[42, 41, 40\], \[72, 33, 31\], \[32, 31, 33\], \[39, 38, 72\], \[33, 72, 38\],\
    \[33, 38, 34\], \[37, 35, 38\], \[34, 38, 35\], \[35, 37, 36\]\])

Rather than create a Triangulation object, can simply pass x, y and triangles arrays to triplot directly. It would be better to use a Triangulation object if the same triangulation was to be used more than once to save duplicated calculations.

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax2.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
('equal')
[ax2.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [triangles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'go-', lw\=1.0)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('triplot of user-specified triangulation')
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Longitude (degrees)')
[ax2.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Latitude (degrees)')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![triplot of user-specified triangulation](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
     / [`matplotlib.pyplot.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot")
    
*   [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
    
*   [`matplotlib.tri.Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
    

**Total running time of the script:** (0 minutes 1.252 seconds)

[`Download Jupyter notebook: triplot_demo.ipynb`](https://matplotlib.org/stable/_downloads/0bd1a8e995583965bd9982eea897efc9/triplot_demo.ipynb)

[`Download Python source code: triplot_demo.py`](https://matplotlib.org/stable/_downloads/3df28a3c8ff5be58c4e114559ebb6ac7/triplot_demo.py)

[`Download zipped: triplot_demo.zip`](https://matplotlib.org/stable/_downloads/f19073a36975c98fd033e3e505ae8b89/triplot_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)