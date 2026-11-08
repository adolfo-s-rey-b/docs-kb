[Skip to main content](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/feature_selection/plot_f_test_vs_mi.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/feature_selection/plot_f_test_vs_mi.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/feature_selection/plot_f_test_vs_mi.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/feature_selection/plot_f_test_vs_mi.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/feature_selection/plot_f_test_vs_mi.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/feature_selection/plot_f_test_vs_mi.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html#sphx-glr-download-auto-examples-feature-selection-plot-f-test-vs-mi-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of F-test and mutual information[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html#comparison-of-f-test-and-mutual-information "Link to this heading")

==========================================================================================================================================================================================================

This example illustrates the differences between univariate F-test statistics and mutual information.

We consider 3 features x\_1, x\_2, x\_3 distributed uniformly over \[0, 1\], the target depends on them as follows:

y = x\_1 + sin(6 \* pi \* x\_2) + 0.1 \* N(0, 1), that is the third feature is completely irrelevant.

The code below plots the dependency of y against individual x\_i and normalized values of univariate F-tests statistics and mutual information.

As F-test captures only linear dependency, it rates x\_1 as the most discriminative feature. On the other hand, mutual information can capture any kind of dependency between variables and it rates x\_2 as the most discriminative feature, which probably agrees better with our intuitive perception for this example. Both methods correctly mark x\_3 as irrelevant.

![F-test=1.00, MI=0.36, F-test=0.28, MI=1.00, F-test=0.00, MI=0.00](https://scikit-learn.org/stable/_images/sphx_glr_plot_f_test_vs_mi_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.feature\_selection import [f\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
, [mutual\_info\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
X \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(1000, 3)
y \= X\[:, 0\] + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(6 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* X\[:, 1\]) + 0.1 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)

f\_test, \_ \= [f\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
(X, y)
f\_test /= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(f\_test)

mi \= [mutual\_info\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
(X, y)
mi /= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(mi)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(15, 5))
for i in range(3):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 3, i + 1)
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, i\], y, edgecolor\="black", s\=20)
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x\_{}$".format(i + 1), fontsize\=14)
    if i \== 0:
        [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$y$", fontsize\=14)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("F-test={:.2f}, MI={:.2f}".format(f\_test\[i\], mi\[i\]), fontsize\=16)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.254 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_f_test_vs_mi.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_f_test_vs_mi.ipynb)

[`Download Jupyter notebook: plot_f_test_vs_mi.ipynb`](https://scikit-learn.org/stable/_downloads/95e2652922af032381167a5aa13f2b36/plot_f_test_vs_mi.ipynb)

[`Download Python source code: plot_f_test_vs_mi.py`](https://scikit-learn.org/stable/_downloads/b15a0f93878767ffa709315b9ebf8a94/plot_f_test_vs_mi.py)

[`Download zipped: plot_f_test_vs_mi.zip`](https://scikit-learn.org/stable/_downloads/27a581bf95a4c4534db079c70a1a14de/plot_f_test_vs_mi.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_tests_for_classification_thumb.png)

[Test with permutations the significance of a classification score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_permutation_tests_for_classification.html)

Test with permutations the significance of a classification score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adjusted_for_chance_measures_thumb.png)

[Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html)

Adjustment for chance in clustering performance evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)

[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Comparison between grid search and successive halving

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/b15a0f93878767ffa709315b9ebf8a94/plot_f_test_vs_mi.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/95e2652922af032381167a5aa13f2b36/plot_f_test_vs_mi.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/27a581bf95a4c4534db079c70a1a14de/plot_f_test_vs_mi.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_f_test_vs_mi.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_f_test_vs_mi.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)