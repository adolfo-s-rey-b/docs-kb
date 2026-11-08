 

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
    

Horizontal boxplot with observations[#](https://seaborn.pydata.org/examples/horizontal_boxplot.html#horizontal-boxplot-with-observations "Permalink to this heading")

======================================================================================================================================================================

![../_images/horizontal_boxplot.png](https://seaborn.pydata.org/_images/horizontal_boxplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`boxplot()`](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")
, [`stripplot()`](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import seaborn as sns
import matplotlib.pyplot as plt

sns.set\_theme(style\="ticks")

\# Initialize the figure with a logarithmic x axis
f, ax \= plt.subplots(figsize\=(7, 6))
ax.set\_xscale("log")

\# Load the example planets dataset
planets \= sns.load\_dataset("planets")

\# Plot the orbital period with horizontal boxes
sns.boxplot(
    planets, x\="distance", y\="method", hue\="method",
    whis\=\[0, 100\], width\=.6, palette\="vlag"
)

\# Add in points to show each observation
sns.stripplot(planets, x\="distance", y\="method", size\=4, color\=".3")

\# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel\="")
sns.despine(trim\=True, left\=True)

Copy to clipboard