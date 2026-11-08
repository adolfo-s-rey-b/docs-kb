 

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

seaborn.FacetGrid.map[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn-facetgrid-map "Permalink to this heading")

============================================================================================================================================

FacetGrid.map(_func_, _\*args_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map.html#seaborn.FacetGrid.map "Permalink to this definition")

Apply a plotting function to each facet’s subset of the data.

Parameters:

**func**callable

A plotting function that takes data and keyword arguments. It must plot to the currently active matplotlib Axes and take a `color` keyword argument. If faceting on the `hue` dimension, it must also take a `label` keyword argument.

**args**strings

Column names in self.data that identify variables with data to plot. The data for each variable is passed to `func` in the order the variables are specified in the call.

**kwargs**keyword arguments

All keyword arguments are passed to the plotting function.

Returns:

**self**object

Returns self.