 

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
    

Scatterplot with varying point sizes and hues[#](https://seaborn.pydata.org/examples/scatter_bubbles.html#scatterplot-with-varying-point-sizes-and-hues "Permalink to this heading")

=====================================================================================================================================================================================

![../_images/scatter_bubbles.png](https://seaborn.pydata.org/_images/scatter_bubbles.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")

import seaborn as sns
sns.set\_theme(style\="white")

\# Load the example mpg dataset
mpg \= sns.load\_dataset("mpg")

\# Plot miles per gallon against horsepower with other semantics
sns.relplot(x\="horsepower", y\="mpg", hue\="origin", size\="weight",
            sizes\=(40, 400), alpha\=.5, palette\="muted",
            height\=6, data\=mpg)

Copy to clipboard