 

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

seaborn.cubehelix\_palette[#](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn-cubehelix-palette "Permalink to this heading")

=========================================================================================================================================================

seaborn.cubehelix\_palette(_n\_colors\=6_, _start\=0_, _rot\=0.4_, _gamma\=1.0_, _hue\=0.8_, _light\=0.85_, _dark\=0.15_, _reverse\=False_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "Permalink to this definition")

Make a sequential palette from the cubehelix system.

This produces a colormap with linearly-decreasing (or increasing) brightness. That means that information will be preserved if printed to black and white or viewed by someone who is colorblind. “cubehelix” is also available as a matplotlib-based palette, but this function gives the user more control over the look of the palette and has a different set of defaults.

In addition to using this function, it is also possible to generate a cubehelix palette generally in seaborn using a string starting with `ch:` and containing other parameters (e.g. `"ch:s=.25,r=-.5"`).

Parameters:

**n\_colors**int

Number of colors in the palette.

**start**float, 0 <= start <= 3

The hue value at the start of the helix.

**rot**float

Rotations around the hue wheel over the range of the palette.

**gamma**float 0 <= gamma

Nonlinearity to emphasize dark (gamma < 1) or light (gamma > 1) colors.

**hue**float, 0 <= hue <= 1

Saturation of the colors.

**dark**float 0 <= dark <= 1

Intensity of the darkest color in the palette.

**light**float 0 <= light <= 1

Intensity of the lightest color in the palette.

**reverse**bool

If True, the palette will go from dark to light.

**as\_cmap**bool

If True, return a [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")
.

Returns:

palette

list of RGB tuples or [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "(in Matplotlib v3.8.2)")

See also

[`choose_cubehelix_palette`](https://seaborn.pydata.org/generated/seaborn.choose_cubehelix_palette.html#seaborn.choose_cubehelix_palette "seaborn.choose_cubehelix_palette")

Launch an interactive widget to select cubehelix palette parameters.

[`dark_palette`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette")

Create a sequential palette with dark low values.

[`light_palette`](https://seaborn.pydata.org/generated/seaborn.light_palette.html#seaborn.light_palette "seaborn.light_palette")

Create a sequential palette with bright low values.

References

Green, D. A. (2011). “A colour scheme for the display of astronomical intensity images”. Bulletin of the Astromical Society of India, Vol. 39, p. 289-295.

Examples

Return a discrete palette with default parameters:

sns.cubehelix\_palette()

Copy to clipboard

Increase the number of colors:

sns.cubehelix\_palette(8)

Copy to clipboard

Return a continuous colormap rather than a discrete palette:

sns.cubehelix\_palette(as\_cmap\=True)

Copy to clipboard

![seaborn_cubehelix color map](<Base64-Image-Removed>)

Change the starting point of the helix:

sns.cubehelix\_palette(start\=2)

Copy to clipboard

Change the amount of rotation in the helix:

sns.cubehelix\_palette(rot\=.2)

Copy to clipboard

Rotate in the reverse direction:

sns.cubehelix\_palette(rot\=-.2)

Copy to clipboard

Apply a nonlinearity to the luminance ramp:

sns.cubehelix\_palette(gamma\=.5)

Copy to clipboard

Increase the saturation of the colors:

sns.cubehelix\_palette(hue\=1)

Copy to clipboard

Change the luminance at the start and end points:

sns.cubehelix\_palette(dark\=.25, light\=.75)

Copy to clipboard

Reverse the direction of the luminance ramp:

sns.cubehelix\_palette(reverse\=True)

Copy to clipboard