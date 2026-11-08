[Skip to main content](https://matplotlib.org/stable/api/container_api.html#main-content)

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
    

`matplotlib.container`[#](https://matplotlib.org/stable/api/container_api.html#module-matplotlib.container "Link to this heading")

===================================================================================================================================

class matplotlib.container.BarContainer(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L42-L116)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "Link to this definition")

Bases: [`Container`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container "matplotlib.container.Container")

Container for the artists of bar plots (e.g. created by [`Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
).

The container can be treated as a tuple of the _patches_ themselves. Additionally, you can access these and further parameters by the attributes.

Attributes:

**patches**list of [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

The artists of the bars.

**errorbar**None or [`ErrorbarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.ErrorbarContainer "matplotlib.container.ErrorbarContainer")

A container for the error bar artists if error bars are present. _None_ otherwise.

**datavalues**None or array-like

The underlying data values corresponding to the bars.

**orientation**{'vertical', 'horizontal'}, default: None

If 'vertical', the bars are assumed to be vertical. If 'horizontal', the bars are assumed to be horizontal.

property bottoms[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer.bottoms "Link to this definition")

Return the values at the lower end of the bars.

Added in version 3.11.

property position\_centers[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer.position_centers "Link to this definition")

Return the centers of bar positions.

Added in version 3.11.

property tops[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer.tops "Link to this definition")

Return the values at the upper end of the bars.

Added in version 3.11.

class matplotlib.container.Container(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L5-L39)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container "Link to this definition")

Bases: [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

Base class for containers.

Containers are classes that collect semantically related Artists such as the bars of a bar plot.

add\_callback(_func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L404-L431)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.add_callback "Link to this definition")

Add a callback function that will be called whenever one of the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
's properties changes.

Parameters:

**func**callable

The callback function. It must have the signature:

def func(artist: Artist) \-> Any

where _artist_ is the calling [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
. Return values may exist but are ignored.

Returns:

int

The observer id associated with the callback. This id can be used for removing the callback with [`remove_callback`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.remove_callback "matplotlib.container.Container.remove_callback")
 later.

See also

[`remove_callback`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.remove_callback "matplotlib.container.Container.remove_callback")

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L32-L33)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.get_children "Link to this definition")

get\_label()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1162-L1164)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.get_label "Link to this definition")

Return the label used for this artist in the legend.

pchanged()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L443-L454)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.pchanged "Link to this definition")

Call all of the registered callbacks.

This function is triggered internally when a property is changed.

See also

[`add_callback`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.add_callback "matplotlib.container.Container.add_callback")

[`remove_callback`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.remove_callback "matplotlib.container.Container.remove_callback")

remove()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L24-L30)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.remove "Link to this definition")

remove\_callback(_oid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L433-L441)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.remove_callback "Link to this definition")

Remove a callback based on its observer id.

See also

[`add_callback`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.add_callback "matplotlib.container.Container.add_callback")

set\_label(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1166-L1179)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container.set_label "Link to this definition")

Set a label that will be displayed in the legend.

Parameters:

**s**object

_s_ will be converted to a string by calling [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
.

class matplotlib.container.ErrorbarContainer(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L119-L148)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.ErrorbarContainer "Link to this definition")

Bases: [`Container`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container "matplotlib.container.Container")

Container for the artists of error bars (e.g. created by [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
).

The container can be treated as the _lines_ tuple itself. Additionally, you can access these and further parameters by the attributes.

Attributes:

**lines**tuple

Tuple of `(data_line, caplines, barlinecols)`.

*   data\_line : A [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
     instance of x, y plot markers and/or line.
    
*   caplines : A tuple of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
     instances of the error bar caps.
    
*   barlinecols : A tuple of [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     with the horizontal and vertical error ranges.
    

**has\_xerr, has\_yerr**bool

`True` if the errorbar has x/y errors.

class matplotlib.container.PieContainer(_wedges_, _values_, _normalize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L151-L220)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Container for the artists of pie charts (e.g. created by [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
).

Added in version 3.11.

Warning

The class name `PieContainer` name is provisional and may change in future to reflect development of its functionality.

You can access the wedge patches and further parameters by the attributes.

Attributes:

**wedges**list of [`Wedge`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")

The artists of the pie wedges.

**values**[`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

The data that the pie is based on.

**fracs**[`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

The fraction of the pie that each wedge represents.

**texts**list of list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The artists of any labels on the pie wedges. Each inner list has one text label per wedge.

add\_texts(_texts_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L207-L209)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer.add_texts "Link to this definition")

Add a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects to the container.

property fracs[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer.fracs "Link to this definition")

remove()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L211-L215)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer.remove "Link to this definition")

Remove all wedges and texts from the axes

property texts[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer.texts "Link to this definition")

property values[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer.values "Link to this definition")

class matplotlib.container.StemContainer(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/container.py#L223-L255)
[#](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.StemContainer "Link to this definition")

Bases: [`Container`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container "matplotlib.container.Container")

Container for the artists created in a [`Axes.stem()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
 plot.

The container can be treated like a namedtuple `(markerline, stemlines, baseline)`.

Attributes:

**markerline**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The artist of the markers at the stem heads.

**stemlines**[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

The artists of the vertical lines for all stems.

**baseline**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The artist of the horizontal baseline.

Parameters:

**markerline\_stemlines\_baseline**tuple

Tuple of `(markerline, stemlines, baseline)`. `markerline` contains the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 of the markers, `stemlines` is a [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 of the main lines, `baseline` is the [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 of the baseline.

On this page