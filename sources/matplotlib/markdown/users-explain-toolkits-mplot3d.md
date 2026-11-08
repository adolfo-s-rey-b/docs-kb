[Skip to main content](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#main-content)

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
    

The mplot3d toolkit[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#the-mplot3d-toolkit "Link to this heading")

=====================================================================================================================================

Generating 3D plots using the mplot3d toolkit.

This tutorial showcases various 3D plots. Click on the figures to see each full gallery example with the code that generates the figures.

3D Axes (of class [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
) are created by passing the `projection="3d"` keyword argument to [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
:

import matplotlib.pyplot as plt
fig \= plt.figure()
ax \= fig.add\_subplot(projection\='3d')

Multiple 3D subplots can be added on the same figure, as for 2D subplots.

[![../../../_images/sphx_glr_subplot3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_001.png)](https://matplotlib.org/gallery/mplot3d/subplot3d.html)

Changed in version 3.2.0: Prior to Matplotlib 3.2.0, it was necessary to explicitly import the [`mpl_toolkits.mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d "mpl_toolkits.mplot3d")
 module to make the '3d' projection to [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
.

See the [mplot3d FAQ](https://matplotlib.org/stable/api/toolkits/mplot3d/faq.html#toolkit-mplot3d-faq)
 for more information about the mplot3d toolkit.

Line plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#line-plots "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

See [`Axes3D.plot`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.axes3d.Axes3D.plot")
 for API documentation.

[![../../../_images/sphx_glr_lines3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_lines3d_001.png)](https://matplotlib.org/gallery/mplot3d/lines3d.html)

Scatter plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#scatter-plots "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.scatter`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.axes3d.Axes3D.scatter")
 for API documentation.

[![../../../_images/sphx_glr_scatter3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_001.png)](https://matplotlib.org/gallery/mplot3d/scatter3d.html)

Wireframe plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#wireframe-plots "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.plot_wireframe`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe")
 for API documentation.

[![../../../_images/sphx_glr_wire3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_wire3d_001.png)](https://matplotlib.org/gallery/mplot3d/wire3d.html)

Surface plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#surface-plots "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")
 for API documentation.

[![../../../_images/sphx_glr_surface3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_surface3d_001.png)](https://matplotlib.org/gallery/mplot3d/surface3d.html)

Tri-Surface plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#tri-surface-plots "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.plot_trisurf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf")
 for API documentation.

[![../../../_images/sphx_glr_trisurf3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_001.png)](https://matplotlib.org/gallery/mplot3d/trisurf3d.html)

Contour plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#contour-plots "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.contour`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contour "mpl_toolkits.mplot3d.axes3d.Axes3D.contour")
 for API documentation.

[![../../../_images/sphx_glr_contour3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_contour3d_001.png)](https://matplotlib.org/gallery/mplot3d/contour3d.html)

Filled contour plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#filled-contour-plots "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.contourf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.axes3d.Axes3D.contourf")
 for API documentation.

[![../../../_images/sphx_glr_contourf3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_001.png)](https://matplotlib.org/gallery/mplot3d/contourf3d.html)

Added in version 1.1.0: The feature demoed in the second contourf3d example was enabled as a result of a bugfix for version 1.1.0.

Fill between 3D lines[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#fill-between-3d-lines "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.fill_between`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between "mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between")
 for API documentation.

[![../../../_images/sphx_glr_fillbetween3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_fillbetween3d_001.png)](https://matplotlib.org/gallery/mplot3d/fillbetween3d.html)

Added in version 3.10.

Polygon plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#polygon-plots "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

See [`Axes3D.add_collection3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d "mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d")
 for API documentation.

[![../../../_images/sphx_glr_polys3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_polys3d_001.png)](https://matplotlib.org/gallery/mplot3d/polys3d.html)

Bar plots[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#bar-plots "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

See [`Axes3D.bar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar "mpl_toolkits.mplot3d.axes3d.Axes3D.bar")
 for API documentation.

[![../../../_images/sphx_glr_bars3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_bars3d_001.png)](https://matplotlib.org/gallery/mplot3d/bars3d.html)

Quiver[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#quiver "Link to this heading")

-----------------------------------------------------------------------------------------------------------

See [`Axes3D.quiver`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl_toolkits.mplot3d.axes3d.Axes3D.quiver "mpl_toolkits.mplot3d.axes3d.Axes3D.quiver")
 for API documentation.

[![../../../_images/sphx_glr_quiver3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_001.png)](https://matplotlib.org/gallery/mplot3d/quiver3d.html)

2D plots in 3D[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#d-plots-in-3d "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

[![../../../_images/sphx_glr_2dcollections3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_001.png)](https://matplotlib.org/gallery/mplot3d/2dcollections3d.html)

Text[#](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#text "Link to this heading")

-------------------------------------------------------------------------------------------------------

See [`Axes3D.text`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "mpl_toolkits.mplot3d.axes3d.Axes3D.text")
 for API documentation.

[![../../../_images/sphx_glr_text3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_text3d_001.png)](https://matplotlib.org/gallery/mplot3d/text3d.html)

On this page