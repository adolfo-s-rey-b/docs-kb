 

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

seaborn.objects.Bar[#](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn-objects-bar "Permalink to this heading")

======================================================================================================================================

_class_ seaborn.objects.Bar(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<0.7>_, _fill=<True>_, _edgecolor=<depend:color>_, _edgealpha=<1>_, _edgewidth=<rc:patch.linewidth>_, _edgestyle=<'-'>_, _width=<0.8>_, _baseline=<0>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "Permalink to this definition")

A bar mark drawn between baseline and data values.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgealpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)
, [edgestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [|width|](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#id1)
, [|baseline|](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#id3)

See also

[`Bars`](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn.objects.Bars "seaborn.objects.Bars")

A faster bar mark with defaults more suitable for histograms.

Examples

The mark draws discrete bars from a baseline to provided values:

so.Plot(flights\["month"\], flights\["passengers"\]).add(so.Bar())

Copy to clipboard

[![../_images/objects.Bar_1_0.png](https://seaborn.pydata.org/_images/objects.Bar_1_0.png)](https://seaborn.pydata.org/_images/objects.Bar_1_0.png)

The bars are oriented depending on the x/y variable types and the `orient` parameter:

so.Plot(flights\["passengers"\], flights\["month"\]).add(so.Bar())

Copy to clipboard

[![../_images/objects.Bar_3_0.png](https://seaborn.pydata.org/_images/objects.Bar_3_0.png)](https://seaborn.pydata.org/_images/objects.Bar_3_0.png)

A common usecase will be drawing histograms on a variable with a nominal scale:

so.Plot(penguins, x\="species").add(so.Bar(), so.Hist())

Copy to clipboard

[![../_images/objects.Bar_5_0.png](https://seaborn.pydata.org/_images/objects.Bar_5_0.png)](https://seaborn.pydata.org/_images/objects.Bar_5_0.png)

When mapping additional variables, the bars will overlap by default:

so.Plot(penguins, x\="species", color\="sex").add(so.Bar(), so.Hist())

Copy to clipboard

[![../_images/objects.Bar_7_0.png](https://seaborn.pydata.org/_images/objects.Bar_7_0.png)](https://seaborn.pydata.org/_images/objects.Bar_7_0.png)

Apply a move transform, such as a [`Dodge`](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "seaborn.objects.Dodge")
 or [`Stack`](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn.objects.Stack "seaborn.objects.Stack")
 to resolve them:

so.Plot(penguins, x\="species", color\="sex").add(so.Bar(), so.Hist(), so.Dodge())

Copy to clipboard

[![../_images/objects.Bar_9_0.png](https://seaborn.pydata.org/_images/objects.Bar_9_0.png)](https://seaborn.pydata.org/_images/objects.Bar_9_0.png)

A number of properties can be mapped or set:

(
    so.Plot(
        penguins, x\="species",
        color\="sex", alpha\="sex", edgestyle\="sex",
    )
    .add(so.Bar(edgewidth\=2), so.Hist(), so.Dodge("fill"))
)

Copy to clipboard

[![../_images/objects.Bar_11_0.png](https://seaborn.pydata.org/_images/objects.Bar_11_0.png)](https://seaborn.pydata.org/_images/objects.Bar_11_0.png)

Combine with [`Range`](https://seaborn.pydata.org/generated/seaborn.objects.Range.html#seaborn.objects.Range "seaborn.objects.Range")
 to plot an estimate with errorbars:

(
    so.Plot(penguins, "body\_mass\_g", "species", color\="sex")
    .add(so.Bar(alpha\=.5), so.Agg(), so.Dodge())
    .add(so.Range(), so.Est(errorbar\="sd"), so.Dodge())
)

Copy to clipboard

[![../_images/objects.Bar_13_0.png](https://seaborn.pydata.org/_images/objects.Bar_13_0.png)](https://seaborn.pydata.org/_images/objects.Bar_13_0.png)