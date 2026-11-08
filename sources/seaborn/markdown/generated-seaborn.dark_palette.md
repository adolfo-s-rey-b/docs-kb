 

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

seaborn.dark\_palette[#](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn-dark-palette "Permalink to this heading")

==========================================================================================================================================

seaborn.dark\_palette(_color_, _n\_colors\=6_, _reverse\=False_, _as\_cmap\=False_, _input\='rgb'_)[#](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "Permalink to this definition")

Make a sequential palette that blends from dark to `color`.

This kind of palette is good for data that range between relatively uninteresting low values and interesting high values.

The `color` parameter can be specified in a number of ways, including all options for defining a color in matplotlib and several additional color spaces that are handled by seaborn. You can also use the database of named colors from the XKCD color survey.

If you are using the IPython notebook, you can also choose this palette interactively with the [`choose_dark_palette()`](https://seaborn.pydata.org/generated/seaborn.choose_dark_palette.html#seaborn.choose_dark_palette "seaborn.choose_dark_palette")
 function.

Parameters:

**color**base color for high values

hex, rgb-tuple, or html color name

**n\_colors**int, optional

number of colors in the palette

**reverse**bool, optional

if True, reverse the direction of the blend

**as\_cmap**bool, optional

If True, return a [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")
.

**input**{‘rgb’, ‘hls’, ‘husl’, xkcd’}

Color space to interpret the input color. The first three options apply to tuple inputs and the latter applies to string inputs.

Returns:

palette

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

See also

[`light_palette`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette "seaborn.light_palette")

Create a sequential palette with bright low values.

[`diverging_palette`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette")

Create a diverging palette with two colors.

Examples

Define a sequential ramp from a dark gray to a specified color:

sns.dark\_palette("seagreen")

Copy to clipboard

Specify the color with a hex code:

sns.dark\_palette("#79C")

Copy to clipboard

Specify the color from the husl system:

sns.dark\_palette((20, 60, 50), input\="husl")

Copy to clipboard

Increase the number of colors:

sns.dark\_palette("xkcd:golden", 8)

Copy to clipboard

Return a continuous colormap rather than a discrete palette:

sns.dark\_palette("#b285bc", as\_cmap\=True)

Copy to clipboard

![blend color map](<Base64-Image-Removed>)