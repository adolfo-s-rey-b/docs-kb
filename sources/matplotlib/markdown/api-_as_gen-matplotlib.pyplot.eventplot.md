[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html#main-content)

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
    

matplotlib.pyplot.eventplot[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html#matplotlib-pyplot-eventplot "Link to this heading")

==============================================================================================================================================================

matplotlib.pyplot.eventplot(_positions_, _\*_, _orientation\='horizontal'_, _lineoffsets\=1_, _linelengths\=1_, _linewidths\=None_, _colors\=None_, _alpha\=None_, _linestyles\='solid'_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3460-L3485)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html#matplotlib.pyplot.eventplot "Link to this definition")

Plot identical parallel lines at the given positions.

This type of plot is commonly used in neuroscience for representing neural events, where it is usually called a spike raster, dot raster, or raster plot.

However, it is useful in any situation where you wish to show the timing or position of multiple sets of discrete events, such as the arrival times of people to a business on each day of the month or the date of hurricanes each year of the last century.

Parameters:

**positions**array-like or list of array-like

A 1D array-like defines the positions of one sequence of events.

Multiple groups of events may be passed as a list of array-likes. Each group can be styled independently by passing lists of values to _lineoffsets_, _linelengths_, _linewidths_, _colors_ and _linestyles_.

Note that _positions_ can be a 2D array, but in practice different event groups usually have different counts so that one will use a list of different-length arrays rather than a 2D array.

**orientation**{'horizontal', 'vertical'}, default: 'horizontal'

The direction of the event sequence:

*   'horizontal': the events are arranged horizontally. The indicator lines are vertical.
    
*   'vertical': the events are arranged vertically. The indicator lines are horizontal.
    

**lineoffsets**float or array-like, default: 1

The offset of the center of the lines from the origin, in the direction orthogonal to _orientation_.

If _positions_ is 2D, this can be a sequence with length matching the length of _positions_.

**linelengths**float or array-like, default: 1

The total height of the lines (i.e. the lines stretches from `lineoffset - linelength/2` to `lineoffset + linelength/2`).

If _positions_ is 2D, this can be a sequence with length matching the length of _positions_.

**linewidths**float or array-like, default: `[rcParams["lines.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.linewidth#rcparam-lines-linewidth) ` (default: `1.5`)

The line width(s) of the event lines, in points.

If _positions_ is 2D, this can be a sequence with length matching the length of _positions_.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of color, default: `[rcParams["lines.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.color#rcparam-lines-color) ` (default: `'C0'`)

The color(s) of the event lines.

If _positions_ is 2D, this can be a sequence with length matching the length of _positions_.

**alpha**float or array-like, default: 1

The alpha blending value(s), between 0 (transparent) and 1 (opaque).

If _positions_ is 2D, this can be a sequence with length matching the length of _positions_.

**linestyles**str or tuple or list of such values, default: 'solid'

Default is 'solid'. Valid strings are \['solid', 'dashed', 'dashdot', 'dotted', '-', '--', '-.', ':'\]. Dash tuples should be of the form:

(offset, onoffseq),

where _onoffseq_ is an even length tuple of on and off ink in points.

If _positions_ is 2D, this can be a sequence with length matching the length of _positions_.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_positions_, _lineoffsets_, _linelengths_, _linewidths_, _colors_, _linestyles_

**\*\*kwargs**

Other keyword arguments are line collection properties. See [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 for a list of the valid properties.

Returns:

list of [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")

The [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
 that were added.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.eventplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.eventplot.html#matplotlib.axes.Axes.eventplot "matplotlib.axes.Axes.eventplot")
.

For _linelengths_, _linewidths_, _colors_, _alpha_ and _linestyles_, if only a single value is given, that value is applied to all lines. If an array-like is given, it must have the same length as _positions_, and each value will be applied to the corresponding row of the array.

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/a024a7f82b28bca9e39a6bd6efb035b3/eventplot_demo.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/a0b0786ed1324f6959608caf78107cb8/eventplot_demo_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8b2ca7af9b269c8fe8ab0b1068d12a68/eventplot_demo_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-eventplot_demo_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-eventplot_demo_00_00.2x.png)

On this page