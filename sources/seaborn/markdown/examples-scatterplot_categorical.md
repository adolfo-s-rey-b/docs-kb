 

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
    

Scatterplot with categorical variables[#](https://seaborn.pydata.org/examples/scatterplot_categorical.html#scatterplot-with-categorical-variables "Permalink to this heading")

===============================================================================================================================================================================

![../_images/scatterplot_categorical.png](https://seaborn.pydata.org/_images/scatterplot_categorical.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`swarmplot()`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html#seaborn.swarmplot "seaborn.swarmplot")

import seaborn as sns
sns.set\_theme(style\="whitegrid", palette\="muted")

\# Load the penguins dataset
df \= sns.load\_dataset("penguins")

\# Draw a categorical scatterplot to show each observation
ax \= sns.swarmplot(data\=df, x\="body\_mass\_g", y\="sex", hue\="species")
ax.set(ylabel\="")

Copy to clipboard