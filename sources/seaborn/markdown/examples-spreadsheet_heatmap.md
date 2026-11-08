 

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
    

Annotated heatmaps[#](https://seaborn.pydata.org/examples/spreadsheet_heatmap.html#annotated-heatmaps "Permalink to this heading")

===================================================================================================================================

![../_images/spreadsheet_heatmap.png](https://seaborn.pydata.org/_images/spreadsheet_heatmap.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`heatmap()`](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")

import matplotlib.pyplot as plt
import seaborn as sns
sns.set\_theme()

\# Load the example flights dataset and convert to long-form
flights\_long \= sns.load\_dataset("flights")
flights \= (
    flights\_long
    .pivot(index\="month", columns\="year", values\="passengers")
)

\# Draw a heatmap with the numeric values in each cell
f, ax \= plt.subplots(figsize\=(9, 6))
sns.heatmap(flights, annot\=True, fmt\="d", linewidths\=.5, ax\=ax)

Copy to clipboard