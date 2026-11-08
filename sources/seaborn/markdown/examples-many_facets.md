 

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
    

Plotting on a large number of facets[#](https://seaborn.pydata.org/examples/many_facets.html#plotting-on-a-large-number-of-facets "Permalink to this heading")

===============================================================================================================================================================

![../_images/many_facets.png](https://seaborn.pydata.org/_images/many_facets.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set\_theme(style\="ticks")

\# Create a dataset with many short random walks
rs \= np.random.RandomState(4)
pos \= rs.randint(\-1, 2, (20, 5)).cumsum(axis\=1)
pos \-= pos\[:, 0, np.newaxis\]
step \= np.tile(range(5), 20)
walk \= np.repeat(range(20), 5)
df \= pd.DataFrame(np.c\_\[pos.flat, step, walk\],
                  columns\=\["position", "step", "walk"\])

\# Initialize a grid of plots with an Axes for each walk
grid \= sns.FacetGrid(df, col\="walk", hue\="walk", palette\="tab20c",
                     col\_wrap\=4, height\=1.5)

\# Draw a horizontal line to show the starting point
grid.refline(y\=0, linestyle\=":")

\# Draw a line plot to show the trajectory of each random walk
grid.map(plt.plot, "step", "position", marker\="o")

\# Adjust the tick positions and labels
grid.set(xticks\=np.arange(5), yticks\=\[\-3, 3\],
         xlim\=(\-.5, 4.5), ylim\=(\-3.5, 3.5))

\# Adjust the arrangement of the plots
grid.fig.tight\_layout(w\_pad\=1)

Copy to clipboard