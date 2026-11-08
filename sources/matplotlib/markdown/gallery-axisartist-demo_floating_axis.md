[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html#sphx-glr-download-gallery-axisartist-demo-floating-axis-py)
 to download the full example code.

floating\_axis demo[#](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axis.html#floating-axis-demo "Link to this heading")

===========================================================================================================================================

Axis within rectangular frame.

The following code demonstrates how to put a floating polar curve within a rectangular box. In order to get a better sense of polar curves, please look at [Curvilinear grid demo](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid.html)
.

![demo floating axis](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
from mpl\_toolkits.axisartist import [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")
, [HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")
import mpl\_toolkits.axisartist.angle\_helper as angle\_helper

def curvelinear\_test2([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """Polar projection, but in a rectangular box."""
    \# see demo\_curvelinear\_grid.py for details
    grid\_helper \= [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")
(
        [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 180., 1.) + [PolarAxes.PolarTransform](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
(),
        extreme\_finder\=[angle\_helper.ExtremeFinderCycle](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle "mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle")
(
            20, 20,
            lon\_cycle\=360, lat\_cycle\=None,
            lon\_minmax\=None, lat\_minmax\=(0, [np.inf](https://docs.python.org/3/library/functions.html#float "builtins.float")
),
        ),
        grid\_locator1\=[angle\_helper.LocatorDMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorDMS.html#mpl_toolkits.axisartist.angle_helper.LocatorDMS "mpl_toolkits.axisartist.angle_helper.LocatorDMS")
(12),
        tick\_formatter1\=[angle\_helper.FormatterDMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.FormatterDMS.html#mpl_toolkits.axisartist.angle_helper.FormatterDMS "mpl_toolkits.axisartist.angle_helper.FormatterDMS")
(),
    )
    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(axes\_class\=[HostAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase")
, grid\_helper\=grid\_helper)

    \# Now create floating axis

    \# floating axis whose first coordinate (theta) is fixed at 60
    ax1.axis\["lat"\] \= axis \= ax1.new\_floating\_axis(0, 60)
    axis.label.set\_text(r"$\\theta = 60^{\\circ}$")
    axis.label.set\_visible(True)

    \# floating axis whose second coordinate (r) is fixed at 6
    ax1.axis\["lon"\] \= axis \= ax1.new\_floating\_axis(1, 6)
    axis.label.set\_text(r"$r = 6$")

    ax1.set\_aspect(1.)
    ax1.set\_xlim(\-5, 12)
    ax1.set\_ylim(\-5, 10)

    ax1.grid(True)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 5))
curvelinear\_test2([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_floating_axis.ipynb`](https://matplotlib.org/stable/_downloads/351e8891cc51b0c7e3cfc853e74e25b5/demo_floating_axis.ipynb)

[`Download Python source code: demo_floating_axis.py`](https://matplotlib.org/stable/_downloads/12927e05bde893cbae7f16aaed1b87eb/demo_floating_axis.py)

[`Download zipped: demo_floating_axis.zip`](https://matplotlib.org/stable/_downloads/db143fff850fb80f4b0cdd2977de7ae0/demo_floating_axis.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)