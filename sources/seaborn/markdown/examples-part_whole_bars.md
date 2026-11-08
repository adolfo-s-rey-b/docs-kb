 

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
    

Horizontal bar plots[#](https://seaborn.pydata.org/examples/part_whole_bars.html#horizontal-bar-plots "Permalink to this heading")

===================================================================================================================================

![../_images/part_whole_bars.png](https://seaborn.pydata.org/_images/part_whole_bars.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`set_color_codes()`](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn.set_color_codes "seaborn.set_color_codes")
, [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")
, [`set_color_codes()`](https://seaborn.pydata.org/generated/seaborn.set_color_codes.html#seaborn.set_color_codes "seaborn.set_color_codes")
, [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import seaborn as sns
import matplotlib.pyplot as plt
sns.set\_theme(style\="whitegrid")

\# Initialize the matplotlib figure
f, ax \= plt.subplots(figsize\=(6, 15))

\# Load the example car crash dataset
crashes \= sns.load\_dataset("car\_crashes").sort\_values("total", ascending\=False)

\# Plot the total crashes
sns.set\_color\_codes("pastel")
sns.barplot(x\="total", y\="abbrev", data\=crashes,
            label\="Total", color\="b")

\# Plot the crashes where alcohol was involved
sns.set\_color\_codes("muted")
sns.barplot(x\="alcohol", y\="abbrev", data\=crashes,
            label\="Alcohol-involved", color\="b")

\# Add a legend and informative axis label
ax.legend(ncol\=2, loc\="lower right", frameon\=True)
ax.set(xlim\=(0, 24), ylabel\="",
       xlabel\="Automobile collisions per billion miles")
sns.despine(left\=True, bottom\=True)

Copy to clipboard