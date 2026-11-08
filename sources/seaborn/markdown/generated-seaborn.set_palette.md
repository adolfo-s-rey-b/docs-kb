 

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

seaborn.set\_palette[#](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn-set-palette "Permalink to this heading")

=======================================================================================================================================

seaborn.set\_palette(_palette_, _n\_colors\=None_, _desat\=None_, _color\_codes\=False_)[#](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette "Permalink to this definition")

Set the matplotlib color cycle using a seaborn palette.

Parameters:

**palette**seaborn color palette | matplotlib colormap | hls | husl

Palette definition. Should be something [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
 can process.

**n\_colors**int

Number of colors in the cycle. The default number of colors will depend on the format of `palette`, see the [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
 documentation for more information.

**desat**float

Proportion to desaturate each color by.

**color\_codes**bool

If `True` and `palette` is a seaborn palette, remap the shorthand color codes (e.g. “b”, “g”, “r”, etc.) to the colors from this palette.

See also

[`color_palette`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")

build a color palette or set the color cycle temporarily in a `with` statement.

[`set_context`](https://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context "seaborn.set_context")

set parameters to scale plot elements

[`set_style`](https://seaborn.pydata.org/generated/seaborn.set_style.html#seaborn.set_style "seaborn.set_style")

set the default parameters for figure style