[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_species_distributions.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_species_distributions.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_species_distributions.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_species_distributions.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_species_distributions.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_species_distributions.html)

Collapse Sidebar Expand Sidebar

fetch\_species\_distributions[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#fetch-species-distributions "Link to this heading")

=========================================================================================================================================================================================

sklearn.datasets.fetch\_species\_distributions(_\*_, _data\_home\=None_, _download\_if\_missing\=True_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_species_distributions.py#L130)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "Link to this definition")

Loader for species distribution dataset from Phillips et. al. (2006).

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#species-distribution-dataset)
.

Parameters:

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

coveragesarray, shape = \[14, 1592, 1212\]

These represent the 14 features measured at each point of the map grid. The latitude/longitude values for the grid are discussed below. Missing data is represented by the value -9999.

trainrecord array, shape = (1624,)

The training points for the data. Each point has three fields:

*   train\[‘species’\] is the species name
    
*   train\[‘dd long’\] is the longitude, in degrees
    
*   train\[‘dd lat’\] is the latitude, in degrees
    

testrecord array, shape = (620,)

The test points for the data. Same format as the training data.

Nx, Nyintegers

The number of longitudes (x) and latitudes (y) in the grid

x\_left\_lower\_corner, y\_left\_lower\_cornerfloats

The (x,y) position of the lower-left corner, in degrees

grid\_sizefloat

The spacing between points of the grid, in degrees

Notes

This dataset represents the geographic distribution of species. The dataset is provided by Phillips et. al. (2006).

The two species are:

*   [“Bradypus variegatus”](http://www.iucnredlist.org/details/3038/0)
     , the Brown-throated Sloth.
    
*   [“Microryzomys minutus”](http://www.iucnredlist.org/details/13408/0)
     , also known as the Forest Small Rice Rat, a rodent that lives in Peru, Colombia, Ecuador, Peru, and Venezuela.
    

References

*   [“Maximum entropy modeling of species geographic distributions”](http://rob.schapire.net/papers/ecolmod.pdf)
     S. J. Phillips, R. P. Anderson, R. E. Schapire - Ecological Modelling, 190:231-259, 2006.
    

Examples

\>>> from sklearn.datasets import fetch\_species\_distributions
\>>> species \= fetch\_species\_distributions()
\>>> species.train\[:5\]
array(\[(b'microryzomys\_minutus', -64.7   , -17.85  ),\
       (b'microryzomys\_minutus', -67.8333, -16.3333),\
       (b'microryzomys\_minutus', -67.8833, -16.3   ),\
       (b'microryzomys\_minutus', -67.8   , -16.2667),\
       (b'microryzomys\_minutus', -67.9833, -15.9   )\],
      dtype=\[('species', 'S22'), ('dd long', '<f4'), ('dd lat', '<f4')\])

Copy to clipboard

For a more extended example, see [Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#sphx-glr-auto-examples-applications-plot-species-distribution-modeling-py)

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_thumb.png)

[Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html)

Species distribution modeling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_kde_thumb.png)

[Kernel Density Estimate of Species Distributions](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html)

Kernel Density Estimate of Species Distributions

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)