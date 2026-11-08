 

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
    

Paired density and scatterplot matrix[#](https://seaborn.pydata.org/examples/pair_grid_with_kde.html#paired-density-and-scatterplot-matrix "Permalink to this heading")

========================================================================================================================================================================

![../_images/pair_grid_with_kde.png](https://seaborn.pydata.org/_images/pair_grid_with_kde.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid "seaborn.PairGrid")

import seaborn as sns
sns.set\_theme(style\="white")

df \= sns.load\_dataset("penguins")

g \= sns.PairGrid(df, diag\_sharey\=False)
g.map\_upper(sns.scatterplot, s\=15)
g.map\_lower(sns.kdeplot)
g.map\_diag(sns.kdeplot, lw\=2)

Copy to clipboard