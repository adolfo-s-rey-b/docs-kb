 

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

seaborn.FacetGrid.facet\_data[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.facet_data.html#seaborn-facetgrid-facet-data "Permalink to this heading")

==================================================================================================================================================================

FacetGrid.facet\_data()[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.facet_data.html#seaborn.FacetGrid.facet_data "Permalink to this definition")

Generator for name indices and data subsets for each facet.

Yields:

**(i, j, k), data\_ijk**tuple of ints, DataFrame

The ints provide an index into the {row, col, hue}\_names attribute, and the dataframe contains a subset of the full data corresponding to each facet. The generator yields subsets that correspond with the self.axes.flat iterator, or self.axes\[i, j\] when `col_wrap` is None.