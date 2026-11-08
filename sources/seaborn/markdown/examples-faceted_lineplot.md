 

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
    

Line plots on multiple facets[#](https://seaborn.pydata.org/examples/faceted_lineplot.html#line-plots-on-multiple-facets "Permalink to this heading")

======================================================================================================================================================

![../_images/faceted_lineplot.png](https://seaborn.pydata.org/_images/faceted_lineplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`color_palette()`](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
, [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")

import seaborn as sns
sns.set\_theme(style\="ticks")

dots \= sns.load\_dataset("dots")

\# Define the palette as a list to specify exact values
palette \= sns.color\_palette("rocket\_r")

\# Plot the lines on two facets
sns.relplot(
    data\=dots,
    x\="time", y\="firing\_rate",
    hue\="coherence", size\="choice", col\="align",
    kind\="line", size\_order\=\["T1", "T2"\], palette\=palette,
    height\=5, aspect\=.75, facet\_kws\=dict(sharex\=False),
)

Copy to clipboard