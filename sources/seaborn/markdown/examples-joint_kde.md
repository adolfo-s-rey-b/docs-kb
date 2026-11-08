 

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
    

Joint kernel density estimate[#](https://seaborn.pydata.org/examples/joint_kde.html#joint-kernel-density-estimate "Permalink to this heading")

===============================================================================================================================================

![../_images/joint_kde.png](https://seaborn.pydata.org/_images/joint_kde.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`jointplot()`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

import seaborn as sns
sns.set\_theme(style\="ticks")

\# Load the penguins dataset
penguins \= sns.load\_dataset("penguins")

\# Show the joint distribution using kernel density estimation
g \= sns.jointplot(
    data\=penguins,
    x\="bill\_length\_mm", y\="bill\_depth\_mm", hue\="species",
    kind\="kde",
)

Copy to clipboard