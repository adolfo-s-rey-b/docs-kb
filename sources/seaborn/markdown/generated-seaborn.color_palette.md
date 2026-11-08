 

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

seaborn.color\_palette[#](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn-color-palette "Permalink to this heading")

=============================================================================================================================================

seaborn.color\_palette(_palette\=None_, _n\_colors\=None_, _desat\=None_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "Permalink to this definition")

Return a list of colors or continuous colormap defining a palette.

Possible `palette` values include:

*   Name of a seaborn palette (deep, muted, bright, pastel, dark, colorblind)
    
*   Name of matplotlib colormap
    
*   ‘husl’ or ‘hls’
    
*   ‘ch:<cubehelix arguments>’
    
*   ‘light:<color>’, ‘dark:<color>’, ‘blend:<color>,<color>’,
    
*   A sequence of colors in any format matplotlib accepts
    

Calling this function with `palette=None` will return the current matplotlib color cycle.

This function can also be used in a `with` statement to temporarily set the color cycle for a plot or set of plots.

See the [tutorial](https://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial)
 for more information.

Parameters:

**palette**None, string, or sequence, optional

Name of palette or None to return current palette. If a sequence, input colors are used but possibly cycled and desaturated.

**n\_colors**int, optional

Number of colors in the palette. If `None`, the default will depend on how `palette` is specified. Named palettes default to 6 colors, but grabbing the current palette or passing in a list of colors will not change the number of colors unless this is specified. Asking for more colors than exist in the palette will cause it to cycle. Ignored when `as_cmap` is True.

**desat**float, optional

Proportion to desaturate each color by.

**as\_cmap**bool

If True, return a [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")
.

Returns:

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

See also

[`set_palette`](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette "seaborn.set_palette")

Set the default color cycle for all plots.

[`set_color_codes`](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn.set_color_codes "seaborn.set_color_codes")

Reassign color codes like `"b"`, `"g"`, etc. to colors from one of the seaborn palettes.

Examples

Calling with no arguments returns all colors from the current default color cycle:

sns.color\_palette()

Copy to clipboard

Other variants on the seaborn categorical color palette can be referenced by name:

sns.color\_palette("pastel")

Copy to clipboard

Return a specified number of evenly spaced hues in the “HUSL” system:

sns.color\_palette("husl", 9)

Copy to clipboard

Return all unique colors in a categorical Color Brewer palette:

sns.color\_palette("Set2")

Copy to clipboard

Return a diverging Color Brewer palette as a continuous colormap:

sns.color\_palette("Spectral", as\_cmap\=True)

Copy to clipboard

![Spectral color map](<Base64-Image-Removed>)

Return one of the perceptually-uniform palettes included in seaborn as a discrete palette:

sns.color\_palette("flare")

Copy to clipboard

Return one of the perceptually-uniform palettes included in seaborn as a continuous colormap:

sns.color\_palette("flare", as\_cmap\=True)

Copy to clipboard

![flare color map](<Base64-Image-Removed>)

Return a customized cubehelix color palette:

sns.color\_palette("ch:s=.25,rot=-.25", as\_cmap\=True)

Copy to clipboard

![seaborn_cubehelix color map](<Base64-Image-Removed>)

Return a light sequential gradient:

sns.color\_palette("light:#5A9", as\_cmap\=True)

Copy to clipboard

![blend color map](<Base64-Image-Removed>)

Return a reversed dark sequential gradient:

sns.color\_palette("dark:#5A9\_r", as\_cmap\=True)

Copy to clipboard

![blend color map](<Base64-Image-Removed>)

Return a blend gradient between two endpoints:

sns.color\_palette("blend:#7AB,#EDA", as\_cmap\=True)

Copy to clipboard

![blend color map](<Base64-Image-Removed>)

Use as a context manager to change the default qualitative color palette:

with sns.color\_palette("Set3"):
    sns.relplot(x\=x, y\=y, hue\=hue, s\=500, legend\=False, height\=1.3, aspect\=4)

sns.relplot(x\=x, y\=y, hue\=hue, s\=500, legend\=False, height\=1.3, aspect\=4)

Copy to clipboard

![../_images/color_palette_23_0.png](https://seaborn.pydata.org/_images/color_palette_23_0.png) ![../_images/color_palette_23_1.png](https://seaborn.pydata.org/_images/color_palette_23_1.png)

See the underlying color values as hex codes:

print(sns.color\_palette("pastel6").as\_hex())

Copy to clipboard

\['#a1c9f4', '#8de5a1', '#ff9f9b', '#d0bbff', '#fffea3', '#b9f2f0'\]

Copy to clipboard