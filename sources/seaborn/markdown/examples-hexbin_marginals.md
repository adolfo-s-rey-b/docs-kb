 

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
    

Hexbin plot with marginal distributions[#](https://seaborn.pydata.org/examples/hexbin_marginals.html#hexbin-plot-with-marginal-distributions "Permalink to this heading")

==========================================================================================================================================================================

![../_images/hexbin_marginals.png](https://seaborn.pydata.org/_images/hexbin_marginals.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`jointplot()`](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot "seaborn.jointplot")

import numpy as np
import seaborn as sns
sns.set\_theme(style\="ticks")

rs \= np.random.RandomState(11)
x \= rs.gamma(2, size\=1000)
y \= \-.5 \* x + rs.normal(size\=1000)

sns.jointplot(x\=x, y\=y, kind\="hex", color\="#4CB391")

Copy to clipboard