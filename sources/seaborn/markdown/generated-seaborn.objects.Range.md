 

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

seaborn.objects.Range[#](https://seaborn.pydata.org/generated/seaborn.objects.Range.html#seaborn-objects-range "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Range(_artist\_kws=<factory>_, _color=<'C0'>_, _alpha=<1>_, _linewidth=<rc:lines.linewidth>_, _linestyle=<rc:lines.linestyle>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Range.html#seaborn.objects.Range "Permalink to this definition")

An oriented line mark drawn between min/max values.

This mark defines the following properties:

[color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)

Examples

This mark will often be used in the context of a stat transform that adds an errorbar interval:

(
    so.Plot(penguins, x\="body\_mass\_g", y\="species", color\="sex")
    .add(so.Dot(), so.Agg(), so.Dodge())
    .add(so.Range(), so.Est(errorbar\="sd"), so.Dodge())
)

Copy to clipboard

[![../_images/objects.Range_1_0.png](https://seaborn.pydata.org/_images/objects.Range_1_0.png)](https://seaborn.pydata.org/_images/objects.Range_1_0.png)

One feature (or potential gotcha) is that the mark will pick up properties like `linestyle` and `linewidth`; exclude those properties from the relevant layer if this behavior is undesired:

(
    so.Plot(penguins, x\="sex", y\="body\_mass\_g", linestyle\="species")
    .facet("species")
    .add(so.Line(marker\="o"), so.Agg())
    .add(so.Range(), so.Est(errorbar\="sd"))
)

Copy to clipboard

[![../_images/objects.Range_3_0.png](https://seaborn.pydata.org/_images/objects.Range_3_0.png)](https://seaborn.pydata.org/_images/objects.Range_3_0.png)

It’s also possible to directly assign the minimum and maximum values for the range:

(
    penguins
    .rename\_axis(index\="penguin")
    .pipe(so.Plot, x\="penguin", ymin\="bill\_depth\_mm", ymax\="bill\_length\_mm")
    .add(so.Range(), color\="island")
)

Copy to clipboard

[![../_images/objects.Range_5_0.png](https://seaborn.pydata.org/_images/objects.Range_5_0.png)](https://seaborn.pydata.org/_images/objects.Range_5_0.png)

When `min`/`max` variables are neither computed as part of a transform or explicitly assigned, the range will cover the full extent of the data at each unique observation on the orient axis:

(
    so.Plot(penguins, x\="sex", y\="body\_mass\_g")
    .facet("species")
    .add(so.Dots(pointsize\=6))
    .add(so.Range(linewidth\=2))
)

Copy to clipboard

[![../_images/objects.Range_7_0.png](https://seaborn.pydata.org/_images/objects.Range_7_0.png)](https://seaborn.pydata.org/_images/objects.Range_7_0.png)