 

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

seaborn.objects.Continuous[#](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn-objects-continuous "Permalink to this heading")

===========================================================================================================================================================

_class_ seaborn.objects.Continuous(_values\=None_, _norm\=None_, _trans\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous "Permalink to this definition")

A numeric scale supporting norms and functional transforms.

tick(_locator\=None_, _\*_, _at\=None_, _upto\=None_, _count\=None_, _every\=None_, _between\=None_, _minor\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous.tick "Permalink to this definition")

Configure the selection of ticks for the scale’s axis or legend.

Parameters:

**locator**[`matplotlib.ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "(in Matplotlib v3.8.2)")
 subclass

Pre-configured matplotlib locator; other parameters will not be used.

**at**sequence of floats

Place ticks at these specific locations (in data units).

**upto**int

Choose “nice” locations for ticks, but do not exceed this number.

**count**int

Choose exactly this number of ticks, bounded by `between` or axis limits.

**every**float

Choose locations at this interval of separation (in data units).

**between**pair of floats

Bound upper / lower ticks when using `every` or `count`.

**minor**int

Number of unlabeled ticks to draw between labeled “major” ticks.

Returns:

scale

Copy of self with new tick configuration.

label(_formatter=None_, _\*_, _like=None_, _base=<default>_, _unit=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Continuous.html#seaborn.objects.Continuous.label "Permalink to this definition")

Configure the appearance of tick labels for the scale’s axis or legend.

Parameters:

**formatter**[`matplotlib.ticker.Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "(in Matplotlib v3.8.2)")
 subclass

Pre-configured formatter to use; other parameters will be ignored.

**like**str or callable

Either a format pattern (e.g., `".2f"`), a format string with fields named `x` and/or `pos` (e.g., `"${x:.2f}"`), or a callable with a signature like `f(x: float, pos: int) -> str`. In the latter variants, `x` is passed as the tick value and `pos` is passed as the tick index.

**base**number

Use log formatter (with scientific notation) having this value as the base. Set to `None` to override the default formatter with a log transform.

**unit**str or (str, str) tuple

Use SI prefixes with these units (e.g., with `unit="g"`, a tick value of 5000 will appear as `5 kg`). When a tuple, the first element gives the separator between the number and unit.

Returns:

scale

Copy of self with new label configuration.