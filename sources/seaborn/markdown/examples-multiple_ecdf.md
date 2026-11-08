 

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
    

Facetted ECDF plots[#](https://seaborn.pydata.org/examples/multiple_ecdf.html#facetted-ecdf-plots "Permalink to this heading")

===============================================================================================================================

![../_images/multiple_ecdf.png](https://seaborn.pydata.org/_images/multiple_ecdf.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`blend_palette()`](https://seaborn.pydata.org/generated/seaborn.blend_palette.html#seaborn.blend_palette "seaborn.blend_palette")
, [`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot "seaborn.displot")

import seaborn as sns
sns.set\_theme(style\="ticks")
mpg \= sns.load\_dataset("mpg")

colors \= (250, 70, 50), (350, 70, 50)
cmap \= sns.blend\_palette(colors, input\="husl", as\_cmap\=True)
sns.displot(
    mpg,
    x\="displacement", col\="origin", hue\="model\_year",
    kind\="ecdf", aspect\=.75, linewidth\=2, palette\=cmap,
)

Copy to clipboard