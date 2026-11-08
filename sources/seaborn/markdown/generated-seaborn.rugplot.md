 

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

seaborn.rugplot[#](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn-rugplot "Permalink to this heading")

==========================================================================================================================

seaborn.rugplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _height\=0.025_, _expand\_margins\=True_, _palette\=None_, _hue\_order\=None_, _hue\_norm\=None_, _legend\=True_, _ax\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.rugplot.html#seaborn.rugplot "Permalink to this definition")

Plot marginal distributions by drawing ticks along the x and y axes.

This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.

Parameters:

**data**[`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
, [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
, mapping, or sequence

Input data structure. Either a long-form collection of vectors that can be assigned to named variables or a wide-form dataset that will be internally reshaped.

**x, y**vectors or keys in `data`

Variables that specify positions on the x and y axes.

**hue**vector or key in `data`

Semantic variable that is mapped to determine the color of plot elements.

**height**float

Proportion of axes extent covered by each rug element. Can be negative.

**expand\_margins**bool

If True, increase the axes margins by the height of the rug to avoid overlap with other elements.

**palette**string, list, dict, or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.8.2)")

Method for choosing the colors to use when mapping the `hue` semantic. String values are passed to [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
. List or dict values imply categorical mapping, while a colormap object implies numeric mapping.

**hue\_order**vector of strings

Specify the order of processing and plotting for categorical levels of the `hue` semantic.

**hue\_norm**tuple or [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "(in Matplotlib v3.8.2)")

Either a pair of values that set the normalization range in data units or an object that will map from data units into a \[0, 1\] interval. Usage implies numeric mapping.

**legend**bool

If False, do not add a legend for semantic variables.

**ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

Pre-existing axes for the plot. Otherwise, call [`matplotlib.pyplot.gca()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "(in Matplotlib v3.8.2)")
 internally.

**kwargs**

Other keyword arguments are passed to `matplotlib.collections.LineCollection()`

Returns:

[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")

The matplotlib axes containing the plot.

Examples

Add a rug along one of the axes:

import seaborn as sns; sns.set\_theme()
tips \= sns.load\_dataset("tips")
sns.kdeplot(data\=tips, x\="total\_bill")
sns.rugplot(data\=tips, x\="total\_bill")

Copy to clipboard

![../_images/rugplot_1_0.png](https://seaborn.pydata.org/_images/rugplot_1_0.png)

Add a rug along both axes:

sns.scatterplot(data\=tips, x\="total\_bill", y\="tip")
sns.rugplot(data\=tips, x\="total\_bill", y\="tip")

Copy to clipboard

![../_images/rugplot_3_0.png](https://seaborn.pydata.org/_images/rugplot_3_0.png)

Represent a third variable with hue mapping:

sns.scatterplot(data\=tips, x\="total\_bill", y\="tip", hue\="time")
sns.rugplot(data\=tips, x\="total\_bill", y\="tip", hue\="time")

Copy to clipboard

![../_images/rugplot_5_0.png](https://seaborn.pydata.org/_images/rugplot_5_0.png)

Draw a taller rug:

sns.scatterplot(data\=tips, x\="total\_bill", y\="tip")
sns.rugplot(data\=tips, x\="total\_bill", y\="tip", height\=.1)

Copy to clipboard

![../_images/rugplot_7_0.png](https://seaborn.pydata.org/_images/rugplot_7_0.png)

Put the rug outside the axes:

sns.scatterplot(data\=tips, x\="total\_bill", y\="tip")
sns.rugplot(data\=tips, x\="total\_bill", y\="tip", height\=-.02, clip\_on\=False)

Copy to clipboard

![../_images/rugplot_9_0.png](https://seaborn.pydata.org/_images/rugplot_9_0.png)

Show the density of a larger dataset using thinner lines and alpha blending:

diamonds \= sns.load\_dataset("diamonds")
sns.scatterplot(data\=diamonds, x\="carat", y\="price", s\=5)
sns.rugplot(data\=diamonds, x\="carat", y\="price", lw\=1, alpha\=.005)

Copy to clipboard

![../_images/rugplot_11_0.png](https://seaborn.pydata.org/_images/rugplot_11_0.png)