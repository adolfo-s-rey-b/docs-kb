 

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
    

Paired categorical plots[#](https://seaborn.pydata.org/examples/paired_pointplots.html#paired-categorical-plots "Permalink to this heading")

=============================================================================================================================================

![../_images/paired_pointplots.png](https://seaborn.pydata.org/_images/paired_pointplots.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Load the example Titanic dataset
titanic \= sns.load\_dataset("titanic")

\# Set up a grid to plot survival probability against several variables
g \= sns.PairGrid(titanic, y\_vars\="survived",
                 x\_vars\=\["class", "sex", "who", "alone"\],
                 height\=5, aspect\=.5)

\# Draw a seaborn pointplot onto each Axes
g.map(sns.pointplot, color\="xkcd:plum")
g.set(ylim\=(0, 1))
sns.despine(fig\=g.fig, left\=True)

Copy to clipboard