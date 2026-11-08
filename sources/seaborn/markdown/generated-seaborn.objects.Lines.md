 

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

seaborn.objects.Lines[#](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn-objects-lines "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Lines(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<1>_, _linewidth=<rc:lines.linewidth>_, _linestyle=<rc:lines.linestyle>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn.objects.Lines "Permalink to this definition")

A faster but less-flexible mark for drawing many lines.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)

See also

[`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")

A mark connecting data points with sorting along the orientation axis.

Examples

Like [`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")
, the mark draws a connecting line between sorted observations:

so.Plot(seaice, "Date", "Extent").add(so.Lines())

Copy to clipboard

[![../_images/objects.Lines_1_0.png](https://seaborn.pydata.org/_images/objects.Lines_1_0.png)](https://seaborn.pydata.org/_images/objects.Lines_1_0.png)

Compared to [`Line`](https://seaborn.pydata.org/generated/seaborn.objects.Line.html#seaborn.objects.Line "seaborn.objects.Line")
, this mark offers fewer settable properties, but it can have better performance when drawing a large number of lines:

(
    so.Plot(
        x\=seaice\["Date"\].dt.day\_of\_year,
        y\=seaice\["Extent"\],
        color\=seaice\["Date"\].dt.year
    )
    .facet(seaice\["Date"\].dt.year.round(\-1))
    .add(so.Lines(linewidth\=.5, color\="#bbca"), col\=None)
    .add(so.Lines(linewidth\=1))
    .scale(color\="ch:rot=-.2,light=.7")
    .layout(size\=(8, 4))
    .label(title\="{}s".format)
)

Copy to clipboard

[![../_images/objects.Lines_3_0.png](https://seaborn.pydata.org/_images/objects.Lines_3_0.png)](https://seaborn.pydata.org/_images/objects.Lines_3_0.png)