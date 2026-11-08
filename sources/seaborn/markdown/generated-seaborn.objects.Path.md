 

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

seaborn.objects.Path[#](https://seaborn.pydata.org/generated/seaborn.objects.Path.html#seaborn-objects-path "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Path(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<1>_, _linewidth=<rc:lines.linewidth>_, _linestyle=<rc:lines.linestyle>_, _marker=<rc:lines.marker>_, _pointsize=<rc:lines.markersize>_, _fillcolor=<depend:color>_, _edgecolor=<depend:color>_, _edgewidth=<rc:lines.markeredgewidth>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Path.html#seaborn.objects.Path "Permalink to this definition")

A mark connecting data points in the order they appear.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [marker](https://seaborn.pydata.org/tutorial/properties.html#marker-property)
, [pointsize](https://seaborn.pydata.org/tutorial/properties.html#pointsize-property)
, [fillcolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)

See also

[`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")

A mark connecting data points with sorting along the orientation axis.

[`Paths`](https://seaborn.pydata.org/generated/seaborn.objects.Paths.html#seaborn.objects.Paths "seaborn.objects.Paths")

A faster but less-flexible mark for drawing many paths.

Examples

Unlike [`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")
, this mark does not sort observations before plotting, making it suitable for plotting trajectories through a variable space:

p \= so.Plot(healthexp, "Spending\_USD", "Life\_Expectancy", color\="Country")
p.add(so.Path())

Copy to clipboard

[![../_images/objects.Path_1_0.png](https://seaborn.pydata.org/_images/objects.Path_1_0.png)](https://seaborn.pydata.org/_images/objects.Path_1_0.png)

It otherwise offers the same set of options, including a number of properties that can be set or mapped:

p.add(so.Path(marker\="o", pointsize\=2, linewidth\=.75, fillcolor\="w"))

Copy to clipboard

[![../_images/objects.Path_3_0.png](https://seaborn.pydata.org/_images/objects.Path_3_0.png)](https://seaborn.pydata.org/_images/objects.Path_3_0.png)