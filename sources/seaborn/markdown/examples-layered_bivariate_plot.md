 

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
    

Bivariate plot with multiple elements[#](https://seaborn.pydata.org/examples/layered_bivariate_plot.html#bivariate-plot-with-multiple-elements "Permalink to this heading")

============================================================================================================================================================================

![../_images/layered_bivariate_plot.png](https://seaborn.pydata.org/_images/layered_bivariate_plot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`scatterplot()`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
, [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")
, [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set\_theme(style\="dark")

\# Simulate data from a bivariate Gaussian
n \= 10000
mean \= \[0, 0\]
cov \= \[(2, .4), (.4, .2)\]
rng \= np.random.RandomState(0)
x, y \= rng.multivariate\_normal(mean, cov, n).T

\# Draw a combo histogram and scatterplot with density contours
f, ax \= plt.subplots(figsize\=(6, 6))
sns.scatterplot(x\=x, y\=y, s\=5, color\=".15")
sns.histplot(x\=x, y\=y, bins\=50, pthresh\=.1, cmap\="mako")
sns.kdeplot(x\=x, y\=y, levels\=5, color\="w", linewidths\=1)

Copy to clipboard