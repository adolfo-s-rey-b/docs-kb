 

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
    

Scatterplot with continuous hues and sizes[#](https://seaborn.pydata.org/examples/scatterplot_sizes.html#scatterplot-with-continuous-hues-and-sizes "Permalink to this heading")

=================================================================================================================================================================================

![../_images/scatterplot_sizes.png](https://seaborn.pydata.org/_images/scatterplot_sizes.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`cubehelix_palette()`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette")
, [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Load the example planets dataset
planets \= sns.load\_dataset("planets")

cmap \= sns.cubehelix\_palette(rot\=-.2, as\_cmap\=True)
g \= sns.relplot(
    data\=planets,
    x\="distance", y\="orbital\_period",
    hue\="year", size\="mass",
    palette\=cmap, sizes\=(10, 200),
)
g.set(xscale\="log", yscale\="log")
g.ax.xaxis.grid(True, "minor", linewidth\=.25)
g.ax.yaxis.grid(True, "minor", linewidth\=.25)
g.despine(left\=True, bottom\=True)

Copy to clipboard