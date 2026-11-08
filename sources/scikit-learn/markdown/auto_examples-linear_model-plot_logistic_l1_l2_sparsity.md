[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html#sphx-glr-download-auto-examples-linear-model-plot-logistic-l1-l2-sparsity-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

L1 Penalty and Sparsity in Logistic Regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html#l1-penalty-and-sparsity-in-logistic-regression "Link to this heading")

======================================================================================================================================================================================================================

Comparison of the sparsity (percentage of zero coefficients) of solutions when L1, L2 and Elastic-Net penalty are used for different values of C. We can see that large values of C give more freedom to the model. Conversely, smaller values of C constrain the model more. In the L1 penalty case, this leads to sparser solutions. As expected, the Elastic-Net penalty sparsity is between that of L1 and L2.

We classify 8x8 images of digits into two classes: 0-4 against 5-9. The visualization shows coefficients of the models for varying C.

![L1 penalty, Elastic-Net l1_ratio = 0.5, L2 penalty](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_001.png)

C=1.00
Sparsity with L1 penalty:                4.69%
Sparsity with Elastic-Net penalty:       4.69%
Sparsity with L2 penalty:                4.69%
Score with L1 penalty:                   0.90
Score with Elastic-Net penalty:          0.90
Score with L2 penalty:                   0.90
C=0.10
Sparsity with L1 penalty:                29.69%
Sparsity with Elastic-Net penalty:       14.06%
Sparsity with L2 penalty:                4.69%
Score with L1 penalty:                   0.90
Score with Elastic-Net penalty:          0.90
Score with L2 penalty:                   0.90
C=0.01
Sparsity with L1 penalty:                84.38%
Sparsity with Elastic-Net penalty:       68.75%
Sparsity with L2 penalty:                4.69%
Score with L1 penalty:                   0.86
Score with Elastic-Net penalty:          0.88
Score with L2 penalty:                   0.89

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X, y \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)

X \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
().fit\_transform(X)

\# classify small against large digits
y \= (y \> 4).astype(int)

l1\_ratio \= 0.5  \# L1 weight in the Elastic-Net regularization

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 3)

\# Set regularization parameter
for i, (C, axes\_row) in enumerate(zip((1, 0.1, 0.01), axes)):
    \# Increase tolerance for short training time
    clf\_l1\_LR \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=C, l1\_ratio\=1, tol\=0.01, solver\="saga")
    clf\_l2\_LR \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=C, l1\_ratio\=0, tol\=0.01, solver\="saga")
    clf\_en\_LR \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=C, l1\_ratio\=l1\_ratio, tol\=0.01, solver\="saga")
    clf\_l1\_LR.fit(X, y)
    clf\_l2\_LR.fit(X, y)
    clf\_en\_LR.fit(X, y)

    coef\_l1\_LR \= clf\_l1\_LR.coef\_.ravel()
    coef\_l2\_LR \= clf\_l2\_LR.coef\_.ravel()
    coef\_en\_LR \= clf\_en\_LR.coef\_.ravel()

    \# coef\_l1\_LR contains zeros due to the
    \# L1 sparsity inducing norm

    sparsity\_l1\_LR \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(coef\_l1\_LR \== 0) \* 100
    sparsity\_l2\_LR \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(coef\_l2\_LR \== 0) \* 100
    sparsity\_en\_LR \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(coef\_en\_LR \== 0) \* 100

    print(f"C={C:.2f}")
    print(f"{'Sparsity with L1 penalty:':<40} {sparsity\_l1\_LR:.2f}%")
    print(f"{'Sparsity with Elastic-Net penalty:':<40} {sparsity\_en\_LR:.2f}%")
    print(f"{'Sparsity with L2 penalty:':<40} {sparsity\_l2\_LR:.2f}%")
    print(f"{'Score with L1 penalty:':<40} {clf\_l1\_LR.score(X, y):.2f}")
    print(f"{'Score with Elastic-Net penalty:':<40} {clf\_en\_LR.score(X, y):.2f}")
    print(f"{'Score with L2 penalty:':<40} {clf\_l2\_LR.score(X, y):.2f}")

    if i \== 0:
        axes\_row\[0\].set\_title("L1 penalty")
        axes\_row\[1\].set\_title("Elastic-Net\\nl1\_ratio = %s" % l1\_ratio)
        axes\_row\[2\].set\_title("L2 penalty")

    for ax, coefs in zip(axes\_row, \[coef\_l1\_LR, coef\_en\_LR, coef\_l2\_LR\]):
        ax.imshow(
            np.abs(coefs.reshape(8, 8)),
            interpolation\="nearest",
            cmap\="binary",
            vmax\=1,
            vmin\=0,
        )
        ax.set\_xticks(())
        ax.set\_yticks(())

    axes\_row\[0\].set\_ylabel(f"C = {C}")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.449 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_logistic_l1_l2_sparsity.ipynb)

[`Download Jupyter notebook: plot_logistic_l1_l2_sparsity.ipynb`](https://scikit-learn.org/stable/_downloads/aec731a57fcba7fde8f5e3d94ffc7c69/plot_logistic_l1_l2_sparsity.ipynb)

[`Download Python source code: plot_logistic_l1_l2_sparsity.py`](https://scikit-learn.org/stable/_downloads/fb191883ea7e76c5eb13dad28d2b0a72/plot_logistic_l1_l2_sparsity.py)

[`Download zipped: plot_logistic_l1_l2_sparsity.zip`](https://scikit-learn.org/stable/_downloads/d5dfa4bf7bbcb5bde05d8b9e576a0de1/plot_logistic_l1_l2_sparsity.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_penalties_thumb.png)

[SGD: Penalties](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html)

SGD: Penalties

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/fb191883ea7e76c5eb13dad28d2b0a72/plot_logistic_l1_l2_sparsity.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/aec731a57fcba7fde8f5e3d94ffc7c69/plot_logistic_l1_l2_sparsity.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d5dfa4bf7bbcb5bde05d8b9e576a0de1/plot_logistic_l1_l2_sparsity.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_logistic_l1_l2_sparsity.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)