[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_species_kde.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_species_kde.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_species_kde.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_species_kde.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_species_kde.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_species_kde.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html#sphx-glr-download-auto-examples-neighbors-plot-species-kde-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Kernel Density Estimate of Species Distributions[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html#kernel-density-estimate-of-species-distributions "Link to this heading")

===========================================================================================================================================================================================================

This shows an example of a neighbors-based query (in particular a kernel density estimate) on geospatial data, using a Ball Tree built upon the Haversine distance metric – i.e. distances over points in latitude/longitude. The dataset is provided by Phillips et. al. (2006) [\[1\]](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html#id2)
. If available, the example uses [basemap](https://matplotlib.org/basemap/)
 to plot the coast lines and national boundaries of South America.

This example does not perform any learning over the data (see [Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#sphx-glr-auto-examples-applications-plot-species-distribution-modeling-py)
 for an example of classification based on the attributes in this dataset). It simply shows the kernel density estimate of observed data points in geospatial coordinates.

The two species are:

*   [“Bradypus variegatus”](https://www.iucnredlist.org/species/3038/47437046)
     , the Brown-throated Sloth.
    
*   [“Microryzomys minutus”](http://www.iucnredlist.org/details/13408/0)
     , also known as the Forest Small Rice Rat, a rodent that lives in Peru, Colombia, Ecuador, Peru, and Venezuela.
    

References[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html#references "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

![Bradypus Variegatus, Microryzomys Minutus](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_kde_001.png)

\- computing KDE in spherical coordinates
- plot coastlines from coverage
- computing KDE in spherical coordinates
- plot coastlines from coverage

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [fetch\_species\_distributions](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")
from sklearn.neighbors import [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")

\# if basemap is available, we'll use it.
\# otherwise, we'll improvise later...
try:
    from mpl\_toolkits.basemap import Basemap

    basemap \= True
except ImportError:
    basemap \= False

def construct\_grids(batch):
    """Construct the map grid from the batch object

    Parameters
    ----------
    batch : Batch object
        The object returned by :func:\`fetch\_species\_distributions\`

    Returns
    -------
    (xgrid, ygrid) : 1-D arrays
        The grid corresponding to the values in batch.coverages
    """
    \# x,y coordinates for corner cells
    xmin \= batch.x\_left\_lower\_corner + batch.grid\_size
    xmax \= xmin + (batch.Nx \* batch.grid\_size)
    ymin \= batch.y\_left\_lower\_corner + batch.grid\_size
    ymax \= ymin + (batch.Ny \* batch.grid\_size)

    \# x coordinates of the grid cells
    xgrid \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(xmin, xmax, batch.grid\_size)
    \# y coordinates of the grid cells
    ygrid \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(ymin, ymax, batch.grid\_size)

    return (xgrid, ygrid)

\# Get matrices/arrays of species IDs and locations
data \= [fetch\_species\_distributions](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")
()
species\_names \= \["Bradypus Variegatus", "Microryzomys Minutus"\]

Xtrain \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[data\["train"\]\["dd lat"\], data\["train"\]\["dd long"\]\]).T
ytrain \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[d.decode("ascii").startswith("micro") for d in data\["train"\]\["species"\]\],
    dtype\="int",
)
Xtrain \*= [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 180.0  \# Convert lat/long to radians

\# Set up the data grid for the contour plot
xgrid, ygrid \= construct\_grids(data)
X, Y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(xgrid\[::5\], ygrid\[::5\]\[::\-1\])
land\_reference \= data.coverages\[6\]\[::5, ::5\]
land\_mask \= (land\_reference \> \-9999).ravel()

xy \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[Y.ravel(), X.ravel()\]).T
xy \= xy\[land\_mask\]
xy \*= [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 180.0

\# Plot map of South America with distributions of each species
fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
fig.subplots\_adjust(left\=0.05, right\=0.95, wspace\=0.05)

for i in range(2):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, i + 1)

    \# construct a kernel density estimate of the distribution
    print(" - computing KDE in spherical coordinates")
    kde \= [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
(
        bandwidth\=0.04, metric\="haversine", kernel\="gaussian", algorithm\="ball\_tree"
    )
    kde.fit(Xtrain\[ytrain \== i\])

    \# evaluate only on the land: -9999 indicates ocean
    Z \= [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(land\_mask.shape\[0\], \-9999, dtype\="int")
    Z\[land\_mask\] \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(kde.score\_samples(xy))
    Z \= Z.reshape(X.shape)

    \# plot contours of the density
    levels \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, Z.max(), 25)
    [plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(X, Y, Z, levels\=levels, cmap\=plt.cm.Reds)

    if basemap:
        print(" - plot coastlines using basemap")
        m \= Basemap(
            projection\="cyl",
            llcrnrlat\=Y.min(),
            urcrnrlat\=Y.max(),
            llcrnrlon\=X.min(),
            urcrnrlon\=X.max(),
            resolution\="c",
        )
        m.drawcoastlines()
        m.drawcountries()
    else:
        print(" - plot coastlines from coverage")
        [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(
            X, Y, land\_reference, levels\=\[\-9998\], colors\="k", linestyles\="solid"
        )
        [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(\[\])
        [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(\[\])

    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(species\_names\[i\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.363 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_species_kde.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_species_kde.ipynb)

[`Download Jupyter notebook: plot_species_kde.ipynb`](https://scikit-learn.org/stable/_downloads/1c4a422dfa5bd721501d19a2b7e2499b/plot_species_kde.ipynb)

[`Download Python source code: plot_species_kde.py`](https://scikit-learn.org/stable/_downloads/02a1306a494b46cc56c930ceec6e8c4a/plot_species_kde.py)

[`Download zipped: plot_species_kde.zip`](https://scikit-learn.org/stable/_downloads/161b401efba4b01936c9871f71688386/plot_species_kde.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_thumb.png)

[Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html)

Species distribution modeling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_thumb.png)

[Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)

Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_pdf_thumb.png)

[Density Estimation for a Gaussian mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html)

Density Estimation for a Gaussian mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/02a1306a494b46cc56c930ceec6e8c4a/plot_species_kde.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1c4a422dfa5bd721501d19a2b7e2499b/plot_species_kde.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/161b401efba4b01936c9871f71688386/plot_species_kde.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_species_kde.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_species_kde.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)