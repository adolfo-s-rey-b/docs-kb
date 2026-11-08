 

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

seaborn.FacetGrid.savefig[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.savefig.html#seaborn-facetgrid-savefig "Permalink to this heading")

========================================================================================================================================================

FacetGrid.savefig(_\*args_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.savefig.html#seaborn.FacetGrid.savefig "Permalink to this definition")

Save an image of the plot.

This wraps [`matplotlib.figure.Figure.savefig()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.savefig "(in Matplotlib v3.8.2)")
, using bbox\_inches=”tight” by default. Parameters are passed through to the matplotlib function.