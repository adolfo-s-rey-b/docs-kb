[Skip to main content](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#sphx-glr-download-auto-examples-cross-decomposition-plot-compare-cross-decomposition-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Compare cross decomposition methods[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#compare-cross-decomposition-methods "Link to this heading")

===========================================================================================================================================================================================================

Simple usage of various cross decomposition algorithms:

*   PLSCanonical
    
*   PLSRegression, with multivariate response, a.k.a. PLS2
    
*   PLSRegression, with univariate response, a.k.a. PLS1
    
*   CCA
    

Given 2 multivariate covarying two-dimensional datasets, X, and Y, PLS extracts the ‘directions of covariance’, i.e. the components of each datasets that explain the most shared variance between both datasets. This is apparent on the **scatterplot matrix** display: components 1 in dataset X and dataset Y are maximally correlated (points lie around the first diagonal). This is also true for components 2 in both dataset, however, the correlation across datasets for different components is weak: the point cloud is very spherical.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset based latent variables model[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#dataset-based-latent-variables-model "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

rng \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(42)

n \= 500
\# 2 latents vars:
l1 \= rng.normal(size\=n)
l2 \= rng.normal(size\=n)

latents \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[l1, l1, l2, l2\]).T
X \= latents + rng.normal(size\=(n, 4))
Y \= latents + rng.normal(size\=(n, 4))

X\_train, X\_test, Y\_train, Y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, Y, test\_size\=0.5, shuffle\=False)

print("Corr(X)")
print([np.round](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round")
([np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X.T), 2))
print("Corr(Y)")
print([np.round](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round")
([np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(Y.T), 2))

Copy to clipboard

Corr(X)
\[\[ 1.    0.48 -0.01  0.  \]\
 \[ 0.48  1.   -0.01  0.  \]\
 \[-0.01 -0.01  1.    0.49\]\
 \[ 0.    0.    0.49  1.  \]\]
Corr(Y)
\[\[ 1.    0.47  0.03  0.05\]\
 \[ 0.47  1.    0.03 -0.01\]\
 \[ 0.03  0.03  1.    0.5 \]\
 \[ 0.05 -0.01  0.5   1.  \]\]

Copy to clipboard

Canonical (symmetric) PLS[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#canonical-symmetric-pls "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Transform data[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#transform-data "Link to this heading")

from sklearn.cross\_decomposition import [PLSCanonical](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")

plsca \= [PLSCanonical](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
(n\_components\=2)
plsca.fit(X\_train, Y\_train)
X\_train\_r, Y\_train\_r \= plsca.transform(X\_train, Y\_train)
X\_test\_r, Y\_test\_r \= plsca.transform(X\_test, Y\_test)

Copy to clipboard

### Scatter plot of scores[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#scatter-plot-of-scores "Link to this heading")

import matplotlib.pyplot as plt

\# On diagonal plot X vs Y scores on each components
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(12, 8))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(221)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\_r\[:, 0\], Y\_train\_r\[:, 0\], label\="train", marker\="o", s\=25)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_test\_r\[:, 0\], Y\_test\_r\[:, 0\], label\="test", marker\="o", s\=25)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("x scores")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y scores")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Comp. 1: X vs Y (test corr = %.2f)"
    % [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X\_test\_r\[:, 0\], Y\_test\_r\[:, 0\])\[0, 1\]
)
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(224)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\_r\[:, 1\], Y\_train\_r\[:, 1\], label\="train", marker\="o", s\=25)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_test\_r\[:, 1\], Y\_test\_r\[:, 1\], label\="test", marker\="o", s\=25)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("x scores")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y scores")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Comp. 2: X vs Y (test corr = %.2f)"
    % [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X\_test\_r\[:, 1\], Y\_test\_r\[:, 1\])\[0, 1\]
)
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")

\# Off diagonal plot components 1 vs 2 for X and Y
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(222)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\_r\[:, 0\], X\_train\_r\[:, 1\], label\="train", marker\="\*", s\=50)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_test\_r\[:, 0\], X\_test\_r\[:, 1\], label\="test", marker\="\*", s\=50)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X comp. 1")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("X comp. 2")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "X comp. 1 vs X comp. 2 (test corr = %.2f)"
    % [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X\_test\_r\[:, 0\], X\_test\_r\[:, 1\])\[0, 1\]
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(223)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(Y\_train\_r\[:, 0\], Y\_train\_r\[:, 1\], label\="train", marker\="\*", s\=50)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(Y\_test\_r\[:, 0\], Y\_test\_r\[:, 1\], label\="test", marker\="\*", s\=50)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Y comp. 1")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Y comp. 2")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Y comp. 1 vs Y comp. 2 , (test corr = %.2f)"
    % [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(Y\_test\_r\[:, 0\], Y\_test\_r\[:, 1\])\[0, 1\]
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Comp. 1: X vs Y (test corr = 0.61), Comp. 2: X vs Y (test corr = 0.66), X comp. 1 vs X comp. 2 (test corr = 0.06), Y comp. 1 vs Y comp. 2 , (test corr = -0.01)](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_cross_decomposition_001.png)

PLS regression, with multivariate response, a.k.a. PLS2[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#pls-regression-with-multivariate-response-a-k-a-pls2 "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.cross\_decomposition import [PLSRegression](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")

n \= 1000
q \= 3
p \= 10
X \= rng.normal(size\=(n, p))
B \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[1, 2\] + \[0\] \* (p \- 2)\] \* q).T
\# each Yj = 1\*X1 + 2\*X2 + noize
Y \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, B) + rng.normal(size\=(n, q)) + 5

pls2 \= [PLSRegression](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
(n\_components\=3)
pls2.fit(X, Y)
print("True B (such that: Y = XB + Err)")
print(B)
\# compare pls2.coef\_ with B
print("Estimated B")
print([np.round](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round")
(pls2.coef\_, 1))
pls2.predict(X)

Copy to clipboard

True B (such that: Y = XB + Err)
\[\[1 1 1\]\
 \[2 2 2\]\
 \[0 0 0\]\
 \[0 0 0\]\
 \[0 0 0\]\
 \[0 0 0\]\
 \[0 0 0\]\
 \[0 0 0\]\
 \[0 0 0\]\
 \[0 0 0\]\]
Estimated B
\[\[ 1.   2.   0.  -0.   0.   0.   0.   0.   0.  -0. \]\
 \[ 1.   2.   0.  -0.  -0.  -0.  -0.  -0.1 -0.   0. \]\
 \[ 1.   2.   0.  -0.   0.   0.  -0.  -0.   0.   0. \]\]

array(\[\[4.09928294, 4.27252412, 4.116446  \],\
       \[3.22383315, 3.36186659, 3.2829478 \],\
       \[6.40665836, 6.45699286, 6.28414926\],\
       ...,\
       \[1.50716084, 1.50460976, 1.5177967 \],\
       \[6.67188307, 6.51139993, 6.47838503\],\
       \[5.93803911, 5.99272896, 5.91191611\]\], shape=(1000, 3))

Copy to clipboard

PLS regression, with univariate response, a.k.a. PLS1[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#pls-regression-with-univariate-response-a-k-a-pls1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n \= 1000
p \= 10
X \= rng.normal(size\=(n, p))
y \= X\[:, 0\] + 2 \* X\[:, 1\] + rng.normal(size\=n) + 5
pls1 \= [PLSRegression](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
(n\_components\=3)
pls1.fit(X, y)
\# note that the number of components exceeds 1 (the dimension of y)
print("Estimated betas")
print([np.round](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round")
(pls1.coef\_, 1))

Copy to clipboard

Estimated betas
\[\[ 1.   2.  -0.   0.  -0.   0.  -0.1  0.  -0.  -0. \]\]

Copy to clipboard

CCA (PLS mode B with symmetric deflation)[#](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#cca-pls-mode-b-with-symmetric-deflation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.cross\_decomposition import [CCA](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")

cca \= [CCA](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
(n\_components\=2)
cca.fit(X\_train, Y\_train)
X\_train\_r, Y\_train\_r \= cca.transform(X\_train, Y\_train)
X\_test\_r, Y\_test\_r \= cca.transform(X\_test, Y\_test)

Copy to clipboard

**Total running time of the script:** (0 minutes 0.205 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo8.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cross_decomposition/plot_compare_cross_decomposition.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo8.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cross_decomposition/plot_compare_cross_decomposition.ipynb)

[`Download Jupyter notebook: plot_compare_cross_decomposition.ipynb`](https://scikit-learn.org/stable/_downloads/0837676cf643e44f0684e848d0967551/plot_compare_cross_decomposition.ipynb)

[`Download Python source code: plot_compare_cross_decomposition.py`](https://scikit-learn.org/stable/_downloads/4a508ac905c7935181ce08bd00a8cda9/plot_compare_cross_decomposition.py)

[`Download zipped: plot_compare_cross_decomposition.zip`](https://scikit-learn.org/stable/_downloads/6a464fa14bf1d3ca99fc9a199d81a8b3/plot_compare_cross_decomposition.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_thumb.png)

[Multilabel classification](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)

Multilabel classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pcr_vs_pls_thumb.png)

[Principal Component Regression vs Partial Least Squares Regression](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html)

Principal Component Regression vs Partial Least Squares Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_thumb.png)

[Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)

Two-class AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4a508ac905c7935181ce08bd00a8cda9/plot_compare_cross_decomposition.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0837676cf643e44f0684e848d0967551/plot_compare_cross_decomposition.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/6a464fa14bf1d3ca99fc9a199d81a8b3/plot_compare_cross_decomposition.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo8.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cross_decomposition/plot_compare_cross_decomposition.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo8.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cross_decomposition/plot_compare_cross_decomposition.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)