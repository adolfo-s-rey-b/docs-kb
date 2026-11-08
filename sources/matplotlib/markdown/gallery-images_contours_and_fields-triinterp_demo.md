[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html#sphx-glr-download-gallery-images-contours-and-fields-triinterp-demo-py)
 to download the full example code.

Triinterp Demo[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html#triinterp-demo "Link to this heading")

==============================================================================================================================================

Interpolation from triangular grid to quad grid.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.tri as mtri

\# Create triangulation.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(\[0, 1, 2, 3, 0.5, 1.5, 2.5, 1, 2, 1.5\])
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(\[0, 0, 0, 0, 1.0, 1.0, 1.0, 2, 2, 3.0\])
[triangles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[0, 1, 4\], \[1, 2, 5\], \[2, 3, 6\], \[1, 5, 4\], \[2, 6, 5\], \[4, 5, 7\],\
             \[5, 6, 8\], \[5, 8, 7\], \[7, 8, 9\]\]
[triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 \= [mtri.Triangulation](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [triangles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\# Interpolate to regularly-spaced quad grid.
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1.5 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1.5 \* [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 3, 20), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 3, 20))

[interp\_lin](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
 \= [mtri.LinearTriInterpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[zi\_lin](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [interp\_lin](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[interp\_cubic\_geom](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
 \= [mtri.CubicTriInterpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, kind\='geom')
[zi\_cubic\_geom](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [interp\_cubic\_geom](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[interp\_cubic\_min\_E](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
 \= [mtri.CubicTriInterpolator](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, kind\='min\_E')
[zi\_cubic\_min\_E](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [interp\_cubic\_min\_E](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Set up the figure
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.flatten()

\# Plot the triangulation.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].tricontourf([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].triplot([triang](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
, 'ko-')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('Triangular grid')

\# Plot linear interpolation to quad grid.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].contourf([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zi\_lin](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k-', lw\=0.5, alpha\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([xi.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k-', lw\=0.5, alpha\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title("Linear interpolation")

\# Plot cubic interpolation to quad grid, kind=geom
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].contourf([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zi\_cubic\_geom](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].plot([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k-', lw\=0.5, alpha\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].plot([xi.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k-', lw\=0.5, alpha\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_title("Cubic interpolation,\\nkind='geom'")

\# Plot cubic interpolation to quad grid, kind=min\_E
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].contourf([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [zi\_cubic\_min\_E](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].plot([xi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k-', lw\=0.5, alpha\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].plot([xi.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yi.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'k-', lw\=0.5, alpha\=0.5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].set\_title("Cubic interpolation,\\nkind='min\_E'")

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Triangular grid, Linear interpolation, Cubic interpolation, kind='geom', Cubic interpolation, kind='min_E'](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
     / [`matplotlib.pyplot.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "matplotlib.pyplot.tricontourf")
    
*   [`matplotlib.axes.Axes.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
     / [`matplotlib.pyplot.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot")
    
*   [`matplotlib.axes.Axes.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
     / [`matplotlib.pyplot.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
    
*   [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
     / [`matplotlib.pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
    
*   [`matplotlib.tri`](https://matplotlib.org/stable/api/tri_api.html#module-matplotlib.tri "matplotlib.tri")
    
*   [`matplotlib.tri.LinearTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "matplotlib.tri.LinearTriInterpolator")
    
*   [`matplotlib.tri.CubicTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
    
*   [`matplotlib.tri.Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
    

**Total running time of the script:** (0 minutes 1.325 seconds)

[`Download Jupyter notebook: triinterp_demo.ipynb`](https://matplotlib.org/stable/_downloads/16cbf477a4e69133c3df55e50029793a/triinterp_demo.ipynb)

[`Download Python source code: triinterp_demo.py`](https://matplotlib.org/stable/_downloads/361aba6dfcdc72919013a5c7520af2e2/triinterp_demo.py)

[`Download zipped: triinterp_demo.zip`](https://matplotlib.org/stable/_downloads/c6ffa34d87ef33cbeb18250b23b0c66c/triinterp_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)