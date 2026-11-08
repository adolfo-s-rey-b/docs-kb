 

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
    

Grouped barplots[#](https://seaborn.pydata.org/examples/grouped_barplot.html#grouped-barplots "Permalink to this heading")

===========================================================================================================================

![../_images/grouped_barplot.png](https://seaborn.pydata.org/_images/grouped_barplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

penguins \= sns.load\_dataset("penguins")

\# Draw a nested barplot by species and sex
g \= sns.catplot(
    data\=penguins, kind\="bar",
    x\="species", y\="body\_mass\_g", hue\="sex",
    errorbar\="sd", palette\="dark", alpha\=.6, height\=6
)
g.despine(left\=True)
g.set\_axis\_labels("", "Body mass (g)")
g.legend.set\_title("")

Copy to clipboard