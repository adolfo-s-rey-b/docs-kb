 

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

seaborn.JointGrid.plot\_marginals[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html#seaborn-jointgrid-plot-marginals "Permalink to this heading")

==============================================================================================================================================================================

JointGrid.plot\_marginals(_func_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html#seaborn.JointGrid.plot_marginals "Permalink to this definition")

Draw univariate plots on each marginal axes.

Parameters:

**func**plotting callable

If a seaborn function, it should accept `x` and `y` and plot when only one of them is defined. Otherwise, it must accept a vector of data as the first positional argument and determine its orientation using the `vertical` parameter, and it must plot on the “current” axes. If `hue` was defined in the class constructor, it must accept `hue` as a parameter.

**kwargs**

Keyword argument are passed to the plotting function.

Returns:

[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 instance

Returns `self` for easy method chaining.