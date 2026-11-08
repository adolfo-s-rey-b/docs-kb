 

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
    

Color palette choices[#](https://seaborn.pydata.org/examples/palette_choices.html#color-palette-choices "Permalink to this heading")

=====================================================================================================================================

![../_images/palette_choices.png](https://seaborn.pydata.org/_images/palette_choices.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")
, [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")
, [`barplot()`](https://seaborn.pydata.org/generated/seaborn.barplot.html#seaborn.barplot "seaborn.barplot")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set\_theme(style\="white", context\="talk")
rs \= np.random.RandomState(8)

\# Set up the matplotlib figure
f, (ax1, ax2, ax3) \= plt.subplots(3, 1, figsize\=(7, 5), sharex\=True)

\# Generate some sequential data
x \= np.array(list("ABCDEFGHIJ"))
y1 \= np.arange(1, 11)
sns.barplot(x\=x, y\=y1, hue\=x, palette\="rocket", ax\=ax1)
ax1.axhline(0, color\="k", clip\_on\=False)
ax1.set\_ylabel("Sequential")

\# Center the data to make it diverging
y2 \= y1 \- 5.5
sns.barplot(x\=x, y\=y2, hue\=x, palette\="vlag", ax\=ax2)
ax2.axhline(0, color\="k", clip\_on\=False)
ax2.set\_ylabel("Diverging")

\# Randomly reorder the data to make it qualitative
y3 \= rs.choice(y1, len(y1), replace\=False)
sns.barplot(x\=x, y\=y3, hue\=x, palette\="deep", ax\=ax3)
ax3.axhline(0, color\="k", clip\_on\=False)
ax3.set\_ylabel("Qualitative")

\# Finalize the plot
sns.despine(bottom\=True)
plt.setp(f.axes, yticks\=\[\])
plt.tight\_layout(h\_pad\=2)

Copy to clipboard