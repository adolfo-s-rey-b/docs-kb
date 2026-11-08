 

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

seaborn.FacetGrid.tick\_params[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.tick_params.html#seaborn-facetgrid-tick-params "Permalink to this heading")

=====================================================================================================================================================================

FacetGrid.tick\_params(_axis\='both'_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.tick_params.html#seaborn.FacetGrid.tick_params "Permalink to this definition")

Modify the ticks, tick labels, and gridlines.

Parameters:

**axis**{‘x’, ‘y’, ‘both’}

The axis on which to apply the formatting.

**kwargs**keyword arguments

Additional keyword arguments to pass to [`matplotlib.axes.Axes.tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "(in Matplotlib v3.8.2)")
.

Returns:

**self**Grid instance

Returns self for easy chaining.