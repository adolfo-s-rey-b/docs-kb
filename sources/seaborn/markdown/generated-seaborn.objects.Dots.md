 

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

seaborn.objects.Dots[#](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html#seaborn-objects-dots "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Dots(_artist\_kws=<factory>_, _marker=<rc:scatter.marker>_, _pointsize=<4>_, _stroke=<0.75>_, _color=<'C0'>_, _alpha=<1>_, _fill=<True>_, _fillcolor=<depend:color>_, _fillalpha=<0.2>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Dots.html#seaborn.objects.Dots "Permalink to this definition")

A dot mark defined by strokes to better handle overplotting.

This mark defines the following properties:

[marker](https://seaborn.pydata.org/tutorial/properties.html#marker-property)
, [pointsize](https://seaborn.pydata.org/tutorial/properties.html#pointsize-property)
, [stroke](https://seaborn.pydata.org/tutorial/properties.html#stroke-property)
, [color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [fillcolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [fillalpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)

See also

[`Dot`](https://seaborn.pydata.org/generated/seaborn.objects.Dot.html#seaborn.objects.Dot "seaborn.objects.Dot")

A mark suitable for dot plots or less-dense scatterplots.

Examples

This mark draws relatively small, partially-transparent dots:

p1 \= so.Plot(mpg, "horsepower", "mpg")
p1.add(so.Dots())

Copy to clipboard

[![../_images/objects.Dots_1_0.png](https://seaborn.pydata.org/_images/objects.Dots_1_0.png)](https://seaborn.pydata.org/_images/objects.Dots_1_0.png)

Fixing or mapping the `color` property changes both the stroke (edge) and fill:

p1.add(so.Dots(), color\="origin")

Copy to clipboard

[![../_images/objects.Dots_3_0.png](https://seaborn.pydata.org/_images/objects.Dots_3_0.png)](https://seaborn.pydata.org/_images/objects.Dots_3_0.png)

These properties can be independently parametrized (although the resulting plot may not always be clear):

(
    p1.add(so.Dots(fillalpha\=.5), color\="origin", fillcolor\="weight")
    .scale(fillcolor\="binary")
)

Copy to clipboard

[![../_images/objects.Dots_5_0.png](https://seaborn.pydata.org/_images/objects.Dots_5_0.png)](https://seaborn.pydata.org/_images/objects.Dots_5_0.png)

Filled and unfilled markers will happily mix:

p1.add(so.Dots(stroke\=1), marker\="origin").scale(marker\=\["o", "x", (6, 2, 1)\])

Copy to clipboard

[![../_images/objects.Dots_7_0.png](https://seaborn.pydata.org/_images/objects.Dots_7_0.png)](https://seaborn.pydata.org/_images/objects.Dots_7_0.png)

The partial opacity also helps to see local density when using jitter:

(
    so.Plot(mpg, "horsepower", "origin")
    .add(so.Dots(), so.Jitter(.25))
)

Copy to clipboard

[![../_images/objects.Dots_9_0.png](https://seaborn.pydata.org/_images/objects.Dots_9_0.png)](https://seaborn.pydata.org/_images/objects.Dots_9_0.png)