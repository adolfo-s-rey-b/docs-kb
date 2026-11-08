 

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
    

Conditional means with observations[#](https://seaborn.pydata.org/examples/jitter_stripplot.html#conditional-means-with-observations "Permalink to this heading")

==================================================================================================================================================================

![../_images/jitter_stripplot.png](https://seaborn.pydata.org/_images/jitter_stripplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")
, [`stripplot()`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")
, [`pointplot()`](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot "seaborn.pointplot")
, [`move_legend()`](https://seaborn.pydata.org/generated/seaborn.move_legend.html#seaborn.move_legend "seaborn.move_legend")

import seaborn as sns
import matplotlib.pyplot as plt

sns.set\_theme(style\="whitegrid")
iris \= sns.load\_dataset("iris")

\# "Melt" the dataset to "long-form" or "tidy" representation
iris \= iris.melt(id\_vars\="species", var\_name\="measurement")

\# Initialize the figure
f, ax \= plt.subplots()
sns.despine(bottom\=True, left\=True)

\# Show each observation with a scatterplot
sns.stripplot(
    data\=iris, x\="value", y\="measurement", hue\="species",
    dodge\=True, alpha\=.25, zorder\=1, legend\=False,
)

\# Show the conditional means, aligning each pointplot in the
\# center of the strips by adjusting the width allotted to each
\# category (.8 by default) by the number of hue levels
sns.pointplot(
    data\=iris, x\="value", y\="measurement", hue\="species",
    dodge\=.8 \- .8 / 3, palette\="dark", errorbar\=None,
    markers\="d", markersize\=4, linestyle\="none",
)

\# Improve the legend
sns.move\_legend(
    ax, loc\="lower right", ncol\=3, frameon\=True, columnspacing\=1, handletextpad\=0,
)

Copy to clipboard