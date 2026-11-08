 

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
    

Timeseries plot with error bands[#](https://seaborn.pydata.org/examples/errorband_lineplots.html#timeseries-plot-with-error-bands "Permalink to this heading")

===============================================================================================================================================================

![../_images/errorband_lineplots.png](https://seaborn.pydata.org/_images/errorband_lineplots.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")

import seaborn as sns
sns.set\_theme(style\="darkgrid")

\# Load an example dataset with long-form data
fmri \= sns.load\_dataset("fmri")

\# Plot the responses for different events and regions
sns.lineplot(x\="timepoint", y\="signal",
             hue\="region", style\="event",
             data\=fmri)

Copy to clipboard