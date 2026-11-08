 

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
    

Joint and marginal histograms[#](https://seaborn.pydata.org/examples/joint_histogram.html#joint-and-marginal-histograms "Permalink to this heading")

=====================================================================================================================================================

![../_images/joint_histogram.png](https://seaborn.pydata.org/_images/joint_histogram.png)

**seaborn components used:** [`set_theme()`](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme "seaborn.set_theme")
, [`load_dataset()`](https://seaborn.pydata.org/generated/seaborn.load_dataset.html#seaborn.load_dataset "seaborn.load_dataset")
, [`JointGrid`](https://seaborn.pydata.org/generated/seaborn.JointGrid.html#seaborn.JointGrid "seaborn.JointGrid")

import seaborn as sns
sns.set\_theme(style\="ticks")

\# Load the planets dataset and initialize the figure
planets \= sns.load\_dataset("planets")
g \= sns.JointGrid(data\=planets, x\="year", y\="distance", marginal\_ticks\=True)

\# Set a log scaling on the y axis
g.ax\_joint.set(yscale\="log")

\# Create an inset legend for the histogram colorbar
cax \= g.figure.add\_axes(\[.15, .55, .02, .2\])

\# Add the joint and marginal histogram plots
g.plot\_joint(
    sns.histplot, discrete\=(True, False),
    cmap\="light:#03012d", pmax\=.8, cbar\=True, cbar\_ax\=cax
)
g.plot\_marginals(sns.histplot, element\="step", color\="#03012d")

Copy to clipboard