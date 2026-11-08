 

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

seaborn.despine[#](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn-despine "Permalink to this heading")

==========================================================================================================================

seaborn.despine(_fig\=None_, _ax\=None_, _top\=True_, _right\=True_, _left\=False_, _bottom\=False_, _offset\=None_, _trim\=False_)[#](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "Permalink to this definition")

Remove the top and right spines from plot(s).

figmatplotlib figure, optional

Figure to despine all axes of, defaults to the current figure.

axmatplotlib axes, optional

Specific axes object to despine. Ignored if fig is provided.

top, right, left, bottomboolean, optional

If True, remove that spine.

offsetint or dict, optional

Absolute distance, in points, spines should be moved away from the axes (negative values move spines inward). A single value applies to all spines; a dict can be used to set offset values per side.

trimbool, optional

If True, limit spines to the smallest and largest major tick on each non-despined axis.

Returns:

None