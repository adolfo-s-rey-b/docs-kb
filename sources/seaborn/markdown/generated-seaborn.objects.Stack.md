 

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

seaborn.objects.Stack[#](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn-objects-stack "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Stack[#](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn.objects.Stack "Permalink to this definition")

Displacement of overlapping bar or area marks along the value axis.

Examples

This transform applies a vertical shift to eliminate overlap between marks with a baseline, such as [`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar")
 or [`Area`](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#seaborn.objects.Area "seaborn.objects.Area")
:

so.Plot(titanic, x\="class", color\="sex").add(so.Bar(), so.Count(), so.Stack())

Copy to clipboard

[![../_images/objects.Stack_1_0.png](https://seaborn.pydata.org/_images/objects.Stack_1_0.png)](https://seaborn.pydata.org/_images/objects.Stack_1_0.png)

Stacking can make it much harder to compare values between groups that get shifted, but it can work well when depicting a part-whole relationship:

(
    so.Plot(titanic, x\="age", alpha\="alive")
    .facet("sex")
    .add(so.Bars(), so.Hist(binwidth\=10), so.Stack())
)

Copy to clipboard

[![../_images/objects.Stack_3_0.png](https://seaborn.pydata.org/_images/objects.Stack_3_0.png)](https://seaborn.pydata.org/_images/objects.Stack_3_0.png)