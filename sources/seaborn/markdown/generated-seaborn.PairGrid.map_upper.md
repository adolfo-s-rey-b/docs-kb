 

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

seaborn.PairGrid.map\_upper[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_upper.html#seaborn-pairgrid-map-upper "Permalink to this heading")

============================================================================================================================================================

PairGrid.map\_upper(_func_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_upper.html#seaborn.PairGrid.map_upper "Permalink to this definition")

Plot with a bivariate function on the upper diagonal subplots.

Parameters:

**func**callable plotting function

Must take x, y arrays as positional arguments and draw onto the “currently active” matplotlib Axes. Also needs to accept kwargs called `color` and `label`.