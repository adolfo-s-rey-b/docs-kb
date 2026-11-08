 

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

seaborn.JointGrid.\_\_init\_\_[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.__init__.html#seaborn-jointgrid-init "Permalink to this heading")

===========================================================================================================================================================

JointGrid.\_\_init\_\_(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _height\=6_, _ratio\=5_, _space\=0.2_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _dropna\=False_, _xlim\=None_, _ylim\=None_, _marginal\_ticks\=False_)[#](https://seaborn.pydata.org/generated/seaborn.JointGrid.__init__.html#seaborn.JointGrid.__init__ "Permalink to this definition")

Set up the grid of subplots and store data internally for easy plotting.

Parameters:

**data**[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
, [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
, mapping, or sequence

Input data structure. Either a long-form collection of vectors that can be assigned to named variables or a wide-form dataset that will be internally reshaped.

**x, y**vectors or keys in `data`

Variables that specify positions on the x and y axes.

**height**number

Size of each side of the figure in inches (it will be square).

**ratio**number

Ratio of joint axes height to marginal axes height.

**space**number

Space between the joint and marginal axes

**dropna**bool

If True, remove missing observations before plotting.

**{x, y}lim**pairs of numbers

Set axis limits to these values before plotting.

**marginal\_ticks**bool

If False, suppress ticks on the count/density axis of the marginal plots.

**hue**vector or key in `data`

Semantic variable that is mapped to determine the color of plot elements. Note: unlike in [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 or [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
, the axes-level functions must support `hue` to use it in [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")
.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

See also

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw a bivariate plot with univariate marginal distributions.

[`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")

Set up a figure with joint and marginal views on multiple variables.

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw multiple bivariate plots with univariate marginal distributions.

Examples

Calling the constructor initializes the figure, but it does not plot anything:

penguins \= sns.load\_dataset("penguins")
sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")

Copy to clipboard

![../_images/JointGrid_1_0.png](https://seaborn.pydata.org/_images/JointGrid_1_0.png)

The simplest plotting method, [`JointGrid.plot()`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html#seaborn.JointGrid.plot "seaborn.JointGrid.plot")
 accepts a pair of functions (one for the joint axes and one for both marginal axes):

g \= sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
g.plot(sns.scatterplot, sns.histplot)

Copy to clipboard

![../_images/JointGrid_3_0.png](https://seaborn.pydata.org/_images/JointGrid_3_0.png)

The [`JointGrid.plot()`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot.html#seaborn.JointGrid.plot "seaborn.JointGrid.plot")
 function also accepts additional keyword arguments, but it passes them to both functions:

g \= sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
g.plot(sns.scatterplot, sns.histplot, alpha\=.7, edgecolor\=".2", linewidth\=.5)

Copy to clipboard

![../_images/JointGrid_5_0.png](https://seaborn.pydata.org/_images/JointGrid_5_0.png)

If you need to pass different keyword arguments to each function, you’ll have to invoke [`JointGrid.plot_joint()`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_joint.html#seaborn.JointGrid.plot_joint "seaborn.JointGrid.plot_joint")
 and [`JointGrid.plot_marginals()`](https://seaborn.pydata.org/generated/seaborn.JointGrid.plot_marginals.html#seaborn.JointGrid.plot_marginals "seaborn.JointGrid.plot_marginals")
:

g \= sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
g.plot\_joint(sns.scatterplot, s\=100, alpha\=.5)
g.plot\_marginals(sns.histplot, kde\=True)

Copy to clipboard

![../_images/JointGrid_7_0.png](https://seaborn.pydata.org/_images/JointGrid_7_0.png)

You can also set up the grid without assigning any data:

g \= sns.JointGrid()

Copy to clipboard

![../_images/JointGrid_9_0.png](https://seaborn.pydata.org/_images/JointGrid_9_0.png)

You can then plot by accessing the `ax_joint`, `ax_marg_x`, and `ax_marg_y` attributes, which are [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")
 objects:

g \= sns.JointGrid()
x, y \= penguins\["bill\_length\_mm"\], penguins\["bill\_depth\_mm"\]
sns.scatterplot(x\=x, y\=y, ec\="b", fc\="none", s\=100, linewidth\=1.5, ax\=g.ax\_joint)
sns.histplot(x\=x, fill\=False, linewidth\=2, ax\=g.ax\_marg\_x)
sns.kdeplot(y\=y, linewidth\=2, ax\=g.ax\_marg\_y)

Copy to clipboard

![../_images/JointGrid_11_0.png](https://seaborn.pydata.org/_images/JointGrid_11_0.png)

The plotting methods can use any seaborn functions that accept `x` and `y` variables:

g \= sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
g.plot(sns.regplot, sns.boxplot)

Copy to clipboard

![../_images/JointGrid_13_0.png](https://seaborn.pydata.org/_images/JointGrid_13_0.png)

If the functions accept a `hue` variable, you can use it by assigning `hue` when you call the constructor:

g \= sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", hue\="species")
g.plot(sns.scatterplot, sns.histplot)

Copy to clipboard

![../_images/JointGrid_15_0.png](https://seaborn.pydata.org/_images/JointGrid_15_0.png)

Horizontal and/or vertical reference lines can be added to the joint and/or marginal axes using :meth:`JointGrid.refline`:

g \= sns.JointGrid(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")
g.plot(sns.scatterplot, sns.histplot)
g.refline(x\=45, y\=16)

Copy to clipboard

![../_images/JointGrid_17_0.png](https://seaborn.pydata.org/_images/JointGrid_17_0.png)

The figure will always be square (unless you resize it at the matplotlib layer), but its overall size and layout are configurable. The size is controlled by the `height` parameter. The relative ratio between the joint and marginal axes is controlled by `ratio`, and the amount of space between the plots is controlled by `space`:

sns.JointGrid(height\=4, ratio\=2, space\=.05)

Copy to clipboard

![../_images/JointGrid_19_0.png](https://seaborn.pydata.org/_images/JointGrid_19_0.png)

By default, the ticks on the density axis of the marginal plots are turned off, but this is configurable:

sns.JointGrid(marginal\_ticks\=True)

Copy to clipboard

![../_images/JointGrid_21_0.png](https://seaborn.pydata.org/_images/JointGrid_21_0.png)

Limits on the two data axes (which are shared across plots) can also be defined when setting up the figure:

sns.JointGrid(xlim\=(\-2, 5), ylim\=(0, 10))

Copy to clipboard

![../_images/JointGrid_23_0.png](https://seaborn.pydata.org/_images/JointGrid_23_0.png)