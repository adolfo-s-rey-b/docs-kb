 

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

seaborn.set\_style[#](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn-set-style "Permalink to this heading")

=================================================================================================================================

seaborn.set\_style(_style\=None_, _rc\=None_)[#](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style "Permalink to this definition")

Set the parameters that control the general style of the plots.

The style parameters control properties like the color of the background and whether a grid is enabled by default. This is accomplished using the matplotlib rcParams system.

The options are illustrated in the [aesthetics tutorial](https://seaborn.pydata.org/tutorial/aesthetics.html)
.

See [`axes_style()`](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style "seaborn.axes_style")
 to get the parameter values.

Parameters:

**style**dict, or one of {darkgrid, whitegrid, dark, white, ticks}

A dictionary of parameters or the name of a preconfigured style.

**rc**dict, optional

Parameter mappings to override the values in the preset seaborn style dictionaries. This only updates parameters that are considered part of the style definition.

Examples

Call the function with the name of a seaborn style to set the default for all plots:

sns.set\_style("whitegrid")
sns.barplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_style_1_0.png](https://seaborn.pydata.org/_images/set_style_1_0.png)

You can also selectively override seaborn’s default parameter values:

sns.set\_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
sns.lineplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_style_3_0.png](https://seaborn.pydata.org/_images/set_style_3_0.png)