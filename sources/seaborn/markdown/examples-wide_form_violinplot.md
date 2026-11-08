 

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
    

Violinplot from a wide-form dataset[#](https://seaborn.pydata.org/examples/wide_form_violinplot.html#violinplot-from-a-wide-form-dataset "Permalink to this heading")

======================================================================================================================================================================

![../_images/wide_form_violinplot.png](https://seaborn.pydata.org/_images/wide_form_violinplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")
, [`despine()`](https://seaborn.pydata.org/generated/seaborn.despine.html#seaborn.despine "seaborn.despine")

import seaborn as sns
import matplotlib.pyplot as plt
sns.set\_theme(style\="whitegrid")

\# Load the example dataset of brain network correlations
df \= sns.load\_dataset("brain\_networks", header\=\[0, 1, 2\], index\_col\=0)

\# Pull out a specific subset of networks
used\_networks \= \[1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17\]
used\_columns \= (df.columns.get\_level\_values("network")
                          .astype(int)
                          .isin(used\_networks))
df \= df.loc\[:, used\_columns\]

\# Compute the correlation matrix and average over networks
corr\_df \= df.corr().groupby(level\="network").mean()
corr\_df.index \= corr\_df.index.astype(int)
corr\_df \= corr\_df.sort\_index().T

\# Set up the matplotlib figure
f, ax \= plt.subplots(figsize\=(11, 6))

\# Draw a violinplot with a narrower bandwidth than the default
sns.violinplot(data\=corr\_df, bw\_adjust\=.5, cut\=1, linewidth\=1, palette\="Set3")

\# Finalize the figure
ax.set(ylim\=(\-.7, 1.05))
sns.despine(left\=True, bottom\=True)

Copy to clipboard