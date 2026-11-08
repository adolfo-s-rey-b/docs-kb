 

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

seaborn.choose\_diverging\_palette[#](https://seaborn.pydata.org/generated/seaborn.choose_diverging_palette.html#seaborn-choose-diverging-palette "Permalink to this heading")

===============================================================================================================================================================================

seaborn.choose\_diverging\_palette(_as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.choose_diverging_palette.html#seaborn.choose_diverging_palette "Permalink to this definition")

Launch an interactive widget to choose a diverging color palette.

This corresponds with the [`diverging_palette()`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette")
 function. This kind of palette is good for data that range between interesting low values and interesting high values with a meaningful midpoint. (For example, change scores relative to some baseline value).

Requires IPython 2+ and must be used in the notebook.

Parameters:

**as\_cmap**bool

If True, the return value is a matplotlib colormap rather than a list of discrete colors.

Returns:

**pal or cmap**list of colors or matplotlib colormap

Object that can be passed to plotting functions.

See also

[`diverging_palette`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette")

Create a diverging color palette or colormap.

[`choose_colorbrewer_palette`](https://seaborn.pydata.org/generated/seaborn.choose_colorbrewer_palette.html#seaborn.choose_colorbrewer_palette "seaborn.choose_colorbrewer_palette")

Interactively choose palettes from the colorbrewer set, including diverging palettes.