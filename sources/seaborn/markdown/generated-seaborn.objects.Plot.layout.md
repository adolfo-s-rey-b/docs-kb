 

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

seaborn.objects.Plot.layout[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.layout.html#seaborn-objects-plot-layout "Permalink to this heading")

==============================================================================================================================================================

Plot.layout(_\*_, _size=<default>_, _engine=<default>_, _extent=<default>_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.layout.html#seaborn.objects.Plot.layout "Permalink to this definition")

Control the figure size and layout.

Note

Default figure sizes and the API for specifying the figure size are subject to change in future “experimental” releases of the objects API. The default layout engine may also change.

Parameters:

**size**(width, height)

Size of the resulting figure, in inches. Size is inclusive of legend when using pyplot, but not otherwise.

**engine**{{“tight”, “constrained”, “none”}}

Name of method for automatically adjusting the layout to remove overlap. The default depends on whether [`Plot.on()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn.objects.Plot.on "seaborn.objects.Plot.on")
 is used.

**extent**(left, bottom, right, top)

Boundaries of the plot layout, in fractions of the figure size. Takes effect through the layout engine; exact results will vary across engines. Note: the extent includes axis decorations when using a layout engine, but it is exclusive of them when `engine="none"`.

Examples

Control the overall dimensions of the figure with `size`:

p \= so.Plot().layout(size\=(4, 4))
p

Copy to clipboard

[![../_images/objects.Plot.layout_1_0.png](https://seaborn.pydata.org/_images/objects.Plot.layout_1_0.png)](https://seaborn.pydata.org/_images/objects.Plot.layout_1_0.png)

Subplots created by using [`Plot.facet()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn.objects.Plot.facet "seaborn.objects.Plot.facet")
 or [`Plot.pair()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html#seaborn.objects.Plot.pair "seaborn.objects.Plot.pair")
 will shrink to fit in the available space:

p.facet(\["A", "B"\], \["X", "Y"\])

Copy to clipboard

[![../_images/objects.Plot.layout_3_0.png](https://seaborn.pydata.org/_images/objects.Plot.layout_3_0.png)](https://seaborn.pydata.org/_images/objects.Plot.layout_3_0.png)

You may find that different automatic layout engines give better or worse results with specific plots:

p.facet(\["A", "B"\], \["X", "Y"\]).layout(engine\="constrained")

Copy to clipboard

[![../_images/objects.Plot.layout_5_0.png](https://seaborn.pydata.org/_images/objects.Plot.layout_5_0.png)](https://seaborn.pydata.org/_images/objects.Plot.layout_5_0.png)

With `extent`, you can control the size of the plot relative to the underlying figure. Because the notebook display adapts the figure background to the plot, this appears only to change the plot size in a notebook context. But it can be useful when saving or displaying through a `pyplot` GUI window:

p.layout(extent\=\[0, 0, .8, 1\]).show()

Copy to clipboard

![../_images/objects.Plot.layout_7_0.png](https://seaborn.pydata.org/_images/objects.Plot.layout_7_0.png)