[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#main-content)

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
    

matplotlib.pyplot.triplot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib-pyplot-triplot "Link to this heading")

========================================================================================================================================================

matplotlib.pyplot.triplot(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4467-L4469)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "Link to this definition")

Draw an unstructured triangular grid as lines and/or markers.

Call signatures:

triplot(triangulation, ...)
triplot(x, y, \[triangles\], \*, \[mask\=mask\], ...)

The triangular grid can be specified either by passing a [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 object as the first parameter, or by passing the points _x_, _y_ and optionally the _triangles_ and a _mask_. If neither of _triangulation_ or _triangles_ are given, the triangulation is calculated on the fly.

Parameters:

**triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

An already created triangular grid.

**x, y, triangles, mask**

Parameters defining the triangular grid. See [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
. This is mutually exclusive with specifying _triangulation_.

**other\_parameters**

All other args and kwargs are forwarded to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
.

Returns:

**lines**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The drawn triangles edges.

**markers**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The drawn marker nodes.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot")
.

Examples using `matplotlib.pyplot.triplot`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#examples-using-matplotlib-pyplot-triplot "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_triplot_demo_thumb.png)

[Triplot Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triplot_demo.html)

Triplot Demo

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_smooth_delaunay_thumb.png)

[Tricontour Smooth Delaunay](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_smooth_delaunay.html)

Tricontour Smooth Delaunay

![](https://matplotlib.org/stable/_images/sphx_glr_trigradient_demo_thumb.png)

[Trigradient Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/trigradient_demo.html)

Trigradient Demo

![](https://matplotlib.org/stable/_images/sphx_glr_triinterp_demo_thumb.png)

[Triinterp Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/triinterp_demo.html)

Triinterp Demo

On this page