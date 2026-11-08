 

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

seaborn.set\_context[#](https://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn-set-context "Permalink to this heading")

=======================================================================================================================================

seaborn.set\_context(_context\=None_, _font\_scale\=1_, _rc\=None_)[#](https://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context "Permalink to this definition")

Set the parameters that control the scaling of plot elements.

These parameters correspond to label size, line thickness, etc. Calling this function modifies the global matplotlib `rcParams`. For more information, see the [aesthetics tutorial](https://seaborn.pydata.org/tutorial/aesthetics.html)
.

The base context is “notebook”, and the other contexts are “paper”, “talk”, and “poster”, which are version of the notebook parameters scaled by different values. Font elements can also be scaled independently of (but relative to) the other values.

See [`plotting_context()`](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context "seaborn.plotting_context")
 to get the parameter values.

Parameters:

**context**dict, or one of {paper, notebook, talk, poster}

A dictionary of parameters or the name of a preconfigured set.

**font\_scale**float, optional

Separate scaling factor to independently scale the size of the font elements.

**rc**dict, optional

Parameter mappings to override the values in the preset seaborn context dictionaries. This only updates parameters that are considered part of the context definition.

Examples

Call the function with the name of a context to set the default for all plots:

sns.set\_context("notebook")
sns.lineplot(x\=\[0, 1, 2\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_context_1_0.png](https://seaborn.pydata.org/_images/set_context_1_0.png)

You can independently scale the font elements relative to the current context:

sns.set\_context("notebook", font\_scale\=1.25)
sns.lineplot(x\=\[0, 1, 2\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_context_3_0.png](https://seaborn.pydata.org/_images/set_context_3_0.png)

It is also possible to override some of the parameters with specific values:

sns.set\_context("notebook", rc\={"lines.linewidth": 3})
sns.lineplot(x\=\[0, 1, 2\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_context_5_0.png](https://seaborn.pydata.org/_images/set_context_5_0.png)