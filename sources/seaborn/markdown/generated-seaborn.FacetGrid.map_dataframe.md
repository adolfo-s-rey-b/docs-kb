 

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

seaborn.FacetGrid.map\_dataframe[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html#seaborn-facetgrid-map-dataframe "Permalink to this heading")

===========================================================================================================================================================================

FacetGrid.map\_dataframe(_func_, _\*args_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.map_dataframe.html#seaborn.FacetGrid.map_dataframe "Permalink to this definition")

Like `.map` but passes args as strings and inserts data in kwargs.

This method is suitable for plotting with functions that accept a long-form DataFrame as a `data` keyword argument and access the data in that DataFrame using string variable names.

Parameters:

**func**callable

A plotting function that takes data and keyword arguments. Unlike the `map` method, a function used here must “understand” Pandas objects. It also must plot to the currently active matplotlib Axes and take a `color` keyword argument. If faceting on the `hue` dimension, it must also take a `label` keyword argument.

**args**strings

Column names in self.data that identify variables with data to plot. The data for each variable is passed to `func` in the order the variables are specified in the call.

**kwargs**keyword arguments

All keyword arguments are passed to the plotting function.

Returns:

**self**object

Returns self.