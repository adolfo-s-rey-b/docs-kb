 

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

seaborn.objects.Plot.add[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn-objects-plot-add "Permalink to this heading")

=====================================================================================================================================================

Plot.add(_mark_, _\*transforms_, _orient\=None_, _legend\=True_, _label\=None_, _data\=None_, _\*\*variables_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "Permalink to this definition")

Specify a layer of the visualization in terms of mark and data transform(s).

This is the main method for specifying how the data should be visualized. It can be called multiple times with different arguments to define a plot with multiple layers.

Parameters:

**mark**[`Mark`](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html#seaborn.objects.Mark "seaborn.objects.Mark")

The visual representation of the data to use in this layer.

**transforms**[`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat")
 or [`Move`](https://seaborn.pydata.org/generated/seaborn.objects.Move.html#seaborn.objects.Move "seaborn.objects.Move")

Objects representing transforms to be applied before plotting the data. Currently, at most one [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat")
 can be used, and it must be passed first. This constraint will be relaxed in the future.

**orient**“x”, “y”, “v”, or “h”

The orientation of the mark, which also affects how transforms are computed. Typically corresponds to the axis that defines groups for aggregation. The “v” (vertical) and “h” (horizontal) options are synonyms for “x” / “y”, but may be more intuitive with some marks. When not provided, an orientation will be inferred from characteristics of the data and scales.

**legend**bool

Option to suppress the mark/mappings for this layer from the legend.

**label**str

A label to use for the layer in the legend, independent of any mappings.

**data**DataFrame or dict

Data source to override the global source provided in the constructor.

**variables**data vectors or identifiers

Additional layer-specific variables, including variables that will be passed directly to the transforms without scaling.

Examples

Every layer must be defined with a [`Mark`](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html#seaborn.objects.Mark "seaborn.objects.Mark")
:

p \= so.Plot(tips, "total\_bill", "tip").add(so.Dot())
p

Copy to clipboard

[![../_images/objects.Plot.add_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_1_0.png)

Call [`Plot.add`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add")
 multiple times to add multiple layers. In addition to the [`Mark`](https://seaborn.pydata.org/generated/seaborn.objects.Mark.html#seaborn.objects.Mark "seaborn.objects.Mark")
, layers can also be defined with [`Stat`](https://seaborn.pydata.org/generated/seaborn.objects.Stat.html#seaborn.objects.Stat "seaborn.objects.Stat")
 or [`Move`](https://seaborn.pydata.org/generated/seaborn.objects.Move.html#seaborn.objects.Move "seaborn.objects.Move")
 transforms:

p.add(so.Line(), so.PolyFit())

Copy to clipboard

[![../_images/objects.Plot.add_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_3_0.png)

Multiple transforms can be stacked into a pipeline.

(
    so.Plot(tips, y\="day", color\="sex")
    .add(so.Bar(), so.Hist(), so.Dodge())
)

Copy to clipboard

[![../_images/objects.Plot.add_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_5_0.png)

Layers have an “orientation”, which affects the transforms and some marks. The orientation is typically inferred from the variable types assigned to `x` and `y`, but it can be specified when it would otherwise be ambiguous:

(
    so.Plot(tips, x\="total\_bill", y\="size", color\="time")
    .add(so.Dot(alpha\=.5), so.Dodge(), so.Jitter(.4), orient\="y")
)

Copy to clipboard

[![../_images/objects.Plot.add_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_7_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_7_0.png)

Variables can be assigned to a specific layer. Note the distinction between how `pointsize` is passed to [`Plot.add`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add")
 — so it is _mapped_ by a scale — while `color` and `linewidth` are passed directly to [`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")
, so they directly set the line’s color and width:

(
    so.Plot(tips, "total\_bill", "tip")
    .add(so.Dots(), pointsize\="size")
    .add(so.Line(color\=".3", linewidth\=3), so.PolyFit())
    .scale(pointsize\=(2, 10))
)

Copy to clipboard

[![../_images/objects.Plot.add_9_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_9_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_9_0.png)

Variables that would otherwise apply to the entire plot can also be _excluded_ from a specific layer by setting their value to `None`:

(
    so.Plot(tips, "total\_bill", "tip", color\="day")
    .facet(col\="day")
    .add(so.Dot(color\="#aabc"), col\=None, color\=None)
    .add(so.Dot())
)

Copy to clipboard

[![../_images/objects.Plot.add_11_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_11_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_11_0.png)

Variables used only by the transforms _must_ be passed at the layer level:

(
    so.Plot(tips, "day")
    .add(so.Bar(), so.Hist(), weight\="size")
    .label(y\="Total patrons")
)

Copy to clipboard

[![../_images/objects.Plot.add_13_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_13_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_13_0.png)

Each layer can be provided with its own data source. If a data source was provided in the constructor, the layer data will be joined using its index:

(
    so.Plot(tips, "total\_bill", "tip")
    .add(so.Dot(color\="#aabc"))
    .add(so.Dot(), data\=tips.query("size == 2"), color\="time")
)

Copy to clipboard

[![../_images/objects.Plot.add_15_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_15_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_15_0.png)

Providing a `label` will annotate the layer in the plot’s legend:

(
    so.Plot(tips, x\="size")
    .add(so.Line(color\="C1"), so.Agg(), y\="total\_bill", label\="Bill")
    .add(so.Line(color\="C2"), so.Agg(), y\="tip", label\="Tip")
    .label(y\="Value")
)

Copy to clipboard

[![../_images/objects.Plot.add_17_0.png](https://seaborn.pydata.org/_images/objects.Plot.add_17_0.png)](https://seaborn.pydata.org/_images/objects.Plot.add_17_0.png)