 

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

seaborn.objects.Plot.share[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.share.html#seaborn-objects-plot-share "Permalink to this heading")

===========================================================================================================================================================

Plot.share(_\*\*shares_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.share.html#seaborn.objects.Plot.share "Permalink to this definition")

Control sharing of axis limits and ticks across subplots.

Keywords correspond to variables defined in the plot, and values can be boolean (to share across all subplots), or one of “row” or “col” (to share more selectively across one dimension of a grid).

Behavior for non-coordinate variables is currently undefined.

Examples

By default, faceted plots will share all axes:

p \= (
    so.Plot(penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
    .facet(col\="species", row\="sex")
    .add(so.Dots())
)
p

Copy to clipboard

[![../_images/objects.Plot.share_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.share_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.share_1_0.png)

Set a coordinate variable to `False` to let each subplot adapt independently:

p.share(x\=False, y\=False)

Copy to clipboard

[![../_images/objects.Plot.share_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.share_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.share_3_0.png)

It’s also possible to share only across rows or columns:

p.share(x\="col", y\="row")

Copy to clipboard

[![../_images/objects.Plot.share_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.share_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.share_5_0.png)

This method is also relevant for paired plots, which have different defaults. In this case, you would need to opt _in_ to full sharing (although it may not always make sense):

(
    so.Plot(penguins, y\="flipper\_length\_mm")
    .pair(x\=\["bill\_length\_mm", "bill\_depth\_mm"\])
    .add(so.Dots())
    .share(x\=True)
)

Copy to clipboard

[![../_images/objects.Plot.share_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.share_7_0.png)](https://seaborn.pydata.org/_images/objects.Plot.share_7_0.png)