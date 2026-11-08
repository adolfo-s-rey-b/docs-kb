 

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

seaborn.objects.Norm[#](https://seaborn.pydata.org/generated/seaborn.objects.Norm.html#seaborn-objects-norm "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Norm(_func\='max'_, _where\=None_, _by\=None_, _percent\=False_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Norm.html#seaborn.objects.Norm "Permalink to this definition")

Divisive scaling on the value axis after aggregating within groups.

Parameters:

**func**str or callable

Function called on each group to define the comparison value.

**where**str

Query string defining the subset used to define the comparison values.

**by**list of variables

Variables used to define aggregation groups.

**percent**bool

If True, multiply the result by 100.

Examples

By default, this transform scales each group relative to its maximum value:

(
    so.Plot(healthexp, x\="Year", y\="Spending\_USD", color\="Country")
    .add(so.Lines(), so.Norm())
    .label(y\="Spending relative to maximum amount")
)

Copy to clipboard

[![../_images/objects.Norm_1_0.png](https://seaborn.pydata.org/_images/objects.Norm_1_0.png)](https://seaborn.pydata.org/_images/objects.Norm_1_0.png)

Use `where` to constrain the values used to define a baseline, and `percent` to scale the output:

(
    so.Plot(healthexp, x\="Year", y\="Spending\_USD", color\="Country")
    .add(so.Lines(), so.Norm(where\="x == x.min()", percent\=True))
    .label(y\="Percent change in spending from 1970 baseline")
)

Copy to clipboard

[![../_images/objects.Norm_3_0.png](https://seaborn.pydata.org/_images/objects.Norm_3_0.png)](https://seaborn.pydata.org/_images/objects.Norm_3_0.png)