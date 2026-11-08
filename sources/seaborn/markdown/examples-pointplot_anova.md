 

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
    

Plotting a three-way ANOVA[#](https://seaborn.pydata.org/examples/pointplot_anova.html#plotting-a-three-way-anova "Permalink to this heading")

===============================================================================================================================================

![../_images/pointplot_anova.png](https://seaborn.pydata.org/_images/pointplot_anova.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Load the example exercise dataset
exercise \= sns.load\_dataset("exercise")

\# Draw a pointplot to show pulse as a function of three categorical factors
g \= sns.catplot(
    data\=exercise, x\="time", y\="pulse", hue\="kind", col\="diet",
    capsize\=.2, palette\="YlGnBu\_d", errorbar\="se",
    kind\="point", height\=6, aspect\=.75,
)
g.despine(left\=True)

Copy to clipboard