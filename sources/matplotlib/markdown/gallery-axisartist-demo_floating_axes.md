[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html#sphx-glr-download-gallery-axisartist-demo-floating-axes-py)
 to download the full example code.

`floating_axes` features[#](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html#floating-axes-features "Link to this heading")

====================================================================================================================================================

Demonstration of features of the [`floating_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.html#module-mpl_toolkits.axisartist.floating_axes "mpl_toolkits.axisartist.floating_axes")
 module:

*   Using [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
     and [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     with changing the shape of the plot.
    
*   Using [`GridHelperCurveLinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear")
     to rotate the plot and set the plot boundary.
    
*   Using [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
     to create a subplot using the return value from [`GridHelperCurveLinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear")
    .
    
*   Making a sector plot by adding more features to [`GridHelperCurveLinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear")
    .
    

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
import mpl\_toolkits.axisartist.angle\_helper as angle\_helper
import mpl\_toolkits.axisartist.floating\_axes as floating\_axes
from mpl\_toolkits.axisartist.grid\_finder import [DictFormatter](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#mpl_toolkits.axisartist.grid_finder.DictFormatter "mpl_toolkits.axisartist.grid_finder.DictFormatter")
, [FixedLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.FixedLocator.html#mpl_toolkits.axisartist.grid_finder.FixedLocator "mpl_toolkits.axisartist.grid_finder.FixedLocator")
, [MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

def setup\_axes1([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect):
    """
    A simple one.
    """
    tr \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(2, 1).rotate\_deg(30)

    grid\_helper \= [floating\_axes.GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear")
(
        tr, extremes\=(\-0.5, 3.5, 0, 4),
        grid\_locator1\=[MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(nbins\=4),
        grid\_locator2\=[MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(nbins\=4))

    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(
        rect, axes\_class\=[floating\_axes.FloatingAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.FloatingAxesBase.html#mpl_toolkits.axisartist.floating_axes.FloatingAxesBase "mpl_toolkits.axisartist.floating_axes.FloatingAxesBase")
, grid\_helper\=grid\_helper)
    [ax1.grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.grid "mpl_toolkits.axisartist.Axes.grid")
()

    aux\_ax \= [ax1.get\_aux\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes")
(tr)

    return ax1, aux\_ax

def setup\_axes2([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect):
    """
    With custom locator and formatter.
    Note that the extreme values are swapped.
    """
    tr \= [PolarAxes.PolarTransform](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
()

    pi \= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
    angle\_ticks \= {
        0: r"$0$",
        pi/4: r"$\\frac{1}{4}\\pi$",
        pi/2: r"$\\frac{1}{2}\\pi$",
    }
    grid\_helper \= [floating\_axes.GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear")
(
        tr, extremes\=(.5\*pi, 0, 2, 1),
        grid\_locator1\=[FixedLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.FixedLocator.html#mpl_toolkits.axisartist.grid_finder.FixedLocator "mpl_toolkits.axisartist.grid_finder.FixedLocator")
(\[\*angle\_ticks\]),
        tick\_formatter1\=[DictFormatter](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#mpl_toolkits.axisartist.grid_finder.DictFormatter "mpl_toolkits.axisartist.grid_finder.DictFormatter")
(angle\_ticks),
        grid\_locator2\=[MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(2),
        tick\_formatter2\=None,
    )
    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(
        rect, axes\_class\=[floating\_axes.FloatingAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.FloatingAxesBase.html#mpl_toolkits.axisartist.floating_axes.FloatingAxesBase "mpl_toolkits.axisartist.floating_axes.FloatingAxesBase")
, grid\_helper\=grid\_helper)
    [ax1.grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.grid "mpl_toolkits.axisartist.Axes.grid")
()

    \# create a parasite Axes whose transData in RA, cz
    aux\_ax \= [ax1.get\_aux\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes")
(tr)

    aux\_ax.patch \= [ax1.patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
  \# for aux\_ax to have a clip path as in ax
    [ax1.patch.zorder](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 0.9  \# but this has a side effect that the patch is
    \# drawn twice, and possibly over some other
    \# artists. So, we decrease the zorder a bit to
    \# prevent this.

    return ax1, aux\_ax

def setup\_axes3([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect):
    """
    Sometimes, things like axis\_direction need to be adjusted.
    """

    tr\_rotate \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().translate(\-95, 0)  \# rotate a bit for better orientation
    tr\_scale \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/180., 1.)  \# scale degree to radians
    tr \= tr\_rotate + tr\_scale + [PolarAxes.PolarTransform](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
()

    \# Specify theta limits in degrees
    ra0, ra1 \= 8.\*15, 14.\*15
    \# Specify radial limits
    cz0, cz1 \= 0, 14000

    grid\_helper \= [floating\_axes.GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear.html#mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear "mpl_toolkits.axisartist.floating_axes.GridHelperCurveLinear")
(
        tr, extremes\=(ra0, ra1, cz0, cz1),
        grid\_locator1\=[angle\_helper.LocatorHMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorHMS.html#mpl_toolkits.axisartist.angle_helper.LocatorHMS "mpl_toolkits.axisartist.angle_helper.LocatorHMS")
(4),
        tick\_formatter1\=[angle\_helper.FormatterHMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.FormatterHMS.html#mpl_toolkits.axisartist.angle_helper.FormatterHMS "mpl_toolkits.axisartist.angle_helper.FormatterHMS")
(),
        grid\_locator2\=[MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(3),
        tick\_formatter2\=None,
    )
    ax1 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(
        rect, axes\_class\=[floating\_axes.FloatingAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.floating_axes.FloatingAxesBase.html#mpl_toolkits.axisartist.floating_axes.FloatingAxesBase "mpl_toolkits.axisartist.floating_axes.FloatingAxesBase")
, grid\_helper\=grid\_helper)

    \# adjust axis
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["left"\].set\_axis\_direction("bottom")
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["right"\].set\_axis\_direction("top")

    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["bottom"\].set\_visible(False)
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["top"\].set\_axis\_direction("bottom")
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["top"\].toggle(ticklabels\=True, label\=True)
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["top"\].major\_ticklabels.set\_axis\_direction("top")
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["top"\].label.set\_axis\_direction("top")

    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["left"\].label.set\_text(r"cz \[km$^{-1}$\]")
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["top"\].label.set\_text(r"$\\alpha\_{1950}$")
    [ax1.grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.grid "mpl_toolkits.axisartist.Axes.grid")
()

    \# create a parasite Axes whose transData in RA, cz
    aux\_ax \= [ax1.get\_aux\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes "mpl_toolkits.axes_grid1.parasite_axes.HostAxesBase.get_aux_axes")
(tr)

    aux\_ax.patch \= [ax1.patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
  \# for aux\_ax to have a clip path as in ax
    [ax1.patch.zorder](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 0.9  \# but this has a side effect that the patch is
    \# drawn twice, and possibly over some other
    \# artists. So, we decrease the zorder a bit to
    \# prevent this.

    return ax1, aux\_ax

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 4))
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(wspace\=0.3, left\=0.05, right\=0.95)

ax1, aux\_ax1 \= setup\_axes1([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 131)
[aux\_ax1.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(\[0, 1, 2, 3\], \[3, 2, 1, 3\])

ax2, aux\_ax2 \= setup\_axes2([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 132)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10)\*.5\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
[radius](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10) + 1.
[aux\_ax2.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [radius](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

ax3, aux\_ax3 \= setup\_axes3([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 133)

[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (8 + [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10)\*(14 \- 8))\*15.  \# in degrees
[radius](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10)\*14000.
[aux\_ax3.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [radius](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo floating axes](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_001_2_00x.png)

[`Download Jupyter notebook: demo_floating_axes.ipynb`](https://matplotlib.org/stable/_downloads/36b7941182e5d255435b53dc79679cc3/demo_floating_axes.ipynb)

[`Download Python source code: demo_floating_axes.py`](https://matplotlib.org/stable/_downloads/c53046419d84d1eb912e1ce17dcc1789/demo_floating_axes.py)

[`Download zipped: demo_floating_axes.zip`](https://matplotlib.org/stable/_downloads/3680ca0f565c46eba7215b4b75100fa9/demo_floating_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)