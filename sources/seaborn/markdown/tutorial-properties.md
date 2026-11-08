 

 Ctrl+K

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
    
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
    
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
    
*   [API](https://seaborn.pydata.org/api.html)
    
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
    
*   [Citing](https://seaborn.pydata.org/citing.html)
    
*   [FAQ](https://seaborn.pydata.org/faq.html)
    

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
    
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
    
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")
    

On this page

Properties of Mark objects[#](https://seaborn.pydata.org/tutorial/properties.html#properties-of-mark-objects "Permalink to this heading")

==========================================================================================================================================

Coordinate properties[#](https://seaborn.pydata.org/tutorial/properties.html#coordinate-properties "Permalink to this heading")

--------------------------------------------------------------------------------------------------------------------------------

### x, y, xmin, xmax, ymin, ymax[#](https://seaborn.pydata.org/tutorial/properties.html#x-y-xmin-xmax-ymin-ymax "Permalink to this heading")

Coordinate properties determine where a mark is drawn on a plot. Canonically, the `x` coordinate is the horizontal position and the `y` coordinate is the vertical position. Some marks accept a span (i.e., `min`, `max`) parameterization for one or both variables. Others may accept `x` and `y` but also use a `baseline` parameter to show a span. The layer’s `orient` parameter determines how this works.

If a variable does not contain numeric data, its scale will apply a conversion so that data can be drawn on a screen. For instance, `Nominal` scales assign an integer index to each distinct category, and `Temporal` scales represent dates as the number of days from a reference “epoch”:

[![../_images/properties_3_0.png](https://seaborn.pydata.org/_images/properties_3_0.png)](https://seaborn.pydata.org/_images/properties_3_0.png)

A `Continuous` scale can also apply a nonlinear transform between data values and spatial positions:

[![../_images/properties_5_0.png](https://seaborn.pydata.org/_images/properties_5_0.png)](https://seaborn.pydata.org/_images/properties_5_0.png)

Color properties[#](https://seaborn.pydata.org/tutorial/properties.html#color-properties "Permalink to this heading")

----------------------------------------------------------------------------------------------------------------------

### color, fillcolor, edgecolor[#](https://seaborn.pydata.org/tutorial/properties.html#color-fillcolor-edgecolor "Permalink to this heading")

All marks can be given a `color`, and many distinguish between the color of the mark’s “edge” and “fill”. Often, simply using `color` will set both, while the more-specific properties allow further control:

[![../_images/properties_8_0.png](https://seaborn.pydata.org/_images/properties_8_0.png)](https://seaborn.pydata.org/_images/properties_8_0.png)

When the color property is mapped, the default palette depends on the type of scale. Nominal scales use discrete, unordered hues, while continuous scales (including temporal ones) use a sequential gradient:

[![../_images/properties_10_0.png](https://seaborn.pydata.org/_images/properties_10_0.png)](https://seaborn.pydata.org/_images/properties_10_0.png)

Note

The default continuous scale is subject to change in future releases to improve discriminability.

Color scales are parameterized by the name of a palette, such as `'viridis'`, `'rocket'`, or `'deep'`. Some palette names can include parameters, including simple gradients (e.g. `'dark:blue'`) or the cubehelix system (e.g. `` 'ch:start=.2,rot=-.4` ``). See the [color palette tutorial](https://seaborn.pydata.org/tutorial/color_palettes.html)
 for guidance on making an appropriate selection.

Continuous scales can also be parameterized by a tuple of colors that the scale should interpolate between. When using a nominal scale, it is possible to provide either the name of the palette (which will be discretely-sampled, if necessary), a list of individual color values, or a dictionary directly mapping data values to colors.

Individual colors may be specified [in a wide range of formats](https://matplotlib.org/stable/tutorials/colors/colors.html)
. These include indexed references to the current color cycle (`'C0'`), single-letter shorthands (`'b'`), grayscale values (`'.4'`), RGB hex codes (`'#4c72b0'`), X11 color names (`'seagreen'`), and XKCD color survey names (`'purpleish'`):

[![../_images/properties_12_0.png](https://seaborn.pydata.org/_images/properties_12_0.png)](https://seaborn.pydata.org/_images/properties_12_0.png)

### alpha, fillalpha, edgealpha[#](https://seaborn.pydata.org/tutorial/properties.html#alpha-fillalpha-edgealpha "Permalink to this heading")

The `alpha` property determines the mark’s opacity. Lowering the alpha can be helpful for representing density in the case of overplotting:

[![../_images/properties_14_0.png](https://seaborn.pydata.org/_images/properties_14_0.png)](https://seaborn.pydata.org/_images/properties_14_0.png)

Mapping the `alpha` property can also be useful even when marks do not overlap because it conveys a sense of importance and can be combined with a `color` scale to represent two variables. Moreover, colors with lower alpha appear less saturated, which can improve the appearance of larger filled marks (such as bars).

As with `color`, some marks define separate `edgealpha` and `fillalpha` properties for additional control.

Style properties[#](https://seaborn.pydata.org/tutorial/properties.html#style-properties "Permalink to this heading")

----------------------------------------------------------------------------------------------------------------------

### fill[#](https://seaborn.pydata.org/tutorial/properties.html#fill "Permalink to this heading")

The `fill` property is relevant to marks with a distinction between the edge and interior and determines whether the interior is visible. It is a boolean state: `fill` can be set only to `True` or `False`:

[![../_images/properties_18_0.png](https://seaborn.pydata.org/_images/properties_18_0.png)](https://seaborn.pydata.org/_images/properties_18_0.png)

### marker[#](https://seaborn.pydata.org/tutorial/properties.html#marker "Permalink to this heading")

The `marker` property is relevant for dot marks and some line marks. The API for specifying markers is very flexible, as detailed in the matplotlib API docs: [`matplotlib.markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "(in Matplotlib v3.8.2)")
.

Markers can be specified using a number of simple string codes:

[![../_images/properties_21_0.png](https://seaborn.pydata.org/_images/properties_21_0.png)](https://seaborn.pydata.org/_images/properties_21_0.png)

They can also be programatically generated using a `(num_sides, fill_style, angle)` tuple:

[![../_images/properties_23_0.png](https://seaborn.pydata.org/_images/properties_23_0.png)](https://seaborn.pydata.org/_images/properties_23_0.png)

See the matplotlib docs for additional formats, including mathtex character codes (`'$...$'`) and arrays of vertices.

A marker property is always mapped with a nominal scale; there is no inherent ordering to the different shapes. If no scale is provided, the plot will programmatically generate a suitably large set of unique markers:

[![../_images/properties_25_0.png](https://seaborn.pydata.org/_images/properties_25_0.png)](https://seaborn.pydata.org/_images/properties_25_0.png)

While this ensures that the shapes are technically distinct, bear in mind that — in most cases — it will be difficult to tell the markers apart if more than a handful are used in a single plot.

Note

The default marker scale is subject to change in future releases to improve discriminability.

### linestyle, edgestyle[#](https://seaborn.pydata.org/tutorial/properties.html#linestyle-edgestyle "Permalink to this heading")

The `linestyle` property is relevant to line marks, and the `edgestyle` property is relevant to a number of marks with “edges. Both properties determine the “dashing” of a line in terms of on-off segments.

Dashes can be specified with a small number of shorthand codes (`'-'`, `'--'`, `'-.'`, and `':'`) or programatically using `(on, off, ...)` tuples. In the tuple specification, the unit is equal to the linewidth:

[![../_images/properties_28_0.png](https://seaborn.pydata.org/_images/properties_28_0.png)](https://seaborn.pydata.org/_images/properties_28_0.png)

Size properties[#](https://seaborn.pydata.org/tutorial/properties.html#size-properties "Permalink to this heading")

--------------------------------------------------------------------------------------------------------------------

### pointsize[#](https://seaborn.pydata.org/tutorial/properties.html#pointsize "Permalink to this heading")

The `pointsize` property is relevant to dot marks and to line marks that can show markers at individual data points. The units correspond to the diameter of the mark in points.

Note that, while the parameterization corresponds to diameter, scales will be applied with a square root transform so that data values are linearly proportional to area:

[![../_images/properties_31_0.png](https://seaborn.pydata.org/_images/properties_31_0.png)](https://seaborn.pydata.org/_images/properties_31_0.png)

### linewidth[#](https://seaborn.pydata.org/tutorial/properties.html#linewidth "Permalink to this heading")

The `linewidth` property is relevant to line marks and determines their thickness. The value should be non-negative and has point units:

[![../_images/properties_33_0.png](https://seaborn.pydata.org/_images/properties_33_0.png)](https://seaborn.pydata.org/_images/properties_33_0.png)

### edgewidth[#](https://seaborn.pydata.org/tutorial/properties.html#edgewidth "Permalink to this heading")

The `edgewidth` property is akin to `linewidth` but applies to marks with an edge/fill rather than to lines. It also has a different default range when used in a scale. The units are the same:

[![../_images/properties_35_0.png](https://seaborn.pydata.org/_images/properties_35_0.png)](https://seaborn.pydata.org/_images/properties_35_0.png)

### stroke[#](https://seaborn.pydata.org/tutorial/properties.html#stroke "Permalink to this heading")

The `stroke` property is akin to `edgewidth` but applies when a dot mark is defined by its stroke rather than its fill. It also has a slightly different default scale range, but otherwise behaves similarly:

[![../_images/properties_37_0.png](https://seaborn.pydata.org/_images/properties_37_0.png)](https://seaborn.pydata.org/_images/properties_37_0.png)

Text properties[#](https://seaborn.pydata.org/tutorial/properties.html#text-properties "Permalink to this heading")

--------------------------------------------------------------------------------------------------------------------

### halign, valign[#](https://seaborn.pydata.org/tutorial/properties.html#halign-valign "Permalink to this heading")

The `halign` and `valign` properties control the _horizontal_ and _vertical_ alignment of text marks. The options for horizontal alignment are `'left'`, `'right'`, and `'center'`, while the options for vertical alignment are `'top'`, `'bottom'`, `'center'`, `'baseline'`, and `'center_baseline'`.

[![../_images/properties_40_0.png](https://seaborn.pydata.org/_images/properties_40_0.png)](https://seaborn.pydata.org/_images/properties_40_0.png)

### fontsize[#](https://seaborn.pydata.org/tutorial/properties.html#fontsize "Permalink to this heading")

The `fontsize` property controls the size of textual marks. The value has point units:

[![../_images/properties_42_0.png](https://seaborn.pydata.org/_images/properties_42_0.png)](https://seaborn.pydata.org/_images/properties_42_0.png)

### offset[#](https://seaborn.pydata.org/tutorial/properties.html#offset "Permalink to this heading")

The `offset` property controls the spacing between a text mark and its anchor position. It applies when _not_ using `center` alignment (i.e., when using left/right or top/bottom). The value has point units.

[![../_images/properties_44_0.png](https://seaborn.pydata.org/_images/properties_44_0.png)](https://seaborn.pydata.org/_images/properties_44_0.png)

Other properties[#](https://seaborn.pydata.org/tutorial/properties.html#other-properties "Permalink to this heading")

----------------------------------------------------------------------------------------------------------------------

### text[#](https://seaborn.pydata.org/tutorial/properties.html#text "Permalink to this heading")

The `text` property is used to set the content of a textual mark. It is always used literally (not mapped), and cast to string when necessary.

### group[#](https://seaborn.pydata.org/tutorial/properties.html#group "Permalink to this heading")

The `group` property is special in that it does not change anything about the mark’s appearance but defines additional data subsets that transforms should operate on independently.