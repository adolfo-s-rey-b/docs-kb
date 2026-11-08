 

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
    

Plotting model residuals[#](https://seaborn.pydata.org/examples/residplot.html#plotting-model-residuals "Permalink to this heading")

=====================================================================================================================================

![../_images/residplot.png](https://seaborn.pydata.org/_images/residplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`residplot()`](https://seaborn.pydata.org/generated/seaborn.residplot.html#seaborn.residplot "seaborn.residplot")

import numpy as np
import seaborn as sns
sns.set\_theme(style\="whitegrid")

\# Make an example dataset with y ~ x
rs \= np.random.RandomState(7)
x \= rs.normal(2, 1, 75)
y \= 2 + 1.5 \* x + rs.normal(0, 2, 75)

\# Plot the residuals after fitting a linear model
sns.residplot(x\=x, y\=y, lowess\=True, color\="g")

Copy to clipboard