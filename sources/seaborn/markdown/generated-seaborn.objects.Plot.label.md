 

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

seaborn.objects.Plot.label[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html#seaborn-objects-plot-label "Permalink to this heading")

===========================================================================================================================================================

Plot.label(_\*_, _title\=None_, _legend\=None_, _\*\*variables_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html#seaborn.objects.Plot.label "Permalink to this definition")

Control the labels and titles for axes, legends, and subplots.

Additional keywords correspond to variables defined in the plot. Values can be one of the following types:

*   string (used literally; pass “” to clear the default label)
    
*   function (called on the default label)
    

For coordinate variables, the value sets the axis label. For semantic variables, the value sets the legend title. For faceting variables, `title=` modifies the subplot-specific label, while `col=` and/or `row=` add a label for the faceting variable.

When using a single subplot, `title=` sets its title.

The `legend=` parameter sets the title for the “layer” legend (i.e., when using `label` in [`Plot.add()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add")
).

Examples

Use strings to override default labels:

p \= (
    so.Plot(penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
    .add(so.Dot(), color\="species")
)
p.label(x\="Length", y\="Depth", color\="")

Copy to clipboard

[![../_images/objects.Plot.label_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_1_0.png)

Pass a function to _modify_ the default label:

p.label(color\=str.capitalize)

Copy to clipboard

[![../_images/objects.Plot.label_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_3_0.png)

Use this method to set the title for a single-axes plot:

p.label(title\="Penguin species exhibit distinct bill shapes")

Copy to clipboard

[![../_images/objects.Plot.label_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_5_0.png)

When faceting, the `title` parameter will modify default titles:

p.facet("sex").label(title\=str.upper)

Copy to clipboard

[![../_images/objects.Plot.label_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_7_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_7_0.png)

And the `col`/`row` parameters will add labels to the title for each facet:

p.facet("sex").label(col\="Sex:")

Copy to clipboard

[![../_images/objects.Plot.label_9_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_9_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_9_0.png)

If more customization is needed, a format string can work well:

p.facet("sex").label(title\="{} penguins".format)

Copy to clipboard

[![../_images/objects.Plot.label_11_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_11_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_11_0.png)

p

Copy to clipboard

[![../_images/objects.Plot.label_12_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_12_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_12_0.png)

When adding labels for each layer, the `legend=` parameter sets the title for the legend:

(
    so.Plot(penguins, x\="species")
    .add(so.Line(color\="C1"), so.Agg(), y\="bill\_length\_mm", label\="length")
    .add(so.Line(color\="C2"), so.Agg(), y\="bill\_depth\_mm", label\="depth")
    .label(legend\="Measurement")
)

Copy to clipboard

[![../_images/objects.Plot.label_14_0.png](https://seaborn.pydata.org/_images/objects.Plot.label_14_0.png)](https://seaborn.pydata.org/_images/objects.Plot.label_14_0.png)