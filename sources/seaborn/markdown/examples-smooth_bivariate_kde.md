 

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
    

Smooth kernel density with marginal histograms[#](https://seaborn.pydata.org/examples/smooth_bivariate_kde.html#smooth-kernel-density-with-marginal-histograms "Permalink to this heading")

============================================================================================================================================================================================

![../_images/smooth_bivariate_kde.png](https://seaborn.pydata.org/_images/smooth_bivariate_kde.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")

import seaborn as sns
sns.set\_theme(style\="white")

df \= sns.load\_dataset("penguins")

g \= sns.JointGrid(data\=df, x\="body\_mass\_g", y\="bill\_depth\_mm", space\=0)
g.plot\_joint(sns.kdeplot,
             fill\=True, clip\=((2200, 6800), (10, 25)),
             thresh\=0, levels\=100, cmap\="rocket")
g.plot\_marginals(sns.histplot, color\="#03051A", alpha\=1, bins\=25)

Copy to clipboard