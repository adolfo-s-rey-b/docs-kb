 

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
    

Stacked histogram on a log scale[#](https://seaborn.pydata.org/examples/histogram_stacked.html#stacked-histogram-on-a-log-scale "Permalink to this heading")

=============================================================================================================================================================

![../_images/histogram_stacked.png](https://seaborn.pydata.org/_images/histogram_stacked.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")
, [`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot "seaborn.histplot")

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set\_theme(style\="ticks")

diamonds \= sns.load\_dataset("diamonds")

f, ax \= plt.subplots(figsize\=(7, 5))
sns.despine(f)

sns.histplot(
    diamonds,
    x\="price", hue\="cut",
    multiple\="stack",
    palette\="light:m\_r",
    edgecolor\=".3",
    linewidth\=.5,
    log\_scale\=True,
)
ax.xaxis.set\_major\_formatter(mpl.ticker.ScalarFormatter())
ax.set\_xticks(\[500, 1000, 2000, 5000, 10000\])

Copy to clipboard