 

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
    

Trivariate histogram with two categorical variables[#](https://seaborn.pydata.org/examples/three_variable_histogram.html#trivariate-histogram-with-two-categorical-variables "Permalink to this heading")

==========================================================================================================================================================================================================

![../_images/three_variable_histogram.png](https://seaborn.pydata.org/_images/three_variable_histogram.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

import seaborn as sns
sns.set\_theme(style\="dark")

diamonds \= sns.load\_dataset("diamonds")
sns.displot(
    data\=diamonds, x\="price", y\="color", col\="clarity",
    log\_scale\=(True, False), col\_wrap\=4, height\=4, aspect\=.7,
)

Copy to clipboard