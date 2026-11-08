 

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

seaborn.move\_legend[#](https://seaborn.pydata.org/generated/seaborn.move_legend.html#seaborn-move-legend "Permalink to this heading")

=======================================================================================================================================

seaborn.move\_legend(_obj_, _loc_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.move_legend.html#seaborn.move_legend "Permalink to this definition")

Recreate a plot’s legend at a new location.

The name is a slight misnomer. Matplotlib legends do not expose public control over their position parameters. So this function creates a new legend, copying over the data from the original object, which is then removed.

Parameters:

**obj**the object with the plot

This argument can be either a seaborn or matplotlib object:

*   [`seaborn.FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
     or [`seaborn.PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
    
*   [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")
     or [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "(in Matplotlib v3.8.2)")
    

**loc**str or int

Location argument, as in [`matplotlib.axes.Axes.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "(in Matplotlib v3.8.2)")
.

**kwargs**

Other keyword arguments are passed to [`matplotlib.axes.Axes.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "(in Matplotlib v3.8.2)")
.

Examples

For axes-level functions, pass the [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")
 object and provide a new location.

ax \= sns.histplot(penguins, x\="bill\_length\_mm", hue\="species")
sns.move\_legend(ax, "center right")

Copy to clipboard

![../_images/move_legend_1_0.png](https://seaborn.pydata.org/_images/move_legend_1_0.png)

Use the `bbox_to_anchor` parameter for more fine-grained control, including moving the legend outside of the axes:

ax \= sns.histplot(penguins, x\="bill\_length\_mm", hue\="species")
sns.move\_legend(ax, "upper left", bbox\_to\_anchor\=(1, 1))

Copy to clipboard

![../_images/move_legend_3_0.png](https://seaborn.pydata.org/_images/move_legend_3_0.png)

Pass additional [`matplotlib.axes.Axes.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "(in Matplotlib v3.8.2)")
 parameters to update other properties:

ax \= sns.histplot(penguins, x\="bill\_length\_mm", hue\="species")
sns.move\_legend(
    ax, "lower center",
    bbox\_to\_anchor\=(.5, 1), ncol\=3, title\=None, frameon\=False,
)

Copy to clipboard

![../_images/move_legend_5_0.png](https://seaborn.pydata.org/_images/move_legend_5_0.png)

It’s also possible to move the legend created by a figure-level function. But when fine-tuning the position, you must bear in mind that the figure will have extra blank space on the right:

g \= sns.displot(
    penguins,
    x\="bill\_length\_mm", hue\="species",
    col\="island", col\_wrap\=2, height\=3,
)
sns.move\_legend(g, "upper left", bbox\_to\_anchor\=(.55, .45))

Copy to clipboard

![../_images/move_legend_7_0.png](https://seaborn.pydata.org/_images/move_legend_7_0.png)

One way to avoid this would be to set `legend_out=False` on the [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
:

g \= sns.displot(
    penguins,
    x\="bill\_length\_mm", hue\="species",
    col\="island", col\_wrap\=2, height\=3,
    facet\_kws\=dict(legend\_out\=False),
)
sns.move\_legend(g, "upper left", bbox\_to\_anchor\=(.55, .45), frameon\=False)

Copy to clipboard

![../_images/move_legend_9_0.png](https://seaborn.pydata.org/_images/move_legend_9_0.png)