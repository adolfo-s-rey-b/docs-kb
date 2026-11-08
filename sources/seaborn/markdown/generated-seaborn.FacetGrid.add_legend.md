 

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

seaborn.FacetGrid.add\_legend[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.add_legend.html#seaborn-facetgrid-add-legend "Permalink to this heading")

==================================================================================================================================================================

FacetGrid.add\_legend(_legend\_data\=None_, _title\=None_, _label\_order\=None_, _adjust\_subtitles\=False_, _\*\*kwargs_)[#](https://seaborn.pydata.org/generated/seaborn.FacetGrid.add_legend.html#seaborn.FacetGrid.add_legend "Permalink to this definition")

Draw a legend, maybe placing it outside axes and resizing the figure.

Parameters:

**legend\_data**dict

Dictionary mapping label names (or two-element tuples where the second element is a label name) to matplotlib artist handles. The default reads from `self._legend_data`.

**title**string

Title for the legend. The default reads from `self._hue_var`.

**label\_order**list of labels

The order that the legend entries should appear in. The default reads from `self.hue_names`.

**adjust\_subtitles**bool

If True, modify entries with invisible artists to left-align the labels and set the font size to that of a title.

**kwargs**key, value pairings

Other keyword arguments are passed to the underlying legend methods on the Figure or Axes object.

Returns:

**self**Grid instance

Returns self for easy chaining.