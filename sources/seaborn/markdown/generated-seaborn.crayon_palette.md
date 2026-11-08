 

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

seaborn.crayon\_palette[#](https://seaborn.pydata.org/generated/seaborn.crayon_palette.html#seaborn-crayon-palette "Permalink to this heading")

================================================================================================================================================

seaborn.crayon\_palette(_colors_)[#](https://seaborn.pydata.org/generated/seaborn.crayon_palette.html#seaborn.crayon_palette "Permalink to this definition")

Make a palette with color names from Crayola crayons.

Colors are taken from here: [https://en.wikipedia.org/wiki/List\_of\_Crayola\_crayon\_colors](https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors)

This is just a simple wrapper around the `seaborn.crayons` dictionary.

Parameters:

**colors**list of strings

List of keys in the `seaborn.crayons` dictionary.

Returns:

palette

A list of colors as RGB tuples.

See also

[`xkcd_palette`](https://seaborn.pydata.org/generated/seaborn.xkcd_palette.html#seaborn.xkcd_palette "seaborn.xkcd_palette")

Make a palette with named colors from the XKCD color survey.