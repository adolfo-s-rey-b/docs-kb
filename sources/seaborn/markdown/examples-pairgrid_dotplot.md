 

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
    

Dot plot with several variables[#](https://seaborn.pydata.org/examples/pairgrid_dotplot.html#dot-plot-with-several-variables "Permalink to this heading")

==========================================================================================================================================================

![../_images/pairgrid_dotplot.png](https://seaborn.pydata.org/_images/pairgrid_dotplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Load the dataset
crashes \= sns.load\_dataset("car\_crashes")

\# Make the PairGrid
g \= sns.PairGrid(crashes.sort\_values("total", ascending\=False),
                 x\_vars\=crashes.columns\[:\-3\], y\_vars\=\["abbrev"\],
                 height\=10, aspect\=.25)

\# Draw a dot plot using the stripplot function
g.map(sns.stripplot, size\=10, orient\="h", jitter\=False,
      palette\="flare\_r", linewidth\=1, edgecolor\="w")

\# Use the same x axis limits on all columns and add better labels
g.set(xlim\=(0, 25), xlabel\="Crashes", ylabel\="")

\# Use semantically meaningful titles for the columns
titles \= \["Total crashes", "Speeding crashes", "Alcohol crashes",\
          "Not distracted crashes", "No previous crashes"\]

for ax, title in zip(g.axes.flat, titles):

    \# Set a different title for each axes
    ax.set(title\=title)

    \# Make the grid horizontal instead of vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left\=True, bottom\=True)

Copy to clipboard