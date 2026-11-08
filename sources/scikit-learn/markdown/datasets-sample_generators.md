[Skip to main content](https://scikit-learn.org/stable/datasets/sample_generators.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/datasets/sample_generators.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/datasets/sample_generators.html)
[1.8.0](https://scikit-learn.org/1.8/datasets/sample_generators.html)
[1.7.2](https://scikit-learn.org/1.7/datasets/sample_generators.html)
[1.6.1](https://scikit-learn.org/1.6/datasets/sample_generators.html)
[1.5.2](https://scikit-learn.org/1.5/datasets/sample_generators.html)
[1.4.2](https://scikit-learn.org/1.4/datasets/sample_generators.html)

Collapse Sidebar Expand Sidebar

9.3. Generated datasets[#](https://scikit-learn.org/stable/datasets/sample_generators.html#generated-datasets "Link to this heading")

======================================================================================================================================

In addition, scikit-learn includes various random sample generators that can be used to build artificial datasets of controlled size and complexity.

9.3.1. Generators for classification and clustering[#](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-classification-and-clustering "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These generators produce a matrix of features and corresponding discrete targets.

### 9.3.1.1. Single label[#](https://scikit-learn.org/stable/datasets/sample_generators.html#single-label "Link to this heading")

[`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
 creates a multiclass dataset by allocating each class to one normally-distributed cluster of points. It provides control over the centers and standard deviations of each cluster. This dataset is used to demonstrate clustering.

import matplotlib.pyplot as plt
from sklearn.datasets import make\_blobs

X, y \= make\_blobs(centers\=3, cluster\_std\=0.5, random\_state\=0)

plt.scatter(X\[:, 0\], X\[:, 1\], c\=y)
plt.title("Three normally-distributed clusters")
plt.show()

Copy to clipboard

[![../_images/sample_generators-1.png](https://scikit-learn.org/stable/_images/sample_generators-1.png)](https://scikit-learn.org/stable/_images/sample_generators-1.png)

[`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
 also creates multiclass datasets but specializes in introducing noise by way of: correlated, redundant and uninformative features; multiple Gaussian clusters per class; and linear transformations of the feature space.

import matplotlib.pyplot as plt
from sklearn.datasets import make\_classification

fig, axs \= plt.subplots(1, 3, figsize\=(12, 4), sharey\=True, sharex\=True)
titles \= \["Two classes,\\none informative feature,\\none cluster per class",\
          "Two classes,\\ntwo informative features,\\ntwo clusters per class",\
          "Three classes,\\ntwo informative features,\\none cluster per class"\]
params \= \[\
    {"n\_informative": 1, "n\_clusters\_per\_class": 1, "n\_classes": 2},\
    {"n\_informative": 2, "n\_clusters\_per\_class": 2, "n\_classes": 2},\
    {"n\_informative": 2, "n\_clusters\_per\_class": 1, "n\_classes": 3}\
\]

for i, param in enumerate(params):
    X, Y \= make\_classification(n\_features\=2, n\_redundant\=0, random\_state\=1, \*\*param)
    axs\[i\].scatter(X\[:, 0\], X\[:, 1\], c\=Y)
    axs\[i\].set\_title(titles\[i\])

plt.tight\_layout()
plt.show()

Copy to clipboard

[![../_images/sample_generators-2.png](https://scikit-learn.org/stable/_images/sample_generators-2.png)](https://scikit-learn.org/stable/_images/sample_generators-2.png)

[`make_gaussian_quantiles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")
 divides a single Gaussian cluster into near-equal-size classes separated by concentric hyperspheres.

import matplotlib.pyplot as plt
from sklearn.datasets import make\_gaussian\_quantiles

X, Y \= make\_gaussian\_quantiles(n\_features\=2, n\_classes\=3, random\_state\=0)
plt.scatter(X\[:, 0\], X\[:, 1\], c\=Y)
plt.title("Gaussian divided into three quantiles")
plt.show()

Copy to clipboard

[![../_images/sample_generators-3.png](https://scikit-learn.org/stable/_images/sample_generators-3.png)](https://scikit-learn.org/stable/_images/sample_generators-3.png)

[`make_hastie_10_2`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "sklearn.datasets.make_hastie_10_2")
 generates a similar binary, 10-dimensional problem.

[`make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
 and [`make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
 generate 2D binary classification datasets that are challenging to certain algorithms (e.g., centroid-based clustering or linear classification), including optional Gaussian noise. They are useful for visualization. [`make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
 produces Gaussian data with a spherical decision boundary for binary classification, while [`make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
 produces two interleaving half-circles.

import matplotlib.pyplot as plt
from sklearn.datasets import make\_circles, make\_moons

fig, (ax1, ax2) \= plt.subplots(nrows\=1, ncols\=2, figsize\=(8, 4))

X, Y \= make\_circles(noise\=0.1, factor\=0.3, random\_state\=0)
ax1.scatter(X\[:, 0\], X\[:, 1\], c\=Y)
ax1.set\_title("make\_circles")

X, Y \= make\_moons(noise\=0.1, random\_state\=0)
ax2.scatter(X\[:, 0\], X\[:, 1\], c\=Y)
ax2.set\_title("make\_moons")

plt.tight\_layout()
plt.show()

Copy to clipboard

[![../_images/sample_generators-4.png](https://scikit-learn.org/stable/_images/sample_generators-4.png)](https://scikit-learn.org/stable/_images/sample_generators-4.png)

### 9.3.1.2. Multilabel[#](https://scikit-learn.org/stable/datasets/sample_generators.html#multilabel "Link to this heading")

[`make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
 generates random samples with multiple labels, reflecting a bag of words drawn from a mixture of topics. The number of topics for each document is drawn from a Poisson distribution, and the topics themselves are drawn from a fixed random distribution. Similarly, the number of words is drawn from Poisson, with words drawn from a multinomial, where each topic defines a probability distribution over words. Simplifications with respect to true bag-of-words mixtures include:

*   Per-topic word distributions are independently drawn, where in reality all would be affected by a sparse base distribution, and would be correlated.
    
*   For a document generated from multiple topics, all topics are weighted equally in generating its bag of words.
    
*   Documents without labels words at random, rather than from a base distribution.
    

[![../_images/sphx_glr_plot_random_multilabel_dataset_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_multilabel_dataset_001.png)](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html)

### 9.3.1.3. Biclustering[#](https://scikit-learn.org/stable/datasets/sample_generators.html#biclustering "Link to this heading")

|     |     |
| --- | --- |
| [`make_biclusters`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters")<br>(shape, n\_clusters, \*\[, ...\]) | Generate a constant block diagonal structure array for biclustering. |
| [`make_checkerboard`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")<br>(shape, n\_clusters, \*\[, ...\]) | Generate an array with block checkerboard structure for biclustering. |

9.3.2. Generators for regression[#](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-regression "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

[`make_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
 produces regression targets as an optionally-sparse random linear combination of random features, with noise. Its informative features may be uncorrelated, or low rank (few features account for most of the variance).

Other regression generators generate functions deterministically from randomized features. [`make_sparse_uncorrelated`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html#sklearn.datasets.make_sparse_uncorrelated "sklearn.datasets.make_sparse_uncorrelated")
 produces a target as a linear combination of four features with fixed coefficients. Others encode explicitly non-linear relations: [`make_friedman1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html#sklearn.datasets.make_friedman1 "sklearn.datasets.make_friedman1")
 is related by polynomial and sine transforms; [`make_friedman2`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html#sklearn.datasets.make_friedman2 "sklearn.datasets.make_friedman2")
 includes feature multiplication and reciprocation; and [`make_friedman3`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman3.html#sklearn.datasets.make_friedman3 "sklearn.datasets.make_friedman3")
 is similar with an arctan transformation on the target.

9.3.3. Generators for manifold learning[#](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-manifold-learning "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`make_s_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "sklearn.datasets.make_s_curve")<br>(\[n\_samples, noise, random\_state\]) | Generate an S curve dataset. |
| [`make_swiss_roll`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")<br>(\[n\_samples, noise, ...\]) | Generate a swiss roll dataset. |

9.3.4. Generators for decomposition[#](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-decomposition "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`make_low_rank_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix")<br>(\[n\_samples, ...\]) | Generate a mostly low rank matrix with bell-shaped singular values. |
| [`make_sparse_coded_signal`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal")<br>(n\_samples, \*, ...) | Generate a signal as a sparse combination of dictionary elements. |
| [`make_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#sklearn.datasets.make_spd_matrix "sklearn.datasets.make_spd_matrix")<br>(n\_dim, \*\[, random\_state\]) | Generate a random symmetric, positive-definite matrix. |
| [`make_sparse_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")<br>(\[n\_dim, alpha, ...\]) | Generate a sparse symmetric definite positive matrix. |

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)