 

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

seaborn.lmplot[#](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn-lmplot "Permalink to this heading")

=======================================================================================================================

seaborn.lmplot(_data_, _\*_, _x\=None_, _y\=None_, _hue\=None_, _col\=None_, _row\=None_, _palette\=None_, _col\_wrap\=None_, _height\=5_, _aspect\=1_, _markers\='o'_, _sharex\=None_, _sharey\=None_, _hue\_order\=None_, _col\_order\=None_, _row\_order\=None_, _legend\=True_, _legend\_out\=None_, _x\_estimator\=None_, _x\_bins\=None_, _x\_ci\='ci'_, _scatter\=True_, _fit\_reg\=True_, _ci\=95_, _n\_boot\=1000_, _units\=None_, _seed\=None_, _order\=1_, _logistic\=False_, _lowess\=False_, _robust\=False_, _logx\=False_, _x\_partial\=None_, _y\_partial\=None_, _truncate\=True_, _x\_jitter\=None_, _y\_jitter\=None_, _scatter\_kws\=None_, _line\_kws\=None_, _facet\_kws\=None_)[#](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "Permalink to this definition")

Plot data and regression model fits across a FacetGrid.

This function combines [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
 and [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
. It is intended as a convenient interface to fit regression models across conditional subsets of a dataset.

When thinking about how to assign variables to different facets, a general rule is that it makes sense to use `hue` for the most important comparison, followed by `col` and `row`. However, always think about your particular dataset and the goals of the visualization you are creating.

There are a number of mutually exclusive options for estimating the regression model. See the [tutorial](https://seaborn.pydata.org/tutorial/regression.html#regression-tutorial)
 for more information.

The parameters to this function span most of the options in [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
, although there may be occasional cases where you will want to use that class and [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
 directly.

Parameters:

**data**DataFrame

Tidy (“long-form”) dataframe where each column is a variable and each row is an observation.

**x, y**strings, optional

Input variables; these should be column names in `data`.

**hue, col, row**strings

Variables that define subsets of the data, which will be drawn on separate facets in the grid. See the `*_order` parameters to control the order of levels of this variable.

**palette**palette name, list, or dict

Colors to use for the different levels of the `hue` variable. Should be something that can be interpreted by [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, or a dictionary mapping hue levels to matplotlib colors.

**col\_wrap**int

“Wrap” the column variable at this width, so that the column facets span multiple rows. Incompatible with a `row` facet.

**height**scalar

Height (in inches) of each facet. See also: `aspect`.

**aspect**scalar

Aspect ratio of each facet, so that `aspect * height` gives the width of each facet in inches.

**markers**matplotlib marker code or list of marker codes, optional

Markers for the scatterplot. If a list, each marker in the list will be used for each level of the `hue` variable.

**share{x,y}**bool, ‘col’, or ‘row’ optional

If true, the facets will share y axes across columns and/or x axes across rows.

Deprecated since version 0.12.0: Pass using the `facet_kws` dictionary.

**{hue,col,row}\_order**lists, optional

Order for the levels of the faceting variables. By default, this will be the order that the levels appear in `data` or, if the variables are pandas categoricals, the category order.

**legend**bool, optional

If `True` and there is a `hue` variable, add a legend.

**legend\_out**bool

If `True`, the figure size will be extended, and the legend will be drawn outside the plot on the center right.

Deprecated since version 0.12.0: Pass using the `facet_kws` dictionary.

**x\_estimator**callable that maps vector -> scalar, optional

Apply this function to each unique value of `x` and plot the resulting estimate. This is useful when `x` is a discrete variable. If `x_ci` is given, this estimate will be bootstrapped and a confidence interval will be drawn.

**x\_bins**int or vector, optional

Bin the `x` variable into discrete bins and then estimate the central tendency and a confidence interval. This binning only influences how the scatterplot is drawn; the regression is still fit to the original data. This parameter is interpreted either as the number of evenly-sized (not necessary spaced) bins or the positions of the bin centers. When this parameter is used, it implies that the default of `x_estimator` is `numpy.mean`.

**x\_ci**“ci”, “sd”, int in \[0, 100\] or None, optional

Size of the confidence interval used when plotting a central tendency for discrete values of `x`. If `"ci"`, defer to the value of the `ci` parameter. If `"sd"`, skip bootstrapping and show the standard deviation of the observations in each bin.

**scatter**bool, optional

If `True`, draw a scatterplot with the underlying observations (or the `x_estimator` values).

**fit\_reg**bool, optional

If `True`, estimate and plot a regression model relating the `x` and `y` variables.

**ci**int in \[0, 100\] or None, optional

Size of the confidence interval for the regression estimate. This will be drawn using translucent bands around the regression line. The confidence interval is estimated using a bootstrap; for large datasets, it may be advisable to avoid that computation by setting this parameter to None.

**n\_boot**int, optional

Number of bootstrap resamples used to estimate the `ci`. The default value attempts to balance time and stability; you may want to increase this value for “final” versions of plots.

**units**variable name in `data`, optional

If the `x` and `y` observations are nested within sampling units, those can be specified here. This will be taken into account when computing the confidence intervals by performing a multilevel bootstrap that resamples both units and observations (within unit). This does not otherwise influence how the regression is estimated or drawn.

**seed**int, numpy.random.Generator, or numpy.random.RandomState, optional

Seed or random number generator for reproducible bootstrapping.

**order**int, optional

If `order` is greater than 1, use `numpy.polyfit` to estimate a polynomial regression.

**logistic**bool, optional

If `True`, assume that `y` is a binary variable and use `statsmodels` to estimate a logistic regression model. Note that this is substantially more computationally intensive than linear regression, so you may wish to decrease the number of bootstrap resamples (`n_boot`) or set `ci` to None.

**lowess**bool, optional

If `True`, use `statsmodels` to estimate a nonparametric lowess model (locally weighted linear regression). Note that confidence intervals cannot currently be drawn for this kind of model.

**robust**bool, optional

If `True`, use `statsmodels` to estimate a robust regression. This will de-weight outliers. Note that this is substantially more computationally intensive than standard linear regression, so you may wish to decrease the number of bootstrap resamples (`n_boot`) or set `ci` to None.

**logx**bool, optional

If `True`, estimate a linear regression of the form y ~ log(x), but plot the scatterplot and regression model in the input space. Note that `x` must be positive for this to work.

**{x,y}\_partial**strings in `data` or matrices

Confounding variables to regress out of the `x` or `y` variables before plotting.

**truncate**bool, optional

If `True`, the regression line is bounded by the data limits. If `False`, it extends to the `x` axis limits.

**{x,y}\_jitter**floats, optional

Add uniform random noise of this size to either the `x` or `y` variables. The noise is added to a copy of the data after fitting the regression, and only influences the look of the scatterplot. This can be helpful when plotting variables that take discrete values.

**{scatter,line}\_kws**dictionaries

Additional keyword arguments to pass to `plt.scatter` and `plt.plot`.

**facet\_kws**dict

Dictionary of keyword arguments for [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

See also

[`regplot`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")

Plot data and a conditional model fit.

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

Subplot grid for plotting conditional relationships.

[`pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot")

Combine [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
 and [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
 (when used with `kind="reg"`).

Notes

The [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
 and [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot")
 functions are closely related, but the former is an axes-level function while the latter is a figure-level function that combines [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
 and [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
.

Examples

See the [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")
 docs for demonstrations of various options for specifying the regression model, which are also accepted here.

Plot a regression fit over a scatter plot:

sns.lmplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm")

Copy to clipboard

![../_images/lmplot_2_0.png](https://seaborn.pydata.org/_images/lmplot_2_0.png)

Condition the regression fit on another variable and represent it using color:

sns.lmplot(data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm", hue\="species")

Copy to clipboard

![../_images/lmplot_4_0.png](https://seaborn.pydata.org/_images/lmplot_4_0.png)

Condition the regression fit on another variable and split across subplots:

sns.lmplot(
    data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm",
    hue\="species", col\="sex", height\=4,
)

Copy to clipboard

![../_images/lmplot_6_0.png](https://seaborn.pydata.org/_images/lmplot_6_0.png)

Condition across two variables using both columns and rows:

sns.lmplot(
    data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm",
    col\="species", row\="sex", height\=3,
)

Copy to clipboard

![../_images/lmplot_8_0.png](https://seaborn.pydata.org/_images/lmplot_8_0.png)

Allow axis limits to vary across subplots:

sns.lmplot(
    data\=penguins, x\="bill\_length\_mm", y\="bill\_depth\_mm",
    col\="species", row\="sex", height\=3,
    facet\_kws\=dict(sharex\=False, sharey\=False),
)

Copy to clipboard

![../_images/lmplot_10_0.png](https://seaborn.pydata.org/_images/lmplot_10_0.png)