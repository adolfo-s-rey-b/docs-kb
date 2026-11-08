 

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

seaborn.FacetGrid.refline[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.refline.html#seaborn-facetgrid-refline "Permalink to this heading")

========================================================================================================================================================

FacetGrid.refline(_\*_, _x\=None_, _y\=None_, _color\='.5'_, _linestyle\='--'_, _\*\*line\_kws_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.refline.html#seaborn.FacetGrid.refline "Permalink to this definition")

Add a reference line(s) to each facet.

Parameters:

**x, y**numeric

Value(s) to draw the line(s) at.

**color**[`matplotlib color`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "(in Matplotlib v3.8.2)")

Specifies the color of the reference line(s). Pass `color=None` to use `hue` mapping.

**linestyle**str

Specifies the style of the reference line(s).

**line\_kws**key, value mappings

Other keyword arguments are passed to [`matplotlib.axes.Axes.axvline()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "(in Matplotlib v3.8.2)")
 when `x` is not None and [`matplotlib.axes.Axes.axhline()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "(in Matplotlib v3.8.2)")
 when `y` is not None.

Returns:

[`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")
 instance

Returns `self` for easy method chaining.