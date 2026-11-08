 

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
    

Linear regression with marginal distributions[#](https://seaborn.pydata.org/examples/regression_marginals.html#linear-regression-with-marginal-distributions "Permalink to this heading")

==========================================================================================================================================================================================

![../_images/regression_marginals.png](https://seaborn.pydata.org/_images/regression_marginals.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`jointplot()`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

import seaborn as sns
sns.set\_theme(style\="darkgrid")

tips \= sns.load\_dataset("tips")
g \= sns.jointplot(x\="total\_bill", y\="tip", data\=tips,
                  kind\="reg", truncate\=False,
                  xlim\=(0, 60), ylim\=(0, 12),
                  color\="m", height\=7)

Copy to clipboard