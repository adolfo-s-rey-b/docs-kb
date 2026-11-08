 

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

seaborn.JointGrid.plot\_joint[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html#seaborn-jointgrid-plot-joint "Permalink to this heading")

==================================================================================================================================================================

JointGrid.plot\_joint(_func_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html#seaborn.JointGrid.plot_joint "Permalink to this definition")

Draw a bivariate plot on the joint axes of the grid.

Parameters:

**func**plotting callable

If a seaborn function, it should accept `x` and `y`. Otherwise, it must accept `x` and `y` vectors of data as the first two positional arguments, and it must plot on the “current” axes. If `hue` was defined in the class constructor, the function must accept `hue` as a parameter.

**kwargs**

Keyword argument are passed to the plotting function.

Returns:

[`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
 instance

Returns `self` for easy method chaining.