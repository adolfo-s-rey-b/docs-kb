 

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

seaborn.set\_theme[#](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn-set-theme "Permalink to this heading")

=================================================================================================================================

seaborn.set\_theme(_context\='notebook'_, _style\='darkgrid'_, _palette\='deep'_, _font\='sans-serif'_, _font\_scale\=1_, _color\_codes\=True_, _rc\=None_)[#](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "Permalink to this definition")

Set aspects of the visual theme for all matplotlib and seaborn plots.

This function changes the global defaults for all plots using the matplotlib rcParams system. The themeing is decomposed into several distinct sets of parameter values.

The options are illustrated in the [aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
 and [color palette](https://seaborn.pydata.org/tutorial/color_palettes.html)
 tutorials.

Parameters:

**context**string or dict

Scaling parameters, see [`plotting_context()`](https://seaborn.pydata.org/generated/seaborn.plotting_context.html#seaborn.plotting_context "seaborn.plotting_context")
.

**style**string or dict

Axes style parameters, see [`axes_style()`](https://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style "seaborn.axes_style")
.

**palette**string or sequence

Color palette, see [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
.

**font**string

Font family, see matplotlib font manager.

**font\_scale**float, optional

Separate scaling factor to independently scale the size of the font elements.

**color\_codes**bool

If `True` and `palette` is a seaborn palette, remap the shorthand color codes (e.g. “b”, “g”, “r”, etc.) to the colors from this palette.

**rc**dict or None

Dictionary of rc parameter mappings to override the above.

Examples

By default, seaborn plots will be made with the current values of the matplotlib rcParams:

sns.barplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_theme_1_0.png](https://seaborn.pydata.org/_images/set_theme_1_0.png)

Calling this function with no arguments will activate seaborn’s “default” theme:

sns.set\_theme()
sns.barplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_theme_3_0.png](https://seaborn.pydata.org/_images/set_theme_3_0.png)

Note that this will take effect for _all_ matplotlib plots, including those not made using seaborn:

plt.bar(\["A", "B", "C"\], \[1, 3, 2\])

Copy to clipboard

![../_images/set_theme_5_0.png](https://seaborn.pydata.org/_images/set_theme_5_0.png)

The seaborn theme is decomposed into several distinct sets of parameters that you can control independently:

sns.set\_theme(style\="whitegrid", palette\="pastel")
sns.barplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_theme_7_0.png](https://seaborn.pydata.org/_images/set_theme_7_0.png)

Pass `None` to preserve the current values for a given set of parameters:

sns.set\_theme(style\="white", palette\=None)
sns.barplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_theme_9_0.png](https://seaborn.pydata.org/_images/set_theme_9_0.png)

You can also override any seaborn parameters or define additional parameters that are part of the matplotlib rc system but not included in the seaborn themes:

custom\_params \= {"axes.spines.right": False, "axes.spines.top": False}
sns.set\_theme(style\="ticks", rc\=custom\_params)
sns.barplot(x\=\["A", "B", "C"\], y\=\[1, 3, 2\])

Copy to clipboard

![../_images/set_theme_11_0.png](https://seaborn.pydata.org/_images/set_theme_11_0.png)