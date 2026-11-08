 

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
    

Faceted logistic regression[#](https://seaborn.pydata.org/examples/logistic_regression.html#faceted-logistic-regression "Permalink to this heading")

=====================================================================================================================================================

![../_images/logistic_regression.png](https://seaborn.pydata.org/_images/logistic_regression.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`lmplot()`](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot "seaborn.lmplot")

import seaborn as sns
sns.set\_theme(style\="darkgrid")

\# Load the example Titanic dataset
df \= sns.load\_dataset("titanic")

\# Make a custom palette with gendered colors
pal \= dict(male\="#6495ED", female\="#F08080")

\# Show the survival probability as a function of age and sex
g \= sns.lmplot(x\="age", y\="survived", col\="sex", hue\="sex", data\=df,
               palette\=pal, y\_jitter\=.02, logistic\=True, truncate\=False)
g.set(xlim\=(0, 80), ylim\=(\-.05, 1.05))

Copy to clipboard