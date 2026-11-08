 

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
    

Scatterplot with marginal ticks[#](https://seaborn.pydata.org/examples/marginal_ticks.html#scatterplot-with-marginal-ticks "Permalink to this heading")

========================================================================================================================================================

![../_images/marginal_ticks.png](https://seaborn.pydata.org/_images/marginal_ticks.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")

import seaborn as sns
sns.set\_theme(style\="white", color\_codes\=True)
mpg \= sns.load\_dataset("mpg")

\# Use JointGrid directly to draw a custom plot
g \= sns.JointGrid(data\=mpg, x\="mpg", y\="acceleration", space\=0, ratio\=17)
g.plot\_joint(sns.scatterplot, size\=mpg\["horsepower"\], sizes\=(30, 120),
             color\="g", alpha\=.6, legend\=False)
g.plot\_marginals(sns.rugplot, height\=1, color\="g", alpha\=.6)

Copy to clipboard