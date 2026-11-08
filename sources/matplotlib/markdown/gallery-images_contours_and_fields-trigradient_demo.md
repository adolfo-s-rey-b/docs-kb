[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html#sphx-glr-download-gallery-images-contours-and-fields-trigradient-demo-py)
 to download the full example code.

Trigradient Demo[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html#trigradient-demo "Link to this heading")

====================================================================================================================================================

Demonstrates computation of gradient with [`matplotlib.tri.CubicTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.tri import [CubicTriInterpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
, [Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [UniformTriRefiner](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")

\# ----------------------------------------------------------------------------
\# Electrical potential of a dipole
\# ----------------------------------------------------------------------------
def dipole\_potential([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    """The electric dipole potential V, at position \*x\*, \*y\*."""
    r\_sq \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2
    theta \= [np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    z \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(theta)/r\_sq
    return ([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(z) \- z) / ([np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(z) \- [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(z))

\# ----------------------------------------------------------------------------
\# Creating a Triangulation
\# ----------------------------------------------------------------------------
\# First create the x and y coordinates of the points.
[n\_angles](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 30
[n\_radii](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10
[min\_radius](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.2
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
\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)).flatten()
[V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= dipole\_potential([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Create the Triangulation; no triangles specified so Delaunay triangulation
\# created.
[triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
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

\# ----------------------------------------------------------------------------
\# Refine data - interpolates the electrical potential V
\# ----------------------------------------------------------------------------
[refiner](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
 \= [UniformTriRefiner](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
)
[tri\_refi](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z\_test\_refi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [refiner.refine\_field](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner.refine_field "matplotlib.tri.UniformTriRefiner.refine_field")
([V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, subdiv\=3)

\# ----------------------------------------------------------------------------
\# Computes the electrical field (Ex, Ey) as gradient of electrical potential
\# ----------------------------------------------------------------------------
[tci](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
 \= [CubicTriInterpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, \-[V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
\# Gradient requested here at the mesh nodes but could be anywhere else:
([Ex](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [Ey](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
) \= [tci.gradient](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator.gradient "matplotlib.tri.CubicTriInterpolator.gradient")
([triang.x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [triang.y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[E\_norm](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([Ex](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\*\*2 + [Ey](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\*\*2)

\# ----------------------------------------------------------------------------
\# Plot the triangulation, the potential iso-contours and the vector field
\# ----------------------------------------------------------------------------
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
('equal')
\# Enforce the margins, and enlarge them to give room for the vectors.
[ax.use\_sticky\_edges](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib.axes.Axes.use_sticky_edges "matplotlib.axes.Axes.use_sticky_edges")
 \= False
[ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(0.07)

[ax.triplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, color\='0.8')

[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0., 1., 0.01)
[ax.tricontour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
([tri\_refi](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z\_test\_refi](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='hot',
              linewidths\=\[2.0, 1.0, 1.0, 1.0\])
\# Plots direction of the electrical vector field
[ax.quiver](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
([triang.x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [triang.y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Ex](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
/[E\_norm](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [Ey](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
/[E\_norm](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
,
          units\='xy', scale\=10., zorder\=3, color\='blue',
          width\=0.007, headwidth\=3., headlength\=4.)

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Gradient plot: an electrical dipole')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Gradient plot: an electrical dipole](https://matplotlib.org/stable/_images/sphx_glr_trigradient_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
     / [`matplotlib.pyplot.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontour.html#matplotlib.pyplot.tricontour "matplotlib.pyplot.tricontour")
    
*   [`matplotlib.axes.Axes.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
     / [`matplotlib.pyplot.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot")
    
*   [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
    
*   [`matplotlib.tri.Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
    
*   [`matplotlib.tri.CubicTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
    
*   [`matplotlib.tri.CubicTriInterpolator.gradient`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator.gradient "matplotlib.tri.CubicTriInterpolator.gradient")
    
*   [`matplotlib.tri.UniformTriRefiner`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "matplotlib.tri.UniformTriRefiner")
    
*   [`matplotlib.axes.Axes.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
     / [`matplotlib.pyplot.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver")
    

[`Download Jupyter notebook: trigradient_demo.ipynb`](https://matplotlib.org/stable/_downloads/5d186c5dea4d6bb9a444c26795fd41db/trigradient_demo.ipynb)

[`Download Python source code: trigradient_demo.py`](https://matplotlib.org/stable/_downloads/49c0b2ce987e181c996206b69c9ac9d9/trigradient_demo.py)

[`Download zipped: trigradient_demo.zip`](https://matplotlib.org/stable/_downloads/e60065192448782704ea11997e8fbbee/trigradient_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)