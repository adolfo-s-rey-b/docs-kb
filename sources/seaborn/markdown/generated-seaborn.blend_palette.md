 

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

seaborn.blend\_palette[#](https://seaborn.pydata.org/generated/seaborn.blend_palette.html#seaborn-blend-palette "Permalink to this heading")

=============================================================================================================================================

seaborn.blend\_palette(_colors_, _n\_colors\=6_, _as\_cmap\=False_, _input\='rgb'_)[#](https://seaborn.pydata.org/generated/seaborn.blend_palette.html#seaborn.blend_palette "Permalink to this definition")

Make a palette that blends between a list of colors.

Parameters:

**colors**sequence of colors in various formats interpreted by `input`

hex code, html color name, or tuple in `input` space.

**n\_colors**int, optional

Number of colors in the palette.

**as\_cmap**bool, optional

If True, return a [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")
.

Returns:

palette

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

Examples