 

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
    

Multiple bivariate KDE plots[#](https://seaborn.pydata.org/examples/multiple_bivariate_kde.html#multiple-bivariate-kde-plots "Permalink to this heading")

==========================================================================================================================================================

![../_images/multiple_bivariate_kde.png](https://seaborn.pydata.org/_images/multiple_bivariate_kde.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn.kdeplot "seaborn.kdeplot")

import seaborn as sns
import matplotlib.pyplot as plt

sns.set\_theme(style\="darkgrid")
iris \= sns.load\_dataset("iris")

\# Set up the figure
f, ax \= plt.subplots(figsize\=(8, 8))
ax.set\_aspect("equal")

\# Draw a contour plot to represent each bivariate density
sns.kdeplot(
    data\=iris.query("species != 'versicolor'"),
    x\="sepal\_width",
    y\="sepal\_length",
    hue\="species",
    thresh\=.1,
)

Copy to clipboard