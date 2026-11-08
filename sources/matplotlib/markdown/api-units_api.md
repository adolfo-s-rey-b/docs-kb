[Skip to main content](https://matplotlib.org/stable/api/units_api.html#main-content)

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
    

`matplotlib.units`[#](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "Link to this heading")

=======================================================================================================================

The classes here provide support for using custom classes with Matplotlib, e.g., those that do not expose the array interface but know how to convert themselves to arrays. It also supports classes with units and units conversion. Use cases include converters for custom objects, e.g., a list of datetime objects, as well as for objects that are unit aware. We don't assume any particular units implementation; rather a units implementation must register with the Registry converter dictionary and provide a [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
. For example, here is a complete implementation which supports plotting with native datetime objects:

import matplotlib.units as units
import matplotlib.dates as dates
import matplotlib.ticker as ticker
import datetime

class DateConverter(units.ConversionInterface):

    @staticmethod
    def convert(value, unit, axis):
        "Convert a datetime value to a scalar or array."
        return dates.date2num(value)

    @staticmethod
    def axisinfo(unit, axis):
        "Return major and minor tick locators and formatters."
        if unit != 'date':
            return None
        majloc \= dates.AutoDateLocator()
        majfmt \= dates.AutoDateFormatter(majloc)
        return units.AxisInfo(majloc\=majloc, majfmt\=majfmt, label\='date')

    @staticmethod
    def default\_units(x, axis):
        "Return the default unit for x or None."
        return 'date'

\# Finally we register our object type with the Matplotlib units registry.
units.registry\[datetime.date\] \= DateConverter()

class matplotlib.units.AxisInfo(_majloc\=None_, _minloc\=None_, _majfmt\=None_, _minfmt\=None_, _label\=None_, _default\_limits\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L72-L105)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Information to support default axis labeling, tick labeling, and limits.

An instance of this class must be returned by [`ConversionInterface.axisinfo`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface.axisinfo "matplotlib.units.ConversionInterface.axisinfo")
.

Parameters:

**majloc, minloc**Locator, optional

Tick locators for the major and minor ticks.

**majfmt, minfmt**Formatter, optional

Tick formatters for the major and minor ticks.

**label**str, optional

The default axis label.

**default\_limits**optional

The default min and max limits of the axis if no data has been plotted.

Notes

If any of the above are `None`, the axis will simply use the default value.

exception matplotlib.units.ConversionError[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L52-L53)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionError "Link to this definition")

Bases: [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")

class matplotlib.units.ConversionInterface[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L108-L132)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The minimal interface for a converter to take custom data types (or sequences) and convert them to values Matplotlib can use.

static axisinfo(_unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L114-L117)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface.axisinfo "Link to this definition")

Return an [`AxisInfo`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
 for the axis with the specified units.

static convert(_obj_, _unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L124-L132)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface.convert "Link to this definition")

Convert _obj_ using _unit_ for the specified _axis_.

If _obj_ is a sequence, return the converted sequence. The output must be a sequence of scalars that can be used by the numpy array layer.

static default\_units(_x_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L119-L122)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface.default_units "Link to this definition")

Return the default unit for _x_ or `None` for the given axis.

class matplotlib.units.DecimalConverter[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L135-L158)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.DecimalConverter "Link to this definition")

Bases: [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")

Converter for decimal.Decimal data to float.

static convert(_value_, _unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L138-L156)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.DecimalConverter.convert "Link to this definition")

Convert Decimals to floats.

The _unit_ and _axis_ arguments are not used.

Parameters:

**value**decimal.Decimal or iterable

Decimal or list of Decimal need to be converted

class matplotlib.units.Registry[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L161-L191)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "Link to this definition")

Bases: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

Register types with conversion interface.

get\_converter(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/units.py#L164-L191)
[#](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry.get_converter "Link to this definition")

Get the converter interface instance for _x_, or None.

On this page