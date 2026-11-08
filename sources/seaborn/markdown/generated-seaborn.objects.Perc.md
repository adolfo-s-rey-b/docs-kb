 

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

seaborn.objects.Perc[#](https://seaborn.pydata.org/generated/seaborn.objects.Perc.html#seaborn-objects-perc "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Perc(_k\=5_, _method\='linear'_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Perc.html#seaborn.objects.Perc "Permalink to this definition")

Replace observations with percentile values.

Parameters:

**k**list of numbers or int

If a list of numbers, this gives the percentiles (in \[0, 100\]) to compute. If an integer, compute `k` evenly-spaced percentiles between 0 and 100. For example, `k=5` computes the 0, 25, 50, 75, and 100th percentiles.

**method**str

Method for interpolating percentiles between observed datapoints. See [`numpy.percentile()`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "(in NumPy v1.26)")
 for valid options and more information.

Examples

The default behavior computes the quartiles and min/max of the input data:

p \= (
    so.Plot(diamonds, "cut", "price")
    .scale(y\="log")
)
p.add(so.Dot(), so.Perc())

Copy to clipboard

[![../_images/objects.Perc_1_0.png](https://seaborn.pydata.org/_images/objects.Perc_1_0.png)](https://seaborn.pydata.org/_images/objects.Perc_1_0.png)

Passing an integer will compute that many evenly-spaced percentiles:

p.add(so.Dot(), so.Perc(20))

Copy to clipboard

[![../_images/objects.Perc_3_0.png](https://seaborn.pydata.org/_images/objects.Perc_3_0.png)](https://seaborn.pydata.org/_images/objects.Perc_3_0.png)

Passing a list will compute exactly those percentiles:

p.add(so.Dot(), so.Perc(\[10, 25, 50, 75, 90\]))

Copy to clipboard

[![../_images/objects.Perc_5_0.png](https://seaborn.pydata.org/_images/objects.Perc_5_0.png)](https://seaborn.pydata.org/_images/objects.Perc_5_0.png)

Combine with a range mark to show a percentile interval:

(
    so.Plot(diamonds, "price", "cut")
    .add(so.Dots(pointsize\=1, alpha\=.2), so.Jitter(.3))
    .add(so.Range(color\="k"), so.Perc(\[25, 75\]), so.Shift(y\=.2))
    .scale(x\="log")
)

Copy to clipboard

[![../_images/objects.Perc_7_0.png](https://seaborn.pydata.org/_images/objects.Perc_7_0.png)](https://seaborn.pydata.org/_images/objects.Perc_7_0.png)