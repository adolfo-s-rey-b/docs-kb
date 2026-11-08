 

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
    

Lineplot from a wide-form dataset[#](https://seaborn.pydata.org/examples/wide_data_lineplot.html#lineplot-from-a-wide-form-dataset "Permalink to this heading")

================================================================================================================================================================

![../_images/wide_data_lineplot.png](https://seaborn.pydata.org/_images/wide_data_lineplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`lineplot()`](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")

import numpy as np
import pandas as pd
import seaborn as sns
sns.set\_theme(style\="whitegrid")

rs \= np.random.RandomState(365)
values \= rs.randn(365, 4).cumsum(axis\=0)
dates \= pd.date\_range("1 1 2016", periods\=365, freq\="D")
data \= pd.DataFrame(values, dates, columns\=\["A", "B", "C", "D"\])
data \= data.rolling(7).mean()

sns.lineplot(data\=data, palette\="tab10", linewidth\=2.5)

Copy to clipboard