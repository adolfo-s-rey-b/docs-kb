 

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
    

Multiple linear regression[#](https://seaborn.pydata.org/examples/multiple_regression.html#multiple-linear-regression "Permalink to this heading")

===================================================================================================================================================

![../_images/multiple_regression.png](https://seaborn.pydata.org/_images/multiple_regression.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot")

import seaborn as sns
sns.set\_theme()

\# Load the penguins dataset
penguins \= sns.load\_dataset("penguins")

\# Plot sepal width as a function of sepal\_length across days
g \= sns.lmplot(
    data\=penguins,
    x\="bill\_length\_mm", y\="bill\_depth\_mm", hue\="species",
    height\=5
)

\# Use more informative axis labels than are provided by default
g.set\_axis\_labels("Snoot length (mm)", "Snoot depth (mm)")

Copy to clipboard