[Skip to main content](https://matplotlib.org/stable/api/colorbar_api.html#main-content)

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
    

`matplotlib.colorbar`[#](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "Link to this heading")

================================================================================================================================

Colorbars are a visualization of the mapping from scalar values to colors. In Matplotlib they are drawn into a dedicated [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.

Note

Colorbars are typically created through [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 or its pyplot wrapper [`pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
, which internally use [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 together with [`make_axes_gridspec`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes_gridspec "matplotlib.colorbar.make_axes_gridspec")
 (for [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\-positioned Axes) or [`make_axes`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "matplotlib.colorbar.make_axes")
 (for non-[`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\-positioned Axes).

End-users most likely won't need to directly use this module's API.

class matplotlib.colorbar.Colorbar(_ax_, _mappable\=None_, _\*_, _alpha\=None_, _location\=None_, _extend\=None_, _extendfrac\=None_, _extendrect\=False_, _ticks\=None_, _format\=None_, _values\=None_, _boundaries\=None_, _spacing\='uniform'_, _drawedges\=False_, _label\=''_, _cmap\=None_, _norm\=None_, _orientation\=None_, _ticklocation\='auto'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L209-L1354)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Draw a colorbar in an existing Axes.

Typically, colorbars are created using [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 or [`pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 and associated with [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
s (such as an [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 generated via [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
).

In order to draw a colorbar not associated with other elements in the figure, e.g. when showing a colormap by itself, one can create an empty [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
, or directly pass _cmap_ and _norm_ instead of _mappable_ to [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
.

Useful public methods are [`set_label()`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
 and [`add_lines()`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.add_lines "matplotlib.colorbar.Colorbar.add_lines")
.

Attributes:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance in which the colorbar is drawn.

**lines**list

A list of [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 (empty if no lines were drawn).

**dividers**[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

A LineCollection (empty if _drawedges_ is `False`).

Parameters:

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance in which the colorbar is drawn.

**mappable**[`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")

The mappable whose colormap and norm will be used.

To show the colors versus index instead of on a 0-1 scale, set the mappable's norm to `colors.NoNorm()`.

**alpha**float

The colorbar transparency between 0 (transparent) and 1 (opaque).

**location**None or {'left', 'right', 'top', 'bottom'}

Set the colorbar's _orientation_ and _ticklocation_. Colorbars on the left and right are vertical, colorbars at the top and bottom are horizontal. The _ticklocation_ is the same as _location_, so if _location_ is 'top', the ticks are on the top. _orientation_ and/or _ticklocation_ can be provided as well and overrides the value set by _location_, but there will be an error for incompatible combinations.

Added in version 3.7.

**extend**{'neither', 'both', 'min', 'max'}

Make pointed end(s) for out-of-range values (unless 'neither'). These are set for a given colormap using the colormap set\_under and set\_over methods.

**extendfrac**{_None_, 'auto', length, lengths}

If set to _None_, both the minimum and maximum triangular colorbar extensions will have a length of 5% of the interior colorbar length (this is the default setting).

If set to 'auto', makes the triangular colorbar extensions the same lengths as the interior boxes (when _spacing_ is set to 'uniform') or the same lengths as the respective adjacent interior boxes (when _spacing_ is set to 'proportional').

If a scalar, indicates the length of both the minimum and maximum triangular colorbar extensions as a fraction of the interior colorbar length. A two-element sequence of fractions may also be given, indicating the lengths of the minimum and maximum colorbar extensions respectively as a fraction of the interior colorbar length.

**extendrect**bool

If _False_ the minimum and maximum colorbar extensions will be triangular (the default). If _True_ the extensions will be rectangular.

**ticks**None or list of ticks or Locator

If None, ticks are determined automatically from the input.

**format**None or str or Formatter

If None, [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 is used. Format strings, e.g., `"%4.2e"` or `"{x:.2e}"`, are supported. An alternative [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 may be given instead.

**drawedges**bool

Whether to draw lines at color boundaries.

**label**str

The label on the colorbar's long axis.

**boundaries, values**None or a sequence

If unset, the colormap will be displayed on a 0-1 scale. If sequences, _values_ must have a length 1 less than _boundaries_. For each region delimited by adjacent entries in _boundaries_, the color mapped to the corresponding value in _values_ will be used. The size of each region is determined by the _spacing_ parameter. Normally only useful for indexed colors (i.e. `norm=NoNorm()`) or other unusual circumstances.

**spacing**{'uniform', 'proportional'}

For discrete colorbars ([`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 or contours), 'uniform' gives each color the same space; 'proportional' makes the space proportional to the data interval.

Other Parameters:

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

The colormap to use. This parameter is ignored, unless _mappable_ is None.

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

The normalization to use. This parameter is ignored, unless _mappable_ is None.

**orientation**None or {'vertical', 'horizontal'}

If None, use the value determined by _location_. If both _orientation_ and _location_ are None then defaults to 'vertical'.

**ticklocation**{'auto', 'left', 'right', 'top', 'bottom'}

The location of the colorbar ticks. The _ticklocation_ must match _orientation_. For example, a horizontal colorbar can only have ticks at the top or the bottom. If 'auto', the ticks will be the same as _location_, so a colorbar to the left will have ticks to the left. If _location_ is None, the ticks will be at the bottom for a horizontal colorbar and at the right for a vertical.

add\_lines(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L753-L831)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.add_lines "Link to this definition")

Draw lines on the colorbar.

The lines are appended to the list `lines`.

Parameters:

**levels**array-like

The positions of the lines.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Either a single color applying to all lines or one color value for each line.

**linewidths**float or array-like

Either a single linewidth applying to all lines or one linewidth for each line.

**erase**bool, default: True

Whether to remove any previously added lines.

Notes

Alternatively, this method can also be called with the signature `colorbar.add_lines(contour_set, erase=True)`, in which case _levels_, _colors_, and _linewidths_ are taken from _contour\_set_.

drag\_pan(_button_, _key_, _x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L1347-L1354)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.drag_pan "Link to this definition")

property formatter[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.formatter "Link to this definition")

Major tick label [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 for the colorbar.

get\_ticks(_minor\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L916-L928)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.get_ticks "Link to this definition")

Return the ticks as a list of locations.

Parameters:

**minor**boolean, default: False

if True return the minor ticks.

property locator[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.locator "Link to this definition")

Major tick [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 for the colorbar.

property long\_axis[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.long_axis "Link to this definition")

Axis that has decorations (ticks, etc) on it.

property minorformatter[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorformatter "Link to this definition")

Minor tick [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 for the colorbar.

property minorlocator[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorlocator "Link to this definition")

Minor tick [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 for the colorbar.

minorticks\_off()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L972-L975)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorticks_off "Link to this definition")

Turn the minor ticks of the colorbar off.

minorticks\_on()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L965-L970)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorticks_on "Link to this definition")

Turn on colorbar minor ticks.

n\_rasterize \= 50[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.n_rasterize "Link to this definition")

remove()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L1042-L1074)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.remove "Link to this definition")

Remove this colorbar from the figure.

If the colorbar was created with `use_gridspec=True` the previous gridspec is restored.

set\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L1004-L1011)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_alpha "Link to this definition")

Set the transparency between 0 (transparent) and 1 (opaque).

If an array is provided, _alpha_ will be set to None to use the transparency values associated with the colormap.

set\_label(_label_, _\*_, _loc\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L977-L1002)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "Link to this definition")

Add a label to the long axis of the colorbar.

Parameters:

**label**str

The label text.

**loc**str, optional

The location of the label.

*   For horizontal orientation one of {'left', 'center', 'right'}
    
*   For vertical orientation one of {'bottom', 'center', 'top'}
    

Defaults to `[rcParams["xaxis.labellocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xaxis.labellocation#rcparam-xaxis-labellocation) ` (default: `'center'`) or `[rcParams["yaxis.labellocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=yaxis.labellocation#rcparam-yaxis-labellocation) ` (default: `'center'`) depending on the orientation.

**\*\*kwargs**

Keyword arguments are passed to [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
 / [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
. Supported keywords are _labelpad_ and [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

set\_ticklabels(_ticklabels_, _\*_, _minor\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L930-L963)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticklabels "Link to this definition")

\[_Discouraged_\] Set tick labels.

Discouraged

The use of this method is discouraged, because of the dependency on tick positions. In most cases, you'll want to use `set_ticks(positions, labels=labels)` instead.

If you are using this method, you should always fix the tick positions before, e.g. by using [`Colorbar.set_ticks`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
 or by explicitly setting a [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
 on the long axis of the colorbar. Otherwise, ticks are free to move and the labels may end up in unexpected positions.

Parameters:

**ticklabels**sequence of str or of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

Texts for labeling each tick location in the sequence set by [`Colorbar.set_ticks`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "matplotlib.colorbar.Colorbar.set_ticks")
; the number of labels must match the number of locations.

**update\_ticks**bool, default: True

This keyword argument is ignored and will be removed. Deprecated

**minor**bool

If True, set minor ticks instead of major ticks.

**\*\*kwargs**

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels.

set\_ticks(_ticks_, _\*_, _labels\=None_, _minor\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L891-L914)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_ticks "Link to this definition")

Set tick locations.

Parameters:

**ticks**1D array-like

List of tick locations.

**labels**list of str, optional

List of tick labels. If not set, the labels show the data value.

**minor**bool, default: False

If `False`, set the major ticks; if `True`, the minor ticks.

**\*\*kwargs**

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels. These take effect only if you pass _labels_. In other cases, please use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

update\_normal(_mappable\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L505-L540)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.update_normal "Link to this definition")

Update solid patches, lines, etc.

This is meant to be called when the norm of the image or contour plot to which this colorbar belongs changes.

If the norm on the mappable is different than before, this resets the locator and formatter for the axis, so if these have been customized, they will need to be customized again. However, if the norm only changes values of _vmin_, _vmax_ or _cmap_ then the old formatter and locator will be preserved.

update\_ticks()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L833-L841)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.update_ticks "Link to this definition")

Set up the ticks and ticklabels. This should not be needed by users.

matplotlib.colorbar.ColorbarBase[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L209-L1354)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.ColorbarBase "Link to this definition")

alias of [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")

matplotlib.colorbar.make\_axes(_parents_, _location\=None_, _orientation\=None_, _fraction\=0.15_, _shrink\=1.0_, _aspect\=20_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L1392-L1493)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "Link to this definition")

Create an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 suitable for a colorbar.

The Axes is placed in the figure of the _parents_ Axes, by resizing and repositioning _parents_.

Parameters:

**parents**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or iterable or [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes to use as parents for placing the colorbar.

**location**None or {'left', 'right', 'top', 'bottom'}

The location, relative to the parent Axes, where the colorbar Axes is created. It also determines the _orientation_ of the colorbar (colorbars on the left and right are vertical, colorbars at the top and bottom are horizontal). If None, the location will come from the _orientation_ if it is set (vertical colorbars on the right, horizontal ones at the bottom), or default to 'right' if _orientation_ is unset.

**orientation**None or {'vertical', 'horizontal'}

The orientation of the colorbar. It is preferable to set the _location_ of the colorbar, as that also determines the _orientation_; passing incompatible values for _location_ and _orientation_ raises an exception.

**fraction**float, default: 0.15

Fraction of original Axes to use for colorbar.

**shrink**float, default: 1.0

Fraction by which to multiply the size of the colorbar.

**aspect**float, default: 20

Ratio of long to short dimensions.

**pad**float, default: 0.05 if vertical, 0.15 if horizontal

Fraction of original Axes between colorbar and new image Axes.

**anchor**(float, float), optional

The anchor point of the colorbar Axes. Defaults to (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal.

**panchor**(float, float), or _False_, optional

The anchor point of the colorbar parent Axes. If _False_, the parent axes' anchor will be unchanged. Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.

Returns:

**cax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The child Axes.

**kwargs**dict

The reduced keyword dictionary to be passed when creating the colorbar instance.

matplotlib.colorbar.make\_axes\_gridspec(_parent_, _\*_, _location\=None_, _orientation\=None_, _fraction\=0.15_, _shrink\=1.0_, _aspect\=20_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorbar.py#L1496-L1585)
[#](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes_gridspec "Link to this definition")

Create an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 suitable for a colorbar.

The Axes is placed in the figure of the _parent_ Axes, by resizing and repositioning _parent_.

This function is similar to [`make_axes`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "matplotlib.colorbar.make_axes")
 and mostly compatible with it. Primary differences are

*   [`make_axes_gridspec`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes_gridspec "matplotlib.colorbar.make_axes_gridspec")
     requires the _parent_ to have a subplotspec.
    
*   [`make_axes`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "matplotlib.colorbar.make_axes")
     positions the Axes in figure coordinates; [`make_axes_gridspec`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes_gridspec "matplotlib.colorbar.make_axes_gridspec")
     positions it using a subplotspec.
    
*   [`make_axes`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "matplotlib.colorbar.make_axes")
     updates the position of the parent. [`make_axes_gridspec`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes_gridspec "matplotlib.colorbar.make_axes_gridspec")
     replaces the parent gridspec with a new one.
    

Parameters:

**parent**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes to use as parent for placing the colorbar.

**location**None or {'left', 'right', 'top', 'bottom'}

The location, relative to the parent Axes, where the colorbar Axes is created. It also determines the _orientation_ of the colorbar (colorbars on the left and right are vertical, colorbars at the top and bottom are horizontal). If None, the location will come from the _orientation_ if it is set (vertical colorbars on the right, horizontal ones at the bottom), or default to 'right' if _orientation_ is unset.

**orientation**None or {'vertical', 'horizontal'}

The orientation of the colorbar. It is preferable to set the _location_ of the colorbar, as that also determines the _orientation_; passing incompatible values for _location_ and _orientation_ raises an exception.

**fraction**float, default: 0.15

Fraction of original Axes to use for colorbar.

**shrink**float, default: 1.0

Fraction by which to multiply the size of the colorbar.

**aspect**float, default: 20

Ratio of long to short dimensions.

**pad**float, default: 0.05 if vertical, 0.15 if horizontal

Fraction of original Axes between colorbar and new image Axes.

**anchor**(float, float), optional

The anchor point of the colorbar Axes. Defaults to (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal.

**panchor**(float, float), or _False_, optional

The anchor point of the colorbar parent Axes. If _False_, the parent axes' anchor will be unchanged. Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.

Returns:

**cax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The child Axes.

**kwargs**dict

The reduced keyword dictionary to be passed when creating the colorbar instance.

On this page