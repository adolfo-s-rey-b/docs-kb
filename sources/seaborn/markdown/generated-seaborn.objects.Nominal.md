 

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

seaborn.objects.Nominal[#](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn-objects-nominal "Permalink to this heading")

==================================================================================================================================================

_class_ seaborn.objects.Nominal(_values\=None_, _order\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal "Permalink to this definition")

A categorical scale without relative importance / magnitude.

tick(_locator\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal.tick "Permalink to this definition")

Configure the selection of ticks for the scale’s axis or legend.

Note

This API is under construction and will be enhanced over time. At the moment, it is probably not very useful.

Parameters:

**locator**[`matplotlib.ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "(in Matplotlib v3.8.2)")
 subclass

Pre-configured matplotlib locator; other parameters will not be used.

Returns:

Copy of self with new tick configuration.

label(_formatter\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Nominal.html#seaborn.objects.Nominal.label "Permalink to this definition")

Configure the selection of labels for the scale’s axis or legend.

Note

This API is under construction and will be enhanced over time. At the moment, it is probably not very useful.

Parameters:

**formatter**[`matplotlib.ticker.Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "(in Matplotlib v3.8.2)")
 subclass

Pre-configured matplotlib formatter; other parameters will not be used.

Returns:

scale

Copy of self with new tick configuration.