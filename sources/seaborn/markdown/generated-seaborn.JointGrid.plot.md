 

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

seaborn.JointGrid.plot[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html#seaborn-jointgrid-plot "Permalink to this heading")

===============================================================================================================================================

JointGrid.plot(_joint\_func_, _marginal\_func_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html#seaborn.JointGrid.plot "Permalink to this definition")

Draw the plot by passing functions for joint and marginal axes.

This method passes the `kwargs` dictionary to both functions. If you need more control, call [`JointGrid.plot_joint()`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html#seaborn.JointGrid.plot_joint "seaborn.JointGrid.plot_joint")
 and [`JointGrid.plot_marginals()`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html#seaborn.JointGrid.plot_marginals "seaborn.JointGrid.plot_marginals")
 directly with specific parameters.

Parameters:

**joint\_func, marginal\_func**callables

Functions to draw the bivariate and univariate plots. See methods referenced above for information about the required characteristics of these functions.

**kwargs**

Additional keyword arguments are passed to both functions.

Returns:

[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 instance

Returns `self` for easy method chaining.