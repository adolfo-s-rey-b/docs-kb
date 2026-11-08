 

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
    

Small multiple time series[#](https://seaborn.pydata.org/examples/timeseries_facets.html#small-multiple-time-series "Permalink to this heading")

=================================================================================================================================================

![../_images/timeseries_facets.png](https://seaborn.pydata.org/_images/timeseries_facets.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")
, [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")

import seaborn as sns

sns.set\_theme(style\="dark")
flights \= sns.load\_dataset("flights")

\# Plot each year's time series in its own facet
g \= sns.relplot(
    data\=flights,
    x\="month", y\="passengers", col\="year", hue\="year",
    kind\="line", palette\="crest", linewidth\=4, zorder\=5,
    col\_wrap\=3, height\=2, aspect\=1.5, legend\=False,
)

\# Iterate over each subplot to customize further
for year, ax in g.axes\_dict.items():

    \# Add the title as an annotation within the plot
    ax.text(.8, .85, year, transform\=ax.transAxes, fontweight\="bold")

    \# Plot every year's time series in the background
    sns.lineplot(
        data\=flights, x\="month", y\="passengers", units\="year",
        estimator\=None, color\=".7", linewidth\=1, ax\=ax,
    )

\# Reduce the frequency of the x axis ticks
ax.set\_xticks(ax.get\_xticks()\[::2\])

\# Tweak the supporting aspects of the plot
g.set\_titles("")
g.set\_axis\_labels("", "Passengers")
g.tight\_layout()

Copy to clipboard