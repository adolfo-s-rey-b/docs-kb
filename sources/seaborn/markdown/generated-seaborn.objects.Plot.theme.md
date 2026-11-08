 

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

seaborn.objects.Plot.theme[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn-objects-plot-theme "Permalink to this heading")

===========================================================================================================================================================

Plot.theme(_config_, _/_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn.objects.Plot.theme "Permalink to this definition")

Control the appearance of elements in the plot.

Note

The API for customizing plot appearance is not yet finalized. Currently, the only valid argument is a dict of matplotlib rc parameters. (This dict must be passed as a positional argument.)

It is likely that this method will be enhanced in future releases.

Matplotlib rc parameters are documented on the following page: [https://matplotlib.org/stable/tutorials/introductory/customizing.html](https://matplotlib.org/stable/tutorials/introductory/customizing.html)

Examples

The default theme uses the same parameters as [`seaborn.set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
 with no additional arguments:

p \= (
    so.Plot(anscombe, "x", "y", color\="dataset")
    .facet("dataset", wrap\=2)
    .add(so.Line(), so.PolyFit(order\=1))
    .add(so.Dot())
)
p

Copy to clipboard

[![../_images/objects.Plot.theme_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_1_0.png)

Pass a dictionary of rc parameters to change the appearance of the plot:

p.theme({"axes.facecolor": "w", "axes.edgecolor": "slategray"})

Copy to clipboard

[![../_images/objects.Plot.theme_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_3_0.png)

Many (though not all) mark properties will reflect theme parameters by default:

p.theme({"lines.linewidth": 4})

Copy to clipboard

[![../_images/objects.Plot.theme_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_5_0.png)

Apply seaborn styles by passing in the output of the style functions:

from seaborn import axes\_style
p.theme(axes\_style("ticks"))

Copy to clipboard

[![../_images/objects.Plot.theme_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_7_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_7_0.png)

Or apply styles that ship with matplotlib:

from matplotlib import style
p.theme(style.library\["fivethirtyeight"\])

Copy to clipboard

[![../_images/objects.Plot.theme_9_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_9_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_9_0.png)

Multiple parameter dictionaries should be passed to the same function call. On Python 3.9+, you can use dictionary union syntax for this:

from seaborn import plotting\_context
p.theme(axes\_style("whitegrid") | plotting\_context("talk"))

Copy to clipboard

[![../_images/objects.Plot.theme_11_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_11_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_11_0.png)

The default theme for all [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 instances can be changed using the `Plot.config` attribute:

so.Plot.config.theme.update(axes\_style("white"))
p

Copy to clipboard

[![../_images/objects.Plot.theme_13_0.png](https://seaborn.pydata.org/_images/objects.Plot.theme_13_0.png)](https://seaborn.pydata.org/_images/objects.Plot.theme_13_0.png)

See [Plot Configuration](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#plot-config)
 for more details.