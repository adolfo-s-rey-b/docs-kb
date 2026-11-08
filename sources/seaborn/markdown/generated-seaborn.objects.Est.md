 

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

seaborn.objects.Est[#](https://seaborn.pydata.org/generated/seaborn.objects.Est.html#seaborn-objects-est "Permalink to this heading")

======================================================================================================================================

_class_ seaborn.objects.Est(_func\='mean'_, _errorbar\=('ci', 95)_, _n\_boot\=1000_, _seed\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Est.html#seaborn.objects.Est "Permalink to this definition")

Calculate a point estimate and error bar interval.

For more information about the various `errorbar` choices, see the [errorbar tutorial](https://seaborn.pydata.org/tutorial/error_bars.html)
.

Additional variables:

*   **weight**: When passed to a layer that uses this stat, a weighted estimate will be computed. Note that use of weights currently limits the choice of function and error bar method to `"mean"` and `"ci"`, respectively.
    

Parameters:

**func**str or callable

Name of a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v1.26)")
 method or a vector -> scalar function.

**errorbar**str, (str, float) tuple, or callable

Name of errorbar method (one of “ci”, “pi”, “se” or “sd”), or a tuple with a method name ane a level parameter, or a function that maps from a vector to a (min, max) interval.

**n\_boot**int

Number of bootstrap samples to draw for “ci” errorbars.

**seed**int

Seed for the PRNG used to draw bootstrap samples.

Examples

The default behavior is to compute the mean and 95% confidence interval (using bootstrapping):

p \= so.Plot(diamonds, "clarity", "carat")
p.add(so.Range(), so.Est())

Copy to clipboard

[![../_images/objects.Est_1_0.png](https://seaborn.pydata.org/_images/objects.Est_1_0.png)](https://seaborn.pydata.org/_images/objects.Est_1_0.png)

Other estimators may be selected by name if they are pandas methods:

p.add(so.Range(), so.Est("median"))

Copy to clipboard

[![../_images/objects.Est_3_0.png](https://seaborn.pydata.org/_images/objects.Est_3_0.png)](https://seaborn.pydata.org/_images/objects.Est_3_0.png)

There are several options for computing the error bar interval, such as (scaled) standard errors:

p.add(so.Range(), so.Est(errorbar\="se"))

Copy to clipboard

[![../_images/objects.Est_5_0.png](https://seaborn.pydata.org/_images/objects.Est_5_0.png)](https://seaborn.pydata.org/_images/objects.Est_5_0.png)

The error bars can also represent the spread of the distribution around the estimate using (scaled) standard deviations:

p.add(so.Range(), so.Est(errorbar\="sd"))

Copy to clipboard

[![../_images/objects.Est_7_0.png](https://seaborn.pydata.org/_images/objects.Est_7_0.png)](https://seaborn.pydata.org/_images/objects.Est_7_0.png)

Because confidence intervals are computed using bootstrapping, there will be small amounts of randomness. Reduce the random variability by increasing the nubmer of bootstrap iterations (although this will be slower), or eliminate it by seeding the random number generator:

p.add(so.Range(), so.Est(seed\=0))

Copy to clipboard

[![../_images/objects.Est_9_0.png](https://seaborn.pydata.org/_images/objects.Est_9_0.png)](https://seaborn.pydata.org/_images/objects.Est_9_0.png)

To compute a weighted estimate (and confidence interval), assign a `weight` variable in the layer where you use the stat:

p.add(so.Range(), so.Est(), weight\="price")

Copy to clipboard

[![../_images/objects.Est_11_0.png](https://seaborn.pydata.org/_images/objects.Est_11_0.png)](https://seaborn.pydata.org/_images/objects.Est_11_0.png)