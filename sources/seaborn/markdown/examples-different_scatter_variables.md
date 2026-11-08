 

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
    

Scatterplot with multiple semantics[#](https://seaborn.pydata.org/examples/different_scatter_variables.html#scatterplot-with-multiple-semantics "Permalink to this heading")

=============================================================================================================================================================================

![../_images/different_scatter_variables.png](https://seaborn.pydata.org/_images/different_scatter_variables.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")
, [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")

import seaborn as sns
import matplotlib.pyplot as plt
sns.set\_theme(style\="whitegrid")

\# Load the example diamonds dataset
diamonds \= sns.load\_dataset("diamonds")

\# Draw a scatter plot while assigning point colors and sizes to different
\# variables in the dataset
f, ax \= plt.subplots(figsize\=(6.5, 6.5))
sns.despine(f, left\=True, bottom\=True)
clarity\_ranking \= \["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"\]
sns.scatterplot(x\="carat", y\="price",
                hue\="clarity", size\="depth",
                palette\="ch:r=-.2,d=.3\_r",
                hue\_order\=clarity\_ranking,
                sizes\=(1, 8), linewidth\=0,
                data\=diamonds, ax\=ax)

Copy to clipboard