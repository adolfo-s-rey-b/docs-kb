 

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
    

Overlapping densities (‘ridge plot’)[#](https://seaborn.pydata.org/examples/kde_ridgeplot.html#overlapping-densities-ridge-plot "Permalink to this heading")

=============================================================================================================================================================

![../_images/kde_ridgeplot.png](https://seaborn.pydata.org/_images/kde_ridgeplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`cubehelix_palette()`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette")
, [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set\_theme(style\="white", rc\={"axes.facecolor": (0, 0, 0, 0)})

\# Create the data
rs \= np.random.RandomState(1979)
x \= rs.randn(500)
g \= np.tile(list("ABCDEFGHIJ"), 50)
df \= pd.DataFrame(dict(x\=x, g\=g))
m \= df.g.map(ord)
df\["x"\] += m

\# Initialize the FacetGrid object
pal \= sns.cubehelix\_palette(10, rot\=-.25, light\=.7)
g \= sns.FacetGrid(df, row\="g", hue\="g", aspect\=15, height\=.5, palette\=pal)

\# Draw the densities in a few steps
g.map(sns.kdeplot, "x",
      bw\_adjust\=.5, clip\_on\=False,
      fill\=True, alpha\=1, linewidth\=1.5)
g.map(sns.kdeplot, "x", clip\_on\=False, color\="w", lw\=2, bw\_adjust\=.5)

\# passing color=None to refline() uses the hue mapping
g.refline(y\=0, linewidth\=2, linestyle\="-", color\=None, clip\_on\=False)

\# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax \= plt.gca()
    ax.text(0, .2, label, fontweight\="bold", color\=color,
            ha\="left", va\="center", transform\=ax.transAxes)

g.map(label, "x")

\# Set the subplots to overlap
g.figure.subplots\_adjust(hspace\=-.25)

\# Remove axes details that don't play well with overlap
g.set\_titles("")
g.set(yticks\=\[\], ylabel\="")
g.despine(bottom\=True, left\=True)

Copy to clipboard