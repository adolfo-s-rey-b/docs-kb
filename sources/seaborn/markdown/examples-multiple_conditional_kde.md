 

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
    

Conditional kernel density estimate[#](https://seaborn.pydata.org/examples/multiple_conditional_kde.html#conditional-kernel-density-estimate "Permalink to this heading")

==========================================================================================================================================================================

![../_images/multiple_conditional_kde.png](https://seaborn.pydata.org/_images/multiple_conditional_kde.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Load the diamonds dataset
diamonds \= sns.load\_dataset("diamonds")

\# Plot the distribution of clarity ratings, conditional on carat
sns.displot(
    data\=diamonds,
    x\="carat", hue\="cut",
    kind\="kde", height\=6,
    multiple\="fill", clip\=(0, None),
    palette\="ch:rot=-.25,hue=1,light=.75",
)

Copy to clipboard