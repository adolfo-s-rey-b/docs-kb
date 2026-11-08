 

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

seaborn.objects.Agg[#](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html#seaborn-objects-agg "Permalink to this heading")

======================================================================================================================================

_class_ seaborn.objects.Agg(_func\='mean'_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Agg.html#seaborn.objects.Agg "Permalink to this definition")

Aggregate data along the value axis using given method.

Parameters:

**func**str or callable

Name of a [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "(in pandas v2.2.0)")
 method or a vector -> scalar function.

See also

`objects.Est`

Aggregation with error bars.

Examples

The default behavior is to aggregate by taking a mean over each group:

p \= so.Plot(diamonds, "clarity", "carat")
p.add(so.Bar(), so.Agg())

Copy to clipboard

[![../_images/objects.Agg_1_0.png](https://seaborn.pydata.org/_images/objects.Agg_1_0.png)](https://seaborn.pydata.org/_images/objects.Agg_1_0.png)

Other aggregation functions can be selected by name if they are pandas methods:

p.add(so.Bar(), so.Agg("median"))

Copy to clipboard

[![../_images/objects.Agg_3_0.png](https://seaborn.pydata.org/_images/objects.Agg_3_0.png)](https://seaborn.pydata.org/_images/objects.Agg_3_0.png)

It’s also possible to pass an arbitrary aggregation function:

p.add(so.Bar(), so.Agg(lambda x: x.quantile(.75) \- x.quantile(.25)))

Copy to clipboard

[![../_images/objects.Agg_5_0.png](https://seaborn.pydata.org/_images/objects.Agg_5_0.png)](https://seaborn.pydata.org/_images/objects.Agg_5_0.png)

When other mapping variables are assigned, they’ll be used to define aggregation groups. With some marks, it may be helpful to use additional transforms, such as [`Dodge`](https://seaborn.pydata.org/generated/seaborn.objects.Dodge.html#seaborn.objects.Dodge "seaborn.objects.Dodge")
:

p.add(so.Bar(), so.Agg(), so.Dodge(), color\="cut")

Copy to clipboard

[![../_images/objects.Agg_7_0.png](https://seaborn.pydata.org/_images/objects.Agg_7_0.png)](https://seaborn.pydata.org/_images/objects.Agg_7_0.png)

The variable that gets aggregated depends on the orientation of the layer, which is usually inferred from the coordinate variable types (but may also be specified with the `orient` parameter in [`Plot.add()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add")
):

so.Plot(diamonds, "carat", "clarity").add(so.Bar(), so.Agg())

Copy to clipboard

[![../_images/objects.Agg_9_0.png](https://seaborn.pydata.org/_images/objects.Agg_9_0.png)](https://seaborn.pydata.org/_images/objects.Agg_9_0.png)