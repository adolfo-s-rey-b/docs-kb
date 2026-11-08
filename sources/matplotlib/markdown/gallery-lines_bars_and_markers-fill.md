[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html#sphx-glr-download-gallery-lines-bars-and-markers-fill-py)
 to download the full example code.

Filled polygon[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html#filled-polygon "Link to this heading")

================================================================================================================================

[`fill()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
 draws a filled polygon based on lists of point coordinates _x_, _y_.

This example uses the [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)
 as an example polygon.

import matplotlib.pyplot as plt
import numpy as np

def koch\_snowflake(order, scale\=10):
    """
    Return two lists x, y of point coordinates of the Koch snowflake.

    Parameters
    ----------
    order : int
        The recursion depth.
    scale : float
        The extent of the snowflake (edge length of the base triangle).
    """
    def \_koch\_snowflake\_complex(order):
        if order \== 0:
            \# initial triangle
            angles \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 120, 240\]) + 90
            return scale / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(3) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(angles) \* 1j)
        else:
            ZR \= 0.5 \- 0.5j \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(3) / 3

            p1 \= \_koch\_snowflake\_complex(order \- 1)  \# start points
            p2 \= [np.roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll "numpy.roll")
(p1, shift\=-1)  \# end points
            dp \= p2 \- p1  \# connection vectors

            new\_points \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
(len(p1) \* 4, dtype\=[np.complex128](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex128 "numpy.complex128")
)
            new\_points\[::4\] \= p1
            new\_points\[1::4\] \= p1 + dp / 3
            new\_points\[2::4\] \= p1 + dp \* ZR
            new\_points\[3::4\] \= p1 + dp / 3 \* 2
            return new\_points

    points \= \_koch\_snowflake\_complex(order)
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= points.real, points.imag
    return [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

Basic usage:

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= koch\_snowflake(order\=5)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 8))
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
('equal')
[plt.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill "matplotlib.pyplot.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![fill](https://matplotlib.org/stable/_images/sphx_glr_fill_001_2_00x.png)

Use keyword arguments _facecolor_ and _edgecolor_ to modify the colors of the polygon. Since the _linewidth_ of the edge is 0 in the default Matplotlib style, we have to set it as well for the edge to become visible.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= koch\_snowflake(order\=2)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, figsize\=(9, 3),
                                    subplot\_kw\={'aspect': 'equal'})
[ax1.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\='lightsalmon', edgecolor\='orangered', linewidth\=3)
[ax3.fill](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\='none', edgecolor\='purple', linewidth\=3)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![fill](https://matplotlib.org/stable/_images/sphx_glr_fill_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")
     / [`matplotlib.pyplot.fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill "matplotlib.pyplot.fill")
    
*   [`matplotlib.axes.Axes.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
     / [`matplotlib.pyplot.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
    

Tags: [styling: shape](https://matplotlib.org/stable/_tags/styling-shape.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

**Total running time of the script:** (0 minutes 1.420 seconds)

[`Download Jupyter notebook: fill.ipynb`](https://matplotlib.org/stable/_downloads/a34c1373ea0f53cfa10f0f00cf9be233/fill.ipynb)

[`Download Python source code: fill.py`](https://matplotlib.org/stable/_downloads/7c4bf2de06c94e0c6ae8aaa88b90ef22/fill.py)

[`Download zipped: fill.zip`](https://matplotlib.org/stable/_downloads/45cd15978e001839386bcc24bcf1fc96/fill.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)