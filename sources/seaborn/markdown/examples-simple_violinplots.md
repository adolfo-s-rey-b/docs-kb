 

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
    

Horizontal, unfilled violinplots[#](https://seaborn.pydata.org/examples/simple_violinplots.html#horizontal-unfilled-violinplots "Permalink to this heading")

=============================================================================================================================================================

![../_images/simple_violinplots.png](https://seaborn.pydata.org/_images/simple_violinplots.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot "seaborn.violinplot")

import seaborn as sns

sns.set\_theme()

seaice \= sns.load\_dataset("seaice")
seaice\["Decade"\] \= seaice\["Date"\].dt.year.round(\-1)
sns.violinplot(seaice, x\="Extent", y\="Decade", orient\="y", fill\=False)

Copy to clipboard