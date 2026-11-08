 

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
    

Anscombe’s quartet[#](https://seaborn.pydata.org/examples/anscombes_quartet.html#anscombe-s-quartet "Permalink to this heading")

=================================================================================================================================

![../_images/anscombes_quartet.png](https://seaborn.pydata.org/_images/anscombes_quartet.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot")

import seaborn as sns
sns.set\_theme(style\="ticks")

\# Load the example dataset for Anscombe's quartet
df \= sns.load\_dataset("anscombe")

\# Show the results of a linear regression within each dataset
sns.lmplot(
    data\=df, x\="x", y\="y", col\="dataset", hue\="dataset",
    col\_wrap\=2, palette\="muted", ci\=None,
    height\=4, scatter\_kws\={"s": 50, "alpha": 1}
)

Copy to clipboard