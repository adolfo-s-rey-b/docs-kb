 

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

seaborn.objects.Dash[#](https://seaborn.pydata.org/generated/seaborn.objects.Dash.html#seaborn-objects-dash "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Dash(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<1>_, _linewidth=<rc:lines.linewidth>_, _linestyle=<rc:lines.linestyle>_, _width=<0.8>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Dash.html#seaborn.objects.Dash "Permalink to this definition")

A line mark drawn as an oriented segment for each datapoint.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [|width|](https://seaborn.pydata.org/generated/seaborn.objects.Dash.html#id1)

Examples

A line segment is drawn for each datapoint, centered on the value along the orientation axis:

p \= so.Plot(penguins, "species", "body\_mass\_g", color\="sex")
p.add(so.Dash())

Copy to clipboard

[![../_images/objects.Dash_1_0.png](https://seaborn.pydata.org/_images/objects.Dash_1_0.png)](https://seaborn.pydata.org/_images/objects.Dash_1_0.png)

A number of properties can be mapped or set directly:

p.add(so.Dash(alpha\=.5), linewidth\="flipper\_length\_mm")

Copy to clipboard

[![../_images/objects.Dash_3_0.png](https://seaborn.pydata.org/_images/objects.Dash_3_0.png)](https://seaborn.pydata.org/_images/objects.Dash_3_0.png)

The mark has a `width` property, which is relative to the spacing between orientation values:

p.add(so.Dash(width\=.5))

Copy to clipboard

[![../_images/objects.Dash_5_0.png](https://seaborn.pydata.org/_images/objects.Dash_5_0.png)](https://seaborn.pydata.org/_images/objects.Dash_5_0.png)

When dodged, the width will automatically adapt:

p.add(so.Dash(), so.Dodge())

Copy to clipboard

[![../_images/objects.Dash_7_0.png](https://seaborn.pydata.org/_images/objects.Dash_7_0.png)](https://seaborn.pydata.org/_images/objects.Dash_7_0.png)

This mark works well to show aggregate values when paired with a strip plot:

(
    p
    .add(so.Dash(), so.Agg(), so.Dodge())
    .add(so.Dots(), so.Dodge(), so.Jitter())
)

Copy to clipboard

[![../_images/objects.Dash_9_0.png](https://seaborn.pydata.org/_images/objects.Dash_9_0.png)](https://seaborn.pydata.org/_images/objects.Dash_9_0.png)

When both coordinate variables are numeric, you can control the orientation explicitly:

(
    so.Plot(
        penguins\["body\_mass\_g"\],
        penguins\["flipper\_length\_mm"\].round(\-1),
    )
    .add(so.Dash(), orient\="y")
)

Copy to clipboard

[![../_images/objects.Dash_11_0.png](https://seaborn.pydata.org/_images/objects.Dash_11_0.png)](https://seaborn.pydata.org/_images/objects.Dash_11_0.png)