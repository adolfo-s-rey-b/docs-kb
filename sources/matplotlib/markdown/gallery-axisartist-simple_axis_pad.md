[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html#sphx-glr-download-gallery-axisartist-simple-axis-pad-py)
 to download the full example code.

Simple axis pad[#](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html#simple-axis-pad "Link to this heading")

=================================================================================================================================

![simple axis pad](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_001_2_00x.png)

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
    ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(
        rect, axes\_class\=[axisartist.Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, grid\_helper\=grid\_helper,
        aspect\=1, xlim\=(\-5, 12), ylim\=(\-5, 10))
    ax.[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
\[:\].set\_visible(False)
    return ax

def add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
):
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["lat"\] \= [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= [ax1.new\_floating\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_floating_axis "mpl_toolkits.axisartist.Axes.new_floating_axis")
(0, 30)
    [axis.label.set\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
(r"$\\theta = 30^{\\circ}$")
    [axis.label.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(True)

    return [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")

def add\_floating\_axis2([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
):
    [ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["lon"\] \= [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= [ax1.new\_floating\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_floating_axis "mpl_toolkits.axisartist.Axes.new_floating_axis")
(1, 6)
    [axis.label.set\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
(r"$r = 6$")
    [axis.label.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(True)

    return [axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(9, 3.))
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.01, right\=0.99, bottom\=0.01, top\=0.99,
                    wspace\=0.01, hspace\=0.01)

def ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, d):
    [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(d, (0.5, 1), (5, \-5),
                 xycoords\="axes fraction", textcoords\="offset points",
                 va\="top", ha\="center")

[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=231)
[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, "default")

[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=232)
[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
[axis.major\_ticklabels.set\_pad](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad")
(10)
ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, "ticklabels.set\_pad(10)")

[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=233)
[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
[axis.label.set\_pad](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_pad")
(20)
ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, "label.set\_pad(20)")

[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=234)
[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
[axis.major\_ticks.set\_tick\_direction](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction "mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction")
("in")
ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, 'ticks.set\_tick\_direction("in")')

[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=235)
[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
[axis.major\_ticks.set\_tick\_direction](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction "mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction")
("out")
ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, 'ticks.set\_tick\_direction("out")')

[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= setup\_axes([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=236)
[axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.AxisArtist")
 \= add\_floating\_axis1([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
[axis.major\_ticks.set\_tick\_direction](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction "mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction")
("inout")
ann([ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
, 'ticks.set\_tick\_direction("inout")')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: simple_axis_pad.ipynb`](https://matplotlib.org/stable/_downloads/48a148a892dcf9bf95f3c0e253699d56/simple_axis_pad.ipynb)

[`Download Python source code: simple_axis_pad.py`](https://matplotlib.org/stable/_downloads/6a991ef2680010dc3e315bc57b8de102/simple_axis_pad.py)

[`Download zipped: simple_axis_pad.zip`](https://matplotlib.org/stable/_downloads/8a1aa925bde21079ff02311379f9ce08/simple_axis_pad.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)