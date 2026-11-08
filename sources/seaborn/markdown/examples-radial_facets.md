 

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
    

FacetGrid with custom projection[#](https://seaborn.pydata.org/examples/radial_facets.html#facetgrid-with-custom-projection "Permalink to this heading")

=========================================================================================================================================================

![../_images/radial_facets.png](https://seaborn.pydata.org/_images/radial_facets.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`FacetGrid`](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid "seaborn.FacetGrid")

import numpy as np
import pandas as pd
import seaborn as sns

sns.set\_theme()

\# Generate an example radial datast
r \= np.linspace(0, 10, num\=100)
df \= pd.DataFrame({'r': r, 'slow': r, 'medium': 2 \* r, 'fast': 4 \* r})

\# Convert the dataframe to long-form or "tidy" format
df \= pd.melt(df, id\_vars\=\['r'\], var\_name\='speed', value\_name\='theta')

\# Set up a grid of axes with a polar projection
g \= sns.FacetGrid(df, col\="speed", hue\="speed",
                  subplot\_kws\=dict(projection\='polar'), height\=4.5,
                  sharex\=False, sharey\=False, despine\=False)

\# Draw a scatterplot onto each axes in the grid
g.map(sns.scatterplot, "theta", "r")

Copy to clipboard