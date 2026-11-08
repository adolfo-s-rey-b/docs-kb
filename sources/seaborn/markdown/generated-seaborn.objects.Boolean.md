 

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

seaborn.objects.Boolean[#](https://seaborn.pydata.org/generated/seaborn.objects.Boolean.html#seaborn-objects-boolean "Permalink to this heading")

==================================================================================================================================================

_class_ seaborn.objects.Boolean(_values\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Boolean.html#seaborn.objects.Boolean "Permalink to this definition")

A scale with a discrete domain of True and False values.

The behavior is similar to the [`Nominal`](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "seaborn.objects.Nominal")
 scale, but property mappings and legends will use a \[True, False\] ordering rather than a sort using numeric rules. Coordinate variables accomplish this by inverting axis limits so as to maintain underlying numeric positioning. Input data are cast to boolean values, respecting missing data.

tick(_locator\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Boolean.html#seaborn.objects.Boolean.tick "Permalink to this definition")

label(_formatter\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Boolean.html#seaborn.objects.Boolean.label "Permalink to this definition")