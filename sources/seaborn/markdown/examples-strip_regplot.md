 

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
    

Regression fit over a strip plot[#](https://seaborn.pydata.org/examples/strip_regplot.html#regression-fit-over-a-strip-plot "Permalink to this heading")

=========================================================================================================================================================

![../_images/strip_regplot.png](https://seaborn.pydata.org/_images/strip_regplot.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot "seaborn.catplot")
, [`regplot()`](https://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot "seaborn.regplot")

import seaborn as sns
sns.set\_theme()

mpg \= sns.load\_dataset("mpg")
sns.catplot(
    data\=mpg, x\="cylinders", y\="acceleration", hue\="weight",
    native\_scale\=True, zorder\=1
)
sns.regplot(
    data\=mpg, x\="cylinders", y\="acceleration",
    scatter\=False, truncate\=False, order\=2, color\=".2",
)

Copy to clipboard