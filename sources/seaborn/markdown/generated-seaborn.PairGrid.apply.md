 

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

seaborn.PairGrid.apply[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.apply.html#seaborn-pairgrid-apply "Permalink to this heading")

===============================================================================================================================================

PairGrid.apply(_func_, _\*args_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.apply.html#seaborn.PairGrid.apply "Permalink to this definition")

Pass the grid to a user-supplied function and return self.

The `func` must accept an object of this type for its first positional argument. Additional arguments are passed through. The return value of `func` is ignored; this method returns self. See the `pipe` method if you want the return value.

Added in v0.12.0.