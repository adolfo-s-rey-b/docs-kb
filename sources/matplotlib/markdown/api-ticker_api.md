[Skip to main content](https://matplotlib.org/stable/api/ticker_api.html#main-content)

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
    

`matplotlib.ticker`[#](https://matplotlib.org/stable/api/ticker_api.html#module-matplotlib.ticker "Link to this heading")

==========================================================================================================================

Tick locating and formatting[#](https://matplotlib.org/stable/api/ticker_api.html#tick-locating-and-formatting "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

This module contains classes for configuring tick locating and formatting. Generic tick locators and formatters are provided, as well as domain specific custom ones.

Although the locators know nothing about major or minor ticks, they are used by the Axis class to support major and minor tick locating and formatting.

### Tick locating[#](https://matplotlib.org/stable/api/ticker_api.html#locators "Link to this heading")

The Locator class is the base class for all tick locators. The locators handle autoscaling of the view limits based on the data limits, and the choosing of tick locations. A useful semi-automatic tick locator is [`MultipleLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
. It is initialized with a base, e.g., 10, and it picks axis limits and ticks that are multiples of that base.

The Locator subclasses defined here are:

|     |     |
| --- | --- |
| [`AutoLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator") | [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")<br> with simple defaults. This is the default tick locator for most plotting. |
| [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator") | Finds up to a max number of intervals with ticks at nice locations. |
| [`LinearLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator") | Space ticks evenly from min to max. |
| [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator") | Space ticks logarithmically from min to max. |
| [`MultipleLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator") | Ticks and range are a multiple of base; either integer or float. |
| [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator") | Tick locations are fixed. |
| [`IndexLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator "matplotlib.ticker.IndexLocator") | Locator for index plots (e.g., where `x = range(len(y))`). |
| [`NullLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator") | No ticks. |
| [`SymmetricalLogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator "matplotlib.ticker.SymmetricalLogLocator") | Locator for use with the symlog norm; works like [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")<br> for the part outside of the threshold and adds 0 if inside the limits. |
| [`AsinhLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator "matplotlib.ticker.AsinhLocator") | Locator for use with the asinh norm, attempting to space ticks approximately uniformly. |
| [`LogitLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator "matplotlib.ticker.LogitLocator") | Locator for logit scaling. |
| [`AutoMinorLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator") | Locator for minor ticks when the axis is linear and the major ticks are uniformly spaced. Subdivides the major tick interval into a specified number of minor intervals, defaulting to 4 or 5 depending on the major interval. |

There are a number of locators specialized for date locations - see the [`dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module.

You can define your own locator by deriving from Locator. You must override the `__call__` method, which returns a sequence of locations, and you will probably want to override the autoscale method to set the view limits from the data limits.

If you want to override the default locator, use one of the above or a custom locator and pass it to the x- or y-axis instance. The relevant methods are:

ax.xaxis.set\_major\_locator(xmajor\_locator)
ax.xaxis.set\_minor\_locator(xminor\_locator)
ax.yaxis.set\_major\_locator(ymajor\_locator)
ax.yaxis.set\_minor\_locator(yminor\_locator)

The default minor locator is [`NullLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
, i.e., no minor ticks on by default.

Note

[`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 instances should not be used with more than one [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 or [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. So instead of:

locator \= MultipleLocator(5)
ax.xaxis.set\_major\_locator(locator)
ax2.xaxis.set\_major\_locator(locator)

do the following instead:

ax.xaxis.set\_major\_locator(MultipleLocator(5))
ax2.xaxis.set\_major\_locator(MultipleLocator(5))

### Tick formatting[#](https://matplotlib.org/stable/api/ticker_api.html#tick-formatting "Link to this heading")

Tick formatting is controlled by classes derived from Formatter. The formatter operates on a single tick value and returns a string to the axis.

|     |     |
| --- | --- |
| [`NullFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter") | No labels on the ticks. |
| [`FixedFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter") | Set the strings manually for the labels. |
| [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter") | User defined function sets the labels. |
| [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter") | Use string [`format`](https://docs.python.org/3/library/functions.html#format "(in Python v3.14)")<br> method. |
| [`FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter") | Use an old-style sprintf format string. |
| [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter") | Default formatter for scalars: autopick the format string. |
| [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter") | Formatter for log axes. |
| [`LogFormatterExponent`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterExponent "matplotlib.ticker.LogFormatterExponent") | Format values for log axis using `exponent = log_base(value)`. |
| [`LogFormatterMathtext`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext") | Format values for log axis using `exponent = log_base(value)` using Math text. |
| [`LogFormatterSciNotation`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterSciNotation "matplotlib.ticker.LogFormatterSciNotation") | Format values for log axis using scientific notation. |
| [`LogitFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter "matplotlib.ticker.LogitFormatter") | Probability formatter. |
| [`EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter") | Format labels in engineering notation. |
| [`PercentFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter") | Format labels as a percentage. |

You can derive your own formatter from the Formatter base class by simply overriding the `__call__` method. The formatter class has access to the axis view and data limits.

To control the major and minor tick label formats, use one of the following methods:

ax.xaxis.set\_major\_formatter(xmajor\_formatter)
ax.xaxis.set\_minor\_formatter(xminor\_formatter)
ax.yaxis.set\_major\_formatter(ymajor\_formatter)
ax.yaxis.set\_minor\_formatter(yminor\_formatter)

In addition to a [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 instance, [`set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 and [`set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
 also accept a `str` or function. `str` input will be internally replaced with an autogenerated [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 with the input `str`. For function input, a [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
 with the input function will be generated and used.

See [Major and minor ticks](https://matplotlib.org/stable/gallery/ticks/major_minor_demo.html)
 for an example of setting major and minor ticks. See the [`matplotlib.dates`](https://matplotlib.org/stable/api/dates_api.html#module-matplotlib.dates "matplotlib.dates")
 module for more information and examples of using date locators and formatters.

class matplotlib.ticker.AsinhLocator(_linear\_width_, _numticks\=11_, _symthresh\=0.2_, _base\=10_, _subs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2790-L2879)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place ticks spaced evenly on an inverse-sinh scale.

Generally used with the [`AsinhScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.AsinhScale "matplotlib.scale.AsinhScale")
 class.

Note

This API is provisional and may be revised in the future based on early user feedback.

Parameters:

**linear\_width**float

The scale parameter defining the extent of the quasi-linear region.

**numticks**int, default: 11

The approximate number of major ticks that will fit along the entire axis

**symthresh**float, default: 0.2

The fractional threshold beneath which data which covers a range that is approximately symmetric about zero will have ticks that are exactly symmetric.

**base**int, default: 10

The number base used for rounding tick locations on a logarithmic scale. If this is less than one, then rounding is to the nearest integer multiple of powers of ten.

**subs**tuple, default: None

Multiples of the number base, typically used for the minor ticks, e.g. (2, 5) when base=10.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2844-L2851)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator.__call__ "Link to this definition")

Return the locations of the ticks.

set\_params(_numticks\=None_, _symthresh\=None_, _base\=None_, _subs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2832-L2842)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator.set_params "Link to this definition")

Set parameters within this locator.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2853-L2879)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.ticker.AutoLocator[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L3028-L3047)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "Link to this definition")

Bases: [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

Place evenly spaced ticks, with the step size and maximum number of ticks chosen automatically.

This is a subclass of [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
, with parameters _nbins = 'auto'_ and _steps = \[1, 2, 2.5, 5, 10\]_.

To know the values of the non-public parameters, please have a look to the defaults of [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
.

class matplotlib.ticker.AutoMinorLocator(_n\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L3050-L3110)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place evenly spaced minor ticks, with the step size and maximum number of ticks chosen automatically.

The Axis must use a linear scale and have evenly spaced major ticks.

Parameters:

**n**int or 'auto', default: `[rcParams["xtick.minor.ndivs"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.minor.ndivs#rcparam-xtick-minor-ndivs) ` (default: `'auto'`) or `[rcParams["ytick.minor.ndivs"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.minor.ndivs#rcparam-ytick-minor-ndivs) ` (default: `'auto'`)

The number of subdivisions of the interval between major ticks; e.g., n=2 will place a single minor tick midway between major ticks.

If _n_ is 'auto', it will be set to 4 or 5: if the distance between the major ticks equals 1, 2.5, 5 or 10 it can be perfectly divided in 5 equidistant sub-intervals with a length multiple of 0.05; otherwise, it is divided in 4 sub-intervals.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L3073-L3106)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator.__call__ "Link to this definition")

Return the locations of the ticks.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L3108-L3110)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.ticker.EngFormatter(_unit\=''_, _places\=None_, _sep\=' '_, _\*_, _usetex\=None_, _useMathText\=None_, _useOffset\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1404-L1604)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "Link to this definition")

Bases: [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")

Format axis values using engineering prefixes to represent powers of 1000, plus a specified unit, e.g., 10 MHz instead of 1e7.

Parameters:

**unit**str, default: ""

Unit symbol to use, suitable for use with single-letter representations of powers of 1000. For example, 'Hz' or 'm'.

**places**int, default: None

Precision with which to display the number, specified in digits after the decimal point (there will be between one and three digits before the decimal point). If it is None, the formatting falls back to the floating point format '%g', which displays up to 6 _significant_ digits, i.e. the equivalent value for _places_ varies between 0 and 5 (inclusive).

**sep**str, default: " "

Separator used between the value and the prefix/unit. For example, one get '3.14 mV' if `sep` is " " (default) and '3.14mV' if `sep` is "". Besides the default behavior, some other useful options may be:

*   `sep=""` to append directly the prefix/unit to the value;
    
*   `sep="\N{THIN SPACE}"` (`U+2009`);
    
*   `sep="\N{NARROW NO-BREAK SPACE}"` (`U+202F`);
    
*   `sep="\N{NO-BREAK SPACE}"` (`U+00A0`).
    

**usetex**bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)

To enable/disable the use of TeX's math mode for rendering the numbers in the formatter.

**useMathText**bool, default: `[rcParams["axes.formatter.use_mathtext"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_mathtext#rcparam-axes-formatter-use-mathtext) ` (default: `False`)

To enable/disable the use mathtext for rendering the numbers in the formatter.

**useOffset**bool or float, default: False

Whether to use offset notation with \\(10^{3\*N}\\) based prefixes. This features allows showing an offset with standard SI order of magnitude prefix near the axis. Offset is computed similarly to how [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 computes it internally, but here you are guaranteed to get an offset which will make the tick labels exceed 3 digits. See also [`set_useOffset`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useOffset "matplotlib.ticker.ScalarFormatter.set_useOffset")
.

Added in version 3.10.

ENG\_PREFIXES \= {-30: 'q', \-27: 'r', \-24: 'y', \-21: 'z', \-18: 'a', \-15: 'f', \-12: 'p', \-9: 'n', \-6: 'µ', \-3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y', 27: 'R', 30: 'Q'}[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter.ENG_PREFIXES "Link to this definition")

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1490-L1503)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter.__call__ "Link to this definition")

Return the format for tick value _x_ at position _pos_.

If there is no currently offset in the data, it returns the best engineering formatting that fits the given argument, independently.

format\_data(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1554-L1604)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter.format_data "Link to this definition")

Format a number in engineering notation, appending a letter representing the power of 1000 of the original number. Some examples:

\>>> format\_data(0)        \# for self.places = 0
'0'

\>>> format\_data(1000000)  \# for self.places = 1
'1.0 M'

\>>> format\_data(\-1e-6)  \# for self.places = 2
'-1.00 µ'

format\_eng(_num_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1550-L1552)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter.format_eng "Link to this definition")

Alias to EngFormatter.format\_data

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1530-L1548)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter.get_offset "Link to this definition")

Return scientific notation, plus offset.

set\_locs(_locs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1505-L1523)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter.set_locs "Link to this definition")

Set the locations of the ticks.

This method is called before computing the tick labels because some formatters need to know all tick locations to do so.

class matplotlib.ticker.FixedFormatter(_seq_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L325-L356)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Return fixed strings for tick labels based only on position, not value.

Note

[`FixedFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
 should only be used together with [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
. Otherwise, the labels may end up in unexpected positions.

Set the sequence _seq_ of strings that will be used for labels.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L339-L350)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter.__call__ "Link to this definition")

Return the label that matches the position, regardless of the value.

For positions `pos < len(seq)`, return `seq[i]` regardless of _x_. Otherwise return empty string. `seq` is the sequence of strings that this object was initialized with.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L352-L353)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter.get_offset "Link to this definition")

set\_offset\_string(_ofs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L355-L356)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter.set_offset_string "Link to this definition")

class matplotlib.ticker.FixedLocator(_locs_, _nbins\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1840-L1880)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place ticks at a set of fixed values.

If _nbins_ is None ticks are placed at all values. Otherwise, the _locs_ array of possible positions will be subsampled to keep the number of ticks \\(\\leq nbins + 1\\). The subsampling will be done to include the smallest absolute value; for example, if zero is included in the array of possibilities, then it will be included in the chosen ticks.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1861-L1862)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator.__call__ "Link to this definition")

Return the locations of the ticks.

set\_params(_nbins\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1856-L1859)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator.set_params "Link to this definition")

Set parameters within this locator.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1864-L1880)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator.tick_values "Link to this definition")

Return the locations of the ticks.

Note

Because the values are fixed, _vmin_ and _vmax_ are not used.

class matplotlib.ticker.FormatStrFormatter(_fmt_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L387-L408)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Use an old-style ('%' operator) format string to format the tick.

The format string should have a single variable format (%) in it. It will be applied to the value (not the position) of the tick.

Negative numeric values (e.g., -1) will use a dash, not a Unicode minus; use mathtext to get a Unicode minus by wrapping the format specifier with $ (e.g. "$%g$").

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L402-L408)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter.__call__ "Link to this definition")

Return the formatted label string.

Only the value _x_ is formatted. The position is ignored.

class matplotlib.ticker.Formatter[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L199-L314)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "Link to this definition")

Bases: [`TickHelper`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper "matplotlib.ticker.TickHelper")

Create a string based on a tick value and location.

The Formatter provides four formatting methods for different use cases:

*   [`format_ticks`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_ticks "matplotlib.ticker.Formatter.format_ticks")
    : The public API for generating tick labels from a set of tick values.
    
*   [`__call__`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.__call__ "matplotlib.ticker.Formatter.__call__")
    : The low-level primitive for formatting a single tick value, potentially in the context of multiple values.
    
*   [`format_data`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "matplotlib.ticker.Formatter.format_data")
    : Context-independent representation of a single value. Used internally, e.g. for offset and scientific-notation strings.
    
*   [`format_data_short`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data_short "matplotlib.ticker.Formatter.format_data_short")
    : Concise plain-text representation of a single value for the interactive mouseover tooltip.
    

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L220-L237)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.__call__ "Link to this definition")

Return the tick label strings for value _x_ at tick index _pos_.

This is the low-level formatting primitive for a single tick in the context of multiple ticks. Any context-dependent state (e.g. locs, offset, order of magnitude) must already be configured, typically by a prior call to `format_ticks` or `set_locs`.

_pos_ defines the index into `self.locs` so that the format can depend on the location. `pos=None` indicates an unspecified location.

The output may contain mathtext or LaTeX markup.

Subclasses must override this method.

static fix\_minus(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L300-L310)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.fix_minus "Link to this definition")

Some classes may want to replace a hyphen for minus with the proper Unicode symbol (U+2212) for typographical correctness. This is a helper method to perform such a replacement when it is enabled via `[rcParams["axes.unicode_minus"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.unicode_minus#rcparam-axes-unicode-minus) ` (default: `True`).

format\_data(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L257-L268)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "Link to this definition")

Return the context-independent string representation of a single _value_.

This is used internally, e.g. for constructing offset and scientific-notation strings. It always formats with `pos=None` and should return a context-independent representation rather than a concise tick label.

The output may contain mathtext or LaTeX markup.

format\_data\_short(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L270-L286)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data_short "Link to this definition")

Return a short string representation of _value_ for the mouseover tooltip (the coordinate display in the interactive figure window).

This should return concise, plain text (no mathtext / LaTeX). The precision is typically adapted to the current axis resolution so that neighbouring pixels produce distinguishable labels.

Defaults to [`Formatter.format_data`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "matplotlib.ticker.Formatter.format_data")
; subclasses should override this to provide a plain-text representation that is independent of the current tick locations.

Note: The mouseover text can be customized by setting the `Axes.fmt_xdata` and `Axes.fmt_ydata` attributes.

format\_ticks(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L239-L255)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_ticks "Link to this definition")

Return the tick label strings for all _values_.

This is the public API for generating tick labels. It calls `set_locs` to configure context-dependent formatting state before delegating to `__call__` for each individual value.

The output may contain mathtext or LaTeX markup.

Use this method (rather than `__call__`) whenever formatting a complete set of tick values, so that formatters which need to see all tick locations (e.g. to determine precision, offsets, or which date components to display) can work correctly.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L288-L289)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.get_offset "Link to this definition")

property locs[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.locs "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

set\_locs(_locs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L291-L298)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.set_locs "Link to this definition")

Set the locations of the ticks.

This method is called before computing the tick labels because some formatters need to know all tick locations to do so.

class matplotlib.ticker.FuncFormatter(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L359-L384)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Use a user-defined function for formatting.

The function should take in two inputs (a tick value `x` and a position `pos`), and return a string containing the corresponding tick label.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L372-L378)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter.__call__ "Link to this definition")

Return the value of the user defined function.

_x_ and _pos_ are passed through as-is.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L380-L381)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter.get_offset "Link to this definition")

set\_offset\_string(_ofs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L383-L384)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter.set_offset_string "Link to this definition")

class matplotlib.ticker.IndexLocator(_base_, _offset_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1807-L1837)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place ticks at every nth point plotted.

IndexLocator assumes index plotting; i.e., that the ticks are placed at integer values in the range between 0 and len(data) inclusive.

Place ticks every _base_ data point, starting at _offset_.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1827-L1830)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator.__call__ "Link to this definition")

Return the locations of the ticks

set\_params(_base\=None_, _offset\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1820-L1825)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator.set_params "Link to this definition")

Set parameters within this locator

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1832-L1837)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.ticker.LinearLocator(_numticks\=None_, _presets\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1902-L1979)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place ticks at evenly spaced values.

The first time this function is called, it will try to set the number of ticks to make a nice tick partitioning. Thereafter, the number of ticks will be fixed to avoid jumping during interactive navigation.

Parameters:

**numticks**int or None, default None

Number of ticks. If None, _numticks_ = 11.

**presets**dict or None, default: None

Dictionary mapping `(vmin, vmax)` to an array of locations. Overrides _numticks_ if there is an entry for the current `(vmin, vmax)`.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1944-L1947)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator.__call__ "Link to this definition")

Return the locations of the ticks.

property numticks[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator.numticks "Link to this definition")

set\_params(_numticks\=None_, _presets\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1937-L1942)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator.set_params "Link to this definition")

Set parameters within this locator.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1949-L1959)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1961-L1979)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator.view_limits "Link to this definition")

Try to choose the view limits intelligently.

class matplotlib.ticker.Locator[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1717-L1804)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "Link to this definition")

Bases: [`TickHelper`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper "matplotlib.ticker.TickHelper")

Determine tick locations.

Note that the same locator should not be used across multiple [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 because the locator stores references to the Axis data and view limits.

MAXTICKS \= 1000[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.MAXTICKS "Link to this definition")

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1758-L1762)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.__call__ "Link to this definition")

Return the locations of the ticks.

nonsingular(_v0_, _v1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1782-L1796)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.nonsingular "Link to this definition")

Adjust a range as needed to avoid singularities.

This method gets called during autoscaling, with `(v0, v1)` set to the data limits on the Axes if the Axes contains any data, or `(-inf, +inf)` if not.

*   If `v0 == v1` (possibly up to some floating point slop), this method returns an expanded interval around this value.
    
*   If `(v0, v1) == (-inf, +inf)`, this method returns appropriate default view limits.
    
*   Otherwise, `(v0, v1)` is returned without modification.
    

raise\_if\_exceeds(_locs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1764-L1780)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.raise_if_exceeds "Link to this definition")

Log at WARNING level if _locs_ is longer than [`Locator.MAXTICKS`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.MAXTICKS "matplotlib.ticker.Locator.MAXTICKS")
.

This is intended to be called immediately before returning _locs_ from `__call__` to inform users in case their Locator returns a huge number of ticks, causing Matplotlib to run out of memory.

The "strange" name of this method dates back to when it would raise an exception instead of emitting a log.

set\_params(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1749-L1756)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.set_params "Link to this definition")

Do nothing, and raise a warning. Any locator class not supporting the set\_params() function will call this.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1732-L1747)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1798-L1804)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.view_limits "Link to this definition")

Select a scale for the range from vmin to vmax.

Subclasses should override this method to change locator behaviour.

class matplotlib.ticker.LogFormatter(_base\=10.0_, _labelOnlyBase\=False_, _minor\_thresholds\=None_, _linthresh\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L911-L1127)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Base class for formatting ticks on a log or symlog scale.

It may be instantiated directly, or subclassed.

Parameters:

**base**float, default: 10.

Base of the logarithm used in all calculations.

**labelOnlyBase**bool, default: False

If True, label ticks only at integer powers of base. This is normally True for major ticks and False for minor ticks.

**minor\_thresholds**(subset, all), default: (1, 0.4)

If labelOnlyBase is False, these two numbers control the labeling of ticks that are not at integer powers of base; normally these are the minor ticks.

The first number (_subset_) is the largest number of major ticks for which minor ticks are labeled; e.g., the default, 1, means that minor ticks are labeled as long as there is no more than 1 major tick. (It is assumed that major ticks are at integer powers of _base_.)

The second number (_all_) is a threshold, in log-units of the axis limit range, over which only a subset of the minor ticks are labeled, so as to avoid crowding; e.g., with the default value (0.4) and the usual `base=10`, all minor ticks are shown only if the axis limit range spans less than 0.4 decades.

**linthresh**None or float, default: None

If a symmetric log scale is in use, its `linthresh` parameter must be supplied here.

Notes

The [`set_locs`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.set_locs "matplotlib.ticker.LogFormatter.set_locs")
 method must be called to enable the subsetting logic controlled by the `minor_thresholds` parameter.

In some cases such as the colorbar, there is no distinction between major and minor ticks; the tick locations might be set manually, or by a locator that puts ticks at integer powers of base and at intermediate locations. For this situation, disable the minor\_thresholds logic by using `minor_thresholds=(np.inf, np.inf)`, so that all ticks will be labeled.

To disable labeling of minor ticks when 'labelOnlyBase' is False, use `minor_thresholds=(0, 0)`. This is the default for the "classic" style.

Examples

To label a subset of minor ticks when there are up to 2 major ticks, and all of the ticks when zoomed in to 0.5 decades or less, use `minor_thresholds=(2, 0.5)`.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1076-L1097)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.__call__ "Link to this definition")

Return the tick label strings for value _x_ at tick index _pos_.

This is the low-level formatting primitive for a single tick in the context of multiple ticks. Any context-dependent state (e.g. locs, offset, order of magnitude) must already be configured, typically by a prior call to `format_ticks` or `set_locs`.

_pos_ defines the index into `self.locs` so that the format can depend on the location. `pos=None` indicates an unspecified location.

The output may contain mathtext or LaTeX markup.

Subclasses must override this method.

format\_data(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1099-L1101)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.format_data "Link to this definition")

Return the context-independent string representation of a single _value_.

This is used internally, e.g. for constructing offset and scientific-notation strings. It always formats with `pos=None` and should return a context-independent representation rather than a concise tick label.

The output may contain mathtext or LaTeX markup.

format\_data\_short(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1103-L1105)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.format_data_short "Link to this definition")

Return a short string representation of _value_ for the mouseover tooltip (the coordinate display in the interactive figure window).

This should return concise, plain text (no mathtext / LaTeX). The precision is typically adapted to the current axis resolution so that neighbouring pixels produce distinguishable labels.

Defaults to [`Formatter.format_data`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "matplotlib.ticker.Formatter.format_data")
; subclasses should override this to provide a plain-text representation that is independent of the current tick locations.

Note: The mouseover text can be customized by setting the `Axes.fmt_xdata` and `Axes.fmt_ydata` attributes.

set\_base(_base_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L984-L991)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.set_base "Link to this definition")

Change the _base_ for labeling.

Warning

Should always match the base used for [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")

set\_label\_minor(_labelOnlyBase_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L993-L1002)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.set_label_minor "Link to this definition")

Switch minor tick labeling on or off.

Parameters:

**labelOnlyBase**bool

If True, label ticks only at integer powers of base.

set\_locs(_locs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1004-L1071)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter.set_locs "Link to this definition")

Use axis view limits to control which ticks are labeled.

The _locs_ parameter is ignored in the present algorithm.

class matplotlib.ticker.LogFormatterExponent(_base\=10.0_, _labelOnlyBase\=False_, _minor\_thresholds\=None_, _linthresh\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1130-L1142)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterExponent "Link to this definition")

Bases: [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")

Format values for log axis using `exponent = log_base(value)`.

class matplotlib.ticker.LogFormatterMathtext(_base\=10.0_, _labelOnlyBase\=False_, _minor\_thresholds\=None_, _linthresh\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1145-L1189)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "Link to this definition")

Bases: [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")

Format values for log axis using `exponent = log_base(value)`.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1154-L1189)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext.__call__ "Link to this definition")

Return the tick label strings for value _x_ at tick index _pos_.

This is the low-level formatting primitive for a single tick in the context of multiple ticks. Any context-dependent state (e.g. locs, offset, order of magnitude) must already be configured, typically by a prior call to `format_ticks` or `set_locs`.

_pos_ defines the index into `self.locs` so that the format can depend on the location. `pos=None` indicates an unspecified location.

The output may contain mathtext or LaTeX markup.

Subclasses must override this method.

class matplotlib.ticker.LogFormatterSciNotation(_base\=10.0_, _labelOnlyBase\=False_, _minor\_thresholds\=None_, _linthresh\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1192-L1205)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterSciNotation "Link to this definition")

Bases: [`LogFormatterMathtext`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")

Format values following scientific notation in a logarithmic axis.

class matplotlib.ticker.LogLocator(_base\=10.0_, _subs\=(1.0,)_, _\*_, _numticks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2399-L2633)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place logarithmically spaced ticks.

Places ticks at the values `subs[j] * base**i`.

Parameters:

**base**float, default: 10.0

The base of the log used, so major ticks are placed at `base**n`, where `n` is an integer.

**subs**None or {'auto', 'all'} or sequence of float, default: (1.0,)

Gives the multiples of integer powers of the base at which to place ticks. The default of `(1.0, )` places ticks only at integer powers of the base. Permitted string values are `'auto'` and `'all'`. Both of these use an algorithm based on the axis view limits to determine whether and how to put ticks between integer powers of the base: - `'auto'`: Ticks are placed only between integer powers. - `'all'`: Ticks are placed between _and_ at integer powers. - `None`: Equivalent to `'auto'`.

**numticks**None or int, default: None

The maximum number of ticks to allow on a given axis. The default of `None` will try to choose intelligently as long as this Locator has already been assigned to an axis using [`get_tick_space`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_space.html#matplotlib.axis.Axis.get_tick_space "matplotlib.axis.Axis.get_tick_space")
, but otherwise falls back to 9.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2467-L2470)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator.__call__ "Link to this definition")

Return the locations of the ticks.

nonsingular(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2613-L2633)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator.nonsingular "Link to this definition")

Adjust a range as needed to avoid singularities.

This method gets called during autoscaling, with `(v0, v1)` set to the data limits on the Axes if the Axes contains any data, or `(-inf, +inf)` if not.

*   If `v0 == v1` (possibly up to some floating point slop), this method returns an expanded interval around this value.
    
*   If `(v0, v1) == (-inf, +inf)`, this method returns appropriate default view limits.
    
*   Otherwise, `(v0, v1)` is returned without modification.
    

set\_params(_base\=None_, _subs\=None_, _\*_, _numticks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2437-L2444)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator.set_params "Link to this definition")

Set parameters within this locator.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2480-L2599)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2601-L2611)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator.view_limits "Link to this definition")

Try to choose the view limits intelligently.

class matplotlib.ticker.LogitFormatter(_\*_, _use\_overline\=False_, _one\_half\='\\\\frac{1}{2}'_, _minor\=False_, _minor\_threshold\=25_, _minor\_number\=6_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1208-L1401)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Probability formatter (using Math text).

Parameters:

**use\_overline**bool, default: False

If x > 1/2, with x = 1 - v, indicate if x should be displayed as $overline{v}$. The default is to display $1 - v$.

**one\_half**str, default: r"\\frac{1}{2}"

The string used to represent 1/2.

**minor**bool, default: False

Indicate if the formatter is formatting minor ticks or not. Basically minor ticks are not labelled, except when only few ticks are provided, ticks with most space with neighbor ticks are labelled. See other parameters to change the default behavior.

**minor\_threshold**int, default: 25

Maximum number of locs for labelling some minor ticks. This parameter have no effect if minor is False.

**minor\_number**int, default: 6

Number of ticks which are labelled when the number of ticks is below the threshold.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1373-L1392)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.__call__ "Link to this definition")

Return the tick label strings for value _x_ at tick index _pos_.

This is the low-level formatting primitive for a single tick in the context of multiple ticks. Any context-dependent state (e.g. locs, offset, order of magnitude) must already be configured, typically by a prior call to `format_ticks` or `set_locs`.

_pos_ defines the index into `self.locs` so that the format can depend on the location. `pos=None` indicates an unspecified location.

The output may contain mathtext or LaTeX markup.

Subclasses must override this method.

format\_data\_short(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1394-L1401)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.format_data_short "Link to this definition")

Return a short string representation of _value_ for the mouseover tooltip (the coordinate display in the interactive figure window).

This should return concise, plain text (no mathtext / LaTeX). The precision is typically adapted to the current axis resolution so that neighbouring pixels produce distinguishable labels.

Defaults to [`Formatter.format_data`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "matplotlib.ticker.Formatter.format_data")
; subclasses should override this to provide a plain-text representation that is independent of the current tick locations.

Note: The mouseover text can be customized by setting the `Axes.fmt_xdata` and `Axes.fmt_ydata` attributes.

set\_locs(_locs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1299-L1339)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.set_locs "Link to this definition")

Set the locations of the ticks.

This method is called before computing the tick labels because some formatters need to know all tick locations to do so.

set\_minor\_number(_minor\_number_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1286-L1297)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.set_minor_number "Link to this definition")

Set the number of minor ticks to label when some minor ticks are labelled.

Parameters:

**minor\_number**int

Number of ticks which are labelled when the number of ticks is below the threshold.

set\_minor\_threshold(_minor\_threshold_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1274-L1284)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.set_minor_threshold "Link to this definition")

Set the threshold for labelling minors ticks.

Parameters:

**minor\_threshold**int

Maximum number of locations for labelling some minor ticks. This parameter have no effect if minor is False.

set\_one\_half(_one\_half_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1265-L1272)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.set_one_half "Link to this definition")

Set the way one half is displayed.

one\_halfstr

The string used to represent 1/2.

use\_overline(_use\_overline_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1253-L1263)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitFormatter.use_overline "Link to this definition")

Switch display mode with overline for labelling p>1/2.

Parameters:

**use\_overline**bool

If x > 1/2, with x = 1 - v, indicate if x should be displayed as $overline{v}$. The default is to display $1 - v$.

class matplotlib.ticker.LogitLocator(_minor\=False_, _\*_, _nbins\='auto'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2882-L3025)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator "Link to this definition")

Bases: [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

Place ticks spaced evenly on a logit scale.

Parameters:

**nbins**int or 'auto', optional

Number of ticks. Only used if minor is False.

**minor**bool, default: False

Indicate if this locator is for minor ticks or not.

property minor[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator.minor "Link to this definition")

nonsingular(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2991-L3025)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator.nonsingular "Link to this definition")

Adjust a range as needed to avoid singularities.

This method gets called during autoscaling, with `(v0, v1)` set to the data limits on the Axes if the Axes contains any data, or `(-inf, +inf)` if not.

*   If `v0 == v1` (possibly up to some floating point slop), this method returns an expanded interval around this value.
    
*   If `(v0, v1) == (-inf, +inf)`, this method returns appropriate default view limits.
    
*   Otherwise, `(v0, v1)` is returned without modification.
    

set\_params(_minor\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2900-L2904)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator.set_params "Link to this definition")

Set parameters within this locator.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2914-L2989)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

class matplotlib.ticker.MaxNLocator(_nbins\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2111-L2329)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place evenly spaced ticks, with a cap on the total number of ticks.

Finds nice tick locations with no more than \\(nbins + 1\\) ticks being within the view limits. Locations beyond the limits are added to support autoscaling.

Parameters:

**nbins**int or 'auto', default: 10

Maximum number of intervals; one less than max number of ticks. If the string 'auto', the number of bins will be automatically determined based on the length of the axis.

**steps**array-like, optional

Sequence of acceptable tick multiples, starting with 1 and ending with 10. For example, if `steps=[1, 2, 4, 5, 10]`, `20, 40, 60` or `0.4, 0.6, 0.8` would be possible sets of ticks because they are multiples of 2. `30, 60, 90` would not be generated because 3 does not appear in this example list of steps.

**integer**bool, default: False

If True, ticks will take only integer values, provided at least _min\_n\_ticks_ integers are found within the view limits.

**symmetric**bool, default: False

If True, autoscaling will result in a range symmetric about zero.

**prune**{'lower', 'upper', 'both', None}, default: None

Remove the 'lower' tick, the 'upper' tick, or ticks on 'both' sides _if they fall exactly on an axis' edge_ (this typically occurs when `[rcParams["axes.autolimit_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.autolimit_mode#rcparam-axes-autolimit-mode) ` (default: `'data'`) is 'round\_numbers'). Removing such ticks is mostly useful for stacked or ganged plots, where the upper tick of an Axes overlaps with the lower tick of the axes above it.

**min\_n\_ticks**int, default: 2

Relax _nbins_ and _integer_ constraints if necessary to obtain this minimum number of ticks.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2297-L2299)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.__call__ "Link to this definition")

Return the locations of the ticks.

default\_params \= {'integer': False, 'min\_n\_ticks': 2, 'nbins': 10, 'prune': None, 'steps': None, 'symmetric': False}[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.default_params "Link to this definition")

set\_params(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2185-L2226)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.set_params "Link to this definition")

Set parameters for this locator.

Parameters:

**nbins**int or 'auto', optional

see [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

**steps**array-like, optional

see [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

**integer**bool, optional

see [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

**symmetric**bool, optional

see [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

**prune**{'lower', 'upper', 'both', None}, optional

see [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

**min\_n\_ticks**int, optional

see [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2301-L2316)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

view\_limits(_dmin_, _dmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2318-L2329)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.view_limits "Link to this definition")

Select a scale for the range from vmin to vmax.

Subclasses should override this method to change locator behaviour.

class matplotlib.ticker.MultipleLocator(_base\=1.0_, _offset\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1982-L2049)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place ticks at every integer multiple of a base plus an offset.

Parameters:

**base**float > 0, default: 1.0

Interval between ticks.

**offset**float, default: 0.0

Value added to each multiple of _base_.

Added in version 3.8.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2019-L2022)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator.__call__ "Link to this definition")

Return the locations of the ticks.

set\_params(_base\=None_, _offset\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2001-L2017)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator.set_params "Link to this definition")

Set parameters within this locator.

Parameters:

**base**float > 0, optional

Interval between ticks.

**offset**float, optional

Value added to each multiple of _base_.

Added in version 3.8.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2024-L2033)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

view\_limits(_dmin_, _dmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2035-L2049)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator.view_limits "Link to this definition")

Set the view limits to the nearest tick values that contain the data.

class matplotlib.ticker.NullFormatter[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L317-L322)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Always return the empty string.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L320-L322)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter.__call__ "Link to this definition")

Return the tick label strings for value _x_ at tick index _pos_.

This is the low-level formatting primitive for a single tick in the context of multiple ticks. Any context-dependent state (e.g. locs, offset, order of magnitude) must already be configured, typically by a prior call to `format_ticks` or `set_locs`.

_pos_ defines the index into `self.locs` so that the format can depend on the location. `pos=None` indicates an unspecified location.

The output may contain mathtext or LaTeX markup.

Subclasses must override this method.

class matplotlib.ticker.NullLocator[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1883-L1899)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place no ticks.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1888-L1889)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator.__call__ "Link to this definition")

Return the locations of the ticks.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1891-L1899)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator.tick_values "Link to this definition")

Return the locations of the ticks.

Note

Because there are no ticks, _vmin_ and _vmax_ are not used.

class matplotlib.ticker.PercentFormatter(_xmax\=100_, _decimals\=None_, _symbol\='%'_, _is\_latex\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1607-L1714)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Format numbers as a percentage.

Parameters:

**xmax**float

Determines how the number is converted into a percentage. _xmax_ is the data value that corresponds to 100%. Percentages are computed as `x / xmax * 100`. So if the data is already scaled to be percentages, _xmax_ will be 100. Another common situation is where _xmax_ is 1.0.

**decimals**None or int

The number of decimal places to place after the point. If _None_ (the default), the number will be computed automatically.

**symbol**str or None

A string that will be appended to the label. It may be _None_ or empty to indicate that no symbol should be used. LaTeX special characters are escaped in _symbol_ whenever latex mode is enabled, unless _is\_latex_ is _True_.

**is\_latex**bool

If _False_, reserved LaTeX characters in _symbol_ will be escaped.

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1639-L1643)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter.__call__ "Link to this definition")

Format the tick as a percentage with the appropriate scaling.

convert\_to\_pct(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1689-L1690)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter.convert_to_pct "Link to this definition")

format\_pct(_x_, _display\_range_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L1645-L1687)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter.format_pct "Link to this definition")

Format the number as a percentage number with the correct number of decimals and adds the percent symbol, if any.

If `self.decimals` is [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, the number of digits after the decimal point is set based on the _display\_range_ of the axis as follows:

| display\_range | decimals | sample |
| --- | --- | --- |
| \>50 | 0   | `x = 34.5` => 35% |
| \>5 | 1   | `x = 34.5` => 34.5% |
| \>0.5 | 2   | `x = 34.5` => 34.50% |
| ... | ... | ... |

This method will not be very good for tiny axis ranges or extremely large ones. It assumes that the values on the chart are percentages displayed on a reasonable scale.

property symbol[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter.symbol "Link to this definition")

The configured percent symbol as a string.

If LaTeX is enabled via `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`), the special characters `{'#', '$', '%', '&', '~', '_', '^', '\', '{', '}'}` are automatically escaped in the string.

class matplotlib.ticker.ScalarFormatter(_useOffset\=None_, _useMathText\=None_, _useLocale\=None_, _\*_, _usetex\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L457-L908)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Format tick values as a number.

Parameters:

**useOffset**bool or float, default: `[rcParams["axes.formatter.useoffset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.useoffset#rcparam-axes-formatter-useoffset) ` (default: `True`)

Whether to use offset notation. See [`set_useOffset`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useOffset "matplotlib.ticker.ScalarFormatter.set_useOffset")
.

**useMathText**bool, default: `[rcParams["axes.formatter.use_mathtext"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_mathtext#rcparam-axes-formatter-use-mathtext) ` (default: `False`)

Whether to use fancy math formatting. See [`set_useMathText`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useMathText "matplotlib.ticker.ScalarFormatter.set_useMathText")
.

**useLocale**bool, default: `[rcParams["axes.formatter.use_locale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_locale#rcparam-axes-formatter-use-locale) ` (default: `False`).

Whether to use locale settings for decimal sign and positive sign. See [`set_useLocale`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useLocale "matplotlib.ticker.ScalarFormatter.set_useLocale")
.

**usetex**bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`)

To enable/disable the use of TeX's math mode for rendering the numbers in the formatter.

Added in version 3.10.

Notes

In addition to the parameters above, the formatting of scientific vs. floating point representation can be configured via [`set_scientific`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_scientific "matplotlib.ticker.ScalarFormatter.set_scientific")
 and [`set_powerlimits`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_powerlimits "matplotlib.ticker.ScalarFormatter.set_powerlimits")
).

**Offset notation and scientific notation**

Offset notation and scientific notation look quite similar at first sight. Both split some information from the formatted tick values and display it at the end of the axis.

*   The scientific notation splits up the order of magnitude, i.e. a multiplicative scaling factor, e.g. `1e6`.
    
*   The offset notation separates an additive constant, e.g. `+1e6`. The offset notation label is always prefixed with a `+` or `-` sign and is thus distinguishable from the order of magnitude label.
    

The following plot with x limits `1_000_000` to `1_000_010` illustrates the different formatting. Note the labels at the right edge of the x axis.

([`Source code`](https://matplotlib.org/stable/_downloads/89cc6a6921a720c4665e5124d19197bc/ticker_api-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9f139206e8f961585b7b4ce20afafbe8/ticker_api-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f6cbba761a6626c0a53b7ab33d8ee7ef/ticker_api-1.png)
)

[![](https://matplotlib.org/stable/_images/api-ticker_api-1.2x.png)](https://matplotlib.org/stable/_images/api-ticker_api-1.2x.png)

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L668-L678)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.__call__ "Link to this definition")

Return the format for tick value _x_ at position _pos_.

property format[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.format "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

format\_data(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L752-L766)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.format_data "Link to this definition")

Return the context-independent string representation of a single _value_.

This is used internally, e.g. for constructing offset and scientific-notation strings. It always formats with `pos=None` and should return a context-independent representation rather than a concise tick label.

The output may contain mathtext or LaTeX markup.

format\_data\_short(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L724-L750)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.format_data_short "Link to this definition")

Return a short string representation of _value_ for the mouseover tooltip (the coordinate display in the interactive figure window).

This should return concise, plain text (no mathtext / LaTeX). The precision is typically adapted to the current axis resolution so that neighbouring pixels produce distinguishable labels.

Defaults to [`Formatter.format_data`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.format_data "matplotlib.ticker.Formatter.format_data")
; subclasses should override this to provide a plain-text representation that is independent of the current tick locations.

Note: The mouseover text can be customized by setting the `Axes.fmt_xdata` and `Axes.fmt_ydata` attributes.

get\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L768-L793)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.get_offset "Link to this definition")

Return scientific notation, plus offset.

get\_useLocale()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L587-L595)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.get_useLocale "Link to this definition")

Return whether locale settings are used for formatting.

See also

[`ScalarFormatter.set_useLocale`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useLocale "matplotlib.ticker.ScalarFormatter.set_useLocale")

get\_useMathText()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L623-L631)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.get_useMathText "Link to this definition")

Return whether to use fancy math formatting.

See also

[`ScalarFormatter.set_useMathText`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useMathText "matplotlib.ticker.ScalarFormatter.set_useMathText")

get\_useOffset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L538-L549)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.get_useOffset "Link to this definition")

Return whether automatic mode for offset notation is active.

This returns True if `set_useOffset(True)`; it returns False if an explicit offset was set, e.g. `set_useOffset(1000)`.

See also

[`ScalarFormatter.set_useOffset`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useOffset "matplotlib.ticker.ScalarFormatter.set_useOffset")

get\_usetex()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L528-L530)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.get_usetex "Link to this definition")

Return whether TeX's math mode is enabled for rendering.

property orderOfMagnitude[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.orderOfMagnitude "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11:

set\_locs(_locs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L795-L802)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_locs "Link to this definition")

Set the locations of the ticks.

This method is called before computing the tick labels because some formatters need to know all tick locations to do so.

set\_powerlimits(_lims_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L690-L722)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_powerlimits "Link to this definition")

Set size thresholds for scientific notation.

Parameters:

**lims**(int, int)

A tuple _(min\_exp, max\_exp)_ containing the powers of 10 that determine the switchover threshold. For a number representable as \\(a \\times 10^\\mathrm{exp}\\) with \\(1 <= |a| < 10\\), scientific notation will be used if `exp <= min_exp` or `exp >= max_exp`.

The default limits are controlled by `[rcParams["axes.formatter.limits"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.limits#rcparam-axes-formatter-limits) ` (default: `[-5, 6]`).

In particular numbers with _exp_ equal to the thresholds are written in scientific notation.

Typically, _min\_exp_ will be negative and _max\_exp_ will be positive.

For example, `formatter.set_powerlimits((-3, 4))` will provide the following formatting: \\(1 \\times 10^{-3}, 9.9 \\times 10^{-3}, 0.01,\\) \\(9999, 1 \\times 10^4\\).

See also

[`ScalarFormatter.set_scientific`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_scientific "matplotlib.ticker.ScalarFormatter.set_scientific")

set\_scientific(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L680-L688)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_scientific "Link to this definition")

Turn scientific notation on or off.

See also

[`ScalarFormatter.set_powerlimits`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_powerlimits "matplotlib.ticker.ScalarFormatter.set_powerlimits")

set\_useLocale(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L597-L606)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useLocale "Link to this definition")

Set whether to use locale settings for decimal sign and positive sign.

Parameters:

**val**bool or None

_None_ resets to `[rcParams["axes.formatter.use_locale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_locale#rcparam-axes-formatter-use-locale) ` (default: `False`).

set\_useMathText(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L633-L664)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useMathText "Link to this definition")

Set whether to use fancy math formatting.

If active, scientific notation is formatted as \\(1.2 \\times 10^3\\).

Parameters:

**val**bool or None

_None_ resets to `[rcParams["axes.formatter.use_mathtext"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_mathtext#rcparam-axes-formatter-use-mathtext) ` (default: `False`).

set\_useOffset(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L551-L583)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useOffset "Link to this definition")

Set whether to use offset notation.

When formatting a set numbers whose value is large compared to their range, the formatter can separate an additive constant. This can shorten the formatted numbers so that they are less likely to overlap when drawn on an axis.

Parameters:

**val**bool or float

*   If False, do not use offset notation.
    
*   If True (=automatic mode), use offset notation if it can make the residual numbers significantly shorter. The exact behavior is controlled by `[rcParams["axes.formatter.offset_threshold"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.offset_threshold#rcparam-axes-formatter-offset-threshold) ` (default: `4`).
    
*   If a number, force an offset of the given value.
    

Examples

With active offset notation, the values

`100_000, 100_002, 100_004, 100_006, 100_008`

will be formatted as `0, 2, 4, 6, 8` plus an offset `+1e5`, which is written to the edge of the axis.

set\_usetex(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L532-L534)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_usetex "Link to this definition")

Set whether to use TeX's math mode for rendering numbers in the formatter.

property useLocale[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.useLocale "Link to this definition")

Return whether locale settings are used for formatting.

See also

[`ScalarFormatter.set_useLocale`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useLocale "matplotlib.ticker.ScalarFormatter.set_useLocale")

property useMathText[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.useMathText "Link to this definition")

Return whether to use fancy math formatting.

See also

[`ScalarFormatter.set_useMathText`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useMathText "matplotlib.ticker.ScalarFormatter.set_useMathText")

property useOffset[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.useOffset "Link to this definition")

Return whether automatic mode for offset notation is active.

This returns True if `set_useOffset(True)`; it returns False if an explicit offset was set, e.g. `set_useOffset(1000)`.

See also

[`ScalarFormatter.set_useOffset`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useOffset "matplotlib.ticker.ScalarFormatter.set_useOffset")

property usetex[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.usetex "Link to this definition")

Return whether TeX's math mode is enabled for rendering.

class matplotlib.ticker.StrMethodFormatter(_fmt_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L423-L454)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Use a new-style format string (as used by [`str.format`](https://docs.python.org/3/library/stdtypes.html#str.format "(in Python v3.14)")
) to format the tick.

The field used for the tick value must be labeled _x_ and the field used for the tick position must be labeled _pos_.

The formatter will respect `[rcParams["axes.unicode_minus"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.unicode_minus#rcparam-axes-unicode-minus) ` (default: `True`) when formatting negative numeric values.

It is typically unnecessary to explicitly construct [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 objects, as [`set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 directly accepts the format string itself.

Examples

\>>> formatter \= StrMethodFormatter("{x} km")
\>>> formatter(10)
"10 km"

\_\_call\_\_(_x_, _pos\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L447-L454)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter.__call__ "Link to this definition")

Return the formatted label string.

_x_ and _pos_ are passed to [`str.format`](https://docs.python.org/3/library/stdtypes.html#str.format "(in Python v3.14)")
 as keyword arguments with those exact names.

class matplotlib.ticker.SymmetricalLogLocator(_transform\=None_, _subs\=None_, _linthresh\=None_, _base\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2636-L2787)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Place ticks spaced linearly near zero and spaced logarithmically beyond a threshold.

Parameters:

**transform**[`SymmetricalLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform "matplotlib.scale.SymmetricalLogTransform")
, optional

If set, defines the _base_ and _linthresh_ of the symlog transform.

**base, linthresh**float, optional

The _base_ and _linthresh_ of the symlog transform, as documented for [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
. These parameters are only used if _transform_ is not set.

**subs**sequence of float, default: \[1\]

The multiples of integer powers of the base where ticks are placed, i.e., ticks are placed at `[sub * base**i for i in ... for sub in subs]`.

Notes

Either _transform_, or both _base_ and _linthresh_, must be given.

\_\_call\_\_()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2682-L2686)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator.__call__ "Link to this definition")

Return the locations of the ticks.

set\_params(_subs\=None_, _numticks\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2675-L2680)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator.set_params "Link to this definition")

Set parameters within this locator.

tick\_values(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2688-L2772)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator.tick_values "Link to this definition")

Return the values of the located ticks given **vmin** and **vmax**.

Note

To get tick locations with the vmin and vmax values defined automatically for the associated `axis` simply call the Locator instance:

\>>> print(type(loc))
<type 'Locator'>
\>>> print(loc())
\[1, 2, 3, 4\]

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L2774-L2787)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator.view_limits "Link to this definition")

Try to choose the view limits intelligently.

class matplotlib.ticker.TickHelper[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L188-L196)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

axis \= None[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper.axis "Link to this definition")

create\_dummy\_axis(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L194-L196)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper.create_dummy_axis "Link to this definition")

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/ticker.py#L191-L192)
[#](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper.set_axis "Link to this definition")

Inheritance diagram of matplotlib.ticker

On this page