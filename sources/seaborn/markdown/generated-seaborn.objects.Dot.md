 

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

seaborn.objects.Dot[#](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn-objects-dot "Permalink to this heading")

======================================================================================================================================

_class_ seaborn.objects.Dot(_artist\_kws=<factory>_, _marker=<'o'>_, _pointsize=<6>_, _stroke=<0.75>_, _color=<'C0'>_, _alpha=<1>_, _fill=<True>_, _edgecolor=<depend:color>_, _edgealpha=<depend:alpha>_, _edgewidth=<0.5>_, _edgestyle=<'-'>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn.objects.Dot "Permalink to this definition")

A mark suitable for dot plots or less-dense scatterplots.

This mark defines the following properties:

[marker](https://seaborn.pydata.org/tutorial/properties.html#marker-property)
, [pointsize](https://seaborn.pydata.org/tutorial/properties.html#pointsize-property)
, [stroke](https://seaborn.pydata.org/tutorial/properties.html#stroke-property)
, [color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgealpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)
, [edgestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)

See also

[`Dots`](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html#seaborn.objects.Dots "seaborn.objects.Dots")

A dot mark defined by strokes to better handle overplotting.

Examples

This mark draws relatively large, filled dots by default:

p1 \= so.Plot(tips, "total\_bill", "tip")
p1.add(so.Dot())

Copy to clipboard

[![../_images/objects.Dot_1_0.png](https://seaborn.pydata.org/_images/objects.Dot_1_0.png)](https://seaborn.pydata.org/_images/objects.Dot_1_0.png)

While [`Dots`](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html#seaborn.objects.Dots "seaborn.objects.Dots")
 is a better choice for dense scatter plots, adding a thin edge can help to resolve individual points:

p1.add(so.Dot(edgecolor\="w"))

Copy to clipboard

[![../_images/objects.Dot_3_0.png](https://seaborn.pydata.org/_images/objects.Dot_3_0.png)](https://seaborn.pydata.org/_images/objects.Dot_3_0.png)

Dodging and jittering can also help to reduce overplotting, when appropriate:

(
    so.Plot(tips, "total\_bill", "day", color\="sex")
    .add(so.Dot(), so.Dodge(), so.Jitter(.2))
)

Copy to clipboard

[![../_images/objects.Dot_5_0.png](https://seaborn.pydata.org/_images/objects.Dot_5_0.png)](https://seaborn.pydata.org/_images/objects.Dot_5_0.png)

The larger dot size makes this mark well suited to representing values along a nominal scale:

p2 \= so.Plot(glue, "Score", "Model").facet("Task", wrap\=4).limit(x\=(\-5, 105))
p2.add(so.Dot())

Copy to clipboard

[![../_images/objects.Dot_7_0.png](https://seaborn.pydata.org/_images/objects.Dot_7_0.png)](https://seaborn.pydata.org/_images/objects.Dot_7_0.png)

A number of properties can be set or mapped:

(
    p2
    .add(so.Dot(pointsize\=6), color\="Year", marker\="Encoder")
    .scale(marker\=\["o", "s"\], color\="flare")
)

Copy to clipboard

[![../_images/objects.Dot_9_0.png](https://seaborn.pydata.org/_images/objects.Dot_9_0.png)](https://seaborn.pydata.org/_images/objects.Dot_9_0.png)

Note that the edge properties are parameterized differently for filled and unfilled markers; use `stroke` and `color` rather than `edgewidth` and `edgecolor` if the marker is unfilled:

p2.add(so.Dot(stroke\=1.5), fill\="Encoder", color\="Encoder")

Copy to clipboard

[![../_images/objects.Dot_11_0.png](https://seaborn.pydata.org/_images/objects.Dot_11_0.png)](https://seaborn.pydata.org/_images/objects.Dot_11_0.png)

Combine with [`Range`](https://seaborn.pydata.org/generated/seaborn.objects.Range.html#seaborn.objects.Range "seaborn.objects.Range")
 to show error bars:

(
    so.Plot(tips, x\="total\_bill", y\="day")
    .add(so.Dot(pointsize\=3), so.Shift(y\=.2), so.Jitter(.2))
    .add(so.Dot(), so.Agg())
    .add(so.Range(), so.Est(errorbar\=("se", 2)))
)

Copy to clipboard

[![../_images/objects.Dot_13_0.png](https://seaborn.pydata.org/_images/objects.Dot_13_0.png)](https://seaborn.pydata.org/_images/objects.Dot_13_0.png)