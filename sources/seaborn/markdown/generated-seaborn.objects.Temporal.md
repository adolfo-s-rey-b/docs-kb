 

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

seaborn.objects.Temporal[#](https://seaborn.pydata.org/generated/seaborn.objects.Temporal.html#seaborn-objects-temporal "Permalink to this heading")

=====================================================================================================================================================

_class_ seaborn.objects.Temporal(_values\=None_, _norm\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Temporal.html#seaborn.objects.Temporal "Permalink to this definition")

A scale for date/time data.

tick(_locator\=None_, _\*_, _upto\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Temporal.html#seaborn.objects.Temporal.tick "Permalink to this definition")

Configure the selection of ticks for the scale’s axis or legend.

Note

This API is under construction and will be enhanced over time.

Parameters:

**locator**[`matplotlib.ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "(in Matplotlib v3.8.2)")
 subclass

Pre-configured matplotlib locator; other parameters will not be used.

**upto**int

Choose “nice” locations for ticks, but do not exceed this number.

Returns:

scale

Copy of self with new tick configuration.

label(_formatter\=None_, _\*_, _concise\=False_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Temporal.html#seaborn.objects.Temporal.label "Permalink to this definition")

Configure the appearance of tick labels for the scale’s axis or legend.

Note

This API is under construction and will be enhanced over time.

Parameters:

**formatter**[`matplotlib.ticker.Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "(in Matplotlib v3.8.2)")
 subclass

Pre-configured formatter to use; other parameters will be ignored.

**concise**bool

If True, use [`matplotlib.dates.ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "(in Matplotlib v3.8.2)")
 to make the tick labels as compact as possible.

Returns:

scale

Copy of self with new label configuration.