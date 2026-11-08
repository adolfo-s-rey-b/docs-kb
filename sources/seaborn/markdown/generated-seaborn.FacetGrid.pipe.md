 

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

seaborn.FacetGrid.pipe[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.pipe.html#seaborn-facetgrid-pipe "Permalink to this heading")

===============================================================================================================================================

FacetGrid.pipe(_func_, _\*args_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.pipe.html#seaborn.FacetGrid.pipe "Permalink to this definition")

Pass the grid to a user-supplied function and return its value.

The `func` must accept an object of this type for its first positional argument. Additional arguments are passed through. The return value of `func` becomes the return value of this method. See the `apply` method if you want to return self instead.

Added in v0.12.0.