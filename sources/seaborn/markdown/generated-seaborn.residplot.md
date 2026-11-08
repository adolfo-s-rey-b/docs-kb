 

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

seaborn.residplot[#](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn-residplot "Permalink to this heading")

================================================================================================================================

seaborn.residplot(_data\=None_, _\*_, _x\=None_, _y\=None_, _x\_partial\=None_, _y\_partial\=None_, _lowess\=False_, _order\=1_, _robust\=False_, _dropna\=True_, _label\=None_, _color\=None_, _scatter\_kws\=None_, _line\_kws\=None_, _ax\=None_)[#](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot "Permalink to this definition")

Plot the residuals of a linear regression.

This function will regress y on x (possibly as a robust or polynomial regression) and then draw a scatterplot of the residuals. You can optionally fit a lowess smoother to the residual plot, which can help in determining if there is structure to the residuals.

Parameters:

**data**DataFrame, optional

DataFrame to use if `x` and `y` are column names.

**x**vector or string

Data or column name in `data` for the predictor variable.

**y**vector or string

Data or column name in `data` for the response variable.

**{x, y}\_partial**vectors or string(s) , optional

These variables are treated as confounding and are removed from the `x` or `y` variables before plotting.

**lowess**boolean, optional

Fit a lowess smoother to the residual scatterplot.

**order**int, optional

Order of the polynomial to fit when calculating the residuals.

**robust**boolean, optional

Fit a robust linear regression when calculating the residuals.

**dropna**boolean, optional

If True, ignore observations with missing data when fitting and plotting.

**label**string, optional

Label that will be used in any plot legends.

**color**matplotlib color, optional

Color to use for all elements of the plot.

**{scatter, line}\_kws**dictionaries, optional

Additional keyword arguments passed to scatter() and plot() for drawing the components of the plot.

**ax**matplotlib axis, optional

Plot into this axis, otherwise grab the current axis or make a new one if not existing.

Returns:

ax: matplotlib axes

Axes with the regression plot.

See also

[`regplot`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")

Plot a simple linear regression model.

[`jointplot`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

Draw a [`residplot()`](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot "seaborn.residplot")
 with univariate marginal distributions (when used with `kind="resid"`).

Examples

Pass `x` and `y` to see a scatter plot of the residuals after fitting a simple regression model:

sns.residplot(data\=mpg, x\="weight", y\="displacement")

Copy to clipboard

![../_images/residplot_1_0.png](https://seaborn.pydata.org/_images/residplot_1_0.png)

Structure in the residual plot can reveal a violation of linear regression assumptions:

sns.residplot(data\=mpg, x\="horsepower", y\="mpg")

Copy to clipboard

![../_images/residplot_3_0.png](https://seaborn.pydata.org/_images/residplot_3_0.png)

Remove higher-order trends to test whether that stabilizes the residuals:

sns.residplot(data\=mpg, x\="horsepower", y\="mpg", order\=2)

Copy to clipboard

![../_images/residplot_5_0.png](https://seaborn.pydata.org/_images/residplot_5_0.png)

Adding a LOWESS curve can help reveal or emphasize structure:

sns.residplot(data\=mpg, x\="horsepower", y\="mpg", lowess\=True, line\_kws\=dict(color\="r"))

Copy to clipboard

![../_images/residplot_7_0.png](https://seaborn.pydata.org/_images/residplot_7_0.png)