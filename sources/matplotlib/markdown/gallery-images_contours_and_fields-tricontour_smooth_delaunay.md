[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html#sphx-glr-download-gallery-images-contours-and-fields-tricontour-smooth-delaunay-py)
 to download the full example code.

Tricontour Smooth Delaunay[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html#tricontour-smooth-delaunay "Link to this heading")

==================================================================================================================================================================================

Demonstrates high-resolution tricontouring of a random set of points; a [`matplotlib.tri.TriAnalyzer`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "matplotlib.tri.TriAnalyzer")
 is used to improve the plot quality.

The initial data points and triangular grid for this demo are:

*   a set of random points is instantiated, inside \[-1, 1\] x \[-1, 1\] square
    
*   A Delaunay triangulation of these points is then computed, of which a random subset of triangles is masked out by the user (based on _init\_mask\_frac_ parameter). This simulates invalidated data.
    

The proposed generic procedure to obtain a high resolution contouring of such a data set is the following:

1.  Compute an extended mask with a [`matplotlib.tri.TriAnalyzer`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "matplotlib.tri.TriAnalyzer")
    , which will exclude badly shaped (flat) triangles from the border of the triangulation. Apply the mask to the triangulation (using set\_mask).
    
2.  Refine and interpolate the data using a [`matplotlib.tri.UniformTriRefiner`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
    .
    
3.  Plot the refined data with [`tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
    .
    

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.tri import [TriAnalyzer](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "matplotlib.tri.TriAnalyzer")
, [Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [UniformTriRefiner](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")

\# ----------------------------------------------------------------------------
\# Analytical test function
\# ----------------------------------------------------------------------------
def experiment\_res(x, y):
    """An analytic function representing experiment results."""
    x \= 2 \* x
    r1 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((0.5 \- x)\*\*2 + (0.5 \- y)\*\*2)
    theta1 \= [np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(0.5 \- x, 0.5 \- y)
    r2 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((\-x \- 0.2)\*\*2 + (\-y \- 0.2)\*\*2)
    theta2 \= [np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-x \- 0.2, \-y \- 0.2)
    z \= (4 \* ([np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((r1/10)\*\*2) \- 1) \* 30 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(3 \* theta1) +
         ([np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((r2/10)\*\*2) \- 1) \* 30 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(5 \* theta2) +
         2 \* (x\*\*2 + y\*\*2))
    return ([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(z) \- z) / ([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(z) \- [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(z))

\# ----------------------------------------------------------------------------
\# Generating the initial data test points and triangulation for the demo
\# ----------------------------------------------------------------------------
\# User parameters for data test points

\# Number of test data points, tested from 3 to 5000 for subdiv=3
[n\_test](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200

\# Number of recursive subdivisions of the initial mesh for smooth plots.
\# Values >3 might result in a very high number of triangles for the refine
\# mesh: new triangles numbering = (4\*\*subdiv)\*ntri
[subdiv](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 3

\# Float > 0. adjusting the proportion of (invalid) initial triangles which will
\# be masked out. Enter 0 for no mask.
[init\_mask\_frac](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.0

\# Minimum circle ratio - border triangles with circle ratio below this will be
\# masked if they touch a border. Suggested value 0.01; use -1 to keep all
\# triangles.
[min\_circle\_ratio](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= .01

\# Random points
[random\_gen](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(seed\=19680801)
[x\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [random\_gen.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.uniform.html#numpy.random.RandomState.uniform "numpy.random.RandomState.uniform")
(\-1., 1., size\=[n\_test](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [random\_gen.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.uniform.html#numpy.random.RandomState.uniform "numpy.random.RandomState.uniform")
(\-1., 1., size\=[n\_test](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[z\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= experiment\_res([x\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# meshing with Delaunay triangulation
[tri](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
([x\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ntri](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [tri.triangles.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]

\# Some invalid data are masked out
[mask\_init](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
([ntri](https://docs.python.org/3/library/functions.html#int "builtins.int")
, dtype\=bool)
[masked\_tri](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [random\_gen.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randint.html#numpy.random.RandomState.randint "numpy.random.RandomState.randint")
(0, [ntri](https://docs.python.org/3/library/functions.html#int "builtins.int")
, int([ntri](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [init\_mask\_frac](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
[mask\_init](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[masked\_tri](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\] \= True
[tri.set\_mask](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
([mask\_init](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# ----------------------------------------------------------------------------
\# Improving the triangulation before high-res plots: removing flat triangles
\# ----------------------------------------------------------------------------
\# masking badly shaped triangles at the border of the triangular mesh.
[mask](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [TriAnalyzer](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "matplotlib.tri.TriAnalyzer")
([tri](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
).get\_flat\_tri\_mask([min\_circle\_ratio](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[tri.set\_mask](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
([mask](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# refining the data
[refiner](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
 \= [UniformTriRefiner](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
([tri](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
)
[tri\_refi](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z\_test\_refi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [refiner.refine\_field](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner.refine_field "matplotlib.tri.UniformTriRefiner.refine_field")
([z\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [subdiv](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[subdiv](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# analytical 'results' for comparison
[z\_expected](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= experiment\_res([tri\_refi.x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [tri\_refi.y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# for the demo: loading the 'flat' triangles for plot
[flat\_tri](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
([x\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y\_test](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[flat\_tri.set\_mask](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
(~[mask](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# ----------------------------------------------------------------------------
\# Now the plots
\# ----------------------------------------------------------------------------
\# User options for plots
[plot\_tri](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
 \= True          \# plot of base triangulation
[plot\_masked\_tri](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
 \= True   \# plot of excessively flat excluded triangles
[plot\_refi\_tri](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
 \= False    \# plot of refined triangulation
[plot\_expected](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
 \= False    \# plot of analytical function values for comparison

\# Graphical options for tricontouring
[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0., 1., 0.025)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
('equal')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Filtering a Delaunay mesh\\n"
             "(application to high-resolution tricontouring)")

\# 1) plot of the refined (computed) data contours:
[ax.tricontour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
([tri\_refi](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z\_test\_refi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='Blues',
              linewidths\=\[2.0, 0.5, 1.0, 0.5\])
\# 2) plot of the expected (analytical) data contours (dashed):
if [plot\_expected](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
:
    [ax.tricontour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
([tri\_refi](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z\_expected](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='Blues',
                  linestyles\='--')
\# 3) plot of the fine mesh on which interpolation was done:
if [plot\_refi\_tri](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
:
    [ax.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
([tri\_refi](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, color\='0.97')
\# 4) plot of the initial 'coarse' mesh:
if [plot\_tri](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
:
    [ax.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
([tri](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, color\='0.7')
\# 4) plot of the unvalidated triangles from naive Delaunay Triangulation:
if [plot\_masked\_tri](https://docs.python.org/3/library/functions.html#bool "builtins.bool")
:
    [ax.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
([flat\_tri](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, color\='red')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Filtering a Delaunay mesh (application to high-resolution tricontouring)](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_delaunay_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
     / [`matplotlib.pyplot.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontour.html#matplotlib.pyplot.tricontour "matplotlib.pyplot.tricontour")
    
*   [`matplotlib.axes.Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
     / [`matplotlib.pyplot.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "matplotlib.pyplot.tricontourf")
    
*   [`matplotlib.axes.Axes.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
     / [`matplotlib.pyplot.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot")
    
*   [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
    
*   [`matplotlib.tri.Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
    
*   [`matplotlib.tri.TriAnalyzer`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "matplotlib.tri.TriAnalyzer")
    
*   [`matplotlib.tri.UniformTriRefiner`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
    

[`Download Jupyter notebook: tricontour_smooth_delaunay.ipynb`](https://matplotlib.org/stable/_downloads/2b27807fd43d90bc64e88f8934069535/tricontour_smooth_delaunay.ipynb)

[`Download Python source code: tricontour_smooth_delaunay.py`](https://matplotlib.org/stable/_downloads/0e6c09e389820026dfb75063860b5045/tricontour_smooth_delaunay.py)

[`Download zipped: tricontour_smooth_delaunay.zip`](https://matplotlib.org/stable/_downloads/91cb7289cc0742a0402b62cfd80716f1/tricontour_smooth_delaunay.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)