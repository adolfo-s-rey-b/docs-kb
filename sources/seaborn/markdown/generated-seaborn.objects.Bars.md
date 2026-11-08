 

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

seaborn.objects.Bars[#](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn-objects-bars "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Bars(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<0.7>_, _fill=<True>_, _edgecolor=<rc:patch.edgecolor>_, _edgealpha=<1>_, _edgewidth=<auto>_, _edgestyle=<'-'>_, _width=<1>_, _baseline=<0>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn.objects.Bars "Permalink to this definition")

A faster bar mark with defaults more suitable for histograms.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgealpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)
, [edgestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [|width|](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#id1)
, [|baseline|](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#id3)

See also

[`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar")

A bar mark drawn between baseline and data values.

Examples

This mark draws bars between a baseline and a value. In contrast to [`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar")
, the bars have a full width and thin edges by default; this makes this mark a better choice for a continuous histogram:

p \= so.Plot(diamonds, "price").scale(x\="log")
p.add(so.Bars(), so.Hist())

Copy to clipboard

[![../_images/objects.Bars_1_0.png](https://seaborn.pydata.org/_images/objects.Bars_1_0.png)](https://seaborn.pydata.org/_images/objects.Bars_1_0.png)

When mapping the color or other properties, bars will overlap by default; this is usually confusing:

p.add(so.Bars(), so.Hist(), color\="cut")

Copy to clipboard

[![../_images/objects.Bars_3_0.png](https://seaborn.pydata.org/_images/objects.Bars_3_0.png)](https://seaborn.pydata.org/_images/objects.Bars_3_0.png)

Using a move transform, such as [`Stack`](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn.objects.Stack "seaborn.objects.Stack")
 or [`Dodge`](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "seaborn.objects.Dodge")
, will resolve the overlap (although faceting might often be a better approach):

p.add(so.Bars(), so.Hist(), so.Stack(), color\="cut")

Copy to clipboard

[![../_images/objects.Bars_5_0.png](https://seaborn.pydata.org/_images/objects.Bars_5_0.png)](https://seaborn.pydata.org/_images/objects.Bars_5_0.png)

A number of different properties can be set or mapped:

p.add(so.Bars(edgewidth\=0), so.Hist(), so.Stack(), alpha\="clarity")

Copy to clipboard

[![../_images/objects.Bars_7_0.png](https://seaborn.pydata.org/_images/objects.Bars_7_0.png)](https://seaborn.pydata.org/_images/objects.Bars_7_0.png)

It is possible to draw unfilled bars, but you must override the default edge color:

p.add(so.Bars(fill\=False, edgecolor\="C0", edgewidth\=1.5), so.Hist())

Copy to clipboard

[![../_images/objects.Bars_9_0.png](https://seaborn.pydata.org/_images/objects.Bars_9_0.png)](https://seaborn.pydata.org/_images/objects.Bars_9_0.png)

It is also possible to narrow the bars, which may be useful for dealing with overlap in some cases:

hist \= so.Hist(binwidth\=.075, binrange\=(2, 5))
(
    p.add(so.Bars(), hist)
    .add(
        so.Bars(color\=".9", width\=.5), hist,
        data\=diamonds.query("cut == 'Ideal'")
    )
)

Copy to clipboard

[![../_images/objects.Bars_11_0.png](https://seaborn.pydata.org/_images/objects.Bars_11_0.png)](https://seaborn.pydata.org/_images/objects.Bars_11_0.png)