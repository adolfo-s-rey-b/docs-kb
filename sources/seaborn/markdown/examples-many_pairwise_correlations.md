 

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
    

Plotting a diagonal correlation matrix[#](https://seaborn.pydata.org/examples/many_pairwise_correlations.html#plotting-a-diagonal-correlation-matrix "Permalink to this heading")

==================================================================================================================================================================================

![../_images/many_pairwise_correlations.png](https://seaborn.pydata.org/_images/many_pairwise_correlations.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`diverging_palette()`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html#seaborn.diverging_palette "seaborn.diverging_palette")
, [`heatmap()`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")

from string import ascii\_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set\_theme(style\="white")

\# Generate a large random dataset
rs \= np.random.RandomState(33)
d \= pd.DataFrame(data\=rs.normal(size\=(100, 26)),
                 columns\=list(ascii\_letters\[26:\]))

\# Compute the correlation matrix
corr \= d.corr()

\# Generate a mask for the upper triangle
mask \= np.triu(np.ones\_like(corr, dtype\=bool))

\# Set up the matplotlib figure
f, ax \= plt.subplots(figsize\=(11, 9))

\# Generate a custom diverging colormap
cmap \= sns.diverging\_palette(230, 20, as\_cmap\=True)

\# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask\=mask, cmap\=cmap, vmax\=.3, center\=0,
            square\=True, linewidths\=.5, cbar\_kws\={"shrink": .5})

Copy to clipboard