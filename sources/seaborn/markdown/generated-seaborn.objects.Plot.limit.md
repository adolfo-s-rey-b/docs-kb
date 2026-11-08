 

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

seaborn.objects.Plot.limit[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.limit.html#seaborn-objects-plot-limit "Permalink to this heading")

===========================================================================================================================================================

Plot.limit(_\*\*limits_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.limit.html#seaborn.objects.Plot.limit "Permalink to this definition")

Control the range of visible data.

Keywords correspond to variables defined in the plot, and values are a `(min, max)` tuple (where either can be `None` to leave unset).

Limits apply only to the axis; data outside the visible range are still used for any stat transforms and added to the plot.

Behavior for non-coordinate variables is currently undefined.

Examples

By default, plot limits are automatically set to provide a small margin around the data (controlled by [`Plot.theme()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn.objects.Plot.theme "seaborn.objects.Plot.theme")
 parameters `axes.xmargin` and `axes.ymargin`):

p \= so.Plot(x\=\[1, 2, 3\], y\=\[1, 3, 2\]).add(so.Line(marker\="o"))
p

Copy to clipboard

[![../_images/objects.Plot.limit_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.limit_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.limit_1_0.png)

Pass a `min`/`max` tuple to pin the limits at specific values:

p.limit(x\=(0, 4), y\=(\-1, 6))

Copy to clipboard

[![../_images/objects.Plot.limit_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.limit_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.limit_3_0.png)

Reversing the `min`/`max` values will invert the axis:

p.limit(y\=(4, 0))

Copy to clipboard

[![../_images/objects.Plot.limit_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.limit_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.limit_5_0.png)

Use `None` for either side to maintain the default value:

p.limit(y\=(0, None))

Copy to clipboard

[![../_images/objects.Plot.limit_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.limit_7_0.png)](https://seaborn.pydata.org/_images/objects.Plot.limit_7_0.png)