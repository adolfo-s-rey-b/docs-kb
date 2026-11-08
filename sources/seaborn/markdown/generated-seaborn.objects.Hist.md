 

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

seaborn.objects.Hist[#](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn-objects-hist "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Hist(_stat\='count'_, _bins\='auto'_, _binwidth\=None_, _binrange\=None_, _common\_norm\=True_, _common\_bins\=True_, _cumulative\=False_, _discrete\=False_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Hist.html#seaborn.objects.Hist "Permalink to this definition")

Bin observations, count them, and optionally normalize or cumulate.

Parameters:

**stat**str

Aggregate statistic to compute in each bin:

*   `count`: the number of observations
    
*   `density`: normalize so that the total area of the histogram equals 1
    
*   `percent`: normalize so that bar heights sum to 100
    
*   `probability` or `proportion`: normalize so that bar heights sum to 1
    
*   `frequency`: divide the number of observations by the bin width
    

**bins**str, int, or ArrayLike

Generic parameter that can be the name of a reference rule, the number of bins, or the bin breaks. Passed to [`numpy.histogram_bin_edges()`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "(in NumPy v1.26)")
.

**binwidth**float

Width of each bin; overrides `bins` but can be used with `binrange`. Note that if `binwidth` does not evenly divide the bin range, the actual bin width used will be only approximately equal to the parameter value.

**binrange**(min, max)

Lowest and highest value for bin edges; can be used with either `bins` (when a number) or `binwidth`. Defaults to data extremes.

**common\_norm**bool or list of variables

When not `False`, the normalization is applied across groups. Use `True` to normalize across all groups, or pass variable name(s) that define normalization groups.

**common\_bins**bool or list of variables

When not `False`, the same bins are used for all groups. Use `True` to share bins across all groups, or pass variable name(s) to share within.

**cumulative**bool

If True, cumulate the bin values.

**discrete**bool

If True, set `binwidth` and `binrange` so that bins have unit width and are centered on integer values

Notes

The choice of bins for computing and plotting a histogram can exert substantial influence on the insights that one is able to draw from the visualization. If the bins are too large, they may erase important features. On the other hand, bins that are too small may be dominated by random variability, obscuring the shape of the true underlying distribution. The default bin size is determined using a reference rule that depends on the sample size and variance. This works well in many cases, (i.e., with “well-behaved” data) but it fails in others. It is always a good to try different bin sizes to be sure that you are not missing something important. This function allows you to specify bins in several different ways, such as by setting the total number of bins to use, the width of each bin, or the specific locations where the bins should break.

Examples

For discrete or categorical variables, this stat is commonly combined with a [`Bar`](https://seaborn.pydata.org/generated/seaborn.objects.Bar.html#seaborn.objects.Bar "seaborn.objects.Bar")
 mark:

so.Plot(penguins, "island").add(so.Bar(), so.Hist())

Copy to clipboard

[![../_images/objects.Hist_1_0.png](https://seaborn.pydata.org/_images/objects.Hist_1_0.png)](https://seaborn.pydata.org/_images/objects.Hist_1_0.png)

When used to estimate a univariate distribution, it is better to use the [`Bars`](https://seaborn.pydata.org/generated/seaborn.objects.Bars.html#seaborn.objects.Bars "seaborn.objects.Bars")
 mark:

p \= so.Plot(penguins, "flipper\_length\_mm")
p.add(so.Bars(), so.Hist())

Copy to clipboard

[![../_images/objects.Hist_3_0.png](https://seaborn.pydata.org/_images/objects.Hist_3_0.png)](https://seaborn.pydata.org/_images/objects.Hist_3_0.png)

The granularity of the bins will influence whether the underlying distribution is accurately represented. Adjust it by setting the total number:

p.add(so.Bars(), so.Hist(bins\=20))

Copy to clipboard

[![../_images/objects.Hist_5_0.png](https://seaborn.pydata.org/_images/objects.Hist_5_0.png)](https://seaborn.pydata.org/_images/objects.Hist_5_0.png)

Alternatively, specify the _width_ of the bins:

p.add(so.Bars(), so.Hist(binwidth\=5))

Copy to clipboard

[![../_images/objects.Hist_7_0.png](https://seaborn.pydata.org/_images/objects.Hist_7_0.png)](https://seaborn.pydata.org/_images/objects.Hist_7_0.png)

By default, the transform returns the count of observations in each bin. The counts can be normalized, e.g. to show a proportion:

p.add(so.Bars(), so.Hist(stat\="proportion"))

Copy to clipboard

[![../_images/objects.Hist_9_0.png](https://seaborn.pydata.org/_images/objects.Hist_9_0.png)](https://seaborn.pydata.org/_images/objects.Hist_9_0.png)

When additional variables define groups, the default behavior is to normalize across all groups:

p \= p.facet("island")
p.add(so.Bars(), so.Hist(stat\="proportion"))

Copy to clipboard

[![../_images/objects.Hist_11_0.png](https://seaborn.pydata.org/_images/objects.Hist_11_0.png)](https://seaborn.pydata.org/_images/objects.Hist_11_0.png)

Pass `common_norm=False` to normalize each distribution independently:

p.add(so.Bars(), so.Hist(stat\="proportion", common\_norm\=False))

Copy to clipboard

[![../_images/objects.Hist_13_0.png](https://seaborn.pydata.org/_images/objects.Hist_13_0.png)](https://seaborn.pydata.org/_images/objects.Hist_13_0.png)

Or, with more than one grouping varible, specify a subset to normalize within:

p.add(so.Bars(), so.Hist(stat\="proportion", common\_norm\=\["col"\]), color\="sex")

Copy to clipboard

[![../_images/objects.Hist_15_0.png](https://seaborn.pydata.org/_images/objects.Hist_15_0.png)](https://seaborn.pydata.org/_images/objects.Hist_15_0.png)

When distributions overlap it may be easier to discern their shapes with an [`Area`](https://seaborn.pydata.org/generated/seaborn.objects.Area.html#seaborn.objects.Area "seaborn.objects.Area")
 mark:

p.add(so.Area(), so.Hist(), color\="sex")

Copy to clipboard

[![../_images/objects.Hist_17_0.png](https://seaborn.pydata.org/_images/objects.Hist_17_0.png)](https://seaborn.pydata.org/_images/objects.Hist_17_0.png)

Or add [`Stack`](https://seaborn.pydata.org/generated/seaborn.objects.Stack.html#seaborn.objects.Stack "seaborn.objects.Stack")
 move to represent a part-whole relationship:

p.add(so.Bars(), so.Hist(), so.Stack(), color\="sex")

Copy to clipboard

[![../_images/objects.Hist_19_0.png](https://seaborn.pydata.org/_images/objects.Hist_19_0.png)](https://seaborn.pydata.org/_images/objects.Hist_19_0.png)