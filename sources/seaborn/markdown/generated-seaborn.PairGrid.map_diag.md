 

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

seaborn.PairGrid.map\_diag[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_diag.html#seaborn-pairgrid-map-diag "Permalink to this heading")

=========================================================================================================================================================

PairGrid.map\_diag(_func_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_diag.html#seaborn.PairGrid.map_diag "Permalink to this definition")

Plot with a univariate function on each diagonal subplot.

Parameters:

**func**callable plotting function

Must take an x array as a positional argument and draw onto the “currently active” matplotlib Axes. Also needs to accept kwargs called `color` and `label`.