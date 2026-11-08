 

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
    

Grouped violinplots with split violins[#](https://seaborn.pydata.org/examples/grouped_violinplots.html#grouped-violinplots-with-split-violins "Permalink to this heading")

===========================================================================================================================================================================

![../_images/grouped_violinplots.png](https://seaborn.pydata.org/_images/grouped_violinplots.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")

import seaborn as sns
sns.set\_theme(style\="dark")

\# Load the example tips dataset
tips \= sns.load\_dataset("tips")

\# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(data\=tips, x\="day", y\="total\_bill", hue\="smoker",
               split\=True, inner\="quart", fill\=False,
               palette\={"Yes": "g", "No": ".35"})

Copy to clipboard