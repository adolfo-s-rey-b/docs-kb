[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html#sphx-glr-download-gallery-axisartist-demo-axis-direction-py)
 to download the full example code.

axis\_direction demo[#](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html#axis-direction-demo "Link to this heading")

==============================================================================================================================================

![bottom, left, top, right, bottom, left, top, right](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.projections import PolarAxes
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
import mpl\_toolkits.axisartist as axisartist
from mpl\_toolkits.axisartist import angle\_helper, grid\_finder
from mpl\_toolkits.axisartist.grid\_helper\_curvelinear import [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")

def setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect):
    """Polar projection, but in a rectangular box."""
    \# see demo\_curvelinear\_grid.py for details
    grid\_helper \= [GridHelperCurveLinear](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.GridHelperCurveLinear")
(
        [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/180., 1.) + [PolarAxes.PolarTransform](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "matplotlib.projections.polar.PolarTransform")
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
        grid\_locator2\=[grid\_finder.MaxNLocator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "mpl_toolkits.axisartist.grid_finder.MaxNLocator")
(5),
        tick\_formatter1\=[angle\_helper.FormatterDMS](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.FormatterDMS.html#mpl_toolkits.axisartist.angle_helper.FormatterDMS "mpl_toolkits.axisartist.angle_helper.FormatterDMS")
(),
    )
    [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(
        rect, axes\_class\=[axisartist.Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, grid\_helper\=grid\_helper,
        aspect\=1, xlim\=(\-5, 12), ylim\=(\-5, 10))
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\[:\].toggle(ticklabels\=False)
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.grid "mpl_toolkits.axisartist.Axes.grid")
(color\=".9")
    return [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")

def add\_floating\_axis1([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
):
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["lat"\] \= [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= [ax.new\_floating\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_floating_axis "mpl_toolkits.axisartist.Axes.new_floating_axis")
(0, 30)
    [axis.label.set\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
(r"$\\theta = 30^{\\circ}$")
    [axis.label.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(True)
    return [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")

def add\_floating\_axis2([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
):
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["lon"\] \= [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= [ax.new\_floating\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_floating_axis "mpl_toolkits.axisartist.Axes.new_floating_axis")
(1, 6)
    [axis.label.set\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
(r"$r = 6$")
    [axis.label.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(True)
    return [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 4), layout\="constrained")

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [d](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate(\["bottom", "left", "top", "right"\]):
    [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=241+[i](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
    [axis.set\_axis\_direction](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction "mpl_toolkits.axisartist.AxisArtist.set_axis_direction")
([d](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [ax.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.set "mpl_toolkits.axisartist.Axes.set")
(title\=[d](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [d](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate(\["bottom", "left", "top", "right"\]):
    [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=245+[i](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis2([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
    [axis.set\_axis\_direction](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction "mpl_toolkits.axisartist.AxisArtist.set_axis_direction")
([d](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [ax.set](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.set "mpl_toolkits.axisartist.Axes.set")
(title\=[d](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.739 seconds)

[`Download Jupyter notebook: demo_axis_direction.ipynb`](https://matplotlib.org/stable/_downloads/6c12378081cacdc3722f0f83cc7d33b7/demo_axis_direction.ipynb)

[`Download Python source code: demo_axis_direction.py`](https://matplotlib.org/stable/_downloads/a209d398996b5e5fa1542119df3c251c/demo_axis_direction.py)

[`Download zipped: demo_axis_direction.zip`](https://matplotlib.org/stable/_downloads/1c80899d074a2ef4d5096298cfab56c1/demo_axis_direction.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)