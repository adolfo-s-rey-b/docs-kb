 

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

seaborn.mpl\_palette[#](https://seaborn.pydata.org/generated/seaborn.mpl_palette.html#seaborn-mpl-palette "Permalink to this heading")

=======================================================================================================================================

seaborn.mpl\_palette(_name_, _n\_colors\=6_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.mpl_palette.html#seaborn.mpl_palette "Permalink to this definition")

Return a palette or colormap from the matplotlib registry.

For continuous palettes, evenly-spaced discrete samples are chosen while excluding the minimum and maximum value in the colormap to provide better contrast at the extremes.

For qualitative palettes (e.g. those from colorbrewer), exact values are indexed (rather than interpolated), but fewer than `n_colors` can be returned if the palette does not define that many.

Parameters:

**name**string

Name of the palette. This should be a named matplotlib colormap.

**n\_colors**int

Number of discrete colors in the palette.

Returns:

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

Examples

Return discrete samples from a continuous matplotlib colormap:

sns.mpl\_palette("viridis")

Copy to clipboard

Return the continuous colormap instead; note how the extreme values are more intense:

sns.mpl\_palette("viridis", as\_cmap\=True)

Copy to clipboard

![viridis color map](<Base64-Image-Removed>)

Return more colors:

sns.mpl\_palette("viridis", 8)

Copy to clipboard

Return values from a qualitative colormap:

sns.mpl\_palette("Set2")

Copy to clipboard

Notice how the palette will only contain distinct colors and can be shorter than requested:

sns.mpl\_palette("Set2", 10)

Copy to clipboard