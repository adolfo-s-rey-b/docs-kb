 

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

seaborn.choose\_colorbrewer\_palette[#](https://seaborn.pydata.org/generated/seaborn.choose_colorbrewer_palette.html#seaborn-choose-colorbrewer-palette "Permalink to this heading")

=====================================================================================================================================================================================

seaborn.choose\_colorbrewer\_palette(_data\_type_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.choose_colorbrewer_palette.html#seaborn.choose_colorbrewer_palette "Permalink to this definition")

Select a palette from the ColorBrewer set.

These palettes are built into matplotlib and can be used by name in many seaborn functions, or by passing the object returned by this function.

Parameters:

**data\_type**{‘sequential’, ‘diverging’, ‘qualitative’}

This describes the kind of data you want to visualize. See the seaborn color palette docs for more information about how to choose this value. Note that you can pass substrings (e.g. ‘q’ for ‘qualitative.

**as\_cmap**bool

If True, the return value is a matplotlib colormap rather than a list of discrete colors.

Returns:

**pal or cmap**list of colors or matplotlib colormap

Object that can be passed to plotting functions.

See also

[`dark_palette`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette")

Create a sequential palette with dark low values.

[`light_palette`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette "seaborn.light_palette")

Create a sequential palette with bright low values.

[`diverging_palette`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette")

Create a diverging palette from selected colors.

[`cubehelix_palette`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette")

Create a sequential palette or colormap using the cubehelix system.