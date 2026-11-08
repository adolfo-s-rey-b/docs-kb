[Skip to main content](https://matplotlib.org/stable/gallery/misc/custom_projection.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/custom_projection.html#sphx-glr-download-gallery-misc-custom-projection-py)
 to download the full example code.

Custom projection[#](https://matplotlib.org/stable/gallery/misc/custom_projection.html#custom-projection "Link to this heading")

=================================================================================================================================

Showcase Hammer projection by alleviating many features of Matplotlib.

![custom projection](https://matplotlib.org/stable/_images/sphx_glr_custom_projection_001_2_00x.png)

import numpy as np

import matplotlib
from matplotlib.axes import [Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
import matplotlib.axis as maxis
from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.projections import [register\_projection](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
import matplotlib.spines as mspines
from matplotlib.ticker import [FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
, [Formatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
, [NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
, [BboxTransformTo](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, [Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

[rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
 \= [matplotlib.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")

\# This example projection class is rather long, but it is designed to
\# illustrate many features, not all of which will be used every time.
\# It is also common to factor out a lot of these methods into common
\# code used by a number of projections with similar characteristics
\# (see geo.py).

class GeoAxes([Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    """
    An abstract base class for geographic projections
    """
    class ThetaFormatter([Formatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
):
        """
        Used to format the theta tick labels.  Converts the native
        unit of radians into degrees and adds a degree symbol.
        """
        def \_\_init\_\_(self, round\_to\=1.0):
            self.\_round\_to \= round\_to

        def \_\_call\_\_(self, x, pos\=None):
            degrees \= round([np.rad2deg](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x) / self.\_round\_to) \* self.\_round\_to
            return f"{degrees:0.0f}\\N{DEGREE SIGN}"

    RESOLUTION \= 75

    def \_init\_axis(self):
        self.xaxis \= [maxis.XAxis](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
(self)
        self.yaxis \= [maxis.YAxis](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")
(self)
        \# Do not register xaxis or yaxis with spines -- as done in
        \# Axes.\_init\_axis() -- until GeoAxes.xaxis.clear() works.
        \# self.spines\['geo'\].register\_axis(self.yaxis)

    def clear(self):
        \# docstring inherited
        super().clear()

        self.set\_longitude\_grid(30)
        self.set\_latitude\_grid(15)
        self.set\_longitude\_grid\_ends(75)
        self.xaxis.set\_minor\_locator([NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
        self.yaxis.set\_minor\_locator([NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
        self.xaxis.set\_ticks\_position('none')
        self.yaxis.set\_ticks\_position('none')
        self.yaxis.set\_tick\_params(label1On\=True)
        \# Why do we need to turn on yaxis tick labels, but
        \# xaxis tick labels are already on?

        self.grid([rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.grid'\])

        [Axes.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(self, \-[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
        [Axes.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(self, \-[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2.0, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2.0)

    def \_set\_lim\_and\_transforms(self):
        \# A (possibly non-linear) projection on the (already scaled) data

        \# There are three important coordinate spaces going on here:
        #
        \# 1. Data space: The space of the data itself
        #
        \# 2. Axes space: The unit rectangle (0, 0) to (1, 1)
        \#    covering the entire plot area.
        #
        \# 3. Display space: The coordinates of the resulting image,
        \#    often in pixels or dpi/inch.

        \# This function makes heavy use of the Transform classes in
        \# \`\`lib/matplotlib/transforms.py.\`\` For more information, see
        \# the inline documentation there.

        \# The goal of the first two transformations is to get from the
        \# data space (in this case longitude and latitude) to Axes
        \# space.  It is separated into a non-affine and affine part so
        \# that the non-affine part does not have to be recomputed when
        \# a simple affine change to the figure has been made (such as
        \# resizing the window or changing the dpi).

        \# 1) The core transformation from data space into
        \# rectilinear space defined in the HammerTransform class.
        self.transProjection \= self.\_get\_core\_transform(self.RESOLUTION)

        \# 2) The above has an output range that is not in the unit
        \# rectangle, so scale and translate it so it fits correctly
        \# within the Axes.  The peculiar calculations of xscale and
        \# yscale are specific to an Aitoff-Hammer projection, so don't
        \# worry about them too much.
        self.transAffine \= self.\_get\_affine\_transform()

        \# 3) This is the transformation from Axes space to display
        \# space.
        self.transAxes \= [BboxTransformTo](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
(self.bbox)

        \# Now put these 3 transforms together -- from data all the way
        \# to display coordinates.  Using the '+' operator, these
        \# transforms will be applied "in order".  The transforms are
        \# automatically simplified, if possible, by the underlying
        \# transformation framework.
        self.transData \= \\
            self.transProjection + \\
            self.transAffine + \\
            self.transAxes

        \# The main data transformation is set up.  Now deal with
        \# gridlines and tick labels.

        \# Longitude gridlines and ticklabels.  The input to these
        \# transforms are in display space in x and Axes space in y.
        \# Therefore, the input values will be in range (-xmin, 0),
        \# (xmax, 1).  The goal of these transforms is to go from that
        \# space to display space.  The tick labels will be offset 4
        \# pixels from the equator.
        self.\_xaxis\_pretransform \= \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
() \\
            .scale(1.0, self.\_longitude\_cap \* 2.0) \\
            .translate(0.0, \-self.\_longitude\_cap)
        self.\_xaxis\_transform \= \\
            self.\_xaxis\_pretransform + \\
            self.transData
        self.\_xaxis\_text1\_transform \= \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(1.0, 0.0) + \\
            self.transData + \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().translate(0.0, 4.0)
        self.\_xaxis\_text2\_transform \= \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(1.0, 0.0) + \\
            self.transData + \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().translate(0.0, \-4.0)

        \# Now set up the transforms for the latitude ticks.  The input to
        \# these transforms are in Axes space in x and display space in
        \# y.  Therefore, the input values will be in range (0, -ymin),
        \# (1, ymax).  The goal of these transforms is to go from that
        \# space to display space.  The tick labels will be offset 4
        \# pixels from the edge of the Axes ellipse.
        yaxis\_stretch \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*2, 1).translate(\-[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0)
        yaxis\_space \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(1.0, 1.1)
        self.\_yaxis\_transform \= \\
            yaxis\_stretch + \\
            self.transData
        yaxis\_text\_base \= \\
            yaxis\_stretch + \\
            self.transProjection + \\
            (yaxis\_space +
             self.transAffine +
             self.transAxes)
        self.\_yaxis\_text1\_transform \= \\
            yaxis\_text\_base + \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().translate(\-8.0, 0.0)
        self.\_yaxis\_text2\_transform \= \\
            yaxis\_text\_base + \\
            [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().translate(8.0, 0.0)

    def \_get\_affine\_transform(self):
        transform \= self.\_get\_core\_transform(1)
        xscale, \_ \= transform.transform(([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0))
        \_, yscale \= transform.transform((0, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2))
        return [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
() \\
            .scale(0.5 / xscale, 0.5 / yscale) \\
            .translate(0.5, 0.5)

    def get\_xaxis\_transform(self, which\='grid'):
        """
        Override this method to provide a transformation for the
        x-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """
        if which not in \['tick1', 'tick2', 'grid'\]:
            raise ValueError(
                "'which' must be one of 'tick1', 'tick2', or 'grid'")
        return self.\_xaxis\_transform

    def get\_xaxis\_text1\_transform(self, pad):
        return self.\_xaxis\_text1\_transform, 'bottom', 'center'

    def get\_xaxis\_text2\_transform(self, pad):
        """
        Override this method to provide a transformation for the
        secondary x-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """
        return self.\_xaxis\_text2\_transform, 'top', 'center'

    def get\_yaxis\_transform(self, which\='grid'):
        """
        Override this method to provide a transformation for the
        y-axis grid and ticks.
        """
        if which not in \['tick1', 'tick2', 'grid'\]:
            raise ValueError(
                "'which' must be one of 'tick1', 'tick2', or 'grid'")
        return self.\_yaxis\_transform

    def get\_yaxis\_text1\_transform(self, pad):
        """
        Override this method to provide a transformation for the
        y-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """
        return self.\_yaxis\_text1\_transform, 'center', 'right'

    def get\_yaxis\_text2\_transform(self, pad):
        """
        Override this method to provide a transformation for the
        secondary y-axis tick labels.

        Returns a tuple of the form (transform, valign, halign)
        """
        return self.\_yaxis\_text2\_transform, 'center', 'left'

    def \_gen\_axes\_patch(self):
        """
        Override this method to define the shape that is used for the
        background of the plot.  It should be a subclass of Patch.

        In this case, it is a Circle (that may be warped by the Axes
        transform into an ellipse).  Any data and gridlines will be
        clipped to this shape.
        """
        return [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((0.5, 0.5), 0.5)

    def \_gen\_axes\_spines(self):
        return {'geo': [mspines.Spine.circular\_spine](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.circular_spine "matplotlib.spines.Spine.circular_spine")
(self, (0.5, 0.5), 0.5)}

    def set\_yscale(self, \*args, \*\*kwargs):
        if args\[0\] != 'linear':
            raise NotImplementedError

    \# Prevent the user from applying scales to one or both of the
    \# axes.  In this particular case, scaling the axes wouldn't make
    \# sense, so we don't allow it.
    set\_xscale \= set\_yscale

    \# Prevent the user from changing the axes limits.  In our case, we
    \# want to display the whole sphere all the time, so we override
    \# set\_xlim and set\_ylim to ignore any input.  This also applies to
    \# interactive panning and zooming in the GUI interfaces.
    def set\_xlim(self, \*args, \*\*kwargs):
        raise TypeError("Changing axes limits of a geographic projection is "
                        "not supported.  Please consider using Cartopy.")

    set\_ylim \= set\_xlim

    def format\_coord(self, lon, lat):
        """
        Override this method to change how the values are displayed in
        the status bar.

        In this case, we want them to be displayed in degrees N/S/E/W.
        """
        lon, lat \= [np.rad2deg](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\[lon, lat\])
        ns \= 'N' if lat \>= 0.0 else 'S'
        ew \= 'E' if lon \>= 0.0 else 'W'
        return ('%f\\N{DEGREE SIGN}%s, %f\\N{DEGREE SIGN}%s'
                % (abs(lat), ns, abs(lon), ew))

    def set\_longitude\_grid(self, degrees):
        """
        Set the number of degrees between each longitude grid.

        This is an example method that is specific to this projection
        class -- it provides a more convenient interface to set the
        ticking than set\_xticks would.
        """
        \# Skip -180 and 180, which are the fixed limits.
        grid \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-180 + degrees, 180, degrees)
        self.xaxis.set\_major\_locator([FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(grid)))
        self.xaxis.set\_major\_formatter(self.ThetaFormatter(degrees))

    def set\_latitude\_grid(self, degrees):
        """
        Set the number of degrees between each longitude grid.

        This is an example method that is specific to this projection
        class -- it provides a more convenient interface than
        set\_yticks would.
        """
        \# Skip -90 and 90, which are the fixed limits.
        grid \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-90 + degrees, 90, degrees)
        self.yaxis.set\_major\_locator([FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(grid)))
        self.yaxis.set\_major\_formatter(self.ThetaFormatter(degrees))

    def set\_longitude\_grid\_ends(self, degrees):
        """
        Set the latitude(s) at which to stop drawing the longitude grids.

        Often, in geographic projections, you wouldn't want to draw
        longitude gridlines near the poles.  This allows the user to
        specify the degree at which to stop drawing longitude grids.

        This is an example method that is specific to this projection
        class -- it provides an interface to something that has no
        analogy in the base Axes class.
        """
        self.\_longitude\_cap \= [np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(degrees)
        self.\_xaxis\_pretransform \\
            .clear() \\
            .scale(1.0, self.\_longitude\_cap \* 2.0) \\
            .translate(0.0, \-self.\_longitude\_cap)

    def get\_data\_ratio(self):
        """
        Return the aspect ratio of the data itself.

        This method should be overridden by any Axes that have a
        fixed data ratio.
        """
        return 1.0

    \# Interactive panning and zooming is not supported with this projection,
    \# so we override all of the following methods to disable it.
    def can\_zoom(self):
        """
        Return whether this Axes supports the zoom box button functionality.

        This Axes object does not support interactive zoom box.
        """
        return False

    def can\_pan(self):
        """
        Return whether this Axes supports the pan/zoom button functionality.

        This Axes object does not support interactive pan/zoom.
        """
        return False

    def start\_pan(self, x, y, button):
        pass

    def end\_pan(self):
        pass

    def drag\_pan(self, button, key, x, y):
        pass

class HammerAxes([GeoAxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    """
    A custom class for the Aitoff-Hammer projection, an equal-area map
    projection.

    https://en.wikipedia.org/wiki/Hammer\_projection
    """

    \# The projection must specify a name. This will be used by the
    \# user to select the projection,
    \# i.e. \`\`subplot(projection='custom\_hammer')\`\`.
    name \= 'custom\_hammer'

    class HammerTransform([Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
):
        """The base Hammer transform."""
        input\_dims \= output\_dims \= 2

        def \_\_init\_\_(self, resolution):
            """
            Create a new Hammer transform.  Resolution is the number of steps
            to interpolate between each input line segment to approximate its
            path in curved Hammer space.
            """
            [Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
.\_\_init\_\_(self)
            self.\_resolution \= resolution

        def transform\_non\_affine(self, ll):
            longitude, latitude \= ll.T

            \# Pre-compute some values
            half\_long \= longitude / 2
            cos\_latitude \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(latitude)
            sqrt2 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2)

            alpha \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1 + cos\_latitude \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(half\_long))
            x \= (2 \* sqrt2) \* (cos\_latitude \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(half\_long)) / alpha
            y \= (sqrt2 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(latitude)) / alpha
            return [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[x, y\])

        def transform\_path\_non\_affine(self, path):
            \# vertices = path.vertices
            ipath \= path.interpolated(self.\_resolution)
            return [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(self.transform(ipath.vertices), ipath.codes)

        def inverted(self):
            return [HammerAxes.InvertedHammerTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
(self.\_resolution)

    class InvertedHammerTransform([Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
):
        input\_dims \= output\_dims \= 2

        def \_\_init\_\_(self, resolution):
            [Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
.\_\_init\_\_(self)
            self.\_resolution \= resolution

        def transform\_non\_affine(self, xy):
            x, y \= xy.T
            z \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1 \- (x / 4) \*\* 2 \- (y / 2) \*\* 2)
            longitude \= 2 \* [np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((z \* x) / (2 \* (2 \* z \*\* 2 \- 1)))
            latitude \= [np.arcsin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(y\*z)
            return [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[longitude, latitude\])

        def inverted(self):
            return [HammerAxes.HammerTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
(self.\_resolution)

    def \_\_init\_\_(self, \*args, \*\*kwargs):
        self.\_longitude\_cap \= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2.0
        super().\_\_init\_\_(\*args, \*\*kwargs)
        self.set\_aspect(0.5, adjustable\='box', anchor\='C')
        self.clear()

    def \_get\_core\_transform(self, resolution):
        return self.HammerTransform(resolution)

\# Now register the projection with Matplotlib so the user can select it.
[register\_projection](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
([HammerAxes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

if \_\_name\_\_ \== '\_\_main\_\_':
    import matplotlib.pyplot as plt

    \# Now make a simple example using the custom projection.
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\={'projection': 'custom\_hammer'})
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[\-1, 1, 1\], \[\-1, \-1, 1\], "o-")
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: custom_projection.ipynb`](https://matplotlib.org/stable/_downloads/f4e20d9bfc3857b25404515f8cd960d6/custom_projection.ipynb)

[`Download Python source code: custom_projection.py`](https://matplotlib.org/stable/_downloads/2de7d801cc807aadc92f195e3402760b/custom_projection.py)

[`Download zipped: custom_projection.zip`](https://matplotlib.org/stable/_downloads/a5505c1419535079af50e8100a25f56e/custom_projection.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)