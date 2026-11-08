 

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

seaborn.objects.Count[#](https://seaborn.pydata.org/generated/seaborn.objects.Count.html#seaborn-objects-count "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Count[#](https://seaborn.pydata.org/generated/seaborn.objects.Count.html#seaborn.objects.Count "Permalink to this definition")

Count distinct observations within groups.

See also

[`Hist`](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn.objects.Hist "seaborn.objects.Hist")

A more fully-featured transform including binning and/or normalization.

Examples

The transform counts distinct observations of the orientation variable defines a new variable on the opposite axis:

so.Plot(tips, x\="day").add(so.Bar(), so.Count())

Copy to clipboard

[![../_images/objects.Count_1_0.png](https://seaborn.pydata.org/_images/objects.Count_1_0.png)](https://seaborn.pydata.org/_images/objects.Count_1_0.png)

When additional mapping variables are defined, they are also used to define groups:

so.Plot(tips, x\="day", color\="sex").add(so.Bar(), so.Count(), so.Dodge())

Copy to clipboard

[![../_images/objects.Count_3_0.png](https://seaborn.pydata.org/_images/objects.Count_3_0.png)](https://seaborn.pydata.org/_images/objects.Count_3_0.png)

Unlike [`Hist`](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn.objects.Hist "seaborn.objects.Hist")
, numeric data are not binned before counting:

so.Plot(tips, x\="size").add(so.Bar(), so.Count())

Copy to clipboard

[![../_images/objects.Count_5_0.png](https://seaborn.pydata.org/_images/objects.Count_5_0.png)](https://seaborn.pydata.org/_images/objects.Count_5_0.png)

When the `y` variable is defined, the counts are assigned to the `x` variable:

so.Plot(tips, y\="size").add(so.Bar(), so.Count())

Copy to clipboard

[![../_images/objects.Count_7_0.png](https://seaborn.pydata.org/_images/objects.Count_7_0.png)](https://seaborn.pydata.org/_images/objects.Count_7_0.png)