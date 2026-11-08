[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#sphx-glr-download-auto-examples-applications-plot-species-distribution-modeling-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Species distribution modeling[#](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#species-distribution-modeling "Link to this heading")

==========================================================================================================================================================================================

Modeling species’ geographic distributions is an important problem in conservation biology. In this example, we model the geographic distribution of two South American mammals given past observations and 14 environmental variables. Since we have only positive examples (there are no unsuccessful observations), we cast this problem as a density estimation problem and use the [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 as our modeling tool. The dataset is provided by Phillips et. al. (2006). If available, the example uses [basemap](https://matplotlib.org/basemap/)
 to plot the coast lines and national boundaries of South America.

The two species are:

*   [Bradypus variegatus](http://www.iucnredlist.org/details/3038/0)
    , the brown-throated sloth.
    
*   [Microryzomys minutus](http://www.iucnredlist.org/details/13408/0)
    , also known as the forest small rice rat, a rodent that lives in Peru, Colombia, Ecuador, Peru, and Venezuela.
    

References[#](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#references "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

*   [“Maximum entropy modeling of species geographic distributions”](http://rob.schapire.net/papers/ecolmod.pdf)
     S. J. Phillips, R. P. Anderson, R. E. Schapire - Ecological Modelling, 190:231-259, 2006.
    

![bradypus variegatus, microryzomys minutus](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_001.png)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Modeling distribution of species 'bradypus variegatus'
 - fit OneClassSVM ... done.
 - plot coastlines from coverage
 - predict species distribution

 Area under the ROC curve : 0.868443
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Modeling distribution of species 'microryzomys minutus'
 - fit OneClassSVM ... done.
 - plot coastlines from coverage
 - predict species distribution

 Area under the ROC curve : 0.993919

time elapsed: 6.66s

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt
import numpy as np

from sklearn import metrics, svm
from sklearn.datasets import [fetch\_species\_distributions](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")
from sklearn.utils import [Bunch](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

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

def create\_species\_bunch(species\_name, train, test, coverages, xgrid, ygrid):
    """Create a bunch with information about a particular organism

    This will use the test/train record arrays to extract the
    data specific to the given species name.
    """
    bunch \= [Bunch](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
(name\=" ".join(species\_name.split("\_")\[:2\]))
    species\_name \= species\_name.encode("ascii")
    points \= dict(test\=test, train\=train)

    for label, pts in points.items():
        \# choose points associated with the desired species
        pts \= pts\[pts\["species"\] \== species\_name\]
        bunch\["pts\_%s" % label\] \= pts

        \# determine coverage values for each of the training & testing points
        ix \= [np.searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
(xgrid, pts\["dd long"\])
        iy \= [np.searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
(ygrid, pts\["dd lat"\])
        bunch\["cov\_%s" % label\] \= coverages\[:, \-iy, ix\].T

    return bunch

def plot\_species\_distribution(
    species\=("bradypus\_variegatus\_0", "microryzomys\_minutus\_0"),
):
    """
    Plot the species distribution.
    """
    if len(species) \> 2:
        print(
            "Note: when more than two species are provided,"
            " only the first two will be used"
        )

    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

    \# Load the compressed data
    data \= [fetch\_species\_distributions](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")
()

    \# Set up the data grid
    xgrid, ygrid \= construct\_grids(data)

    \# The grid in x,y coordinates
    X, Y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(xgrid, ygrid\[::\-1\])

    \# create a bunch for each species
    BV\_bunch \= create\_species\_bunch(
        species\[0\], data.train, data.test, data.coverages, xgrid, ygrid
    )
    MM\_bunch \= create\_species\_bunch(
        species\[1\], data.train, data.test, data.coverages, xgrid, ygrid
    )

    \# background points (grid coordinates) for evaluation
    [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(13)
    background\_points \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[\
        [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
(low\=0, high\=data.Ny, size\=10000),\
        [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
(low\=0, high\=data.Nx, size\=10000),\
    \].T

    \# We'll make use of the fact that coverages\[6\] has measurements at all
    \# land points.  This will help us decide between land and water.
    land\_reference \= data.coverages\[6\]

    \# Fit, predict, and plot for each species.
    for i, species in enumerate(\[BV\_bunch, MM\_bunch\]):
        print("\_" \* 80)
        print("Modeling distribution of species '%s'" % species.name)

        \# Standardize features
        mean \= species.cov\_train.mean(axis\=0)
        std \= species.cov\_train.std(axis\=0)
        train\_cover\_std \= (species.cov\_train \- mean) / std

        \# Fit OneClassSVM
        print(" - fit OneClassSVM ... ", end\="")
        clf \= [svm.OneClassSVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
(nu\=0.1, kernel\="rbf", gamma\=0.5)
        clf.fit(train\_cover\_std)
        print("done.")

        \# Plot map of South America
        [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, i + 1)
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

        print(" - predict species distribution")

        \# Predict species distribution using the training data
        Z \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
((data.Ny, data.Nx), dtype\=[np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)

        \# We'll predict only for the land points.
        idx \= (land\_reference \> \-9999).nonzero()
        coverages\_land \= data.coverages\[:, idx\[0\], idx\[1\]\].T

        pred \= clf.decision\_function((coverages\_land \- mean) / std)
        Z \*= pred.min()
        Z\[idx\[0\], idx\[1\]\] \= pred

        levels \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(Z.min(), Z.max(), 25)
        Z\[land\_reference \== \-9999\] \= \-9999

        \# plot contours of the prediction
        [plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(X, Y, Z, levels\=levels, cmap\=plt.cm.Reds)
        [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(format\="%.2f")

        \# scatter training/testing points
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            species.pts\_train\["dd long"\],
            species.pts\_train\["dd lat"\],
            s\=2\*\*2,
            c\="black",
            marker\="^",
            label\="train",
        )
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            species.pts\_test\["dd long"\],
            species.pts\_test\["dd lat"\],
            s\=2\*\*2,
            c\="black",
            marker\="x",
            label\="test",
        )
        [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
        [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(species.name)
        [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("equal")

        \# Compute AUC with regards to background points
        pred\_background \= Z\[background\_points\[0\], background\_points\[1\]\]
        pred\_test \= clf.decision\_function((species.cov\_test \- mean) / std)
        scores \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[pred\_test, pred\_background\]
        y \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[[np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")\
(pred\_test.shape), [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")\
(pred\_background.shape)\]
        fpr, tpr, thresholds \= [metrics.roc\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
(y, scores)
        roc\_auc \= [metrics.auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(fpr, tpr)
        [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(\-35, \-70, "AUC: %.3f" % roc\_auc, ha\="right")
        print("\\n Area under the ROC curve : %f" % roc\_auc)

    print("\\ntime elapsed: %.2fs" % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

plot\_species\_distribution()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 6.859 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_species_distribution_modeling.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_species_distribution_modeling.ipynb)

[`Download Jupyter notebook: plot_species_distribution_modeling.ipynb`](https://scikit-learn.org/stable/_downloads/b5d1ec88ae06ced89813c50d00effe51/plot_species_distribution_modeling.ipynb)

[`Download Python source code: plot_species_distribution_modeling.py`](https://scikit-learn.org/stable/_downloads/69878e8e2864920aa874c5a68cecf1d3/plot_species_distribution_modeling.py)

[`Download zipped: plot_species_distribution_modeling.zip`](https://scikit-learn.org/stable/_downloads/20976afc231c41d12cde1932ddd60594/plot_species_distribution_modeling.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_kde_thumb.png)

[Kernel Density Estimate of Species Distributions](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html)

Kernel Density Estimate of Species Distributions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_thumb.png)

[Test with permutations the significance of a classification score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Test with permutations the significance of a classification score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/69878e8e2864920aa874c5a68cecf1d3/plot_species_distribution_modeling.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b5d1ec88ae06ced89813c50d00effe51/plot_species_distribution_modeling.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/20976afc231c41d12cde1932ddd60594/plot_species_distribution_modeling.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_species_distribution_modeling.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_species_distribution_modeling.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)