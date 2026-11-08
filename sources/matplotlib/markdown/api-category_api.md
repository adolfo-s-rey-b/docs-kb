[Skip to main content](https://matplotlib.org/stable/api/category_api.html#main-content)

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
    

`matplotlib.category`[#](https://matplotlib.org/stable/api/category_api.html#module-matplotlib.category "Link to this heading")

================================================================================================================================

Plotting of string "category" data: `plot(['d', 'f', 'a'], [1, 2, 3])` will plot three points with x-axis values of 'd', 'f', 'a'.

See [Plotting categorical variables](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html)
 for an example.

The module uses Matplotlib's [`matplotlib.units`](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
 mechanism to convert from strings to integers and provides a tick locator, a tick formatter, and the [`UnitData`](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.UnitData "matplotlib.category.UnitData")
 class that creates and stores the string-to-integer mapping.

class matplotlib.category.StrCategoryConverter[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L26-L116)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter "Link to this definition")

Bases: [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")

static axisinfo(_unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L61-L86)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter.axisinfo "Link to this definition")

Set the default axis ticks and labels.

Parameters:

**unit**[`UnitData`](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.UnitData "matplotlib.category.UnitData")

object string unit information for value

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

axis for which information is being set

Note

_axis_ is not used

Returns:

[`AxisInfo`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.AxisInfo "matplotlib.units.AxisInfo")

Information to support default tick labeling

static convert(_value_, _unit_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L27-L59)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter.convert "Link to this definition")

Convert strings in _value_ to floats using mapping information stored in the _unit_ object.

Parameters:

**value**str or iterable

Value or list of values to be converted.

**unit**[`UnitData`](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.UnitData "matplotlib.category.UnitData")

An object mapping strings to integers.

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

The axis on which the converted value is plotted.

Note

_axis_ is unused.

Returns:

float or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of float

static default\_units(_data_, _axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L88-L109)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter.default_units "Link to this definition")

Set and update the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 units.

Parameters:

**data**str or iterable of str

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")

axis on which the data is plotted

Returns:

[`UnitData`](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.UnitData "matplotlib.category.UnitData")

object storing string to integer mapping

class matplotlib.category.StrCategoryFormatter(_units\_mapping_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L139-L166)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

String representation of the data at every tick.

Parameters:

**units\_mapping**dict

Mapping of category names (str) to indices (int).

format\_ticks(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L154-L157)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryFormatter.format_ticks "Link to this definition")

Return the tick label strings for all _values_.

This is the public API for generating tick labels. It calls `set_locs` to configure context-dependent formatting state before delegating to `__call__` for each individual value.

The output may contain mathtext or LaTeX markup.

Use this method (rather than `__call__`) whenever formatting a complete set of tick values, so that formatters which need to see all tick locations (e.g. to determine precision, offsets, or which date components to display) can work correctly.

class matplotlib.category.StrCategoryLocator(_units\_mapping_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L119-L136)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Tick at every integer mapping of the string data.

Parameters:

**units\_mapping**dict

Mapping of category names (str) to indices (int).

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L134-L136)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.category.UnitData(_data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L169-L227)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.UnitData "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Create mapping between unique categorical values and integer ids.

Parameters:

**data**iterable

sequence of string values

update(_data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/category.py#L199-L227)
[#](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.UnitData.update "Link to this definition")

Map new values to integer identifiers.

Parameters:

**data**iterable of str or bytes

Raises:

TypeError

If elements in _data_ are neither str nor bytes.

On this page