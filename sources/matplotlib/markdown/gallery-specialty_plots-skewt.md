[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html#sphx-glr-download-gallery-specialty-plots-skewt-py)
 to download the full example code.

SkewT-logP diagram: using transforms and custom projections[#](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html#skewt-logp-diagram-using-transforms-and-custom-projections "Link to this heading")

===================================================================================================================================================================================================================

This serves as an intensive exercise of Matplotlib's transforms and custom projection API. This example produces a so-called SkewT-logP diagram, which is a common plot in meteorology for displaying vertical profiles of temperature. As far as Matplotlib is concerned, the complexity comes from having X and Y axes that are not orthogonal. This is handled by including a skew component to the basic Axes transforms. Additional complexity comes in handling the fact that the upper and lower X-axes have different data ranges, which necessitates a bunch of custom classes for ticks, spines, and axis to handle this.

from contextlib import [ExitStack](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")

from matplotlib.axes import [Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
import matplotlib.axis as maxis
from matplotlib.projections import [register\_projection](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
import matplotlib.spines as mspines
import matplotlib.transforms as transforms

\# The sole purpose of this class is to look at the upper, lower, or total
\# interval as appropriate and see what parts of the tick to draw, if any.
class SkewXTick([maxis.XTick](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XTick "matplotlib.axis.XTick")
):
    def draw(self, renderer):
        \# When adding the callbacks with \`stack.callback\`, we fetch the current
        \# visibility state of the artist with \`get\_visible\`; the ExitStack will
        \# restore these states (\`set\_visible\`) at the end of the block (after
        \# the draw).
        with [ExitStack](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
() as stack:
            for artist in \[self.gridline, self.tick1line, self.tick2line,\
                           self.label1, self.label2\]:
                stack.callback(artist.set\_visible, artist.get\_visible())
            needs\_lower \= transforms.\_interval\_contains(
                self.axes.lower\_xlim, self.get\_loc())
            needs\_upper \= transforms.\_interval\_contains(
                self.axes.upper\_xlim, self.get\_loc())
            self.tick1line.set\_visible(
                self.tick1line.get\_visible() and needs\_lower)
            self.label1.set\_visible(
                self.label1.get\_visible() and needs\_lower)
            self.tick2line.set\_visible(
                self.tick2line.get\_visible() and needs\_upper)
            self.label2.set\_visible(
                self.label2.get\_visible() and needs\_upper)
            super().draw(renderer)

    def get\_view\_interval(self):
        return self.axes.xaxis.get\_view\_interval()

\# This class exists to provide two separate sets of intervals to the tick,
\# as well as create instances of the custom tick
class SkewXAxis([maxis.XAxis](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
):
    def \_get\_tick(self, major):
        return [SkewXTick](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XTick "matplotlib.axis.XTick")
(self.axes, None, major\=major)

    def get\_view\_interval(self):
        return self.axes.upper\_xlim\[0\], self.axes.lower\_xlim\[1\]

\# This class exists to calculate the separate data range of the
\# upper X-axis and draw the spine there. It also provides this range
\# to the X-axis artist for ticking and gridlines
class SkewSpine([mspines.Spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
):
    def \_adjust\_location(self):
        pts \= self.\_path.vertices
        if self.spine\_type \== 'top':
            pts\[:, 0\] \= self.axes.upper\_xlim
        else:
            pts\[:, 0\] \= self.axes.lower\_xlim

\# This class handles registration of the skew-xaxes as a projection as well
\# as setting up the appropriate transformations. It also overrides standard
\# spines and axes instances as appropriate.
class SkewXAxes([Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    \# The projection must specify a name.  This will be used be the
    \# user to select the projection, i.e. \`\`subplot(projection='skewx')\`\`.
    name \= 'skewx'

    def \_init\_axis(self):
        \# Taken from Axes and modified to use our modified X-axis
        self.xaxis \= [SkewXAxis](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
(self)
        self.spines.top.register\_axis(self.xaxis)
        self.spines.bottom.register\_axis(self.xaxis)
        self.yaxis \= [maxis.YAxis](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")
(self)
        self.spines.left.register\_axis(self.yaxis)
        self.spines.right.register\_axis(self.yaxis)

    def \_gen\_axes\_spines(self):
        spines \= {'top': [SkewSpine.linear\_spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.linear_spine "matplotlib.spines.Spine.linear_spine")
(self, 'top'),
                  'bottom': [mspines.Spine.linear\_spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.linear_spine "matplotlib.spines.Spine.linear_spine")
(self, 'bottom'),
                  'left': [mspines.Spine.linear\_spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.linear_spine "matplotlib.spines.Spine.linear_spine")
(self, 'left'),
                  'right': [mspines.Spine.linear\_spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.linear_spine "matplotlib.spines.Spine.linear_spine")
(self, 'right')}
        return spines

    def \_set\_lim\_and\_transforms(self):
        """
        This is called once when the plot is created to set up all the
        transforms for the data, text and grids.
        """
        rot \= 30

        \# Get the standard transform setup from the Axes base class
        super().\_set\_lim\_and\_transforms()

        \# Need to put the skew in the middle, after the scale and limits,
        \# but before the transAxes. This way, the skew is done in Axes
        \# coordinates thus performing the transform around the proper origin
        \# We keep the pre-transAxes transform around for other users, like the
        \# spines for finding bounds
        self.transDataToAxes \= (
            self.transScale
            + self.transLimits
            + [transforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().skew\_deg(rot, 0)
        )
        \# Create the full transform from Data to Pixels
        self.transData \= self.transDataToAxes + self.transAxes

        \# Blended transforms like this need to have the skewing applied using
        \# both axes, in axes coords like before.
        self.\_xaxis\_transform \= (
            [transforms.blended\_transform\_factory](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
(
                self.transScale + self.transLimits,
                [transforms.IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())
            + [transforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().skew\_deg(rot, 0)
            + self.transAxes
        )

    @property
    def lower\_xlim(self):
        return self.axes.viewLim.intervalx

    @property
    def upper\_xlim(self):
        pts \= \[\[0., 1.\], \[1., 1.\]\]
        return self.transDataToAxes.inverted().transform(pts)\[:, 0\]

\# Now register the projection with matplotlib so the user can select it.
[register\_projection](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
([SkewXAxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

if \_\_name\_\_ \== '\_\_main\_\_':
    \# Now make a simple example using the custom projection.
    from io import [StringIO](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")

    import matplotlib.pyplot as plt
    import numpy as np

    from matplotlib.ticker import [MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
, [NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
, [ScalarFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")

    \# Some example data.
    [data\_txt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
        944.0    634    5.0   -2.0
        925.0    798    3.4   -2.6
        911.8    914    2.4   -2.7
        906.0    966    2.0   -2.7
        877.9   1219    0.4   -3.2
        850.0   1478   -1.3   -3.7
        841.0   1563   -1.9   -3.8
        823.0   1736    1.4   -0.7
        813.6   1829    4.5    1.2
        809.0   1875    6.0    2.2
        798.0   1988    7.4   -0.6
        791.0   2061    7.6   -1.4
        783.9   2134    7.0   -1.7
        755.1   2438    4.8   -3.1
        727.3   2743    2.5   -4.4
        700.5   3048    0.2   -5.8
        700.0   3054    0.2   -5.8
        698.0   3077    0.0   -6.0
        687.0   3204   -0.1   -7.1
        648.9   3658   -3.2  -10.9
        631.0   3881   -4.7  -12.7
        600.7   4267   -6.4  -16.7
        592.0   4381   -6.9  -17.9
        577.6   4572   -8.1  -19.6
        555.3   4877  -10.0  -22.3
        536.0   5151  -11.7  -24.7
        533.8   5182  -11.9  -25.0
        500.0   5680  -15.9  -29.9
        472.3   6096  -19.7  -33.4
        453.0   6401  -22.4  -36.0
        400.0   7310  -30.7  -43.7
        399.7   7315  -30.8  -43.8
        387.0   7543  -33.1  -46.1
        382.7   7620  -33.8  -46.8
        342.0   8398  -40.5  -53.5
        320.4   8839  -43.7  -56.7
        318.0   8890  -44.1  -57.1
        310.0   9060  -44.7  -58.7
        306.1   9144  -43.9  -57.9
        305.0   9169  -43.7  -57.7
        300.0   9280  -43.5  -57.5
        292.0   9462  -43.7  -58.7
        276.0   9838  -47.1  -62.1
        264.0  10132  -47.5  -62.5
        251.0  10464  -49.7  -64.7
        250.0  10490  -49.7  -64.7
        247.0  10569  -48.7  -63.7
        244.0  10649  -48.9  -63.9
        243.3  10668  -48.9  -63.9
        220.0  11327  -50.3  -65.3
        212.0  11569  -50.5  -65.5
        210.0  11631  -49.7  -64.7
        200.0  11950  -49.9  -64.9
        194.0  12149  -49.9  -64.9
        183.0  12529  -51.3  -66.3
        164.0  13233  -55.3  -68.3
        152.0  13716  -56.5  -69.5
        150.0  13800  -57.1  -70.1
        136.0  14414  -60.5  -72.5
        132.0  14600  -60.1  -72.1
        131.4  14630  -60.2  -72.2
        128.0  14792  -60.9  -72.9
        125.0  14939  -60.1  -72.1
        119.0  15240  -62.2  -73.8
        112.0  15616  -64.9  -75.9
        108.0  15838  -64.1  -75.1
        107.8  15850  -64.1  -75.1
        105.0  16010  -64.7  -75.7
        103.0  16128  -62.9  -73.9
        100.0  16310  -62.5  -73.5
    '''

    \# Parse the data
    sound\_data \= [StringIO](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
([data\_txt](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [p](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [h](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Td](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")
(sound\_data, unpack\=True)

    \# Create a new figure. The dimensions here give a good aspect ratio
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6.5875, 6.2125))
    ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='skewx')

    [plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)

    \# Plot the data using normal plotting functions, in this case using
    \# log scaling in Y, as dictated by the typical meteorological plot
    [ax.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy")
([T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [p](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='C3')
    [ax.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy")
([Td](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [p](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='C2')

    \# An example of a slanted line at constant X
    [l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(0, color\='C0')

    \# Disables the log-formatting that comes with semilogy
    [ax.yaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([ScalarFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
())
    [ax.yaxis.set\_minor\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(100, 1000, 10))
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(1050, 100)

    [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(10))
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-50, 50)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![skewt](https://matplotlib.org/stable/_images/sphx_glr_skewt_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
    
*   [`matplotlib.spines`](https://matplotlib.org/stable/api/spines_api.html#module-matplotlib.spines "matplotlib.spines")
    
*   [`matplotlib.spines.Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
    
*   [`matplotlib.spines.Spine.register_axis`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.register_axis "matplotlib.spines.Spine.register_axis")
    
*   [`matplotlib.projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
    
*   [`matplotlib.projections.register_projection`](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
    

[`Download Jupyter notebook: skewt.ipynb`](https://matplotlib.org/stable/_downloads/11cd5287e12be054c10233b646917055/skewt.ipynb)

[`Download Python source code: skewt.py`](https://matplotlib.org/stable/_downloads/9ef69631965afeca01de4c5ac9e56e25/skewt.py)

[`Download zipped: skewt.zip`](https://matplotlib.org/stable/_downloads/c64c16365eca07d0643aa9588e70e2ad/skewt.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)