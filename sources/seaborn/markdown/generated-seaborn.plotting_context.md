 

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

seaborn.plotting\_context[#](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn-plotting-context "Permalink to this heading")

======================================================================================================================================================

seaborn.plotting\_context(_context\=None_, _font\_scale\=1_, _rc\=None_)[#](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context "Permalink to this definition")

Get the parameters that control the scaling of plot elements.

These parameters correspond to label size, line thickness, etc. For more information, see the [aesthetics tutorial](https://seaborn.pydata.org/tutorial/aesthetics.html)
.

The base context is “notebook”, and the other contexts are “paper”, “talk”, and “poster”, which are version of the notebook parameters scaled by different values. Font elements can also be scaled independently of (but relative to) the other values.

This function can also be used as a context manager to temporarily alter the global defaults. See [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
 or [`set_context()`](https://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context "seaborn.set_context")
 to modify the global defaults for all plots.

Parameters:

**context**None, dict, or one of {paper, notebook, talk, poster}

A dictionary of parameters or the name of a preconfigured set.

**font\_scale**float, optional

Separate scaling factor to independently scale the size of the font elements.

**rc**dict, optional

Parameter mappings to override the values in the preset seaborn context dictionaries. This only updates parameters that are considered part of the context definition.

Examples

Calling with no arguments will return the current defaults for the parameters that get scaled:

sns.plotting\_context()

Copy to clipboard

{'font.size': 10.0,
 'axes.labelsize': 'medium',
 'axes.titlesize': 'large',
 'xtick.labelsize': 'medium',
 'ytick.labelsize': 'medium',
 'legend.fontsize': 'medium',
 'legend.title\_fontsize': None,
 'axes.linewidth': 0.8,
 'grid.linewidth': 0.8,
 'lines.linewidth': 1.5,
 'lines.markersize': 6.0,
 'patch.linewidth': 1.0,
 'xtick.major.width': 0.8,
 'ytick.major.width': 0.8,
 'xtick.minor.width': 0.6,
 'ytick.minor.width': 0.6,
 'xtick.major.size': 3.5,
 'ytick.major.size': 3.5,
 'xtick.minor.size': 2.0,
 'ytick.minor.size': 2.0}

Copy to clipboard

Calling with the name of a predefined style will show those values:

sns.plotting\_context("talk")

Copy to clipboard

{'axes.linewidth': 1.875,
 'grid.linewidth': 1.5,
 'lines.linewidth': 2.25,
 'lines.markersize': 9.0,
 'patch.linewidth': 1.5,
 'xtick.major.width': 1.875,
 'ytick.major.width': 1.875,
 'xtick.minor.width': 1.5,
 'ytick.minor.width': 1.5,
 'xtick.major.size': 9.0,
 'ytick.major.size': 9.0,
 'xtick.minor.size': 6.0,
 'ytick.minor.size': 6.0,
 'font.size': 18.0,
 'axes.labelsize': 18.0,
 'axes.titlesize': 18.0,
 'xtick.labelsize': 16.5,
 'ytick.labelsize': 16.5,
 'legend.fontsize': 16.5,
 'legend.title\_fontsize': 18.0}

Copy to clipboard

Use the function as a context manager to temporarily change the parameter values:

with sns.plotting\_context("talk"):
    sns.lineplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/plotting_context_5_0.png](https://seaborn.pydata.org/_images/plotting_context_5_0.png)