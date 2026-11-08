 

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

seaborn.objects.Shift[#](https://seaborn.pydata.org/generated/seaborn.objects.Shift.html#seaborn-objects-shift "Permalink to this heading")

============================================================================================================================================

_class_ seaborn.objects.Shift(_x\=0_, _y\=0_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Shift.html#seaborn.objects.Shift "Permalink to this definition")

Displacement of all marks with the same magnitude / direction.

Parameters:

**x, y**float

Magnitude of shift, in data units, along each axis.

Examples

Use this transform to layer multiple marks that would otherwise overlap and be hard to interpret:

(
    so.Plot(penguins, "species", "body\_mass\_g")
    .add(so.Dots(), so.Jitter())
    .add(so.Range(), so.Perc(\[25, 75\]), so.Shift(x\=.2))
)

Copy to clipboard

[![../_images/objects.Shift_1_0.png](https://seaborn.pydata.org/_images/objects.Shift_1_0.png)](https://seaborn.pydata.org/_images/objects.Shift_1_0.png)

For y variables with a nominal scale, bear in mind that the axis will be inverted and a positive shift will move downwards:

(
    so.Plot(diamonds, "carat", "clarity")
    .add(so.Dots(), so.Jitter())
    .add(so.Range(), so.Perc(\[25, 75\]), so.Shift(y\=.25))
)

Copy to clipboard

[![../_images/objects.Shift_3_0.png](https://seaborn.pydata.org/_images/objects.Shift_3_0.png)](https://seaborn.pydata.org/_images/objects.Shift_3_0.png)