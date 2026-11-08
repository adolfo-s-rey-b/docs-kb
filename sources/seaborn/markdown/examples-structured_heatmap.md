 

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
    

Discovering structure in heatmap data[#](https://seaborn.pydata.org/examples/structured_heatmap.html#discovering-structure-in-heatmap-data "Permalink to this heading")

========================================================================================================================================================================

![../_images/structured_heatmap.png](https://seaborn.pydata.org/_images/structured_heatmap.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`husl_palette()`](https://seaborn.pydata.org/generated/seaborn.husl_palette.html#seaborn.husl_palette "seaborn.husl_palette")
, [`clustermap()`](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap "seaborn.clustermap")

import pandas as pd
import seaborn as sns
sns.set\_theme()

\# Load the brain networks example dataset
df \= sns.load\_dataset("brain\_networks", header\=\[0, 1, 2\], index\_col\=0)

\# Select a subset of the networks
used\_networks \= \[1, 5, 6, 7, 8, 12, 13, 17\]
used\_columns \= (df.columns.get\_level\_values("network")
                          .astype(int)
                          .isin(used\_networks))
df \= df.loc\[:, used\_columns\]

\# Create a categorical palette to identify the networks
network\_pal \= sns.husl\_palette(8, s\=.45)
network\_lut \= dict(zip(map(str, used\_networks), network\_pal))

\# Convert the palette to vectors that will be drawn on the side of the matrix
networks \= df.columns.get\_level\_values("network")
network\_colors \= pd.Series(networks, index\=df.columns).map(network\_lut)

\# Draw the full plot
g \= sns.clustermap(df.corr(), center\=0, cmap\="vlag",
                   row\_colors\=network\_colors, col\_colors\=network\_colors,
                   dendrogram\_ratio\=(.1, .2),
                   cbar\_pos\=(.02, .32, .03, .2),
                   linewidths\=.75, figsize\=(12, 13))

g.ax\_row\_dendrogram.remove()

Copy to clipboard