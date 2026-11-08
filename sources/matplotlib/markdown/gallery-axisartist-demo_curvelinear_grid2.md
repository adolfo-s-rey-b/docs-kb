[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html#sphx-glr-download-gallery-axisartist-demo-curvelinear-grid2-py)
 to download the full example code.

Demo CurveLinear Grid2[#](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html#demo-curvelinear-grid2 "Link to this heading")

======================================================================================================================================================

Custom grid and ticklines.

This example demonstrates how to use GridHelperCurveLinear to define custom grids and ticklines by applying a transformation on the grid. As showcase on the plot, a 5x5 matrix is displayed on the Axes.

![demo curvelinear grid2](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid2_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits.axisartist.axislines import [Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
from mpl\_toolkits.axisartist.grid\_finder import [ExtremeFinderSimple](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple "mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple")
, [MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
from mpl\_toolkits.axisartist.grid\_helper\_curvelinear import [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")

def curvelinear\_test1([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """Grid for custom transform."""

    def tr(x, y):
        return [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x)\*abs(x)\*\*.5, y

    def inv\_tr(x, y):
        return [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x)\*x\*\*2, y

    grid\_helper \= [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")
(
        (tr, inv\_tr),
        extreme\_finder\=[ExtremeFinderSimple](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple.html#mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple "mpl_toolkits.axisartist.grid_finder.ExtremeFinderSimple")
(20, 20),
        \# better tick density
        grid\_locator1\=[MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(nbins\=6), grid\_locator2\=[MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(nbins\=6))

    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(axes\_class\=[Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, grid\_helper\=grid\_helper)
    \# ax1 will have a ticks and gridlines defined by the given
    \# transform (+ transData of the Axes). Note that the transform of the Axes
    \# itself (i.e., transData) is not affected by the given transform.

    ax1.imshow([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(25).reshape(5, 5),
               vmax\=50, cmap\="gray\_r", origin\="lower")

if \_\_name\_\_ \== "\_\_main\_\_":
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 4))
    curvelinear\_test1([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_curvelinear_grid2.ipynb`](https://matplotlib.org/stable/_downloads/e14ab5a33ba3f97dd9fd03e78f38006f/demo_curvelinear_grid2.ipynb)

[`Download Python source code: demo_curvelinear_grid2.py`](https://matplotlib.org/stable/_downloads/0466e9045f8fe3100f98c2a3b536994c/demo_curvelinear_grid2.py)

[`Download zipped: demo_curvelinear_grid2.zip`](https://matplotlib.org/stable/_downloads/646eee8362effab86287e6830c0d8320/demo_curvelinear_grid2.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)