 

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

seaborn.objects.Band[#](https://seaborn.pydata.org/generated/seaborn.objects.Band.html#seaborn-objects-band "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Band(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<0.2>_, _fill=<True>_, _edgecolor=<depend:color>_, _edgealpha=<1>_, _edgewidth=<0>_, _edgestyle=<'-'>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Band.html#seaborn.objects.Band "Permalink to this definition")

A fill mark representing an interval between values.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgealpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)
, [edgestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)

See also

[`Area`](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#seaborn.objects.Area "seaborn.objects.Area")

A fill mark drawn from a baseline to data values.

Examples

The mark fills between pairs of data points to show an interval on the value axis:

p \= so.Plot(seaice, x\="Day", ymin\="1980", ymax\="2019")
p.add(so.Band())

Copy to clipboard

[![../_images/objects.Band_1_0.png](https://seaborn.pydata.org/_images/objects.Band_1_0.png)](https://seaborn.pydata.org/_images/objects.Band_1_0.png)

By default it draws a faint ribbon with no edges, but edges can be added:

p.add(so.Band(alpha\=.5, edgewidth\=2))

Copy to clipboard

[![../_images/objects.Band_3_0.png](https://seaborn.pydata.org/_images/objects.Band_3_0.png)](https://seaborn.pydata.org/_images/objects.Band_3_0.png)

The defaults are optimized for the main expected usecase, where the mark is combined with a line to show an errorbar interval:

(
    so.Plot(fmri, x\="timepoint", y\="signal", color\="event")
    .add(so.Band(), so.Est())
    .add(so.Line(), so.Agg())
)

Copy to clipboard

[![../_images/objects.Band_5_0.png](https://seaborn.pydata.org/_images/objects.Band_5_0.png)](https://seaborn.pydata.org/_images/objects.Band_5_0.png)

When min/max values are not explicitly assigned or added in a transform, the band will cover the full extent of the data:

(
    so.Plot(fmri, x\="timepoint", y\="signal", color\="event")
    .add(so.Line(linewidth\=.5), group\="subject")
    .add(so.Band())
)

Copy to clipboard

[![../_images/objects.Band_7_0.png](https://seaborn.pydata.org/_images/objects.Band_7_0.png)](https://seaborn.pydata.org/_images/objects.Band_7_0.png)