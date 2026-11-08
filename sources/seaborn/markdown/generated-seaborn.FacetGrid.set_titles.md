 

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

seaborn.FacetGrid.set\_titles[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_titles.html#seaborn-facetgrid-set-titles "Permalink to this heading")

==================================================================================================================================================================

FacetGrid.set\_titles(_template\=None_, _row\_template\=None_, _col\_template\=None_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_titles.html#seaborn.FacetGrid.set_titles "Permalink to this definition")

Draw titles either above each facet or on the grid margins.

Parameters:

**template**string

Template for all titles with the formatting keys {col\_var} and {col\_name} (if using a `col` faceting variable) and/or {row\_var} and {row\_name} (if using a `row` faceting variable).

**row\_template:**

Template for the row variable when titles are drawn on the grid margins. Must have {row\_var} and {row\_name} formatting keys.

**col\_template:**

Template for the column variable when titles are drawn on the grid margins. Must have {col\_var} and {col\_name} formatting keys.

Returns:

self: object

Returns self.