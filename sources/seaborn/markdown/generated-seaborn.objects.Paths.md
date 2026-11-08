 

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

seaborn.objects.Paths[#](https://seaborn.pydata.org/generated/seaborn.objects.Paths.html#seaborn-objects-paths "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Paths(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<1>_, _linewidth=<rc:lines.linewidth>_, _linestyle=<rc:lines.linestyle>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Paths.html#seaborn.objects.Paths "Permalink to this definition")

A faster but less-flexible mark for drawing many paths.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)

See also

[`Path`](https://seaborn.pydata.org/generated/seaborn.objects.Path.html#seaborn.objects.Path "seaborn.objects.Path")

A mark connecting data points in the order they appear.

Examples

Unlike [`Lines`](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn.objects.Lines "seaborn.objects.Lines")
, this mark does not sort observations before plotting, making it suitable for plotting trajectories through a variable space:

p \= (
    so.Plot(networks)
    .pair(
        x\=\["5", "8", "12", "15"\],
        y\=\["6", "13", "16"\],
    )
    .layout(size\=(8, 5))
    .share(x\=True, y\=True)
)
p.add(so.Paths())

Copy to clipboard

[![../_images/objects.Paths_1_0.png](https://seaborn.pydata.org/_images/objects.Paths_1_0.png)](https://seaborn.pydata.org/_images/objects.Paths_1_0.png)

The mark has the same set of properties as [`Lines`](https://seaborn.pydata.org/generated/seaborn.objects.Lines.html#seaborn.objects.Lines "seaborn.objects.Lines")
:

p.add(so.Paths(linewidth\=1, alpha\=.8), color\="hemi")

Copy to clipboard

[![../_images/objects.Paths_3_0.png](https://seaborn.pydata.org/_images/objects.Paths_3_0.png)](https://seaborn.pydata.org/_images/objects.Paths_3_0.png)