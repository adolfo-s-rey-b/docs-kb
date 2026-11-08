 

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

seaborn.objects.Jitter[#](https://seaborn.pydata.org/generated/seaborn.objects.Jitter.html#seaborn-objects-jitter "Permalink to this heading")

===============================================================================================================================================

_class_ seaborn.objects.Jitter(_width=<default>_, _x=0_, _y=0_, _seed=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Jitter.html#seaborn.objects.Jitter "Permalink to this definition")

Random displacement along one or both axes to reduce overplotting.

Parameters:

**width**float

Magnitude of jitter, relative to mark width, along the orientation axis. If not provided, the default value will be 0 when `x` or `y` are set, otherwise there will be a small amount of jitter applied by default.

**x**float

Magnitude of jitter, in data units, along the x axis.

**y**float

Magnitude of jitter, in data units, along the y axis.

Examples

When used without any arguments, a small amount of jitter will be applied along the orientation axis:

(
    so.Plot(penguins, "species", "body\_mass\_g")
    .add(so.Dots(), so.Jitter())
)

Copy to clipboard

[![../_images/objects.Jitter_1_0.png](https://seaborn.pydata.org/_images/objects.Jitter_1_0.png)](https://seaborn.pydata.org/_images/objects.Jitter_1_0.png)

The `width` parameter controls the amount of jitter relative to the spacing between the marks:

(
    so.Plot(penguins, "species", "body\_mass\_g")
    .add(so.Dots(), so.Jitter(.5))
)

Copy to clipboard

[![../_images/objects.Jitter_3_0.png](https://seaborn.pydata.org/_images/objects.Jitter_3_0.png)](https://seaborn.pydata.org/_images/objects.Jitter_3_0.png)

The `width` parameter always applies to the orientation axis, so the direction of jitter will adapt along with the orientation:

(
    so.Plot(penguins, "body\_mass\_g", "species")
    .add(so.Dots(), so.Jitter(.5))
)

Copy to clipboard

[![../_images/objects.Jitter_5_0.png](https://seaborn.pydata.org/_images/objects.Jitter_5_0.png)](https://seaborn.pydata.org/_images/objects.Jitter_5_0.png)

Because the `width` jitter is relative, it can be used when the orientation axis is numeric without further tweaking:

(
    so.Plot(penguins\["body\_mass\_g"\].round(\-3), penguins\["flipper\_length\_mm"\])
    .add(so.Dots(), so.Jitter())
)

Copy to clipboard

[![../_images/objects.Jitter_7_0.png](https://seaborn.pydata.org/_images/objects.Jitter_7_0.png)](https://seaborn.pydata.org/_images/objects.Jitter_7_0.png)

In contrast to `width`, the `x` and `y` parameters always refer to specific axes and control the jitter in data units:

(
    so.Plot(penguins\["body\_mass\_g"\].round(\-3), penguins\["flipper\_length\_mm"\])
    .add(so.Dots(), so.Jitter(x\=100))
)

Copy to clipboard

[![../_images/objects.Jitter_9_0.png](https://seaborn.pydata.org/_images/objects.Jitter_9_0.png)](https://seaborn.pydata.org/_images/objects.Jitter_9_0.png)

Both `x` and `y` can be used in a single transform:

(
    so.Plot(
        penguins\["body\_mass\_g"\].round(\-3),
        penguins\["flipper\_length\_mm"\].round(\-1),
    )
    .add(so.Dots(), so.Jitter(x\=200, y\=5))
)

Copy to clipboard

[![../_images/objects.Jitter_11_0.png](https://seaborn.pydata.org/_images/objects.Jitter_11_0.png)](https://seaborn.pydata.org/_images/objects.Jitter_11_0.png)