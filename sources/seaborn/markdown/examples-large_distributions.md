 

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
    

Plotting large distributions[#](https://seaborn.pydata.org/examples/large_distributions.html#plotting-large-distributions "Permalink to this heading")

=======================================================================================================================================================

![../_images/large_distributions.png](https://seaborn.pydata.org/_images/large_distributions.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`boxenplot()`](https://seaborn.pydata.org/generated/seaborn.boxenplot.html#seaborn.boxenplot "seaborn.boxenplot")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

diamonds \= sns.load\_dataset("diamonds")
clarity\_ranking \= \["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"\]

sns.boxenplot(
    diamonds, x\="clarity", y\="carat",
    color\="b", order\=clarity\_ranking, width\_method\="linear",
)

Copy to clipboard