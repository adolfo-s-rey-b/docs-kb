[Skip to main content](https://matplotlib.org/stable/gallery/units/evans_test.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/units/evans_test.html#sphx-glr-download-gallery-units-evans-test-py)
 to download the full example code.

Evans test[#](https://matplotlib.org/stable/gallery/units/evans_test.html#evans-test "Link to this heading")

=============================================================================================================

A mockup "Foo" units class which supports conversion and different tick formatting depending on the "unit". Here the "unit" is just a scalar conversion factor, but this example shows that Matplotlib is entirely agnostic to what kind of units client packages use.

![Custom units, default units, xunits = 2.0](https://matplotlib.org/stable/_images/sphx_glr_evans_test_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as ticker
import matplotlib.units as units

class Foo:
    def \_\_init\_\_(self, val, unit\=1.0):
        self.unit \= unit
        self.\_val \= val \* unit

    def value(self, unit):
        if unit is None:
            unit \= self.unit
        return self.\_val / unit

class FooConverter([units.ConversionInterface](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
):
    @staticmethod
    def axisinfo(unit, axis):
        """Return the Foo AxisInfo."""
        if unit \== 1.0 or unit \== 2.0:
            return [units.AxisInfo](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
(
                majloc\=[ticker.IndexLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator "matplotlib.ticker.IndexLocator")
(8, 0),
                majfmt\=[ticker.FormatStrFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
("VAL: %s"),
                label\='foo',
                )

        else:
            return None

    @staticmethod
    def convert(obj, unit, axis):
        """
        Convert \*obj\* using \*unit\*.

        If \*obj\* is a sequence, return the converted sequence.
        """
        if [np.iterable](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "numpy.iterable")
(obj):
            return \[o.value(unit) for o in obj\]
        else:
            return obj.value(unit)

    @staticmethod
    def default\_units([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, axis):
        """Return the default unit for \*x\* or None."""
        if [np.iterable](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "numpy.iterable")
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
            for thisx in [x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
                return thisx.unit
        else:
            return [x.unit](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

[units.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[Foo\] \= [FooConverter](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
()

\# create some Foos
[x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[Foo(val, 1.0) for val in range(0, 50, 2)\]
\# and some arbitrary y data
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[i for i in range(len([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
))\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Custom units")
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(bottom\=0.2)

\# plot specifying units
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'o', xunits\=2.0)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("xunits = 2.0")
[ax2.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='x', rotation\=30, rotation\_mode\='xtick')

\# plot without specifying units; will use the None branch for axisinfo
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)  \# uses default units
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('default units')
[ax1.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='x', rotation\=30, rotation\_mode\='xtick')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: evans_test.ipynb`](https://matplotlib.org/stable/_downloads/9ee6fa8ef30a30648a2c41743c24d783/evans_test.ipynb)

[`Download Python source code: evans_test.py`](https://matplotlib.org/stable/_downloads/dd53845e9b4ff2a1c978459bd05b003e/evans_test.py)

[`Download zipped: evans_test.zip`](https://matplotlib.org/stable/_downloads/bff637033ef05905fdbd57d7bf46714f/evans_test.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)