[Skip to main content](https://matplotlib.org/stable/gallery/units/basic_units.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/units/basic_units.html#sphx-glr-download-gallery-units-basic-units-py)
 to download the full example code.

Basic units[#](https://matplotlib.org/stable/gallery/units/basic_units.html#basic-units "Link to this heading")

================================================================================================================

This file implements a units library that supports registering arbitrary units, conversions between units, and math with unitized data. This library also implements a Matplotlib unit converter and registers its units with Matplotlib. This library is used in the examples to demonstrate Matplotlib's unit support. It is only maintained for the purposes of building documentation and should never be used outside of the Matplotlib documentation.

import itertools
import math

from packaging.version import parse as parse\_version

import numpy as np

import matplotlib.ticker as ticker
import matplotlib.units as units

class ProxyDelegate:
    def \_\_init\_\_(self, fn\_name, proxy\_type):
        self.proxy\_type \= proxy\_type
        self.fn\_name \= fn\_name

    def \_\_get\_\_(self, obj, objtype\=None):
        return self.proxy\_type(self.fn\_name, obj)

class TaggedValueMeta(type):
    def \_\_init\_\_(self, name, bases, dict):
        for fn\_name in self.\_proxies:
            if not hasattr(self, fn\_name):
                setattr(self, fn\_name,
                        ProxyDelegate(fn\_name, self.\_proxies\[fn\_name\]))

class PassThroughProxy:
    def \_\_init\_\_(self, fn\_name, obj):
        self.fn\_name \= fn\_name
        self.target \= obj.proxy\_target

    def \_\_call\_\_(self, \*args):
        fn \= getattr(self.target, self.fn\_name)
        ret \= fn(\*args)
        return ret

class ConvertArgsProxy(PassThroughProxy):
    def \_\_init\_\_(self, fn\_name, obj):
        super().\_\_init\_\_(fn\_name, obj)
        self.unit \= obj.unit

    def \_\_call\_\_(self, \*args):
        converted\_args \= \[\]
        for a in args:
            try:
                converted\_args.append(a.convert\_to(self.unit))
            except AttributeError:
                converted\_args.append(TaggedValue(a, self.unit))
        converted\_args \= tuple(\[c.get\_value() for c in converted\_args\])
        return super().\_\_call\_\_(\*converted\_args)

class ConvertReturnProxy(PassThroughProxy):
    def \_\_init\_\_(self, fn\_name, obj):
        super().\_\_init\_\_(fn\_name, obj)
        self.unit \= obj.unit

    def \_\_call\_\_(self, \*args):
        ret \= super().\_\_call\_\_(\*args)
        return (NotImplemented if ret is NotImplemented
                else TaggedValue(ret, self.unit))

class ConvertAllProxy(PassThroughProxy):
    def \_\_init\_\_(self, fn\_name, obj):
        super().\_\_init\_\_(fn\_name, obj)
        self.unit \= obj.unit

    def \_\_call\_\_(self, \*args):
        converted\_args \= \[\]
        arg\_units \= \[self.unit\]
        for a in args:
            if hasattr(a, 'get\_unit') and not hasattr(a, 'convert\_to'):
                \# If this argument has a unit type but no conversion ability,
                \# this operation is prohibited.
                return NotImplemented

            if hasattr(a, 'convert\_to'):
                try:
                    a \= a.convert\_to(self.unit)
                except Exception:
                    pass
                arg\_units.append(a.get\_unit())
                converted\_args.append(a.get\_value())
            else:
                converted\_args.append(a)
                if hasattr(a, 'get\_unit'):
                    arg\_units.append(a.get\_unit())
                else:
                    arg\_units.append(None)
        converted\_args \= tuple(converted\_args)
        ret \= super().\_\_call\_\_(\*converted\_args)
        if ret is NotImplemented:
            return NotImplemented
        ret\_unit \= unit\_resolver(self.fn\_name, arg\_units)
        if ret\_unit is NotImplemented:
            return NotImplemented
        return TaggedValue(ret, ret\_unit)

class TaggedValue(metaclass\=[TaggedValueMeta](https://docs.python.org/3/library/functions.html#type "builtins.type")
):

    \_proxies \= {'\_\_add\_\_': ConvertAllProxy,
                '\_\_sub\_\_': ConvertAllProxy,
                '\_\_mul\_\_': ConvertAllProxy,
                '\_\_rmul\_\_': ConvertAllProxy,
                '\_\_cmp\_\_': ConvertAllProxy,
                '\_\_lt\_\_': ConvertAllProxy,
                '\_\_gt\_\_': ConvertAllProxy,
                '\_\_len\_\_': PassThroughProxy}

    def \_\_new\_\_(cls, value, unit):
        \# generate a new subclass for value
        value\_class \= type(value)
        try:
            subcls \= type(f'TaggedValue\_of\_{value\_class.\_\_name\_\_}',
                          (cls, value\_class), {})
            return object.\_\_new\_\_(subcls)
        except TypeError:
            return object.\_\_new\_\_(cls)

    def \_\_init\_\_(self, value, unit):
        self.value \= value
        self.unit \= unit
        self.proxy\_target \= self.value

    def \_\_copy\_\_(self):
        return TaggedValue(self.value, self.unit)

    def \_\_getattribute\_\_(self, name):
        if name.startswith('\_\_'):
            return object.\_\_getattribute\_\_(self, name)
        variable \= object.\_\_getattribute\_\_(self, 'value')
        if hasattr(variable, name) and name not in self.\_\_class\_\_.\_\_dict\_\_:
            return getattr(variable, name)
        return object.\_\_getattribute\_\_(self, name)

    def \_\_array\_\_(self, dtype\=object, copy\=False):
        return [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(self.value, dtype)

    def \_\_array\_wrap\_\_(self, array, context\=None, return\_scalar\=False):
        return TaggedValue(array, self.unit)

    def \_\_repr\_\_(self):
        return f'TaggedValue({self.value!r}, {self.unit!r})'

    def \_\_str\_\_(self):
        return f"{self.value} in {self.unit}"

    def \_\_len\_\_(self):
        return len(self.value)

    if parse\_version([np.\_\_version\_\_](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
) \>= parse\_version('1.20'):
        def \_\_getitem\_\_(self, key):
            return TaggedValue(self.value\[key\], self.unit)

    def \_\_iter\_\_(self):
        \# Return a generator expression rather than use \`yield\`, so that
        \# TypeError is raised by iter(self) if appropriate when checking for
        \# iterability.
        return (TaggedValue(inner, self.unit) for inner in self.value)

    def get\_compressed\_copy(self, mask):
        new\_value \= [np.ma.masked\_array](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
(self.value, mask\=mask).compressed()
        return TaggedValue(new\_value, self.unit)

    def convert\_to(self, unit):
        if unit \== self.unit or not unit:
            return self
        try:
            new\_value \= self.unit.convert\_value\_to(self.value, unit)
        except AttributeError:
            new\_value \= self
        return TaggedValue(new\_value, unit)

    def get\_value(self):
        return self.value

    def get\_unit(self):
        return self.unit

class BasicUnit:
    \# numpy scalars convert eager and np.float64(2) \* BasicUnit('cm')
    \# would thus return a numpy scalar. To avoid this, we increase the
    \# priority of the BasicUnit.
    \_\_array\_priority\_\_ \= [np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
(0).\_\_array\_priority\_\_ + 1

    def \_\_init\_\_(self, name, fullname\=None):
        self.name \= name
        if fullname is None:
            fullname \= name
        self.fullname \= fullname
        self.conversions \= dict()

    def \_\_repr\_\_(self):
        return f'BasicUnit({self.name})'

    def \_\_str\_\_(self):
        return self.fullname

    def \_\_call\_\_(self, value):
        return TaggedValue(value, self)

    def \_\_mul\_\_(self, rhs):
        value \= rhs
        unit \= self
        if hasattr(rhs, 'get\_unit'):
            value \= rhs.get\_value()
            unit \= rhs.get\_unit()
            unit \= unit\_resolver('\_\_mul\_\_', (self, unit))
        if unit is NotImplemented:
            return NotImplemented
        return TaggedValue(value, unit)

    def \_\_rmul\_\_(self, lhs):
        return self\*lhs

    def \_\_array\_wrap\_\_(self, array, context\=None, return\_scalar\=False):
        return TaggedValue(array, self)

    def \_\_array\_\_(self, t\=None, context\=None, copy\=False):
        ret \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(1)
        if t is not None:
            return ret.astype(t)
        else:
            return ret

    def add\_conversion\_factor(self, unit, factor):
        def convert(x):
            return x\*factor
        self.conversions\[unit\] \= convert

    def add\_conversion\_fn(self, unit, fn):
        self.conversions\[unit\] \= fn

    def get\_conversion\_fn(self, unit):
        return self.conversions\[unit\]

    def convert\_value\_to(self, value, unit):
        conversion\_fn \= self.conversions\[unit\]
        ret \= conversion\_fn(value)
        return ret

    def get\_unit(self):
        return self

class UnitResolver:
    def addition\_rule(self, [units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
):
        for unit\_1, unit\_2 in [itertools.pairwise](https://docs.python.org/3/library/itertools.html#itertools.pairwise "itertools.pairwise")
([units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
):
            if unit\_1 != unit\_2:
                return NotImplemented
        return [units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
\[0\]

    def multiplication\_rule(self, [units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
):
        non\_null \= \[u for u in [units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")\
 if u\]
        if len(non\_null) \> 1:
            return NotImplemented
        return non\_null\[0\]

    op\_dict \= {
        '\_\_mul\_\_': multiplication\_rule,
        '\_\_rmul\_\_': multiplication\_rule,
        '\_\_add\_\_': addition\_rule,
        '\_\_radd\_\_': addition\_rule,
        '\_\_sub\_\_': addition\_rule,
        '\_\_rsub\_\_': addition\_rule}

    def \_\_call\_\_(self, operation, [units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
):
        if operation not in self.op\_dict:
            return NotImplemented

        return self.op\_dict\[operation\](self, [units](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
)

unit\_resolver \= UnitResolver()

cm \= BasicUnit('cm', 'centimeters')
inch \= BasicUnit('inch', 'inches')
inch.add\_conversion\_factor(cm, 2.54)
cm.add\_conversion\_factor(inch, 1/2.54)

radians \= BasicUnit('rad', 'radians')
degrees \= BasicUnit('deg', 'degrees')
radians.add\_conversion\_factor(degrees, 180.0/[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
degrees.add\_conversion\_factor(radians, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/180.0)

secs \= BasicUnit('s', 'seconds')
hertz \= BasicUnit('Hz', 'Hertz')
minutes \= BasicUnit('min', 'minutes')

secs.add\_conversion\_fn(hertz, lambda x: 1./x)
secs.add\_conversion\_factor(minutes, 1/60.0)

\# radians formatting
def rad\_fn(x, pos\=None):
    if x \>= 0:
        n \= int((x / [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* 2.0 + 0.25)
    else:
        n \= int((x / [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
) \* 2.0 \- 0.25)

    if n \== 0:
        return '0'
    elif n \== 1:
        return r'$\\pi/2$'
    elif n \== 2:
        return r'$\\pi$'
    elif n \== \-1:
        return r'$-\\pi/2$'
    elif n \== \-2:
        return r'$-\\pi$'
    elif n % 2 \== 0:
        return fr'${n//2}\\pi$'
    else:
        return fr'${n}\\pi/2$'

class BasicUnitConverter([units.ConversionInterface](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
):
    @staticmethod
    def axisinfo(unit, axis):
        """Return AxisInfo instance for x and unit."""

        if unit \== radians:
            return [units.AxisInfo](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
(
                majloc\=[ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(base\=[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2),
                majfmt\=[ticker.FuncFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
(rad\_fn),
                label\=unit.fullname,
            )
        elif unit \== degrees:
            return [units.AxisInfo](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
(
                majloc\=[ticker.AutoLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator")
(),
                majfmt\=[ticker.FormatStrFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
(r'$%i^\\circ$'),
                label\=unit.fullname,
            )
        elif unit is not None:
            if hasattr(unit, 'fullname'):
                return [units.AxisInfo](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
(label\=unit.fullname)
            elif hasattr(unit, 'unit'):
                return [units.AxisInfo](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")
(label\=unit.unit.fullname)
        return None

    @staticmethod
    def convert(val, unit, axis):
        if [np.iterable](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "numpy.iterable")
(val):
            if isinstance(val, [np.ma.MaskedArray](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
):
                val \= val.astype(float).filled([np.nan](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
            out \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
(len(val))
            for i, thisval in enumerate(val):
                if [np.ma.is\_masked](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html#numpy.ma.is_masked "numpy.ma.is_masked")
(thisval):
                    out\[i\] \= [np.nan](https://docs.python.org/3/library/functions.html#float "builtins.float")
                else:
                    try:
                        out\[i\] \= thisval.convert\_to(unit).get\_value()
                    except AttributeError:
                        out\[i\] \= thisval
            return out
        if [np.ma.is\_masked](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_masked.html#numpy.ma.is_masked "numpy.ma.is_masked")
(val):
            return [np.nan](https://docs.python.org/3/library/functions.html#float "builtins.float")
        else:
            return val.convert\_to(unit).get\_value()

    @staticmethod
    def default\_units(x, axis):
        """Return the default unit for x or None."""
        if [np.iterable](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "numpy.iterable")
(x):
            for thisx in x:
                return thisx.unit
        return x.unit

def cos(x):
    if [np.iterable](https://numpy.org/doc/stable/reference/generated/numpy.iterable.html#numpy.iterable "numpy.iterable")
(x):
        return \[[math.cos](https://docs.python.org/3/library/math.html#math.cos "math.cos")\
(val.convert\_to(radians).get\_value()) for val in x\]
    else:
        return [math.cos](https://docs.python.org/3/library/math.html#math.cos "math.cos")
(x.convert\_to(radians).get\_value())

[units.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[BasicUnit\] \= [units.registry](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
\[TaggedValue\] \= [BasicUnitConverter](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
()

[`Download Jupyter notebook: basic_units.ipynb`](https://matplotlib.org/stable/_downloads/49240427aff1b343a7fb24df8f0f0f4e/basic_units.ipynb)

[`Download Python source code: basic_units.py`](https://matplotlib.org/stable/_downloads/0f0fd288c7d4a6a16f4835b96343f597/basic_units.py)

[`Download zipped: basic_units.zip`](https://matplotlib.org/stable/_downloads/884586c02a56e9e0fcc5b1cd890e7d63/basic_units.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)