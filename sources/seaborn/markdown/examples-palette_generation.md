 

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
    

Different cubehelix palettes[#](https://seaborn.pydata.org/examples/palette_generation.html#different-cubehelix-palettes "Permalink to this heading")

======================================================================================================================================================

![../_images/palette_generation.png](https://seaborn.pydata.org/_images/palette_generation.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`cubehelix_palette()`](https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette "seaborn.cubehelix_palette")
, [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set\_theme(style\="white")
rs \= np.random.RandomState(50)

\# Set up the matplotlib figure
f, axes \= plt.subplots(3, 3, figsize\=(9, 9), sharex\=True, sharey\=True)

\# Rotate the starting point around the cubehelix hue circle
for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):

    \# Create a cubehelix colormap to use with kdeplot
    cmap \= sns.cubehelix\_palette(start\=s, light\=1, as\_cmap\=True)

    \# Generate and plot a random bivariate dataset
    x, y \= rs.normal(size\=(2, 50))
    sns.kdeplot(
        x\=x, y\=y,
        cmap\=cmap, fill\=True,
        clip\=(\-5, 5), cut\=10,
        thresh\=0, levels\=15,
        ax\=ax,
    )
    ax.set\_axis\_off()

ax.set(xlim\=(\-3.5, 3.5), ylim\=(\-3.5, 3.5))
f.subplots\_adjust(0, 0, 1, 1, .08, .08)

Copy to clipboard