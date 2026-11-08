 

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

seaborn.choose\_dark\_palette[#](https://seaborn.pydata.org/generated/seaborn.choose_dark_palette.html#seaborn-choose-dark-palette "Permalink to this heading")

================================================================================================================================================================

seaborn.choose\_dark\_palette(_input\='husl'_, _as\_cmap\=False_)[#](https://seaborn.pydata.org/generated/seaborn.choose_dark_palette.html#seaborn.choose_dark_palette "Permalink to this definition")

Launch an interactive widget to create a dark sequential palette.

This corresponds with the [`dark_palette()`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette")
 function. This kind of palette is good for data that range between relatively uninteresting low values and interesting high values.

Requires IPython 2+ and must be used in the notebook.

Parameters:

**input**{‘husl’, ‘hls’, ‘rgb’}

Color space for defining the seed value. Note that the default is different than the default input for [`dark_palette()`](https://seaborn.pydata.org/generated/seaborn.dark_palette.html#seaborn.dark_palette "seaborn.dark_palette")
.

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

[`cubehelix_palette`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette")

Create a sequential palette or colormap using the cubehelix system.