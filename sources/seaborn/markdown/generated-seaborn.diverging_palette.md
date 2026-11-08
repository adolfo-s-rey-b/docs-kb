 

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

seaborn.diverging\_palette[#](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn-diverging-palette "Permalink to this heading")

=========================================================================================================================================================

seaborn.diverging\_palette(_h\_neg_, _h\_pos_, _s\=75_, _l\=50_, _sep\=1_, _n\=6_, _center\='light'_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "Permalink to this definition")

Make a diverging palette between two HUSL colors.

If you are using the IPython notebook, you can also choose this palette interactively with the [`choose_diverging_palette()`](https://seaborn.pydata.org/generated/seaborn.choose_diverging_palette.html#seaborn.choose_diverging_palette "seaborn.choose_diverging_palette")
 function.

Parameters:

**h\_neg, h\_pos**float in \[0, 359\]

Anchor hues for negative and positive extents of the map.

**s**float in \[0, 100\], optional

Anchor saturation for both extents of the map.

**l**float in \[0, 100\], optional

Anchor lightness for both extents of the map.

**sep**int, optional

Size of the intermediate region.

**n**int, optional

Number of colors in the palette (if not returning a cmap)

**center**{“light”, “dark”}, optional

Whether the center of the palette is light or dark

**as\_cmap**bool, optional

If True, return a [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")
.

Returns:

palette

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

See also

[`dark_palette`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette")

Create a sequential palette with dark values.

[`light_palette`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette "seaborn.light_palette")

Create a sequential palette with light values.

Examples