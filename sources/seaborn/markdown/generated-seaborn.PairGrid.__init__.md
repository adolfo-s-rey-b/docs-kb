 

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

seaborn.PairGrid.\_\_init\_\_[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.__init__.html#seaborn-pairgrid-init "Permalink to this heading")

========================================================================================================================================================

PairGrid.\_\_init\_\_(_data_, _\*_, _hue\=None_, _vars\=None_, _x\_vars\=None_, _y\_vars\=None_, _hue\_order\=None_, _palette\=None_, _hue\_kws\=None_, _corner\=False_, _diag\_sharey\=True_, _height\=2.5_, _aspect\=1_, _layout\_pad\=0.5_, _despine\=True_, _dropna\=False_)[#](https://seaborn.pydata.org/generated/seaborn.PairGrid.__init__.html#seaborn.PairGrid.__init__ "Permalink to this definition")

Initialize the plot figure and PairGrid object.

Parameters:

**data**DataFrame

Tidy (long-form) dataframe where each column is a variable and each row is an observation.

**hue**string (variable name)

Variable in `data` to map plot aspects to different colors. This variable will be excluded from the default x and y variables.

**vars**list of variable names

Variables within `data` to use, otherwise use every column with a numeric datatype.

**{x, y}\_vars**lists of variable names

Variables within `data` to use separately for the rows and columns of the figure; i.e. to make a non-square plot.

**hue\_order**list of strings

Order for the levels of the hue variable in the palette

**palette**dict or seaborn color palette

Set of colors for mapping the `hue` variable. If a dict, keys should be values in the `hue` variable.

**hue\_kws**dictionary of param -> list of values mapping

Other keyword arguments to insert into the plotting call to let other plot attributes vary across levels of the hue variable (e.g. the markers in a scatterplot).

**corner**bool

If True, don’t add axes to the upper (off-diagonal) triangle of the grid, making this a “corner” plot.

**height**scalar

Height (in inches) of each facet.

**aspect**scalar

Aspect \* height gives the width (in inches) of each facet.

**layout\_pad**scalar

Padding between axes; passed to `fig.tight_layout`.

**despine**boolean

Remove the top and right spines from the plots.

**dropna**boolean

Drop missing values from the data before plotting.

See also

[`pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot")

Easily drawing common uses of [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
.

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

Subplot grid for plotting conditional relationships.

Examples

Calling the constructor sets up a blank grid of subplots with each row and one column corresponding to a numeric variable in the dataset:

penguins \= sns.load\_dataset("penguins")
g \= sns.PairGrid(penguins)

Copy to clipboard

![../_images/PairGrid_1_0.png](https://seaborn.pydata.org/_images/PairGrid_1_0.png)

Passing a bivariate function to [`PairGrid.map()`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map.html#seaborn.PairGrid.map "seaborn.PairGrid.map")
 will draw a bivariate plot on every axes:

g \= sns.PairGrid(penguins)
g.map(sns.scatterplot)

Copy to clipboard

![../_images/PairGrid_3_0.png](https://seaborn.pydata.org/_images/PairGrid_3_0.png)

Passing separate functions to [`PairGrid.map_diag()`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_diag.html#seaborn.PairGrid.map_diag "seaborn.PairGrid.map_diag")
 and [`PairGrid.map_offdiag()`](https://seaborn.pydata.org/generated/seaborn.PairGrid.map_offdiag.html#seaborn.PairGrid.map_offdiag "seaborn.PairGrid.map_offdiag")
 will show each variable’s marginal distribution on the diagonal:

g \= sns.PairGrid(penguins)
g.map\_diag(sns.histplot)
g.map\_offdiag(sns.scatterplot)

Copy to clipboard

![../_images/PairGrid_5_0.png](https://seaborn.pydata.org/_images/PairGrid_5_0.png)

It’s also possible to use different functions on the upper and lower triangles of the plot (which are otherwise redundant):

g \= sns.PairGrid(penguins, diag\_sharey\=False)
g.map\_upper(sns.scatterplot)
g.map\_lower(sns.kdeplot)
g.map\_diag(sns.kdeplot)

Copy to clipboard

![../_images/PairGrid_7_0.png](https://seaborn.pydata.org/_images/PairGrid_7_0.png)

Or to avoid the redundancy altogether:

g \= sns.PairGrid(penguins, diag\_sharey\=False, corner\=True)
g.map\_lower(sns.scatterplot)
g.map\_diag(sns.kdeplot)

Copy to clipboard

![../_images/PairGrid_9_0.png](https://seaborn.pydata.org/_images/PairGrid_9_0.png)

The [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
 constructor accepts a `hue` variable. This variable is passed directly to functions that understand it:

g \= sns.PairGrid(penguins, hue\="species")
g.map\_diag(sns.histplot)
g.map\_offdiag(sns.scatterplot)
g.add\_legend()

Copy to clipboard

![../_images/PairGrid_11_0.png](https://seaborn.pydata.org/_images/PairGrid_11_0.png)

But you can also pass matplotlib functions, in which case a groupby is performed internally and a separate plot is drawn for each level:

g \= sns.PairGrid(penguins, hue\="species")
g.map\_diag(plt.hist)
g.map\_offdiag(plt.scatter)
g.add\_legend()

Copy to clipboard

![../_images/PairGrid_13_0.png](https://seaborn.pydata.org/_images/PairGrid_13_0.png)

Additional semantic variables can be assigned by passing data vectors directly while mapping the function:

g \= sns.PairGrid(penguins, hue\="species")
g.map\_diag(sns.histplot)
g.map\_offdiag(sns.scatterplot, size\=penguins\["sex"\])
g.add\_legend(title\="", adjust\_subtitles\=True)

Copy to clipboard

![../_images/PairGrid_15_0.png](https://seaborn.pydata.org/_images/PairGrid_15_0.png)

When using seaborn functions that can implement a numeric hue mapping, you will want to disable mapping of the variable on the diagonal axes. Note that the `hue` variable is excluded from the list of variables shown by default:

g \= sns.PairGrid(penguins, hue\="body\_mass\_g")
g.map\_diag(sns.histplot, hue\=None, color\=".3")
g.map\_offdiag(sns.scatterplot)
g.add\_legend()

Copy to clipboard

![../_images/PairGrid_17_0.png](https://seaborn.pydata.org/_images/PairGrid_17_0.png)

The `vars` parameter can be used to control exactly which variables are used:

variables \= \["body\_mass\_g", "bill\_length\_mm", "flipper\_length\_mm"\]
g \= sns.PairGrid(penguins, hue\="body\_mass\_g", vars\=variables)
g.map\_diag(sns.histplot, hue\=None, color\=".3")
g.map\_offdiag(sns.scatterplot)
g.add\_legend()

Copy to clipboard

![../_images/PairGrid_19_0.png](https://seaborn.pydata.org/_images/PairGrid_19_0.png)

The plot need not be square: separate variables can be used to define the rows and columns:

x\_vars \= \["body\_mass\_g", "bill\_length\_mm", "bill\_depth\_mm", "flipper\_length\_mm"\]
y\_vars \= \["body\_mass\_g"\]
g \= sns.PairGrid(penguins, hue\="species", x\_vars\=x\_vars, y\_vars\=y\_vars)
g.map\_diag(sns.histplot, color\=".3")
g.map\_offdiag(sns.scatterplot)
g.add\_legend()

Copy to clipboard

![../_images/PairGrid_21_0.png](https://seaborn.pydata.org/_images/PairGrid_21_0.png)

It can be useful to explore different approaches to resolving multiple distributions on the diagonal axes:

g \= sns.PairGrid(penguins, hue\="species")
g.map\_diag(sns.histplot, multiple\="stack", element\="step")
g.map\_offdiag(sns.scatterplot)
g.add\_legend()

Copy to clipboard

![../_images/PairGrid_23_0.png](https://seaborn.pydata.org/_images/PairGrid_23_0.png)