 

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

seaborn.set\_color\_codes[#](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn-set-color-codes "Permalink to this heading")

====================================================================================================================================================

seaborn.set\_color\_codes(_palette\='deep'_)[#](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn.set_color_codes "Permalink to this definition")

Change how matplotlib color shorthands are interpreted.

Calling this will change how shorthand codes like “b” or “g” are interpreted by matplotlib in subsequent plots.

Parameters:

**palette**{deep, muted, pastel, dark, bright, colorblind}

Named seaborn palette to use as the source of colors.

See also

[`set`](https://seaborn.pydata.org/generated/seaborn.set.html#seaborn.set "seaborn.set")

Color codes can be set through the high-level seaborn style manager.

[`set_palette`](https://seaborn.pydata.org/generated/seaborn.set_palette.html#seaborn.set_palette "seaborn.set_palette")

Color codes can also be set through the function that sets the matplotlib color cycle.