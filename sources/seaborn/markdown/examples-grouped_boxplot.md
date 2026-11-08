 

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
    

Grouped boxplots[#](https://seaborn.pydata.org/examples/grouped_boxplot.html#grouped-boxplots "Permalink to this heading")

===========================================================================================================================

![../_images/grouped_boxplot.png](https://seaborn.pydata.org/_images/grouped_boxplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import seaborn as sns
sns.set\_theme(style\="ticks", palette\="pastel")

\# Load the example tips dataset
tips \= sns.load\_dataset("tips")

\# Draw a nested boxplot to show bills by day and time
sns.boxplot(x\="day", y\="total\_bill",
            hue\="smoker", palette\=\["m", "g"\],
            data\=tips)
sns.despine(offset\=10, trim\=True)

Copy to clipboard