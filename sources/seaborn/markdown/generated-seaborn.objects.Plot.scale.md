 

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

seaborn.objects.Plot.scale[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html#seaborn-objects-plot-scale "Permalink to this heading")

===========================================================================================================================================================

Plot.scale(_\*\*scales_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html#seaborn.objects.Plot.scale "Permalink to this definition")

Specify mappings from data units to visual properties.

Keywords correspond to variables defined in the plot, including coordinate variables (`x`, `y`) and semantic variables (`color`, `pointsize`, etc.).

A number of “magic” arguments are accepted, including:

*   The name of a transform (e.g., `"log"`, `"sqrt"`)
    
*   The name of a palette (e.g., `"viridis"`, `"muted"`)
    
*   A tuple of values, defining the output range (e.g. `(1, 5)`)
    
*   A dict, implying a [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
     scale (e.g. `{"a": .2, "b": .5}`)
    
*   A list of values, implying a [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
     scale (e.g. `["b", "r"]`)
    

For more explicit control, pass a scale spec object such as [`Continuous`](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous "seaborn.objects.Continuous")
 or [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
. Or pass `None` to use an “identity” scale, which treats data values as literally encoding visual properties.

Examples

Passing the name of a function, such as `"log"` or `"symlog"` will set the scale’s transform:

p1 \= so.Plot(diamonds, x\="carat", y\="price")
p1.add(so.Dots()).scale(y\="log")

Copy to clipboard

[![../_images/objects.Plot.scale_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_1_0.png)

String arguments can also specify the the name of a palette that defines the output values (or “range”) of the scale:

p1.add(so.Dots(), color\="clarity").scale(color\="crest")

Copy to clipboard

[![../_images/objects.Plot.scale_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_3_0.png)

The scale’s range can alternatively be specified as a tuple of min/max values:

p1.add(so.Dots(), pointsize\="carat").scale(pointsize\=(2, 10))

Copy to clipboard

[![../_images/objects.Plot.scale_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_5_0.png)

The tuple format can also be used for a color scale:

p1.add(so.Dots(), color\="carat").scale(color\=(".4", "#68d"))

Copy to clipboard

[![../_images/objects.Plot.scale_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_7_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_7_0.png)

For more control pass a scale object, such as [`Continuous`](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous "seaborn.objects.Continuous")
, which allows you to specify the input domain (`norm`), output range (`values`), and nonlinear transform (`trans`):

(
    p1.add(so.Dots(), color\="carat")
    .scale(color\=so.Continuous((".4", "#68d"), norm\=(1, 3), trans\="sqrt"))
)

Copy to clipboard

[![../_images/objects.Plot.scale_9_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_9_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_9_0.png)

The scale objects also offer an interface for configuring the location of the scale ticks (including in the legend) and the formatting of the tick labels:

(
    p1.add(so.Dots(), color\="price")
    .scale(
        x\=so.Continuous(trans\="sqrt").tick(every\=.5),
        y\=so.Continuous().label(like\="${x:g}"),
        color\=so.Continuous("ch:.2").tick(upto\=4).label(unit\=""),
    )
    .label(y\="")
)

Copy to clipboard

[![../_images/objects.Plot.scale_11_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_11_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_11_0.png)

If the scale includes a nonlinear transform, it will be applied _before_ any statistical transforms:

(
    p1.add(so.Dots(color\=".7"))
    .add(so.Line(), so.PolyFit(order\=2))
    .scale(y\="log")
    .limit(y\=(250, 25000))
)

Copy to clipboard

[![../_images/objects.Plot.scale_13_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_13_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_13_0.png)

The scale is also relevant for when numerical data should be treated as categories. Consider the following histogram:

p2 \= so.Plot(mpg, "cylinders").add(so.Bar(), so.Hist())
p2

Copy to clipboard

[![../_images/objects.Plot.scale_15_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_15_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_15_0.png)

By default, the plot gives `cylinders` a continuous scale, since it is a vector of floats. But assigning a [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
 scale causes the histogram to bin observations properly:

p2.scale(x\=so.Nominal())

Copy to clipboard

[![../_images/objects.Plot.scale_17_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_17_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_17_0.png)

The default behavior for semantic mappings also depends on input data types and can be modified by the scale. Consider the sequential mapping applied to the colors in this plot:

p3 \= (
    so.Plot(mpg, "weight", "acceleration", color\="cylinders")
    .add(so.Dot(), marker\="origin")
)
p3

Copy to clipboard

[![../_images/objects.Plot.scale_19_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_19_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_19_0.png)

Passing the name of a qualitative palette will select a [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
 scale:

p3.scale(color\="deep")

Copy to clipboard

[![../_images/objects.Plot.scale_21_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_21_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_21_0.png)

A [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
 scale is also implied when the output values are given as a list or dictionary:

p3.scale(
    color\=\["#49b", "#a6a", "#5b8"\],
    marker\={"japan": ".", "europe": "+", "usa": "\*"},
)

Copy to clipboard

[![../_images/objects.Plot.scale_23_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_23_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_23_0.png)

Pass a [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
 object directly to control the order of the category mappings:

p3.scale(
    color\=so.Nominal(\["#008fd5", "#fc4f30", "#e5ae38"\]),
    marker\=so.Nominal(order\=\["japan", "europe", "usa"\])
)

Copy to clipboard

[![../_images/objects.Plot.scale_25_0.png](https://seaborn.pydata.org/_images/objects.Plot.scale_25_0.png)](https://seaborn.pydata.org/_images/objects.Plot.scale_25_0.png)