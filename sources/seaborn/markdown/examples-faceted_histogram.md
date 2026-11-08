 

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
    

Facetting histograms by subsets of data[#](https://seaborn.pydata.org/examples/faceted_histogram.html#facetting-histograms-by-subsets-of-data "Permalink to this heading")

===========================================================================================================================================================================

![../_images/faceted_histogram.png](https://seaborn.pydata.org/_images/faceted_histogram.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

import seaborn as sns

sns.set\_theme(style\="darkgrid")
df \= sns.load\_dataset("penguins")
sns.displot(
    df, x\="flipper\_length\_mm", col\="species", row\="sex",
    binwidth\=3, height\=3, facet\_kws\=dict(margin\_titles\=True),
)

Copy to clipboard