 

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

seaborn.objects.Plot.pair[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html#seaborn-objects-plot-pair "Permalink to this heading")

========================================================================================================================================================

Plot.pair(_x\=None_, _y\=None_, _wrap\=None_, _cross\=True_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html#seaborn.objects.Plot.pair "Permalink to this definition")

Produce subplots by pairing multiple `x` and/or `y` variables.

Parameters:

**x, y**sequence(s) of data vectors or identifiers

Variables that will define the grid of subplots.

**wrap**int

When using only `x` or `y`, “wrap” subplots across a two-dimensional grid with this many columns (when using `x`) or rows (when using `y`).

**cross**bool

When False, zip the `x` and `y` lists such that the first subplot gets the first pair, the second gets the second pair, etc. Otherwise, create a two-dimensional grid from the cartesian product of the lists.

Examples

Plot one dependent variable against multiple independent variables by assigning `y` and pairing on `x`:

(
    so.Plot(mpg, y\="acceleration")
    .pair(x\=\["displacement", "weight"\])
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_2_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_2_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_2_0.png)

Show multiple pairwise relationships by passing lists to both `x` and `y`:

(
    so.Plot(mpg)
    .pair(x\=\["displacement", "weight"\], y\=\["horsepower", "acceleration"\])
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_4_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_4_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_4_0.png)

When providing lists for both `x` and `y`, pass `cross=False` to pair each position in the list rather than showing all pairwise relationships:

(
    so.Plot(mpg)
    .pair(
        x\=\["weight", "acceleration"\],
        y\=\["displacement", "horsepower"\],
        cross\=False,
    )
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_6_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_6_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_6_0.png)

When plotting against several `x` or `y` variables, it is possible to `wrap` the subplots to produce a two-dimensional grid:

(
    so.Plot(mpg, y\="mpg")
    .pair(x\=\["displacement", "weight", "horsepower", "cylinders"\], wrap\=2)
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_8_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_8_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_8_0.png)

Pairing can be combined with faceting, either pairing on `y` and faceting on `col` or pairing on `x` and faceting on `row`:

(
    so.Plot(mpg, x\="weight")
    .pair(y\=\["horsepower", "acceleration"\])
    .facet(col\="origin")
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_10_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_10_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_10_0.png)

While typically convenient to assign pairing variables as references to the common `data`, it’s also possible to pass a list of vectors:

(
    so.Plot(mpg\["weight"\])
    .pair(y\=\[mpg\["horsepower"\], mpg\["acceleration"\]\])
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_12_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_12_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_12_0.png)

When customizing the plot through methods like [`Plot.label()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html#seaborn.objects.Plot.label "seaborn.objects.Plot.label")
, [`Plot.limit()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.limit.html#seaborn.objects.Plot.limit "seaborn.objects.Plot.limit")
, or [`Plot.scale()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html#seaborn.objects.Plot.scale "seaborn.objects.Plot.scale")
, you can refer to the individual coordinate variables as `x0`, `x1`, etc.:

(
    so.Plot(mpg, y\="mpg")
    .pair(x\=\["weight", "displacement"\])
    .label(x0\="Weight (lb)", x1\="Displacement (cu in)", y\="MPG")
    .add(so.Dots())
)

Copy to clipboard

[![../_images/objects.Plot.pair_14_0.png](https://seaborn.pydata.org/_images/objects.Plot.pair_14_0.png)](https://seaborn.pydata.org/_images/objects.Plot.pair_14_0.png)