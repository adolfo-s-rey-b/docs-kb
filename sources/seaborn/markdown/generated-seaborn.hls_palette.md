 

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

seaborn.hls\_palette[#](https://seaborn.pydata.org/generated/seaborn.hls_palette.html#seaborn-hls-palette "Permalink to this heading")

=======================================================================================================================================

seaborn.hls\_palette(_n\_colors\=6_, _h\=0.01_, _l\=0.6_, _s\=0.65_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.hls_palette.html#seaborn.hls_palette "Permalink to this definition")

Return hues with constant lightness and saturation in the HLS system.

The hues are evenly sampled along a circular path. The resulting palette will be appropriate for categorical or cyclical data.

The `h`, `l`, and `s` values should be between 0 and 1.

Note

While the separation of the resulting colors will be mathematically constant, the HLS system does not construct a perceptually-uniform space, so their apparent intensity will vary.

Parameters:

**n\_colors**int

Number of colors in the palette.

**h**float

The value of the first hue.

**l**float

The lightness value.

**s**float

The saturation intensity.

**as\_cmap**bool

If True, return a matplotlib colormap object.

Returns:

palette

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

See also

[`husl_palette`](https://seaborn.pydata.org/generated/seaborn.husl_palette.html#seaborn.husl_palette "seaborn.husl_palette")

Make a palette using evenly spaced hues in the HUSL system.

Examples

By default, return 6 colors with identical lightness and saturation and evenly-sampled hues:

sns.hls\_palette()

Copy to clipboard

Increase the number of colors:

sns.hls\_palette(8)

Copy to clipboard

Decrease the lightness:

sns.hls\_palette(l\=.3)

Copy to clipboard

Decrease the saturation:

sns.hls\_palette(s\=.3)

Copy to clipboard

Change the start-point for hue sampling:

sns.hls\_palette(h\=.5)

Copy to clipboard

Return a continuous colormap. Notice the perceptual discontinuities, especially around yellow, cyan, and magenta:

sns.hls\_palette(as\_cmap\=True)

Copy to clipboard

![hls color map](<Base64-Image-Removed>)