[Skip to main content](https://matplotlib.org/stable/gallery/scales/custom_scale.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/scales/custom_scale.html#sphx-glr-download-gallery-scales-custom-scale-py)
 to download the full example code.

Custom scale[#](https://matplotlib.org/stable/gallery/scales/custom_scale.html#custom-scale "Link to this heading")

====================================================================================================================

Custom scales can be created in two ways

1.  For simple cases, use [`FuncScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale "matplotlib.scale.FuncScale")
     and the `'function'` option of [`set_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
     and [`set_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
    . See the last example in [Scales overview](https://matplotlib.org/stable/gallery/scales/scales.html)
    .
    
2.  Create a custom scale class such as the one in this example, which implements the scaling use for latitude data in a Mercator Projection. This more complicated approach is useful when
    
    *   You are making special use of the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
         class, such as the special handling of values beyond the threshold in `MercatorLatitudeTransform` below.
        
    *   You want to override the default locators and formatters for the axis (`set_default_locators_and_formatters` below).
        
    *   You want to limit the range of the axis (`limit_range_for_scale` below).
        

![Mercator projection](https://matplotlib.org/stable/_images/sphx_glr_custom_scale_001_2_00x.png)

import numpy as np
from numpy import ma

from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib.ticker import [FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
, [FuncFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")

class MercatorLatitudeScale([mscale.ScaleBase](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
):
    """
    Scales data in range -pi/2 to pi/2 (-90 to 90 degrees) using
    the system used to scale latitudes in a Mercator\_\_ projection.

    The scale function:
      ln(tan(y) + sec(y))

    The inverse scale function:
      atan(sinh(y))

    Since the Mercator scale tends to infinity at +/- 90 degrees,
    there is user-defined threshold, above and below which nothing
    will be plotted.  This defaults to +/- 85 degrees.

    \_\_ https://en.wikipedia.org/wiki/Mercator\_projection
    """

    \# The scale class must have a member \`\`name\`\` that defines the string used
    \# to select the scale.  For example, \`\`ax.set\_yscale("mercator")\`\` would be
    \# used to select this scale.
    name \= 'mercator'

    def \_\_init\_\_(self, axis, \*, thresh\=[np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(85), \*\*kwargs):
        """
        Any keyword arguments passed to \`\`set\_xscale\`\` and \`\`set\_yscale\`\` will
        be passed along to the scale's constructor.

        thresh: The degree above which to crop the data.
        """
        super().\_\_init\_\_(axis)
        if thresh \>= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2:
            raise ValueError("thresh must be less than pi/2")
        self.thresh \= thresh

    def get\_transform(self):
        """
        Override this method to return a new instance that does the
        actual transformation of the data.

        The MercatorLatitudeTransform class is defined below as a
        nested class of this one.
        """
        return self.MercatorLatitudeTransform(self.thresh)

    def set\_default\_locators\_and\_formatters(self, axis):
        """
        Override to set up the locators and formatters to use with the
        scale.  This is only required if the scale requires custom
        locators and formatters.  Writing custom locators and
        formatters is rather outside the scope of this example, but
        there are many helpful examples in :mod:\`.ticker\`.

        In our case, the Mercator example uses a fixed locator from -90 to 90
        degrees and a custom formatter to convert the radians to degrees and
        put a degree symbol after the value.
        """
        fmt \= [FuncFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
(
            lambda x, pos\=None: f"{[np.degrees](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(x):.0f}\\N{DEGREE SIGN}")
        axis.set(major\_locator\=[FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([np.radians](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(range(\-90, 90, 10))),
                 major\_formatter\=fmt, minor\_formatter\=fmt)

    def limit\_range\_for\_scale(self, vmin, vmax, minpos):
        """
        Override to limit the bounds of the axis to the domain of the
        transform.  In the case of Mercator, the bounds should be
        limited to the threshold that was passed in.  Unlike the
        autoscaling provided by the tick locators, this range limiting
        will always be adhered to, whether the axis range is set
        manually, determined automatically or changed through panning
        and zooming.
        """
        return max(vmin, \-self.thresh), min(vmax, self.thresh)

    class MercatorLatitudeTransform([mtransforms.Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
):
        \# There are two value members that must be defined.
        \# \`\`input\_dims\`\` and \`\`output\_dims\`\` specify number of input
        \# dimensions and output dimensions to the transformation.
        \# These are used by the transformation framework to do some
        \# error checking and prevent incompatible transformations from
        \# being connected together.  When defining transforms for a
        \# scale, which are, by definition, separable and have only one
        \# dimension, these members should always be set to 1.
        input\_dims \= output\_dims \= 1

        def \_\_init\_\_(self, thresh):
            [mtransforms.Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
.\_\_init\_\_(self)
            self.thresh \= thresh

        def transform\_non\_affine(self, a):
            """
            This transform takes a numpy array and returns a transformed copy.
            Since the range of the Mercator scale is limited by the
            user-specified threshold, the input array must be masked to
            contain only valid values.  Matplotlib will handle masked arrays
            and remove the out-of-range data from the plot.  However, the
            returned array \*must\* have the same shape as the input array, since
            these values need to remain synchronized with values in the other
            dimension.
            """
            masked \= [ma.masked\_where](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")
((a < \-self.thresh) | (a \> self.thresh), a)
            if masked.mask.any():
                return ma.log([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return [np.log](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.tan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(a) + 1 / [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(a)))

        def inverted(self):
            """
            Override this method so Matplotlib knows how to get the
            inverse transform for this transform.
            """
            return [MercatorLatitudeScale.InvertedMercatorLatitudeTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
(
                self.thresh)

    class InvertedMercatorLatitudeTransform([mtransforms.Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
):
        input\_dims \= output\_dims \= 1

        def \_\_init\_\_(self, thresh):
            [mtransforms.Transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
.\_\_init\_\_(self)
            self.thresh \= thresh

        def transform\_non\_affine(self, a):
            return [np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.sinh](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(a))

        def inverted(self):
            return [MercatorLatitudeScale.MercatorLatitudeTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
(self.thresh)

\# Now that the Scale class has been defined, it must be registered so
\# that Matplotlib can find it.
[mscale.register\_scale](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "matplotlib.scale.register_scale")
([MercatorLatitudeScale](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
)

if \_\_name\_\_ \== '\_\_main\_\_':
    import matplotlib.pyplot as plt

    [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-180.0, 180.0, 0.1)
    [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.radians](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)/2.

    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, '-', lw\=2)
    [plt.yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")
('mercator')

    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
('Longitude')
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
('Latitude')
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Mercator projection')
    [plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.060 seconds)

[`Download Jupyter notebook: custom_scale.ipynb`](https://matplotlib.org/stable/_downloads/89bcffa85728ef8c09a8c94e84b43418/custom_scale.ipynb)

[`Download Python source code: custom_scale.py`](https://matplotlib.org/stable/_downloads/fa2e2df1666c376511e25ba972f9b06c/custom_scale.py)

[`Download zipped: custom_scale.zip`](https://matplotlib.org/stable/_downloads/85e2c82c745a6745fb44a4d85cc79905/custom_scale.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)