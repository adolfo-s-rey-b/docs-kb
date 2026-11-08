 

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
    

Scatterplot heatmap[#](https://seaborn.pydata.org/examples/heat_scatter.html#scatterplot-heatmap "Permalink to this heading")

==============================================================================================================================

![../_images/heat_scatter.png](https://seaborn.pydata.org/_images/heat_scatter.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`relplot()`](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot "seaborn.relplot")

import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Load the brain networks dataset, select subset, and collapse the multi-index
df \= sns.load\_dataset("brain\_networks", header\=\[0, 1, 2\], index\_col\=0)

used\_networks \= \[1, 5, 6, 7, 8, 12, 13, 17\]
used\_columns \= (df.columns
                  .get\_level\_values("network")
                  .astype(int)
                  .isin(used\_networks))
df \= df.loc\[:, used\_columns\]

df.columns \= df.columns.map("-".join)

\# Compute a correlation matrix and convert to long-form
corr\_mat \= df.corr().stack().reset\_index(name\="correlation")

\# Draw each cell as a scatter point with varying size and color
g \= sns.relplot(
    data\=corr\_mat,
    x\="level\_0", y\="level\_1", hue\="correlation", size\="correlation",
    palette\="vlag", hue\_norm\=(\-1, 1), edgecolor\=".7",
    height\=10, sizes\=(50, 250), size\_norm\=(\-.2, .8),
)

\# Tweak the figure to finalize
g.set(xlabel\="", ylabel\="", aspect\="equal")
g.despine(left\=True, bottom\=True)
g.ax.margins(.02)
for label in g.ax.get\_xticklabels():
    label.set\_rotation(90)

Copy to clipboard