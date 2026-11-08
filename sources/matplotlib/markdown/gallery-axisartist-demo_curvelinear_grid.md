[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html#sphx-glr-download-gallery-axisartist-demo-curvelinear-grid-py)
 to download the full example code.

Curvilinear grid demo[#](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html#curvilinear-grid-demo "Link to this heading")

===================================================================================================================================================

Custom grid and ticklines.

This example demonstrates how to use [`GridHelperCurveLinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear")
 to define custom grids and ticklines by applying a transformation on the grid. This can be used, as shown on the second plot, to create polar projections in a rectangular box.

![demo curvelinear grid](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
from mpl\_toolkits.axisartist import [Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, [HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")
, angle\_helper
from mpl\_toolkits.axisartist.grid\_helper\_curvelinear import [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")

def curvelinear\_test1([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """
    Grid for custom transform.
    """

    def tr(x, y): return x, y \- x
    def inv\_tr(x, y): return x, y + x

    grid\_helper \= [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")
((tr, inv\_tr))

    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(1, 2, 1, axes\_class\=[Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, grid\_helper\=grid\_helper)
    \# ax1 will have ticks and gridlines defined by the given transform (+
    \# transData of the Axes).  Note that the transform of the Axes itself
    \# (i.e., transData) is not affected by the given transform.
    xx, yy \= tr([np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[3, 6\]), [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[5, 10\]))
    ax1.plot(xx, yy)

    ax1.set\_aspect(1)
    ax1.set\_xlim(0, 10)
    ax1.set\_ylim(0, 10)

    ax1.axis\["t"\] \= ax1.new\_floating\_axis(0, 3)
    ax1.axis\["t2"\] \= ax1.new\_floating\_axis(1, 7)
    ax1.grid(True, zorder\=0)

def curvelinear\_test2([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """
    Polar projection, but in a rectangular box.
    """

    \# PolarAxes.PolarTransform takes radian. However, we want our coordinate
    \# system in degree
    tr \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/180, 1) + [PolarAxes.PolarTransform](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
()
    \# Polar projection, which involves cycle, and also has limits in
    \# its coordinates, needs a special method to find the extremes
    \# (min, max of the coordinate within the view).
    extreme\_finder \= [angle\_helper.ExtremeFinderCycle](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle "mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle")
(
        nx\=20, ny\=20,  \# Number of sampling points in each direction.
        lon\_cycle\=360, lat\_cycle\=None,
        lon\_minmax\=None, lat\_minmax\=(0, [np.inf](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
    )
    \# Find grid values appropriate for the coordinate (degree, minute, second).
    grid\_locator1 \= [angle\_helper.LocatorDMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorDMS.html#mpl_toolkits.axisartist.angle_helper.LocatorDMS "mpl_toolkits.axisartist.angle_helper.LocatorDMS")
(12)
    \# Use an appropriate formatter.  Note that the acceptable Locator and
    \# Formatter classes are a bit different than that of Matplotlib, which
    \# cannot directly be used here (this may be possible in the future).
    tick\_formatter1 \= [angle\_helper.FormatterDMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.FormatterDMS.html#mpl_toolkits.axisartist.angle_helper.FormatterDMS "mpl_toolkits.axisartist.angle_helper.FormatterDMS")
()

    grid\_helper \= [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")
(
        tr, extreme\_finder\=extreme\_finder,
        grid\_locator1\=grid\_locator1, tick\_formatter1\=tick\_formatter1)
    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(
        1, 2, 2, axes\_class\=[HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")
, grid\_helper\=grid\_helper)

    \# make ticklabels of right and top axis visible.
    ax1.axis\["right"\].major\_ticklabels.set\_visible(True)
    ax1.axis\["top"\].major\_ticklabels.set\_visible(True)
    \# let right axis shows ticklabels for 1st coordinate (angle)
    ax1.axis\["right"\].get\_helper().nth\_coord\_ticks \= 0
    \# let bottom axis shows ticklabels for 2nd coordinate (radius)
    ax1.axis\["bottom"\].get\_helper().nth\_coord\_ticks \= 1

    ax1.set\_aspect(1)
    ax1.set\_xlim(\-5, 12)
    ax1.set\_ylim(\-5, 10)

    ax1.grid(True, zorder\=0)

    \# A parasite Axes with given transform
    ax2 \= ax1.get\_aux\_axes(tr)
    \# note that ax2.transData == tr + ax1.transData
    \# Anything you draw in ax2 will match the ticks and grids of ax1.
    ax2.plot([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 30, 51), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(10, 10, 51), linewidth\=2)

    ax2.pcolor([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 90, 4), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 4),
               [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(9).reshape((3, 3)))
    ax2.contour([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 90, 4), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 4),
                [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(16).reshape((4, 4)), colors\="k")

if \_\_name\_\_ \== "\_\_main\_\_":
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 4))

    curvelinear\_test1([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
    curvelinear\_test2([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_curvelinear_grid.ipynb`](https://matplotlib.org/stable/_downloads/c489281f9c2c188621a9c8ede846c392/demo_curvelinear_grid.ipynb)

[`Download Python source code: demo_curvelinear_grid.py`](https://matplotlib.org/stable/_downloads/0dff3dd67468123eb00b27dd85176840/demo_curvelinear_grid.py)

[`Download zipped: demo_curvelinear_grid.zip`](https://matplotlib.org/stable/_downloads/f2aa14dd0210669ddd68a3101d7e6d24/demo_curvelinear_grid.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)