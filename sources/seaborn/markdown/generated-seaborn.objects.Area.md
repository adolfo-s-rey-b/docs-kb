 

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

seaborn.objects.Area[#](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#seaborn-objects-area "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Area(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<0.2>_, _fill=<True>_, _edgecolor=<depend:color>_, _edgealpha=<1>_, _edgewidth=<rc:patch.linewidth>_, _edgestyle=<'-'>_, _baseline=<0>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#seaborn.objects.Area "Permalink to this definition")

A fill mark drawn from a baseline to data values.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgealpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)
, [edgestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [|baseline|](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#id1)

See also

[`Band`](https://seaborn.pydata.org/generated/seaborn.objects.Band.html#seaborn.objects.Band "seaborn.objects.Band")

A fill mark representing an interval between values.

Examples

p \= so.Plot(healthexp, "Year", "Spending\_USD").facet("Country", wrap\=3)
p.add(so.Area())

Copy to clipboard

[![../_images/objects.Area_0_0.png](https://seaborn.pydata.org/_images/objects.Area_0_0.png)](https://seaborn.pydata.org/_images/objects.Area_0_0.png)

The `color` property sets both the edge and fill color:

p.add(so.Area(), color\="Country")

Copy to clipboard

[![../_images/objects.Area_2_0.png](https://seaborn.pydata.org/_images/objects.Area_2_0.png)](https://seaborn.pydata.org/_images/objects.Area_2_0.png)

It’s also possible to map only the `edgecolor`:

p.add(so.Area(color\=".5", edgewidth\=2), edgecolor\="Country")

Copy to clipboard

[![../_images/objects.Area_4_0.png](https://seaborn.pydata.org/_images/objects.Area_4_0.png)](https://seaborn.pydata.org/_images/objects.Area_4_0.png)

The mark is drawn as a polygon, but it can be combined with [`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")
 to draw a shaded region by setting `edgewidth=0`:

p.add(so.Area(edgewidth\=0)).add(so.Line())

Copy to clipboard

[![../_images/objects.Area_6_0.png](https://seaborn.pydata.org/_images/objects.Area_6_0.png)](https://seaborn.pydata.org/_images/objects.Area_6_0.png)

The layer’s orientation defines the axis that the mark fills from:

p.add(so.Area(), x\="Spending\_USD", y\="Year", orient\="y")

Copy to clipboard

[![../_images/objects.Area_8_0.png](https://seaborn.pydata.org/_images/objects.Area_8_0.png)](https://seaborn.pydata.org/_images/objects.Area_8_0.png)

This mark can be stacked to show part-whole relationships:

(
    so.Plot(healthexp, "Year", "Spending\_USD", color\="Country")
    .add(so.Area(alpha\=.7), so.Stack())
)

Copy to clipboard

[![../_images/objects.Area_10_0.png](https://seaborn.pydata.org/_images/objects.Area_10_0.png)](https://seaborn.pydata.org/_images/objects.Area_10_0.png)