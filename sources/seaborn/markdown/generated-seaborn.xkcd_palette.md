 

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

seaborn.xkcd\_palette[#](https://seaborn.pydata.org/generated/seaborn.xkcd_palette.html#seaborn-xkcd-palette "Permalink to this heading")

==========================================================================================================================================

seaborn.xkcd\_palette(_colors_)[#](https://seaborn.pydata.org/generated/seaborn.xkcd_palette.html#seaborn.xkcd_palette "Permalink to this definition")

Make a palette with color names from the xkcd color survey.

See xkcd for the full list of colors: [https://xkcd.com/color/rgb/](https://xkcd.com/color/rgb/)

This is just a simple wrapper around the `seaborn.xkcd_rgb` dictionary.

Parameters:

**colors**list of strings

List of keys in the `seaborn.xkcd_rgb` dictionary.

Returns:

palette

A list of colors as RGB tuples.

See also

[`crayon_palette`](https://seaborn.pydata.org/generated/seaborn.crayon_palette.html#seaborn.crayon_palette "seaborn.crayon_palette")

Make a palette with Crayola crayon colors.